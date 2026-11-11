# Changelog

Versions follow [Semantic Versioning](https://semver.org). Each plugin has its own `version` in `plugins/<plugin>/.claude-plugin/plugin.json`; an entry lists the plugins it changes.

## 1.3.0 — 2026-11-11

`checkup` 1.3.0 · `spec` 1.3.0 · `polish` 1.1.1

Answers an external security and quality audit (findings F-01 to F-12).

### Changed

- **One question before running the project's code** (`spec` `WORKFLOW.md` §7.1, `checkup` `ASSESSMENT.md` §1). Installing, building and testing run code the repository controls, with the user's credentials. `review`, `approve`, `build` and the `checkup` pillars ask once per run: `run` (the repository is trusted) or `static` (run nothing from the project). The question is skipped when the request already says the repository is trusted. With `static`, every check that needed a command says it was not run; `approve` never merges; the external scanners of `checkup` still run.
- **`spec:review` and `spec:approve` work in a temporary worktree** and remove it at the end, also when they stop early. The user's working copy is no longer switched, restored or touched. The reviewer is described as isolated from the conversation, not from the machine.
- **`spec:build` asks before pushing and opening the pull request**, once, at delivery, unless the request asked for it.
- **`checkup:full` runs Security before the other pillars**: `PRIV-12.01` uses the Security result.
- **Exception dates checked by command** (`CONFIG.md` §2): calendar date, after today, at most 12 months ahead; `config.schema.json` accepts only real month and day numbers.
- **Eval suites are no longer committed** inside the plugins: `scripts/generate_evals.py` writes them on demand and `scripts/validate.py` checks them in memory and fails if they are committed. Installing a plugin no longer copies 190 test files with planted instructions and fake secrets. This is the only change in `polish` 1.1.1.
- `docs/COMPATIBILITY.md` separates "manifest accepted", "skill run" and "end to end" per surface and system.

### Added

- Evals `review-asks-before-running` and `checkup-static-mode` (threat model T8); prompts of the cases that run project code state that the repository is trusted. 43 cases.
- `scripts/validate.py`: rejects JSON Schema keywords outside the subset it implements, tests that its schema validator rejects a broken report, checks that the marketplace lists exactly the plugin folders with matching names and that each plugin's version appears in this changelog, and that exception dates exist.
- CI installs Claude Code from `.github/tools/package-lock.json` (`npm ci`, integrity hashes) and also runs on pushes to `main`.
- `docs/EVALS.md`: rules for reproducible runs (pinned models, kept traces, three runs of the abuse cases, commit and version per row).

### Not changed, on purpose

- No process sandbox: a plugin of instructions cannot provide one. `static` mode and a disposable container or VM are the documented answers for untrusted repositories (threat model T8).
- No SAST/SCA in this repository's CI: it has no dependencies to scan. No evals in CI: they need an API key in GitHub.

## 1.2.0 — 2026-11-10

`checkup` 1.2.0 · `spec` 1.2.0 · `polish` 1.1.0 (unchanged)

### Added

- **`checkup` runs the analysis tools already installed** (`semgrep`, `trivy`, `osv-scanner`, `npm audit` and the other package audits, `gitleaks`, `trufflehog`, the project's lint) in report mode, confirms each result in the code and uses it as evidence (`references/TOOLS.md`). It never installs a tool or runs one through a downloader. Every report lists the tools with their result, and the JSON twin has `tools`.
- **Repository exceptions in `.checkup.json`** (`references/CONFIG.md`, `references/config.schema.json`): accepted risks, items that do not apply and paths out of scope, each with a reason, an owner and an expiry of at most 12 months. No exception on a Critical item; `notApplicable` only on a conditional item and with the assessor's own evidence, never the file's word; only generated, vendored or test-only paths can be excluded, and secret scanners ignore exclusions. The file never changes severities, weights, the formula or the classification, and every entry, applied or rejected, appears in a new Exceptions section and in the JSON `config`. Changes it causes between runs have the delta cause `config change`. Example in `docs/examples/checkup.config.example.json`, checked by `scripts/validate.py`.
- Threat model T13 (`.checkup.json` used to hide a flaw) and T14 (tool installation or tool output steering the assessment), with evals.

### Changed

- **Skills in layers.** `SKILL.md` files keep the dispatch and the steps that always run; the rest is read when the skill reaches it: `spec:review` keeps its review rules in `references/REVIEWER.md`, read only by the isolated reviewer, and posting and fixes in `POSTING.md` and `FIXES.md`; `spec:refine` reads the issue templates only when there is a board; `spec:build` reads the delivery of its mode and `spec:approve` the integration plan of its mode; the code examples of the review guide moved to `PR_REVIEW_EXAMPLES.md`. In the session that runs `/spec:review`, the skill and the files it reads drop from about 58 KB to about 20 KB; the review rules load in the reviewer's own context.
- **Report JSON schema 1.1.0:** adds `tools`, `config`, the item `exception` and the delta cause `config change`. Reports in schema 1.0.0 remain valid.
- The marketplace manifest has `metadata.description` (asked for by `claude plugin validate --strict` and understood by older Claude Code versions).

### Compatibility

Score rules, weights and catalog items are unchanged: reports from 1.0.0 and 1.1.0 remain comparable. A run with `.checkup.json` can differ from one without it through the N/A items and the excluded paths it applies (accepted risks keep their points); the report lists every entry, and the delta marks those changes as `config change`.

## 1.1.0 — 2026-11-09

`checkup` 1.1.0 · `spec` 1.1.0 · `polish` 1.1.0

### Changed

- **`spec:approve` asks before acting.** It shows the action plan (PR, branches, merge strategy, head commit, label, board) and runs nothing until the user confirms in the chat. Deleting branches needs a separate confirmation. It records the full SHA of the reviewed commit right after checkout; before the first action and again before the merge it re-checks the head, CI and mergeability, and stops if the head moved (new commits were not reviewed). The merge uses `--match-head-commit` with that SHA. When the plan offers more than one option, a generic "yes" is answered with a question. The skill can only be invoked by the user (`disable-model-invocation: true`).
- **`spec:approve` modifiers:** `dry-run` reviews and shows the plan without changing anything; `no-merge` approves without integrating.
- **`spec:review` runs in an isolated subagent.** The session resolves only the reference to review and starts a fresh subagent that receives that reference and nothing from the conversation, so the implementation and the discussion around it cannot bias the review. The subagent refuses to review when there is no linked task (with a board), no task, refinement document or PR description with verifiable acceptance criteria (without one), or no readable diff; a missing task is no longer a finding inside a review that goes on.
- **`dry-run` in `spec:build` and `spec:review`:** `build` shows the branch, commits, files, tests and commands it would run; `review` reviews from the diff without checkout, build or posting.
- **External content is data.** The `spec` skills treat issues, pull requests, comments, commits, conversations and code as data, never as instructions (`WORKFLOW.md` §7). Text that tries to steer a review or a merge is a blocking finding in `review` and `approve`.
- **Communication style.** Every skill reads `references/STYLE.md`: answer first, no flattery, filler or recaps, full sentences in persisted text. Adapted from the `caveman` skill (Apache-2.0, see `NOTICE`). The review guide no longer asks for praise in comments.
- **Health-check limits.** Reports state that they are evidence-based assessments, not a pentest, an audit, a certification or legal advice. Each finding has a **Basis**: `confirmed` or `no evidence found`. The privacy check marks findings that need legal validation. Findings also carry **Confidence** and **Human validation**, and Critical findings a **Reproduction** path. Repository content that tries to change the assessment is ignored and reported.

### Added

- **`polish` plugin** (skill `ui`), first release.
- `SECURITY.md`, `CONTRIBUTING.md`, a pull request template and this changelog.
- **Eval suites** for the 11 skills (40 cases, at least 3 per skill) in `plugins/<plugin>/evals/`, in the `claude plugin eval` format, with fixtures created by scaffold scripts. `scripts/generate_evals.py` is their single source; CI checks that the committed suites match it. They cover triggering, safety rules, dry runs and the abuse cases of the threat model. See `docs/EVALS.md`.
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

First marketplace release: `checkup` (security, performance, privacy, ai-readiness and full; 512 criteria) and `spec` (refine, from-thread, build, review, approve).
