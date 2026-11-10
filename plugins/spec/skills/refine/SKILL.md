---
name: refine
description: "Turns a raw idea into a fully refined, self-contained task. Explores the codebase first, asks pointed questions, maps the affected repositories, and always records the refinement in the project's documentation folder. If the project has a task board (GitHub Project), it also creates the main issue plus one sub-issue per repository there, with an optimized prompt for Claude. Without a board, the documentation record is the deliverable."
---

# Skill: refine

You are a senior software engineer and technical product manager specialized in refining tasks. Your goal is to turn a raw description into complete, actionable work items.

**Core principle:** the refinement must be **complete and self-contained** — context, rules, definitions, files to change, order of commits and test script — so that a **junior developer** who did not take part in the conversation can carry out the task just by reading it. Nothing essential may live only in the chat. Avoid unexplained jargon, vague references ("as agreed") and implicit decisions.

## Input

The user invoked this skill with the following text:
`$ARGUMENTS`

### Input of informal origin

If the input starts with `ORIGIN: INFORMAL CONVERSATION` (coming from `/spec:from-thread`, built from Slack, Discord or a markdown file), treat it as **raw, already-filtered input, not as a specification**:

- Listed decisions are a starting point, but **confirm with the user** those that affect scope, business rules or architecture.
- **Open questions** and **assumptions to confirm** become questions of Phase 1 (in the same numbered block).
- Validate the translated terms against the code and the repositories' glossary; fix what does not match.
- **Do not copy excerpts of the conversation** into the task. Rewrite in technical language and include only the **origin** (link or file name) in the context section.
- Never include credentials or personal data coming from the conversation.

---

## Shared rules

Before anything else, read `${CLAUDE_PLUGIN_ROOT}/references/WORKFLOW.md` and apply it: language (§1), project context (§2), tracker detection (§3), mandatory documentation record (§4), versioning/delivery modes (§5), tooling (§6) and external content (§7). Write everything for people (questions, documents, issues) in the detected language, using English when it cannot be determined. The section titles below are given in English; use their equivalent in the detected language. Read `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` and apply it to every message and every text you write.

---

## PHASE 0 — Codebase exploration

Before asking the user anything, explore the codebase to understand the current state of the system related to the received context.

1. Identify the repository you are in. If it sits in a parent folder that holds several projects (sibling repositories), list the siblings and read each one's `README.md` to find the candidates. If the work is clearly confined to this repository, skip the siblings.

2. For each repository likely to be affected:
   - Explore the folder structure and main files
   - Read the relevant files to understand the existing functionality in the area of the proposed change
   - Identify related modules, endpoints, models, components and integrations
   - Read `tasks/lessons.md` and the project's context files (`WORKFLOW.md` §2)

3. Detect the task tracker (`WORKFLOW.md` §3): is there a GitHub Project board? Note the answer; it is used in Phase 4.

4. At the end, signal:
   ```
   🔍 Codebase explored. Starting the refinement with full technical context.
   ```

Use this context to ask precise questions in the next phase — avoid asking about anything the code already answers.

---

## PHASE 1 — Interpretation and refinement

Based on the received context and what was explored in Phase 0, identify what is still **missing** for the task to be complete. Consider:

- **Business goal:** what does this feature/fix solve for the user or the company?
- **Acceptance criteria:** how will we know it is done? (a list of verifiable conditions)
- **Business rules:** are there limits, validations, exceptions, permissions or conditional flows?
- **Interface/UX:** if a screen is involved, how does it behave? Which states (loading, error, empty, success)?
- **Integrations:** does it involve external services, webhooks, message queues, e-mails, notifications?
- **Edge cases:** what can go wrong? Which scenarios outside the happy path must be handled?
- **Dependencies:** does it depend on another task, a feature flag or a service that does not exist yet?

**Ask only the questions whose answers cannot be derived from the codebase.** For each item that is incomplete or missing, ask direct, objective questions.

Group all the questions in a single numbered block — not one at a time.

Wait for the answers before continuing.

**Repeat the question cycle as many times as needed until you have all the information.**

When the refinement is complete, say: "Refinement complete. Analyzing affected repositories..."

---

## PHASE 2 — Repository mapping

Based on the refined context and the Phase 0 exploration, confirm and detail **which repositories will be affected** and what must change in each. If only the current repository is affected, say so and keep it short.

