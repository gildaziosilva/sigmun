# 004 – Mapa de Serviços – Gestão Documental

#### Mapa de Serviços – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-004

**Domínio:** Gestão Documental

**Versão:** 1.0

**Status:** Em elaboração

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

O **Mapa de Serviços – Gestão Documental** (`DOM-GDO`) tem como finalidade mapear e descrever os serviços (endpoints REST) que o domínio deve prover, organizando-os em serviços internos (consumidos por outros módulos do SIGMUN) e serviços expostos (consumidos por sistemas externos e usuários finais).

Este artefato traduz as capacidades (`002-Mapa-de-Capacidades-Gestao-Documental.md`) e processos (`003-Mapa-de-Processos-Gestao-Documental.md`) em contratos de serviço, orientando a implementação dos routers, schemas e use cases.

---

# 2. Princípios

O mapa de serviços observa os seguintes princípios:

* **RESTful** — conformidade com padrões REST (recursos, verbos HTTP, códigos de status);
* **Versionamento** — prefixo `/api/v1/gdo` para evolução controlada;
* **Segurança por padrão** — autenticação via DOM-IDN em todos os endpoints;
* **Paginação** — listagens com paginação e filtros;
* **Idempotência** — operações seguras repetíveis sem efeitos colaterais;
* **Documentação automática** — schemas Pydantic para OpenAPI/Swagger;
* **Padrão de resposta** — formato consistente (data, meta, errors).

---

# 3. Conceito de Serviço

Para este domínio, considera-se **serviço** qualquer operação exposta via HTTP que:

* implemente uma capacidade de negócio;
* seja consumida por atores internos ou externos;
* respeite contratos de entrada (request) e saída (response);
* registre auditoria automaticamente;
* aplique regras de negócio do domínio.

---

# 4. Classificação dos Serviços

Os serviços classificam-se em:

| Tipo | Descrição | Exemplo |
| --- | --- | --- |
| **Interno** | Consumido por outros módulos SIGMUN | `GET /api/v1/gdo/documentos/{id}` |
| **Exposto** | Consumido por sistemas externos/usuários | `POST /api/v1/gdo/documentos` |
| **Público** | Acesso livre (Portal da Transparência) | `GET /api/v1/gdo/consulta-publica` |

---

# 5. Estrutura de Endpoints

## 5.1 Convenções

* **Prefixo base:** `/api/v1/gdo`
* **Formato:** JSON (application/json)
* **Autenticação:** Bearer Token (via DOM-IDN)
* **Idioma:** pt-BR (mensagens de erro)

## 5.2 Padrão de Resposta

```json
{
  "data": { },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 100
  },
  "errors": [ ]
}
```

## 5.3 Códigos de Status HTTP

| Código | Descrição | Uso |
| --- | --- | --- |
| 200 | OK | Consultas e atualizações bem-sucedidas |
| 201 | Created | Criação de recursos |
| 204 | No Content | Downloads e operações sem retorno |
| 400 | Bad Request | Dados inválidos |
| 401 | Unauthorized | Sem autenticação |
| 403 | Forbidden | Sem permissão |
| 404 | Not Found | Recurso não encontrado |
| 409 | Conflict | Conflito de estado (duplicidade) |
| 422 | Unprocessable Entity | Erro de validação |
| 500 | Internal Server Error | Erro interno |

---

# 6. Serviços de Documentos

**Router:** `documentos_router.py` | **Prefixo:** `/api/v1/gdo/documentos`

## 6.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/documentos` | Criar documento (upload/digitalização) | Exposto | Servidor/Gestor Documental |
| `GET` | `/documentos` | Listar documentos (paginado, filtros) | Interno | Servidor/Gestor Documental |
| `GET` | `/documentos/{id}` | Buscar documento por ID | Interno | Servidor/Gestor Documental |
| `GET` | `/documentos/{id}/download` | Baixar arquivo do documento | Interno | Servidor/Gestor Documental |
| `PUT` | `/documentos/{id}` | Atualizar metadados do documento | Exposto | Servidor/Gestor Documental |
| `DELETE` | `/documentos/{id}` | Excluir documento (soft delete) | Interno | Administrador GDO |
| `GET` | `/documentos/{id}/versoes` | Listar versões do documento | Interno | Servidor/Gestor Documental |
| `GET` | `/documentos/{id}/versoes/{versao}` | Buscar versão específica | Interno | Servidor/Gestor Documental |

