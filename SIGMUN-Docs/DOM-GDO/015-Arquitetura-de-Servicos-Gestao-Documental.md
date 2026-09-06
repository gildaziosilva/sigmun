# 015 – Arquitetura de Serviços – Gestão Documental

#### Arquitetura de Serviços – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-015

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `001-Mapa-de-Atores-Gestao-Documental.md`
* `002-Mapa-de-Capacidades-Gestao-Documental.md`
* `003-Mapa-de-Processos-Gestao-Documental.md`
* `004-Mapa-de-Servicos-Gestao-Documental.md`
* `005-Casos-de-Uso-Gestao-Documental.md`
* `006-Historias-de-Usuario-Gestao-Documental.md`
* `007-Regras-de-Negocio-Gestao-Documental.md`
* `008-Requisitos-Funcionais-Gestao-Documental.md`
* `009-Requisitos-Nao-Funcionais-Gestao-Documental.md`
* `010-Especificacoes-Gestao-Documental.md`
* `011-Criterios-de-Aceitacao-Gestao-Documental.md`
* `012-Matriz-de-Rastreabilidade-Gestao-Documental.md`
* `013-Modelo-de-Dados-Gestao-Documental.md`
* `014-Modelo-de-Integracao-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define a **Arquitetura de Serviços do Domínio de Gestão Documental do SIGMUN**.

A arquitetura estabelece a organização dos serviços de negócio, serviços de aplicação e interfaces necessárias para disponibilizar as capacidades do domínio de forma modular, segura, rastreável e integrada à arquitetura corporativa do SIGMUN.

O documento serve como referência para:

* arquitetura de software;
* desenvolvimento de APIs;
* serviços de aplicação;
* integrações;
* interfaces de usuário;
* automações;
* eventos;
* segurança;
* auditoria;
* testes;
* implantação;
* evolução do domínio.

---

# 2. Objetivos

A arquitetura de serviços tem como objetivos:

1. transformar capacidades de negócio em serviços reutilizáveis;
2. separar regras de negócio de interfaces;
3. reduzir acoplamento entre componentes;
4. permitir integração entre domínios;
5. disponibilizar APIs padronizadas;
6. permitir processamento síncrono e assíncrono;
7. garantir segurança e rastreabilidade;
8. permitir evolução independente dos serviços;
9. apoiar diferentes canais de acesso;
10. preservar a governança arquitetural do SIGMUN.

---

# 3. Princípios

A arquitetura deverá observar os seguintes princípios.

## 3.1 Serviços Orientados ao Negócio

Os serviços deverão representar capacidades e responsabilidades reais do domínio.

## 3.2 Baixo Acoplamento

Serviços deverão possuir o menor acoplamento possível entre si.

## 3.3 Alta Coesão

Cada serviço deverá possuir responsabilidade claramente definida.

## 3.4 Contratos Explícitos

As interfaces deverão possuir contratos claramente definidos.

## 3.5 API First

Quando houver necessidade de exposição externa ou integração, a definição do contrato deverá preceder a implementação.

## 3.6 Segurança por Padrão

Todo serviço deverá considerar:

* autenticação;
* autorização;
* auditoria;
* proteção de dados;
* rate limiting.

## 3.7 Observabilidade

Todo serviço deverá ser observável por:

* logs;
* métricas;
* traces;
* alertas.

---

# 4. Estrutura da Arquitetura

## 4.1 Visão Geral

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CAMADA DE APRESENTAÇÃO                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Web Admin  │  Portal Público  │  Mobile  │  API Externa  │  Webhooks         │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CAMADA DE API GATEWAY                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Rate Limiting  │  Autenticação  │  Roteamento  │  Logging  │  Versionamento   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                            CAMADA DE SERVIÇOS                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│  documento_service  │  tramitacao_service  │  processo_service  │  authz_service │
│  classificacao_svc  │  assinatura_service  │  pesquisa_service   │  admin_service │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CAMADA DE DOMÍNIO                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Documento Aggregate  │  Processo Aggregate  │  Tramitacao Entity  │  Policies │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         CAMADA DE INFRAESTRUTURA                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  Repository  │  Event Bus  │  Cache  │  Storage  │  Message Queue  │  OCR      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## 4.2 Camadas da Arquitetura

| Camada | Responsabilidade | Componentes |
| --- | --- | --- |
| Apresentação | Interfaces com usuários | Web Admin, Portal Público, Mobile, API Externa |
| API Gateway | Controle de acesso e rate limiting | Autenticação, Roteamento, Logging |
| Serviços | Orquestração de operações | Serviços de aplicação |
| Domínio | Regras de negócio | Agregados, Entidades, Value Objects, Policies |
| Infraestrutura | Persistência e integração | Repository, Event Bus, Cache, Storage |

---

# 5. Serviços de Domínio

## 5.1 documento_service

**Responsabilidade:** Gerenciar o ciclo de vida dos documentos

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| criar_documento | Comando | Criar novo documento digital |
| importar_documento | Comando | Importar documento externo |
| digitalizar_documento | Comando | Digitalizar documento físico |
| obter_documento | Consulta | Consultar documento por ID |
| listar_documentos | Consulta | Listar documentos com filtros |
| atualizar_metadados | Comando | Atualizar metadados do documento |
| criar_versao | Comando | Criar nova versão do documento |
| restaurar_versao | Comando | Restaurar versão anterior |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| DocumentoCriado | Documento criado com sucesso |
| DocumentoAtualizado | Metadados do documento atualizados |
| NovaVersaoCriada | Nova versão do documento criada |
| VersaoRestaurada | Versão anterior restaurada |

---

## 5.2 tramitacao_service

**Responsabilidade:** Gerenciar a tramitação de documentos entre unidades

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| tramitar_documento | Comando | Tramitar documento para outra unidade |
| receber_documento | Comando | Confirmar recebimento |
| devolver_documento | Comando | Devolver documento à origem |
| listar_tramitacoes | Consulta | Listar tramitações do documento |
| consultar_historico | Consulta | Consultar histórico de tramitação |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| DocumentoTramitado | Documento tramitado para destino |
| DocumentoRecebido | Documento recebido na unidade |
| DocumentoDevolvido | Documento devolvido à origem |

---

## 5.3 processo_service

**Responsabilidade:** Gerenciar processos documentais

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| abrir_processo | Comando | Abrir novo processo documental |
| incluir_documento | Comando | Incluir documento em processo |
| encerrar_processo | Comando | Encerrar processo |
| reabrir_processo | Comando | Reabrir processo encerrado |
| obter_processo | Consulta | Consultar processo por ID |
| listar_processos | Consulta | Listar processos com filtros |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| ProcessoAberto | Processo documental aberto |
| DocumentoIncluido | Documento incluído em processo |
| ProcessoEncerrado | Processo encerrado |
| ProcessoReaberto | Processo reaberto |

---

## 5.4 classificacao_service

**Responsabilidade:** Gerenciar classificação arquivística

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| classificar_documento | Comando | Atribuir classificação ao documento |
| reclassificar_documento | Comando | Reclassificar documento |
| vincular_temporalidade | Comando | Vincular temporalidade automaticamente |
| obter_classificacao | Consulta | Consultar classificação |
| listar_plano_classificacao | Consulta | Listar plano de classificação |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| DocumentoClassificado | Documento classificado |
| DocumentoReclassificado | Documento reclassificado |

---

## 5.5 assinatura_service

**Responsabilidade:** Gerenciar assinaturas digitais

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| assinar_documento | Comando | Assinar documento digitalmente |
| validar_assinatura | Consulta | Validar assinatura digital |
| listar_assinaturas | Consulta | Listar assinaturas do documento |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| DocumentoAssinado | Documento assinado digitalmente |
| AssinaturaInvalidada | Assinatura inválida detectada |

---

## 5.6 pesquisa_service

**Responsabilidade:** Gerenciar pesquisa e consulta de documentos

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| pesquisar_documentos | Consulta | Pesquisa textual e por filtros |
| consultar_documento_publico | Consulta | Consulta pública de documentos |
| solicitar_via | Consulta | Solicitar via digital de documento |
| gerar_relatorio | Consulta | Gerar relatório do acervo |

---

## 5.7 destinacao_service

**Responsabilidade:** Gerenciar destinação de documentos

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| avaliar_destinacao | Comando | Avaliar documento para destinação |
| aprovar_eliminacao | Comando | Aprovar eliminação (autoridade) |
| destinar_guarda_permanente | Comando | Destinar à guarda permanente |
| prorrogar_retencao | Comando | Prorrogar prazo de retenção |
| gerar_termo_eliminacao | Comando | Gerar termo de eliminação |

**Eventos Publicados:**

| Evento | Descrição |
| --- | --- |
| DocumentoAvaliado | Documento avaliado para destinação |
| DocumentoEliminado | Documento eliminado |
| DocumentoGuardaPermanente | Destinado à guarda permanente |

---

## 5.8 admin_service

**Responsabilidade:** Gerenciar configurações do domínio

**Operações:**

| Operação | Tipo | Descrição |
| --- | --- | --- |
| configurar_plano_classificacao | Comando | Configurar plano de classificação |
| configurar_temporalidade | Comando | Configurar tabela de temporalidade |
| configurar_taxonomia | Comando | Configurar taxonomias |
| gerenciar_permissoes | Comando | Gerenciar permissões de acesso |

---

# 6. API Endpoints

## 6.1 Documentos

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/documentos` | Criar documento | documento_service |
| GET | `/api/v1/gdo/documentos/{id}` | Consultar documento | documento_service |
| GET | `/api/v1/gdo/documentos` | Listar documentos | documento_service |
| POST | `/api/v1/gdo/documentos/{id}/versoes` | Criar versão | documento_service |
| POST | `/api/v1/gdo/documentos/{id}/restaurar` | Restaurar versão | documento_service |
| PUT | `/api/v1/gdo/documentos/{id}/metadados` | Atualizar metadados | documento_service |

