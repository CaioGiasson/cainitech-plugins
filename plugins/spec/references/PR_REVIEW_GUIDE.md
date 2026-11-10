# Pull Request Review Guide — General Best Practices

Used by `/spec:review`, `/spec:approve` and the internal review of `/spec:build`. It is language- and stack-neutral: the examples are in TypeScript or pseudo-code only to illustrate an idea. **The project's own conventions always win** (see `WORKFLOW.md` §2): where this guide and the project disagree, follow the project.

## 🎯 Goal of a review

A good code review should:

-   ✅ Ensure quality and consistency
-   ✅ Share knowledge
-   ✅ Prevent bugs and security problems
-   ✅ Improve maintainability
-   ✅ Be constructive and educational

## 🔎 How to review

### 1. Understand the context

Before reviewing:

-   [ ] Read the PR description (or the change summary, when there is no PR)
-   [ ] Understand the problem being solved
-   [ ] Check related tasks/issues and the refinement document
-   [ ] Look at the commit history

### 2. Structural review

-   [ ] **Modified files**: files are in the right place
-   [ ] **Change size**: is the change too big? Suggest splitting it
-   [ ] **Dependencies**: are the new dependencies really needed?
-   [ ] **Breaking changes**: are there any? Are they documented?

### 3. Code review

-   [ ] **Logic**: is the logic correct?
-   [ ] **Edge cases**: were edge cases considered?
-   [ ] **Performance**: any obvious performance problems?
-   [ ] **Security**: any vulnerabilities?
-   [ ] **Tests**: do the tests cover the necessary cases?

### 4. Best-practices review

Use the checklist below: clean code, typing, error handling, security, performance, observability, database migrations, tests, documentation.

Code examples for the checklist items and model review comments are in `${CLAUDE_PLUGIN_ROOT}/references/PR_REVIEW_EXAMPLES.md`. Read it only when you need a model for an item or for the wording of a comment.

## 📋 Review checklist

### 🔍 First impression

-   [ ] **Descriptive title**: the title explains what was done
-   [ ] **Complete description**: explains the problem, the solution and the context
-   [ ] **Adequate size**: not too large (ideally < 500 lines)
-   [ ] **Organized commits**: commits are logical and atomic
-   [ ] **Up-to-date branch**: the branch is up to date with the base branch

### ✅ Clean code

-   [ ] **Descriptive names**: variables, functions and classes have clear names
-   [ ] **Small functions**: functions do one thing
-   [ ] **No duplication**: duplicated code was extracted
-   [ ] **Useful comments**: comments explain the “why”, not the “what”
-   [ ] **No dead code**: commented-out or unused code was removed

### ✅ Typing *(statically typed or gradually typed languages)*

-   [ ] **Avoid the escape hatches** (`any`, `Object`, unchecked casts, `# type: ignore`): if strictly necessary (e.g., an untyped library or complex dynamic data), it must be justified with a comment
-   [ ] **Explicit types**: types are clear (avoid ambiguous inference)
-   [ ] **Well-defined interfaces**: interfaces describe clear contracts
-   [ ] **Type guards**: types are validated where needed
-   [ ] **Appropriate generics**: generics are used when they make sense

### ✅ Functions and methods

-   [ ] **Avoid long parameter lists**: functions with more than ~3 parameters should take a configuration object (DTO/interface). The goal is readability and maintainability
-   [ ] **Single responsibility**: each function has a single responsibility
-   [ ] **Input validation**: parameters are validated up front
-   [ ] **Error handling**: errors are handled properly

### ✅ Error handling

-   [ ] **Specific errors**: custom/typed errors with clear messages, following the project's error hierarchy if it has one
-   [ ] **Correct status codes**: appropriate HTTP status (for APIs)
-   [ ] **Adequate logging**: errors are logged with context
-   [ ] **Do not expose details**: messages do not expose internals
-   [ ] **Appropriate try/catch**: try/catch only where necessary

### ✅ Security

