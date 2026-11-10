#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval
cat > index.js <<'EOF_FIXTURE'
function add(a, b) { return a + b; }
module.exports = { add };
EOF_FIXTURE
git add -A && git commit -q -m "init"
