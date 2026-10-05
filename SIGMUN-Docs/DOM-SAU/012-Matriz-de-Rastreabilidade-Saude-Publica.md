# 012 – Matriz-de-Rastreabilidade – Saúde Pública

#### Matriz-de-Rastreabilidade – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-012

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-SAU-001 | CadastrarPaciente | HU-SAU-001 | RF-SAU-001 | RF-CUM-001 |
| CU-SAU-002 | RegistrarAtendimento | HU-SAU-002 | RF-SAU-002 | RF-CUM-001 |
| CU-SAU-003 | AgendarConsulta | HU-SAU-003 | RF-SAU-003 | RF-CUM-001 |
| CU-SAU-004 | ConfirmarAgendamento | HU-SAU-004 | RF-SAU-004 | RF-CUM-001 |
| CU-SAU-005 | CancelarAgendamento | HU-SAU-001 | RF-SAU-005 | RF-CUM-001 |
| CU-SAU-006 | RealizarAgendamento | HU-SAU-002 | RF-SAU-006 | RF-CUM-001 |
| CU-SAU-007 | SolicitarRegulacao | HU-SAU-003 | RF-SAU-007 | RF-CUM-001 |
| CU-SAU-008 | AutorizarRegulacao | HU-SAU-004 | RF-SAU-008 | RF-CUM-001 |
| CU-SAU-009 | NegarRegulacao | HU-SAU-001 | RF-SAU-009 | RF-CUM-001 |
| CU-SAU-010 | CadastrarMedicamento | HU-SAU-002 | RF-SAU-010 | RF-CUM-001 |
| CU-SAU-011 | ReporEstoque | HU-SAU-003 | RF-SAU-011 | RF-CUM-001 |
| CU-SAU-012 | DispensarMedicamento | HU-SAU-004 | RF-SAU-012 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Saude-Publica-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
