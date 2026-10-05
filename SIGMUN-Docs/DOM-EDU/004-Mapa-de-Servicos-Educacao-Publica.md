# 004 – Mapa-de-Servicos – Educação Pública

#### Mapa-de-Servicos – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-004

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **o mapa de serviços** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/edu`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/edu/alunos` | alunos | Listar Alunos |
| POST | `/api/v1/edu/alunos` | alunos | Cadastrar Aluno |
| GET | `/api/v1/edu/alunos/{aluno_id}` | alunos | Obter Aluno |
| PATCH | `/api/v1/edu/alunos/{aluno_id}` | alunos | Atualizar Aluno |
| GET | `/api/v1/edu/diario` | diario | Listar Diario |
| POST | `/api/v1/edu/diario` | diario | Registrar Lancamento |
| GET | `/api/v1/edu/matriculas` | matriculas | Listar Matriculas |
| POST | `/api/v1/edu/matriculas` | matriculas | Realizar Matricula |
| GET | `/api/v1/edu/matriculas/{matricula_id}` | matriculas | Obter Matricula |
| POST | `/api/v1/edu/matriculas/{matricula_id}/cancelar` | matriculas | Cancelar Matricula |
| POST | `/api/v1/edu/matriculas/{matricula_id}/concluir` | matriculas | Concluir Matricula |
| POST | `/api/v1/edu/matriculas/{matricula_id}/transferir` | matriculas | Transferir Matricula |
| GET | `/api/v1/edu/merenda/distribuicoes` | merenda | Listar Distribuicoes |
| POST | `/api/v1/edu/merenda/distribuicoes` | merenda | Distribuir Merenda |
| GET | `/api/v1/edu/merenda/itens` | merenda | Listar Itens Merenda |
| POST | `/api/v1/edu/merenda/itens` | merenda | Cadastrar Item Merenda |
| GET | `/api/v1/edu/merenda/itens/{item_id}` | merenda | Obter Item Merenda |
| POST | `/api/v1/edu/merenda/itens/{item_id}/repor` | merenda | Repor Item Merenda |
| GET | `/api/v1/edu/transporte/passagens` | transporte | Listar Passagens |
| POST | `/api/v1/edu/transporte/passagens` | transporte | Registrar Passagem |
| GET | `/api/v1/edu/transporte/rotas` | transporte | Listar Rotas |
| POST | `/api/v1/edu/transporte/rotas` | transporte | Cadastrar Rota |
| GET | `/api/v1/edu/transporte/rotas/{rota_id}` | transporte | Obter Rota |
| POST | `/api/v1/edu/transporte/rotas/{rota_id}/ativar` | transporte | Ativar Rota |
| POST | `/api/v1/edu/transporte/rotas/{rota_id}/inativar` | transporte | Inativar Rota |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| alunos | 4 |
| diario | 2 |
| matriculas | 6 |
| merenda | 6 |
| transporte | 7 |

---

# 4. Lacunas a validar

* Definir a regra de elegibilidade à merenda.
* Definir a integração com o sistema estadual de educação.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Educacao-Publica-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
