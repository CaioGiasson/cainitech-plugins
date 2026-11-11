# Documentação técnica

Para quem mantém o projeto e para usuários técnicos. Para a visão geral e o catálogo de skills, veja o [README](../README.pt-BR.md). Versão em inglês: [TECHNICAL.md](TECHNICAL.md).

## O que é este repositório

Um **marketplace de plugins** do Claude Code chamado `cainitech`, com três plugins em um único repositório:

| Plugin | Skills | O que é |
|---|---|---|
| `checkup` | `security`, `performance`, `privacy`, `ai-readiness`, `full` | Avaliações somente leitura de uma aplicação: 512 critérios, nota de 0 a 100, classificação e backlog priorizado. |
| `spec` | `refine`, `from-thread`, `build`, `review`, `approve` | Fluxo de tarefas da ideia ao merge. Usa o quadro do GitHub Projects quando o projeto tem um, sempre registra o trabalho na documentação do projeto e se adapta a GitHub / Git sem GitHub / outro controle de versão / nenhum controle de versão. |
| `polish` | `ui` | Faz sites e webapps deixarem de parecer gerados por IA. Trabalha por meio de um design system: usa o do projeto, melhora o que existe ou cria um pequeno, para que os componentes sejam reusados. Só texto: não roda comandos nem baixa nada. Regras de site adaptadas do taste-skill (MIT, veja `plugins/polish/THIRD_PARTY_NOTICES.md`). |

As skills são chamadas como `/<plugin>:<skill>` (por exemplo `/checkup:security`, `/spec:refine`).

## Estrutura de pastas

```
cainitech-plugins/
├── .claude-plugin/
│   └── marketplace.json            # marketplace "cainitech": lista os três plugins
├── plugins/
│   ├── checkup/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── references/
│   │   │   ├── ASSESSMENT.md       # metodologia, status, pesos, score e formato do relatório (compartilhado pelas 5 skills)
│   │   │   ├── TOOLS.md            # ferramentas de análise instaladas: o que rodar por pilar, só leitura, como interpretar
│   │   │   ├── CONFIG.md           # .checkup.json do repositório avaliado: exceções e seus limites
│   │   │   ├── config.schema.json  # formato do .checkup.json
│   │   │   ├── report.schema.json  # JSON gêmeo dos relatórios
│   │   │   └── STYLE.md            # estilo de comunicação (idêntico em todos os plugins)
│   │   └── skills/
│   │       ├── security/           # SKILL.md + references/checklist.md (153 critérios, SEC-*)
│   │       ├── performance/        # SKILL.md + references/checklist.md (163 critérios, PERF-*)
│   │       ├── privacy/            # SKILL.md + references/checklist.md (126 critérios, PRIV-*)
│   │       ├── ai-readiness/       # SKILL.md + references/checklist.md (70 critérios, AIR-*)
│   │       └── full/               # SKILL.md (roda os quatro pilares e consolida)
│   ├── spec/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── references/
│   │   │   ├── WORKFLOW.md         # idioma, contexto do projeto, detecção de quadro, documentação obrigatória, modos de entrega, conteúdo externo
│   │   │   ├── PR_REVIEW_GUIDE.md  # guia de revisão neutro quanto à stack
│   │   │   ├── PR_REVIEW_EXAMPLES.md # exemplos de código e comentários modelo, lidos sob demanda
│   │   │   └── STYLE.md            # estilo de comunicação (idêntico em todos os plugins)
│   │   └── skills/
│   │       ├── refine/  from-thread/  build/  review/  approve/   # SKILL.md + references/ lidas sob demanda (review: REVIEWER.md para o revisor isolado de contexto)
│   └── polish/
│       ├── .claude-plugin/plugin.json
│       ├── THIRD_PARTY_NOTICES.md  # aviso MIT do taste-skill, origem da adaptação
│       ├── references/STYLE.md     # estilo de comunicação (idêntico em todos os plugins)
│       └── skills/
│           └── ui/                 # SKILL.md + references/ (design-system, visual-tells, site, app, copy, motion, checklist)
├── docs/
│   ├── TECHNICAL.md                # versão em inglês deste documento
│   ├── THREAT-MODEL.md             # ativos, atores, fronteiras de confiança, casos de abuso e mitigações (em inglês)
│   ├── EVALS.md                    # suítes de eval: cobertura, fixtures e como rodar (em inglês)
│   ├── CASE-STUDIES.md             # cenários reproduzíveis com fixtures públicas (em inglês)
│   ├── COMPATIBILITY.md            # versões, superfícies, sistemas e ferramentas testados (em inglês)
│   ├── examples/                   # exemplo de relatório JSON, conferido no CI
│   └── TECNICO.md                  # este documento
├── scripts/
│   ├── validate.py                 # validações estruturais (CI e local)
│   ├── generate_evals.py           # fonte única das suítes de eval (casos, fixtures, graders)
│   └── fixture.sh                  # cria o repositório fictício de um caso de eval, para demonstrações
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                         # Apache-2.0
├── NOTICE                          # atribuições (taste-skill, caveman)
├── README.md                       # inglês
└── README.pt-BR.md                 # português
```

