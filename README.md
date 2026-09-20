# Codex Skills Kit

Colecao de skills reutilizaveis para desenvolvimento de software, qualidade visual e historico Git.

## Skills incluidas

| Skill | Finalidade |
|---|---|
| `senior-fullstack-mentor` | Planejamento, ensino, implementacao autorizada e validacao full-stack |
| `conventional-commits` | Planejamento e validacao de commits atomicos no padrao Conventional Commits 1.0.0 |
| `design-taste-frontend` | Direcao visual anti-generica para landing pages, portfolios e redesigns |
| `mui-template-frontend` | Selecao e adaptacao dos templates React oficiais e gratuitos do Material UI |

## Estrutura

```text
codex-skills-kit/
|-- README.md
|-- .gitignore
|-- scripts/
|   `-- validate_skills.py
`-- skills/
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
