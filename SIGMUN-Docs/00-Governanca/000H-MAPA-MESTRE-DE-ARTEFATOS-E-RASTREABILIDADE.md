# 000H – Mapa Mestre de Artefatos e Rastreabilidade

#### Mapa Mestre de Artefatos e Rastreabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Governança / Requisitos / Arquitetura Corporativa

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
* Mapa-de-Secretarias-v1.0.md
* Mapa-de-Servicos-v1.0.md
* Modelo-de-Competencias-v1.0.md
* Modelo-de-Governanca-Administrativa-v1.0.md
* Glossario-de-Negocio-v1.0.md
* Casos-de-Uso-v1.0.md
* Historias-de-Usuario-v1.0.md
* Regras-de-Negocio-v1.0.md
* Requisitos-Funcionais-v1.0.md
* Requisitos-Nao-Funcionais-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md
* Matriz-de-Rastreabilidade-v1.0.md

---

# 1. Finalidade

O **Mapa Mestre de Artefatos e Rastreabilidade** é o instrumento corporativo utilizado para visualizar, controlar e acompanhar os principais artefatos produzidos durante o ciclo de vida do SIGMUN.

Seu objetivo é fornecer uma visão integrada de:

* documentos;
* modelos;
* requisitos;
* regras;
* processos;
* serviços;
* casos de uso;
* histórias de usuário;
* especificações;
* critérios de aceitação;
* testes;
* componentes;
* decisões arquiteturais;
* evidências;
* entregas.

O documento deverá permitir identificar rapidamente **o que existe, o que está em elaboração, o que está aprovado, o que depende de outro artefato e quais elementos ainda não possuem rastreabilidade completa**.

---

# 2. Objetivos

São objetivos deste documento:

* estabelecer uma visão única dos artefatos do SIGMUN;
* controlar a evolução documental;
* identificar lacunas;
* identificar duplicidades;
* acompanhar dependências;
* apoiar auditorias;
* apoiar governança;
* facilitar análise de impacto;
* garantir rastreabilidade;
* apoiar planejamento;
* apoiar desenvolvimento;
* apoiar testes;
* apoiar homologação;
* preservar conhecimento institucional.

---

# 3. Princípio Fundamental

O SIGMUN deverá buscar rastreabilidade **da necessidade até a evidência de atendimento**.

A cadeia de referência deverá ser:

```text
Necessidade
    ↓
Objetivo
    ↓
Capacidade
    ↓
Domínio
    ↓
Processo
    ↓
Serviço
    ↓
Caso de Uso / História de Usuário
    ↓
Regra de Negócio
    ↓
Requisito Funcional
    ↓
Requisito Não Funcional
    ↓
Especificação
    ↓
Implementação
    ↓
Critério de Aceitação
    ↓
Teste
    ↓
Evidência
    ↓
Entrega
```

Essa cadeia constitui a **rastreabilidade ponta a ponta do SIGMUN**.

---

# 4. O que é um Artefato

Para fins do SIGMUN, considera-se artefato qualquer elemento formal produzido, mantido ou utilizado para representar conhecimento, decisão, requisito, modelo, especificação, implementação, validação ou evidência.

Exemplos:

* documento;
* requisito;
* regra;
* processo;
* serviço;
* modelo;
* decisão;
* caso de uso;
* história;
* especificação;
* teste;
* evidência;
* código;
* configuração.

---

# 5. Classificação dos Artefatos

Os artefatos poderão ser classificados em grandes grupos.

## 5.1 Governança

Exemplos:

```text
Políticas
Planos
Modelos de Governança
Registros de Decisão
Matrizes
Indicadores
```

---

## 5.2 Estratégia

Exemplos:

```text
Objetivos
Diretrizes
Princípios
Cadeia de Valor
Capacidades
```

---

## 5.3 Negócio

Exemplos:

```text
Atores
Domínios
Secretarias
Processos
Serviços
Competências
Glossário
```

---

## 5.4 Requisitos

Exemplos:

```text
Casos de Uso
Histórias de Usuário
Regras de Negócio
Requisitos Funcionais
Requisitos Não Funcionais
```

---

## 5.5 Especificação

Exemplos:

