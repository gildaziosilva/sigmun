# 005 – Casos-de-Uso – Metadados Corporativos

#### Casos-de-Uso – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-005

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

Este artefato detalha **os casos de uso** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-MET-001 | RegistrarMetadado | `RegistrarMetadadoUseCase` | Caso de uso para criar um novo metadado. |
| CU-MET-002 | CriarMetadado | `CriarMetadadoUseCase` | Caso de uso para criar um novo metadado. |
| CU-MET-003 | AtualizarMetadado | `AtualizarMetadadoUseCase` | Caso de uso para atualizar um metadado. |
| CU-MET-004 | ConsultarMetadado | `ConsultarMetadadoUseCase` | Caso de uso para buscar metadados. |
| CU-MET-005 | BuscarMetadado | `BuscarMetadadoUseCase` | Caso de uso para buscar metadados. |
| CU-MET-006 | ListarMetadados | `ListarMetadadosUseCase` | Caso de uso para buscar metadados. |
| CU-MET-007 | AtivarMetadado | `AtivarMetadadoUseCase` | Caso de uso para ativar um metadado. |
| CU-MET-008 | DesativarMetadado | `DesativarMetadadoUseCase` | Caso de uso para desativar um metadado. |
| CU-MET-009 | AlterarSituacaoMetadado | `AlterarSituacaoMetadadoUseCase` | Caso de uso para alterar a situação de um metadado (espelho DOM-COM). |
| CU-MET-010 | ExcluirMetadado | `ExcluirMetadadoUseCase` | Caso de uso para deletar um metadado. |
| CU-MET-011 | DeletarMetadado | `DeletarMetadadoUseCase` | Caso de uso para deletar um metadado. |
| CU-MET-012 | RegistrarValorMetadado | `RegistrarValorMetadadoUseCase` | Caso de uso para atribuir um valor de metadado a uma entidade. |
| CU-MET-013 | AtribuirValorMetadado | `AtribuirValorMetadadoUseCase` | Caso de uso para atribuir um valor de metadado a uma entidade. |
| CU-MET-014 | ConsultarValorMetadado | `ConsultarValorMetadadoUseCase` | Caso de uso para buscar valores de metadados. |
| CU-MET-015 | BuscarValorMetadado | `BuscarValorMetadadoUseCase` | Caso de uso para buscar valores de metadados. |
| CU-MET-016 | ListarValoresMetadado | `ListarValoresMetadadoUseCase` | Caso de uso para buscar valores de metadados. |
| CU-MET-017 | RemoverValorMetadado | `RemoverValorMetadadoUseCase` | Caso de uso para remover um valor de metadado. |
| CU-MET-018 | ValidarValorMetadado | `ValidarValorMetadadoUseCase` | Caso de uso para validar um valor contra um metadado. |
| CU-MET-019 | RegistrarClassificacao | `RegistrarClassificacaoUseCase` | Caso de uso para criar uma nova classificação. |
| CU-MET-020 | CriarClassificacao | `CriarClassificacaoUseCase` | Caso de uso para criar uma nova classificação. |
| CU-MET-021 | AtualizarClassificacao | `AtualizarClassificacaoUseCase` | Caso de uso para atualizar uma classificação. |
| CU-MET-022 | ConsultarClassificacao | `ConsultarClassificacaoUseCase` | Caso de uso para buscar classificações. |
| CU-MET-023 | BuscarClassificacao | `BuscarClassificacaoUseCase` | Caso de uso para buscar classificações. |
| CU-MET-024 | ExcluirClassificacao | `ExcluirClassificacaoUseCase` | Caso de uso para deletar uma classificação. |
| CU-MET-025 | DeletarClassificacao | `DeletarClassificacaoUseCase` | Caso de uso para deletar uma classificação. |
| CU-MET-026 | RegistrarTaxonomia | `RegistrarTaxonomiaUseCase` | Caso de uso para criar uma nova taxonomia. |
| CU-MET-027 | CriarTaxonomia | `CriarTaxonomiaUseCase` | Caso de uso para criar uma nova taxonomia. |
| CU-MET-028 | AtualizarTaxonomia | `AtualizarTaxonomiaUseCase` | Caso de uso para atualizar uma taxonomia. |
| CU-MET-029 | ConsultarTaxonomia | `ConsultarTaxonomiaUseCase` | Caso de uso para buscar taxonomias. |
| CU-MET-030 | BuscarTaxonomia | `BuscarTaxonomiaUseCase` | Caso de uso para buscar taxonomias. |
| CU-MET-031 | ListarTaxonomias | `ListarTaxonomiasUseCase` | Caso de uso para buscar taxonomias. |
| CU-MET-032 | ExcluirTaxonomia | `ExcluirTaxonomiaUseCase` | Caso de uso para deletar uma taxonomia. |
| CU-MET-033 | DeletarTaxonomia | `DeletarTaxonomiaUseCase` | Caso de uso para deletar uma taxonomia. |
| CU-MET-034 | RegistrarTermo | `RegistrarTermoUseCase` | Caso de uso para criar um novo termo de taxonomia. |
| CU-MET-035 | CriarTermo | `CriarTermoUseCase` | Caso de uso para criar um novo termo de taxonomia. |
| CU-MET-036 | AtualizarTermo | `AtualizarTermoUseCase` | Caso de uso para atualizar um termo de taxonomia. |
| CU-MET-037 | ConsultarTermo | `ConsultarTermoUseCase` | Caso de uso para buscar termos de taxonomia. |
| CU-MET-038 | BuscarTermo | `BuscarTermoUseCase` | Caso de uso para buscar termos de taxonomia. |
| CU-MET-039 | ListarTermos | `ListarTermosUseCase` | Caso de uso para buscar termos de taxonomia. |
| CU-MET-040 | ExcluirTermo | `ExcluirTermoUseCase` | Caso de uso para deletar um termo de taxonomia. |
| CU-MET-041 | DeletarTermo | `DeletarTermoUseCase` | Caso de uso para deletar um termo de taxonomia. |

---

# 3. Cobertura

Casos de uso no código: **41**. Operações publicadas: **30**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Metadados-Corporativos-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
