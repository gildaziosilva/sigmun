# 012 – Matriz-de-Rastreabilidade – Metadados Corporativos

#### Matriz-de-Rastreabilidade – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-012

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-MET-001 | RegistrarMetadado | HU-MET-001 | RF-MET-001 | RF-CUM-001 |
| CU-MET-002 | CriarMetadado | HU-MET-002 | RF-MET-002 | RF-CUM-001 |
| CU-MET-003 | AtualizarMetadado | HU-MET-003 | RF-MET-003 | RF-CUM-001 |
| CU-MET-004 | ConsultarMetadado | HU-MET-004 | RF-MET-004 | RF-CUM-001 |
| CU-MET-005 | BuscarMetadado | HU-MET-001 | RF-MET-005 | RF-CUM-001 |
| CU-MET-006 | ListarMetadados | HU-MET-002 | RF-MET-006 | RF-CUM-001 |
| CU-MET-007 | AtivarMetadado | HU-MET-003 | RF-MET-007 | RF-CUM-001 |
| CU-MET-008 | DesativarMetadado | HU-MET-004 | RF-MET-008 | RF-CUM-001 |
| CU-MET-009 | AlterarSituacaoMetadado | HU-MET-001 | RF-MET-009 | RF-CUM-001 |
| CU-MET-010 | ExcluirMetadado | HU-MET-002 | RF-MET-010 | RF-CUM-001 |
| CU-MET-011 | DeletarMetadado | HU-MET-003 | RF-MET-011 | RF-CUM-001 |
| CU-MET-012 | RegistrarValorMetadado | HU-MET-004 | RF-MET-012 | RF-CUM-001 |
| CU-MET-013 | AtribuirValorMetadado | HU-MET-001 | RF-MET-013 | RF-CUM-001 |
| CU-MET-014 | ConsultarValorMetadado | HU-MET-002 | RF-MET-014 | RF-CUM-001 |
| CU-MET-015 | BuscarValorMetadado | HU-MET-003 | RF-MET-015 | RF-CUM-001 |
| CU-MET-016 | ListarValoresMetadado | HU-MET-004 | RF-MET-016 | RF-CUM-001 |
| CU-MET-017 | RemoverValorMetadado | HU-MET-001 | RF-MET-017 | RF-CUM-001 |
| CU-MET-018 | ValidarValorMetadado | HU-MET-002 | RF-MET-018 | RF-CUM-001 |
| CU-MET-019 | RegistrarClassificacao | HU-MET-003 | RF-MET-019 | RF-CUM-001 |
| CU-MET-020 | CriarClassificacao | HU-MET-004 | RF-MET-020 | RF-CUM-001 |
| CU-MET-021 | AtualizarClassificacao | HU-MET-001 | RF-MET-021 | RF-CUM-001 |
| CU-MET-022 | ConsultarClassificacao | HU-MET-002 | RF-MET-022 | RF-CUM-001 |
| CU-MET-023 | BuscarClassificacao | HU-MET-003 | RF-MET-023 | RF-CUM-001 |
| CU-MET-024 | ExcluirClassificacao | HU-MET-004 | RF-MET-024 | RF-CUM-001 |
| CU-MET-025 | DeletarClassificacao | HU-MET-001 | RF-MET-025 | RF-CUM-001 |
| CU-MET-026 | RegistrarTaxonomia | HU-MET-002 | RF-MET-026 | RF-CUM-001 |
| CU-MET-027 | CriarTaxonomia | HU-MET-003 | RF-MET-027 | RF-CUM-001 |
| CU-MET-028 | AtualizarTaxonomia | HU-MET-004 | RF-MET-028 | RF-CUM-001 |
| CU-MET-029 | ConsultarTaxonomia | HU-MET-001 | RF-MET-029 | RF-CUM-001 |
| CU-MET-030 | BuscarTaxonomia | HU-MET-002 | RF-MET-030 | RF-CUM-001 |
| CU-MET-031 | ListarTaxonomias | HU-MET-003 | RF-MET-030 | RF-CUM-001 |
| CU-MET-032 | ExcluirTaxonomia | HU-MET-004 | RF-MET-030 | RF-CUM-001 |
| CU-MET-033 | DeletarTaxonomia | HU-MET-001 | RF-MET-030 | RF-CUM-001 |
| CU-MET-034 | RegistrarTermo | HU-MET-002 | RF-MET-030 | RF-CUM-001 |
| CU-MET-035 | CriarTermo | HU-MET-003 | RF-MET-030 | RF-CUM-001 |
| CU-MET-036 | AtualizarTermo | HU-MET-004 | RF-MET-030 | RF-CUM-001 |
| CU-MET-037 | ConsultarTermo | HU-MET-001 | RF-MET-030 | RF-CUM-001 |
| CU-MET-038 | BuscarTermo | HU-MET-002 | RF-MET-030 | RF-CUM-001 |
| CU-MET-039 | ListarTermos | HU-MET-003 | RF-MET-030 | RF-CUM-001 |
| CU-MET-040 | ExcluirTermo | HU-MET-004 | RF-MET-030 | RF-CUM-001 |
| CU-MET-041 | DeletarTermo | HU-MET-001 | RF-MET-030 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Metadados-Corporativos-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
