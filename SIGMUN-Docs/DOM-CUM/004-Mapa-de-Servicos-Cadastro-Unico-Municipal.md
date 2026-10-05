# 004 – Mapa-de-Servicos – Cadastro Único Municipal

#### Mapa-de-Servicos – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-004

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **o mapa de serviços** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/cadastro`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/cadastro/pessoas` | pessoas | Lista pessoas com filtros e paginação |
| POST | `/api/v1/cadastro/pessoas` | pessoas | Registra uma nova pessoa (PF ou PJ) com filhos do agregado |
| DELETE | `/api/v1/cadastro/pessoas/{pessoa_id}` | pessoas | Exclui logicamente uma pessoa (soft-delete) |
| GET | `/api/v1/cadastro/pessoas/{pessoa_id}` | pessoas | Consulta uma pessoa pelo ID |
| PATCH | `/api/v1/cadastro/pessoas/{pessoa_id}/categoria` | pessoas | Altera a categoria cadastral da pessoa |
| POST | `/api/v1/cadastro/pessoas/{pessoa_id}/contatos` | pessoas | Adiciona um contato à pessoa |
| PATCH | `/api/v1/cadastro/pessoas/{pessoa_id}/dados-fisicos` | pessoas | Atualiza dados da pessoa física |
| PATCH | `/api/v1/cadastro/pessoas/{pessoa_id}/dados-juridicos` | pessoas | Atualiza dados da pessoa jurídica |
| POST | `/api/v1/cadastro/pessoas/{pessoa_id}/documentos` | pessoas | Adiciona um documento à pessoa |
| POST | `/api/v1/cadastro/pessoas/{pessoa_id}/enderecos` | pessoas | Adiciona um endereço à pessoa |
| GET | `/api/v1/cadastro/unidades-administrativas` | unidades-administrativas | Lista unidades administrativas com paginação |
| POST | `/api/v1/cadastro/unidades-administrativas` | unidades-administrativas | Registra uma nova unidade administrativa |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| pessoas | 10 |
| unidades-administrativas | 2 |

---

# 4. Lacunas a validar

* Autenticação: resolvido no ADR-0007 (JWT do DOM-IDN obrigatório nas escritas).
* Revisão periódica: definida no ADR-0007 (12 meses, tarefa mensal, indicador).
* Compartilhamento: contrato formal definido no ADR-0007 (fonte oficial, id opaco).

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Cadastro-Unico-Municipal-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
