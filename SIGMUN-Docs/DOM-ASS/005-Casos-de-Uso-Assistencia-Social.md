# 005 – Casos-de-Uso – Assistência Social

#### Casos-de-Uso – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-005

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **os casos de uso** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-ASS-001 | CadastrarFamilia | `CadastrarFamiliaUseCase` | Cadastra uma família no CadÚnico (RN-ASS-001). |
| CU-ASS-002 | CadastrarPessoa | `CadastrarPessoaUseCase` | Cadastra uma pessoa no CadÚnico (RN-ASS-002). |
| CU-ASS-003 | CadastrarUnidade | `CadastrarUnidadeUseCase` | Cadastra uma unidade de assistência social. |
| CU-ASS-004 | AtualizarFamilia | `AtualizarFamiliaUseCase` | Atualiza o cadastro de uma família do CadÚnico. |
| CU-ASS-005 | ExcluirFamilia | `ExcluirFamiliaUseCase` | Exclui (soft-delete) uma família do CadÚnico. |
| CU-ASS-006 | AtualizarPessoa | `AtualizarPessoaUseCase` | Atualiza o cadastro de uma pessoa do CadÚnico. |
| CU-ASS-007 | ExcluirPessoa | `ExcluirPessoaUseCase` | Exclui (soft-delete) uma pessoa do CadÚnico. |
| CU-ASS-008 | AtualizarUnidade | `AtualizarUnidadeUseCase` | Atualiza o cadastro de uma unidade de assistência social. |
| CU-ASS-009 | ExcluirUnidade | `ExcluirUnidadeUseCase` | Exclui (soft-delete) uma unidade de assistência social. |
| CU-ASS-010 | SolicitarBeneficio | `SolicitarBeneficioUseCase` | Solicita um benefício eventual (RN-ASS-003). |
| CU-ASS-011 | AprovarBeneficio | `AprovarBeneficioUseCase` | Aprova um benefício eventual. |
| CU-ASS-012 | NegarBeneficio | `NegarBeneficioUseCase` | Nega um benefício eventual. |
| CU-ASS-013 | EntregarBeneficio | `EntregarBeneficioUseCase` | Registra entrega de benefício eventual. |
| CU-ASS-014 | CancelarBeneficio | `CancelarBeneficioUseCase` | Cancela um benefício eventual. |
| CU-ASS-015 | RegistrarAtendimento | `RegistrarAtendimentoUseCase` | Registra atendimento social (RN-ASS-004). |

---

# 3. Cobertura

Casos de uso no código: **15**. Operações publicadas: **31**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Assistencia-Social-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
