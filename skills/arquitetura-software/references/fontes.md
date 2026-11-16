# Base bibliográfica e protocolo de pesquisa

Data da consulta: 16/11/2026. Idioma da síntese: português brasileiro.

## Método e limites

Esta é uma revisão narrativa ampla e dirigida à prática, não uma revisão sistemática com protocolo exaustivo. Foram priorizadas fontes de autores, editoras, universidades, sociedades científicas e documentação oficial. O conjunto abaixo contém 36 entradas: dez livros/referências de livros, dez trabalhos científicos ou relatórios técnicos e dezesseis guias, padrões e recursos didáticos.

“Consulta parcial” significa descrição editorial, índice, resumo ou seções selecionadas; não leitura integral. “Texto aberto” significa que o conteúdo está disponível na fonte, não que todas as páginas tenham sido lidas. Não incluir cópias de livros ou textos integrais de terceiros. Não alegar que esta pesquisa altera permanentemente o treinamento do modelo: a especialização resulta das instruções e referências carregadas durante a tarefa.

Usar as fontes para fundamentar conceitos, não para provar que uma arquitetura específica atende a requisitos sem medição. Os exemplos, templates e recomendações operacionais deste pacote são síntese própria. Quando retomados, aprofundar a fonte relevante e verificar detalhes que dependam de versão ou contexto.

## Livros e referências de livros

