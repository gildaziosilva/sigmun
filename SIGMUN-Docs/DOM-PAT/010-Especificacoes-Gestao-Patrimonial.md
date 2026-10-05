# 010 – Especificacoes – Gestão Patrimonial

#### Especificacoes – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-010

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

Este artefato detalha **as especificações** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/pat/bens` | bens | JSON (payload do domínio) |
| POST | `/api/v1/pat/bens` | bens | JSON (payload do domínio) |
| GET | `/api/v1/pat/bens/{bem_id}` | bens | JSON (payload do domínio) |
| POST | `/api/v1/pat/bens/{bem_id}/baixar` | bens | JSON (payload do domínio) |
| GET | `/api/v1/pat/bens/{bem_id}/depreciacoes` | bens | JSON (payload do domínio) |
| POST | `/api/v1/pat/bens/{bem_id}/depreciar` | bens | JSON (payload do domínio) |
| POST | `/api/v1/pat/transferencias` | transferencias | JSON (payload do domínio) |
| POST | `/api/v1/pat/transferencias/{transferencia_id}/concluir` | transferencias | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
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

**Documento:** 010-Gestao-Patrimonial-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
