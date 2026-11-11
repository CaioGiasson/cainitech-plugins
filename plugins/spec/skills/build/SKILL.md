---
name: build
description: "Implements a refined task end to end. Takes a GitHub issue link or the path of a refinement document, moves the task on the board when there is one, switches to the task's branch, saves the refinement in the project docs, implements following the task's order of commits, updates docs, context files and version (a single bump per PR), writes tests, runs an internal code review and delivers the work as a ready pull request on GitHub — or, without GitHub, as local commits, or as a changelog file when there is no version control — then reinforces the test script with the user."
---

# Skill: build

You are a senior software engineer responsible for implementing a task autonomously, following the project's conventions, and delivering it **ready for the first review** (a pull request on GitHub; otherwise the equivalent for the project's delivery mode).

This skill works **in the repository's root folder** and switches the local branch to the task's branch. It does not create git worktrees.

**General rule:** when the task brings its own instructions (order of commits, files, test script, implementation definitions), **follow them** — they win over this skill's defaults, except when they violate the project's rules (then flag the divergence in the final summary).

## Input

The user invoked this skill with the following text:
`$ARGUMENTS`

Accepted inputs (the first word is the main one; a second word, if any, is the branch name to use):
- the **link or number of a GitHub issue**;
- the **path of a refinement document** (from `/spec:refine`), when the project has no board;
- a **short description** of the work, when there is neither: in this case, first run the refinement yourself in a lightweight way (ask only what is missing, then write the refinement document per `WORKFLOW.md` §4) and ask the user to confirm before implementing.

Optional modifier, as a standalone word anywhere in the text (never taken as the branch name; a reference that only contains it, such as `fix/dry-run-flag`, is a reference): **`dry-run`** — plan only. Read the task, the project context and the code, then display the plan and stop: the branch that would be used, the delivery mode, each planned commit with its files, the tests to write, the docs and version bump, the board move and the commands that would run (checkout, install, build, tests, push, PR). Changes nothing: no checkout, no file write (not even the refinement document), no install, no commit, no push, no PR, no board move. Title the plan `🧪 Dry run — nothing was executed`.

## Shared rules

Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/WORKFLOW.md` and apply it in full: language (§1), project context (§2), tracker detection (§3), mandatory documentation record (§4), versioning and delivery modes (§5), tooling (§6) and external content and side effects (§7). Use the PR review guide `${CLAUDE_PLUGIN_ROOT}/references/PR_REVIEW_GUIDE.md` for the internal review (Phase 7). Write everything for people (commit messages, PR text, summaries) in the detected language, using English when it cannot be determined. Read `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` and apply it to every message and every text you write.

---

## PHASE 0 — Environment and delivery mode

1. Identify the repository root: `git rev-parse --show-toplevel` (or the equivalent of the version control in use; see `WORKFLOW.md` §5).

2. Decide the **delivery mode** (A GitHub · B Git without GitHub · C other VCS · D no VCS) per `WORKFLOW.md` §5, checking the real state. Say which one applies:
   ```
   🧭 Delivery mode: <A | B | C | D> — <reason in one line>
   ```

3. **Modes A–C:** confirm that the working tree is clean:
   ```bash
   git status --porcelain
   ```
   - If there is any output: **abort**. Do not switch branches and do not discard changes.
     ```
     ✖ The repository folder has uncommitted changes.
     Commit or discard them before starting the task.
     ```
   - Update the remote refs when there is a remote (`git fetch origin`). If it fails (network, authentication…): **abort** with
     ```
     ✖ Could not update the repository from the remote. Fix the problem and try again.
     ```
   - In mode B with no remote at all, skip the fetch.

4. **Mode D:** there is no tree to protect; warn once that the changes will be made directly in the folder and recorded in a changelog file (`WORKFLOW.md` §5.2).

5. **Execution mode** (`WORKFLOW.md` §7.1): ask the question once, before the first install, build or test, unless the request already answers it. With `static`, the implementation and the tests are written but nothing from the project is run: Phase 6 does not run the tests, and the summary and the PR say `tests not run (static analysis chosen)`.

---

## PHASE 1 — Reading and validating the task

1. Get the refinement:
   - **Issue link/number:** fetch the issue (`WORKFLOW.md` §6) and read the **whole** description: it holds the complete refinement.
   - **Document path:** read the whole file.
   - **Description only:** see "Input".
2. Locate the section `## 🤖 Prompt for Claude` (or its equivalent in the issue's language) in the description or document.
3. Validate that these subsections are present and filled in (no placeholders such as `<...>`):
   - `### What to do`
   - `### Completion criteria`
