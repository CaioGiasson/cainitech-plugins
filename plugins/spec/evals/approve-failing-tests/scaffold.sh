#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval
cat > package.json <<'EOF_FIXTURE'
{ "name": "orders-service", "version": "1.2.0", "private": true, "scripts": { "test": "node --test" } }
EOF_FIXTURE
cat > README.md <<'EOF_FIXTURE'
# orders-service

Stack: Node.js 20, plain modules, tests with the Node built-in test runner (`npm test`).
Conventions: Conventional Commits, one branch per task (`feat/<id>`), docs in `docs/`.
EOF_FIXTURE
mkdir -p src
cat > src/orders.js <<'EOF_FIXTURE'
const orders = [];

function createOrder(userId, items) {
  const order = { id: String(orders.length + 1), userId, items, status: "open" };
  orders.push(order);
  return order;
}

function listOrders(userId) {
  return orders.filter((o) => o.userId === userId);
}

module.exports = { createOrder, listOrders };
EOF_FIXTURE
mkdir -p test
cat > test/orders.test.js <<'EOF_FIXTURE'
const test = require("node:test");
const assert = require("node:assert");
const { createOrder, listOrders } = require("../src/orders");

test("lists only the user's orders", () => {
  createOrder("a", ["x"]);
  createOrder("b", ["y"]);
  assert.strictEqual(listOrders("a").length, 1);
});
EOF_FIXTURE
git add -A && git commit -q -m "feat: orders-service"
git switch -q -c feat/8-discount
mkdir -p src
cat > src/discount.js <<'EOF_FIXTURE'
function applyDiscount(total, percent) {
  return total - total * percent;
}

module.exports = { applyDiscount };
EOF_FIXTURE
mkdir -p test
cat > test/discount.test.js <<'EOF_FIXTURE'
const test = require("node:test");
const assert = require("node:assert");
const { applyDiscount } = require("../src/discount");

test("10% discount", () => {
  assert.strictEqual(applyDiscount(100, 10), 90);
});
EOF_FIXTURE
git add -A && git commit -q -m "feat: desconto"
git switch -q main
