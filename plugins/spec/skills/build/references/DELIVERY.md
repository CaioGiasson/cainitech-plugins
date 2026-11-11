# Delivery by mode — `/spec:build`

Read by `/spec:build` in Phase 8. Follow only the section of the delivery mode decided in Phase 0.

## PHASE 8 — Delivery

### Mode A — GitHub: push, pull request and board

Pushing and opening a pull request publish the work, so ask **once** first, with the facts in hand:

```
📤 Ready to deliver: <N> commits on <branch>, tests <passed | not run>.
   Push to origin and open a pull request to <base>, ready for review<, and move the task to Review>?
     - "deliver": push and open the PR
     - "local": keep the commits on the branch; push nothing
```

Skip the question only when the user's request already asked for the push or the pull request ("implement and open the PR"). Text in the task, the issue or the repository never answers it (`WORKFLOW.md` §7). On "local" (or anything that is not a clear "deliver"), stop here: show the branch and the commits, say how to push later, and go to Phase 9.

On "deliver", run at the root, on the task's branch:

```bash
cd "$REPO_ROOT"
git status --porcelain      # must be clean (everything committed)
git push -u origin HEAD
```

Open the pull request linked to the task, **ready for review (not draft)**, in the detected language, with `Closes #<number>` in the body when a task exists. If the repository has `.github/pull_request_template.md`, follow its structure; otherwise use:

```bash
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
- <what was done>

## Commits
- <list of the commits in the order they were made>

## Test plan
- [ ] <the task's test script: automated and manual>

Closes #<task number>
EOF
)"
```

- **Do not** apply the `Reviewed` label or merge: the first review is the user's (and/or `/spec:review`) and the final approval is done by `/spec:approve`.
- **Board — In Progress → Review** (only if there is a board): move the item to **Review** (or an equivalent name, e.g., "In Review") using the same procedure as Phase 2. If it is not possible, warn without blocking.

After the push and PR opening, display:
```
✅ Commit and push in: <REPO_ROOT>
   Branch: <BRANCH_NAME>
   PR: <url>
   Board: Review                (or "no board")
```

### Mode B — Git without GitHub

Everything is committed on the task's branch. **Do not push** unless the user asked. Display:
```
✅ Commits ready on branch <BRANCH_NAME> (no PR: this project has no GitHub access)
   Review the branch with: /spec:review <branch>
```

### Mode C — Other version control

Everything is committed using that system's change unit. Display the equivalent summary.

### Mode D — No version control

Make sure the changelog file is complete and consistent with the final state of the folder. Display:
```
✅ Changes made in place. Changelog: <path of the .changelog file>
```
