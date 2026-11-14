# skills

Private skills. One folder per skill: `skills/<name>/SKILL.md` (frontmatter `name` and `description`).
Start from `_template/`.

Install into a project (never `-g`), from the project root:

    bunx skills add ~/workspace/rdev-space/ai-config --list
    bunx skills add ~/workspace/rdev-space/ai-config --skill <name> -a claude-code -a kiro-cli -a omp

Notes:
- Without `-g` the skill lands in `<project>/.agents/skills` and is recorded in `skills-lock.json`; commit both.
- A local path is copied at install time. Re-run `bunx skills update` after editing a skill here.
- Remote form once this repo is pushed (private works through git/gh/SSH auth): `bunx skills add <owner>/ai-config --skill <name>`.

Public skills I use (source, what they do, install line): see `public.md`. Add a row there when you start using a new one.

Triggering: a description alone loads a skill unreliably (about half the runs for `cloud-network-diagram`; 1 of 12 in the skill-creator trigger test). Where a skill matters, also put one line in the project's AGENTS.md or steering, for example:

    Diagram requests (cloud, network, flow, IP plan, route tables): load the `cloud-network-diagram` skill first.
