# Matriz de Rastreabilidade

#### Matriz de Rastreabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL-v1.0.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000E-GUIA-DE-CONTRIBUICAO.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
* Cadeia-de-Valor-v1.1.md
* Mapa-de-Atores-v1.0.md
* Mapa-de-Capacidades-v1.0.md
* Mapa-de-Dominios-v1.0.md
* Mapa-de-Processos-v1.0.md
* Mapa-de-Servicos-v1.0.md
* Casos-de-Uso-v1.0.md
* Historias-de-Usuario-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md

---

# 1. Finalidade

Este documento estabelece o padrão corporativo para criação, utilização, manutenção e governança da **Matriz de Rastreabilidade do SIGMUN**.

A Matriz de Rastreabilidade tem como finalidade demonstrar a relação entre os diferentes artefatos que compõem o ciclo de transformação de uma necessidade de negócio em uma solução implementada, testada e aceita.

A rastreabilidade deverá permitir responder, de forma objetiva:

* de onde surgiu uma necessidade;
* qual processo ou serviço ela suporta;
* qual requisito foi derivado;
* qual especificação detalha o requisito;
* quais critérios de aceitação validam a solução;
* quais testes verificam o atendimento;
* qual entrega implementou a necessidade;
* quais impactos poderão ocorrer quando houver mudança.

---

# 2. Objetivos

A Matriz deverá apoiar:

* governança de requisitos;
* controle de escopo;
* análise de impacto;
* controle de mudanças;
* validação;
* testes;
* auditoria;
* gestão de qualidade;
* gestão de arquitetura;
* gestão de riscos;
* planejamento;
* homologação;
* manutenção;
* evolução do SIGMUN.

---

# 3. Princípios

A rastreabilidade deverá observar:

* unicidade de identificação;
* relacionamento explícito;
* consistência;
* completude;
* atualização contínua;
* verificabilidade;
* transparência;
* responsabilidade;
* histórico;
* preservação do contexto.

---

# 4. Conceito de Rastreabilidade

Rastreabilidade é a capacidade de acompanhar um elemento ao longo de seu ciclo de vida, identificando suas origens, relacionamentos, dependências, transformações e resultados.

No SIGMUN, a rastreabilidade deverá ser tratada como uma característica estrutural da gestão de requisitos.

---

# 5. Cadeia Corporativa de Rastreabilidade

A cadeia principal deverá ser:

```text
Objetivo Estratégico
        ↓
Capacidade
        ↓
Domínio
        ↓
Processo
        ↓
Serviço
        ↓
Ator / Parte Interessada
        ↓
Caso de Uso / História de Usuário
        ↓
Requisito
        ↓
Especificação
        ↓
Critério de Aceitação
        ↓
Caso de Teste
        ↓
Resultado do Teste
        ↓
Entrega
```

Essa cadeia representa o fluxo principal de rastreabilidade do SIGMUN.

---

# 6. Rastreabilidade Bidirecional

A rastreabilidade deverá ser bidirecional.

## 6.1. Rastreabilidade para Frente

Permite responder:

> O que foi produzido a partir deste requisito?

Exemplo:

```text
REQ-001
   ↓
ESP-001
   ↓
CA-001
   ↓
TEST-001
   ↓
ENT-001
```

---

## 6.2. Rastreabilidade para Trás

Permite responder:

> Por que esta funcionalidade existe?

Exemplo:

```text
ENT-001
   ↑
TEST-001
   ↑
CA-001
   ↑
ESP-001
   ↑
REQ-001
   ↑
HU-001
   ↑
PROC-001
   ↑
OBJ-001
```

---

# 7. Tipos de Rastreabilidade

O SIGMUN deverá considerar diferentes dimensões de rastreabilidade.

## 7.1. Rastreabilidade de Origem

Relaciona um artefato à sua origem.

Exemplo:

```text
HU-COMPRAS-001
        ↓
RF-COMPRAS-001
```

---

## 7.2. Rastreabilidade de Derivação

Indica quando um elemento foi derivado de outro.

Exemplo:

```text
Requisito
   ↓
Especificação
```

---

## 7.3. Rastreabilidade de Validação

Relaciona requisitos aos critérios que comprovam seu atendimento.

```text
Requisito
   ↓
Critério de Aceitação
```

---

## 7.4. Rastreabilidade de Verificação

Relaciona critérios ou requisitos aos testes.

```text
Critério
   ↓
Teste
```

---

## 7.5. Rastreabilidade de Implementação

Relaciona requisitos ou especificações aos componentes que os implementam.

```text
Especificação
   ↓
Componente
```

