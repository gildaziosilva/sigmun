# 018 – Plano de Testes – Gestão Documental

#### Plano de Testes – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-018

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
* `015-Arquitetura-de-Servicos-Gestao-Documental.md`
* `016-Modelo-de-Seguranca-Gestao-Documental.md`
* `017-Modelo-de-Auditoria-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define o **Plano de Testes do Domínio de Gestão Documental do SIGMUN**.

O plano estabelece a estratégia, os níveis, tipos, ambientes, dados, responsabilidades, critérios e evidências necessários para verificar se o domínio atende aos requisitos definidos.

O objetivo é garantir que o domínio seja:

* funcionalmente correto;
* seguro;
* integrado;
* auditável;
* resiliente;
* performático;
* utilizável;
* rastreável;
* compatível com as regras de negócio.

---

# 2. Objetivos

São objetivos deste plano:

1. validar os requisitos funcionais;
2. validar os requisitos não funcionais;
3. verificar as regras de negócio;
4. validar os critérios de aceitação;
5. verificar as integrações;
6. validar o modelo de segurança;
7. verificar a trilha de auditoria;
8. validar o modelo de dados;
9. identificar defeitos;
10. reduzir riscos de implantação;
11. garantir rastreabilidade entre requisitos e testes;
12. produzir evidências de qualidade;
13. apoiar homologação;
14. apoiar implantação;
15. garantir regressão controlada.

---

# 3. Princípios de Testes

## 3.1 Qualidade desde o Início

Os testes deverão ser considerados desde a definição dos requisitos.

## 3.2 Rastreabilidade

Todo teste deverá ser rastreável a um ou mais requisitos.

## 3.3 Independência

Os ambientes de teste deverão ser independentes do ambiente de produção.

## 3.4 Reprodutibilidade

Os testes deverão ser reproduzíveis em diferentes execuções.

## 3.5 Automação

Testes repetitivos deverão ser automatizados.

---

# 4. Níveis de Testes

## 4.1 Testes Unitários

**Escopo:** Componentes individuais (funções, métodos, classes)

**Responsabilidade:** Desenvolvedor

**Ferramentas:** pytest, unittest

**Cobertura mínima:** 80% do código

**Critérios de aceitação:**
* Todos os testes unitários devem passar
* Cobertura de código >= 80%
* Sem erros de lógica identificados

## 4.2 Testes de Integração

**Escopo:** Interação entre componentes e serviços

**Responsabilidade:** Desenvolvedor / QA

**Ferramentas:** pytest, requests

**Cobertura:**
* Integração entre serviços do domínio
* Integração com DOM-IDN (autenticação)
* Integração com DOM-CUM (unidades)
* Integração com DOM-MET (metadados)
* Integração com banco de dados

**Critérios de aceitação:**
* Fluxos completos funcionando
* Dados persistidos corretamente
* Integrações respondendo dentro do tempo esperado

## 4.3 Testes de API

**Escopo:** Endpoints REST do domínio

**Responsabilidade:** QA

**Ferramentas:** pytest, requests, Postman

**Cobertura:**
* Todos os endpoints documentados
* Validação de contratos
* Códigos de status HTTP
* Autenticação e autorização
* Rate limiting

**Critérios de aceitação:**
* Todos os endpoints respondendo corretamente
* Contratos respeitados
* Segurança funcionando

## 4.4 Testes de Sistema

**Escopo:** Funcionalidades completas do domínio

**Responsabilidade:** QA

**Cobertura:**
* Todos os casos de uso
* Todos os critérios de aceitação
* Regras de negócio

**Critérios de aceitação:**
* Funcionalidades completas funcionando
* Regras de negócio atendidas
* Critérios de aceitação satisfeitos

## 4.5 Testes de Aceitação

**Escopo:** Validação com usuários de negócio

**Responsabilidade:** QA + Negócio

**Cobertura:**
* Fluxos principais do negócio
* Cenários de uso real

**Critérios de aceitação:**
* Aprovação do usuário de negócio
* Atendimento às necessidades operacionais

---

# 5. Tipos de Testes

## 5.1 Testes Funcionais

| Tipo | Descrição | Cobertura |
| --- | --- | --- |
| Positivo | Fluxos principais | Todos os requisitos funcionais |
| Negativo | Fluxos de erro | Validações e exceções |
| Limite | Condições de contorno | Campos obrigatórios, tamanhos máximos |
| Regressão | Manutenção de funcionalidades | A cada alteração |

## 5.2 Testes Não Funcionais

| Tipo | Descrição | Critérios |
| --- | --- | --- |
| Performance | Tempo de resposta | Consultas <= 2s |
| Carga | Volume simultâneo | 100 usuários simultâneos |
| Stress | Limite do sistema | Identificar ponto de falha |
| Segurança | Proteção de dados | Sem vulnerabilidades críticas |
| Usabilidade | Facilidade de uso | Tempo de treinamento <= 4h |
| Confiabilidade | Disponibilidade | 99,5% uptime |

## 5.3 Testes de Segurança

| Tipo | Descrição | Cobertura |
| --- | --- | --- |
| Autenticação | Verificar identidade | Tokens JWT, sessões |
| Autorização | Verificar permissões | RBAC, perfis |
| Proteção de dados | Criptografia | Em trânsito e repouso |
| Vulnerabilidades | OWASP Top 10 | SQL Injection, XSS, CSRF |
| Auditoria | Registros de auditoria | Imutabilidade, rastreabilidade |

## 5.4 Testes de Integração

| Tipo | Descrição | Sistemas |
| --- | --- | --- |
| DOM-IDN | Autenticação | Login, permissões |
| DOM-CUM | Unidades | Consulta, listagem |
| DOM-MET | Metadados | Taxonomias, indexação |
| DOM-COMPRAS | Processos | Vínculo de documentos |
| Portal Transparência | Publicação | Documentos públicos |
| ICP-Brasil | Certificados | Validação de assinaturas |

---

# 6. Ambientes de Testes

## 6.1 Ambiente de Desenvolvimento (DEV)

**Finalidade:** Testes unitários e de integração iniciais

**Características:**
* Banco de dados dedicado
* Dados de teste fictícios
* Configurações de debug habilitadas

## 6.2 Ambiente de Testes (QA)

**Finalidade:** Testes funcionais e não funcionais

**Características:**
* Banco de dados dedicado
* Dados de teste representativos
* Integrações com outros domínios
* Configurações similares à produção

## 6.3 Ambiente de Homologação (HML)

**Finalidade:** Validação com usuários de negócio

**Características:**
* Banco de dados similar à produção
* Dados de produção anonimizados
* Todas as integrações ativas
* Configurações idênticas à produção

## 6.4 Ambiente de Produção (PRD)

**Finalidade:** Operação real

**Características:**
* Dados reais
* Alta disponibilidade
* Monitoramento ativo

---

# 7. Dados de Testes

## 7.1 Geração de Dados

| Tipo | Descrição | Quantidade |
| --- | --- | --- |
| Unidades administrativas | Unidades de teste | 10 |
| Usuários | Perfis diversos | 20 |
| Documentos | Tipos variados | 1000 |
| Processos | Processos documentais | 100 |
| Classificações | Plano de classificação | 50 |

## 7.2 Dados Sensíveis

* Dados pessoais devem ser anonimizados
* Documentos sigilosos devem ser marcados como teste
* Dados de produção não devem ser usados em testes

---

# 8. Responsabilidades

## 8.1 Desenvolvedor

* Testes unitários
* Testes de integração
* Correção de defeitos
* Cobertura de código

## 8.2 QA (Quality Assurance)

* Testes funcionais
* Testes não funcionais
* Testes de regressão
* Automação de testes

## 8.3 Negócio

* Testes de aceitação
* Validação de regras de negócio
* Aprovação para produção

## 8.4 DevOps

* Ambientes de testes
* Pipelines de CI/CD
* Monitoramento

---

# 9. Critérios de Entrada e Saída

## 9.1 Critérios de Entrada (Ready for Testing)

* Requisitos aprovados
* Código implementado e revisado
* Testes unitários passando
* Ambiente de testes disponível
* Dados de testes preparados

## 9.2 Critérios de Saída (Done)

* Todos os testes planejados executados
* 100% dos testes críticos passando
* 95% dos testes totais passando
* Nenhum defeito crítico aberto
* Documentação atualizada
* Evidências coletadas

---

# 10. Critérios de Aceitação dos Testes

## 10.1 Testes Funcionais

* Todos os requisitos funcionais testados
* Todas as regras de negócio validadas
* Todos os critérios de aceitação verificados

## 10.2 Testes Não Funcionais

* Tempo de resposta dentro dos limites
* Carga suportada conforme especificado
* Segurança sem vulnerabilidades críticas

## 10.3 Testes de Integração

* Todas as integrações funcionando
* Contratos respeitados
* Tratamento de erros adequado

---

# 11. Métricas de Testes

## 11.1 Métricas de Cobertura

| Métrica | Meta |
| --- | --- |
| Cobertura de código | >= 80% |
| Cobertura de requisitos | 100% |
| Cobertura de regras de negócio | 100% |

## 11.2 Métricas de Qualidade

| Métrica | Meta |
| --- | --- |
| Taxa de sucesso dos testes | >= 95% |
| Defeitos críticos abertos | 0 |
| Defeitos altos abertos | <= 2 |
| Tempo médio de correção | <= 2 dias |

## 11.3 Métricas de Progresso

| Métrica | Descrição |
| --- | --- |
| Testes planejados vs executados | Progresso da execução |
| Testes passando vs falhando | Qualidade do código |
| Defeitos abertos vs fechados | Progresso de correção |

---

# 12. Gerenciamento de Defeitos

## 12.1 Classificação de Severidade

| Nível | Descrição | SLA |
| --- | --- | --- |
| Crítico | Sistema inoperável | 4 horas |
| Alto | Funcionalidade principal afetada | 1 dia |
| Médio | Funcionalidade secundária afetada | 3 dias |
| Baixo | Melhoria ou cosmético | 15 dias |

## 12.2 Fluxo de Defeitos

```text
Aberto
  ↓
