# Avaliação, documentação e evolução

## Revisar um sistema existente

1. Registrar pergunta, escopo e versão analisada.
2. Ler instruções do projeto, manifests, configuração, pontos de entrada, esquema e testes relevantes. Usar `rg` e leituras direcionadas; não despejar o repositório inteiro.
3. Rastrear um fluxo normal e um fluxo de falha. Anotar evidências por arquivo/símbolo e, quando disponível, execução.
4. Mapear módulos, chamadas, dados compartilhados e unidades de implantação. Confirmar dependências de runtime que não aparecem nos imports.
5. Comparar estrutura e comportamento com os requisitos prioritários.
6. Classificar cada achado por consequência, confiança e prioridade; distinguir fato de hipótese e preferência estética.
7. Recomendar a menor intervenção eficaz e a prova que confirmaria a melhora.

Se não houver acesso ao código ou ambiente, produzir avaliação conceitual e declarar o limite. Não inventar módulos, vulnerabilidades ou gargalos. Contagem de arquivos e desenho de pastas não demonstram qualidade.

## Avaliar trade-offs

Usar uma avaliação leve inspirada no ATAM: explicitar objetivos de negócio, abordagem arquitetural e cenários; priorizar riscos; identificar decisões sensíveis e efeitos sobre qualidades diferentes; documentar dúvidas e experimentos. ATAM é um método estruturado com participação de stakeholders; não chamar este roteiro reduzido de execução formal do método. [P09]

Exemplo original: cache pode melhorar latência e reduzir carga, mas aumenta dificuldade de invalidação e risco de exposição entre organizações. O TTL é um ponto sensível. A decisão exige declarar qual atraso é permitido e como testar isolamento.

Para risco, estimar impacto e plausibilidade com base explícita. Não inventar probabilidade numérica para dar aparência de precisão. Registrar gatilho de revisão e responsável. Para dívida técnica, registrar custo atual, cenário de agravamento e intervenção possível, não apenas “código ruim”.

## Comunicar com vistas suficientes

C4 oferece contexto, containers, componentes e código, além de vistas de suporte. Selecionar o nível pela pergunta do leitor. Identificar responsabilidades, relações e fronteiras. Em diagramas pequenos, preferir poucos elementos com conexões nomeadas a dezenas de caixas sem semântica. [G01]

Usar arc42 como checklist de cobertura quando a documentação exigir contexto, estrutura, execução, implantação, decisões, qualidades e riscos. Não copiar todas as seções para um projeto trivial. Registrar também dono e data para que documentação possa ser revisada. [G03]

Registrar uma decisão relevante por ADR: contexto, opções, decisão, consequências e evidência. Preservar histórico quando uma decisão for substituída; não reescrever o passado como se a opção atual sempre tivesse sido escolhida. [G02]

## Verificar propriedades arquiteturais

Uma fitness function verifica uma propriedade importante ao longo da evolução. Escolher verificações que possam detectar regressão: regras de dependência, compatibilidade de contrato, isolamento, orçamento de latência ou exercício de recuperação. Não tratar uma pontuação de lint como representação completa da arquitetura. [B09]

| Propriedade | Evidência possível | Limitação |
| --- | --- | --- |
| Fronteira de módulo | Regra de imports e teste de API pública | Dependências dinâmicas podem escapar |
| Compatibilidade | Teste de contrato com consumidores conhecidos | Não cobre consumidores desconhecidos |
| Integridade sob repetição | Ensaio de duplicatas e falhas de confirmação | Depende do modelo de falha ensaiado |
| Desempenho | Carga representativa e telemetria | Não extrapolar além do ambiente medido |
| Recuperabilidade | Restauração e reconciliação verificadas | Um ensaio não garante todos os desastres |

Não executar testes destrutivos ou carga em produção sem autorização específica.

## Migrar gradualmente

Considerar Strangler Fig para substituir capacidades progressivamente por trás de uma fronteira de roteamento, mantendo funcionamento do restante. Avaliar se o legado permite interceptar chamadas e separar dados. Não impor o padrão quando o custo do convívio superar o de uma troca pequena e controlada. [G10]

Planejar expandir → migrar → contrair: introduzir contrato/schema compatível, preencher dados com controles, migrar consumidores, verificar reconciliação e só então remover o antigo. Evitar dual writes ingênuos. Definir a autoridade dos dados em cada fase.

Para cada etapa, especificar entrada, saída, métricas, critério de parada e recuperação. Testar leitura e escrita de versões coexistentes. Não apagar coluna, fila ou endpoint enquanto houver consumidores dependentes. Quando houver transformação irreversível ou efeito externo, projetar roll-forward, restauração e/ou compensação, e explicitar o limite do rollback.