```text
Especificações Funcionais
Especificações Técnicas
Contratos de API
Modelos de Dados
Interfaces
Workflows
```

---

## 5.6 Arquitetura

Exemplos:

```text
Arquitetura de Negócio
Arquitetura de Dados
Arquitetura de Software
Arquitetura de Segurança
Arquitetura de Integração
Arquitetura de Implantação
Arquitetura de UX
```

---

## 5.7 Implementação

Exemplos:

```text
Código
Componentes
APIs
Configurações
Scripts
Infraestrutura
```

---

## 5.8 Qualidade

Exemplos:

```text
Critérios de Aceitação
Casos de Teste
Resultados de Teste
Evidências
Relatórios
```

---

# 6. Ciclo de Vida dos Artefatos

Cada artefato deverá possuir um estado.

Estados recomendados:

```text
Proposto
Em Elaboração
Em Análise
Em Revisão
Em Validação
Aprovado
Vigente
Em Atualização
Superado
Arquivado
Cancelado
```

---

# 7. Estados de Engenharia

Para artefatos diretamente relacionados ao desenvolvimento:

```text
Backlog
Análise
Especificação
Desenvolvimento
Code Review
Teste
Homologação
Produção
Encerrado
```

---

# 8. Identificação dos Artefatos

Todo artefato rastreável deverá possuir identificador único.

Exemplos:

| Tipo                    | Prefixo |
| ----------------------- | ------- |
| Objetivo                | `OBJ-`  |
| Capacidade              | `CAP-`  |
| Domínio                 | `DOM-`  |
| Processo                | `PROC-` |
| Serviço                 | `SERV-` |
| Caso de Uso             | `UC-`   |
| História de Usuário     | `HU-`   |
| Regra de Negócio        | `RN-`   |
| Requisito Funcional     | `RF-`   |
| Requisito Não Funcional | `RNF-`  |
| Especificação           | `ESP-`  |
| Critério de Aceitação   | `CA-`   |
| Teste                   | `TST-`  |
| Decisão Arquitetural    | `ADR-`  |
| Evidência               | `EVD-`  |

---

# 9. Identificação por Domínio

Quando aplicável, o identificador deverá incorporar o domínio.

Exemplo:

```text
PROC-COMPRAS-001
SERV-COMPRAS-001
UC-COMPRAS-001
HU-COMPRAS-001
RN-COMPRAS-001
RF-COMPRAS-001
RNF-COMPRAS-001
ESP-COMPRAS-001
CA-COMPRAS-001
TST-COMPRAS-001
```

---

# 10. Registro Mestre de Artefatos

O SIGMUN deverá manter um inventário central dos artefatos.

Modelo:

| ID                 | Artefato               | Tipo       | Domínio | Versão | Status     | Responsável   |
| ------------------ | ---------------------- | ---------- | ------- | ------ | ---------- | ------------- |
| `CAP-COMPRAS-001`  | Gestão de Compras      | Capacidade | Compras | 1.0    | Vigente    | Equipe SIGMUN |
| `PROC-COMPRAS-001` | Contratação            | Processo   | Compras | 1.0    | Vigente    | Equipe SIGMUN |
| `SERV-COMPRAS-001` | Gestão de Contratações | Serviço    | Compras | 1.0    | Em Análise | Equipe SIGMUN |
| `RF-COMPRAS-001`   | Cadastrar Fornecedor   | RF         | Compras | 1.0    | Proposto   | Equipe SIGMUN |

Este registro deverá evoluir conforme o projeto avançar.

---

# 11. Relação entre Artefatos

Os artefatos deverão possuir relacionamentos explícitos.

Exemplo:

```text
CAP-COMPRAS-001
       ↓
PROC-COMPRAS-001
       ↓
SERV-COMPRAS-001
       ↓
UC-COMPRAS-001
       ↓
RF-COMPRAS-001
```

---

# 12. Rastreabilidade Vertical

A rastreabilidade vertical demonstra a relação entre níveis diferentes de abstração.

Exemplo:

```text
Objetivo Estratégico
        ↓
Capacidade
        ↓
Processo
        ↓
Serviço
        ↓
Requisito
        ↓
Teste
```

---

