# Codex Skillforge

Coleção de skills para desenvolvimento, arquitetura, revisão, design e acompanhamento de trabalho no Obsidian.

## Catálogo

A coleção contém **26 skills**. Os nomes abaixo são os declarados no frontmatter; algumas pastas preservam os nomes usados pela instalação local.

| Skill | Pasta | Finalidade |
|---|---|---|
| `apple-design` | [`apple-design`](skills/apple-design/SKILL.md) | Gestos, movimento e princípios de interface Apple para a web |
| `brandkit` | [`brandkit`](skills/brandkit/SKILL.md) | Identidade visual, sistemas de logo e apresentações de marca |
| `industrial-brutalist-ui` | [`brutalist-skill`](skills/brutalist-skill/SKILL.md) | Interfaces de estética industrial e brutalista |
| `vercel-composition-patterns` | [`composition-patterns`](skills/composition-patterns/SKILL.md) | Composição e APIs de componentes React |
| `context7-docs` | [`context7-docs`](skills/context7-docs/SKILL.md) | Documentação alinhada à versão da biblioteca |
| `conventional-commits` | [`conventional-commits`](skills/conventional-commits/SKILL.md) | Planejamento e validação de commits atômicos |
| `coupling-analysis` | [`coupling-analysis`](skills/coupling-analysis/SKILL.md) | Análise de acoplamento entre módulos |
| `domain-analysis` | [`domain-analysis`](skills/domain-analysis/SKILL.md) | Domínios e limites de serviços com DDD |
| `gh-address-comments` | [`gh-address-comments`](skills/gh-address-comments/SKILL.md) | Feedback de revisão em pull requests |
| `gpt-taste` | [`gpt-tasteskill`](skills/gpt-tasteskill/SKILL.md) | Composição visual e animação com GSAP |
| `image-to-code` | [`image-to-code-skill`](skills/image-to-code-skill/SKILL.md) | Implementação de interface orientada por imagens de referência |
| `imagegen-frontend-mobile` | [`imagegen-frontend-mobile`](skills/imagegen-frontend-mobile/SKILL.md) | Conceitos visuais de telas e fluxos móveis |
| `imagegen-frontend-web` | [`imagegen-frontend-web`](skills/imagegen-frontend-web/SKILL.md) | Referências visuais de páginas por seção |
| `minimalist-ui` | [`minimalist-skill`](skills/minimalist-skill/SKILL.md) | Interfaces editoriais minimalistas |
| `mui-template-frontend` | [`mui-template-frontend`](skills/mui-template-frontend/SKILL.md) | Templates oficiais e gratuitos do Material UI |
| `obsidian-workflow` | [`obsidian-workflow`](skills/obsidian-workflow/SKILL.md) | Vault, seis módulos técnicos, registro e acompanhamento |
| `vercel-react-best-practices` | [`react-best-practices`](skills/react-best-practices/SKILL.md) | Desempenho e boas práticas em React/Next.js |
| `redesign-existing-projects` | [`redesign-skill`](skills/redesign-skill/SKILL.md) | Auditoria e evolução visual de interfaces existentes |
| `security-audit` | [`security-audit`](skills/security-audit/SKILL.md) | Auditoria defensiva oficial da Cloudflare |
| `senior-fullstack-mentor` | [`senior-fullstack-mentor`](skills/senior-fullstack-mentor/SKILL.md) | Mentoria, execução autorizada e validação full-stack |
| `high-end-visual-design` | [`soft-skill`](skills/soft-skill/SKILL.md) | Diretrizes para qualidade visual |
| `stitch-design-taste` | [`stitch-skill`](skills/stitch-skill/SKILL.md) | Design semântico para Google Stitch |
| `design-taste-frontend` | [`taste-skill`](skills/taste-skill/SKILL.md) | Direção visual para páginas e redesigns |
| `technical-design-doc-creator` | [`technical-design-doc-creator`](skills/technical-design-doc-creator/SKILL.md) | Documentos de projeto técnico e decisões de arquitetura |
| `tlc-spec-driven` | [`tlc-spec-driven`](skills/tlc-spec-driven/SKILL.md) | Requisitos, planejamento e implementação guiados por especificação |
| `web-design-guidelines` | [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Revisão de interface e acessibilidade |

## Instalação e atualização local

Copie a pasta completa de cada skill desejada para o diretório de skills do seu agente, incluindo scripts, referências, assets e licenças. Compare versões e preserve alterações locais antes de substituir um pacote. Publicar no GitHub não instala nem atualiza as skills globais automaticamente.

Para Obsidian, copie somente `skills/obsidian-workflow/`: ela já inclui os seis módulos técnicos e não depende das antigas skills separadas. As versões globais existentes não são removidas por este repositório. Se migrar sua instalação para a unificada, revise referências e atalhos antigos antes de desativar qualquer pacote anterior.

A obrigatoriedade de registro aplica-se a trabalho relevante e autorizado, proporcional à necessidade do usuário. A skill preserva notas manuais, evita duplicação, mantém evidências e pendências e respeita a preferência de não registrar. Não agenda acompanhamento automaticamente. A seleção automática da skill depende do agente; o pacote não altera instruções globais ou configurações de ativação.

## Origem e licenças

As versões locais selecionadas foram preservadas, com suas referências e ferramentas. O [manifesto da coleção](COLLECTION-MANIFEST.json) registra hashes dos arquivos locais e fontes de atribuição. O commit upstream consultado não é apresentado como revisão original de uma instalação cuja origem exata não foi estabelecida.

- Pacotes Tech Leads Club: conteúdo de skills sob CC-BY-4.0 e software sob MIT, conforme licença incluída e atribuição em cada pacote.
- Pacotes Leonxlnx, Emil Kowalski, Vercel e módulos de Steph Ango: MIT, com autoria preservada nos avisos de cada pacote. A declaração MIT de Vercel está no README upstream; o aviso incluído materializa esses termos.
- `gh-address-comments`: Apache-2.0, com licença original preservada.
- `security-audit`: pacote Cloudflare sob MIT; a revisão incorporada está em seu UPSTREAM.md.

A coleção tem licenças por componente; nenhuma licença única foi aplicada sobre todos os conteúdos. Mudanças de empacotamento são identificadas nos respectivos avisos. Este pacote não inclui templates premium do Material UI.

## Validação

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
node --test skills/security-audit/validate-findings.test.cjs skills/security-audit/validate-coverage-ledger.test.cjs
```

O validador local usa apenas a biblioteca padrão Python. Verifica estrutura, campos básicos do frontmatter (incluindo descrições multilinha), nomes duplicados, referências Markdown fora de exemplos de código e metadados de invocação. Não é um parser YAML completo nem comprova comportamento em execução.

A unificada contém [cenários de aceitação](skills/obsidian-workflow/references/behavior-scenarios.md) para revisão de comportamento. A validação oficial de autoria usa PyYAML; nesta rodada foi disponibilizado somente em diretório temporário.

## Limites operacionais

- `security-audit` exige os controles de sandbox e delegação definidos pelo pacote para o fluxo completo. Recursos ausentes são bloqueios de validação.
- `context7-docs` não instala nem configura o MCP; sem conexão utiliza documentação oficial e explicita a limitação.
- Obsidian CLI, Defuddle e Knap são ferramentas opcionais que precisam estar disponíveis para seus comandos. A edição direta de arquivos do vault é uma alternativa quando compatível.
- As skills visuais podem exigir ferramentas de imagem, navegador ou stack específicas; publicar os arquivos não disponibiliza essas ferramentas.

Testes estruturais e dos validadores não comprovam validação autenticada, renderização no aplicativo ou execução real de todas as skills. As pesquisas seguintes estão no [backlog](BACKLOG.md).
