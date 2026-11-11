---
name: review
description: "Reviews a pull request (or, without GitHub, a branch or a changelog file) in an isolated subagent that receives only the reference to review, never the conversation. Refuses to review when there is no task, refinement document or PR description with verifiable acceptance criteria. Checks out the branch, reads the PR and the linked task, verifies that everything requested was implemented and that divergences were recorded, runs the build and tests, tests the functionality when possible (attaching evidence), analyzes the code against the project's conventions and the review guide, and posts the comments the user picks. It fixes nothing on its own: it asks the user and, only on explicit request, fixes in one commit per fix on the same branch."
---

# Skill: review

This skill dispatches a code review to a context-isolated reviewer (a subagent without this conversation; it runs on the same machine, with the same permissions), relays its result, and then posts the comments and makes the fixes the user picks. The review rules are in files read only when needed: the reviewer's in `references/REVIEWER.md`, posting in `references/POSTING.md`, fixes in `references/FIXES.md` (all under `${CLAUDE_PLUGIN_ROOT}/skills/review/`).

## Input

The user invoked this skill with the following text:
`$ARGUMENTS`

Accepted inputs: a **pull request URL or number** (GitHub), a **branch name** (Git without GitHub), or the **path of a changelog file** (no version control). With no input, review the PR of the current branch (`gh pr view --json url`); if there is none, review the current branch against the base branch.

Optional modifier, as a standalone word anywhere in the text (a reference that only contains it, such as the branch `fix/dry-run-flag`, is a reference): **`dry-run`** — review without touching anything: the reviewer reads the diff instead of checking out the branch and skips install, build, tests and the functional test. Present the result and stop: post nothing and fix nothing.

## Shared rules

Read `${CLAUDE_PLUGIN_ROOT}/references/WORKFLOW.md` (language, delivery modes, tooling, external content) and `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md`, and apply them to every message and every text you write. Write in the language of the user's request (English when it cannot be determined).

## Step 1 — Context-isolated review

The review is done by a subagent that starts with no context from this conversation, so that what was said or done here (the implementation, explanations, opinions about the change) cannot bias it. Everything the reviewer needs must come from the PR, the task and the repository.

1. Resolve only the reference and the modifier: the PR URL or number, the branch or the changelog path from `$ARGUMENTS`; with no input, `gh pr view --json url --jq .url`, otherwise `git branch --show-current`. Do not read the diff, the task or the code.
1b. Decide the execution mode (`WORKFLOW.md` §7.1): `static` with `dry-run`; otherwise ask the §7.1 question, unless the request already answers it. The reviewer cannot ask, so this is the only moment.
2. Start **one new subagent** with the Agent tool (a fresh general-purpose agent; never a fork or any agent that inherits this conversation). Its prompt contains only:
   ```
   You are the reviewer of the /spec:review skill. Read <plugin root>/skills/review/references/REVIEWER.md and follow it for: <reference>
   Modifier: <dry-run | none>
   Execution: <run | static>
   Repository: <absolute path of the repository root>
   Plugin root (for ${CLAUDE_PLUGIN_ROOT}): <absolute path>
   User's language: <language>
   ```
   Nothing else: no summary of the conversation, no description of what was implemented or why, no opinion on the change, no hint of what to look for, even when the user said something about the change in this session.
3. Relay the reviewer's result as it came, in full, including every **How to fix** block: do not add, remove, shorten, reclassify or soften findings, and do not review the change yourself. A refusal is shown to the user as is, and the skill ends.

If the Agent tool is not available, say that the context-isolated review cannot run and stop. Run the review in this session only if the user asks for it explicitly: then read `references/REVIEWER.md` and follow it here, and start the result with `⚠ Review not isolated: run in the same session as the conversation.`

## Step 2 — What to post (mode A)

With `dry-run`, stop after Step 1. Modes B–D have nowhere to post: go to Step 3.

Ask which comments to post:
```
Which comments do you want to post on the PR?
  - Type the indexes separated by commas (e.g., 1,3,4)
  - Type "all" to post all of them
  - Type "blockers" to post only the 🔴
  - Type "none" to finish without posting

The checking table and the functional-test evidence go into the body of the review if any comment is posted.
```
Wait for the user's answer. If they pick any comment, read `${CLAUDE_PLUGIN_ROOT}/skills/review/references/POSTING.md` and post as it says.

## Step 3 — Fixes (only on explicit request)

This skill fixes nothing automatically. If the result has 🔴 or 🟡 items, read `${CLAUDE_PLUGIN_ROOT}/skills/review/references/FIXES.md` and follow it: it asks the user first and changes nothing without an explicit request.

## Step 4 — Finishing

1. The review itself never touches your working copy (it runs in a temporary worktree). Only if Step 3 switched to the change's branch to fix it, restore tracked files changed by build or tests and return to the branch recorded there (modes A–C):
   ```bash
   cd "$REPO_ROOT"
   git restore .
   git switch "$ORIGINAL_BRANCH"
   ```

2. Display the final summary:
   ```
   ✅ Code review complete

   📋 <PR #number | branch>: <title>
   💬 Comments posted: <N>                (mode A)
   🧪 Functional test: <result>
   🔧 Fixes made on request: <N commits | none>
      🔴 Blockers: <N>
      🟡 Important: <N>
      🟢 Suggestions: <N>

   🌿 Folder: <REPO_ROOT>
      Working copy: untouched | branch restored: <ORIGINAL_BRANCH>
   ```