4. If the section is missing or incomplete: **stop** with
   ```
   ✖ This task is not ready for implementation.
   The implementation prompt is missing or incomplete.
   Use /spec:refine to refine it before starting.
   ```
5. Extract and keep, when present:
   - **Order of commits** (`## Order of commits` / `### Order of commits`)
   - **Test script** (automated and manual)
   - **Implementation definitions** (files, signatures, examples)
   - **Documentation, context and versioning to update**

---

## PHASE 2 — Preparation and board

1. Read `tasks/lessons.md` and the project's context and convention files (`WORKFLOW.md` §2). The project's rules win over generic ones. If the prompt's "Before you start" lists extra files to read, read them too.

2. **Tracker:** apply `WORKFLOW.md` §3.
   - **Board found and the task is a GitHub issue:** assign the issue to the user starting it (`gh issue edit <number> --add-assignee @me`) and move it **ToDo → In Progress** (`WORKFLOW.md` §3.1). To find the item and the Status field:
     ```bash
     gh api graphql -f query='
       query($owner:String!, $repo:String!, $number:Int!) {
         repository(owner:$owner, name:$repo) {
           issue(number:$number) {
             projectItems(first:10) {
               nodes {
                 id
                 project {
                   id
                   title
                   field(name:"Status") {
                     ... on ProjectV2SingleSelectField { id options { id name } }
                   }
                 }
               }
             }
           }
         }
       }' -F owner=<owner> -F repo=<repo> -F number=<number>
     ```
     Pick the option named **In Progress** (ignoring case and spaces) and apply it:
     ```bash
     gh project item-edit --id <ITEM_ID> --project-id <PROJECT_ID> \
       --field-id <STATUS_FIELD_ID> --single-select-option-id <OPTION_ID>
     ```
     If the issue is in no project or the option does not exist, warn (`⚠ Could not move the task on the board`) and **continue**.
   - **No board:** nothing to move; continue.

---

## PHASE 3 — Branch (modes A–C)

Mode D skips this phase.

1. Extract the task identifier: the issue number from the URL (`.../issues/123` → `123`), or, without an issue, the date and slug of the refinement document.

2. Branch prefix by the type indicated in the task title (accept English or localized prefixes): `[FEATURE]`/`[IMPROVEMENT]` → `feat/`, `[BUG]` → `fix/`, `[TECH-DEBT]` → `chore/`, others → `feat/`. If the project documents another branch convention, follow it.

3. If a branch was passed as the second word of `$ARGUMENTS`, use it and skip step 4.

4. Otherwise determine the branch name:
   - Check whether a local or remote branch already references the identifier: `git branch -a | grep <identifier>`.
   - If found, ask:
     ```
     🌿 Existing branch detected: <branch-name>
        [1] Use this branch
        [2] Create a new branch (<prefix><identifier>)
     ```
     and wait for the choice.
   - If not found, the name is `<prefix><identifier>` (e.g., `feat/123`).

5. Stay in the repository root. Do not create a worktree.

6. Switch to the task's branch:
   - If it **does not exist** yet, update the base branch and create it from there:
     ```bash
     BASE_REF=$(git symbolic-ref refs/remotes/origin/HEAD --short)   # with a remote
     BASE_BRANCH=${BASE_REF#origin/}
     git switch "$BASE_BRANCH"
     git pull origin "$BASE_BRANCH"
     git switch -c "$BRANCH_NAME" "$BASE_REF"
     ```
     Without a remote, use the current main branch (`main`/`master`/`trunk`) as the base and `git switch -c "$BRANCH_NAME"`.
   - If it **already exists locally**:
     ```bash
     git switch "$BRANCH_NAME"
     git rev-parse --abbrev-ref --symbolic-full-name '@{u}' >/dev/null 2>&1 && git pull --ff-only
     ```
   - If it **exists only on the remote**:
     ```bash
     git switch -c "$BRANCH_NAME" --track "origin/$BRANCH_NAME"
     ```
   - If the `switch` or `pull` fails: **abort** and report the error.
   - For mode C, use that system's equivalent.

