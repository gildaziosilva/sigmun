# 010 – Especificacoes – Atendimento ao Cidadão

#### Especificacoes – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-010

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

Este artefato detalha **as especificações** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/ate/atendimentos` | atendimentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/atendimentos/iniciar` | atendimentos | JSON (payload do domínio) |
| GET | `/api/v1/ate/atendimentos/{atendimento_id}` | atendimentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/atendimentos/{atendimento_id}/cancelar` | atendimentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/atendimentos/{atendimento_id}/concluir` | atendimentos | JSON (payload do domínio) |
| GET | `/api/v1/ate/atendimentos/{atendimento_id}/encaminhamentos` | atendimentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/avaliacoes` | avaliacoes | JSON (payload do domínio) |
| GET | `/api/v1/ate/avaliacoes/{avaliacao_id}` | avaliacoes | JSON (payload do domínio) |
| POST | `/api/v1/ate/encaminhamentos` | encaminhamentos | JSON (payload do domínio) |
| GET | `/api/v1/ate/encaminhamentos/{encaminhamento_id}` | encaminhamentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/encaminhamentos/{encaminhamento_id}/concluir` | encaminhamentos | JSON (payload do domínio) |
| POST | `/api/v1/ate/filas` | filas | JSON (payload do domínio) |
| POST | `/api/v1/ate/filas/{fila_id}/fechar` | filas | JSON (payload do domínio) |
| GET | `/api/v1/ate/health` | health | JSON (payload do domínio) |
| POST | `/api/v1/ate/senhas` | senhas | JSON (payload do domínio) |
| POST | `/api/v1/ate/senhas/{senha_id}/atender` | senhas | JSON (payload do domínio) |
| POST | `/api/v1/ate/senhas/{senha_id}/chamar` | senhas | JSON (payload do domínio) |
| POST | `/api/v1/ate/senhas/{senha_id}/rechamar` | senhas | JSON (payload do domínio) |
| POST | `/api/v1/ate/triagens` | triagens | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
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

**Documento:** 010-Atendimento-ao-Cidadao-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
