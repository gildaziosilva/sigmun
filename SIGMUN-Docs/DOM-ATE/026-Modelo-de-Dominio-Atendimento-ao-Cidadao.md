# 026 – Modelo-de-Dominio – Atendimento ao Cidadão

#### Modelo-de-Dominio – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-026

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **o modelo de domínio** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| atendimentos | `AtendimentoModel` | 13 |
| avaliacoes_atendimento | `AvaliacaoAtendimentoModel` | 11 |
| canais_atendimento | `CanalAtendimentoModel` | 11 |
| chamadas | `ChamadaModel` | 15 |
| encaminhamentos | `EncaminhamentoModel` | 12 |
| eventos_outbox | `EventoOutboxModel` | 11 |
| filas_atendimento | `FilaAtendimentoModel` | 11 |
| guiches | `GuicheModel` | 11 |
| senhas | `SenhaModel` | 14 |
| servicos_atendimento | `ServicoAtendimentoModel` | 11 |
| triagens | `TriagemModel` | 12 |
| unidades_atendimento | `UnidadeAtendimentoModel` | 11 |

---

# 3. Domínios de valor

### StatusAtendimento

| Membro | Valor |
| --- | --- |
| AGUARDANDO | "aguardando" |
| EM_ANDAMENTO | "em_andamento" |
| CONCLUIDO | "concluido" |
| ENCERRADO | "encerrado" |
| CANCELADO | "cancelado" |
### StatusSenha

| Membro | Valor |
| --- | --- |
| EMITIDA | "emitida" |
| CHAMADA | "chamada" |
| ATENDIDA | "atendida" |
| RECHAMADA | "rechamada" |
| NAO_COMPARECEU | "nao_compareceu" |
| CANCELADA | "cancelada" |
### TipoCanal

| Membro | Valor |
| --- | --- |
| PRESENCIAL | "presencial" |
| TELEFONE | "telefone" |
| EMAIL | "email" |
| CHAT | "chat" |
| PORTAL | "portal" |
| MOBILE | "mobile" |
### PrioridadeAtendimento

| Membro | Valor |
| --- | --- |
| BAIXA | 1 |
| NORMAL | 2 |
| ALTA | 3 |
| URGENTE | 4 |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-ATE-001 | a triagem identifica serviço, canal e prioridade. |
| RN-ATE-002 | a fila respeita prioridade e ordem de chegada. |
| RN-ATE-003 | o registro do atendimento exige o guichê que o executou. |
| RN-ATE-004 | a avaliação registra nota e comentário do cidadão. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Atendimento-ao-Cidadao-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
