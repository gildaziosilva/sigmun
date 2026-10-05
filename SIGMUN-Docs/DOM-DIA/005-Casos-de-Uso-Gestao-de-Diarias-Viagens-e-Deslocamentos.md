# 005 – Casos-de-Uso – Gestão de Diárias, Viagens e Deslocamentos

#### Casos-de-Uso – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-005

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **os casos de uso** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-DIA-001 | CriarViagem | `CriarViagemUseCase` | Caso de uso para criar uma nova viagem. |
| CU-DIA-002 | AtualizarViagem | `AtualizarViagemUseCase` | Caso de uso para atualizar uma viagem existente. |
| CU-DIA-003 | TramitarViagem | `TramitarViagemUseCase` | Caso de uso para tramitar uma viagem entre unidades. |
| CU-DIA-004 | VisitarViagem | `VisitarViagemUseCase` | Caso de uso para registrar visita em viagem (registra chegada). |
| CU-DIA-005 | CriarDiaria | `CriarDiariaUseCase` | Caso de uso para criar uma diária. |
| CU-DIA-006 | AtualizarDiaria | `AtualizarDiariaUseCase` | Caso de uso para atualizar uma diária. |
| CU-DIA-007 | SolicitarDiaria | `SolicitarDiariaUseCase` | Caso de uso para solicitar uma diária (cria e registra a solicitação). |
| CU-DIA-008 | CriarPrestacaoContas | `CriarPrestacaoContasUseCase` | Caso de uso para criar uma prestação de contas (abertura). |
| CU-DIA-009 | AprovarPrestacao | `AprovarPrestacaoUseCase` | Caso de uso para aprovar uma prestação de contas. |
| CU-DIA-010 | GlosarPrestacao | `GlosarPrestacaoUseCase` | Caso de uso para glosar uma prestação de contas. |
| CU-DIA-011 | RestituirPrestacao | `RestituirPrestacaoUseCase` | Caso de uso para restituir valor glosado. |
| CU-DIA-012 | AutorizarDiaria | `AutorizarDiariaUseCase` | Caso de uso para autorizar uma diária. |
| CU-DIA-013 | CalcularDiaria | `CalcularDiariaUseCase` | Caso de uso para calcular o valor da diária. |
| CU-DIA-014 | ConcederDiaria | `ConcederDiariaUseCase` | Caso de uso para confirmar concessão da diária. |
| CU-DIA-015 | IniciarPrestacao | `IniciarPrestacaoUseCase` | Caso de uso para iniciar a prestação de contas. |
| CU-DIA-016 | PagarDiaria | `PagarDiariaUseCase` | Caso de uso para registrar pagamento da diária. |
| CU-DIA-017 | ConfirmarConcessao | `ConfirmarConcessaoUseCase` | Caso de uso para confirmar a concessão da diária (RN-DIA-006). |
| CU-DIA-018 | ReverterParaPagamento | `ReverterParaPagamentoUseCase` | Caso de uso para reverter a diária para pagamento (RN-DIA-008). |
| CU-DIA-019 | CancelarDiaria | `CancelarDiariaUseCase` | Caso de uso para cancelar uma diária. |

---

# 3. Cobertura

Casos de uso no código: **19**. Operações publicadas: **20**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Gestao-de-Diarias-Viagens-e-Deslocamentos-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
