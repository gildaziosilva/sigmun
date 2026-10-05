# 010 – Especificacoes – Ouvidoria

#### Especificacoes – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-010

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **as especificações** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/ouv/denuncias` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/denuncias` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/denuncias/{denuncia_id}/encaminhar` | v | JSON (payload do domínio) |
| GET | `/api/v1/ouv/estatisticas` | v | JSON (payload do domínio) |
| GET | `/api/v1/ouv/manifestacoes` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/manifestacoes` | v | JSON (payload do domínio) |
| GET | `/api/v1/ouv/manifestacoes-vencendo` | v | JSON (payload do domínio) |
| GET | `/api/v1/ouv/manifestacoes/{identificador}` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/avaliar` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/prorrogar` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/responder` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/status` | v | JSON (payload do domínio) |
| GET | `/api/v1/ouv/pedidos-lai` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/pedidos-lai` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/pedidos-lai/{pedido_id}/recurso` | v | JSON (payload do domínio) |
| POST | `/api/v1/ouv/pedidos-lai/{recurso_id}/decidir-recurso` | v | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-OU-001 | toda manifestação recebe protocolo e prazo. |
| RN-OU-002 | a denúncia admite proteção de identidade. |
| RN-OU-003 | o pedido de informação segue prazo próprio e admite recurso. |
| RN-OU-004 | o encerramento não apaga o histórico da manifestação. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Ouvidoria-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
