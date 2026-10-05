# 004 – Mapa-de-Servicos – Dados Corporativos

#### Mapa-de-Servicos – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-004

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **o mapa de serviços** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/dad`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/dad/ativos` | ativos | Lista ativos de dados |
| POST | `/api/v1/dad/ativos` | ativos | Cria um novo ativo de dado |
| GET | `/api/v1/dad/ativos/{ativo_id}` | ativos | Busca ativo por ID |
| POST | `/api/v1/dad/ativos/{ativo_id}/arquivar` | ativos | Arquiva um ativo |
| POST | `/api/v1/dad/ativos/{ativo_id}/ativar` | ativos | Ativa um ativo |
| POST | `/api/v1/dad/ativos/{ativo_id}/desativar` | ativos | Desativa um ativo |
| GET | `/api/v1/dad/catalogos` | catalogos | Lista catálogos |
| POST | `/api/v1/dad/catalogos` | catalogos | Cria um novo catálogo |
| DELETE | `/api/v1/dad/catalogos/{catalogo_id}` | catalogos | Deleta um catálogo |
| GET | `/api/v1/dad/catalogos/{catalogo_id}` | catalogos | Busca catálogo por ID |
| PATCH | `/api/v1/dad/catalogos/{catalogo_id}` | catalogos | Atualiza um catálogo |
| DELETE | `/api/v1/dad/catalogos/{catalogo_id}/ativos/{ativo_id}` | catalogos | Remove ativo do catálogo |
| POST | `/api/v1/dad/catalogos/{catalogo_id}/ativos/{ativo_id}` | catalogos | Adiciona ativo ao catálogo |
| GET | `/api/v1/dad/linhagens` | linhagens | Lista linhagens |
| POST | `/api/v1/dad/linhagens` | linhagens | Cria uma nova linhagem |
| DELETE | `/api/v1/dad/linhagens/{linhagem_id}` | linhagens | Deleta uma linhagem |
| GET | `/api/v1/dad/linhagens/{linhagem_id}` | linhagens | Busca linhagem por ID |
| PATCH | `/api/v1/dad/linhagens/{linhagem_id}` | linhagens | Atualiza uma linhagem |
| GET | `/api/v1/dad/politicas` | politicas | Lista políticas |
| POST | `/api/v1/dad/politicas` | politicas | Cria uma nova política |
| DELETE | `/api/v1/dad/politicas/{politica_id}` | politicas | Deleta uma política |
| GET | `/api/v1/dad/politicas/{politica_id}` | politicas | Busca política por ID |
| PATCH | `/api/v1/dad/politicas/{politica_id}` | politicas | Atualiza uma política |
| POST | `/api/v1/dad/politicas/{politica_id}/regras` | politicas | Adiciona regra à política |
| GET | `/api/v1/dad/qualidade` | qualidade | Lista registros de qualidade |
| POST | `/api/v1/dad/qualidade` | qualidade | Avalia qualidade de um ativo |
| DELETE | `/api/v1/dad/qualidade/{qualidade_id}` | qualidade | Deleta registro de qualidade |
| GET | `/api/v1/dad/qualidade/{qualidade_id}` | qualidade | Busca registro de qualidade por ID |
| PATCH | `/api/v1/dad/qualidade/{qualidade_id}` | qualidade | Atualiza registro de qualidade |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| ativos | 6 |
| catalogos | 7 |
| linhagens | 5 |
| politicas | 6 |
| qualidade | 5 |

---

# 4. Lacunas a validar

* Definir o calendário de avaliação de qualidade por criticidade do ativo.
* Definir a integração automática de metadados com o DOM-MET.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Dados-Corporativos-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