## 6.2 Tramitação

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/documentos/{id}/tramitacoes` | Tramitar documento | tramitacao_service |
| POST | `/api/v1/gdo/tramitacoes/{id}/receber` | Receber documento | tramitacao_service |
| POST | `/api/v1/gdo/tramitacoes/{id}/devolver` | Devolver documento | tramitacao_service |
| GET | `/api/v1/gdo/documentos/{id}/tramitacoes` | Listar tramitações | tramitacao_service |

## 6.3 Processos

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/processos` | Abrir processo | processo_service |
| PUT | `/api/v1/gdo/processos/{id}/encerrar` | Encerrar processo | processo_service |
| PUT | `/api/v1/gdo/processos/{id}/reabrir` | Reabrir processo | processo_service |
| POST | `/api/v1/gdo/processos/{id}/documentos` | Incluir documento | processo_service |
| GET | `/api/v1/gdo/processos/{id}` | Consultar processo | processo_service |
| GET | `/api/v1/gdo/processos` | Listar processos | processo_service |

## 6.4 Classificação

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| PUT | `/api/v1/gdo/documentos/{id}/classificacao` | Classificar documento | classificacao_service |
| GET | `/api/v1/gdo/classificacao/plano` | Listar plano | classificacao_service |

## 6.5 Assinatura

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/documentos/{id}/assinaturas` | Assinar documento | assinatura_service |
| GET | `/api/v1/gdo/documentos/{id}/assinaturas/validar` | Validar assinatura | assinatura_service |

## 6.6 Destinação

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/documentos/{id}/avaliar` | Avaliar destinação | destinacao_service |
| POST | `/api/v1/gdo/documentos/{id}/eliminar` | Aprovar eliminação | destinacao_service |
| POST | `/api/v1/gdo/documentos/{id}/guarda-permanente` | Guarda permanente | destinacao_service |
| POST | `/api/v1/gdo/documentos/{id}/prorrogar` | Prorrogar retenção | destinacao_service |