# 13. Rastreabilidade Horizontal

A rastreabilidade horizontal relaciona artefatos do mesmo nível.

Exemplo:

```text
RF-COMPRAS-001
       ↕
RF-COMPRAS-002
       ↕
RF-COMPRAS-003
```

Essa relação poderá indicar:

* dependência;
* complementaridade;
* conflito;
* reutilização;
* precedência.

---

# 14. Rastreabilidade Bidirecional

A rastreabilidade deverá funcionar nos dois sentidos.

### Para frente

```text
Necessidade
   ↓
Requisito
   ↓
Implementação
   ↓
Teste
```

### Para trás

```text
Teste
   ↓
Requisito
   ↓
Necessidade
```

Isso permitirá responder tanto:

> "Qual teste comprova este requisito?"

quanto:

> "Por que este requisito existe?"

---

# 15. Rastreabilidade de Negócio

```text
Objetivo
   ↓
Capacidade
   ↓
Processo
   ↓
Serviço
```

---

# 16. Rastreabilidade de Requisitos

```text
Serviço
   ↓
Caso de Uso
   ↓
História
   ↓
Regra
   ↓
RF
   ↓
RNF
```

---

# 17. Rastreabilidade Técnica

```text
RF / RNF
    ↓
Especificação
    ↓
Componente
    ↓
Código
    ↓
Teste
```

---

# 18. Rastreabilidade de Qualidade

```text
Requisito
    ↓
Critério de Aceitação
    ↓
Teste
    ↓
Resultado
    ↓
Evidência
```

---

# 19. Rastreabilidade Arquitetural

```text
Requisito
    ↓
Decisão Arquitetural
    ↓
Elemento Arquitetural
    ↓
Implementação
```

---

# 20. Rastreabilidade de Dados

```text
Processo
    ↓
Informação
    ↓
Entidade
    ↓
Atributo
    ↓
Armazenamento
```

---

# 21. Rastreabilidade de Segurança

```text
Ativo
   ↓
Risco
   ↓
Controle
   ↓
Requisito de Segurança
   ↓
Implementação
   ↓
Teste
```

---

# 22. Rastreabilidade de Privacidade

```text
Dado Pessoal
   ↓
Finalidade
   ↓
Tratamento
   ↓
Controle
   ↓
Requisito
   ↓
Evidência
```

---

# 23. Rastreabilidade de Mudanças

Toda mudança relevante deverá permitir identificar:

```text
Mudança
   ↓
Motivo
   ↓
Artefatos afetados
   ↓
Impactos
   ↓
Decisão
   ↓
Implementação
   ↓
Teste
```

---

# 24. Matriz Mestre de Rastreabilidade

A matriz deverá permitir consolidar relações.

| Origem     | Relação      | Destino    | Status   |
| ---------- | ------------ | ---------- | -------- |
| `OBJ-001`  | gera         | `CAP-001`  | Completa |
| `CAP-001`  | suporta      | `PROC-001` | Completa |
| `PROC-001` | realiza      | `SERV-001` | Completa |
| `SERV-001` | possui       | `UC-001`   | Completa |
| `UC-001`   | gera         | `RF-001`   | Completa |
| `RF-001`   | possui       | `CA-001`   | Pendente |
| `CA-001`   | validado por | `TST-001`  | Pendente |

---

# 25. Matriz de Cobertura

A cobertura deverá ser monitorada.

Exemplo:

| Artefato     | Total | Com rastreabilidade | Sem rastreabilidade |
| ------------ | ----: | ------------------: | ------------------: |
| Processos    |   100 |                  90 |                  10 |
| Serviços     |    80 |                  70 |                  10 |
| Casos de Uso |   150 |                 130 |                  20 |
| RF           |   500 |                 480 |                  20 |
| RNF          |   100 |                  95 |                   5 |
| Critérios    |   500 |                 470 |                  30 |
| Testes       |   700 |                 650 |                  50 |

---

# 26. Indicadores de Rastreabilidade

Poderão ser acompanhados:

### Cobertura de Origem

Percentual de requisitos com origem identificada.

### Cobertura de Critérios

Percentual de requisitos com critérios de aceitação.

### Cobertura de Testes

