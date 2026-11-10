"""Validações estruturais do marketplace, executadas no CI e localmente.

Uso: python3 -X utf8 scripts/validate.py [--fingerprints]
"""

import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGINS = ("checkup", "spec", "polish")
CATALOGS = {"security": 153, "performance": 163, "privacy": 126, "ai-readiness": 70}
STYLE_REFERENCE = "${CLAUDE_PLUGIN_ROOT}/references/STYLE.md"
CATALOG_CHANGELOG = "plugins/checkup/references/CATALOG-CHANGELOG.md"
REPORT_SCHEMA = "plugins/checkup/references/report.schema.json"
REPORT_EXAMPLE = "docs/examples/security-report.example.json"
USER_ONLY_SKILLS = ("plugins/spec/skills/approve/SKILL.md",)
FORBIDDEN_PATHS = re.compile(r"^personal/|(^|/)\.env(?!\.example$)(\.[^/]+)?$")

errors = []


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else None


def catalog_items(skill):
    text = read(f"plugins/checkup/skills/{skill}/references/checklist.md").replace("\r", "")
    blocks = re.findall(r"^(#### [A-Z]+-\d+\.\d+ · .*?)(?=^#{2,4} |\Z)", text, re.M | re.S)
    return text, [re.sub(r"[ \t]+$", "", block.strip(), flags=re.M) for block in blocks]


def fingerprint(blocks):
    return hashlib.sha256("\n".join(blocks).encode("utf-8")).hexdigest()[:12]


def check_catalogs():
    changelog = read(CATALOG_CHANGELOG)
    latest = re.search(r"^## (\d+\.\d+\.\d+) — .*?(?=^## |\Z)", changelog, re.M | re.S)
    if not latest:
        errors.append(f"{CATALOG_CHANGELOG}: nenhuma versão encontrada")
        return
    for skill, count in CATALOGS.items():
        path = f"plugins/checkup/skills/{skill}/references/checklist.md"
        text, blocks = catalog_items(skill)
        ids = [re.match(r"#### (\S+)", block).group(1) for block in blocks]
        severities = [re.search(r"^\*\*(Critical|Important|Minor)\*\*", block, re.M) for block in blocks]
        if len(ids) != count:
            errors.append(f"{path}: {len(ids)} itens, esperado {count}")
        if len(set(ids)) != len(ids):
            errors.append(f"{path}: IDs duplicados")
        if not all(severities):
            errors.append(f"{path}: item sem severidade")
            continue
        totals = [sum(1 for s in severities if s.group(1) == name) for name in ("Critical", "Important", "Minor")]
        header = re.search(r"\*\*Total items:\*\* (\d+) — Critical: (\d+) · Important: (\d+) · Minor: (\d+)", text)
        if not header or [int(n) for n in header.groups()] != [len(ids)] + totals:
            errors.append(f"{path}: totais do cabeçalho diferem dos itens ({len(ids)} — {' · '.join(map(str, totals))})")
        row = re.search(rf"^\| {re.escape(skill)} \| (\d+) \| (\d+) · (\d+) · (\d+) \| `([0-9a-f]{{12}})` \|$", latest.group(0), re.M)
        if not row:
            errors.append(f"{CATALOG_CHANGELOG}: versão {latest.group(1)} sem linha para {skill}")
        elif [int(n) for n in row.groups()[:4]] != [len(ids)] + totals or row.group(5) != fingerprint(blocks):
            errors.append(
                f"{path}: o catálogo mudou desde a versão {latest.group(1)}; registre uma nova versão em {CATALOG_CHANGELOG} "
                f"(atual: {len(ids)} itens, {' · '.join(map(str, totals))}, fingerprint {fingerprint(blocks)})"
            )


def check_plugin_references():
    for plugin in PLUGINS:
        root = f"plugins/{plugin}"
        for md in glob.glob(f"{root}/**/*.md", root_dir=ROOT, recursive=True):
            md = md.replace(os.sep, "/")
            for match in re.finditer(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)", read(md)):
                ref = match.group(1).rstrip(".,`)")
                if not os.path.exists(os.path.join(ROOT, root, ref)):
                    errors.append(f"{md}: referência inexistente {ref}")


