# Posting the review — `/spec:review`, mode A

Read by `/spec:review` only after the user picked the comments to post. The selection, the reviewer's result and the PR (`owner`, `repo`, number) come from the skill.

## Posting

Based on the user's selection:

1. Post each selected comment on the PR **as an inline comment** — linked to the specific file and line of the diff:

   **Via MCP (preferred):**
   Use `mcp__github__create_pull_request_review` with `comments` containing `path`, `line` and `body` for each inline comment.

   **Via the gh CLI (fallback):**
   ```bash
   gh api repos/<owner>/<repo>/pulls/<number>/reviews \
     --method POST \
     --field body='<summary: Requested × Implemented table, divergences, functional-test evidence>' \
     --field event='COMMENT' \
     --field 'comments[][path]=<file>' \
     --field 'comments[][line]=<line>' \
     --field 'comments[][body]=<text>'
   ```

   The body of each 🔴/🟡 comment includes the full **How to fix** block. Group all selected comments into **a single review**, not separate requests.

1b. The review **body** must contain, in markdown: the summary of the result, the reviewer's **📋 Requested × Implemented** table, the state of the divergences (recorded or not) and the reviewer's **🧪 Functional test** table with its evidence (scenarios, commands, outputs obtained and verdict; or the reason it was not executed), as the reviewer returned them. No tokens, passwords or personal data.

2. If any **blocker items were selected**, submit the review with `event: REQUEST_CHANGES`.
   If there are **only suggestions**, submit with `event: COMMENT`.

3. Signal progress:
   ```
   📤 Posting comments on the PR...
      ✔ [1] file.ts:42 — posted
      ✔ [3] other-file.ts:88 — posted
      ...
   ```
