# Codex Skills Kit

Colecao de skills reutilizaveis para desenvolvimento de software, qualidade visual e historico Git.

## Skills incluidas

| Skill | Finalidade |
|---|---|
| `senior-fullstack-mentor` | Planejamento, ensino, implementacao autorizada e validacao full-stack |
| `conventional-commits` | Planejamento e validacao de commits atomicos no padrao Conventional Commits 1.0.0 |
| `design-taste-frontend` | Direcao visual anti-generica para landing pages, portfolios e redesigns |
| `mui-template-frontend` | Selecao e adaptacao dos templates React oficiais e gratuitos do Material UI |

| `security-audit` | Auditoria defensiva oficial da Cloudflare, com evidencias e validadores |
| `context7-docs` | Documentacao de bibliotecas alinhada a versao do projeto |

## Estrutura

```text
codex-skills-kit/
|-- README.md
|-- .gitignore
|-- scripts/
|   `-- validate_skills.py
`-- skills/
    |-- context7-docs/
    |-- security-audit/
    |-- conventional-commits/
    |-- mui-template-frontend/
    |-- senior-fullstack-mentor/
    `-- taste-skill/
```

O nome da pasta `taste-skill` foi preservado para manter compatibilidade com a instalacao atual; o nome declarado em seu `SKILL.md` e `design-taste-frontend`.

## Instalacao local

Copie apenas as pastas desejadas de `skills/` para o diretorio de skills do Codex. Cada skill e autocontida e possui um `SKILL.md` na raiz.

Antes de substituir uma skill ja instalada, compare as versoes e preserve alteracoes locais.

## Validacao

```bash
python3 scripts/validate_skills.py
python3 skills/conventional-commits/scripts/validate_commit_message.py \
  --message 'feat(skills): add reusable Codex skill collection'
```

O primeiro comando verifica estrutura, frontmatter, placeholders e links locais. O segundo valida a estrutura portavel de uma mensagem Conventional Commits.

## Fontes e limites

A skill `mui-template-frontend` aponta para o [catalogo oficial do Material UI](https://mui.com/material-ui/getting-started/templates/) e para o repositorio [`mui/material-ui`](https://github.com/mui/material-ui). Ela nao incorpora os templates premium da MUI Store e nao congela uma copia do codigo dos templates gratuitos.

Este pacote nao cria commits, nao publica no GitHub e nao escolhe uma licenca para o repositorio automaticamente. Antes da publicacao, o mantenedor deve revisar a autoria e definir a licenca apropriada para cada conteudo.

## Atualizacao de 2026-10-21

A skill mentor foi sincronizada com a instalacao local: profundidade adaptativa, exploracao de alternativas, representacao de arquitetura, experimentos e tecnologias desconhecidas. As outras tres skills existentes ja coincidiam com a instalacao e foram preservadas.

A skill `security-audit` e uma copia completa do upstream Cloudflare, com licenca MIT e commit em `skills/security-audit/UPSTREAM.md`. Copie sua pasta inteira, incluindo os validadores e companions. Seu workflow completo depende de delegacao e sandbox com os controles exigidos pelo proprio pacote; capacidades ausentes devem aparecer como bloqueios de validacao.

A skill `context7-docs` nao instala nem configura o servico. Quando as ferramentas nao estiverem conectadas, utiliza documentacao oficial e declara a limitacao.

Validacao adicional do pacote Cloudflare (Node.js):

```bash
node --test skills/security-audit/validate-findings.test.cjs skills/security-audit/validate-coverage-ledger.test.cjs
```

Esses testes verificam os validadores; nao comprovam uma auditoria real ou acesso autenticado ao Context7. Consulte [BACKLOG.md](BACKLOG.md) para as pesquisas seguintes.
