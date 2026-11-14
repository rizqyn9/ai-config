# Public skills

Skills I have used from the internet. Browse more: <https://skills.sh> or `bunx skills find <query>`.

Install (per project, never `-g`): `bunx skills add <source> --skill <name> -a claude-code -a kiro-cli`
List a source first: `bunx skills add <source> --list`

★ = read in at least one omp session (264 checked). No ★ means not seen, not useless: slash-command use is not counted.
One line per skill, so `grep -i <word> public.md` finds it. Format: `name | source | tags | what it does`.

## Sources

| source | link | skills |
|---|---|---|
| `mattpocock/skills` | https://github.com/mattpocock/skills | engineering and writing workflow |
| `heygen-com/hyperframes` | https://github.com/heygen-com/hyperframes | HTML to video |
| `stablyai/orca` | https://github.com/stablyai/orca | Orca app |
| `leonxlnx/taste-skill` | https://github.com/leonxlnx/taste-skill | frontend design |
| `anthropics/skills` | https://github.com/anthropics/skills | frontend design |
| `vercel-labs/agent-skills` | https://github.com/vercel-labs/agent-skills | UI review |
| `vercel-labs/skills` | https://github.com/vercel-labs/skills | skills CLI |
| `pbakaus/impeccable` | https://github.com/pbakaus/impeccable | frontend design |
| `nextlevelbuilder/ui-ux-pro-max-skill` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | UI/UX |
| `nutlope/hallmark` | https://github.com/nutlope/hallmark | design |
| `Agents365-ai/drawio-skill` | https://github.com/Agents365-ai/drawio-skill | diagrams |

## Engineering workflow

- `code-review` ★ | mattpocock/skills | review, git | Review changes since a commit, branch or tag against repo standards and spec.
- `codebase-design` ★ | mattpocock/skills | design, modules | Vocabulary for deep modules; improve a module's interface and find deepening chances.
- `diagnosing-bugs` ★ | mattpocock/skills | debug, perf | Diagnosis loop for hard bugs and performance regressions.
- `tdd` ★ | mattpocock/skills | testing | Test-driven development.
- `domain-modeling` | mattpocock/skills | domain, docs | Build and sharpen the domain model, glossary and ADRs.
- `improve-codebase-architecture` | mattpocock/skills | architecture | Scan for deepening opportunities, show an HTML report, grill through the chosen one.
- `prototype` | mattpocock/skills | design | Throwaway prototype to answer a design question.
- `research` | mattpocock/skills | research, docs | Investigate a question with primary sources and save findings as Markdown.
- `retro` | mattpocock/skills | process | Retrospective on a coding session.
- `handoff` | mattpocock/skills | context | Compact the conversation into a handoff doc for another agent.
- `setup-pre-commit` | mattpocock/skills | setup, git | Husky, lint-staged, Prettier, type check and tests as pre-commit hooks.
- `setup-ts-deep-modules` | mattpocock/skills | setup, typescript | dependency-cruiser so each package is a deep module with entry-point files only.
- `setup-matt-pocock-skills` | mattpocock/skills | setup | Configure a repo (issue tracker, triage labels, doc layout) for this skill set. Run once first.
- `ask-matt` | mattpocock/skills | router | Ask which skill or flow fits the situation.

## Planning and issues

- `grill-me` | mattpocock/skills | interview | Relentless interview to sharpen a plan or design.
- `grill-with-docs` | mattpocock/skills | interview, docs | Same, and writes ADRs and glossary as it goes.
- `grilling` | mattpocock/skills | interview | Stress-test a plan, decision or idea.
- `to-spec` | mattpocock/skills | spec, issues | Turn the conversation into a spec on the issue tracker, no interview.
- `to-tickets` | mattpocock/skills | tickets, issues | Break a plan or spec into tracer-bullet tickets with blocking edges.
- `implement-spec` | mattpocock/skills | spec | Implement the result of to-spec and to-tickets.
- `implement` | mattpocock/skills | spec | Implement work from a spec or a set of tickets.
- `triage` | mattpocock/skills | issues | Move issues and external PRs through triage states and write agent-ready briefs.
- `wayfinder` | mattpocock/skills | planning, issues | Plan work bigger than one session as a map of decision tickets.
- `to-questionnaire` | mattpocock/skills | decisions | Turn an undecided question into a questionnaire for someone else.
- `loop-me` | mattpocock/skills | workflow | Grill me about specs for workflows I want to build.
- `teach` | mattpocock/skills | learning | Teach a new skill or concept.
- `wait-what` | mattpocock/skills | communication | Re-pitch the last message when it did not land.

