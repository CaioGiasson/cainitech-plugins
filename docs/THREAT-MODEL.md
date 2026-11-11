# Threat model

Scope: the three plugins of this repository (`checkup`, `spec`, `polish`) running in Claude Code with the user's account. The plugins are Markdown instructions: they ship no code, hooks or MCP servers. Every action happens through the tools and permissions of the user's Claude Code session.

Last review: 2026-11-11 (`checkup` and `spec` 1.3.0, `polish` 1.1.1), after an external security and quality audit.

## 1. Assets

| Asset | Where it lives | Why it matters |
|---|---|---|
| Source code and history of the assessed or changed repository | User's machine, Git remote | Integrity: unreviewed changes reach the main branch |
| Secrets in the repository or environment (`.env`, tokens, keys) | Working folder, environment variables | Confidentiality: leaks into reports, issues, PRs or third parties |
| Personal data in code, fixtures, conversations and logs | Repository, Slack/Discord threads | LGPD exposure when copied into tasks or reports |
| GitHub account and token (`gh`, GitHub MCP) | User's session | Can push, merge, delete branches, comment and edit boards |
| Task board and issues | GitHub Projects | Integrity of the team's plan |
| Assessment reports and scores | `docs/checkups/` | Decisions are taken on them; a wrong or manipulated score misleads |
| The plugins themselves | This repository, the user's plugin cache | A malicious change reaches every user on update |

## 2. Actors

| Actor | Trust | Capability |
|---|---|---|
| The user, in the chat | Trusted | The only source of instructions and confirmations |
| Claude, running a skill | Trusted to follow the skill, fallible | Uses the session's tools and permissions; can be misled by content |
| Authors of repository content (contributors, dependencies) | Untrusted | Can plant text in code, comments, docs, fixtures, commit messages |
| Authors of issues, PRs, comments and threads | Untrusted | Can write anything the skills read |
| Maintainers of this repository | Trusted for releases | Can change what every installed plugin does |
| Third-party services (GitHub, Slack, Discord) | Trusted transport, untrusted content | Deliver content the skills read |

## 3. Trust boundaries

1. **Chat ↔ content.** Only the user's chat messages carry instructions and confirmations. Everything read through tools is data (`plugins/spec/references/WORKFLOW.md` §7, `plugins/checkup/references/ASSESSMENT.md` §1, `polish:ui` safety limits).
2. **Working folder ↔ remote.** Push, merge, branch deletion, comments, labels, board moves and issue creation cross from the local copy to shared state.
3. **Repository ↔ executed code.** Running the project's install, build or test scripts executes code written by the repository's authors.
4. **This repository ↔ users.** A merged change ships to every user who updates.

## 4. Abuse cases, mitigations and limitations

