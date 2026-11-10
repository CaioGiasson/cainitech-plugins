#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval
cat > index.html <<'EOF_FIXTURE'
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Padaria Lua</title>
<style>
  body { font-family: Inter, sans-serif; background: linear-gradient(135deg, #6366f1, #a855f7); color: white; }
  .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
</style></head>
<body>
  <h1>Unlock the Power of Fresh Bread 🚀</h1>
  <p>Revolutionize your mornings with our seamless, cutting-edge bakery experience.</p>
  <div class="cards">
    <div>⚡ Fast</div><div>✨ Fresh</div><div>🔒 Secure</div>
  </div>
</body>
</html>
EOF_FIXTURE
cat > pricing.html <<'EOF_FIXTURE'
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Pricing</title></head>
<body><h1>Pricing</h1><p>Bread: $3. Cake: $20.</p></body></html>
EOF_FIXTURE
git add -A && git commit -q -m "feat: site"
