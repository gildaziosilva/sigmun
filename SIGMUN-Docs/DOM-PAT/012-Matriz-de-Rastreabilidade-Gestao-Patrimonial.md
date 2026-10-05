# 012 – Matriz-de-Rastreabilidade – Gestão Patrimonial

#### Matriz-de-Rastreabilidade – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-012

**Domínio:** Gestão Patrimonial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Patrimonial.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-PAT-001 | CadastrarBem | HU-PAT-001 | RF-PAT-001 | RF-CUM-001 |
| CU-PAT-002 | DepreciarBem | HU-PAT-002 | RF-PAT-002 | RF-CUM-001 |
| CU-PAT-003 | TransferirBem | HU-PAT-003 | RF-PAT-003 | RF-CUM-001 |
| CU-PAT-004 | ConcluirTransferencia | HU-PAT-004 | RF-PAT-004 | RF-CUM-001 |
| CU-PAT-005 | BaixarBem | HU-PAT-001 | RF-PAT-005 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Gestao-Patrimonial-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