Confirmado
  ↓
Em correção
  ↓
Corrigido
  ↓
Em verificação
  ↓
Verificado
  ↓
Fechado
```

---

# 13. Automação de Testes

## 13.1 Escopo da Automação

* Testes de regressão
* Testes de API
* Testes de integração
* Testes de fumaça (smoke tests)

## 13.2 Ferramentas

| Ferramenta | Uso |
| --- | --- |
| pytest | Testes unitários e de integração |
| requests | Testes de API |
| Selenium | Testes de interface (futuro) |
| Locust | Testes de performance |
| OWASP ZAP | Testes de segurança |

## 13.3 Pipeline CI/CD

```text
Commit
  ↓
Build
  ↓
Testes Unitários
  ↓
Testes de Integração
  ↓
Análise de Código
  ↓
Deploy QA
  ↓
Testes de API
  ↓
Testes de Regressão
  ↓
Aprovação
  ↓
Deploy HML
  ↓
Testes de Aceitação
  ↓
Deploy PRD
```

---

# 14. Refinamento Futuro

O plano deste documento representa a primeira versão dos testes do domínio.

Durante o refinamento, o plano poderá:

* ser expandido com novos cenários;
* ser ajustado conforme evolução dos requisitos;
* ser integrado com ferramentas de automação;
* ser atualizado conforme novas regulamentações.

---

# 15. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`TEST-MAP-GDO-001`

**Tipo:**

Plano de Testes.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 16. Próximo Artefato

O próximo artefato recomendado é:

`019-Casos-de-Teste-Gestao-Documental.md`

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
      ↓
017-Modelo de Auditoria
      ↓
018-Plano de Testes
      ↓
019-Casos de Teste
```

---

# 17. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: níveis, tipos, métricas |

---

**Documento:** 018-Plano-de-Testes-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
