#!/usr/bin/env bash
set -euo pipefail
git init -q -b main
git config user.email eval@example.com
git config user.name eval
mkdir -p src
cat > src/user.model.js <<'EOF_FIXTURE'
// Cadastro de clientes
module.exports = {
  fields: ["name", "email", "cpf", "birthDate", "phone"],
  retention: "forever",
};
EOF_FIXTURE
mkdir -p docs
cat > docs/privacy-policy.md <<'EOF_FIXTURE'
# Política de privacidade

Não armazenamos CPF. Os dados são apagados 12 meses após o encerramento da conta.
EOF_FIXTURE
cat > README.md <<'EOF_FIXTURE'
# cadastro-clientes

Serviço de cadastro de clientes de uma loja brasileira.
EOF_FIXTURE
git add -A && git commit -q -m "feat: cadastro"