---

## 7.6. Rastreabilidade de Mudança

Relaciona uma alteração ao conjunto de artefatos impactados.

```text
Mudança
   ↓
Requisito
   ↓
Especificação
   ↓
Teste
```

---

# 8. Identificação dos Artefatos

Todos os elementos rastreáveis deverão possuir identificadores únicos.

Exemplos:

```text
OBJ-001
CAP-001
DOM-001
PROC-001
SERV-001
ATOR-001
UC-001
HU-001
REQ-001
ESP-001
CA-001
TEST-001
ENT-001
```

Os padrões específicos de identificação deverão seguir os documentos corporativos correspondentes.

---

# 9. Regra de Unicidade

Um identificador não deverá ser reutilizado.

Mesmo quando um requisito for cancelado, seu identificador deverá permanecer associado ao histórico.

---

# 10. Estrutura da Matriz

A estrutura mínima recomendada será:

| Origem   | Elemento      | Destino  | Tipo de Relação | Status  |
| -------- | ------------- | -------- | --------------- | ------- |
| PROC-001 | Processo      | HU-001   | Origina         | Vigente |
| HU-001   | História      | REQ-001  | Deriva          | Vigente |
| REQ-001  | Requisito     | ESP-001  | Detalha         | Vigente |
| ESP-001  | Especificação | CA-001   | Define          | Vigente |
| CA-001   | Critério      | TEST-001 | Verifica        | Vigente |

---

# 11. Matriz de Rastreabilidade Principal

A matriz corporativa poderá utilizar a seguinte estrutura:

| ID Objetivo | ID Capacidade | ID Processo | ID Serviço | ID Ator  | ID UC/HU | ID Requisito | ID Especificação | ID Critério | ID Teste | Status  |
| ----------- | ------------- | ----------- | ---------- | -------- | -------- | ------------ | ---------------- | ----------- | -------- | ------- |
| OBJ-001     | CAP-001       | PROC-001    | SERV-001   | ATOR-001 | HU-001   | REQ-001      | ESP-001          | CA-001      | TEST-001 | Vigente |

Essa estrutura deverá ser utilizada quando houver necessidade de visão ponta a ponta.

---

# 12. Matriz de Requisitos

Uma visão específica poderá ser utilizada para controle dos requisitos:

| Requisito | Origem | Especificação | Critério | Teste    | Status  |
| --------- | ------ | ------------- | -------- | -------- | ------- |
| REQ-001   | HU-001 | ESP-001       | CA-001   | TEST-001 | Vigente |
| REQ-002   | UC-002 | ESP-002       | CA-002   | TEST-002 | Vigente |

---

# 13. Matriz de Histórias de Usuário

| História | Processo | Serviço  | Requisito | Critério | Teste    |
| -------- | -------- | -------- | --------- | -------- | -------- |
| HU-001   | PROC-001 | SERV-001 | REQ-001   | CA-001   | TEST-001 |

---

# 14. Matriz de Casos de Uso

| Caso de Uso | Ator     | Processo | Requisito | Especificação | Teste    |
| ----------- | -------- | -------- | --------- | ------------- | -------- |
| UC-001      | ATOR-001 | PROC-001 | REQ-001   | ESP-001       | TEST-001 |

---

# 15. Matriz de Especificações

| Especificação | Requisito | Dados    | Integração | Critério | Teste    |
| ------------- | --------- | -------- | ---------- | -------- | -------- |
| ESP-001       | REQ-001   | DADO-001 | INT-001    | CA-001   | TEST-001 |

---

# 16. Matriz de Critérios de Aceitação

| Critério | Requisito | Especificação | Teste    | Resultado |
| -------- | --------- | ------------- | -------- | --------- |
| CA-001   | REQ-001   | ESP-001       | TEST-001 | Aprovado  |

---

# 17. Matriz de Testes

| Teste    | Requisito | Critério | Especificação | Resultado |
| -------- | --------- | -------- | ------------- | --------- |
| TEST-001 | REQ-001   | CA-001   | ESP-001       | Aprovado  |

---

# 18. Rastreabilidade de Dados

Quando um requisito utilizar dados relevantes, deverá ser possível identificar:

```text
Requisito
   ↓
Especificação
   ↓
Dado
   ↓
Entidade
   ↓
Fonte
   ↓
Destino
```

Essa rastreabilidade deverá estar alinhada ao modelo de dados e à governança de dados do SIGMUN.

---

# 19. Rastreabilidade de Integrações

Quando houver integração:

