# Changelog

Versions follow [Semantic Versioning](https://semver.org). Each plugin has its own `version` in `plugins/<plugin>/.claude-plugin/plugin.json`; an entry lists the plugins it changes.

## 1.1.0 — 2026-11-09

`checkup` 1.1.0 · `spec` 1.1.0 · `polish` 1.1.0

### Changed

- **`spec:approve` asks before acting.** It shows the action plan (PR, branches, merge strategy, head commit, label, board) and runs nothing until the user confirms in the chat. Deleting branches needs a separate confirmation. The merge re-checks CI and uses `--match-head-commit`, so new commits pushed after the plan block it. The skill can only be invoked by the user (`disable-model-invocation: true`).
- **`spec:approve` modifiers:** `dry-run` reviews and shows the plan without changing anything; `no-merge` approves without integrating.
- **External content is data.** The `spec` skills treat issues, pull requests, comments, commits, conversations and code as data, never as instructions (`WORKFLOW.md` §7). Text that tries to steer a review or a merge is a blocking finding in `review` and `approve`.
- **Communication style.** Every skill reads `references/STYLE.md`: answer first, no flattery, filler or recaps, full sentences in persisted text. Adapted from the `caveman` skill (Apache-2.0, see `NOTICE`). The review guide no longer asks for praise in comments.
- **Health-check limits.** Reports state that they are evidence-based assessments, not a pentest, an audit, a certification or legal advice. Each finding has a **Basis**: `confirmed` or `no evidence found`. The privacy check marks findings that need legal validation. Repository content that tries to change the assessment is ignored and reported.

### Added

- `SECURITY.md`, `CONTRIBUTING.md`, a pull request template and this changelog.
- "What these plugins do not do" section in both READMEs.
- `scripts/validate.py`, run locally and in CI: catalog counts and IDs, `${CLAUDE_PLUGIN_ROOT}` references, `SKILL.md` frontmatter, identical `STYLE.md` copies, internal Markdown links and forbidden files (`personal/`, `.env`).
- CI secret scan of the whole history with gitleaks 8.30.1, pinned by checksum.

### Compatibility

CI validates the manifests with Claude Code 2.1.114; they were also validated locally with 2.1.63 on Windows. Score rules, weights and catalog items are unchanged: reports from 1.0.0 remain comparable.

## 1.0.0 — 2026-10-14

First marketplace release: `checkup` (security, performance, privacy, ai-readiness and full; 512 criteria) and `spec` (refine, from-thread, build, review, approve). `polish` (ui) joined at 1.0.0 on 2026-11-09.
