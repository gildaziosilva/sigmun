# 010 – Especificacoes – Metadados Corporativos

#### Especificacoes – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-010

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **as especificações** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/met/classificacoes` | classificacoes | JSON (payload do domínio) |
| POST | `/api/v1/met/classificacoes` | classificacoes | JSON (payload do domínio) |
| DELETE | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | JSON (payload do domínio) |
| GET | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | JSON (payload do domínio) |
| PUT | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | JSON (payload do domínio) |
| GET | `/api/v1/met/entidades/{entidade_tipo}/{entidade_id}/valores` | entidades | JSON (payload do domínio) |
| GET | `/api/v1/met/metadados` | metadados | JSON (payload do domínio) |
| POST | `/api/v1/met/metadados` | metadados | JSON (payload do domínio) |
| DELETE | `/api/v1/met/metadados/{metadado_id}` | metadados | JSON (payload do domínio) |
| GET | `/api/v1/met/metadados/{metadado_id}` | metadados | JSON (payload do domínio) |
| PUT | `/api/v1/met/metadados/{metadado_id}` | metadados | JSON (payload do domínio) |
| POST | `/api/v1/met/metadados/{metadado_id}/ativar` | metadados | JSON (payload do domínio) |
| POST | `/api/v1/met/metadados/{metadado_id}/desativar` | metadados | JSON (payload do domínio) |
| GET | `/api/v1/met/taxonomias` | taxonomias | JSON (payload do domínio) |
| POST | `/api/v1/met/taxonomias` | taxonomias | JSON (payload do domínio) |
| DELETE | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | JSON (payload do domínio) |
| GET | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | JSON (payload do domínio) |
| PUT | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | JSON (payload do domínio) |
| GET | `/api/v1/met/taxonomias/{taxonomia_id}/termos` | taxonomias | JSON (payload do domínio) |
| GET | `/api/v1/met/termos` | termos | JSON (payload do domínio) |
| POST | `/api/v1/met/termos` | termos | JSON (payload do domínio) |
| DELETE | `/api/v1/met/termos/{termo_id}` | termos | JSON (payload do domínio) |
| GET | `/api/v1/met/termos/{termo_id}` | termos | JSON (payload do domínio) |
| PUT | `/api/v1/met/termos/{termo_id}` | termos | JSON (payload do domínio) |
| GET | `/api/v1/met/termos/{termo_id}/filhos` | termos | JSON (payload do domínio) |
| GET | `/api/v1/met/valores` | valores | JSON (payload do domínio) |
| POST | `/api/v1/met/valores` | valores | JSON (payload do domínio) |
| DELETE | `/api/v1/met/valores/{valor_id}` | valores | JSON (payload do domínio) |
| GET | `/api/v1/met/valores/{valor_id}` | valores | JSON (payload do domínio) |
| PUT | `/api/v1/met/valores/{valor_id}` | valores | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-MET-001 | metadado não pode ser duplicado para a mesma entidade e atributo. |
| RN-MET-002 | classificação vigente determina o acesso e a obrigatoriedade. |
| RN-MET-003 | taxonomiaterms devem referenciar a taxonomia vigente. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Metadados-Corporativos-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