```text
Requisito
   ↓
Especificação
   ↓
Integração
   ↓
API / Serviço
   ↓
Sistema Externo
```

Deverão ser identificados os artefatos correspondentes.

---

# 20. Rastreabilidade de Segurança

Quando aplicável:

```text
Requisito
   ↓
Especificação
   ↓
Controle de Segurança
   ↓
Teste de Segurança
```

---

# 21. Rastreabilidade de Proteção de Dados

Quando houver tratamento de dados pessoais:

```text
Necessidade
   ↓
Requisito
   ↓
Dado Pessoal
   ↓
Finalidade
   ↓
Controle
   ↓
Teste / Evidência
```

---

# 22. Rastreabilidade de Processos

A matriz deverá permitir identificar quais requisitos suportam determinado processo.

Exemplo:

```text
PROC-COMPRAS-001
        ↓
HU-COMPRAS-001
HU-COMPRAS-002
        ↓
REQ-COMPRAS-001
REQ-COMPRAS-002
```

---

# 23. Rastreabilidade de Serviços

Deverá ser possível identificar quais requisitos sustentam cada serviço.

Exemplo:

```text
SERV-COMPRAS-001
        ↓
REQ-COMPRAS-001
REQ-COMPRAS-002
REQ-COMPRAS-003
```

---

# 24. Rastreabilidade de Capacidades

Deverá ser possível identificar os requisitos que contribuem para determinada capacidade organizacional.

Exemplo:

```text
CAP-COMPRAS-001
        ↓
PROC-COMPRAS-001
        ↓
REQ-COMPRAS-001
REQ-COMPRAS-002
```

---

# 25. Rastreabilidade de Objetivos

A matriz deverá permitir demonstrar como uma necessidade operacional contribui para objetivos estratégicos.

Exemplo:

```text
OBJ-001
   ↓
CAP-001
   ↓
PROC-001
   ↓
SERV-001
   ↓
HU-001
   ↓
REQ-001
```

Essa visão é especialmente importante para governança e priorização.

---

# 26. Rastreabilidade de Valor Público

Quando aplicável, deverá ser possível relacionar uma entrega ao benefício público esperado.

```text
Objetivo
   ↓
Serviço
   ↓
Requisito
   ↓
Entrega
   ↓
Resultado
   ↓
Valor Público
```

---

# 27. Cobertura de Requisitos

A cobertura deverá indicar quantos requisitos possuem os artefatos necessários.

Exemplo:

```text
Requisitos totais: 100

Com especificação: 95
Sem especificação: 5

Com critérios de aceitação: 92
Sem critérios: 8

Com testes: 88
Sem testes: 12
```

---

# 28. Índice de Cobertura

Quando utilizado, poderá ser calculado:

```text
Cobertura = (Elementos rastreados / Elementos totais) × 100
```

Exemplo:

```text
Cobertura de testes =
(Requisitos com testes / Total de requisitos) × 100
```

---

# 29. Requisitos Órfãos

Um requisito será considerado órfão quando não possuir relacionamento necessário com outros artefatos.

Exemplos:

```text
Requisito sem origem
Requisito sem especificação
Requisito sem critério de aceitação
Requisito sem teste
```

Requisitos órfãos deverão ser analisados.

---

# 30. Artefatos Órfãos

Também deverão ser identificados artefatos que não possuam justificativa ou relacionamento.

Exemplo:

```text
Especificação sem requisito relacionado
Teste sem requisito relacionado
História sem processo ou serviço relacionado
```

---

# 31. Relações Inválidas

Deverão ser identificadas relações inconsistentes.

Exemplos:

* requisito relacionado a processo inexistente;
* teste relacionado a requisito cancelado;
* especificação relacionada a requisito inexistente;
* critério relacionado a especificação inexistente.

---

# 32. Análise de Impacto

A matriz deverá ser utilizada para avaliar impactos antes de alterações.

Exemplo:

```text
Alteração:
REQ-COMPRAS-001

Impactos:

ESP-COMPRAS-001
ESP-COMPRAS-002
CA-COMPRAS-001
CA-COMPRAS-002
TEST-COMPRAS-001
TEST-COMPRAS-002
API-COMPRAS-001
```

---

# 33. Análise de Impacto Reversa

Também deverá ser possível partir de um componente alterado e identificar suas origens.

```text
API-COMPRAS-001
       ↑
ESP-COMPRAS-001
       ↑
REQ-COMPRAS-001
       ↑
HU-COMPRAS-001
       ↑
PROC-COMPRAS-001
```

---

# 34. Gestão de Mudanças

Toda mudança relevante deverá avaliar:

