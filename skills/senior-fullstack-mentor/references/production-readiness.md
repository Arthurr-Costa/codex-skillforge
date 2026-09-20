# Prontidão para produção

Ensine que implementação termina quando o comportamento pode ser operado e recuperado.

## Checklist contextual

- configuração por ambiente;
- secrets e permissões;
- migrations e rollback;
- logs estruturados e correlação;
- métricas e alertas acionáveis;
- timeouts e limites;
- retries e idempotência;
- health checks;
- backups e restauração;
- deploy gradual quando necessário;
- runbook e responsável;
- proteção de dados pessoais;
- validação no ambiente correto.

Local não prova produção. Código no disco não prova processo servido. Teste sintético não prova integração real.

Para incidentes, priorize contenção segura, preservação de evidência, restauração, comunicação e análise posterior. Não faça uma mudança irreversível sob pressão sem delimitar impacto e recuperação.
