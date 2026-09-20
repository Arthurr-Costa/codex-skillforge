# Mentoria de segurança

Modele ativo, ator, fronteira de confiança, ameaça e controle.

## Controles recorrentes

- validação de entrada e codificação de saída;
- autorização no servidor e menor privilégio;
- queries parametrizadas;
- gestão de sessão e CSRF;
- CORS restrito;
- proteção contra XSS, SSRF, path traversal e command injection;
- upload validado por conteúdo, tamanho e destino;
- segredos fora do código e dos logs;
- dependências verificadas por fontes atuais;
- auditoria proporcional ao dado e ao risco.

Diferencie indício, fraqueza, vulnerabilidade explorável e risco aceito. Regex não confirma vulnerabilidade.

Nunca peça que o usuário cole um `.env` completo. Trabalhe com nomes de variáveis, valores redigidos e metadados. Para corrigir exposição real, ensine remoção, rotação e verificação de histórico.
