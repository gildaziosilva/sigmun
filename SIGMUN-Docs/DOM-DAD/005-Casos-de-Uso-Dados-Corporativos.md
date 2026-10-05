# 005 – Casos-de-Uso – Dados Corporativos

#### Casos-de-Uso – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-005

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

Este artefato detalha **os casos de uso** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-DAD-001 | CriarAtivo | `CriarAtivoUseCase` | Caso de uso para criar um novo ativo de dado. |
| CU-DAD-002 | AtivarAtivo | `AtivarAtivoUseCase` | Caso de uso para ativar um ativo. |
| CU-DAD-003 | DesativarAtivo | `DesativarAtivoUseCase` | Caso de uso para desativar um ativo. |
| CU-DAD-004 | ArquivarAtivo | `ArquivarAtivoUseCase` | Caso de uso para arquivar um ativo. |
| CU-DAD-005 | BuscarAtivo | `BuscarAtivoUseCase` | Caso de uso para buscar ativos. |
| CU-DAD-006 | AtualizarQualidade | `AtualizarQualidadeUseCase` | Caso de uso para atualizar qualidade do ativo. |
| CU-DAD-007 | CriarCatalogo | `CriarCatalogoUseCase` | Caso de uso para criar um novo catálogo. |
| CU-DAD-008 | AtualizarCatalogo | `AtualizarCatalogoUseCase` | Caso de uso para atualizar um catálogo. |
| CU-DAD-009 | BuscarCatalogo | `BuscarCatalogoUseCase` | Caso de uso para buscar catálogos. |
| CU-DAD-010 | DeletarCatalogo | `DeletarCatalogoUseCase` | Caso de uso para deletar um catálogo. |
| CU-DAD-011 | AdicionarAtivoCatalogo | `AdicionarAtivoCatalogoUseCase` | Caso de uso para adicionar ativo ao catálogo. |
| CU-DAD-012 | RemoverAtivoCatalogo | `RemoverAtivoCatalogoUseCase` | Caso de uso para remover ativo do catálogo. |
| CU-DAD-013 | CriarLinhagem | `CriarLinhagemUseCase` | Caso de uso para criar uma nova linhagem. |
| CU-DAD-014 | AtualizarLinhagem | `AtualizarLinhagemUseCase` | Caso de uso para atualizar uma linhagem. |
| CU-DAD-015 | BuscarLinhagem | `BuscarLinhagemUseCase` | Caso de uso para buscar linhagens. |
| CU-DAD-016 | DeletarLinhagem | `DeletarLinhagemUseCase` | Caso de uso para deletar uma linhagem. |
| CU-DAD-017 | CriarPolitica | `CriarPoliticaUseCase` | Caso de uso para criar uma nova política. |
| CU-DAD-018 | AtualizarPolitica | `AtualizarPoliticaUseCase` | Caso de uso para atualizar uma política. |
| CU-DAD-019 | BuscarPolitica | `BuscarPoliticaUseCase` | Caso de uso para buscar políticas. |
| CU-DAD-020 | DeletarPolitica | `DeletarPoliticaUseCase` | Caso de uso para deletar uma política. |
| CU-DAD-021 | AdicionarRegraPolitica | `AdicionarRegraPoliticaUseCase` | Caso de uso para adicionar regra à política. |
| CU-DAD-022 | RemoverRegraPolitica | `RemoverRegraPoliticaUseCase` | Caso de uso para remover regra da política. |
| CU-DAD-023 | AvaliarQualidade | `AvaliarQualidadeUseCase` | Caso de uso para avaliar qualidade de um ativo. |
| CU-DAD-024 | AtualizarQualidadeDados | `AtualizarQualidadeDadosUseCase` | Caso de uso para atualizar qualidade de dados. |
| CU-DAD-025 | BuscarQualidade | `BuscarQualidadeUseCase` | Caso de uso para buscar registros de qualidade. |
| CU-DAD-026 | DeletarQualidade | `DeletarQualidadeUseCase` | Caso de uso para deletar registro de qualidade. |

---

# 3. Cobertura

Casos de uso no código: **26**. Operações publicadas: **29**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Dados-Corporativos-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
