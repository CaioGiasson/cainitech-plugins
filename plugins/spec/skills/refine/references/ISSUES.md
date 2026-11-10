# Creating the tasks on the board — `/spec:refine`

Read by `/spec:refine` only after the user confirmed a board in Phase 4. Without a board, nothing here applies.

## PHASE 5 — Creating the tasks (only with a board)

Apply `WORKFLOW.md` §6 for GitHub access.

### 5.1 — Main issue (product view)

Create an issue in the main repository chosen by the user in the following format:

**Title:** `[FEATURE] <clear, direct title of the functionality>`
(adjust the prefix by type: `[BUG]`, `[IMPROVEMENT]`, `[TECH-DEBT]`; accept the project's own prefixes if it has them)

**Label:** every issue gets the label for its type. If there is no suitable label, ask the user which one to create, create it and only then associate it.

**Body:**

```markdown
## Objective

<Product-oriented description: what this feature delivers, which problem it solves, the value for the user or business.>

## Context

<Background information relevant to someone reading the task without having taken part in the refinement. Include the origin (link or file name) when it came from an informal conversation, and the path of the refinement document.>

## Business rules

<Numbered list of all rules, validations, permissions and conditional flows.>

## Acceptance criteria

- [ ] <verifiable criterion 1>
- [ ] <verifiable criterion 2>
- [ ] ...

## Main flow

<Step-by-step description of the happy path, from the user's or the system's point of view.>

## Edge cases and error handling

- <edge case 1 and how it must be handled>
- <edge case 2 and how it must be handled>
- ...

## End-to-end acceptance script

<Step by step, from the user's point of view, to validate the complete feature across all repositories, with the expected result at each step.>

## Definitions and glossary

<Domain terms the team needs to know to implement correctly.>

## Sub-issues

> The technical issues per repository will be linked here after creation.
```

---

### 5.2 — Sub-issues per repository

For **each affected repository**, create an issue in the respective repository (`owner/repo-name`) in the following format:

**Title:** `[FEATURE] <feature title> — <repo-name>`

**Body:**

```markdown
## Context

<Why this issue exists. Which larger feature it belongs to. Link to the main issue.>

Main issue: <owner>/<repo>#<number>

## Scope of the changes

<Technical, precise description of what must change in this repository. Modules, endpoints, models, components, message queues, etc.>

## Implementation definitions (step by step)

<A guide detailed enough for a junior developer: for each change, the exact file (path) to create/change, the function/class/route/field involved, expected signatures and types, request/response examples (JSON), error messages and HTTP codes, translation keys, database fields/indexes and reference code snippets ("follow the pattern of `<existing file>`"). Explain the why of non-obvious decisions and the domain terms.>

## Order of commits

> Follow this order. Each commit is independent, describes a single change and leaves the project compiling with green tests. Use the project's commit convention (Conventional Commits prefix by default).

1. `docs: save the refinement of issue #<number> in <docs folder>/specs/` — files: `<docs folder>/specs/<file>.md`
2. `<prefix>: <commit message>` — files: `<list of files to create/change>`; what to do: <objective description>
3. `test: <commit message>` — files: `<test files>`
4. `docs: <commit message>` — API contract, README, context files etc.
5. `chore: bump version to <x.y.z>` — last commit, once per PR (only if the project versions itself)

## Test script

**Automated tests (the developer creates and runs them):**
- [ ] `<test file>` — scenario: <what it validates>, expected result: <result>

**Manual tests (the user runs them after the implementation):**

| # | Precondition | Steps | Expected result |
|---|---|---|---|
| 1 | <initial state, e.g., user logged in, seed data> | <1. open… 2. click… 3. submit…> | <what must happen, including HTTP status/messages> |
| 2 | … | … | … (include at least one error scenario and one edge case) |

## Documentation, context and versioning to update

- [ ] This refinement saved in `<docs folder>/specs/`
- [ ] API contract (OpenAPI, request collections, inventory), when there is a new/changed endpoint and the project keeps one
- [ ] README/docs/ADR/glossary affected: <list>
- [ ] Context files (`CLAUDE.md`, `AGENTS.md`, `CONTEXT.md`) if commands, structure or conventions change: <list or "not applicable">
- [ ] A single version bump in the PR (expected type: patch | minor | major), only if the project versions itself

## Dependencies

<List of dependencies on other repositories or services. E.g., "Depends on <owner>/<repo> exposing endpoint POST /mfa/enable".>

## Edge cases and technical cautions

- <caution 1>
- <caution 2>
- ...

## Technical acceptance criteria

- [ ] <verifiable technical criterion 1>
- [ ] <verifiable technical criterion 2>
- [ ] ...

<!-- Project conventions checklist — derive it from the project's own rules (AGENTS.md, CONTRIBUTING.md, lint and test configuration) and include only the items that apply to this repository. Typical items: -->

**Conventions and quality** *(adapt to the project)*
- [ ] Naming, layering and structure follow the project's conventions
- [ ] Input validated at external boundaries; errors handled with the project's error types
- [ ] No hardcoded configuration or secrets; no sensitive data in logs or responses
- [ ] Tests written for the affected logic, including error paths and authorization rules
- [ ] User-visible text in the project's translation catalogs for all languages, when there is a UI
- [ ] API contract and docs updated, when applicable

---

## 🤖 Prompt for Claude

> Paste this prompt when opening this repository in Claude Code to start the implementation (or run `/spec:build <issue link>`).

---

You are implementing the following task in this repository (`<repo-name>`):

**Feature:** <feature title>
**Issue:** <issue link>

### Before you start

- Read `tasks/lessons.md` if it exists in this repository.
- Read the project's own context and convention files: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, the lint/format/test configuration. The project's rules win over any generic rule.
- Read the refinement document `<path>` (the same content as this issue).

### What to do

<Direct, technical description of the changes needed in this repository, in the imperative. Be specific: probable files, patterns to follow, expected behavior.>

### Rules and constraints

<List the business rules and technical constraints relevant to this repository specifically.>

### Edge cases to handle

<List the edge cases the implementation in this repository must cover.>

### Order of commits

<Repeat here the ordered list from the "Order of commits" section of this issue. The agent must follow it in order.>

### Test script

<Repeat here the test script (automated and manual) of this issue. At the end of the implementation, the agent must present it again to the user.>

### Completion criteria

- [ ] <criterion 1>
- [ ] <criterion 2>

### Additional context

- Stack: <the repository's stack, per its README.md>
- Do not add dependencies without a clear need.
- Create or update tests for whatever is changed.

---
```

---

### 5.3 — Linking to the GitHub Project

Link each created issue (main and sub-issues) to the project of the board chosen in Phase 4:

```bash
gh project item-add <project-number> --owner <owner> --url <issue-url>
```

After linking, set each item's **Status** field to **ToDo** (`gh project field-list` to get the field and option; `gh project item-edit --id <ITEM_ID> --project-id <PROJECT_ID> --field-id <STATUS_FIELD_ID> --single-select-option-id <TODO_OPTION_ID>`; see `WORKFLOW.md` §3.1). If the board has no such option, note it in the summary.

Signal progress:
```
🔗 Linking issues to the project...
   ✔ Main issue linked
   ✔ [repo-name] linked
   ...
```

If linking fails for any issue, list it in the final summary without blocking the others.

---

## PHASE 6 — Update the main issue (only with a board)

Edit the main issue to include the links of the created sub-issues in the `## Sub-issues` section.
