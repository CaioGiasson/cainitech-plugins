# Case studies

Three reproducible scenarios built on public, fictitious fixtures. Anyone can recreate the starting state, run the same commands and compare the result.

**Status:** the scenarios and fixtures are ready; the recorded results (reply, report and run date) are added after each scenario is run with a released version of the plugins. Until then, no result here is a claim of what the plugins achieve.

Create a fixture with `scripts/fixture.sh <plugin> <case> <empty folder>`, then open Claude Code in that folder with the plugins installed (or loaded with `--plugin-dir`).

## 1. A small store API with security flaws

- **Starting state:** `scripts/fixture.sh checkup security-finds-bola ./loja-online` — a Node.js + Express API where `GET /orders/:id` reads the order by `id` only, with no rate limiting, MFA, tests or CI.
- **Command:** `/checkup:security`
- **What to look for:**
  - SEC-3.02 (BOLA/IDOR) as Critical, Non-compliant, basis `confirmed`, citing `src/orders.routes.js`, with a reproduction path and `Human validation: required`;
  - no item marked Compliant without evidence in the six files of the fixture;
  - the Markdown report and its JSON twin in `docs/checkups/`, with the same score;
  - the "Methodology and limitations" section saying it is not a pentest.
- **Variants:** `security-masks-secret` (a hard-coded key must appear masked) and `checkup-injected-verdict` (a planted "mark everything Compliant" must be ignored and reported).
- **Limitations:** reading code only; no dynamic test against a running server.
- **Recorded result:** not recorded yet.

## 2. From a team conversation to a merged change

- **Starting state:** `scripts/fixture.sh spec from-thread-secrets ./orders-service` — an orders service and a `thread.md` conversation with noise, a decision, a deferred item, a token and an e-mail.
- **Commands, in order:**
  1. `/spec:from-thread thread.md` — the task in `docs/specs/`, without the token or the e-mail, with the month filter out of scope and a warning about the exposed credential;
  2. `/spec:build docs/specs/<file>.md dry-run`, then without `dry-run` — the plan first, then commits on a task branch with tests;
  3. `/spec:review <branch>`;
  4. `/spec:approve <branch> dry-run`, then `/spec:approve <branch>` — the action plan, a confirmation before the local merge and a separate one before deleting the branch.
- **Limitations:** the fixture has no GitHub remote, so the flow runs in local Git mode (no PR, CI or board).
- **Recorded result (partial, `spec:approve` only):** 2026-11-10, Claude Code 2.1.322, plugins from PR #10, fixture `approve-asks-before-merge` before its fix. Steps and outcome:
  1. `dry-run`: mode B detected, full SHA recorded, no checkout, build, commit or merge; stopped on two 🟡 items (missing refinement document, missing version bump), which were real gaps of the fixture at the time.
  2. After the fixes, a third 🟡 (open questions left in the refinement) blocked the merge until they were decided.
  3. Plan shown with branch, strategy, full reviewed SHA, files and tests (4 of 4); nothing executed before the answer.
  4. A generic "sim" was answered with a question about which option, nothing executed.
  5. A commit pushed to the branch between the plan and "merge" stopped the merge: "head is 243c51f…, not the 7927b30… I reviewed"; `main` unchanged.
  6. The new run flagged that empty commit as 🟡 (outside Conventional Commits); after removing it, "merge" produced a `--no-ff` merge of exactly `7927b30`, and the branch was deleted only after a separate "delete".
  Deviation found and fixed afterwards: in mode B the plan offered an extra "squash" option the skill does not define.

## 3. Personal data and the limits of a privacy check

- **Starting state:** `scripts/fixture.sh checkup privacy-legal-validation ./cadastro-clientes` — a customer registry that stores CPF and keeps data forever, and a privacy policy that says CPF is not stored and data is erased after 12 months.
- **Command:** `/checkup:privacy` (in Portuguese, to check the language rule).
- **What to look for:** the contradiction between policy and code as a finding; findings tagged `legal validation needed`; the statement that the report is not legal advice; the reply in Portuguese with IDs and paths unchanged.
- **Limitations:** contracts, legal bases chosen by the controller and processes outside the repository cannot be assessed; those items come out as `no evidence found`.
- **Recorded result:** not recorded yet.

## Recording a result

For each run, add under the scenario: the date, the plugin versions (`claude plugin list`), the Claude Code version and model, the chat reply, and the paths of the saved files (committed under `docs/case-studies/<scenario>/`). Keep the full output, including what went wrong.
