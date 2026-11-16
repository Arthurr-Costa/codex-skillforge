# Fundamentos e fronteiras

Usar os identificadores da bibliografia em `fontes.md`. As orientações abaixo são síntese aplicada, não transcrição de livros.

## Arquitetura, projeto e descrição

Tratar arquitetura como as estruturas e decisões relevantes para compreender e evoluir um sistema em seu contexto. Investigar módulos, elementos em execução, comunicação, dados e alocação à infraestrutura; um único desenho não responde a todas as perguntas. A descrição registra aspectos da arquitetura, mas não é o sistema. A ISO 42010 trata da descrição, sem prescrever ferramenta ou método de criação. [B02, P02, G16]

Reconhecer significância arquitetural pelo alcance, risco, dependências e dificuldade de reversão. Uma escolha aparentemente local, como formato de identificador público, pode se tornar contrato duradouro. Uma biblioteca trocável atrás de uma interface estreita pode ter pouco impacto estrutural.

## Modularidade e informação escondida

Usar a separação para conter mudanças. Investigar quais decisões podem variar e quais conhecimentos cada consumidor realmente precisa. Parnas demonstra que critérios de decomposição afetam flexibilidade e compreensão; não basta dividir etapas de processamento. [P01]

Aplicar perguntas operacionais:

- Qual mudança de negócio atravessa mais módulos?
- Quem pode alterar este dado ou interpretar este estado?
- O consumidor depende da intenção ou de detalhes do armazenamento?
- O contrato pode mudar sem uma implantação coordenada?
- Uma falha se propaga mesmo sem dependência de código?

Distinguir acoplamento estrutural (imports, bibliotecas), temporal (necessidade de disponibilidade simultânea), de dados (schema e autoridade), semântico (regras compartilhadas) e operacional (implantação, configuração e incidentes). Um broker reduz certas dependências temporais, mas não elimina dependência de significado nem compatibilidade.

Usar coesão como relação entre responsabilidades e razões de mudança, não como tamanho de arquivo. Métricas de dependências e mudanças conjuntas são sinais investigativos; não transformar limiares genéricos em diagnóstico automático. [B01, B03]

## Domínio e DDD

Começar por linguagem, processos, regras e conflitos de significado. Delimitar bounded contexts onde um modelo e seus termos são coerentes. Mapear relações e tradução entre contextos. Distinguir contexto de domínio de serviço, pacote, equipe e banco: não há correspondência obrigatória de um para um. [B05]

Para desenho tático, identificar entidades por identidade, objetos de valor por significado e igualdade, e agregados por regras que precisam permanecer consistentes. Evitar agregados enormes e repositórios para cada tabela por automatismo. Perguntar se a complexidade das regras justifica um modelo rico; operações simples podem caber em procedimentos de aplicação claros. [B05, B06]

Exemplo original: em um sistema de atendimento, “cliente” no agendamento e “pagador” no faturamento podem ter regras e ciclos diferentes. Compartilhar um cadastro não obriga compartilhar todos os estados. Se confirmar uma reserva exige atualizar duas tabelas atomicamente, separar os responsáveis em serviços cria uma nova obrigação de coordenação; não resolve a regra por si só.

## Dependências e separação de mecanismos

Em portas e adaptadores, representar capacidades que a aplicação requer ou oferece. Encapsular acesso a HTTP, arquivos, interface gráfica ou banco quando isso protege regras, testes ou alternativas reais. O número de lados do desenho não é requisito. [G04]

Separar fluxo de controle de direção da dependência de código. A aplicação pode chamar um adaptador por um contrato que ela define. Não duplicar todas as entidades do ORM apenas para cumprir um diagrama; justificar a tradução pelo isolamento obtido.

Tratar SOLID, DRY e simplicidade como heurísticas locais, não como prova de qualidade de uma arquitetura. Remover duplicação conceitual quando representa a mesma regra; tolerar alguma repetição quando uma abstração compartilhada acoplaria contextos que evoluem independentemente.

## Aspecto sociotécnico

Registrar quem decide, mantém e atende incidentes de cada parte. Analisar dependências entre times, necessidade de coordenação e carga de aprendizagem. A autonomia técnica precisa de propriedade e capacidade operacional. Não usar organização atual como destino inevitável: propor limites e responsabilidades em conjunto. [B08, B09]
