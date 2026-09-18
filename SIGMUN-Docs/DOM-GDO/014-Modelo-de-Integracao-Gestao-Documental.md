# 014 – Modelo de Integração – Gestão Documental

#### Modelo de Integração – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-014

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define o **Modelo de Integração do Domínio de Gestão Documental do SIGMUN**.

O modelo estabelece como o domínio deverá se comunicar com:

* outros domínios do SIGMUN;
* serviços corporativos;
* sistemas municipais;
* sistemas estaduais;
* sistemas federais;
* plataformas de transparência;
* serviços externos autorizados.

O objetivo é garantir que as integrações sejam:

* padronizadas;
* seguras;
* rastreáveis;
* resilientes;
* desacopladas;
* auditáveis;
* versionáveis;
* governáveis.

---

# 2. Objetivos

São objetivos deste modelo:

1. estabelecer padrões de integração do domínio;
2. definir contratos de integração;
3. garantir segurança nas trocas de informações;
4. evitar acoplamento direto entre bancos de dados;
5. promover reutilização de serviços corporativos;
6. permitir rastreabilidade de ponta a ponta;
7. apoiar auditoria;
8. facilitar evolução independente dos domínios;
9. garantir resiliência;
10. permitir observabilidade.

---

# 3. Princípios de Integração

## 3.1 Integração via APIs e Eventos

O domínio deverá se integrar preferencialmente por:

* APIs RESTful (síncrono);
* Eventos de domínio (assíncrono);
* Filas de mensageria quando aplicável.

**NÃO é permitido:**

* Acesso direto ao banco de dados de outro domínio
* Compartilhamento de tabelas entre domínios
* Dependência de implementação interna de outro domínio

## 3.2 Contratos Explícitos

Toda integração deverá possuir contrato conhecido pelas partes envolvidas.

## 3.3 API First

Quando a integração ocorrer por API, o contrato deverá ser definido antes da implementação.

## 3.4 Eventos para Desacoplamento

Quando apropriado, eventos deverão ser utilizados para comunicar mudanças de estado sem exigir dependência síncrona.

## 3.5 Segurança por Princípio

Toda integração deverá possuir autenticação, autorização e proteção adequadas ao risco.

## 3.6 Observabilidade

Toda integração relevante deverá permitir identificar:

* origem;
* destino;
* operação;
* resultado;
* tempo de resposta;
* erros.

---

# 4. Integrações com Outros Domínios

## 4.1 Domínio de Identidade e Acesso (DOM-IDN)

**Natureza:** Consumo

**Finalidade:** Autenticação e autorização de usuários

**Tipo de Integração:** API RESTful (síncrono)

**Serviços Utilizados:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/idn/usuarios/{id}` | GET | Consultar usuário |
| `/api/v1/idn/usuarios/{id}/permissoes` | GET | Consultar permissões |
| `/api/v1/idn/auth/validar-token` | POST | Validar token JWT |

**Contrato:**
* Autenticação via Bearer Token (JWT)
* Resposta em formato JSON
* Códigos de status HTTP padrão

**Resiliência:**
* Timeout: 5 segundos
* Retry: 3 tentativas com backoff exponencial
* Fallback: Cache local de permissões

---

## 4.2 Domínio de Cadastro Único Municipal (DOM-CUM)

**Natureza:** Consumo

**Finalidade:** Consultar unidades administrativas e pessoas

**Tipo de Integração:** API RESTful (síncrono)

**Serviços Utilizados:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/cum/unidades/{id}` | GET | Consultar unidade administrativa |
| `/api/v1/cum/unidades` | GET | Listar unidades |
| `/api/v1/cum/pessoas/{id}` | GET | Consultar pessoa |

**Contrato:**
* Autenticação via Bearer Token (JWT)
* Resposta em formato JSON
* Paginação padrão

**Resiliência:**
* Timeout: 5 segundos
* Retry: 3 tentativas
* Fallback: Cache local de unidades

---

## 4.3 Domínio de Metadados Corporativos (DOM-MET)

**Natureza:** Consumo e Provisão

**Finalidade:** Compartilhar modelo de metadados e indexação

**Tipo de Integração:** API RESTful + Eventos

