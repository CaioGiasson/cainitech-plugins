#!/usr/bin/env bash
# Cria em uma pasta nova o repositório fictício de um caso de eval, para demonstrações e testes manuais.
# Uso: scripts/fixture.sh <plugin> <caso> <pasta-destino>
# Exemplo: scripts/fixture.sh checkup security-finds-bola /tmp/loja-online
set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Uso: $0 <plugin> <caso> <pasta-destino>" >&2
  exit 2
fi

root="$(cd "$(dirname "$0")/.." && pwd)"
scaffold="$root/plugins/$1/evals/$2/scaffold.sh"
target="$3"

if [ ! -f "$scaffold" ]; then
  # as suítes não são versionadas: gera a partir de scripts/generate_evals.py
  python3 -X utf8 "$root/scripts/generate_evals.py" >/dev/null
fi
if [ ! -f "$scaffold" ]; then
  echo "Caso sem fixture: $scaffold" >&2
  exit 1
fi
if [ -e "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then
  echo "A pasta de destino precisa estar vazia: $target" >&2
  exit 1
fi

mkdir -p "$target"
(cd "$target" && bash "$scaffold")
echo "Fixture criada em $target"
