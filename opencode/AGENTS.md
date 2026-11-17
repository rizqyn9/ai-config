# Working rules

## Never claim it works without running it
- Run the command or test. Paste the real output.
- Could not run it? Say what you skipped and why. "Should work" is not a result.

## Before editing
- Read the file. Find how the surrounding code already does it, then match that.
- Smallest diff that solves the problem. No new dependency if the stdlib or an
  installed package covers it.
- No scaffolding for later: no TODO stubs, no unused interfaces, no config for a
  value that never changes.
- Do not rewrite unrelated code, reformat whole files, or delete unfamiliar work
  you did not write. Investigate first; ask if unclear.

## Irreversible actions
- Never `git commit`, `git push`, `git reset --hard`, force-push, rewrite
  history, or delete branches unless asked in this turn.
- Never delete files you did not create without asking.

## Finding things
- `grep`/`glob` first, then `read` only the line ranges you need.
- Wide searches and reviews: delegate to the `scout` and `reviewer` subagents
  instead of reading everything into this context.
- Give paths plus line numbers, not pasted file dumps.
- Verify third-party API shapes against the docs or the installed package, never
  from memory.

## Answers
- Reply in the language the user writes in.
- Lead with the finding or the change; skip narrating the process.
- State assumptions out loud when the request is ambiguous, then proceed.