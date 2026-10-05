# 010 – Especificacoes – Assistência Social

#### Especificacoes – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-010

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

Este artefato detalha **as especificações** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/ass/atendimentos` | atendimentos | JSON (payload do domínio) |
| POST | `/api/v1/ass/atendimentos` | atendimentos | JSON (payload do domínio) |
| GET | `/api/v1/ass/atendimentos/{atendimento_id}` | atendimentos | JSON (payload do domínio) |
| GET | `/api/v1/ass/beneficios` | beneficios | JSON (payload do domínio) |
| POST | `/api/v1/ass/beneficios` | beneficios | JSON (payload do domínio) |
| GET | `/api/v1/ass/beneficios/{beneficio_id}` | beneficios | JSON (payload do domínio) |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/aprovar` | beneficios | JSON (payload do domínio) |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/cancelar` | beneficios | JSON (payload do domínio) |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/entregar` | beneficios | JSON (payload do domínio) |
| POST | `/api/v1/ass/beneficios/{beneficio_id}/negar` | beneficios | JSON (payload do domínio) |
| GET | `/api/v1/ass/familias` | familias | JSON (payload do domínio) |
| POST | `/api/v1/ass/familias` | familias | JSON (payload do domínio) |
| GET | `/api/v1/ass/familias/nis/{nis}` | familias | JSON (payload do domínio) |
| DELETE | `/api/v1/ass/familias/{familia_id}` | familias | JSON (payload do domínio) |
| GET | `/api/v1/ass/familias/{familia_id}` | familias | JSON (payload do domínio) |
| PATCH | `/api/v1/ass/familias/{familia_id}` | familias | JSON (payload do domínio) |
| GET | `/api/v1/ass/familias/{familia_id}/beneficios` | familias | JSON (payload do domínio) |
| GET | `/api/v1/ass/familias/{familia_id}/pessoas` | familias | JSON (payload do domínio) |
| GET | `/api/v1/ass/pessoas` | pessoas | JSON (payload do domínio) |
| POST | `/api/v1/ass/pessoas` | pessoas | JSON (payload do domínio) |
| GET | `/api/v1/ass/pessoas/cpf/{cpf}` | pessoas | JSON (payload do domínio) |
| DELETE | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | JSON (payload do domínio) |
| GET | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | JSON (payload do domínio) |
| PATCH | `/api/v1/ass/pessoas/{pessoa_id}` | pessoas | JSON (payload do domínio) |
| GET | `/api/v1/ass/pessoas/{pessoa_id}/atendimentos` | pessoas | JSON (payload do domínio) |
| GET | `/api/v1/ass/unidades` | unidades | JSON (payload do domínio) |
| POST | `/api/v1/ass/unidades` | unidades | JSON (payload do domínio) |
| DELETE | `/api/v1/ass/unidades/{unidade_id}` | unidades | JSON (payload do domínio) |
| GET | `/api/v1/ass/unidades/{unidade_id}` | unidades | JSON (payload do domínio) |
| PATCH | `/api/v1/ass/unidades/{unidade_id}` | unidades | JSON (payload do domínio) |
| GET | `/api/v1/ass/unidades/{unidade_id}/atendimentos` | unidades | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-ASS-001 | o NIS da família é único no cadastro municipal |
| RN-ASS-002 | o CPF da pessoa é único no cadastro municipal |
| RN-ASS-003 | o benefício eventual obedece à máquina de estados |
| RN-ASS-004 | atendimentos são registrados por unidade CRAS/CREAS |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Assistencia-Social-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