Percentual de requisitos com testes associados.

### Cobertura de Evidências

Percentual de testes aprovados com evidência.

### Cobertura de Implementação

Percentual de requisitos implementados.

---

# 27. Índice de Rastreabilidade

Poderá ser criado um indicador corporativo:

```text
ITR =

(Requisitos com rastreabilidade completa /
 Total de requisitos aplicáveis) × 100
```

A fórmula poderá ser refinada posteriormente pelo modelo de indicadores do SIGMUN.

---

# 28. Rastreabilidade Completa

Considera-se uma cadeia completa quando houver, conforme aplicabilidade:

```text
Origem
  ↓
Negócio
  ↓
Requisito
  ↓
Especificação
  ↓
Critério
  ↓
Teste
  ↓
Evidência
```

Nem todo artefato necessitará possuir todas as relações.

A aplicabilidade deverá ser registrada.

---

# 29. Artefatos Órfãos

São considerados órfãos os artefatos sem relacionamento necessário com outros artefatos.

Exemplos:

```text
RF sem origem
RF sem critério
RF sem teste
Teste sem requisito
Processo sem serviço
Serviço sem processo
Código sem requisito
```

Artefatos órfãos deverão ser analisados.

---

# 30. Artefatos Duplicados

O mapa deverá permitir identificar artefatos que representam a mesma necessidade.

Quando identificada duplicidade:

1. analisar;
2. consolidar quando possível;
3. cancelar o duplicado;
4. preservar histórico;
5. atualizar referências.

---

# 31. Artefatos Conflitantes

Quando houver requisitos, regras ou decisões conflitantes, deverá ser aberta análise formal.

Exemplo:

```text
RN-001
    ↕
RN-002
    ↓
Conflito
    ↓
Análise
    ↓
Decisão
```

Quando aplicável, a decisão deverá ser registrada em ADR.

---

# 32. Artefatos Superados

Um artefato substituído não deverá ser simplesmente apagado.

Deverá ser marcado como:

```text
Superado
```

e possuir referência para o artefato substituto.

---

# 33. Artefatos Cancelados

Artefatos cancelados deverão permanecer rastreáveis para preservação histórica.

Deverão registrar:

* motivo;
* data;
* responsável;
* decisão;
* substituto, quando houver.

---

# 34. Controle de Versão

Cada artefato deverá possuir versão conforme o padrão documental do SIGMUN.

A alteração de um artefato poderá provocar impacto em artefatos relacionados.

---

# 35. Análise de Impacto

Antes de alterar um artefato crítico, deverá ser possível identificar:

```text
Artefato alterado
       ↓
Dependentes
       ↓
Impactos
       ↓
Testes afetados
       ↓
Documentos afetados
       ↓
Decisões afetadas
```

---

# 36. Impacto em Requisitos

Alterar uma regra poderá afetar:

```text
RN
 ↓
RF
 ↓
RNF
 ↓
ESP
 ↓
CA
 ↓
TST
```

---

# 37. Impacto em Processos

Alterar um processo poderá afetar:

```text
Processo
 ↓
Serviço
 ↓
Caso de Uso
 ↓
Requisitos
 ↓
Implementação
```

---

# 38. Impacto em Arquitetura

Alterar um requisito crítico poderá provocar:

```text
Requisito
 ↓
Arquitetura
 ↓
Componentes
 ↓
Infraestrutura
 ↓
Custos
```

---

# 39. Impacto em Dados

Alterações poderão afetar:

```text
Requisito
 ↓
Modelo Conceitual
 ↓
Modelo Lógico
 ↓
Modelo Físico
 ↓
Migração
 ↓
Integrações
```

---

# 40. Impacto em Testes

Toda alteração relevante deverá avaliar:

* casos de teste afetados;
* critérios afetados;
* dados de teste;
* evidências;
* regressão.

---

# 41. Dashboard Mestre

O Mapa Mestre poderá futuramente alimentar um painel com:

