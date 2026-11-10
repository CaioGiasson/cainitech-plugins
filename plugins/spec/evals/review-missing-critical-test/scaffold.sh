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
git switch -q -c feat/7-refund
mkdir -p docs/specs
cat > docs/specs/7-refund.md <<'EOF_FIXTURE'
# 7 — Refund a payment

- Branch: `feat/7-refund`

## Objective
`refund(order, amount)` records a partial or full refund of an order.

## Acceptance criteria
- A refund adds `amount` to `order.refunded`.
- A refund above the order total is rejected with an error.

## Order of commits
1. feat: estorno de pagamento

## Test script
1. Run `npm test`: all tests pass.
EOF_FIXTURE
mkdir -p src
cat > src/refunds.js <<'EOF_FIXTURE'
// Estorno de pagamento: fluxo crítico de dinheiro
function refund(order, amount) {
  if (amount > order.total) throw new Error("amount above total");
  order.refunded = (order.refunded || 0) + amount;
  return order;
}

module.exports = { refund };
EOF_FIXTURE
git add -A && git commit -q -m "feat: estorno de pagamento"
git switch -q main
