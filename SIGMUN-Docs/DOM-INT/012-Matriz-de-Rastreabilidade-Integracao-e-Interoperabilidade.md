# 012 – Matriz-de-Rastreabilidade – Integração e Interoperabilidade

#### Matriz-de-Rastreabilidade – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-012

**Domínio:** Integração e Interoperabilidade

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Integracao-e-Interoperabilidade.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-INT-001 | CriarApiExterna | HU-INT-001 | RF-INT-001 | RF-CUM-001 |
| CU-INT-002 | BuscarApiExterna | HU-INT-002 | RF-INT-002 | RF-CUM-001 |
| CU-INT-003 | AtualizarApiExterna | HU-INT-003 | RF-INT-003 | RF-CUM-001 |
| CU-INT-004 | MudarEstadoApi | HU-INT-004 | RF-INT-004 | RF-CUM-001 |
| CU-INT-005 | DeletarApiExterna | HU-INT-001 | RF-INT-005 | RF-CUM-001 |
| CU-INT-006 | CriarContratoIntegracao | HU-INT-002 | RF-INT-006 | RF-CUM-001 |
| CU-INT-007 | BuscarContratoIntegracao | HU-INT-003 | RF-INT-007 | RF-CUM-001 |
| CU-INT-008 | AtualizarContratoIntegracao | HU-INT-004 | RF-INT-008 | RF-CUM-001 |
| CU-INT-009 | AprovarContratoIntegracao | HU-INT-001 | RF-INT-009 | RF-CUM-001 |
| CU-INT-010 | RetirarContratoIntegracao | HU-INT-002 | RF-INT-010 | RF-CUM-001 |
| CU-INT-011 | DeletarContratoIntegracao | HU-INT-003 | RF-INT-011 | RF-CUM-001 |
| CU-INT-012 | CriarConector | HU-INT-004 | RF-INT-012 | RF-CUM-001 |
| CU-INT-013 | BuscarConector | HU-INT-001 | RF-INT-013 | RF-CUM-001 |
| CU-INT-014 | AtualizarConector | HU-INT-002 | RF-INT-014 | RF-CUM-001 |
| CU-INT-015 | MudarEstadoConector | HU-INT-003 | RF-INT-015 | RF-CUM-001 |
| CU-INT-016 | DeletarConector | HU-INT-004 | RF-INT-016 | RF-CUM-001 |
| CU-INT-017 | RegistrarWebhook | HU-INT-001 | RF-INT-017 | RF-CUM-001 |
| CU-INT-018 | BuscarWebhook | HU-INT-002 | RF-INT-018 | RF-CUM-001 |
| CU-INT-019 | AtualizarWebhook | HU-INT-003 | RF-INT-019 | RF-CUM-001 |
| CU-INT-020 | MudarEstadoWebhook | HU-INT-004 | RF-INT-020 | RF-CUM-001 |
| CU-INT-021 | DeletarWebhook | HU-INT-001 | RF-INT-021 | RF-CUM-001 |
| CU-INT-022 | BuscarEntregaWebhook | HU-INT-002 | RF-INT-022 | RF-CUM-001 |
| CU-INT-023 | RetryEntregaWebhook | HU-INT-003 | RF-INT-023 | RF-CUM-001 |
| CU-INT-024 | CancelarEntregaWebhook | HU-INT-004 | RF-INT-024 | RF-CUM-001 |
| CU-INT-025 | ConsumirOutbox | HU-INT-001 | RF-INT-025 | RF-CUM-001 |
| CU-INT-026 | DespacharWebhooks | HU-INT-002 | RF-INT-026 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Integracao-e-Interoperabilidade-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