```text
┌─────────────────────────────┐
│ ARTEFATOS                   │
├─────────────────────────────┤
│ Total                       │
│ Vigentes                    │
│ Em elaboração               │
│ Em revisão                  │
│ Superados                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ RASTREABILIDADE              │
├─────────────────────────────┤
│ Cobertura de origem         │
│ Cobertura de critérios      │
│ Cobertura de testes         │
│ Cobertura de evidências     │
└─────────────────────────────┘

┌─────────────────────────────┐
│ RISCOS                       │
├─────────────────────────────┤
│ Órfãos                      │
│ Conflitos                   │
│ Duplicidades                │
│ Pendências                  │
└─────────────────────────────┘
```

---

# 42. Governança de Responsabilidades

Cada artefato deverá possuir responsável.

Papéis possíveis:

* proprietário do negócio;
* responsável pelo processo;
* analista de negócio;
* arquiteto;
* analista de requisitos;
* desenvolvedor;
* especialista de segurança;
* especialista de dados;
* responsável por testes;
* gestor;
* equipe SIGMUN.

---

# 43. Dono do Artefato

O responsável pelo artefato deverá garantir:

* qualidade;
* atualização;
* rastreabilidade;
* validação;
* histórico;
* consistência.

---

# 44. Critérios para Considerar um Artefato Completo

Um artefato será considerado completo quando:

* possuir identificação;
* possuir versão;
* possuir responsável;
* possuir status;
* possuir conteúdo suficiente;
* possuir relações aplicáveis;
* possuir validação;
* possuir rastreabilidade.

---

# 45. Critérios para Considerar uma Cadeia Completa

Uma cadeia deverá ser considerada completa quando:

* a origem estiver identificada;
* o requisito estiver definido;
* a implementação estiver relacionada;
* o critério estiver definido;
* o teste existir;
* o resultado estiver registrado;
* a evidência estiver disponível.

---

# 46. Processo de Atualização do Mapa

Sempre que um artefato relevante for criado ou alterado:

```text
Criar / Alterar Artefato
        ↓
Atualizar Registro Mestre
        ↓
Atualizar Relações
        ↓
Avaliar Impactos
        ↓
Atualizar Matriz
        ↓
Validar
```

---

# 47. Revisão Periódica

O Mapa Mestre deverá ser revisado periodicamente.

A revisão deverá identificar:

* artefatos desatualizados;
* relações quebradas;
* requisitos órfãos;
* testes sem requisitos;
* documentos duplicados;
* inconsistências;
* dependências;
* impactos pendentes.

---

# 48. Auditoria

O Mapa Mestre poderá ser utilizado como instrumento de auditoria.

Uma auditoria poderá selecionar qualquer requisito e percorrer sua cadeia:

```text
RF
 ↓
Origem
 ↓
Regra
 ↓
Especificação
 ↓
Critério
 ↓
Teste
 ↓
Evidência
```

---

# 49. Princípio "Nenhum Requisito Sem Origem"

Todo requisito relevante deverá possuir origem identificada.

Exceções deverão ser justificadas.

---

# 50. Princípio "Nenhum Requisito Sem Validação"

Todo requisito implementável deverá possuir critério de aceitação ou método equivalente de validação.

---

# 51. Princípio "Nenhum Requisito Crítico Sem Teste"

Requisitos críticos deverão possuir testes adequados e evidência de atendimento.

---

# 52. Princípio "Nenhum Código Sem Justificativa"

Todo componente relevante deverá possuir rastreabilidade para uma necessidade, requisito, decisão arquitetural ou requisito técnico válido.

---

# 53. Princípio "Nenhum Teste Sem Objetivo"

Todo teste deverá demonstrar alguma propriedade, requisito ou risco identificado.

---

# 54. Princípio "Nenhuma Mudança Sem Impacto"

Alterações relevantes deverão possuir análise de impacto proporcional à sua criticidade.

---

# 55. Modelo de Registro Individual

```markdown
# <ID> – <Nome>

**Tipo:** <Tipo>

**Domínio:** <Domínio>

**Versão:** <Versão>

**Status:** <Status>

**Responsável:** <Responsável>

## Origem

<Origem>

## Relacionamentos

### Depende de

- <ID>

### Gera

- <ID>

### Relaciona-se com

- <ID>

### É validado por

- <ID>

### Implementado por

- <ID>

### Evidenciado por

- <ID>
```

---

# 56. Modelo de Matriz

