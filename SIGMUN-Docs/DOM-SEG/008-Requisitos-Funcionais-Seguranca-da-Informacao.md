# 008 – Requisitos-Funcionais – Segurança da Informação

#### Requisitos-Funcionais – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-008

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-SEG-001 | GET /api/v1/seg/chaves | Média | chaves | CAP-SEG-001 |
| RF-SEG-002 | POST /api/v1/seg/chaves | Alta | chaves | CAP-SEG-001 |
| RF-SEG-003 | DELETE /api/v1/seg/chaves/{chave_id} | Alta | chaves | CAP-SEG-001 |
| RF-SEG-004 | GET /api/v1/seg/chaves/{chave_id} | Média | chaves | CAP-SEG-001 |
| RF-SEG-005 | POST /api/v1/seg/chaves/{chave_id}/expirar | Alta | chaves | CAP-SEG-001 |
| RF-SEG-006 | POST /api/v1/seg/chaves/{chave_id}/revogar | Alta | chaves | CAP-SEG-001 |
| RF-SEG-007 | GET /api/v1/seg/controles | Média | controles | CAP-SEG-001 |
| RF-SEG-008 | POST /api/v1/seg/controles | Alta | controles | CAP-SEG-001 |
| RF-SEG-009 | DELETE /api/v1/seg/controles/{controle_id} | Alta | controles | CAP-SEG-001 |
| RF-SEG-010 | GET /api/v1/seg/controles/{controle_id} | Média | controles | CAP-SEG-001 |
| RF-SEG-011 | PUT /api/v1/seg/controles/{controle_id} | Média | controles | CAP-SEG-001 |
| RF-SEG-012 | POST /api/v1/seg/controles/{controle_id}/implementar | Alta | controles | CAP-SEG-001 |
| RF-SEG-013 | POST /api/v1/seg/controles/{controle_id}/parcial | Alta | controles | CAP-SEG-001 |
| RF-SEG-014 | GET /api/v1/seg/credenciais | Média | credenciais | CAP-SEG-001 |
| RF-SEG-015 | POST /api/v1/seg/credenciais | Alta | credenciais | CAP-SEG-001 |
| RF-SEG-016 | GET /api/v1/seg/credenciais/{credencial_id} | Média | credenciais | CAP-SEG-001 |
| RF-SEG-017 | POST /api/v1/seg/credenciais/{credencial_id}/revogar | Alta | credenciais | CAP-SEG-001 |
| RF-SEG-018 | POST /api/v1/seg/credenciais/{credencial_id}/suspender | Alta | credenciais | CAP-SEG-001 |
| RF-SEG-019 | GET /api/v1/seg/incidentes | Média | incidentes | CAP-SEG-001 |
| RF-SEG-020 | POST /api/v1/seg/incidentes | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-021 | DELETE /api/v1/seg/incidentes/{incidente_id} | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-022 | GET /api/v1/seg/incidentes/{incidente_id} | Média | incidentes | CAP-SEG-001 |
| RF-SEG-023 | POST /api/v1/seg/incidentes/{incidente_id}/encerrar | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-024 | POST /api/v1/seg/incidentes/{incidente_id}/escalar | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-025 | POST /api/v1/seg/incidentes/{incidente_id}/mitigar | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-026 | POST /api/v1/seg/incidentes/{incidente_id}/resolver | Alta | incidentes | CAP-SEG-001 |
| RF-SEG-027 | GET /api/v1/seg/politicas | Média | politicas | CAP-SEG-001 |
| RF-SEG-028 | POST /api/v1/seg/politicas | Alta | politicas | CAP-SEG-001 |
| RF-SEG-029 | DELETE /api/v1/seg/politicas/{politica_id} | Alta | politicas | CAP-SEG-001 |
| RF-SEG-030 | GET /api/v1/seg/politicas/{politica_id} | Média | politicas | CAP-SEG-001 |
| RF-SEG-031 | PUT /api/v1/seg/politicas/{politica_id} | Média | politicas | CAP-SEG-001 |
| RF-SEG-032 | POST /api/v1/seg/politicas/{politica_id}/aprovar | Alta | politicas | CAP-SEG-001 |

---

# 3. Cobertura

Operações publicadas: **32**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Seguranca-da-Informacao-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
