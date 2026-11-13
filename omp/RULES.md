# User preferences

- Use bun for installing, running scripts, and executing packages (`bun add`, `bun run`, `bunx`). Never use npm, npx, yarn, or pnpm.
- Write docs, code comments, and commit messages in English. Keep them and replies minimal: no filler, no restating what the code already says.
- Do not create or edit CI pipelines (GitHub Actions, GitLab CI, etc.). Run checks locally.
- In Elysia, never use TypeBox (`t` from `elysia`, `@sinclair/typebox`). Validate params, query, body, and response with Zod v4 via Standard Schema.