**Serviços Utilizados:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/met/metadados` | GET | Consultar metadados disponíveis |
| `/api/v1/met/taxonomias` | GET | Consultar taxonomias |
| `/api/v1/gdo/documentos/{id}/metadados` | PUT | Atualizar metadados |

**Eventos Publicados:**

| Evento | Descrição | Payload |
| --- | --- | --- |
| `gdo.documento.criado` | Documento criado | documento_id, tipo, unidade |
| `gdo.documento.classificado` | Documento classificado | documento_id, classificacao |
| `gdo.documento.arquivado` | Documento arquivado | documento_id, data |
| `gdo.documento.eliminado` | Documento eliminado | documento_id, termo |

**Eventos Consumidos:**

| Evento | Descrição | Ação |
| --- | --- | --- |
| `met.taxonomia.atualizada` | Taxonomia atualizada | Atualizar cache local |

---

## 4.4 Domínio de Compras e Contratações (DOM-COM)

**Natureza:** Provisão e Consumo

**Finalidade:** Vincular documentos a processos de compras

**Tipo de Integração:** API RESTful + Eventos

**Serviços Fornecidos:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/gdo/documentos` | POST | Criar documento vinculado |
| `/api/v1/gdo/documentos/{id}` | GET | Consultar documento |
| `/api/v1/gdo/processos/{id}/documentos` | GET | Listar documentos do processo |

**Eventos Publicados:**

| Evento | Descrição | Payload |
| --- | --- | --- |
| `gdo.documento.vinculado_processo` | Documento vinculado a processo | documento_id, processo_id |

**Eventos Consumidos:**

| Evento | Descrição | Ação |
| --- | --- | --- |
| `compras.processo.criado` | Processo criado | Disponibilizar vínculo |
| `compras.processo.encerrado` | Processo encerrado | Atualizar documentos vinculados |

---

## 4.5 Domínio de Dados Corporativos (DOM-DAD)

**Natureza:** Consumo

**Finalidade:** Alinhar políticas de tratamento LGPD

**Tipo de Integração:** API RESTful