| ID | Obra e autoria | Material consultado e acesso | Uso principal |
| --- | --- | --- | --- |
| B01 | Mark Richards; Neal Ford. *Fundamentals of Software Architecture*, 2ª ed., 2025 | [Editora: descrição e sumário](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/). Consulta parcial; livro completo comercial | Mapa de fundamentos, estilos e decisões |
| B02 | Len Bass; Paul Clements; Rick Kazman. *Software Architecture in Practice*, 4ª ed., 2021 | [Editora: descrição e sumário](https://www.oreilly.com/library/view/software-architecture-in/9780136885979/); [curso do SEI](https://sei.cmu.edu/training/software-architecture-principles-practices/). Consulta parcial | Qualidades, estruturas e avaliação |
| B03 | Neal Ford; Mark Richards; Pramod Sadalage; Zhamak Dehghani. *Software Architecture: The Hard Parts*, 2021 | [Editora: descrição e sumário](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/). Consulta parcial | Decomposição, granularidade e dados |
| B04 | Martin Kleppmann. *Designing Data-Intensive Applications*, 1ª ed., 2017 | [Site do autor](https://dataintensive.net/); [sumário da edição](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). Consulta parcial. Esta entrada identifica a edição usada, não afirma ser a mais recente | Dados e garantias distribuídas |
| B05 | Eric Evans. *Domain-Driven Design: Tackling Complexity in the Heart of Software*, publicação em 2003/copyright 2004 | [DDD Reference do autor](https://www.domainlanguage.com/ddd/reference/): descrição indexada consultada; abertura direta retornou 403, PDF não lido. [Exposição de Martin Fowler](https://martinfowler.com/bliki/DomainDrivenDesign.html) consultada | Linguagem, contexto e modelagem. Distinguir fonte do autor e explicação complementar |
| B06 | Martin Fowler e colaboradores. *Patterns of Enterprise Application Architecture*, 2002 | [Página do autor](https://martinfowler.com/books/eaa.html). Descrição e escopo consultados, não livro integral | Organização da lógica e persistência |
| B07 | Gregor Hohpe; Bobby Woolf. *Enterprise Integration Patterns*, 2003 | [Site dos autores e catálogo](https://www.enterpriseintegrationpatterns.com/). Catálogo e tópicos consultados | Vocabulário de integração e mensagens |
| B08 | Sam Newman. *Building Microservices*, 2ª ed., 2021 | [Página do autor](https://samnewman.io/books/building_microservices_2nd_edition/). Consulta parcial | Custos e operação de serviços independentes |
| B09 | Neal Ford; Rebecca Parsons; Patrick Kua; Pramod Sadalage. *Building Evolutionary Architectures*, 2ª ed. | [Editora: descrição e sumário](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/). Consulta parcial | Evolução e fitness functions |
| B10 | Betsy Beyer; Chris Jones; Jennifer Petoff; Niall Richard Murphy, editores. *Site Reliability Engineering*, 2016 | [Capítulo aberto sobre objetivos de serviço](https://sre.google/sre-book/service-level-objectives/). Seções de SLI/SLO/SLA consultadas | Qualidade operacional e medição |

## Trabalhos científicos e relatórios técnicos

| ID | Publicação | Evidência consultada | Contribuição e limite |
| --- | --- | --- | --- |
| P01 | D. L. Parnas. *On the Criteria To Be Used in Decomposing Systems into Modules*. CACM 15(12), 1053–1058, 1972 | [DOI 10.1145/361598.361623](https://doi.org/10.1145/361598.361623), resumo e metadados | Critérios de decomposição; não oferece uma métrica universal de qualidade |
| P02 | David Garlan; Mary Shaw. *An Introduction to Software Architecture*. 1993; relatório CMU-CS-94-166, 1994 | [Página dos autores](https://www.cs.cmu.edu/~able/publications/intro_softarch/); [PDF aberto](https://www.cs.cmu.edu/afs/cs/project/able/ftp/intro_softarch/intro_softarch.pdf), introdução e organização consultadas | Estilos e organização global; terminologia histórica exige contextualização |
| P03 | Seth Gilbert; Nancy Lynch. *Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. SIGACT News, 2002 | [PDF hospedado pelo autor](https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf), modelo e definições consultados; DOI 10.1145/564585.564601 | Limite formal sob partições; definições não equivalem a qualquer uso comercial de “disponível” |
| P04 | Leslie Lamport. *Time, Clocks, and the Ordering of Events in a Distributed System*. CACM, 1978 | [Página do autor na Microsoft Research](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/) e material indexado do paper; DOI 10.1145/359545.359563 | Causalidade e ordenação; timestamps físicos não provam causalidade |
| P05 | Michael J. Fischer; Nancy A. Lynch; Michael S. Paterson. *Impossibility of Distributed Consensus with One Faulty Process*. MIT-LCS-TR-282, 1982 | [Repositório institucional do MIT](https://dspace.mit.edu/entities/publication/287e7d14-a6f3-4ab4-b21a-a98ea86c1212), resumo consultado. Esta entrada é do relatório, não da publicação de periódico de 1985 | Impossibilidade sob hipóteses formais; não impede consenso prático |
| P06 | Diego Ongaro; John Ousterhout. *In Search of an Understandable Consensus Algorithm*. USENIX ATC, 305–319, 2014 | [Publicação original e resumo](https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro) | Consenso de log e compreensibilidade; não substitui análise da implantação |
| P07 | John D. C. Little. *A Proof for the Queuing Formula: L = λW*. Operations Research 9(3), 383–387, 1961 | [Publicação original INFORMS](https://pubsonline.informs.org/doi/epdf/10.1287/opre.9.3.383), resumo indexado consultado | Relação entre médias em filas; não usar como dimensionamento completo nem confundir média com pico |
| P08 | Jeffrey Dean; Luiz André Barroso. *The Tail at Scale*. CACM 56, 74–80, 2013 | [Google Research](https://research.google/pubs/the-tail-at-scale/), resumo consultado | Latência de cauda; resultados em larga escala não são requisito automático para todo produto |
| P09 | Rick Kazman; Mark Klein; Paul Clements. *ATAM: Method for Architecture Evaluation*. CMU/SEI-2000-TR-004, 2000 | [Relatório SEI](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/) e [PDF](https://www.sei.cmu.edu/documents/629/2000_005_001_13706.pdf). Resumo consultado; PDF localizado, sem leitura integral | Avaliar compromissos e riscos; roteiro adaptado não é ATAM formal |
| P10 | Mario Barbacci e colaboradores. *Quality Attribute Workshops (QAWs), Third Edition*. CMU/SEI-2003-TR-016, 2003 | [Relatório SEI](https://sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/), resumo institucional; DOI 10.1184/R1/6582656.v1 | Elicitar cenários antes de definir arquitetura |

## Guias, padrões e conteúdo didático

| ID | Fonte primária | Conteúdo consultado e aplicação |
| --- | --- | --- |
| G01 | Simon Brown. [C4 model](https://c4model.com/) | Visão geral: níveis de abstração e vistas; aprofundar os diagramas específicos quando usados |
| G02 | ADR community. [Architectural Decision Records](https://adr.github.io/) | Definição, justificativa e histórico de decisões |
| G03 | Peter Hruschka; Gernot Starke. [arc42 overview](https://arc42.org/overview) | Organização da documentação; não foi copiado o template licenciado |
| G04 | Alistair Cockburn. [Hexagonal Architecture, artigo original de 2005](https://alistair.cockburn.us/hexagonal-architecture) | Intenção, portas, adaptadores e isolamento da aplicação |
| G05 | Martin Fowler. [CQRS](https://martinfowler.com/bliki/CQRS.html), 2011 | Separação de modelos; cautela com complexidade |
| G06 | Chris Richardson. [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) | Problema de escrita/publicação, solução e duplicatas |
| G07 | Chris Richardson. [Saga](https://microservices.io/patterns/data/saga.html) | Coordenação e compensação; não confundir com o artigo original de 1987, cujo PDF não foi acessado |
| G08 | Martin Fowler. [Monolith First](https://martinfowler.com/bliki/MonolithFirst.html), 2015 | Argumento baseado em experiência, não teorema nem ensaio controlado |
| G09 | Marc Brooker/Amazon. [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), 2019 | Tratamento de falhas transitórias e risco de amplificação |
| G10 | Microsoft. [Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) | Substituição incremental de capacidades |
| G11 | OWASP. [ASVS](https://asvs.owasp.org/) | Visão geral; versão 5.0.0 publicada em 30/05/2025. Consultar requisitos detalhados antes de afirmar aderência |
| G12 | AWS. [Well-Architected](https://aws.amazon.com/architecture/well-architected/) | Página geral; estrutura para revisão, sujeita ao contexto do fornecedor |
| G13 | Microsoft. [Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/) | Pilares e propósito; selecionar guias detalhados conforme o workload |
| G14 | iSAQB. [CPSA Foundation curriculum](https://public.isaqb.org/curriculum-foundation/curriculum-foundation-en.html) | Estrutura curricular da versão 2025.1-rev2-EN; não usado o release candidate como currículo estável |
| G15 | MIT. [6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | Ementa e recursos de aulas/laboratórios; curso não realizado nesta pesquisa |
| G16 | ISO. [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) | Resumo oficial e escopo; texto normativo completo comercial, não consultado |

## Atualizar e resolver divergências

Verificar novamente versões de padrões, tecnologias, preços e limites quando forem relevantes. Para conceitos estáveis, manter a edição citada e procurar fonte original quando a precisão exigir. Para afirmação quantitativa, registrar população, ambiente, método, período e limitações. Não extrapolar estudo de um sistema para todos os sistemas.

Para aprofundamento: localizar publicação original, registrar acesso real, ler definição e hipóteses, buscar evidência contrária e transformar a conclusão em hipótese verificável no projeto. Manter referência indisponível como indicação de leitura, sem usá-la como prova de trecho não lido.
