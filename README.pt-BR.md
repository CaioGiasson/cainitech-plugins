<p align="right"><a href="README.md">🇺🇸 English</a> · <b>🇧🇷 Português</b></p>

<div align="center">

# Seu Claude, com jeito de time

**Três plugins que ensinam o Claude a trabalhar como um time experiente: da ideia à tarefa, da tarefa ao código, do código à revisão, um check-up de toda a sua aplicação e bom gosto de design para os sites que ele constrói. Você pede em português. Ele entrega.**

<table>
<tr>
<td align="center" width="25%"><h3>3 plugins</h3>instale só o que precisa<br><sub><a href="#catálogo-de-skills">ver catálogo</a></sub></td>
<td align="center" width="25%"><h3>11 skills</h3>prontas para usar<br><sub><a href="#catálogo-de-skills">ver catálogo</a></sub></td>
<td align="center" width="25%"><h3>512 critérios</h3>avaliados no check-up completo<br><sub><a href="#check-up-do-sistema">ver detalhes</a></sub></td>
<td align="center" width="25%"><h3>1 mensagem</h3>para instalar, direto no chat<br><sub><a href="#como-instalar">ver instalação</a></sub></td>
</tr>
</table>

**[Valor](#por-que-isso-importa-para-o-negócio) · [Instalar](#como-instalar) · [Antes e depois](#antes-e-depois) · [Catálogo](#catálogo-de-skills) · [Como usar](#como-usar) · [Atualizar](#como-atualizar) · [Dúvidas](#dúvidas-comuns) · [Privacidade](#privacidade)**

</div>

---

## Por que isso importa para o negócio

**Menos retrabalho, entregas mais previsíveis e riscos descobertos antes de virarem incidente.** Os plugins transformam o jeito de trabalhar do seu time em algo que o Claude repete todo dia, para todo mundo.

| O problema do dia a dia | O que os plugins fazem | O que muda para o negócio |
|---|---|---|
| Pedidos vagos geram idas e vindas e retrabalho | Transformam ideias e conversas soltas em tarefas completas, com objetivo, regras e roteiro de testes | Menos dúvidas no meio do caminho e entregas mais fáceis de estimar |
| Cada pessoa trabalha de um jeito | Todo mundo segue o mesmo passo a passo e o mesmo padrão de qualidade | Qualidade previsível e entrada de novas pessoas mais rápida |
| Programar, testar e revisar consome o tempo do time | O Claude implementa, cria testes, se revisa e entrega um pedido de revisão pronto | O time gasta energia nas decisões, não nas tarefas repetitivas |
| Riscos de segurança, desempenho e LGPD aparecem tarde | Check-ups com nota de 0 a 100 e lista de problemas por prioridade | Você enxerga os riscos antes de virarem incidente e tem um plano de ação com ordem clara |
| O conhecimento fica na cabeça de poucas pessoas | Toda tarefa fica registrada na documentação do próprio projeto, com ou sem quadro de tarefas | Menos dependência de pessoas-chave |

**Para quem é:** gestores e líderes que querem previsibilidade, pessoas de produto que querem tarefas bem definidas e times de desenvolvimento que querem mais tempo para o que importa.

**Se adapta ao projeto que você tem:** usa o quadro de tarefas do GitHub quando existe, funciona sem GitHub e, se o projeto não tem nenhum controle de versão, mantém um registro simples das mudanças. Responde no idioma em que você escreve.

## Antes e depois

<table>
<tr>
<th width="50%">Sem os plugins</th>
<th width="50%">Com os plugins</th>
</tr>
<tr>
<td valign="top">

> "Precisamos de um jeito de baixar a fatura."

Uma frase solta. Cada pessoa entende de um jeito, o desenvolvedor faz perguntas por dias e o resultado depende de quem pegou a tarefa.

</td>
<td valign="top">

> Tarefa completa: objetivo, regras, o que mudar, como testar — no seu quadro e na sua documentação. Código pronto para revisão e um roteiro de testes na mão.

O Claude estuda o sistema, pergunta só o que falta e entrega no padrão do time.

</td>
</tr>
</table>

<sub>Exemplo ilustrativo do tipo de resultado que cada skill produz.</sub>

**Mesma ideia. Entrega organizada, no padrão do time.**

## Como instalar

Você não precisa aprender comandos. Precisa do **aplicativo Claude** (aba **Code**). Se faltar mais alguma coisa, o próprio Claude avisa e te guia.

1. Abra o aplicativo Claude e entre na aba **Code**.
2. Cole esta mensagem no chat e envie:

   > Instale os plugins do marketplace CaioGiasson/cainitech-plugins: rode `claude plugin marketplace add CaioGiasson/cainitech-plugins`, depois `claude plugin install checkup@cainitech`, `claude plugin install spec@cainitech` e `claude plugin install design@cainitech`, e me avise quando terminar.

3. Espere o Claude confirmar e abra uma **nova conversa**. As skills já aparecem quando você digita `/`.

Uma mensagem. Só isso. Quer só os check-ups, só o fluxo de tarefas ou só as regras de design? Peça apenas o `checkup`, o `spec` ou o `design`.

**Prefere clicar?** Com o marketplace adicionado (passo 2), clique no botão **+** ao lado da caixa de mensagem, escolha **Plugins** e depois **Add plugin** para instalar, ou **Manage plugins** para ligar, desligar, atualizar ou remover um plugin.

<sub>Prefere o terminal ou o VS Code? Veja a <a href="docs/TECNICO.md">documentação técnica</a>.</sub>

## Como atualizar

Quando sair uma nova versão, abra **+ → Plugins → Manage plugins**, escolha o plugin e clique em **Update now**. Ou envie esta mensagem ao Claude na aba **Code**:

> Atualize os plugins da cainitech: rode `claude plugin marketplace update cainitech`, depois `claude plugin update checkup@cainitech`, `claude plugin update spec@cainitech` e `claude plugin update design@cainitech`.

Skills novas e melhorias chegam na hora (abra uma nova conversa para carregá-las).

## Como usar

Em qualquer conversa na aba **Code**, digite `/` e escolha a skill na lista. As skills de um plugin aparecem como `/<plugin>:<skill>`. Depois escreva o que precisa em português normal.

> `/spec:refine` Quero que o cliente consiga baixar a fatura em PDF na tela de pagamentos.

Se preferir, só descreva o que quer. O Claude também sugere a skill certa.

> As skills respondem no idioma em que você escreve. Se não conseguirem identificar, usam inglês.

## Catálogo de skills

Onze skills em três plugins. Cada uma diz o que faz e qual resultado você recebe.

| Plugin | Grupo | Para que serve | Skills |
|---|---|---|---|
| **`spec`** | **[Da ideia à tarefa](#da-ideia-à-tarefa-pronta)** | Transformar conversa solta em tarefa clara e registrada | `/spec:from-thread` · `/spec:refine` |
| **`spec`** | **[Do código à entrega](#do-código-à-entrega)** | Programar, revisar e finalizar | `/spec:build` · `/spec:review` · `/spec:approve` |
| **`checkup`** | **[Check-up do sistema](#check-up-do-sistema)** | Medir a saúde do projeto, sem alterar nada | `/checkup:security` · `/checkup:performance` · `/checkup:privacy` · `/checkup:ai-readiness` · `/checkup:full` |
| **`design`** | **[Design de sites](#design-de-sites)** | Criar ou revisar páginas que não pareçam feitas por IA | `/design:frontend` |

**O caminho completo de uma tarefa:** `/spec:from-thread` ou `/spec:refine` → `/spec:build` → `/spec:review` → você testa → `/spec:approve`.

### Da ideia à tarefa pronta

| Skill | O que faz | O que você recebe |
|---|---|---|
| **`/spec:from-thread`** | Lê uma conversa informal (link de thread do Slack, link do Discord ou arquivo `.md`), ignora o ruído e separa decisões de dúvidas e opiniões. | Uma tarefa refinada, registrada na documentação do projeto e, se houver quadro de tarefas no GitHub, criada lá — sem piadas, gírias nem informações soltas. |
| **`/spec:refine`** | Pega uma ideia descrita em poucas linhas, estuda o sistema, faz perguntas objetivas e detalha tudo. | Uma tarefa completa (objetivo, regras, o que mudar e como testar), clara o bastante para qualquer pessoa executar. Ela é **sempre registrada na documentação do projeto**; se houver quadro, também é criada lá, com uma sub-tarefa para cada sistema envolvido. |

### Do código à entrega

| Skill | O que faz | O que você recebe |
|---|---|---|
| **`/spec:build`** | Recebe uma tarefa, move no quadro para "Em andamento" (se houver quadro), programa a solução, cria os testes e se revisa sozinha. | No GitHub: uma *pull request* (pedido de revisão) pronta, com o código em etapas organizadas e um roteiro de testes para você conferir. Sem GitHub: commits locais organizados. Sem controle de versão: um arquivo de registro com a cópia de cada mudança. |
| **`/spec:review`** | Revisa uma mudança: confere se tudo o que foi pedido foi feito, roda os testes e analisa a qualidade do código. | Comentários de revisão publicados no trecho certo do código, depois que você escolhe o que postar (sem GitHub, a revisão vem no chat). Só corrige algo se você pedir. |
| **`/spec:approve`** | Entra depois dos seus testes manuais e faz a última revisão antes de finalizar. | Se estiver tudo certo: no GitHub, comentário final, marcação "Reviewed", entrega concluída (*merge*) e limpeza das cópias de trabalho; sem GitHub, um merge local. Se achar problema sério, apenas avisa você e não mexe em nada. |

### Check-up do sistema

**Só leem e avaliam. Não alteram nada no seu projeto.** Cada check-up entrega um relatório com **nota de 0 a 100**, uma **classificação** e uma **lista de problemas por prioridade**, pronta para virar plano de ação. O relatório fica salvo na pasta `docs/checkups` do projeto avaliado.

| Skill | O que avalia | Critérios | O que você recebe |
|---|---|---:|---|
| **`/checkup:security`** | Segurança: login, proteção de dados, brechas conhecidas, segredos expostos. Serve de preparação para um teste de invasão. | 153 | Nota de segurança e pontos fracos por gravidade. |
| **`/checkup:performance`** | Velocidade, capacidade de crescer, estabilidade e custos de infraestrutura. | 163 | Onde o sistema fica lento ou caro e o que priorizar. |
| **`/checkup:privacy`** | Conformidade com a LGPD: consentimento, direitos dos titulares, guarda de dados pessoais. | 126 | Lacunas legais, cada uma ligada ao artigo da lei. |
| **`/checkup:ai-readiness`** | Quão preparado o projeto está para ser desenvolvido com ajuda de IA: documentação, testes, organização. | 70 | O que melhorar para a IA trabalhar mais rápido e errar menos. |
| **`/checkup:full`** | Os quatro check-ups de uma vez. | 512 | Os quatro relatórios mais um geral, com nota única, riscos que atravessam as áreas e uma lista única de prioridades. |

Como ler a nota:

| Nota | Classificação |
|---|---|
| 90 a 100 | 🏆 Platinum |
| 70 a 89 | 🥇 Gold |
| 50 a 69 | 🥈 Silver |
| 25 a 49 | 🥉 Bronze |
| 0 a 24 | 🚨 Dangerous |

### Design de sites

**Só regras: não roda comandos nem baixa nada.** Neutra: não traz marca nem design system próprio, e o design system do seu projeto sempre prevalece.

| Skill | O que faz | O que você recebe |
|---|---|---|
| **`/design:frontend`** | Cria, redesenha ou revisa um site ou landing page: o tipo de negócio define o plano da página, uma seção por tela, bordas iguais, texto direto sem os vícios de escrita de IA, movimento discreto. Acrescente `review` para só avaliar uma página. | Uma página com cara de empresa profissional, mais um relatório com cada dado assumido e cada foto ou material que o cliente ainda precisa enviar. No modo `review`, um checklist do que falha e como corrigir. |

<sub>Adaptado do <a href="https://github.com/Leonxlnx/taste-skill">taste-skill</a> (MIT), sem os scripts, hooks e downloads dele.</sub>

## Como é o resultado de um check-up

Exemplo **com dados fictícios** de um `/checkup:security` em um projeto chamado `loja-online`. É a resposta que aparece no chat; o relatório completo é salvo em arquivo.

```text
# Score Security: 56,1 / 100 — Silver

63 compliant · 28 parciais · 46 não compliant · 16 N/A (153 critérios)
Evolução: primeira execução

🔴 Críticos não compliant (14):
  SEC-2.04 · Brute force, credential stuffing e evasão de rate limit
  SEC-2.05 · MFA
  SEC-2.08 · Recovery
  SEC-3.02 · BOLA/IDOR
  SEC-5.06 · XSS
  … e mais 9 (lista completa no relatório)
🟠 Top 5 do backlog por ganho no score:
  SEC-3.02 · Validar dono do pedido em todas as rotas /orders · +1,0 pt
  SEC-2.04 · Rate limit por conta e por IP no login · +1,0 pt
  SEC-2.08 · Token de recuperação de uso único e com expiração · +1,0 pt
  SEC-2.05 · Oferecer MFA para contas administrativas · +1,0 pt
  SEC-5.06 · Sanitizar o campo de comentário do produto · +1,0 pt

📄 Relatório: docs/checkups/2026-10-14-security.md
```

<details>
<summary><b>Ver um trecho do relatório salvo em arquivo</b></summary>

````markdown
# Score: 56,1 / 100
## Classificação: Silver

# Assessment de Security — loja-online

| Campo | Valor |
|---|---|
| Data | 2026-10-14 |
| Commit avaliado | `a3f9c21` (branch `main`) |
| Catálogo | application-assessment v3 — 153 itens (137 aplicáveis, 16 N/A) |
| Escopo | API Node.js + Next.js + MongoDB; app mobile e LLM fora do escopo (N/A) |
| Execução anterior | primeira execução |

## Resumo

| Severidade | Compliant | Parcial | Não compliant | N/A | Pontos obtidos / possíveis |
|---|---:|---:|---:|---:|---:|
| Crítico | 20 | 9 | 14 | 5 | 73,5 / 129 |
| Importante | 36 | 17 | 28 | 8 | 89 / 162 |
| Menor | 7 | 2 | 4 | 3 | 8 / 13 |
| **Total** | 63 | 28 | 46 | 16 | **170,5 / 304 = 56,1** |

Principais riscos: qualquer cliente logado consegue ver pedidos de outros clientes
trocando o número na URL; o login não limita tentativas, o que permite adivinhar
senhas; contas administrativas não exigem segundo fator.

## 1. Itens não compliant

### 1.1 Críticos

#### SEC-3.02 · BOLA/IDOR — Crítico · Não compliant

- **Critério:** toda rota que recebe o identificador de um objeto confirma, no servidor, que o usuário autenticado tem direito a ele.
- **Situação encontrada:** as rotas de pedidos buscam o registro só pelo `id`, sem comparar com o usuário logado.
- **Motivo do status:** o controle não existe e não há teste negativo (ASSESSMENT §2 e §3).
- **Evidência:** `src/modules/orders/orders.controller.ts:58` — `orders.findById(req.params.id)` sem filtro por `userId`; busca `rg "findById\(req.params" src/` → 6 ocorrências, 5 sem verificação de dono.
- **Componentes afetados:** `GET /orders/:id`, `PATCH /orders/:id`, `GET /orders/:id/invoice` e outras 3 rotas.
- **Impacto / risco:** um cliente autenticado percorre ids sequenciais e lê nome, endereço e itens de pedidos de terceiros (vazamento de dados pessoais, com impacto na LGPD).
- **Recomendação:** buscar sempre por `{ id, userId }` na camada de repositório e responder 404 quando não encontrar. Adicionar teste em que o usuário A tenta ler o pedido do usuário B e recebe 404.
- **Critério de reteste:** teste negativo de acesso cruzado existe e passa no CI para todas as rotas listadas.
- **Esforço estimado:** P (≤ 1 dia)
- **Referências:** SEC-3.02 · OWASP API Security Top 10 (API1 — BOLA)

## 5. Backlog sugerido

| Prioridade | ID | Título da tarefa | Severidade | Esforço | Ganho no score |
|---:|---|---|---|---|---:|
| 1 | SEC-3.02 | Validar dono do pedido em todas as rotas `/orders` | Crítico | P | +1,0 |
| 2 | SEC-2.04 | Rate limit por conta e por IP no login | Crítico | P | +1,0 |
| 3 | SEC-2.08 | Token de recuperação de uso único e com expiração | Crítico | P | +1,0 |
| 4 | SEC-2.05 | Oferecer MFA para contas administrativas | Crítico | M | +1,0 |

*(…demais seções omitidas neste exemplo)*
````

</details>

Depois do relatório, o Claude oferece transformar os itens do backlog em tarefas com `/spec:refine`, se o plugin `spec` estiver instalado.

## Antes de usar as skills de tarefas

As skills `/spec:*` usam o **quadro de tarefas do GitHub** quando o projeto tem um, pela conexão com o GitHub que você já tiver (ou pelo GitHub CLI, `gh`). Se algo pedir acesso, é só aprovar quando o Claude perguntar. Sem quadro? Elas registram tudo na documentação do projeto e continuam funcionando. Sem GitHub, ou sem nenhum controle de versão? Elas se adaptam (commits locais, ou um arquivo de registro das mudanças).

## Dúvidas comuns

**Preciso saber programar?** Não para instalar nem para usar o refinamento de tarefas e os check-ups.

**As skills mudam meu projeto sem avisar?** Os check-ups nunca alteram nada. As demais mostram o que vão fazer e pedem confirmação nas decisões importantes.

**Onde o trabalho fica registrado?** Sempre na pasta de documentação do projeto (em `docs/specs/`), com ou sem quadro de tarefas. A única forma de pular o registro é dizer explicitamente ao Claude para não documentar.

**A skill não apareceu na lista.** Abra uma nova conversa depois de instalar ou atualizar.

**Quero criar ou editar skills, ou entender a estrutura de pastas.** Veja a [documentação técnica](docs/TECNICO.md).

## Ferramentas recomendadas

Ferramentas opcionais que fazem os plugins funcionarem melhor. Nenhuma é obrigatória.

| Ferramenta | Ajuda em | Observações |
|---|---|---|
| **[GitHub CLI (`gh`)](https://cli.github.com)** | As skills `/spec:*`: ler e criar issues, mover cards no quadro, abrir e mesclar pull requests | Instale e entre com `gh auth login`. Para mover cards no quadro, rode também `gh auth refresh -s project`. Sem ele, o `spec` continua funcionando pelos modos alternativos. Um conector do GitHub (MCP) também serve. |
| **Conector do Slack ou do Discord** | `/spec:from-thread`, que lê uma conversa a partir de um link | Sem um deles, cole a conversa em um arquivo `.md` e informe o caminho do arquivo ao Claude. |
| **[Caveman](https://github.com/JuliusBrussee/caveman)** | Fazer o Claude responder com menos palavras, para economizar tokens | Totalmente opcional e **não testado com estes plugins**. Segundo o README dele, só a skill (`npx skills add JuliusBrussee/caveman -g`) não envia nada, enquanto o CLI envia estatísticas de uso por padrão; por isso, instale só a skill se privacidade for importante para você. O estilo dele privilegia respostas muito curtas: teste antes de depender dele, já que os relatórios e as tarefas do `checkup` e do `spec` seguem modelos fixos e detalhados. |

## Privacidade

- Os plugins são só arquivos de texto (instruções para o Claude). Instalá-los **copia** esses arquivos para o seu computador e não executa código próprio.
- As skills rodam dentro do seu Claude, com a sua conta e as suas permissões.
- As skills `/spec:*` leem e escrevem no GitHub (e na pasta do seu projeto) porque esse é o trabalho delas, sempre com a sua conta.

## Licença

[Apache-2.0](LICENSE). Uso, cópia e adaptação livres, inclusive comerciais, mantendo o aviso da licença.

---

<div align="center">

**Um time, um jeito de trabalhar. Cada pessoa com o seu Claude.**

<sub>
<a href="docs/TECNICO.md">Documentação técnica</a> ·
<a href="https://github.com/CaioGiasson/cainitech-plugins/issues">Issues</a>
</sub>

</div>