## 6.2 Schemas

**DocumentoCreateRequest:**
```json
{
  "tipo_documental": "string",
  "titulo": "string",
  "descricao": "string",
  "classificacao_id": "uuid",
  "autor_id": "uuid",
  "unidade_id": "uuid",
  "processo_id": "uuid (opcional)",
  "arquivo": "binary (multipart/form-data)"
}
```

**DocumentoResponse:**
```json
{
  "id": "uuid",
  "codigo": "string (único)",
  "tipo_documental": "string",
  "titulo": "string",
  "descricao": "string",
  "classificacao": { "id": "uuid", "codigo": "string", "nome": "string" },
  "autor": { "id": "uuid", "nome": "string" },
  "unidade": { "id": "uuid", "nome": "string" },
  "hash_sha256": "string",
  "tamanho_bytes": "integer",
  "versao_atual": "integer",
  "data_criacao": "datetime",
  "data_atualizacao": "datetime",
  "status": "string (corrente/arquivado/eliminado)"
}
```

---

# 7. Serviços de Processos Documentais

**Router:** `processos_router.py` | **Prefixo:** `/api/v1/gdo/processos`

## 7.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/processos` | Abrir processo documental | Exposto | Servidor/Gestor Documental |
| `GET` | `/processos` | Listar processos (paginado, filtros) | Interno | Servidor/Gestor Documental |
| `GET` | `/processos/{id}` | Buscar processo por ID | Interno | Servidor/Gestor Documental |
| `POST` | `/processos/{id}/documentos` | Incluir documento no processo | Exposto | Servidor/Gestor Documental |
| `POST` | `/processos/{id}/tramitacao` | Tramitar processo | Exposto | Servidor/Gestor Documental |
| `POST` | `/processos/{id}/despacho` | Registrar despacho/parecer | Exposto | Servidor/Gestor Documental |
| `POST` | `/processos/{id}/encerramento` | Encerrar processo | Exposto | Servidor/Gestor Documental |
| `POST` | `/processos/{id}/reabertura` | Reabrir processo | Exposto | Servidor/Gestor Documental |
| `GET` | `/processos/{id}/historico` | Histórico de tramitação | Interno | Servidor/Gestor Documental |

## 7.2 Schemas

**ProcessoCreateRequest:**
```json
{
  "tipo_processo": "string",
  "assunto": "string",
  "interessado_id": "uuid",
  "unidade_origem_id": "uuid",
  "classificacao_id": "uuid"
}
```

**ProcessoResponse:**
```json
{
  "id": "uuid",
  "numero": "string (único, autuado)",
  "tipo_processo": "string",
  "assunto": "string",
  "interessado": { "id": "uuid", "nome": "string" },
  "unidade_origem": { "id": "uuid", "nome": "string" },
  "unidade_atual": { "id": "uuid", "nome": "string" },
  "classificacao": { "id": "uuid", "codigo": "string", "nome": "string" },
  "status": "string (aberto/em_tramite/encerrado/arquivado)",
  "data_autuacao": "datetime",
  "data_ultima_movimentacao": "datetime"
}
```

---

# 8. Serviços de Classificação e Temporalidade

**Router:** `classificacao_router.py` | **Prefixo:** `/api/v1/gdo/classificacao`

