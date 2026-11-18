# Índice de Registros de Decisões Arquiteturais (ADRs)

**Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal  
**Domínio:** Governança  
**Versão:** 1.1  
**Status do índice:** Vigente  
**Classificação da Informação:** Pública  
**Responsável:** Equipe SIGMUN  
**Última atualização:** 2026-11-18

## Finalidade

Este índice reúne os Registros de Decisões Arquiteturais (ADRs) mantidos no
diretório. O status e o registro de aprovação abaixo reproduzem o que está
documentado em cada ADR; a ausência de informação não deve ser interpretada
como aprovação.

## Relação de ADRs

| ADR | Decisão / assunto | Status registrado no ADR | Registro de aprovação documentado |
| --- | --- | --- | --- |
| [ADR-0000](ADR-0000-adopt-apache-2.0-license.md) | Adoção da Apache License 2.0 | Aceita | Equipe SIGMUN indicada como decisora; 17/08/2026 |
| [ADR-0001](ADR-0001-Arquitetura-Modular.md) | Arquitetura modular | Vigente | Não identificado no documento |
| [ADR-0002](ADR-0002-Offline-First.md) | Estratégia Offline First | Vigente | Não identificado no documento |
| [ADR-0003](ADR-0003-APIs-REST.md) | APIs REST e comunicação entre sistemas | Vigente | Não identificado no documento |
| [ADR-0004](ADR-0004-Neutralidade-Tecnologica.md) | Neutralidade tecnológica | Vigente | Não identificado no documento |
| [ADR-0005](ADR-0005-Cadastro-Unico-Municipal.md) | Cadastro Único Municipal | Vigente | Não identificado no documento |
| [ADR-0006](ADR-0006-Compras-canonicalizacao.md) | Canonicalização de Compras e Contratações: DOM-COM como identificador vigente | Aprovado pelo solicitante; vigente para a normalização registrada | Aprovação explícita do solicitante em 17/09/2026; sem alegação de aprovação institucional adicional |
| [ADR-0007](ADR-0007-cadastro-autenticacao-revisao-compartilhamento.md) | Autenticação, revisão cadastral e compartilhamento de pessoa (DOM-CUM) | Status da decisão não explicitado; revisão indicada como vigente | Não identificado no documento |
| [ADR-0008](ADR-0008-ouv-autorizacao-dados-sigilosos.md) | Autorização e sigilo de dados de Ouvidoria (DOM-OUV) | Proposto — aguardando aprovação | Aprovação pendente, conforme o próprio ADR |
| [ADR-0009](ADR-0009-fim-autenticacao-legada-headers.md) | Encerramento da autenticação legada por headers | Aceito | Não individualizado no documento |
| [ADR-0010](ADR-0010-endpoints-publicos.md) | Inventário explícito de endpoints públicos por decisão | Aceito | Não individualizado no documento |
| [ADR-0011](ADR-0011-paginacao-unificada.md) | Convenção única de paginação (base 1; page_size padrão 20, máximo 100) | Aceito | Não individualizado no documento |
| [ADR-0012](ADR-0012-envelope-erro-padronizado.md) | Envelope de erro padronizado com correlation_id | Aceito | Não individualizado no documento |
| [ADR-0013](ADR-0013-openapi-versionado-diff-gate.md) | Versionamento do OpenAPI e gate de diff para breaking changes | Aceito | Não individualizado no documento |

## Critérios de leitura

- **Status do ADR** representa o estado declarado no respectivo registro. Não
  equivale, por si só, a comprovação de implementação ou validação operacional.
- **Registro de aprovação** identifica somente a instância ou pessoa cuja
  aprovação está expressamente documentada. Não se presume aprovação
  institucional, ata ou deliberação de comitê.
- Quando o documento não informa o status da decisão ou a aprovação, o índice
  registra essa ausência em vez de inferir uma condição.
- O ADR-0008 permanece proposto e aguardando aprovação; sua presença no índice
  não significa que a decisão esteja aprovada.
- A quantidade de endpoints públicos deve ser consultada no inventário vigente
  do ADR-0010, e não em descrições históricas anteriores.

## Integridade do índice

Os links relativos desta tabela apontam para os arquivos ADR existentes no
mesmo diretório. Alterações de nome, inclusão, retirada ou renumeração de ADRs
devem ser refletidas neste índice após verificação dos destinos e das
referências relacionadas.
