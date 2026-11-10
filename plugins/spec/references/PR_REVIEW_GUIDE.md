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

## 📋 Review checklist

### 🔍 First impression

-   [ ] **Descriptive title**: the title explains what was done
-   [ ] **Complete description**: explains the problem, the solution and the context
-   [ ] **Adequate size**: not too large (ideally < 500 lines)
-   [ ] **Organized commits**: commits are logical and atomic
-   [ ] **Up-to-date branch**: the branch is up to date with the base branch

### ✅ Clean code

-   [ ] **Descriptive names**: variables, functions and classes have clear names

    ```typescript
    // ❌ Review
    const d = getData()
    const u = processUser(u)

    // ✅ Approve
    const userData = getUserData()
    const processedUser = processUser(userData)
    ```

-   [ ] **Small functions**: functions do one thing

    ```typescript
    // ❌ Review - function too big
    function processOrder(order) {
    	validate(order)
    	calculate(order)
    	save(order)
    	sendEmail(order)
    	log(order)
    	// ... 50 more lines
    }
    ```

-   [ ] **No duplication**: duplicated code was extracted
-   [ ] **Useful comments**: comments explain the “why”, not the “what”
-   [ ] **No dead code**: commented-out or unused code was removed

### ✅ Typing *(statically typed or gradually typed languages)*

-   [ ] **Avoid the escape hatches** (`any`, `Object`, unchecked casts, `# type: ignore`): if strictly necessary (e.g., an untyped library or complex dynamic data), it must be justified with a comment

    ```typescript
    // ❌ Review - no justification
    function process(data: any) {}

    // ✅ Approve - justified
    // Using any temporarily because the legacy library has no types
    function process(data: any) {}

    // ✅ Approve - typed properly
    function process(data: UserData) {}
    ```

-   [ ] **Explicit types**: types are clear (avoid ambiguous inference)
-   [ ] **Well-defined interfaces**: interfaces describe clear contracts
-   [ ] **Type guards**: types are validated where needed
-   [ ] **Appropriate generics**: generics are used when they make sense

### ✅ Functions and methods

-   [ ] **Avoid long parameter lists**: functions with more than ~3 parameters should take a configuration object (DTO/interface). The goal is readability and maintainability

    ```typescript
    // ❌ Review - too many parameters
    function createUser(name, email, age, city, country, phone) {}

    // ✅ Approve - configuration object
    function createUser(userData: CreateUserData) {}
    ```

-   [ ] **Single responsibility**: each function has a single responsibility
-   [ ] **Input validation**: parameters are validated up front
-   [ ] **Error handling**: errors are handled properly

### ✅ Error handling

-   [ ] **Specific errors**: custom/typed errors with clear messages, following the project's error hierarchy if it has one

    ```typescript
    // ❌ Review
    throw new Error('Error')

    // ✅ Approve
    throw new ValidationError('Email format is invalid')
    ```

-   [ ] **Correct status codes**: appropriate HTTP status (for APIs)
-   [ ] **Adequate logging**: errors are logged with context
-   [ ] **Do not expose details**: messages do not expose internals
-   [ ] **Appropriate try/catch**: try/catch only where necessary

### ✅ Security

-   [ ] **Input validation**: all inputs at external boundaries are validated

    ```typescript
    // ❌ Review - no validation
    function updateUser(userId: string, data: any) {
    	return db.users.update({ where: { id: userId }, data })
    }

    // ✅ Approve - validated
    function updateUser(userId: string, data: UpdateUserData) {
    	validateUserId(userId)
    	validateUserData(data)
    	return db.users.update({ where: { id: userId }, data })
    }
    ```

-   [ ] **Sanitization**: data is sanitized before processing
-   [ ] **Authentication**: protected endpoints require authentication
-   [ ] **Authorization**: permissions are checked on the server
-   [ ] **Secrets in the environment**: credentials and URLs are not hardcoded

### ✅ Performance

-   [ ] **Optimized queries**: efficient queries (indexes, projections)

    ```typescript
    // ❌ Review - N+1 queries
    const users = await db.users.findMany()
    for (const user of users) {
    	user.posts = await db.posts.findMany({ where: { userId: user.id } })
    }

    // ✅ Approve - single query
    const users = await db.users.findMany({
    	include: { posts: true },
    })
    ```

-   [ ] **Pagination**: large lists are paginated
-   [ ] **Appropriate cache**: cache is used when it makes sense
-   [ ] **No queries in loops**: avoid queries inside loops
-   [ ] **Configured timeouts**: external requests have timeouts

