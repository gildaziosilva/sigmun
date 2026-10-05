# 012 – Matriz-de-Rastreabilidade – Dados Corporativos

#### Matriz-de-Rastreabilidade – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-012

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-DAD-001 | CriarAtivo | HU-DAD-001 | RF-DAD-001 | RF-CUM-001 |
| CU-DAD-002 | AtivarAtivo | HU-DAD-002 | RF-DAD-002 | RF-CUM-001 |
| CU-DAD-003 | DesativarAtivo | HU-DAD-003 | RF-DAD-003 | RF-CUM-001 |
| CU-DAD-004 | ArquivarAtivo | HU-DAD-004 | RF-DAD-004 | RF-CUM-001 |
| CU-DAD-005 | BuscarAtivo | HU-DAD-001 | RF-DAD-005 | RF-CUM-001 |
| CU-DAD-006 | AtualizarQualidade | HU-DAD-002 | RF-DAD-006 | RF-CUM-001 |
| CU-DAD-007 | CriarCatalogo | HU-DAD-003 | RF-DAD-007 | RF-CUM-001 |
| CU-DAD-008 | AtualizarCatalogo | HU-DAD-004 | RF-DAD-008 | RF-CUM-001 |
| CU-DAD-009 | BuscarCatalogo | HU-DAD-001 | RF-DAD-009 | RF-CUM-001 |
| CU-DAD-010 | DeletarCatalogo | HU-DAD-002 | RF-DAD-010 | RF-CUM-001 |
| CU-DAD-011 | AdicionarAtivoCatalogo | HU-DAD-003 | RF-DAD-011 | RF-CUM-001 |
| CU-DAD-012 | RemoverAtivoCatalogo | HU-DAD-004 | RF-DAD-012 | RF-CUM-001 |
| CU-DAD-013 | CriarLinhagem | HU-DAD-001 | RF-DAD-013 | RF-CUM-001 |
| CU-DAD-014 | AtualizarLinhagem | HU-DAD-002 | RF-DAD-014 | RF-CUM-001 |
| CU-DAD-015 | BuscarLinhagem | HU-DAD-003 | RF-DAD-015 | RF-CUM-001 |
| CU-DAD-016 | DeletarLinhagem | HU-DAD-004 | RF-DAD-016 | RF-CUM-001 |
| CU-DAD-017 | CriarPolitica | HU-DAD-001 | RF-DAD-017 | RF-CUM-001 |
| CU-DAD-018 | AtualizarPolitica | HU-DAD-002 | RF-DAD-018 | RF-CUM-001 |
| CU-DAD-019 | BuscarPolitica | HU-DAD-003 | RF-DAD-019 | RF-CUM-001 |
| CU-DAD-020 | DeletarPolitica | HU-DAD-004 | RF-DAD-020 | RF-CUM-001 |
| CU-DAD-021 | AdicionarRegraPolitica | HU-DAD-001 | RF-DAD-021 | RF-CUM-001 |
| CU-DAD-022 | RemoverRegraPolitica | HU-DAD-002 | RF-DAD-022 | RF-CUM-001 |
| CU-DAD-023 | AvaliarQualidade | HU-DAD-003 | RF-DAD-023 | RF-CUM-001 |
| CU-DAD-024 | AtualizarQualidadeDados | HU-DAD-004 | RF-DAD-024 | RF-CUM-001 |
| CU-DAD-025 | BuscarQualidade | HU-DAD-001 | RF-DAD-025 | RF-CUM-001 |
| CU-DAD-026 | DeletarQualidade | HU-DAD-002 | RF-DAD-026 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Dados-Corporativos-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