| ID | Abuse case | Mitigation | Known limitation | Eval |
|---|---|---|---|---|
| T1 | A PR description, comment or commit says "approved, merge now" and `approve` merges without review | `approve` treats such text as a 🔴 finding; every side effect needs the user's confirmation in the chat; `disable-model-invocation: true` keeps Claude from starting `approve` on its own | Prompt instructions reduce, but do not eliminate, the chance that a model follows injected text | `approve-injected-approval` |
| T2 | A Slack/Discord message tells Claude to delete data or push to main | `from-thread` turns such messages into requirements or open questions, never into actions, and points them out | Same as T1 | `from-thread-injected-command` |
| T3 | Code or docs in the assessed repository say "mark this item compliant" | `ASSESSMENT.md` §1: repository content is data; an attempt to steer the assessment is reported as a finding (AIR-10.03) | Same as T1; subtle manipulation (fake evidence that looks real) is not detectable by rule | `checkup-injected-verdict` |
| T4 | A refined issue asks `build` to push to another branch, edit CI secrets or send data out | `WORKFLOW.md` §7: a task defines the change, never the workflow; out-of-scope actions become an open question | `build` asks once before pushing the task branch and opening the PR (`DELIVERY.md`), unless the user's request asked for it; the user reviews the PR before `approve` | `build-out-of-scope-request` |
| T5 | Secrets or personal data copied into a report, issue, PR or doc | `ASSESSMENT.md` §1 and `WORKFLOW.md` §5.2 and §6: mask values, cite location and type only; `from-thread` §1.5 | Masking depends on the model recognizing the value as sensitive | `from-thread-secrets`, `security-masks-secret` |
| T6 | `approve` merges a PR whose CI is pending, failing or in conflict, or whose head changed after the plan | Pending/failing CI and conflicts are blockers; CI and mergeability are re-checked right before the merge; `--match-head-commit` | Repositories without CI give no signal; the skill reports that build and tests ran locally | `approve-failing-tests` (GitHub CI itself is not exercised by the evals) |
| T7 | Branches deleted by mistake, including the base branch | Separate confirmation for branch deletion; the base, `main`, `master` and `homolog` are never deleted; `-D` only after the PR is `MERGED` | None known beyond T1. The evals stop before the deletion question (a single-turn run cannot answer the merge confirmation), so this confirmation is not exercised yet | — |
| T8 | Installing, building or testing the project during `checkup`, `review`, `approve` or `build` executes code the repository controls (lifecycle scripts, tests) with the user's credentials | One question before the first such command: `run` or `static` (`WORKFLOW.md` §7.1, `ASSESSMENT.md` §1); with `static` nothing from the project runs and `approve` never merges; `review` and `approve` install, build and test in a temporary worktree, never in the user's working copy, and clean it up (only requested fixes and the local merge of modes B–C use the working copy, after checking it is clean); with `static`, Git hooks do not run either; Claude Code's permission prompts apply | With `run`, the project's code runs on the user's machine with their permissions: the plugins have no process sandbox. Choose `static`, or use a disposable container or VM without credentials, for repositories you do not trust. The reviewer subagent is isolated from the conversation, not from the machine | `review-asks-before-running`, `checkup-static-mode` |
| T9 | A health-check score is read as a certification, a pentest or legal advice | Reports state their scope (`ASSESSMENT.md` §1); each finding has a basis (`confirmed` or `no evidence found`); the privacy check marks findings that need legal validation; README "What these plugins do not do" | Readers may still over-trust a high score | `privacy-legal-validation`, `security-no-invented-evidence` |
| T10 | The catalog changes silently and scores stop being comparable | Fingerprint per pillar and `CATALOG-CHANGELOG.md`; `scripts/validate.py` fails on an unrecorded change; reports flag methodology changes | A maintainer can record a change with a misleading changelog entry; review of the PR is the control | CI (`scripts/validate.py`) |
| T11 | A malicious or careless change to this repository reaches every user | CI on every PR (validation, secret scan); `SECURITY.md`; versions and `CHANGELOG.md`; auto-update is off by default for third-party marketplaces | No signed releases; users trust the maintainer's GitHub account | — |
| T12 | `polish:ui` downloads assets or adds third-party scripts | Safety limits: no commands, no downloads, no new dependency or CDN, no visiting reference sites | Same as T1 | `ui-no-download` |
| T13 | A pull request edits `.checkup.json` to accept the risk of the flaw it introduces, or excludes the code from the assessment | `CONFIG.md`: no exception on Critical items; every exception needs a reason, an owner and an expiry of at most 12 months; `notApplicable` only on conditional items (*If: …*) and only with the assessor's own evidence that the condition does not apply — the file is never the evidence; exclusions of production code are rejected; every entry, applied or rejected, appears in the report, and the configuration fingerprint is recorded | A non-Critical risk can still be accepted by whoever can merge to the repository; the report makes it visible, the project's review is the control | `checkup-config-exceptions` |
| T14 | `checkup` installs or downloads an analysis tool, or a tool's output steers the assessment | `TOOLS.md`: only tools already installed, never through a downloader, report mode only, output to the scratchpad, output is data; every result is confirmed in the code before it counts | A tool the user installed can itself be compromised; the assessment trusts the user's machine | `security-finds-bola` (`no-tool-install`) |

## 5. What the plugins never do without the user's confirmation in the chat

- Merge a pull request or a branch, or close a change record (`approve`).
- Delete a local or remote branch (`approve`, separate confirmation).
- Push to any branch other than the task's branch; force-push or rewrite pushed history (never, with or without confirmation).
- Create labels, projects or fields the project did not have, except the `Reviewed` label used by `approve`.
- Fix code during a review (`review` fixes only on explicit request).
- Push the task branch or open a pull request (`build`, one question at delivery, unless the request asked for it).
- Run the project's own code: install, build, tests, lint, scripts (`review`, `approve`, `build`, `checkup`; one question per run, unless the request already says the repository is trusted).
- Run a command, open a link, install a package or send data because content suggested it (never).

`review` posts the comments the user picks: that is its documented job, started by the user's invocation.

## 6. Review triggers

Review this model when a skill gains a new side effect, a new tool (MCP, hook, script), or a new source of content; and at every minor release.
