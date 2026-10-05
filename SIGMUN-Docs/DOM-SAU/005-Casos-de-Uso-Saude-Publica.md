# 005 – Casos-de-Uso – Saúde Pública

#### Casos-de-Uso – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-005

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **os casos de uso** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-SAU-001 | CadastrarPaciente | `CadastrarPacienteUseCase` | Cadastra um paciente (RN-SAU-001). |
| CU-SAU-002 | RegistrarAtendimento | `RegistrarAtendimentoUseCase` | Registra atendimento no prontuario (RN-SAU-010). |
| CU-SAU-003 | AgendarConsulta | `AgendarConsultaUseCase` | Agenda consulta/exame SUS (RN-SAU-020). |
| CU-SAU-004 | ConfirmarAgendamento | `ConfirmarAgendamentoUseCase` | Confirma agendamento. |
| CU-SAU-005 | CancelarAgendamento | `CancelarAgendamentoUseCase` | Cancela agendamento. |
| CU-SAU-006 | RealizarAgendamento | `RealizarAgendamentoUseCase` | Marca comparecimento. |
| CU-SAU-007 | SolicitarRegulacao | `SolicitarRegulacaoUseCase` | Abre solicitacao na central (RN-SAU-030). |
| CU-SAU-008 | AutorizarRegulacao | `AutorizarRegulacaoUseCase` | Autoriza solicitacao. |
| CU-SAU-009 | NegarRegulacao | `NegarRegulacaoUseCase` | Nega solicitacao. |
| CU-SAU-010 | CadastrarMedicamento | `CadastrarMedicamentoUseCase` | Cadastra medicamento. |
| CU-SAU-011 | ReporEstoque | `ReporEstoqueUseCase` | Registra entrada de estoque. |
| CU-SAU-012 | DispensarMedicamento | `DispensarMedicamentoUseCase` | Dispensa medicamento com baixa atomica (RN-SAU-040). |

---

# 3. Cobertura

Casos de uso no código: **12**. Operações publicadas: **18**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Saude-Publica-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