## 8.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/classificacao/planos` | Criar plano de classificação | Interno | Administrador GDO |
| `GET` | `/classificacao/planos` | Listar planos de classificação | Interno | Servidor/Gestor Documental |
| `GET` | `/classificacao/planos/{id}` | Buscar plano por ID | Interno | Servidor/Gestor Documental |
| `PUT` | `/classificacao/planos/{id}` | Atualizar plano | Interno | Administrador GDO |
| `DELETE` | `/classificacao/planos/{id}` | Excluir plano | Interno | Administrador GDO |
| `POST` | `/classificacao/temporalidade` | Criar tabela de temporalidade | Interno | Administrador GDO |
| `GET` | `/classificacao/temporalidade` | Listar tabelas de temporalidade | Interno | Servidor/Gestor Documental |
| `GET` | `/classificacao/temporalidade/{id}` | Buscar tabela por ID | Interno | Servidor/Gestor Documental |
| `PUT` | `/classificacao/temporalidade/{id}` | Atualizar tabela | Interno | Administrador GDO |
| `GET` | `/classificacao/documentos-vencidos` | Listar documentos com prazo vencido | Interno | Autoridade Homologadora |

---

# 9. Serviços de Pesquisa e Consulta

**Router:** `pesquisa_router.py` | **Prefixo:** `/api/v1/gdo/pesquisa`

## 9.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/pesquisa/documentos` | Pesquisar documentos (filtros, paginação) | Interno | Servidor/Gestor Documental |
| `POST` | `/pesquisa/processos` | Pesquisar processos (filtros, paginação) | Interno | Servidor/Gestor Documental |
| `GET` | `/consulta-publica/documentos` | Consultar documentos públicos | Público | Público (cidadão) |
| `GET` | `/consulta-publica/documentos/{id}` | Detalhar documento público | Público | Público (cidadão) |
| `GET` | `/consulta-publica/documentos/{id}/download` | Baixar documento público | Público | Público (cidadão) |

---

# 10. Serviços de Assinatura e Autenticação

**Router:** `assinatura_router.py` | **Prefixo:** `/api/v1/gdo/assinatura`

## 10.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/assinatura/eletronica/{documento_id}` | Assinar documento eletronicamente | Exposto | Servidor/Gestor Documental |
| `POST` | `/assinatura/digital/{documento_id}` | Assinar documento digitalmente (ICP-Brasil) | Exposto | Servidor/Gestor Documental |
| `POST` | `/assinatura/validar` | Validar assinatura de documento | Interno | Sistema/Servidor |
| `POST` | `/assinatura/autenticar-copia/{documento_id}` | Autenticar cópia de documento | Interno | Servidor/Gestor Documental |

---

# 11. Serviços de Arquivamento e Destinação

**Router:** `arquivamento_router.py` | **Prefixo:** `/api/v1/gdo/arquivamento`

## 11.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `POST` | `/arquivamento/documentos/{id}` | Arquivar documento | Exposto | Servidor/Gestor Documental |
| `POST` | `/arquivamento/processos/{id}` | Arquivar processo | Exposto | Servidor/Gestor Documental |
| `POST` | `/destinacao/eliminar` | Eliminar documentos (lote) | Interno | Autoridade Homologadora |
| `POST` | `/destinacao/guarda-permanente` | Transferir para guarda permanente | Interno | Autoridade Homologadora |
| `POST` | `/destinacao/prorrogar` | Prorrogar prazo de temporalidade | Interno | Autoridade Homologadora |
| `GET` | `/destinacao/termo/{id}` | Gerar termo de eliminação/guarda | Interno | Autoridade Homologadora |

---

# 12. Serviços de Auditoria

**Router:** `auditoria_router.py` | **Prefixo:** `/api/v1/gdo/auditoria`

## 12.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `GET` | `/auditoria/documentos/{id}/historico` | Histórico de ações no documento | Interno | Administrador GDO |
| `GET` | `/auditoria/processos/{id}/historico` | Histórico de ações no processo | Interno | Administrador GDO |
| `GET` | `/auditoria/relatorios/acesso` | Relatório de acessos | Interno | Administrador GDO |
| `GET` | `/auditoria/relatorios/movimentacao` | Relatório de movimentação | Interno | Administrador GDO |