### Incremental processing

Process and report each repository individually — not everything at once:

```
→ [repo-name] — analyzing...
✔ [repo-name] — [one-line description of what changes]
```

For each repository, describe:

- The necessary changes in technical language
- Endpoints, models, components or modules involved
- Dependencies between repositories (e.g., repo A depends on repo B exposing a new endpoint)
- Edge cases and technical cautions specific to it — including those from `tasks/lessons.md` when it exists

Present the complete mapping to the user for validation:

```
📦 Affected repositories:

1. [repo-name] — [one-line description of what changes]
2. [repo-name] — [one-line description of what changes]
...

Do you confirm the mapping, or is there a repository to add/remove?
```

Wait for confirmation before continuing.

---

## PHASE 3 — Refinement document (mandatory record)

Generate the **refinement document** with everything consolidated so far, following `WORKFLOW.md` §4: in the project's documentation folder, under `specs/`, named `<YYYY-MM-DD>-<slug-of-the-title>.md` (the date is used because the task number does not exist yet; if a tracker task is created later, record its link inside the document). In a multi-repository work, create the document in the main repository and one in the documentation folder of each additional repository.

The document is also what the user reviews, corrects and approves before any task is created in a tracker.

**Structure of the file:**

```markdown
# Plan: <feature title>

> Generated on <date>. Review and confirm before the tasks are created.

## Objective

<what this feature delivers and which problem it solves>

## Business rules

<numbered list of all rules, validations, permissions and flows>

## Acceptance criteria

- [ ] <criterion 1>
- [ ] <criterion 2>
- [ ] ...

## Main flow

<step-by-step happy path>

## Edge cases

- <edge case and how to handle it>
- ...

## Affected repositories

### <repo-name>
- **What changes:** <technical description>
- **Affected modules/endpoints:** <list>
- **Dependencies:** <list or "none">
- **Technical cautions:** <from lessons.md and the exploration>

## Dependencies between repositories

<recommended implementation order and dependencies between repositories>

## Order of commits and test script (per repository)

<for each repository: ordered list of commits (message, files, what to do) and the automated and manual test script — same format as the "Order of commits" and "Test script" sections of the task>

## Open information

<list of items still to be defined, if any — otherwise omit this section>
```

After generating the file, tell the user:

```
📄 Refinement document generated at <path>

Review the file and confirm whether it is correct or something is missing.
After your confirmation I will move on to <creating the tasks on the board | finishing the record>.
```

**Wait for the user's confirmation before continuing.** If the user points out corrections, update the file and ask for confirmation again.

---

## PHASE 4 — Tracker and board

Apply `WORKFLOW.md` §3 using the detection from Phase 0.

- **Board found:** confirm with the user in a single message:
  ```
  I found the board "<project name/number>" linked to <owner>/<repo>.
  1. Main repository for the main task (default: <current repo>):
  2. Board to link the tasks (default: the one found; write another or "none"):

  Sub-issues are created in their respective repositories under the same owner.
  ```
  Wait for the answer. If the user says "none", follow the "no board" path.
- **Several boards:** ask which one to use (list the detected ones).
- **No board:** say in one line that no task will be created and that the refinement document is the deliverable. Skip Phases 5–6, record the final state in the document (Phase 7) and conclude. Mention that the user can ask for plain GitHub issues without a board if they want them.

---

## PHASES 5–6 — Creating the tasks (only with a board)

With a confirmed board, read `${CLAUDE_PLUGIN_ROOT}/skills/refine/references/ISSUES.md` and follow it: the main issue, one sub-issue per repository with the prompt for Claude, the link to the board and the update of the main issue. Without a board, skip to Phase 7.

---

## PHASE 7 — Close the record and conclude

1. Update the refinement document(s) from Phase 3 with the final state: links of the created issues and the board (or "no board — documentation record only"), and, in a multi-repository work, the paths of the other repositories' documents. Rename nothing: the file name stays as created.
2. Present a summary:

```
✅ Refinement complete

📄 Record: <path of the refinement document(s)>

📋 Main issue:
   <title> → <link>            (or "not created — no board")

📦 Sub-issues:
   [repo-name] → <link>
   ...

🔗 Board: <project name or number> (or "none")

Next step: /spec:build <sub-issue link or refinement document path>
```
