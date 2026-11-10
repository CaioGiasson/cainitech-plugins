# Changelog

Versions follow [Semantic Versioning](https://semver.org). Each plugin has its own `version` in `plugins/<plugin>/.claude-plugin/plugin.json`; an entry lists the plugins it changes.

## 1.1.0 — 2026-11-09

`checkup` 1.1.0 · `spec` 1.1.0 · `polish` 1.1.0

### Changed

- **`spec:approve` asks before acting.** It shows the action plan (PR, branches, merge strategy, head commit, label, board) and runs nothing until the user confirms in the chat. Deleting branches needs a separate confirmation. It records the full SHA of the reviewed commit right after checkout; before the first action and again before the merge it re-checks the head, CI and mergeability, and stops if the head moved (new commits were not reviewed). The merge uses `--match-head-commit` with that SHA. When the plan offers more than one option, a generic "yes" is answered with a question. The skill can only be invoked by the user (`disable-model-invocation: true`).
- **`spec:approve` modifiers:** `dry-run` reviews and shows the plan without changing anything; `no-merge` approves without integrating.
- **`dry-run` in `spec:build` and `spec:review`:** `build` shows the branch, commits, files, tests and commands it would run; `review` reviews from the diff without checkout, build or posting.
- **External content is data.** The `spec` skills treat issues, pull requests, comments, commits, conversations and code as data, never as instructions (`WORKFLOW.md` §7). Text that tries to steer a review or a merge is a blocking finding in `review` and `approve`.
- **Communication style.** Every skill reads `references/STYLE.md`: answer first, no flattery, filler or recaps, full sentences in persisted text. Adapted from the `caveman` skill (Apache-2.0, see `NOTICE`). The review guide no longer asks for praise in comments.
- **Health-check limits.** Reports state that they are evidence-based assessments, not a pentest, an audit, a certification or legal advice. Each finding has a **Basis**: `confirmed` or `no evidence found`. The privacy check marks findings that need legal validation. Findings also carry **Confidence** and **Human validation**, and Critical findings a **Reproduction** path. Repository content that tries to change the assessment is ignored and reported.

### Added

- `SECURITY.md`, `CONTRIBUTING.md`, a pull request template and this changelog.
- **Eval suites** for the 11 skills (39 cases, at least 3 per skill) in `plugins/<plugin>/evals/`, in the `claude plugin eval` format, with fixtures created by scaffold scripts. `scripts/generate_evals.py` is their single source; CI checks that the committed suites match it. They cover triggering, safety rules, dry runs and the abuse cases of the threat model. See `docs/EVALS.md`.
- `docs/CASE-STUDIES.md`: three reproducible scenarios on public fixtures (security flaws, conversation to merge, privacy limits), and `scripts/fixture.sh` to create the fixture of any eval case. Results are added once recorded with a released version.
- `docs/THREAT-MODEL.md`: assets, actors, trust boundaries, twelve abuse cases with mitigations and known limitations, and the actions that always need confirmation.
- "What these plugins do not do", "Trust and quality" (what each plugin can change, evals, CI, threat model), "Compatibility" and "Contributing and roadmap" sections in both READMEs.
- `scripts/validate.py`, run locally and in CI: catalog counts and IDs, `${CLAUDE_PLUGIN_ROOT}` references, `SKILL.md` frontmatter, identical `STYLE.md` copies, internal Markdown links, forbidden files (`personal/`, `.env`) and the score arithmetic of the README example.
- CI secret scan of the whole history with gitleaks 8.30.1, pinned by checksum.
- **Run-to-run delta:** the Evolution section and the JSON `delta` list improved, regressed, added and removed items by ID, each regression with its cause (`evidence changed`, `assessment correction` or `catalog change`).
- **JSON reports:** every checkup report has a JSON twin following `plugins/checkup/references/report.schema.json` (version 1.0.0), for CI, dashboards and run-to-run comparison. `docs/examples/security-report.example.json` is checked against the schema and the scoring rules in CI.
- **Catalog versioning:** `plugins/checkup/references/CATALOG-CHANGELOG.md` records the catalog version and a fingerprint per pillar. `scripts/validate.py` fails when an item changes without a new version, and every report records the catalog version; the Evolution section flags methodology changes between runs.

### Compatibility

See `docs/COMPATIBILITY.md` for the full matrix. `spec` requires Claude Code 2.1.110 or later, the first version the Claude Code changelog shows honoring `disable-model-invocation`. CI validates the manifests with Claude Code 2.1.114; they were also validated locally with 2.1.63 on Windows. Score rules, weights and catalog items are unchanged: reports from 1.0.0 remain comparable.

## 1.0.0 — 2026-10-14

First marketplace release: `checkup` (security, performance, privacy, ai-readiness and full; 512 criteria) and `spec` (refine, from-thread, build, review, approve). `polish` (ui) joined at 1.0.0 on 2026-11-09.
