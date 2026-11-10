# Pull Request Review Guide — examples

Examples for `PR_REVIEW_GUIDE.md`, read on demand. They are in TypeScript or pseudo-code only to illustrate an idea; **the project's own conventions always win**.

## Checklist examples

### ✅ Clean code

**Descriptive names**

```typescript
// ❌ Review
const d = getData()
const u = processUser(u)

// ✅ Approve
const userData = getUserData()
const processedUser = processUser(userData)
```

**Small functions**

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

### ✅ Typing *(statically typed or gradually typed languages)*

**Avoid the escape hatches**

```typescript
// ❌ Review - no justification
function process(data: any) {}

// ✅ Approve - justified
// Using any temporarily because the legacy library has no types
function process(data: any) {}

// ✅ Approve - typed properly
function process(data: UserData) {}
```

### ✅ Functions and methods

**Avoid long parameter lists**

```typescript
// ❌ Review - too many parameters
function createUser(name, email, age, city, country, phone) {}

// ✅ Approve - configuration object
function createUser(userData: CreateUserData) {}
```

### ✅ Error handling

**Specific errors**

```typescript
// ❌ Review
throw new Error('Error')

// ✅ Approve
throw new ValidationError('Email format is invalid')
```

### ✅ Security

**Input validation**

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

### ✅ Performance

**Optimized queries**

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

### ✅ REST APIs *(when the change touches HTTP endpoints)*

**RESTful naming**

```
// ❌ Review
GET  /getUserById/123
POST /createNewUser

// ✅ Approve
GET  /users/123
POST /users
```

### ✅ Tests

**Clear naming**

```typescript
// ❌ Review
it('test 1', () => {})

// ✅ Approve
it('should throw ValidationError when email is invalid', () => {})
```

### ✅ Observability and logging

**The application's logger**

```typescript
// ❌ Review
console.log('User created', userId)

// ✅ Approve
logger.info('User created', { userId })
```

### ✅ Environment variables and configuration

**Config outside the code**

```typescript
// ❌ Review
const apiUrl = 'https://api.example.com'

// ✅ Approve
const apiUrl = process.env.API_URL
```

### ✅ Git and commits

**Descriptive messages**

```
❌ Review: "fix"
✅ Approve: "Validate email format on user creation input"
```

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
