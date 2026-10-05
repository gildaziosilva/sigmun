# 005 – Casos-de-Uso – Educação Pública

#### Casos-de-Uso – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-005

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **os casos de uso** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-EDU-001 | CadastrarAluno | `CadastrarAlunoUseCase` | Cadastra um aluno (RN-EDU-001). |
| CU-EDU-002 | RealizarMatricula | `RealizarMatriculaUseCase` | Realiza a matricula do aluno (RN-EDU-010). |
| CU-EDU-003 | TransferirMatricula | `TransferirMatriculaUseCase` | Transfere a matricula para outra escola (RN-EDU-010). |
| CU-EDU-004 | CancelarMatricula | `CancelarMatriculaUseCase` | Cancela a matricula vigente (RN-EDU-010). |
| CU-EDU-005 | ConcluirMatricula | `ConcluirMatriculaUseCase` | Conclui a matricula (fim do ano letivo) (RN-EDU-010). |
| CU-EDU-006 | RegistrarLancamentoDiario | `RegistrarLancamentoDiarioUseCase` | Registra frequencia/nota no diario digital (RN-EDU-020). |
| CU-EDU-007 | CadastrarRotaTransporte | `CadastrarRotaTransporteUseCase` | Cadastra uma rota de transporte escolar (RN-EDU-030). |
| CU-EDU-008 | InativarRotaTransporte | `InativarRotaTransporteUseCase` | Inativa rota (encerra novas passagens). |
| CU-EDU-009 | AtivarRotaTransporte | `AtivarRotaTransporteUseCase` | Reativa rota de transporte escolar. |
| CU-EDU-010 | RegistrarPassagem | `RegistrarPassagemUseCase` | Registra passagem com cheque de vagas (RN-EDU-030). |
| CU-EDU-011 | CadastrarItemMerenda | `CadastrarItemMerendaUseCase` | Cadastra item do estoque de merenda. |
| CU-EDU-012 | ReporEstoqueMerenda | `ReporEstoqueMerendaUseCase` | Registra entrada de estoque de merenda. |
| CU-EDU-013 | DistribuirMerenda | `DistribuirMerendaUseCase` | Distribui merenda com baixa atomica de estoque (RN-EDU-040). |

---

# 3. Cobertura

Casos de uso no código: **13**. Operações publicadas: **25**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Educacao-Publica-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