```markdown
| Origem | Relação | Destino | Status | Observação |
|---|---|---|---|---|
| OBJ-001 | gera | CAP-001 | Completa | |
| CAP-001 | suporta | PROC-001 | Completa | |
| PROC-001 | realiza | SERV-001 | Completa | |
| SERV-001 | possui | UC-001 | Completa | |
| UC-001 | gera | RF-001 | Completa | |
| RF-001 | possui | CA-001 | Pendente | |
| CA-001 | validado por | TST-001 | Pendente | |
```

---

# 57. Exemplo Completo

```text
OBJ-COMPRAS-001
        │
        ▼
CAP-COMPRAS-001
        │
        ▼
PROC-COMPRAS-001
        │
        ▼
SERV-COMPRAS-001
        │
        ▼
UC-COMPRAS-001
        │
        ├──────────────┐
        ▼              ▼
HU-COMPRAS-001    RN-COMPRAS-001
        │              │
        └──────┬───────┘
               ▼
        RF-COMPRAS-001
               │
        ┌──────┴──────┐
        ▼             ▼
 RNF-COMPRAS-001   ESP-COMPRAS-001
        │             │
        └──────┬──────┘
               ▼
         CA-COMPRAS-001
               │
               ▼
         TST-COMPRAS-001
               │
               ▼
         EVD-COMPRAS-001
```

---

# 58. Indicadores de Maturidade

O Mapa Mestre poderá posteriormente alimentar indicadores como:

### Nível 1 — Documentado

O artefato existe.

### Nível 2 — Relacionado

O artefato possui relacionamentos.

### Nível 3 — Rastreável

A cadeia de origem e destino está definida.

### Nível 4 — Verificado

Existe teste ou mecanismo de validação.

### Nível 5 — Evidenciado

Existe evidência objetiva de atendimento.

---

# 59. Visão de Maturidade

```text
                 EVIDENCIADO
                     ▲
                     │
                  TESTADO
                     ▲
                     │
                RASTREÁVEL
                     ▲
                     │
                RELACIONADO
                     ▲
                     │
                DOCUMENTADO
```

Essa estrutura poderá futuramente ser integrada aos modelos de maturidade digital do SIGMUN.

---

# 60. Uso como Instrumento de Gestão

O Mapa Mestre não deverá ser apenas um catálogo documental.

Ele deverá apoiar decisões:

* onde investir;
* quais requisitos priorizar;
* quais processos possuem lacunas;
* quais serviços estão incompletos;
* quais áreas possuem maior risco;
* quais funcionalidades possuem maior impacto;
* quais componentes devem ser reutilizados.

---

# 61. Uso como Instrumento de Arquitetura

O mapa permitirá identificar quais requisitos exercem maior pressão sobre a arquitetura.

Exemplo:

```text
RNF-ESC
RNF-PERF
RNF-SEG
RNF-DISP
RNF-CON
       ↓
Pressões Arquiteturais
       ↓
Decisões Arquiteturais
```

---

# 62. Uso como Instrumento de Desenvolvimento

O desenvolvimento deverá receber requisitos com contexto suficiente.

```text
Processo
   ↓
Serviço
   ↓
Requisito
   ↓
Especificação
   ↓
Desenvolvimento
```

---

# 63. Uso como Instrumento de Testes

A equipe de testes deverá conseguir navegar no sentido inverso:

```text
Teste
   ↓
Critério
   ↓
Requisito
   ↓
Regra
   ↓
Processo
   ↓
Necessidade
```

---

# 64. Uso para Gestão de Mudanças

O mapa deverá permitir estimar o impacto de uma mudança antes de sua aprovação.

Quanto maior o número de dependências, maior poderá ser o impacto potencial.

---

# 65. Uso para Conhecimento Corporativo

O Mapa Mestre deverá funcionar em conjunto com o **Catálogo Corporativo do Conhecimento**.

O Catálogo responde:

> **Onde está o conhecimento?**

O Mapa Mestre responde:

> **Como esse conhecimento se relaciona?**

---

# 66. Uso para Governança

O Mapa Mestre poderá ser utilizado por:

* Comitê de Governança;
* Comitê de Arquitetura;
* Gestão de Produtos;
* Gestão de Projetos;
* Analistas de Negócio;
* Arquitetos;
* Desenvolvimento;
* QA;
* Segurança;
* Dados;
* gestores municipais.

---

# 67. Regra de Ouro

O SIGMUN deverá buscar a seguinte condição:

> **Nenhum artefato importante isolado.**

Todo artefato relevante deverá possuir contexto e relações suficientes para que outra pessoa consiga compreender:

* por que existe;
* de onde veio;
* o que influencia;
* o que depende dele;
* como é validado;
* qual evidência demonstra seu atendimento.

---

# 68. Meta de Rastreabilidade

Como objetivo corporativo, o SIGMUN deverá buscar:

```text
100% dos requisitos críticos
        ↓
100% com origem
        ↓
100% com critérios
        ↓
100% com testes
        ↓
100% com evidências
```

Para requisitos não críticos, as metas poderão ser definidas conforme risco e criticidade.

---

# 69. Próxima Evolução

Após a consolidação deste documento, o Mapa Mestre deverá evoluir para uma estrutura que permita:

* geração automática de matrizes;
* validação automática de referências;
* identificação de artefatos órfãos;
* identificação de links quebrados;
* indicadores de cobertura;
* dashboards;
* análise de impacto;
* integração com ferramentas de desenvolvimento;
* integração com gestão de testes;
* integração com catálogo de conhecimento.

---

# 70. Direção Arquitetural

A longo prazo, o Mapa Mestre poderá deixar de ser apenas um arquivo Markdown e tornar-se uma **estrutura de metadados do SIGMUN**.

Conceitualmente:

```text
              CATÁLOGO CORPORATIVO
                       │
                       ▼
             GRAFO DE CONHECIMENTO
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     NEGÓCIO       REQUISITOS     ARQUITETURA
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  IMPLEMENTAÇÃO
                       │
                       ▼
                    TESTES
                       │
                       ▼
                   EVIDÊNCIAS
```

Essa evolução deverá ser considerada futuramente no **Catálogo Corporativo do Conhecimento** e na arquitetura de dados do SIGMUN.

---

# 71. Checklist de Controle

Antes de considerar uma cadeia de desenvolvimento completa:

* [ ] Existe necessidade identificada?
* [ ] Existe objetivo relacionado?
* [ ] Existe capacidade relacionada?
* [ ] Existe processo relacionado?
* [ ] Existe serviço relacionado?
* [ ] Existem atores identificados?
* [ ] Existem casos de uso ou histórias?
* [ ] Existem regras de negócio?
* [ ] Existem requisitos funcionais?
* [ ] Existem requisitos não funcionais?
* [ ] Existem especificações?
* [ ] Existem critérios de aceitação?
* [ ] Existem testes?
* [ ] Existem evidências?
* [ ] A implementação está rastreada?
* [ ] As relações estão atualizadas?
* [ ] O impacto de mudanças foi avaliado?

---

# 72. Governança

Este documento deverá ser mantido sob governança da arquitetura corporativa e da gestão de requisitos do SIGMUN.

Alterações estruturais neste modelo deverão ser avaliadas antes de sua adoção.

O Mapa Mestre deverá ser atualizado sempre que novos artefatos ou relações relevantes forem criados, modificados, substituídos ou descontinuados.

---

# 73. Disposições Finais

O **Mapa Mestre de Artefatos e Rastreabilidade** constitui o instrumento central de integração entre negócio, requisitos, arquitetura, desenvolvimento e qualidade.

Seu propósito não é substituir os documentos especializados, mas estabelecer as relações entre eles.

A existência de um artefato isolado não será considerada suficiente para demonstrar maturidade.

O valor do artefato será determinado também pela sua capacidade de integrar-se à cadeia de conhecimento e execução do SIGMUN.

O objetivo final é permitir que qualquer requisito relevante possa ser acompanhado:

> **da necessidade que o originou até a evidência de que foi efetivamente atendido.**

---

# Controle de Versões

| Versão | Data       | Descrição                                             |
| ------ | ---------- | ----------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do Mapa Mestre de Artefatos e Rastreabilidade |

---

**Documento:** 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
