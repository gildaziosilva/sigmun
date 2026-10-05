# 004 – Mapa-de-Servicos – Assistência Social

#### Mapa-de-Servicos – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-004

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **o mapa de serviços** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/ass`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/ass/atendimentos` | atendimentos | Listar Atendimentos |
| POST | `/api/v1/ass/atendimentos` | atendimentos | Registrar Atendimento |
| GET | `/api/v1/ass/atendimentos/{atendimento_id}` | atendimentos | Obter Atendimento |
| GET | `/api/v1/ass/beneficios` | beneficios | Listar Beneficios |
| POST | `/api/v1/ass/beneficios` | beneficios | Solicitar Beneficio |
| GET | `/api/v1/ass/beneficios/{beneficio_id}` | beneficios | Obter Beneficio |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/aprovar` | beneficios | Aprovar Beneficio |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/cancelar` | beneficios | Cancelar Beneficio |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/entregar` | beneficios | Entregar Beneficio |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/negar` | beneficios | Negar Beneficio |
| GET | `/api/v1/ass/familias` | familias | Listar Familias |
| POST | `/api/v1/ass/familias` | familias | Cadastrar Familia |
| GET | `/api/v1/ass/familias/nis/{nis}` | familias | Obter Familia Por Nis |
| DELETE | `/api/v1/ass/familias/{familia_id}` | familias | Excluir Familia |
| GET | `/api/v1/ass/familias/{familia_id}` | familias | Obter Familia |
| PATCH | `/api/v1/ass/familias/{familia_id}` | familias | Atualizar Familia |
| GET | `/api/v1/ass/familias/{familia_id}/beneficios` | familias | Listar Beneficios Da Familia |
| GET | `/api/v1/ass/familias/{familia_id}/pessoas` | familias | Listar Pessoas Da Familia |
| GET | `/api/v1/ass/pessoas` | pessoas | Listar Pessoas |
| POST | `/api/v1/ass/pessoas` | pessoas | Cadastrar Pessoa |
| GET | `/api/v1/ass/pessoas/cpf/{cpf}` | pessoas | Obter Pessoa Por Cpf |
| DELETE | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | Excluir Pessoa |
| GET | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | Obter Pessoa |
| PATCH | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | Atualizar Pessoa |
| GET | `/api/v1/ass/pessoas/{pessoa_id}/atendimentos` | pessoas | Listar Atendimentos Da Pessoa |
| GET | `/api/v1/ass/unidades` | unidades | Listar Unidades |
| POST | `/api/v1/ass/unidades` | unidades | Cadastrar Unidade |
| DELETE | `/api/v1/ass/unidades/{unidade_id}` | unidades | Excluir Unidade |
| GET | `/api/v1/ass/unidades/{unidade_id}` | unidades | Obter Unidade |
| PATCH | `/api/v1/ass/unidades/{unidade_id}` | unidades | Atualizar Unidade |
| GET | `/api/v1/ass/unidades/{unidade_id}/atendimentos` | unidades | Listar Atendimentos Da Unidade |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| atendimentos | 3 |
| beneficios | 7 |
| familias | 8 |
| pessoas | 7 |
| unidades | 6 |

---

# 4. Lacunas a validar

* Definir o glossário de tipos de benefício eventual por município.
* Formalizar o fluxo de aferimento de renda com o DOM-IND.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Assistencia-Social-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