def check_skills():
    for skill in glob.glob("plugins/*/skills/*/SKILL.md", root_dir=ROOT):
        skill = skill.replace(os.sep, "/")
        text = read(skill)
        meta = frontmatter(text)
        if meta is None:
            errors.append(f"{skill}: frontmatter ausente")
            continue
        name = re.search(r"^name: (.+)$", meta, re.M)
        if not name or name.group(1).strip() != skill.split("/")[-2]:
            errors.append(f"{skill}: 'name' diferente do nome da pasta")
        if not re.search(r'^description: ".+"$', meta, re.M):
            errors.append(f"{skill}: 'description' ausente ou sem aspas duplas")
        if STYLE_REFERENCE not in text:
            errors.append(f"{skill}: não referencia {STYLE_REFERENCE}")
        user_only = re.search(r"^disable-model-invocation: true$", meta, re.M) is not None
        if user_only != (skill in USER_ONLY_SKILLS):
            errors.append(f"{skill}: 'disable-model-invocation: true' esperado só em {', '.join(USER_ONLY_SKILLS)}")


def check_style_copies():
    copies = {plugin: read(f"plugins/{plugin}/references/STYLE.md") for plugin in PLUGINS}
    if len(set(copies.values())) != 1:
        errors.append("plugins/*/references/STYLE.md: as cópias não são idênticas")


def check_markdown_links():
    for md in glob.glob("**/*.md", root_dir=ROOT, recursive=True):
        md = md.replace(os.sep, "/")
        text = re.sub(r"```.*?```", "", read(md), flags=re.S)
        for target in re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'href="([^"]+)"', text):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#")[0]
            if path and not os.path.exists(os.path.join(ROOT, os.path.dirname(md), path)):
                errors.append(f"{md}: link interno quebrado {target}")


def check_forbidden_paths():
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    for path in tracked.splitlines():
        if FORBIDDEN_PATHS.search(path):
            errors.append(f"{path}: arquivo proibido no repositório (contexto pessoal ou segredos)")


def classification(score):
    for limit, name in ((25, "Dangerous"), (50, "Bronze"), (70, "Silver"), (90, "Gold")):
        if score < limit:
            return name
    return "Platinum"


def check_readme_examples():
    """Confere o exemplo de relatório dos READMEs contra as regras de pontuação do ASSESSMENT.md (§4 e §5)."""
    weights = (3, 2, 1)
    _, blocks = catalog_items("security")
    catalog_totals = [sum(1 for b in blocks if re.search(rf"^\*\*{name}\*\*", b, re.M)) for name in ("Critical", "Important", "Minor")]
    number = r"(\d+(?:[.,]\d+)?)"
    for readme, labels in (("README.md", ("Critical", "Important", "Minor")), ("README.pt-BR.md", ("Crítico", "Importante", "Menor"))):
        text = read(readme)
        earned_total = possible_total = 0
        counts_total = [0, 0, 0, 0]
        for label, weight, catalog_count in zip(labels, weights, catalog_totals):
            row = re.search(rf"^\| {label} \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| {number} / (\d+) \|$", text, re.M)
            if not row:
                errors.append(f"{readme}: linha '{label}' do resumo do exemplo não encontrada")
                return
            compliant, partial, non_compliant, not_applicable = (int(n) for n in row.groups()[:4])
            earned = compliant * weight + partial * weight / 2
            possible = (compliant + partial + non_compliant) * weight
            if float(row.group(5).replace(",", ".")) != earned or int(row.group(6)) != possible:
                errors.append(f"{readme}: pontos de '{label}' deveriam ser {earned:g} / {possible}")
            if compliant + partial + non_compliant + not_applicable != catalog_count:
                errors.append(f"{readme}: '{label}' soma {compliant + partial + non_compliant + not_applicable} itens, o catálogo tem {catalog_count}")
            earned_total += earned
            possible_total += possible
            counts_total = [a + b for a, b in zip(counts_total, (compliant, partial, non_compliant, not_applicable))]
        score = round(100 * earned_total / possible_total, 1)
        total = re.search(rf"^\| \*\*Total\*\* \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| \*\*{number} / (\d+) = {number}\*\* \|$", text, re.M)
        if not total:
            errors.append(f"{readme}: linha Total do resumo do exemplo não encontrada")
            return
        stated = [float(g.replace(",", ".")) for g in total.groups()]
        if stated != counts_total + [earned_total, possible_total, score]:
            errors.append(f"{readme}: linha Total deveria ser {counts_total} e {earned_total:g} / {possible_total} = {score}")
        expected = classification(score)
        counts_line = re.search(r"^(\d+) compliant · (\d+) (?:partial|parciais) · (\d+) (?:non-compliant|não compliant) · (\d+) N/A", text, re.M)
        if not counts_line or [int(n) for n in counts_line.groups()] != counts_total:
            errors.append(f"{readme}: a linha de contagens da resposta no chat deveria ser {counts_total}")
        for match in re.finditer(r"^# [^\n]*?[Ss]core[^\n]*?: " + number + r" / 100(?: — (\w+))?$", text, re.M):
            if float(match.group(1).replace(",", ".")) != score or (match.group(2) and match.group(2) != expected):
                errors.append(f"{readme}: '{match.group(0)}' deveria mostrar {score} e {expected}")
        if not re.search(rf"^## (?:Classification|Classificação): {expected}$", text, re.M):
            errors.append(f"{readme}: classificação do exemplo deveria ser {expected}")