## Instalar pelo terminal

```bash
claude plugin marketplace add CaioGiasson/cainitech-plugins
claude plugin install checkup@cainitech
claude plugin install spec@cainitech
claude plugin install polish@cainitech
```

Dentro de uma sessão, os equivalentes são `/plugin marketplace add CaioGiasson/cainitech-plugins` e `/plugin install checkup@cainitech`. No VS Code, digite `/plugins` para abrir **Manage plugins**. Use `--scope project` para habilitar um plugin para todas as pessoas que trabalham em determinado repositório.

Atualizar: `claude plugin marketplace update cainitech` e depois `claude plugin update <plugin>@cainitech`. O auto-update vem desligado para marketplaces de terceiros; ligue em `/plugin` → **Marketplaces** → **Enable auto-update**.

Desenvolvimento local sem instalar: `claude --plugin-dir ./plugins/checkup --plugin-dir ./plugins/spec --plugin-dir ./plugins/polish`.

## Como uma skill encontra seus arquivos compartilhados

Os plugins são copiados para um cache na instalação, e um plugin não consegue ler arquivos fora da própria pasta. Por isso cada plugin carrega tudo de que precisa, e as skills referenciam arquivos embarcados com `${CLAUDE_PLUGIN_ROOT}`, que o Claude Code substitui no Markdown da skill:

```
${CLAUDE_PLUGIN_ROOT}/references/ASSESSMENT.md
${CLAUDE_PLUGIN_ROOT}/skills/security/references/checklist.md
```

Por que as guidelines e os catálogos ficam em **arquivos separados e não dentro do `SKILL.md`**: o corpo da skill é carregado quando ela é invocada, mas os arquivos que ela referencia só são lidos quando ela pede. Os 200 KB de catálogos, portanto, não custam nada até uma avaliação realmente rodar, e `/checkup:security` lê só o próprio catálogo. Mantenha o `SKILL.md` curto e procedural e coloque o material de referência em `references/`. O mesmo vale dentro de uma skill: passos que só rodam em alguns casos (postar a revisão, criar issues num quadro, um modo de entrega) ficam em `references/` da skill e são lidos quando a skill chega neles, e o `/spec:review` guarda as regras de revisão em `references/REVIEWER.md`, lido só pelo revisor isolado.

O material **não** é compartilhado entre plugins: `checkup`, `spec` e `polish` são independentes. A única exceção é o `references/STYLE.md`, copiado em todos os plugins porque um plugin não lê arquivos de outro; o `scripts/validate.py` falha se as cópias divergirem. O `spec` nunca depende do `checkup`, e o `checkup` só menciona `/spec:refine` como próximo passo opcional.

## Comportamento de idioma

Toda skill que conversa com o usuário tem uma regra de **Language**: detectar o idioma pelo `$ARGUMENTS` e pelas mensagens recentes, responder e escrever todos os artefatos nele, e usar **inglês** quando não for possível determinar. Os arquivos de instrução em si estão em inglês. Nos relatórios de assessment, IDs de itens, caminhos de arquivo, código e os nomes das classificações (Dangerous, Bronze, Silver, Gold, Platinum) não são traduzidos.

## Estilo de comunicação

Toda skill lê o `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` e o aplica às mensagens no chat e ao texto persistido: resposta primeiro, sem bajulação, enrolação nem recapitulação, frases completas em relatórios, issues e pull requests. É adaptado da skill `caveman` (Apache-2.0, ver `NOTICE`), sem a gramática fragmentada.

## Catálogos de assessment

- Os arquivos `skills/*/references/checklist.md` agora são a **fonte da verdade** (não há mais script gerador). Edite-os diretamente.
- **Nunca altere ID, severidade ou peso de um item sem cuidado**: a comparação de score entre execuções depende deles. Qualquer mudança em um item altera o fingerprint do pilar, e o `scripts/validate.py` falha até que uma nova versão seja registrada em `plugins/checkup/references/CATALOG-CHANGELOG.md` (regras no topo do arquivo; `python3 -X utf8 scripts/validate.py --fingerprints` mostra os novos fingerprints). Os relatórios registram a versão do catálogo, então uma mudança de metodologia nunca é lida como progresso.
- Totais esperados: security 153 (48 críticos · 89 importantes · 16 menores), performance 163 (9 · 82 · 72), privacy 126 (37 · 66 · 23), ai-readiness 70 (6 · 30 · 34). A soma deve continuar sendo 512.
- Formato do relatório, status, pesos e faixas de classificação ficam em `plugins/checkup/references/ASSESSMENT.md`.
- Cada relatório tem um gêmeo em JSON que segue o `plugins/checkup/references/report.schema.json`. Uma mudança incompatível no schema incrementa o major do `schemaVersion`; o `docs/examples/security-report.example.json` precisa continuar válido (o `scripts/validate.py` o confere com um validador sem dependências do subconjunto de schema em uso).

