# 026 – Modelo-de-Dominio – Saúde Pública

#### Modelo-de-Dominio – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-026

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

Este artefato detalha **o modelo de domínio** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| agendamentos | `AgendamentoModel` | 11 |
| atendimentos | `AtendimentoModel` | 11 |
| dispensacoes | `DispensacaoModel` | 8 |
| medicamentos | `MedicamentoModel` | 9 |
| pacientes | `PacienteModel` | 15 |
| regulacoes | `RegulacaoModel` | 11 |

---

# 3. Domínios de valor

### TipoAtendimento

| Membro | Valor |
| --- | --- |
| CONSULTA | "consulta" |
| RETORNO | "retorno" |
| URGENCIA | "urgencia" |
| VISITA_DOMICILIAR | "visita_domiciliar" |
| TELEATENDIMENTO | "teleatendimento" |
### StatusAgendamento

| Membro | Valor |
| --- | --- |
| AGENDADO | "agendado" |
| CONFIRMADO | "confirmado" |
| CANCELADO | "cancelado" |
| REALIZADO | "realizado" |
| FALTA | "falta" |
### PrioridadeRegulacao

| Membro | Valor |
| --- | --- |
| ROTINA | "rotina" |
| PRIORITARIA | "prioritaria" |
| URGENCIA | "urgencia" |
### StatusRegulacao

| Membro | Valor |
| --- | --- |
| SOLICITADA | "solicitada" |
| AUTORIZADA | "autorizada" |
| NEGADA | "negada" |
| AGENDADA | "agendada" |
### Sexo

| Membro | Valor |
| --- | --- |
| MASCULINO | "masculino" |
| FEMININO | "feminino" |
| IGNORADO | "ignorado" |
### StatusPaciente

| Membro | Valor |
| --- | --- |
| ATIVO | "ativo" |
| INATIVO | "inativo" |
| OBITO | "obito" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-SAU-001 | o CNS do paciente é único no cadastro municipal |
| RN-SAU-002 | prontuário reúne atendimentos em ordem cronológica |
| RN-SAU-003 | a regulação é autorizada conforme a prioridade registrada. |
| RN-SAU-004 | a dispensação referencia o paciente e o medicamento administered. |
| RN-SAU-010 | atendimento exige paciente e profissional/estabelecimento |
| RN-SAU-020 | agendamento nasce ``agendado`` e só transita para |
| RN-SAU-030 | regulação nasce ``solicitada`` e transita para |
| RN-SAU-040 | dispensação exige estoque suficiente; baixa é atômica no |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Saude-Publica-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
