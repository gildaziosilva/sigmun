# 026 – Modelo-de-Dominio – Gestão Patrimonial

#### Modelo-de-Dominio – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-026

**Domínio:** Gestão Patrimonial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Patrimonial.md`
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

Este artefato detalha **o modelo de domínio** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| bens | `BemModel` | 17 |
| depreciacoes | `DepreciacaoModel` | 8 |
| transferencias | `TransferenciaModel` | 11 |

---

# 3. Domínios de valor

### TipoBem

| Membro | Valor |
| --- | --- |
| MOVEL | "movel" |
| IMOVEL | "imovel" |
### StatusBem

| Membro | Valor |
| --- | --- |
| EM_USO | "em_uso" |
| OCIOSO | "ocioso" |
| EM_TRANSFERENCIA | "em_transferencia" |
| BAIXADO | "baixado" |
### StatusTransferencia

| Membro | Valor |
| --- | --- |
| PENDENTE | "pendente" |
| CONCLUIDA | "concluida" |
| CANCELADA | "cancelada" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-PAT-001 | o tombo/código do bem é único no município |
| RN-PAT-002 | a depreciação é calculada pelo método linear |
| RN-PAT-003 | bens baixados não podem ser depreciados ou transferidos |
| RN-PAT-010 | uma transferência registra a movimentação entre localizações |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Gestao-Patrimonial-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
