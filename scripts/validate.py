"""Validações estruturais do marketplace, executadas no CI e localmente.

Uso: python3 -X utf8 scripts/validate.py
"""

import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGINS = ("checkup", "spec", "polish")
CATALOGS = {"security": 153, "performance": 163, "privacy": 126, "ai-readiness": 70}
STYLE_REFERENCE = "${CLAUDE_PLUGIN_ROOT}/references/STYLE.md"
USER_ONLY_SKILLS = ("plugins/spec/skills/approve/SKILL.md",)
FORBIDDEN_PATHS = re.compile(r"^personal/|(^|/)\.env(?!\.example$)(\.[^/]+)?$")

errors = []


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else None


def check_catalogs():
    for skill, count in CATALOGS.items():
        path = f"plugins/checkup/skills/{skill}/references/checklist.md"
        ids = re.findall(r"^#### ([A-Z]+-\d+\.\d+)", read(path), re.M)
        if len(ids) != count:
            errors.append(f"{path}: {len(ids)} itens, esperado {count}")
        if len(set(ids)) != len(ids):
            errors.append(f"{path}: IDs duplicados")


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


check_catalogs()
check_plugin_references()
check_skills()
check_style_copies()
check_markdown_links()
check_forbidden_paths()

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Validações OK")