**Serviços Utilizados:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/dad/consentimento/{pessoa_id}` | GET | Verificar consentimento |
| `/api/v1/dad/dados-pessoais` | POST | Registrar tratamento |

**Contrato:**
* Autenticação via Bearer Token (JWT)
* Dados sensíveis criptografados

---

# 5. Integrações com Sistemas Externos

## 5.1 Portal da Transparência

**Natureza:** Provisão

**Finalidade:** Publicar documentos de acesso público

**Tipo de Integração:** API RESTful + Eventos

**Serviços Fornecidos:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| `/api/v1/gdo/consulta-publica` | GET | Consultar documentos públicos |
| `/api/v1/gdo/documentos/{id}/via` | GET | Obter via digital |

**Eventos Publicados:**

| Evento | Descrição | Payload |
| --- | --- | --- |
| `gdo.documento.publicado` | Documento publicado | documento_id, data_publicacao |

**Segurança:**
* Documentos públicos: acesso sem autenticação
* Documentos restritos: requer autenticação
* Mascaramento de dados pessoais (LGPD)

---

## 5.2 Certificador Digital (ICP-Brasil)

**Natureza:** Consumo

**Finalidade:** Validar certificados digitais e assinaturas

**Tipo de Integração:** API RESTful (externa)

**Serviços Utilizados:**

| Serviço | Método | Descrição |
| --- | --- | --- |
| Validar certificado | POST | Validar validade do certificado |
| Verificar assinatura | POST | Verificar validade da assinatura |

**Resiliência:**
* Timeout: 10 segundos
* Retry: 2 tentativas
* Fallback: Cache de certificados válidos

---

## 5.3 Diário Oficial Eletrônico

**Natureza:** Provisão

**Finalidade:** Publicar atos oficiais

**Tipo de Integração:** API RESTful + Eventos

**Eventos Consumidos:**

| Evento | Descrição | Ação |
| --- | --- | --- |
| `gdo.documento.assinado` | Documento oficial assinado | Publicar no diário |

---

# 6. Eventos de Domínio

## 6.1 Eventos Publicados

| Evento | Descrição | Tópico | Payload |
| --- | --- | --- | --- |
| `gdo.documento.criado` | Documento criado | gdo.documentos | {id, codigo, tipo, unidade} |
| `gdo.documento.classificado` | Documento classificado | gdo.documentos | {id, classificacao, temporalidade} |
| `gdo.documento.tramitado` | Documento tramitado | gdo.tramitacoes | {id, origem, destino, data} |
| `gdo.documento.recebido` | Documento recebido | gdo.tramitacoes | {id, unidade, data} |
| `gdo.documento.arquivado` | Documento arquivado | gdo.documentos | {id, fase, data} |
| `gdo.documento.assinado` | Documento assinado | gdo.assinaturas | {id, signatario, data} |
| `gdo.documento.eliminado` | Documento eliminado | gdo.documentos | {id, termo, data} |
| `gdo.documento.publicado` | Documento publicado | gdo.transparencia | {id, data_publicacao} |
| `gdo.documento.vinculado_processo` | Documento vinculado | gdo.integracao | {documento_id, processo_id} |

## 6.2 Eventos Consumidos

| Evento | Origem | Descrição | Ação |
| --- | --- | --- | --- |
| `idn.usuario.atualizado` | DOM-IDN | Usuário atualizado | Atualizar cache |
| `cum.unidade.atualizada` | DOM-CUM | Unidade atualizada | Atualizar cache |
| `met.taxonomia.atualizada` | DOM-MET | Taxonomia atualizada | Atualizar cache |
| `compras.processo.criado` | DOM-COM | Processo criado | Disponibilizar vínculo |
| `compras.processo.encerrado` | DOM-COM | Processo encerrado | Atualizar documentos |

---

# 7. Segurança de Integração

## 7.1 Autenticação

* Todas as APIs internas: Bearer Token (JWT) via DOM-IDN
* APIs públicas: Chave de API (API Key) quando aplicável
* Sistemas externos: mTLS ou OAuth 2.0

## 7.2 Autorização

* Verificar permissões via DOM-IDN
* Controle de acesso por perfil (RBAC)
* Permissões granulares por documento

## 7.3 Proteção de Dados

* Criptografia em trânsito: TLS 1.2+
* Criptografia em repouso: AES-256 para documentos sigilosos
* Mascaramento de dados pessoais em consultas públicas
* Conformidade com LGPD

## 7.4 Rate Limiting

* APIs internas: 1000 req/min por serviço
* APIs públicas: 100 req/min por IP
* Proteção contra DDoS

---

# 8. Resiliência

## 8.1 Padrões de Resiliência

| Padrão | Aplicação | Configuração |
| --- | --- | --- |
| Timeout | Todas as chamadas externas | 5-10 segundos |
| Retry | Operações idempotentes | 3 tentativas com backoff |
| Circuit Breaker | Serviços críticos | Abertura após 5 falhas |
| Fallback | Consultas de referência | Cache local |
| Bulkhead | Isolamento de threads | Pool separado por serviço |

## 8.2 Tratamento de Erros

* Códigos de erro padronizados
* Mensagens de erro claras (sem exposição de detalhes internos)
* Log de erros para análise
* Alertas para falhas recorrentes

---

# 9. Observabilidade

## 9.1 Métricas

* Tempo de resposta por integração
* Taxa de sucesso/erro
* Volume de chamadas
* Latência de eventos

## 9.2 Logs

* Log de todas as chamadas de integração
* Correlation ID para rastreabilidade
* Níveis: INFO, WARN, ERROR

## 9.3 Alertas

* Falha de integração com serviço crítico
* Tempo de resposta acima do limite
* Taxa de erro acima de 5%

---

# 10. Refinamento Futuro

O modelo deste documento representa a primeira versão das integrações do domínio.

Durante o refinamento, o modelo poderá:

* ser expandido com novas integrações;
* ser ajustado conforme evolução dos domínios;
* ser integrado com plataforma de mensageria;
* ser documentado via AsyncAPI para eventos.

---

# 11. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`INT-MAP-GDO-001`

**Tipo:**

Modelo de Integração.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 12. Próximo Artefato

O próximo artefato recomendado é:

`015-Arquitetura-de-Servicos-Gestao-Documental.md`

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
```

---

# 13. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: integrações, eventos, segurança |

---

**Documento:** 014-Modelo-de-Integracao-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