JSON_TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def schema_errors(value, schema, root, path="$"):
    """Validador mínimo do subconjunto de JSON Schema usado em report.schema.json (sem dependências)."""
    if "$ref" in schema:
        schema = root["$defs"][schema["$ref"].split("/")[-1]]
    found = []
    types = schema.get("type")
    if types:
        types = [types] if isinstance(types, str) else types
        def matches(name):
            if name in ("number", "integer"):
                ok = isinstance(value, (int, float)) and not isinstance(value, bool)
                return ok and (name == "number" or float(value).is_integer())
            return isinstance(value, JSON_TYPES[name])
        if not any(matches(name) for name in types):
            return [f"{path}: tipo {type(value).__name__}, esperado {types}"]
    if value is None:
        return found
    if "enum" in schema and value not in schema["enum"]:
        found.append(f"{path}: {value!r} fora de {schema['enum']}")
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            found.append(f"{path}: {value!r} não casa com {schema['pattern']}")
        if len(value) < schema.get("minLength", 0):
            found.append(f"{path}: texto vazio")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get("minimum", value) or value > schema.get("maximum", value):
            found.append(f"{path}: {value} fora do intervalo")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            found.append(f"{path}: itens insuficientes")
        for index, item in enumerate(value):
            found += schema_errors(item, schema.get("items", {}), root, f"{path}[{index}]")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        found += [f"{path}: campo obrigatório '{key}' ausente" for key in schema.get("required", []) if key not in value]
        for key, item in value.items():
            if key in properties:
                found += schema_errors(item, properties[key], root, f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                found.append(f"{path}: campo não previsto '{key}'")
            elif isinstance(schema.get("additionalProperties"), dict):
                found += schema_errors(item, schema["additionalProperties"], root, f"{path}.{key}")
    return found


def check_report_example():
    schema = json.loads(read(REPORT_SCHEMA))
    example = json.loads(read(REPORT_EXAMPLE))
    errors.extend(f"{REPORT_EXAMPLE}: {e}" for e in schema_errors(example, schema, schema))
    weights = {"critical": 3, "important": 2, "minor": 1}
    earned = possible = 0
    for severity, weight in weights.items():
        row = example["totals"][severity]
        row_earned = row["compliant"] * weight + row["partial"] * weight / 2
        row_possible = (row["compliant"] + row["partial"] + row["nonCompliant"]) * weight
        if (row["earned"], row["possible"]) != (row_earned, row_possible):
            errors.append(f"{REPORT_EXAMPLE}: totais de {severity} deveriam ser {row_earned:g} / {row_possible}")
        earned += row_earned
        possible += row_possible
    score = round(100 * earned / possible, 1)
    if (example["totals"]["earned"], example["totals"]["possible"], example["score"]) != (earned, possible, score):
        errors.append(f"{REPORT_EXAMPLE}: total deveria ser {earned:g} / {possible} = {score}")
    if example["classification"] != classification(score):
        errors.append(f"{REPORT_EXAMPLE}: classificação deveria ser {classification(score)}")
    _, blocks = catalog_items(example["pillar"])
    severities = {re.match(r"#### (\S+)", b).group(1): re.search(r"^\*\*(Critical|Important|Minor)\*\*", b, re.M).group(1) for b in blocks}
    for item in example["items"]:
        if severities.get(item["id"]) != item["severity"]:
            errors.append(f"{REPORT_EXAMPLE}: {item['id']} não existe no catálogo ou a severidade difere")
    if example["catalog"]["fingerprints"].get(example["pillar"]) != fingerprint(blocks):
        errors.append(f"{REPORT_EXAMPLE}: fingerprint do catálogo desatualizado")


if "--fingerprints" in sys.argv:
    for skill in CATALOGS:
        print(f"{skill}: {fingerprint(catalog_items(skill)[1])}")
    sys.exit(0)

check_catalogs()
check_plugin_references()
check_skills()
check_style_copies()
check_markdown_links()
check_forbidden_paths()
check_readme_examples()
check_report_example()

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Validações OK")