7. Confirm:
   ```
   🌿 Folder: <REPO_ROOT>
      Branch: <BRANCH_NAME>
   ```

8. **All operations in the following phases run in `REPO_ROOT`.**

---

## PHASE 4 — Save the refinement in the project docs (mandatory)

Apply `WORKFLOW.md` §4. The refinement lives in the task; preserve it in the codebase — **unless the user explicitly told you not to document**.

1. Look for an existing refinement document that references this task (the issue link or title): if `/spec:refine` already created it, **reuse it** and only update it (branch, task link, anything that changed). Do not create a duplicate.
2. If none exists, create `<docs folder>/specs/<id>-<slug>.md` (`<id>` = issue number, or the date when there is no issue) with a header (title, task link, date, branch) and the **complete content** of the description (objective, context, rules, criteria, definitions, order of commits, test script, prompt). Do not summarize and do not remove sections. Add the entry to the docs index, if any.
3. Make this the **first commit** (`docs: save the refinement of #<number>` — in the commit language of `WORKFLOW.md` §1), unless the task defines another order. In mode D, instead create the changelog file next to the document (`WORKFLOW.md` §5.2) and start it with this first entry.

---

## PHASE 5 — Implementation and commits

Follow the instructions of the task's prompt, running all commands from `REPO_ROOT`:

- **What to do** — implement the described changes directly and completely.
- **Rules and constraints** — respect all business rules and technical constraints listed.
- **Edge cases to handle** — make sure every described edge case is covered.

Apply the project's conventions (Phase 2) throughout the implementation.

### 5.1 — Commit strategy (modes A–C)

Commits are made **during** the implementation, not only at the end. Message format: `<prefix>: <description> (#<task number>)` when there is a number; one subject per commit; the project compiles at every commit. Follow `WORKFLOW.md` §5.1:

