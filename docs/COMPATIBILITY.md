# Compatibility

What each version of the plugins was checked against, at three separate levels:

- **Manifest accepted:** `claude plugin validate` and `scripts/validate.py` pass. Says nothing about behavior.
- **Skill run:** the skill ran end to end, by an eval case or by hand, on a fixture.
- **End to end:** the whole flow ran against real services (GitHub PR, CI, board, merge).

## Plugins 1.3 (`checkup` 1.3.1, `spec` 1.3.0, `polish` 1.1.1)

| Surface / system | Manifest accepted | Skill run | End to end |
|---|---|---|---|
| CLI on Linux (Ubuntu, CI) | Yes, Claude Code 2.1.114 | No | No |
| CLI on WSL2 (Ubuntu 22.04) | Yes, 2.1.322 | Yes, by the evals: `trigger` cases of the three plugins, `slow` cases of `spec`, `slow` cases of `checkup` and `polish` (results in `docs/EVALS.md`) | No |
| CLI on Windows 10 (native) | Yes, 2.1.63 and 2.1.322 | `spec:approve` by hand (`docs/CASE-STUDIES.md`, scenario 2) | No |
| Desktop app (Code tab) | Same plugin system as the CLI | Not tested | No |
| VS Code extension | Same plugin system | Not tested | No |
| macOS | Not tested | Not tested | No |

Runs in local Git mode only: pushes, pull requests, comments, labels, board moves and merges on GitHub have not been exercised by an automated test (`docs/EVALS.md`, "Known limits").

| Requirement | Detail |
|---|---|
| Claude Code (plugins) | Any version with plugin marketplaces. The manifests use only fields that 2.1.114 also accepts |
| Claude Code (`spec`) | **2.1.110 or later.** `spec:approve` relies on `disable-model-invocation: true` so that Claude cannot start it on its own. A version that ignores the field drops that protection without warning; the confirmations inside `approve` do not depend on it. The changelog first mentions the field in 2.1.110 |
| Claude Code (evals) | 2.1.269 or later (`claude plugin eval`); Bash grants need an OS sandbox, so Windows runs them under WSL2 |
| Running the assessed project | The project's own toolchain (Node, Python, Go…), only when the user chooses `run` (`WORKFLOW.md` §7.1, `ASSESSMENT.md` §1) |

## External tools

| Tool | Used by | Requirement | Without it |
|---|---|---|---|
| GitHub CLI (`gh`), signed in | `spec:*` (issues, PRs, comments, merge) | `gh auth login`; the `repo` scope | `spec` falls back to local Git, another VCS or a changelog file |
| `project` scope of `gh` | `spec:*` board moves | `gh auth refresh -s project` | Board moves are skipped with a warning |
| GitHub MCP | `spec:*`, as an alternative to `gh` | A connected GitHub MCP server | Uses `gh`, or falls back as above |
| Slack MCP | `spec:from-thread` with a Slack link | A connected Slack integration | Paste the conversation into a `.md` file |
| Discord MCP | `spec:from-thread` with a Discord link | A connected Discord integration | Paste the conversation into a `.md` file |
| GitHub Projects | `spec:*` boards | A project linked to the repository or its owner | The refinement document in `docs/specs/` is the record |

## Known limitations

- Other trackers (Linear, Jira, GitLab) are used only when the session has a connected tool for them; there is no built-in integration.
- `spec:approve` does not wait for pending CI: it reports it and stops. Run it again when CI finishes.
- Merge strategies other than squash are used only when the repository's rules or settings define them.

Report a compatibility problem as an issue with the Claude Code version, the surface and the operating system.