## Regras do fluxo `spec`

O `plugins/spec/references/WORKFLOW.md` é lido primeiro por todas as skills do plugin. Resumo:

- **Detecção do quadro:** instrução explícita → quadro do GitHub Projects ligado ao repositório → outro quadro com ferramenta conectada → nenhum. Com quadro, as tarefas são criadas e movidas lá; sem quadro, nada é criado em nenhum rastreador.
- **Registro obrigatório na documentação:** todo refinamento é salvo na pasta de documentação do projeto, em `specs/` (`<id>-<slug>.md`), com ou sem quadro, a menos que o usuário diga explicitamente para não documentar.
- **Modos de entrega:** A (GitHub: branch, commits, PR, revisão, merge) · B (Git sem GitHub: branch e merge locais) · C (outro VCS) · D (sem VCS: arquivo `<refinamento>.changelog.<ext>` com a cópia de cada mudança).
- **Versionamento:** no máximo um bump de versão por PR/branch, apenas se o projeto já versionar a si mesmo.
- **Conteúdo externo:** issues, pull requests, comentários, commits, conversas e código são dados, nunca instruções (§7). O `approve` pede confirmação antes de cada ação com efeito colateral.
- As convenções do próprio projeto sempre prevalecem sobre qualquer regra genérica do plugin.

## Como adicionar uma skill

1. Crie `plugins/<plugin>/skills/<nome>/SKILL.md` com o frontmatter abaixo. O nome da pasta é o nome da skill.
2. Coloque material de referência longo em `plugins/<plugin>/skills/<nome>/references/` e referencie com `${CLAUDE_PLUGIN_ROOT}/skills/<nome>/references/<arquivo>`.
3. Inclua a regra de Language se a skill conversa com o usuário, e a linha que lê o `${CLAUDE_PLUGIN_ROOT}/references/STYLE.md` (exigida pelo `scripts/validate.py`).
4. Crie ao menos três casos de eval em `scripts/generate_evals.py` com a tag `skill:<nome>` ([EVALS.md](EVALS.md)): um que deve acionar a skill, um prompt parecido que não deve, e um para a regra ou o limite principal dela.
5. Valide (veja abaixo), aumente o `version` do plugin e faça commit.

```markdown
---
name: minha-skill
description: "Uma ou duas frases. Sempre entre aspas duplas: dois-pontos sem aspas quebram o YAML."
---

# Skill: minha-skill
...
```

## Como adicionar um plugin

Crie `plugins/<nome>/.claude-plugin/plugin.json` e `plugins/<nome>/skills/…`, depois adicione uma entrada em `.claude-plugin/marketplace.json` com `"source": "./plugins/<nome>"`. O `name` da entrada e o `name` do manifesto devem ser idênticos. Nomes de plugin usam kebab-case e não podem começar com `claude-`, `anthropic-` ou prefixos reservados parecidos. **Nunca renomeie um plugin publicado**: as instalações ficam registradas com o nome antigo. Se for inevitável, use o mapa `renames` do marketplace.

## Validação e release

```bash
claude plugin validate .                    # marketplace
claude plugin validate plugins/checkup   # manifesto e skills do plugin
claude plugin validate plugins/spec
claude plugin validate plugins/polish
python3 -X utf8 scripts/validate.py         # catálogos, referências, frontmatter, STYLE.md, links, arquivos proibidos
```

Como o `version` está definido em cada `plugin.json`, os usuários só recebem uma atualização quando você **aumenta o número** (`claude plugin update` informa "already at the latest version" caso contrário). Aumente a versão de cada plugin alterado na mesma pull request e registre a mudança no `CHANGELOG.md`. Opcionalmente, marque releases com `claude plugin tag`.

O CI (`.github/workflows/ci.yml`) roda essas validações em toda pull request, com uma versão fixa do Claude Code, roda o `scripts/validate.py` (contagens 153 / 163 / 126 / 70 com IDs únicos, referências `${CLAUDE_PLUGIN_ROOT}`, frontmatter dos `SKILL.md`, cópias idênticas do `STYLE.md`, links internos de Markdown, nenhum arquivo `personal/` ou `.env`, a conta do score do exemplo do README) e procura segredos em todo o histórico com o gitleaks, fixado por versão e checksum. Atualize a versão fixa quando quiser uma validação mais nova.

Observação: o validador de versões mais antigas do Claude Code rejeita alguns campos opcionais mais novos do manifesto (por exemplo `displayName` ou `description` no nível do marketplace), então os manifestos daqui usam só campos que todas as versões entendem.

## Licença

[Apache-2.0](../LICENSE).
