# Compatibility

What each version of the plugins was checked against. "Validated" means the manifests and structure pass `claude plugin validate` and `scripts/validate.py`; "run" means the skills were executed end to end; "not tested" means neither.

## Plugins 1.1.0

| Component | Requirement | Status |
|---|---|---|
| Claude Code (plugins) | Any version with plugin marketplaces. Plugin manifests use only the fields every version understands | Validated with 2.1.63 (Windows 10) and 2.1.114 (CI, Ubuntu) |
| Claude Code (`spec` plugin) | **2.1.110 or later.** `spec:approve` relies on the skill frontmatter field `disable-model-invocation: true` so that Claude cannot start it on its own. A version that ignores the field drops that protection without warning. The Claude Code changelog first mentions the field in 2.1.110 (a fix, so the field existed by then); the version that introduced it is not in the changelog | Required minimum (not tested on older versions); the confirmations inside `approve` do not depend on the field |
| Claude Code (evals) | 2.1.269 or later (`claude plugin eval`) | Suites validated structurally; not run yet |
| CLI (`claude`) | — | Validated; skills not run yet |
| Desktop app (Code tab) | Same plugin system as the CLI | Not tested |
| VS Code extension | `/plugins` → Manage plugins | Not tested |
| Windows | — | Validated (manifests); evals need WSL2 |
| macOS, Linux | — | Linux validated in CI (manifests); macOS not tested |
| Skills that run on the assessed project | The project's own toolchain (Node, Python, Go…) for build and tests | Depends on the project |

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
