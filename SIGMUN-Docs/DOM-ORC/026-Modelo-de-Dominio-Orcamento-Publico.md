# 026 – Modelo-de-Dominio – Orçamento Público

#### Modelo-de-Dominio – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-026

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

Este artefato detalha **o modelo de domínio** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| dotacoes | `DotacaoModel` | 18 |
| ldos | `LDOModel` | 14 |
| loas | `LOAModel` | 14 |
| ppas | `PPAModel` | 12 |
| reservas | `ReservaModel` | 16 |

---

# 3. Domínios de valor

### StatusDotacao

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| ENCERRADA | "encerrada" |
### StatusLDO

| Membro | Valor |
| --- | --- |
| ELABORACAO | "elaboracao" |
| APROVADA | "aprovada" |
| SANCIONADA | "sancionada" |
| CANCELADA | "cancelada" |
### StatusLOA

| Membro | Valor |
| --- | --- |
| ELABORACAO | "elaboracao" |
| APROVADA | "aprovada" |
| PUBLICADA | "publicada" |
| CANCELADA | "cancelada" |
### StatusPPA

| Membro | Valor |
| --- | --- |
| ELABORACAO | "elaboracao" |
| VIGENTE | "vigente" |
| ENCERRADO | "encerrado" |
| CANCELADO | "cancelado" |
### StatusReserva

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| CONVERTIDA | "convertida" |
| CANCELADA | "cancelada" |
| EXPIRADA | "expirada" |

---

# 4. Regras

| ID | Descrição |
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

**Documento:** 026-Orcamento-Publico-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
