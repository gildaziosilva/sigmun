# 008 – Requisitos-Funcionais – Atendimento ao Cidadão

#### Requisitos-Funcionais – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-008

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-ATE-001 | GET /api/v1/ate/atendimentos | Média | atendimentos | CAP-ATE-001 |
| RF-ATE-002 | POST /api/v1/ate/atendimentos/iniciar | Alta | atendimentos | CAP-ATE-001 |
| RF-ATE-003 | GET /api/v1/ate/atendimentos/{atendimento_id} | Média | atendimentos | CAP-ATE-001 |
| RF-ATE-004 | POST /api/v1/ate/atendimentos/{atendimento_id}/cancelar | Alta | atendimentos | CAP-ATE-001 |
| RF-ATE-005 | POST /api/v1/ate/atendimentos/{atendimento_id}/concluir | Alta | atendimentos | CAP-ATE-001 |
| RF-ATE-006 | GET /api/v1/ate/atendimentos/{atendimento_id}/encaminhamentos | Média | atendimentos | CAP-ATE-001 |
| RF-ATE-007 | POST /api/v1/ate/avaliacoes | Alta | avaliacoes | CAP-ATE-001 |
| RF-ATE-008 | GET /api/v1/ate/avaliacoes/{avaliacao_id} | Média | avaliacoes | CAP-ATE-001 |
| RF-ATE-009 | POST /api/v1/ate/encaminhamentos | Alta | encaminhamentos | CAP-ATE-001 |
| RF-ATE-010 | GET /api/v1/ate/encaminhamentos/{encaminhamento_id} | Média | encaminhamentos | CAP-ATE-001 |
| RF-ATE-011 | POST /api/v1/ate/encaminhamentos/{encaminhamento_id}/concluir | Alta | encaminhamentos | CAP-ATE-001 |
| RF-ATE-012 | POST /api/v1/ate/filas | Alta | filas | CAP-ATE-001 |
| RF-ATE-013 | POST /api/v1/ate/filas/{fila_id}/fechar | Alta | filas | CAP-ATE-001 |
| RF-ATE-014 | GET /api/v1/ate/health | Média | health | CAP-ATE-001 |
| RF-ATE-015 | POST /api/v1/ate/senhas | Alta | senhas | CAP-ATE-001 |
| RF-ATE-016 | POST /api/v1/ate/senhas/{senha_id}/atender | Alta | senhas | CAP-ATE-001 |
| RF-ATE-017 | POST /api/v1/ate/senhas/{senha_id}/chamar | Alta | senhas | CAP-ATE-001 |
| RF-ATE-018 | POST /api/v1/ate/senhas/{senha_id}/rechamar | Alta | senhas | CAP-ATE-001 |
| RF-ATE-019 | POST /api/v1/ate/triagens | Alta | triagens | CAP-ATE-001 |

---

# 3. Cobertura

Operações publicadas: **19**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Atendimento-ao-Cidadao-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