### ✅ REST APIs *(when the change touches HTTP endpoints)*

-   [ ] **RESTful naming**: URLs follow REST conventions

    ```
    // ❌ Review
    GET  /getUserById/123
    POST /createNewUser

    // ✅ Approve
    GET  /users/123
    POST /users
    ```

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

    ```typescript
    // ❌ Review
    it('test 1', () => {})

    // ✅ Approve
    it('should throw ValidationError when email is invalid', () => {})
    ```

### ✅ Observability and logging

-   [ ] **The application's logger** — not `print`/`console.log` in application code, when the project has a logger

    ```typescript
    // ❌ Review
    console.log('User created', userId)

    // ✅ Approve
    logger.info('User created', { userId })
    ```

-   [ ] **Log levels**: appropriate use of info, warn, error
-   [ ] **Context in logs**: logs include enough context
-   [ ] **No sensitive data**: credentials and personal data do not appear in logs
-   [ ] **Metrics / tracing / feature flags** — desirable; do not block a PR for their absence unless explicitly agreed

### ✅ Environment variables and configuration

-   [ ] **Config outside the code**: configuration is not hardcoded

    ```typescript
    // ❌ Review
    const apiUrl = 'https://api.example.com'

    // ✅ Approve
    const apiUrl = process.env.API_URL
    ```

-   [ ] **Validation at startup**: required variables are validated
-   [ ] **Documentation**: variables are documented (`.env.example` or equivalent)
-   [ ] **No secrets in code**: secrets are never committed

### ✅ Git and commits

-   [ ] **Atomic commits**: each commit represents a logical change
-   [ ] **Descriptive messages**: clear, descriptive messages

    ```
    ❌ Review: "fix"
    ✅ Approve: "Validate email format on user creation input"
    ```

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

## 📝 Examples of Change Requests and Comments

### Example 1: Input validation (Change Request 🔴)

```typescript
// Code in the PR
function createUser(email: string, age: number) {
	return db.users.create({ email, age })
}
```

**Change Request (🔴):**

```
Change request (🔴): This function does not validate its inputs. An invalid
email or a negative age can cause problems in the database and break the user
creation flow. Risk: invalid data can be persisted.

Suggestion: add validation before creating:

function createUser(email: string, age: number) {
  if (!isValidEmail(email)) {
    throw new ValidationError('Invalid email format')
  }
  if (age < 0 || age > 150) {
    throw new ValidationError('Age must be between 0 and 150')
  }
  return db.users.create({ email, age })
}
```

### Example 2: Performance (Change Request 🟡)

```typescript
// Code in the PR
const users = await db.users.findMany()
for (const user of users) {
	user.posts = await db.posts.findMany({ where: { userId: user.id } })
}
```

**Change Request (🟡):**

```
Change request (🟡): This causes an N+1 query problem. For 100 users there
will be 101 database queries. Risk: in production with many users this can
significantly degrade performance and overload the database.

Suggestion: use include to join in a single query:

const users = await db.users.findMany({
  include: { posts: true }
})
```

### Example 3: Typing (Change Request 🟡)

```typescript
// Code in the PR
function process(data: any) {
	return data.value * 2
}
```

**Change Request (🟡):**

```
Change request (🟡): Using `any` removes the benefits of the type system and
can cause runtime errors if `data.value` does not exist or is not a number.
Risk: loss of type safety and possible bugs that are hard to detect.

Suggestion: create an interface to type it properly:

interface ProcessableData {
  value: number
}

function process(data: ProcessableData): number {
  return data.value * 2
}
```

### Example 4: Naming (Comment 🟢)

```typescript
// Code in the PR
function calc(x: number, y: number): number {
	return x + y
}
```

**Comment (🟢):**

```
Comment (🟢): How about renaming `calc` to something more descriptive such as
`calculateSum` or `addNumbers`? That would make the code more readable and
self-documenting. It is not critical, but it would be an improvement.
```

### Example 5: Organization (Comment 🟢)

```typescript
// Code in the PR
function processOrder(order: Order) {
	validate(order)
	calculate(order)
	save(order)
	sendEmail(order)
	log(order)
	return order
}
```

**Comment (🟢):**

```
Comment (🟢): This function does several things. Did you consider extracting
some responsibilities into separate functions? For example, `sendOrderEmail()`
and `logOrderCreation()`. That would make the code more testable and reusable.
It is not urgent, but it would be a good refactor for the future.
```

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