## Writing

- `writing-for-agents` ★ | mattpocock/skills | writing, skills | Write skills, AGENTS.md and CLAUDE.md for agents.
- `writing-fragments` | mattpocock/skills | writing | Explore: mine raw fragments, no structure yet.
- `writing-beats` | mattpocock/skills | writing | Exploit: assemble material into a journey of beats.
- `writing-shape` | mattpocock/skills | writing | Exploit: shape material into an article.

## Frontend and design

- `impeccable` ★ | pbakaus/impeccable | frontend, design | Interface craft and design quality for UI work. Was in Kiro only.
- `frontend-design` ★ | anthropics/skills | frontend, design | Distinctive visual design that does not read as templated.
- `ui-ux-pro-max` ★ | nextlevelbuilder/ui-ux-pro-max-skill | ui, ux, a11y | UI/UX intelligence for web, mobile and desktop: design, review, accessibility.
- `redesign-existing-projects` ★ | leonxlnx/taste-skill | frontend, redesign | Audit an existing site, remove generic AI patterns, raise quality.
- `web-design-guidelines` ★ | vercel-labs/agent-skills | ui, review, a11y | Review UI code against Web Interface Guidelines.
- `design-taste-frontend` | leonxlnx/taste-skill | frontend, design | Anti-slop landing pages and portfolios with a real design system.
- `hallmark` | nutlope/hallmark | design | Was in Kiro only. Not reviewed.
- `shadcn-components` ★, `shadcn-theming` ★, `shadcn-registries` | unknown | frontend, shadcn | Source not in the lock file. Find with `bunx skills find shadcn`.

## Diagrams

- `drawio-skill` | Agents365-ai/drawio-skill | diagrams | Create, edit, lint and export draw.io diagrams (architecture, ERD, UML, C4).
- `excalidraw-diagram` | unknown | diagrams | Was in Kiro only. Find with `bunx skills find excalidraw`.

## Video (HyperFrames)

Start with `hyperframes`; it is the entry point for any video request.

- `hyperframes` ★ | heygen-com/hyperframes | video | Entry point for making, editing or rendering video and motion graphics.
- `hyperframes-core` ★ | heygen-com/hyperframes | video | Composition contract: structure, timing attributes, tracks, sub-compositions.
- `hyperframes-animation` | heygen-com/hyperframes | video, motion | Motion rules, scene transitions and runtime adapters (GSAP and others).
- `hyperframes-keyframes` | heygen-com/hyperframes | video, motion | Zooms, punch-ins, camera moves, 2D/3D keyframes.
- `hyperframes-creative` | heygen-com/hyperframes | video, design | Design spec, palettes, typography, narration, beat planning.
- `hyperframes-audio` | heygen-com/hyperframes | video, audio | Mix audio: fades, gain, ducking, music under voiceover.
- `hyperframes-registry` | heygen-com/hyperframes | video | Search and install registry blocks before hand-building a visual.
- `hyperframes-cli` | heygen-com/hyperframes | video, cli | CLI loop: init, add, lint, preview, render, publish.
- `hyperframes-studio` | heygen-com/hyperframes | video | Work with a person on a project in Studio.
- `media-use` | heygen-com/hyperframes | video, assets | Resolve music, SFX, images, icons, voice into local files with a ledger.
- `product-launch-video` ★ | heygen-com/hyperframes | video, marketing | Turn a URL, script or brief into a product launch video.

## Orca and tooling

- `orca-cli` ★ | stablyai/orca | orca, cli | Operate Orca worktrees, terminals, repos and the embedded browser.
- `orchestration` | stablyai/orca | orca, agents | Run work in separate Orca worker agents and collect results.
- `computer-use` | stablyai/orca | orca, gui | Drive a local app window: accessibility tree, clicks, typing, screenshots.
- `find-skills` | vercel-labs/skills | skills | Discover and install skills when asked "is there a skill for X".
- `wizard` ★ | mattpocock/skills | scripting | Generate an interactive bash wizard for steps only a human can do.

## Not public

- `ui-components`: private skill from the erp repo.