## 6.7 Pesquisa e Consulta Pública

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| GET | `/api/v1/gdo/pesquisa` | Pesquisar documentos | pesquisa_service |
| GET | `/api/v1/gdo/consulta-publica` | Consulta pública | pesquisa_service |
| GET | `/api/v1/gdo/documentos/{id}/via` | Obter via digital | pesquisa_service |
| GET | `/api/v1/gdo/relatorios/acervo` | Relatório do acervo | pesquisa_service |

## 6.8 Administração

| Método | Endpoint | Descrição | Serviço |
| --- | --- | --- | --- |
| POST | `/api/v1/gdo/admin/plano-classificacao` | Configurar plano | admin_service |
| POST | `/api/v1/gdo/admin/temporalidade` | Configurar temporalidade | admin_service |
| PUT | `/api/v1/gdo/admin/permissoes/{id}` | Configurar permissões | admin_service |

---

# 7. Padrões de Implementação

## 7.1 Padrão de Resposta

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

## 7.2 Códigos de Status HTTP

| Código | Uso |
| --- | --- |
| 200 | Consultas e atualizações bem-sucedidas |
| 201 | Criação de recursos |
| 400 | Dados inválidos |
| 401 | Sem autenticação |
| 403 | Sem permissão |
| 404 | Recurso não encontrado |
| 409 | Conflito de estado |
| 500 | Erro interno |

