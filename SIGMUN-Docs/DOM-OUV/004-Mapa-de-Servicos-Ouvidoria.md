# 004 – Mapa-de-Servicos – Ouvidoria

#### Mapa-de-Servicos – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-004

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

Este artefato detalha **o mapa de serviços** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/ou`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/ouv/denuncias` | v | Listar Denuncias |
| POST | `/api/v1/ouv/denuncias` | v | Registrar Denuncia |
| POST | `/api/v1/ouv/denuncias/{denuncia_id}/encaminhar` | v | Encaminhar Denuncia |
| GET | `/api/v1/ouv/estatisticas` | v | Obter Estatisticas |
| GET | `/api/v1/ouv/manifestacoes` | v | Listar Manifestacoes |
| POST | `/api/v1/ouv/manifestacoes` | v | Registrar Manifestacao |
| GET | `/api/v1/ouv/manifestacoes-vencendo` | v | Manifestacoes Vencendo Prazo |
| GET | `/api/v1/ouv/manifestacoes/{identificador}` | v | Obter Manifestacao |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/avaliar` | v | Avaliar Manifestacao |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/prorrogar` | v | Prorrogar Prazo |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/responder` | v | Responder Manifestacao |
| POST | `/api/v1/ouv/manifestacoes/{manifestacao_id}/status` | v | Alterar Status |
| GET | `/api/v1/ouv/pedidos-lai` | v | Listar Pedidos Lai |
| POST | `/api/v1/ouv/pedidos-lai` | v | Registrar Pedido Lai |
| POST | `/api/v1/ouv/pedidos-lai/{pedido_id}/recurso` | v | Interpor Recurso Lai |
| POST | `/api/v1/ouv/pedidos-lai/{recurso_id}/decidir-recurso` | v | Decidir Recurso Lai |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| v | 16 |

---

# 4. Lacunas a validar

* Definir o prazo legal por tipo de manifestação e por LAI.
* Definir a integração com o FalaBR / e-OUV.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Ouvidoria-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