-   [ ] **Input validation**: all inputs at external boundaries are validated
-   [ ] **Sanitization**: data is sanitized before processing
-   [ ] **Authentication**: protected endpoints require authentication
-   [ ] **Authorization**: permissions are checked on the server
-   [ ] **Secrets in the environment**: credentials and URLs are not hardcoded

### ✅ Performance

-   [ ] **Optimized queries**: efficient queries (indexes, projections)
-   [ ] **Pagination**: large lists are paginated
-   [ ] **Appropriate cache**: cache is used when it makes sense
-   [ ] **No queries in loops**: avoid queries inside loops
-   [ ] **Configured timeouts**: external requests have timeouts

### ✅ REST APIs *(when the change touches HTTP endpoints)*

-   [ ] **RESTful naming**: URLs follow REST conventions
-   [ ] **Correct HTTP methods**: GET, POST, PATCH, PUT, DELETE are appropriate
-   [ ] **Appropriate status codes**: HTTP status reflects the result
-   [ ] **Documentation**: the API contract is updated where the project keeps it (OpenAPI/Swagger, request collections, API docs) — missing contract for a new or changed endpoint is a blocker when the project adopts one
-   [ ] **Consistent responses**: the project's response envelope/format is used

### ✅ Database

-   [ ] **Transactions when needed**: atomic operations use transactions
-   [ ] **Appropriate indexes**: indexes for frequent queries
-   [ ] **Safe migrations**: reversible or expand/contract; no destructive change before consumers migrate
-   [ ] **Soft delete**: follow the project's convention; filters must consider how the datastore represents “not deleted” (e.g., a field that is absent or null)

### ✅ Tests

-   [ ] **Tests created**: new features have tests
-   [ ] **Adequate coverage**: tests cover the main cases
-   [ ] **Isolated tests**: tests do not depend on each other
-   [ ] **Proper mocks**: external dependencies are mocked
-   [ ] **Edge cases**: edge cases are tested
-   [ ] **Clear naming**: test names describe behavior

### ✅ Observability and logging

-   [ ] **The application's logger** — not `print`/`console.log` in application code, when the project has a logger
-   [ ] **Log levels**: appropriate use of info, warn, error
-   [ ] **Context in logs**: logs include enough context
-   [ ] **No sensitive data**: credentials and personal data do not appear in logs
-   [ ] **Metrics / tracing / feature flags** — desirable; do not block a PR for their absence unless explicitly agreed

### ✅ Environment variables and configuration

-   [ ] **Config outside the code**: configuration is not hardcoded
-   [ ] **Validation at startup**: required variables are validated
-   [ ] **Documentation**: variables are documented (`.env.example` or equivalent)
-   [ ] **No secrets in code**: secrets are never committed

### ✅ Git and commits

-   [ ] **Atomic commits**: each commit represents a logical change
-   [ ] **Descriptive messages**: clear, descriptive messages
-   [ ] **No unnecessary files**: `.env`, dependency folders and build output are not committed
-   [ ] **Branch naming**: the branch follows the convention and links to the task

### ✅ Documentation

-   [ ] **README updated**: significant changes are documented
-   [ ] **Comments on complex code**: complex code is commented
-   [ ] **API documentation**: the API is documented (Swagger, etc.) when the project keeps it
-   [ ] **Refinement document**: the refinement is recorded in the project's docs (see `WORKFLOW.md` §4)
-   [ ] **Context files**: `AGENTS.md`/`CLAUDE.md`/`CONTEXT.md`/`tasks/lessons.md` are updated when commands, structure or conventions change
-   [ ] **UI text**: user-visible text is in the project's text/translation catalogs in all supported languages, when there is a UI
-   [ ] **Version**: at most **one** version bump per PR, and a bump is present when the project versions itself

### ✅ Code quality

-   [ ] **Lint passed**: the linter is configured and passing
-   [ ] **Consistent formatting**: code is formatted by the project's formatter
-   [ ] **Organized imports**: imports are organized and without duplicates

## 💬 How to give feedback

### ✅ Constructive feedback