---

# 13. Serviços de Segurança e Acesso

**Router:** `seguranca_router.py` | **Prefixo:** `/api/v1/gdo/seguranca`

## 13.1 Endpoints

| Método | Endpoint | Descrição | Tipo | Atores |
| --- | --- | --- | --- | --- |
| `PUT` | `/seguranca/documentos/{id}/acesso` | Configurar acesso ao documento | Interno | Administrador GDO |
| `PUT` | `/seguranca/documentos/{id}/sigilo` | Classificar sigilo do documento | Interno | Administrador GDO |
| `GET` | `/seguranca/documentos/{id}/permissoes` | Consultar permissões do documento | Interno | Administrador GDO |

---

# 14. Relacionamento com Atores

| Serviço | Ator Principal | Ator Secundário |
| --- | --- | --- |
| Documentos | Servidor/Gestor Documental | Administrador GDO |
| Processos | Servidor/Gestor Documental | — |
| Classificação/Temporalidade | Administrador GDO | Autoridade Homologadora |
| Pesquisa/Consulta | Servidor/Gestor Documental | Público (consulta) |
| Assinatura | Servidor/Gestor Documental | Autoridade Homologadora |
| Arquivamento/Destinação | Servidor/Gestor Documental | Autoridade Homologadora |
| Auditoria | Administrador GDO | Autoridade Homologadora |
| Segurança | Administrador GDO | — |

---

# 15. Relacionamento com Capacidades

| Serviço | Capacidade (Nível 1) | Capacidade (Nível 2) |
| --- | --- | --- |
| Documentos | GDO-F01 Gestão de Documentos | GDO-F01-P01 a P06 |
| Processos | GDO-F02 Gestão de Processos | GDO-F02-P01 a P06 |
| Classificação | GDO-F06 Classificação/Temporalidade | GDO-F06-P01 a P03 |
| Pesquisa | GDO-F03 Pesquisa e Consulta | GDO-F03-P01 a P05 |
| Assinatura | GDO-F04 Assinatura | GDO-F04-P01 a P04 |
| Arquivamento | GDO-F01 Gestão de Documentos | GDO-F01-P05 Arquivamento |
| Destinação | GDO-F01 Gestão de Documentos | GDO-F01-P06 Destinação |
| Auditoria | GDO-F09 Auditoria | GDO-F09-P01 a P03 |
| Segurança | GDO-F10 Segurança/Acesso | GDO-F10-P01 a P03 |

---

# 16. Relacionamento com Outros Domínios

| Serviço | Domínio Relacionado | Natureza |
| --- | --- | --- |
| Assinatura | DOM-IDN (Identidade) | Consome serviço de autenticação |
| Auditoria | DOM-IDN (Identidade) | Consome `core.trilha_auditoria` |
| Segurança | DOM-IDN (Identidade) | Consome perfis/permissões |
| Documentos | DOM-MET (Metadados) | Compartilha modelo de metadados |
| Processos | DOM-COMPRAS | Vincula `processo_documental` |
| Consulta Pública | DOM-CUM (Cadastro) | Valida acesso por pessoa |
| Segurança (LGPD) | DOM-DAD (Dados) | Alinha políticas de tratamento |

---

# 17. Identificador do Artefato

| Atributo | Valor |
| --- | --- |
| **Identificador** | `ACT-SER-GDO-001` |
| **Código do artefato** | `DOM-GDO-004` |
| **Versão** | 2.0 |
| **Data** | 2026-09-01 |
| **Responsável** | Equipe SIGMUN |
| **Status** | Vigente |

---

# 18. Controle de Versões

| Versão | Data | Descrição | Autor |
| --- | --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato | Equipe SIGMUN |
| 2.0 | 2026-09-01 | Conteúdo detalhado: 9 routers, ~50 endpoints, schemas, relacionamentos | Equipe SIGMUN |

---

**Documento:** 004-Mapa-de-Servicos-Gestao-Documental.md

**Última atualização:** 2026-09-01

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