* artefatos afetados;
* dependências;
* testes afetados;
* integrações;
* dados;
* segurança;
* documentação;
* impactos operacionais.

---

# 35. Rastreabilidade e Versionamento

A matriz deverá preservar o histórico das relações relevantes.

Alterações deverão registrar:

* versão;
* data;
* responsável;
* motivo;
* impacto.

---

# 36. Status das Relações

As relações poderão possuir:

```text
Proposta
Validada
Vigente
Superada
Cancelada
```

---

# 37. Responsabilidades

## 37.1. Analista de Negócio

Responsável por garantir coerência das relações de negócio.

## 37.2. Analista de Requisitos

Responsável pela rastreabilidade dos requisitos.

## 37.3. Product Owner / Responsável pelo Produto

Responsável pela priorização e validação do valor.

## 37.4. Arquitetura

Responsável por avaliar impactos arquiteturais.

## 37.5. Desenvolvimento

Responsável por manter relações com os elementos implementados quando aplicável.

## 37.6. Testes / Qualidade

Responsável pela rastreabilidade dos testes.

## 37.7. Governança

Responsável por supervisionar a conformidade do processo.

---

# 38. Manutenção

A Matriz deverá ser atualizada sempre que ocorrer alteração relevante em:

* requisitos;
* histórias;
* casos de uso;
* especificações;
* critérios;
* testes;
* processos;
* serviços;
* arquitetura;
* integrações.

---

# 39. Momento da Atualização

A rastreabilidade não deverá ser construída somente ao final do projeto.

Ela deverá ser construída progressivamente.

Fluxo recomendado:

```text
Identificação
      ↓
Relacionamento
      ↓
Refinamento
      ↓
Validação
      ↓
Implementação
      ↓
Teste
      ↓
Aceitação
      ↓
Manutenção
```

---

# 40. Auditoria

A Matriz poderá ser utilizada como evidência de:

* controle de requisitos;
* controle de mudanças;
* qualidade;
* conformidade;
* testes;
* governança;
* prestação de contas.

---

# 41. Rastreabilidade Mínima Obrigatória

Todo requisito considerado vigente deverá possuir, quando aplicável:

```text
Origem
   ↓
Requisito
   ↓
Especificação
   ↓
Critério de Aceitação
   ↓
Teste
```

A ausência de qualquer relação deverá ser justificada.

---

# 42. Rastreabilidade Completa

Para requisitos estratégicos ou críticos, recomenda-se:

```text
Objetivo
   ↓
Capacidade
   ↓
Processo
   ↓
Serviço
   ↓
Ator
   ↓
História / Caso de Uso
   ↓
Requisito
   ↓
Especificação
   ↓
Dados
   ↓
Integração
   ↓
Critério
   ↓
Teste
   ↓
Entrega
   ↓
Resultado
```

---

# 43. Requisitos Legais

Requisitos derivados de legislação deverão possuir rastreabilidade específica.

Exemplo:

```text
Legislação
   ↓
Obrigação
   ↓
Requisito
   ↓
Especificação
   ↓
Critério
   ↓
Teste
```

Deverá ser possível identificar a origem legal da obrigação.

---

# 44. Requisitos de Segurança

Deverão possuir rastreabilidade:

```text
Risco / Ameaça
   ↓
Requisito de Segurança
   ↓
Controle
   ↓
Especificação
   ↓
Teste
```

---

# 45. Requisitos de Dados

Deverão possuir rastreabilidade:

```text
Necessidade
   ↓
Requisito
   ↓
Dado
   ↓
Regra
   ↓
Especificação
   ↓
Teste
```

---

# 46. Requisitos Não Funcionais

Requisitos não funcionais deverão possuir rastreabilidade específica.

Exemplos:

* desempenho;
* disponibilidade;
* segurança;
* acessibilidade;
* escalabilidade;
* interoperabilidade;
* observabilidade.

---

# 47. Rastreabilidade de Arquitetura

Quando um requisito produzir impacto arquitetural:

```text
Requisito
   ↓
Decisão Arquitetural
   ↓
Componente
   ↓
Implementação
```

Quando houver decisão arquitetural relevante, deverá ser avaliada a necessidade de ADR.

---

# 48. Rastreabilidade de Entregas

A entrega deverá ser vinculada aos requisitos que atende.

Exemplo:

| Entrega | Requisito | Versão | Status       |
| ------- | --------- | ------ | ------------ |
| ENT-001 | REQ-001   | 1.0    | Entregue     |
| ENT-002 | REQ-002   | 1.0    | Em validação |

---

