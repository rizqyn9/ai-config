// Safety net for approvalMode: yolo. Blocks a few destructive bash commands and redacts secrets from tool output.
// ponytail: regex heuristics, not a shell parser; upgrade path is a real command tokenizer.
import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

const DANGEROUS: [RegExp, string][] = [
	[/\brm\s+(-\w*[rR]\w*\s+-\w*f|-\w*f\w*\s+-\w*[rR]|-\w*[rR]\w*f\w*|-\w*f\w*[rR]\w*)\s+(--\s+)?(\/|~|\$HOME|\.)(\s|\/?$|\/\*)/, "rm -rf on /, ~, $HOME or ."],
	[/\bgit\s+push\b.*(--force\b(?!-with-lease)|\s-f\b)/, "git push --force (use --force-with-lease)"],
	[/\bgit\s+reset\s+--hard\b/, "git reset --hard"],
	[/\bgit\s+clean\s+-\w*f/, "git clean -f"],
	[/\bcurl\b[^|]*\|\s*(sudo\s+)?(ba|z)?sh\b/, "curl | sh"],
];

const SECRETS: RegExp[] = [
	/\bABSK[A-Za-z0-9+/=]{40,}/g, // Bedrock long-term API key
	/\bAKIA[A-Z0-9]{16}\b/g, // AWS access key id
	/\bghp_[A-Za-z0-9]{36}\b/g, // GitHub PAT
	/\bsk-[A-Za-z0-9_-]{20,}/g, // OpenAI/Anthropic style
];

export const blockReason = (cmd: string) => DANGEROUS.find(([re]) => re.test(cmd))?.[1];
export const redact = (text: string) => SECRETS.reduce((t, re) => t.replace(re, "[REDACTED]"), text);

export default function safety(pi: ExtensionAPI): void {
	pi.on("tool_call", async event => {
		if (event.toolName !== "bash") return;
		const why = blockReason(String(event.input.command ?? ""));
		if (why) return { block: true, reason: `Blocked by safety hook: ${why}. Ask the user to run it themselves.` };
	});

	pi.on("tool_result", async event => {
		if (event.isError) return;
		let changed = false;
		const content = event.content.map(chunk => {
			if (chunk.type !== "text") return chunk;
			const text = redact(chunk.text);
			if (text !== chunk.text) changed = true;
			return { ...chunk, text };
		});
		if (changed) return { content };
	});
}
