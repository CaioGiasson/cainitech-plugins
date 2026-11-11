# Fixes on request — `/spec:review`

Read by `/spec:review` only when the reviewer's result has 🔴 or 🟡 items, after the review was posted or the user decided not to post it.

## Fixes

**This skill fixes nothing automatically.** After posting the review, or deciding not to post it:

1. If there are 🔴/🟡 items, **ask the user** whether they want the fixes made:
   ```
   Do you want me to fix any item?
     - Type the indexes (e.g., 1,3) or "blockers" / "important" / "all"
     - Type "no" to finish without fixing
   ```
   Wait for the answer. Without an explicit request, **do not change code, do not commit and do not push**. 🟢 suggestions are fixed only if the user expressly includes them.

2. On explicit request, fix **only the indicated items**, on the **same branch as the change** (without creating a new branch):
   - Before starting, in `REPO_ROOT` (modes A–C): if `git status --porcelain` is not empty, **stop** and ask the user to commit or stash their work first. Then record `ORIGINAL_BRANCH="$(git branch --show-current)"`, switch to the change's branch (`git switch "$PR_BRANCH"`, or `git switch -c "$PR_BRANCH" --track "origin/$PR_BRANCH"`) and `git pull --ff-only` when it tracks a remote.
   - Follow each item's **How to fix**.
   - Make **one commit per fix** (never group distinct items), with `git add <the fix's files>` and a conventional-commit message referencing the item (e.g., `fix: validate the ID number in createPerson (review #2)`). Never use `--no-verify`.
   - Run build, lint and tests after each fix, only with execution `run` (`WORKFLOW.md` §7.1, the mode decided in Step 1); if it fails, fix it before moving on. With `static`, say in the summary that the fixes were not run.
   - **No new version bump** and no history rewriting (`--force`/rebase forbidden).
   - At the end, `git push` on the same branch (mode A; in mode B only if the user asks) and comment on the PR with a summary: item → commit.
   - In mode D, apply the fixes in place and append them to the changelog file.

3. If a fix requires a product decision or widens the scope, **stop and ask** instead of deciding alone.
