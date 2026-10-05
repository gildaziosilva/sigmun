# 012 – Matriz-de-Rastreabilidade – Orçamento Público

#### Matriz-de-Rastreabilidade – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-012

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-ORC-001 | CriarDotacao | HU-ORC-001 | RF-ORC-001 | RF-CUM-001 |
| CU-ORC-002 | SuplementarDotacao | HU-ORC-002 | RF-ORC-002 | RF-CUM-001 |
| CU-ORC-003 | AnularDotacao | HU-ORC-003 | RF-ORC-003 | RF-CUM-001 |
| CU-ORC-004 | ReservarSaldo | HU-ORC-004 | RF-ORC-004 | RF-CUM-001 |
| CU-ORC-005 | CancelarReserva | HU-ORC-001 | RF-ORC-005 | RF-CUM-001 |
| CU-ORC-006 | CriarPPA | HU-ORC-002 | RF-ORC-006 | RF-CUM-001 |
| CU-ORC-007 | PublicarPPA | HU-ORC-003 | RF-ORC-007 | RF-CUM-001 |
| CU-ORC-008 | CriarLDO | HU-ORC-004 | RF-ORC-008 | RF-CUM-001 |
| CU-ORC-009 | SancionarLDO | HU-ORC-001 | RF-ORC-009 | RF-CUM-001 |
| CU-ORC-010 | CriarLOA | HU-ORC-002 | RF-ORC-010 | RF-CUM-001 |
| CU-ORC-011 | PublicarLOA | HU-ORC-003 | RF-ORC-011 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Orcamento-Publico-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
