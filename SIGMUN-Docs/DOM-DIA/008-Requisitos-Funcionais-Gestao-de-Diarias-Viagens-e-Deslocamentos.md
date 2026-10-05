# 008 – Requisitos-Funcionais – Gestão de Diárias, Viagens e Deslocamentos

#### Requisitos-Funcionais – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-008

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **os requisitos funcionais** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-DIA-001 | POST /api/v1/dia/diarias | Alta | diarias | CAP-DIA-001 |
| RF-DIA-002 | GET /api/v1/dia/diarias/servidor/{servidor_id} | Média | diarias | CAP-DIA-001 |
| RF-DIA-003 | GET /api/v1/dia/diarias/status/{status} | Média | diarias | CAP-DIA-001 |
| RF-DIA-004 | GET /api/v1/dia/diarias/{diaria_id} | Média | diarias | CAP-DIA-001 |
| RF-DIA-005 | POST /api/v1/dia/diarias/{diaria_id}/autorizar | Alta | diarias | CAP-DIA-001 |
| RF-DIA-006 | POST /api/v1/dia/diarias/{diaria_id}/calcular | Alta | diarias | CAP-DIA-001 |
| RF-DIA-007 | POST /api/v1/dia/diarias/{diaria_id}/conceder | Alta | diarias | CAP-DIA-001 |
| RF-DIA-008 | POST /api/v1/dia/diarias/{diaria_id}/iniciar-prestacao | Alta | diarias | CAP-DIA-001 |
| RF-DIA-009 | POST /api/v1/dia/diarias/{diaria_id}/pagar | Alta | diarias | CAP-DIA-001 |
| RF-DIA-010 | POST /api/v1/dia/prestacoes | Alta | prestacoes | CAP-DIA-001 |
| RF-DIA-011 | GET /api/v1/dia/prestacoes/abertas | Média | prestacoes | CAP-DIA-001 |
| RF-DIA-012 | GET /api/v1/dia/prestacoes/{prestacao_id} | Média | prestacoes | CAP-DIA-001 |
| RF-DIA-013 | POST /api/v1/dia/prestacoes/{prestacao_id}/aprovar | Alta | prestacoes | CAP-DIA-001 |
| RF-DIA-014 | POST /api/v1/dia/prestacoes/{prestacao_id}/glosar | Alta | prestacoes | CAP-DIA-001 |
| RF-DIA-015 | POST /api/v1/dia/prestacoes/{prestacao_id}/restituir | Alta | prestacoes | CAP-DIA-001 |
| RF-DIA-016 | POST /api/v1/dia/viagens | Alta | viagens | CAP-DIA-001 |
| RF-DIA-017 | GET /api/v1/dia/viagens/servidor/{servidor_id} | Média | viagens | CAP-DIA-001 |
| RF-DIA-018 | GET /api/v1/dia/viagens/{viagem_id} | Média | viagens | CAP-DIA-001 |
| RF-DIA-019 | POST /api/v1/dia/viagens/{viagem_id}/tramitar | Alta | viagens | CAP-DIA-001 |
| RF-DIA-020 | POST /api/v1/dia/viagens/{viagem_id}/visitar | Alta | viagens | CAP-DIA-001 |

---

# 3. Cobertura

Operações publicadas: **20**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Gestao-de-Diarias-Viagens-e-Deslocamentos-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
