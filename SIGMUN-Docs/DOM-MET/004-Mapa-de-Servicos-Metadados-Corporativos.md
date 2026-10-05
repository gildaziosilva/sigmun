# 004 – Mapa-de-Servicos – Metadados Corporativos

#### Mapa-de-Servicos – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-004

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

Este artefato detalha **o mapa de serviços** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/met`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/met/classificacoes` | classificacoes | Lista classificações |
| POST | `/api/v1/met/classificacoes` | classificacoes | Cria uma nova classificação |
| DELETE | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | Deleta uma classificação |
| GET | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | Busca uma classificação por ID |
| PUT | `/api/v1/met/classificacoes/{classificacao_id}` | classificacoes | Atualiza uma classificação |
| GET | `/api/v1/met/entidades/{entidade_tipo}/{entidade_id}/valores` | entidades | Busca todos os valores de metadados de uma entidade |
| GET | `/api/v1/met/metadados` | metadados | Lista metadados |
| POST | `/api/v1/met/metadados` | metadados | Cria um novo metadado |
| DELETE | `/api/v1/met/metadados/{metadado_id}` | metadados | Deleta um metadado |
| GET | `/api/v1/met/metadados/{metadado_id}` | metadados | Busca um metadado por ID |
| PUT | `/api/v1/met/metadados/{metadado_id}` | metadados | Atualiza um metadado |
| POST | `/api/v1/met/metadados/{metadado_id}/ativar` | metadados | Ativa um metadado |
| POST | `/api/v1/met/metadados/{metadado_id}/desativar` | metadados | Desativa um metadado |
| GET | `/api/v1/met/taxonomias` | taxonomias | Lista taxonomias |
| POST | `/api/v1/met/taxonomias` | taxonomias | Cria uma nova taxonomia |
| DELETE | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | Deleta uma taxonomia |
| GET | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | Busca uma taxonomia por ID |
| PUT | `/api/v1/met/taxonomias/{taxonomia_id}` | taxonomias | Atualiza uma taxonomia |
| GET | `/api/v1/met/taxonomias/{taxonomia_id}/termos` | taxonomias | Busca todos os termos de uma taxonomia |
| GET | `/api/v1/met/termos` | termos | Lista termos de taxonomia |
| POST | `/api/v1/met/termos` | termos | Cria um novo termo de taxonomia |
| DELETE | `/api/v1/met/termos/{termo_id}` | termos | Deleta um termo de taxonomia |
| GET | `/api/v1/met/termos/{termo_id}` | termos | Busca um termo por ID |
| PUT | `/api/v1/met/termos/{termo_id}` | termos | Atualiza um termo de taxonomia |
| GET | `/api/v1/met/termos/{termo_id}/filhos` | termos | Busca os termos filhos diretos de um termo |
| GET | `/api/v1/met/valores` | valores | Lista valores |
| POST | `/api/v1/met/valores` | valores | Atribui um valor de metadado a uma entidade |
| DELETE | `/api/v1/met/valores/{valor_id}` | valores | Remove um valor de metadado |
| GET | `/api/v1/met/valores/{valor_id}` | valores | Busca um valor de metadado por ID |
| PUT | `/api/v1/met/valores/{valor_id}` | valores | Atualiza o valor de um valor de metadado |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| classificacoes | 5 |
| entidades | 1 |
| metadados | 7 |
| taxonomias | 6 |
| termos | 6 |
| valores | 5 |

---

# 4. Lacunas a validar

* Definir a curadoria periódica de metadados obsoletos.
* Definir a integração automática com o catálogo do DOM-DAD.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Metadados-Corporativos-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
