# 010 – Especificacoes – Orçamento Público

#### Especificacoes – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-010

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **as especificações** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| POST | `/api/v1/orc/dotacoes` | dotacoes | JSON (payload do domínio) |
| POST | `/api/v1/orc/dotacoes/{dotacao_id}/anular` | dotacoes | JSON (payload do domínio) |
| GET | `/api/v1/orc/dotacoes/{dotacao_id}/saldo` | dotacoes | JSON (payload do domínio) |
| POST | `/api/v1/orc/dotacoes/{dotacao_id}/suplementar` | dotacoes | JSON (payload do domínio) |
| POST | `/api/v1/orc/ldos` | ldos | JSON (payload do domínio) |
| POST | `/api/v1/orc/ldos/{ldo_id}/sancionar` | ldos | JSON (payload do domínio) |
| POST | `/api/v1/orc/loas` | loas | JSON (payload do domínio) |
| POST | `/api/v1/orc/loas/{loa_id}/publicar` | loas | JSON (payload do domínio) |
| POST | `/api/v1/orc/ppas` | ppas | JSON (payload do domínio) |
| POST | `/api/v1/orc/ppas/{ppa_id}/publicar` | ppas | JSON (payload do domínio) |
| POST | `/api/v1/orc/reservas` | reservas | JSON (payload do domínio) |
| POST | `/api/v1/orc/reservas/{reserva_id}/cancelar` | reservas | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-ORC-001 | quadriênio (ano_inicial/ano_final) é único por município |
| RN-ORC-002 | PPA nasce em elaboração; só PPA publicado pode fundamentar LDO/LOA |
| RN-ORC-003 | PPA encerrado é terminal (imutável) |
| RN-ORC-010 | exercício é único no município |
| RN-ORC-011 | LDO exige PPA vigente que cubra o exercício |
| RN-ORC-012 | LDO sancionada é terminal (imutável) |
| RN-ORC-020 | exercício é único no município |
| RN-ORC-021 | LOA exige LDO sancionada do mesmo exercício |
| RN-ORC-022 | LOA publicada é terminal para edição (apenas suplementação via dotação) |
| RN-ORC-030 | código da dotação é único por exercício |
| RN-ORC-031 | suplementação/anulação nunca deixa valor atualizado negativo |
| RN-ORC-032 | reserva/empenho exige saldo disponível |
| RN-ORC-033 | dotação encerrada é terminal (imutável) |
| RN-ORC-040 | reserva consome saldo disponível da dotação no ato da criação |
| RN-ORC-041 | reserva ATIVA pode ser cancelada (devolve saldo) ou convertida |
| RN-ORC-042 | reserva CANCELADA/CONVERTIDA/EXPIRADA é terminal |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Orcamento-Publico-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
