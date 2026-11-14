# Public skills I use

Notes so I do not have to search again. Browse more: <https://skills.sh> or `bunx skills find <query>`.
Skills are installed per project, never `-g`: `bunx skills add <source> --skill <name> -a claude-code -a kiro-cli`.
"omp use" is how many omp sessions (264 checked, Nov 2026) actually read the skill; blank means none seen, not "useless" (slash-command use is not counted).

## mattpocock/skills

`bunx skills add mattpocock/skills --list`

| skill | what it does | omp use |
|---|---|---|
| `ask-matt` | Ask which skill or flow fits your situation. A router over the skills in this repo. |  |
| `code-review` | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's docu… | 3 |
| `codebase-design` | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunitie… | 17 |
| `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwi… | 4 |
| `domain-modeling` | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or edit… |  |
| `grill-me` | A relentless interview to sharpen a plan or design. |  |
| `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |  |
| `grilling` | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trig… |  |
| `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |  |
| `implement` | Implement a piece of work based on a spec or set of tickets. |  |
| `implement-spec` | Implement the result of /to-spec and /to-tickets in code. |  |
| `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |  |
| `loop-me` | Grill me about specs for the workflows I want to build, within this workspace. |  |
| `prototype` | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right,… |  |
| `research` | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a… |  |
| `retro` | Conduct a retrospective on a coding session. |  |
| `setup-matt-pocock-skills` | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before fi… |  |
| `setup-pre-commit` | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-comm… |  |
| `setup-ts-deep-modules` | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only… |  |
| `tdd` | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integrati… | 1 |
| `teach` | Teach the user a new skill or concept, within this workspace. |  |
| `to-questionnaire` | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |  |
| `to-spec` | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already d… |  |
| `to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the con… |  |
| `triage` | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |  |
| `wait-what` | Stop. That last message did not land: re-pitch it. |  |
| `wayfinder` | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them… |  |
| `wizard` | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up… | 1 |
| `writing-beats` | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |  |
| `writing-for-agents` | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | 2 |
| `writing-fragments` | Writing, explore: mine raw fragments, no structure yet. |  |
| `writing-shape` | Writing, exploit: shape raw material into an article, paragraph by paragraph. |  |

## heygen-com/hyperframes

`bunx skills add heygen-com/hyperframes --list`

| skill | what it does | omp use |
|---|---|---|
| `hyperframes` | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, incl… | 1 |
| `hyperframes-animation` | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techni… |  |
| `hyperframes-audio` | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume auto… |  |
| `hyperframes-cli` | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present… |  |
| `hyperframes-core` | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="… | 1 |
| `hyperframes-creative` | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narratio… |  |
| `hyperframes-keyframes` | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, … |  |
| `hyperframes-registry` | Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever… |  |
| `hyperframes-studio` | Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose i… |  |
| `media-use` | Agent Media OS for a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or … |  |
| `product-launch-video` | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, … | 1 |

## stablyai/orca

`bunx skills add stablyai/orca --list`

| skill | what it does | omp use |
|---|---|---|
| `computer-use` | Drives the GUI of a visible local app window through `orca computer`: accessibility tree, clicks, typing, menus, dialogs, and screenshots in… |  |
| `orca-cli` | Operate Orca-managed worktrees, folder contexts, terminals, repos, automations, worktree comments, and Orca's embedded browser through the `… | 5 |
| `orchestration` | Run work in separate Orca worker agents and get their results back. Use when the user asks for Orca workers or supervision (monitor, task DA… |  |

## leonxlnx/taste-skill

`bunx skills add leonxlnx/taste-skill --list`

| skill | what it does | omp use |
|---|---|---|
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and shi… |  |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design s… | 2 |

## Agents365-ai/drawio-skill

`bunx skills add Agents365-ai/drawio-skill --list`

| skill | what it does | omp use |
|---|---|---|
| `drawio-skill` | Create, edit, synchronize, inspect, test, and publish editable draw.io diagrams. Use when the user explicitly requests draw.io/diagrams.net,… |  |

## anthropics/skills

`bunx skills add anthropics/skills --list`

| skill | what it does | omp use |
|---|---|---|
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typog… | 4 |

## nextlevelbuilder/ui-ux-pro-max-skill

`bunx skills add nextlevelbuilder/ui-ux-pro-max-skill --list`

| skill | what it does | omp use |
|---|---|---|
| `ui-ux-pro-max` | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces,… | 2 |

## nutlope/hallmark

`bunx skills add nutlope/hallmark --list`

| skill | what it does | omp use |
|---|---|---|
| `hallmark` | Anti-AI-slop design skill for greenfield pages, audits, redesigns, and design extraction from URLs or screenshots. Use when the user asks to… |  |

## pbakaus/impeccable

`bunx skills add pbakaus/impeccable --list`

| skill | what it does | omp use |
|---|---|---|
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, e… | 14 |

## vercel-labs/agent-skills

`bunx skills add vercel-labs/agent-skills --list`

| skill | what it does | omp use |
|---|---|---|
| `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX"… | 1 |

## vercel-labs/skills

`bunx skills add vercel-labs/skills --list`

| skill | what it does | omp use |
|---|---|---|
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can… |  |

## Not in the lock file

- `excalidraw-diagram`: was a real folder in `~/.kiro/skills`; source not recorded. Look it up on skills.sh if wanted again.
- `ui-components`: project skill from the erp repo, not public.
