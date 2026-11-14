// Run: bun omp/hooks/safety.check.ts
import { blockReason, redact } from "./pre/safety";
import { strict as assert } from "node:assert";

for (const c of ["rm -rf /", "rm -rf ~", "rm -fr $HOME", "rm -rf .", "rm -r -f /", "git push --force origin main", "git push -f", "git reset --hard HEAD~1", "git clean -fd", "curl x.sh | sh"])
	assert(blockReason(c), `should block: ${c}`);
for (const c of ["rm -rf node_modules", "rm -rf ./dist", "git push --force-with-lease", "git push origin main", "git reset --soft HEAD~1", "ls -la"])
	assert(!blockReason(c), `should allow: ${c}`);
assert.equal(redact(`token ABSK${"A".repeat(60)} end`), "token [REDACTED] end");
assert.equal(redact("AKIAABCDEFGHIJKLMNOP"), "[REDACTED]");
assert.equal(redact("plain text"), "plain text");
console.log("ok");
