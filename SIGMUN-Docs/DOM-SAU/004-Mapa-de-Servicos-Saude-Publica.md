# 004 – Mapa-de-Servicos – Saúde Pública

#### Mapa-de-Servicos – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-004

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

Este artefato detalha **o mapa de serviços** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/sau`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/sau/agendamentos` | agendamentos | Listar Agendamentos |
| POST | `/api/v1/sau/agendamentos` | agendamentos | Agendar |
| POST | `/api/v1/sau/agendamentos/{agendamento_id}/cancelar` | agendamentos | Cancelar |
| POST | `/api/v1/sau/agendamentos/{agendamento_id}/confirmar` | agendamentos | Confirmar |
| POST | `/api/v1/sau/agendamentos/{agendamento_id}/realizar` | agendamentos | Realizar |
| POST | `/api/v1/sau/atendimentos` | atendimentos | Registrar Atendimento |
| POST | `/api/v1/sau/dispensacoes` | dispensacoes | Dispensar |
| GET | `/api/v1/sau/medicamentos` | medicamentos | Listar Medicamentos |
| POST | `/api/v1/sau/medicamentos` | medicamentos | Cadastrar Medicamento |
| POST | `/api/v1/sau/medicamentos/{medicamento_id}/repor` | medicamentos | Repor |
| GET | `/api/v1/sau/pacientes` | pacientes | Listar Pacientes |
| POST | `/api/v1/sau/pacientes` | pacientes | Cadastrar Paciente |
| GET | `/api/v1/sau/pacientes/{paciente_id}` | pacientes | Obter Paciente |
| GET | `/api/v1/sau/pacientes/{paciente_id}/prontuario` | pacientes | Obter Prontuario |
| GET | `/api/v1/sau/regulacoes` | regulacoes | Listar Regulacoes |
| POST | `/api/v1/sau/regulacoes` | regulacoes | Solicitar |
| POST | `/api/v1/sau/regulacoes/{regulacao_id}/autorizar` | regulacoes | Autorizar |
| POST | `/api/v1/sau/regulacoes/{regulacao_id}/negar` | regulacoes | Negar |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| agendamentos | 5 |
| atendimentos | 1 |
| dispensacoes | 1 |
| medicamentos | 3 |
| pacientes | 4 |
| regulacoes | 4 |

---

# 4. Lacunas a validar

* Definir a integração com o prontuário estadual.
* Definir a regra de dispensação por tipo de medicamento.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Saude-Publica-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