# 49. Rastreabilidade de Incidentes e Defeitos

Quando aplicável:

```text
Defeito
   ↓
Teste
   ↓
Critério
   ↓
Requisito
   ↓
Especificação
```

Isso permitirá avaliar o impacto de um defeito sobre o negócio.

---

# 50. Indicadores

A gestão poderá utilizar indicadores como:

### 50.1. Cobertura de Origem

Percentual de requisitos com origem identificada.

### 50.2. Cobertura de Especificação

Percentual de requisitos com especificação.

### 50.3. Cobertura de Aceitação

Percentual de requisitos com critérios de aceitação.

### 50.4. Cobertura de Testes

Percentual de requisitos com testes.

### 50.5. Cobertura Ponta a Ponta

Percentual de requisitos que possuem cadeia completa de rastreabilidade.

---

# 51. Indicador de Rastreabilidade Ponta a Ponta

Poderá ser utilizado:

```text
IRP =
(Requisitos com rastreabilidade completa /
Total de requisitos aplicáveis) × 100
```

A metodologia oficial dos indicadores deverá permanecer alinhada ao modelo corporativo de indicadores do SIGMUN.

---

# 52. Painel de Rastreabilidade

Quando houver ferramenta apropriada, recomenda-se disponibilizar painel contendo:

* total de requisitos;
* requisitos órfãos;
* cobertura de especificações;
* cobertura de critérios;
* cobertura de testes;
* requisitos críticos;
* mudanças pendentes;
* relações inválidas;
* cobertura ponta a ponta.

---

# 53. Matriz de Exemplo

```text
OBJ-001
  ↓
CAP-001
  ↓
PROC-COMPRAS-001
  ↓
SERV-COMPRAS-001
  ↓
HU-COMPRAS-001
  ↓
REQ-COMPRAS-001
  ↓
ESP-COMPRAS-001
  ↓
CA-COMPRAS-001
  ↓
TEST-COMPRAS-001
  ↓
ENT-COMPRAS-001
```

---

# 54. Modelo Corporativo

O modelo mínimo recomendado será:

```markdown
# MATRIZ DE RASTREABILIDADE

#### Matriz de Rastreabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md

---

# 1. Matriz Principal

| Objetivo | Capacidade | Processo | Serviço | Ator | HU/UC | Requisito | Especificação | Critério | Teste | Entrega | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OBJ-001 | CAP-001 | PROC-001 | SERV-001 | ATOR-001 | HU-001 | REQ-001 | ESP-001 | CA-001 | TEST-001 | ENT-001 | Vigente |

---

# 2. Requisitos Órfãos

| Requisito | Problema | Ação |
|---|---|---|
| REQ-XXX | Sem critério | Criar critério |

---

# 3. Cobertura

| Indicador | Total | Cobertos | Percentual |
|---|---:|---:|---:|
| Requisitos | 100 | 95 | 95% |
| Especificações | 95 | 90 | 94,7% |
| Critérios | 100 | 92 | 92% |
| Testes | 100 | 88 | 88% |

---

# 4. Mudanças

| ID | Data | Elemento | Impacto | Status |
|---|---|---|---|---|
| CHG-001 | AAAA-MM-DD | REQ-001 | ESP-001 / TEST-001 | Avaliação |

---

# 5. Observações

<Observações>

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |
```

---

# 55. Governança

A Matriz de Rastreabilidade deverá ser considerada um artefato oficial de governança de requisitos.

Alterações significativas deverão respeitar o processo definido no:

```text
000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
```

---

# 56. Regra Fundamental

Todo requisito relevante deverá permitir responder:

> **Por que existe?**

> **Quem precisa dele?**

> **Qual processo ou serviço ele suporta?**

> **Como foi especificado?**

> **Como será aceito?**

> **Como foi testado?**

> **O que será impactado se ele mudar?**

---

# 57. Disposições Finais

A Matriz de Rastreabilidade constitui mecanismo fundamental para assegurar coerência entre negócio, requisitos, arquitetura, desenvolvimento, testes e operação do SIGMUN.

Sua utilização deverá reduzir a perda de contexto, facilitar a análise de impacto e aumentar a capacidade de governança sobre a evolução do sistema.

A rastreabilidade deverá ser tratada como parte integrante do ciclo de vida dos requisitos e não como atividade documental realizada apenas ao final do desenvolvimento.

---

# Controle de Versões

| Versão | Data       | Descrição                                                  |
| ------ | ---------- | ---------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do padrão corporativo de Matriz de Rastreabilidade |

---

**Documento:** Matriz-de-Rastreabilidade-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
