# Integration by delivery mode — `/spec:approve`

Read by `/spec:approve` only on Path B (no 🔴 or 🟡), after Phase 5's confirmation rules. Those rules apply to every step below.

### Mode A — GitHub

1. **Action plan.** Collect the facts and display them:
   ```
   📋 Ready to integrate — confirm before anything changes

   🔀 PR #<number>: <title>
   🌿 <PR_BRANCH> → <BASE_BRANCH>
   🔗 Merge strategy: <squash | merge | rebase> (<source of the choice>)
   🧾 Reviewed commit: <REVIEWED_SHA, full>
   🚦 CI: ✅ green · Mergeable: ✅
   📁 Files changed: <N> (<top paths>)
   💬 PR comment: review result (preview below)
   🏷 Label: Reviewed (<exists | will be created>)
   📌 Board: <current status> → Done      (or "no board")

   Actions after your confirmation, in order:
   1. Comment on the PR
   2. Apply the Reviewed label
   3. Merge the PR (branches are kept; deleting them is a separate confirmation)
   4. Move the board item to Done

   Reply "merge" to run 1–4, "approve only" to run 1–2 without merging, or "cancel".
   ```
   With `no-merge`, list only actions 1–2 and offer "approve" or "cancel".

2. **Wait for the answer.** "cancel" or anything other than an explicit yes: stop and display the summary (step 6) with every action marked as skipped.

3. **Execute only what was confirmed**, in order, after the state check (Confirmation rules):
   - **Comment on the PR** with the review result: what was reviewed, build/tests/CI, "no blocking or important items" and the 🟢 suggestions (if any) as an optional follow-up.
   - **`Reviewed` label:** apply it to the PR. If the label does not exist in the repository, create it (`gh label create Reviewed`) and then apply it.
   - **Merge** ("merge" only). Run the state check again (Confirmation rules); if it stops, do not merge. Otherwise:
     ```bash
     gh pr merge <number> --squash --match-head-commit "$REVIEWED_SHA"
     ```
     - Use the strategy shown in the plan: `--squash` unless the repository defines another standard (check the project's rules and the repository's merge settings), in which case `--merge` or `--rebase`.
     - Do not pass `--delete-branch`: branch deletion has its own confirmation (step 5).
     - If the merge fails (branch protection, conflict, pending check): **do not force**; report the reason and stop.
   - **Board** ("merge" only): if the project has a board (`WORKFLOW.md` §3), move the task to **Done** (`WORKFLOW.md` §3.1). If the board does not do it automatically and it cannot be done, say so in the summary.

4. **Update the local base** (only after a successful merge), without switching the user's branch:
   ```bash
   if [ "$(git branch --show-current)" = "$BASE_BRANCH" ] && [ -z "$(git status --porcelain)" ]; then
     git pull --ff-only origin "$BASE_BRANCH"
   else
     git fetch origin "$BASE_BRANCH:$BASE_BRANCH"
   fi
   ```
   If the update fails (local commits on the base, for example), say so and leave it.

5. **Branch cleanup — separate confirmation** (only after a successful merge):
   - Find the base branch (`main`/`master`) and the PR's branch (`PR_BRANCH`). **Never** delete `main`, `master`, `homolog`, the base branch or any branch other than `PR_BRANCH`.
   - Ask:
     ```
     🌿 Delete the branch <PR_BRANCH>?
        local:  <exists | does not exist>
        remote: origin/<PR_BRANCH> <exists | does not exist>
     Reply "delete" to remove both, "local" for the local one only, or "keep".
     ```
   - On "delete" or "local", delete the **local** branch. If it is the branch checked out in the user's working copy (`git branch --show-current`), it cannot be deleted from there: when `git status --porcelain` is empty, say so and switch to the base first (`git switch "$BASE_BRANCH"`); otherwise skip the local deletion and say why. Then `git branch -d "$PR_BRANCH"`. Since a squash does not preserve history, `-d` may fail; in that case, confirm that the PR is `MERGED` (`gh pr view <number> --json state`) and only then use `git branch -D "$PR_BRANCH"`.
   - On "delete", also delete the **remote** branch if it still exists:
     ```bash
     git ls-remote --exit-code --heads origin "$PR_BRANCH" >/dev/null 2>&1 && git push origin --delete "$PR_BRANCH"
     git fetch --prune origin
     ```

6. Display the summary, marking each action as done (✔), skipped (⏭) or failed (✖):
   ```
   ✅ PR approved and merged              (or "✅ PR approved, not merged", or "⏹ Cancelled")

   🔀 PR #<number>: <title>
   🔍 Review: no blocking/important items — <N> 🟢 suggestion(s)
   💬 Comment: ✔/⏭/✖
   🏷 Label Reviewed: ✔/⏭/✖
   🔗 Merge: ✔/⏭/✖ (<sha of the merge commit>)
   📌 Board: Done ✔/⏭/✖                  (or "no board")
   🌿 Branches removed: local ✔/⏭  remote ✔/⏭
   📍 Current branch: <branch>
   ```

### Mode B/C — Git without GitHub, or another VCS

1. **Action plan.** Display the branch, the base, the merge strategy (the project's convention; otherwise `--no-ff`), `REVIEWED_SHA`, the build and test results and the files changed, then ask: reply "merge" to merge locally with that strategy, or "cancel". Offer no other strategy: the strategy comes from the project's convention, and changing it is the user's call, made by saying so. With `no-merge`, display the review result only and stop.
2. On an explicit yes, run the state check (Confirmation rules), then merge the branch into the base **locally**, only if the build and tests are green. The merge happens in the user's working copy: if `git status --porcelain` is not empty, **stop** and ask them to commit or stash first, and record `ORIGINAL_BRANCH="$(git branch --show-current)"` to return to it afterwards (`git switch "$ORIGINAL_BRANCH"`):
   ```bash
   git switch "$BASE_BRANCH"
   git merge --no-ff -m "Merge branch '<PR_BRANCH>'" '<REVIEWED_SHA>'      # or: git merge --squash '<REVIEWED_SHA>' && git commit
   ```
   Merge `REVIEWED_SHA`, the reviewed commit, never the branch name: the local branch may be behind or missing. If the merge conflicts or fails: **do not force**; abort the merge (`git merge --abort`), report and stop.
3. **Separate confirmation** before deleting the local branch: ask `🌿 Delete the local branch <PR_BRANCH>?` and offer "delete" or "keep". On "delete": `git branch -d "$PR_BRANCH"`; use `-D` only after confirming the merge result contains its changes. Then return to `ORIGINAL_BRANCH`, unless it was the deleted branch: in that case stay on the base and say so.
4. If there is a remote: **do not push** on your own. Tell the user the base branch is ahead of the remote and ask whether to push, and whether to delete the remote branch.
5. Display the summary with each action marked as done, skipped or failed, and the current branch. For mode C, use that system's equivalents.

### Mode D — No version control

There is nothing to merge. Show the closing entry that would be appended to the changelog file (`approved`, date, and the review result) and ask for confirmation. On an explicit yes, append it and display:
```
✅ Change approved — record closed in <changelog path>
```
Otherwise display `⏭ Record not closed` and stop.