## 7.3 Versionamento

* Prefixo: `/api/v1/gdo`
* Evolução via versão da API (v1, v2, etc.)
* Manter compatibilidade retroativa quando possível

---

# 8. Segurança

## 8.1 Autenticação

* Bearer Token (JWT) via DOM-IDN
* Validação em todas as requisições

## 8.2 Autorização

* Controle de acesso baseado em perfis (RBAC)
* Perfis: USUARIO_GDO, AUTORIDADE_GDO, ADMIN_GDO, AUDITOR_GDO, PUBLICO
* Permissões granulares por documento

## 8.3 Proteção de Dados

* Criptografia em trânsito: TLS 1.2+
* Criptografia em repouso: AES-256 para documentos sigilosos
* Mascaramento de dados pessoais em consultas públicas

---

# 9. Resiliência

| Padrão | Configuração |
| --- | --- |
| Timeout | 5-10 segundos |
| Retry | 3 tentativas com backoff exponencial |
| Circuit Breaker | Abertura após 5 falhas |
| Fallback | Cache local para consultas de referência |
| Rate Limiting | 1000 req/min (interno), 100 req/min (público) |

---

# 10. Refinamento Futuro

A arquitetura deste documento representa a primeira versão dos serviços do domínio.

Durante o refinamento, a arquitetura poderá:

* ser expandida com novos serviços;
* ser ajustada conforme evolução dos requisitos;
* ser integrada com plataforma de mensageria;
* ser documentada via OpenAPI/Swagger.

---

# 11. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`ARQ-MAP-GDO-001`

**Tipo:**

Arquitetura de Serviços.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 12. Próximo Artefato

O próximo artefato recomendado é:

`016-Modelo-de-Seguranca-Gestao-Documental.md`

A cadeia de detalhamento ficará:

```text
000-Domínio
      ↓
001-Atores
      ↓
002-Capacidades
      ↓
003-Processos
      ↓
004-Serviços
      ↓
005-Casos de Uso
      ↓
006-Histórias de Usuário
      ↓
007-Regras de Negócio
      ↓
008-Requisitos Funcionais
      ↓
009-Requisitos Não Funcionais
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
      ↓
013-Modelo de Dados
      ↓
014-Modelo de Integração
      ↓
015-Arquitetura de Serviços
      ↓
016-Modelo de Segurança
```

---

# 13. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 8 serviços, 35+ endpoints |

---

**Documento:** 015-Arquitetura-de-Servicos-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
