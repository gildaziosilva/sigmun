# 005 – Casos-de-Uso – Cadastro Único Municipal

#### Casos-de-Uso – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-005

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **os casos de uso** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-CUM-001 | RegistrarPessoa | `RegistrarPessoaUseCase` | Orquestra o registro de uma nova pessoa com seus dados de contato. |
| CU-CUM-002 | ConsultarPessoa | `ConsultarPessoaUseCase` | Consulta o agregado Pessoa hidratado (endereços/documentos/contatos). |
| CU-CUM-003 | ListarPessoas | `ListarPessoasUseCase` | Lista pessoas com filtros e paginação. |
| CU-CUM-004 | AtualizarPessoaFisica | `AtualizarPessoaFisicaUseCase` | Atualiza os dados da extensão física de uma pessoa (PATCH parcial). |
| CU-CUM-005 | AtualizarPessoaJuridica | `AtualizarPessoaJuridicaUseCase` | Atualiza os dados da extensão jurídica de uma pessoa (PATCH parcial). |
| CU-CUM-006 | AlterarCategoriaPessoa | `AlterarCategoriaPessoaUseCase` | Altera a categoria cadastral da pessoa. |
| CU-CUM-007 | ExcluirPessoa | `ExcluirPessoaUseCase` | Exclui logicamente a pessoa e seus dados filhos (RN-CUM-007). |
| CU-CUM-008 | RegistrarUnidade | `RegistrarUnidadeUseCase` | Orquestra o registro de uma nova unidade administrativa. |
| CU-CUM-009 | ConsultarUnidade | `ConsultarUnidadeUseCase` | Consulta uma unidade administrativa pelo ID. |
| CU-CUM-010 | ListarUnidades | `ListarUnidadesUseCase` | Lista unidades administrativas com paginação. |
| CU-CUM-011 | AtualizarUnidade | `AtualizarUnidadeUseCase` | Atualiza dados de uma unidade administrativa (PATCH parcial). |
| CU-CUM-012 | ExcluirUnidade | `ExcluirUnidadeUseCase` | Exclui logicamente uma unidade administrativa (RN-CUM-007). |

---

# 3. Cobertura

Casos de uso no código: **12**. Operações publicadas: **12**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Cadastro-Unico-Municipal-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