**Good feedback:**

```
"This function is doing too many things. How about extracting the validation
into a separate function `validateUserData()`? That would make the code more
testable and reusable."
```

**Bad feedback:**

```
"This function is wrong."
```

### ✅ Questions vs criticism

**Better:**

```
"What is the reason for using `any` here? Could we type it better?"
```

**Avoid:**

```
"Don't use `any`!"
```

### ✅ Specific suggestions

**Good:**

```
"To avoid N+1 queries we can use `include: { posts: true }` in the initial
query. Example: ..."
```

**Bad:**

```
"Optimize this query."
```

## 🚦 Priority levels

### 🔴 Blocker (Must Fix)

-   Security vulnerabilities
-   Critical bugs that break functionality
-   Serious violations of code standards
-   Missing tests on critical code

### 🟡 Important (Should Fix)

-   Performance problems
-   Hard-to-maintain code
-   Missing important documentation
-   Insufficient tests

### 🟢 Suggestion (Nice to Have)

-   Readability improvements
-   Minor optimizations
-   Additional documentation
-   Non-critical refactors

### 🧭 Change Request vs Comment

**Change Request (mandatory / blocks approval)**  
Use it when the change is necessary to keep **correctness, security, consistency or maintainability**.

Typical criteria:

-   **🔴 Blocker**: bug, vulnerability, broken contract/API, high risk of incident, data loss.
-   **🟡 Important**: relevant maintenance/performance risk, ambiguous behavior, missing tests on an important flow, technical debt that will “charge interest” quickly.

Suggested format:

-   **“Change request (🔴/🟡): …”**
-   Include **the why**, the **risk** and (if possible) **a concrete suggestion**.

Examples:

-   “Change request (🔴): input validation is missing; it may allow invalid data and break flow X.”
-   “Change request (🟡): this introduces N+1; in production it tends to degrade performance.”

**Comment (non-blocking / suggestion)**  
Use it when it is a desirable improvement but **not essential** for merging now.

Typical criteria:

-   **🟢 Suggestion**: readability, organization, names, micro-optimizations, stylistic alternatives, non-critical refactors.
-   Improvements that can become a **follow-up**/issue without immediate risk.

Suggested format:

-   **“Comment (🟢): …”**
-   Prefer questions and options (“How about…?” / “Did you consider…?”).

Examples:

-   “Comment (🟢): maybe rename `x` to something more descriptive.”
-   “Comment (🟢): this logic could be extracted into a function to ease testing.”

**Quick map (priority → feedback type)**:

-   **🔴 Blocker** → **always** Change Request
-   **🟡 Important** → **normally** Change Request (unless it is clearly a safe follow-up)
-   **🟢 Suggestion** → **always** Comment

When something is “almost important” but not worth blocking:

-   mark it as **Comment (🟡 optional / follow-up)** and suggest opening an issue/task as technical debt.

## ✅ Final checklist before approving

1. [ ] Code follows good general practices and the project's conventions
2. [ ] Tests created and passing
3. [ ] Documentation updated
4. [ ] Lint passed
5. [ ] No obvious security vulnerabilities
6. [ ] Performance considered
7. [ ] No breaking changes (or they are documented)
8. [ ] Feedback given was addressed
9. [ ] The change is up to date with the base branch

## 💡 Tips for reviewers

-   **Be respectful**: remember there is a person on the other side
-   **Be specific**: vague comments do not help
-   **Explain the why**: help the person understand the reason
-   **Suggest solutions**: do not just point out problems
-   **No praise or filler**: every comment states a problem, its impact and the fix (`STYLE.md`)
-   **Learn together**: use the review to learn as well

## 🎯 When to approve

Approve the change when:

-   ✅ The code follows good practices
-   ✅ Tests pass and cover the main cases
-   ✅ Documentation is up to date
-   ✅ There are no critical security or performance problems
-   ✅ Important feedback was addressed
-   ✅ You understood the code and trust it

**It does not have to be perfect**: small improvements can be made in future PRs.