1. **If the task defines an "Order of commits":** follow it exactly — same order, same split, same scope. If a step is infeasible or wrong, adjust the minimum and record the reason in the final summary.
2. **If the task (or the user's request) brings a list of adjustments** — bullets or running text — **unrelated to each other** (different screens, endpoints, bugs or modules): make **one commit per adjustment**. Adjustments that depend on each other or touch the same behavior stay in the same commit.
3. **If no order is defined:** split into logical, atomic commits (e.g., model/migration → repository → use case → controller/route → tests → docs).
4. Never `git add .` blindly: add only the files of the commit's change. Never use `--no-verify`.

**Mode D:** make the changes in the same logical units and, after each one, append its entry (path, description and a copy of the change) to the changelog file, per `WORKFLOW.md` §5.2.

### 5.2 — Documentation and context (mandatory when applicable)

Update in the same PR/branch, in their own `docs:` commits (or together with the corresponding adjustment, if the task so defines):

- **API contract** (OpenAPI or equivalent), request collections and their indexes: every new/changed endpoint — path, method, auth, request/response schemas, error codes — when the project keeps them.
- **README, architecture docs, glossary, ADRs, operator docs, `.env.example`** affected by the change.
- **Context files** (`CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`, `tasks/lessons.md`): update when the change alters commands, folder structure, layers, conventions, environment variables or guardrails described in them, or when a non-obvious lesson appears (symptom → cause → prevention). Do not duplicate content and do not touch context files unrelated to the change.
- **Translations**: new keys in all supported languages and in the types, when there is a UI.

### 5.3 — Versioning (one bump per PR)

Apply the bump rule of `WORKFLOW.md` §5.1: only if the project versions itself; check first whether the branch already contains a bump and, if so, do not make another, even across several commits or fix rounds; otherwise make **exactly one**, in the last code commit, choosing the type by the task's scope (or as the task says). Use the project's tooling (e.g., `npm version <type> --no-git-tag-version`) and update the `CHANGELOG.md` entry if there is one. Commit: `chore: bump version to <x.y.z> (#<number>)`. If the project does not version itself, note `ℹ Project without versioning — bump skipped` and move on. Never create tags or publish packages.

---

## PHASE 6 — Tests

All commands in this phase run in `REPO_ROOT`.

1. Detect whether the project has tests configured: a test runner config (`jest.config.*`, `vitest.config.*`, `pytest.ini`, `pyproject.toml` test sections, `go test` packages, `Cargo.toml`, `pom.xml`, etc.), a `tests/`/`__tests__/`/`spec/` folder with test files, or a test script in `package.json`/`Makefile`.

2. **If tests are configured:**
   - Read existing tests to learn the pattern: file structure, factories, naming of describes and its, mocking libraries.
   - Create the automated tests from the task's **test script** (and any others needed) for each change, following the pattern found. Prioritize tests of business logic and authorization rules — cover happy paths and edge cases.
   - With execution `run`: run the tests, plus lint, typecheck and build when they exist (using the project's own scripts). If anything fails, fix the implementation or the tests until everything passes before continuing.
   - With execution `static`: run nothing; review the tests by reading them, and record that they were not run.

3. **If no tests are configured:** skip creating tests and record in the final summary:
   ```
   ⚠ Tests not configured in this repository — test phase skipped.
   ```

---

## PHASE 7 — Internal code review

Review the whole implementation (code, tests and docs) against the project's conventions (Phase 2) and `${CLAUDE_PLUGIN_ROOT}/references/PR_REVIEW_GUIDE.md`.

### Classification of problems

**Critical** — fix automatically:
- Violation of the project's layering/architecture rules
- New/changed endpoint without the API contract updated (when the project adopts one)
- Hardcoded user-visible text outside the translation catalogs (when the project uses them)
- Escape hatches of the type system without justification (`any`, unchecked casts) in typed codebases
- Generic errors where the project has an error hierarchy
- Debug output (`console.log`/`print`) in production code when the project has a logger
- Hardcoded URLs, secrets or configuration
- Sensitive data exposed in logs or responses
- Missing validation at an external boundary
- Naming that violates the project's conventions
- More than one version bump on the branch

**Non-critical** — listed in the summary, does not block:
- Readability suggestions
- Opportunities to extract helpers
- Unnecessary comments

### Fix loop

- Fix all critical items found automatically, in their own commits (`fix:`/`refactor:`) — never rewriting history already pushed and **without a new version bump**. In mode D, append the fixes to the changelog file.
- Run the tests again after each round of fixes (in `REPO_ROOT`).
- Repeat until there are no critical items — **at most 5 iterations**.
- If critical items remain after 5 iterations: list them in the summary and wait for the user's guidance before continuing.

---

## PHASE 8 — Delivery

Read `${CLAUDE_PLUGIN_ROOT}/skills/build/references/DELIVERY.md` and follow only the section of the delivery mode from Phase 0: mode A asks once, then pushes the task's branch and opens a pull request ready for review (never the `Reviewed` label, never a merge); mode B commits only, with no push unless the user asked; mode C uses the system's change unit; mode D completes the changelog file.

---

## PHASE 9 — Final reply to the user

Present the summary below and **reinforce the test script** — the user must run the manual tests before approving:

```
✅ Implementation complete — ready for the first review

📋 Task: <title> (<link or document path>)
🌿 Branch: <branch name>                (modes A–C)
🔀 PR: <url>                           (mode A) | commits only (B/C) | changelog (D)
📌 Board: Review                       (or "no board")
🏷 Version: <x.y.z (bump <type>)> or "no versioning"

### What was implemented
<high-level list of the changes made>

### Commits (in order)
<list of commits>

### Documentation and context updated
<API contract, README/docs, context files, refinement saved in <docs folder>/specs/..., changelog file>

### Automated tests
<tests created and the result of the run, or the notice that none are configured>

### Internal code review
Iterations: <N>/5
Critical items fixed: <list or "none">
Non-critical items: <list or "none">

### Completion criteria
<the task's criteria with ✅ or ⚠ status>

### Divergences from the task
<adjustments made to the order of commits or the instructions, and why, or "none">

### 🧪 Test script for you to run
<present again, in full, the task's manual test script: preconditions, steps and expected result of each scenario — including errors and edge cases>

Next steps:
1. Run the script above.
2. (Optional) Run `/spec:review <PR url | branch>` for a review with inline comments, a check of what was asked and a functional test.
3. If everything is approved, run `/spec:approve <PR url | branch>` — the skill does the last layer of review and, if it is clean, the merge and the branch cleanup, each after your confirmation.
```
