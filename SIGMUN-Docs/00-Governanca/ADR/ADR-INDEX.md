# ADR INDEX



**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Governança

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



---



- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



---



Este documento encontra-se em elaboração e deverá ser atualizado conforme a evolução do SIGMUN.



---



**Documento:**ADR-INDEX.md

**Última atualização:** 2026-10-08

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente


## Decisão de canonicalização de Compras

| ADR | Decisão | Aprovação registrada |
| --- | --- | --- |
| [ADR-0000](ADR-0000-adopt-apache-2.0-license.md) | licença do projeto | Aprovação Institucional de Fundação|
| [ADR-0001](ADR-0001-Arquitetura-Modular.md) | Arquitetura do projeto | Aprovação Institucional de Fundação|
| [ADR-0002](ADR-0002-Offline-First.md) | Funcionamento a partir do armazenamento local  | Aprovação Institucional de Fundação | 
| [ADR-0003](ADR-0003-APIs-REST.md) | Comunicação entre sistemas | Aprovação Institucional de Fundação | 
| [ADR-0004](ADR-0004-Neutralidade-Tecnologica.md) | regras externas não devem ou discriminar o sistema | Aprovação Institucional de Fundação |
| [ADR-0005](ADR-0005-Cadastro-Unico-Municipal.md) | Cadastro Unico Municipal Compartilhado | Aprovação Institucional de Fundação |
| [ADR-0006](ADR-0006-Compras-canonicalizacao.md) | DOM-COM vigente; formas históricas preservadas seletivamente | Solicitante da tarefa, em 17/09/2026; sem presumir aprovação institucional adicional |
| [ADR-0007](ADR-0007-cadastro-autenticacao-revisao-compartilhamento.md) | Cadastro | Aprovado pela Equipe SIGMUN durante Desenvolvimento |
| [ADR-0008](ADR-0008-ouv-autorizacao-dados-sigilosos.md) | Dados Sigilosos | Aprovado pela Equipe SIGMUN durante Desenvolvimento |
| [ADR-0009](ADR-0009-fim-autenticacao-legada-headers.md) | Autenticação | Aprovado pela Equipe SIGMUN durante Desenvolvimento |
| [ADR-0010](ADR-0010-endpoints-publicos.md) | Inventário explícito das 18 rotas anônimas por decisão; varredura obrigatória (`scripts/verificar_rotas_publicas.py`) | 06/10/2026 — TODO2 T-2.3 |
| [ADR-0011](ADR-0011-paginacao-unificada.md) | Convenção única de paginação: page=1 (base 1), page_size=20 (máx 100); módulo compartilhado `src/shared/presentation/paginacao.py` | 08/10/2026 — TODO2 T-3.1 |
| [ADR-0012](ADR-0012-envelope-erro-padronizado.md) | Envelope de erro padronizado com correlation_id; exception handlers globais em `src/main.py`; códigos categorizados (VALIDATION_ERROR, NOT_FOUND, etc.) | 08/10/2026 — TODO2 T-3.2 |
| [ADR-0013](ADR-0013-openapi-versionado-diff-gate.md) | openapi.json versionado com gate de diff no CI; breaking changes detectadas (path/operação/parâmetro/schema removidos, security aumentada); non-breaking apenas aviso | 08/10/2026 — TODO2 T-3.3 |