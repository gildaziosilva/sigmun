# 002 – Mapa de Capacidades – Gestão de Compras e Contratações

#### Mapa de Capacidades – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* Cadeia-de-Valor.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md

---

# 1. Finalidade

O **Mapa de Capacidades – Gestão de Compras e Contratações** identifica e organiza as capacidades que o Município necessita possuir para realizar adequadamente suas atividades de compras e contratações.

As capacidades representam **o que a organização precisa ser capaz de fazer**, independentemente:

* da estrutura organizacional utilizada;
* do processo escolhido;
* da tecnologia empregada;
* do sistema utilizado;
* da unidade responsável;
* da forma de execução.

Este documento estabelece a visão estrutural das capacidades do domínio e servirá de referência para:

* processos;
* serviços;
* requisitos;
* arquitetura;
* dados;
* sistemas;
* competências;
* indicadores;
* governança;
* evolução do domínio.

---

# 2. Conceito de Capacidade

Para o SIGMUN, uma capacidade representa uma aptidão organizacional necessária para produzir determinado resultado.

A capacidade responde à pergunta:

> **"O que o Município precisa ser capaz de fazer?"**

Não responde diretamente:

> "Qual tela deverá existir?"

nem:

> "Qual procedimento deverá ser executado?"

nem:

> "Qual sistema deverá implementar a função?"

---

# 3. Diferença entre Capacidade, Processo, Serviço e Funcionalidade

A distinção deverá ser preservada:

```text
CAPACIDADE
O que a organização precisa ser capaz de fazer.

        ↓

PROCESSO
Como uma atividade organizacional é executada.

        ↓

SERVIÇO
O que é disponibilizado para um usuário ou consumidor.

        ↓

CASO DE USO
Como um ator interage para alcançar um resultado.

        ↓

REQUISITO
O que a solução deve atender.

        ↓

FUNCIONALIDADE
Como o sistema materializa determinado requisito.
```

---

# 4. Princípios do Mapa de Capacidades

O mapa deverá observar os seguintes princípios:

* capacidades devem ser relativamente estáveis;
* capacidades não devem depender de tecnologia específica;
* capacidades não devem ser confundidas com departamentos;
* uma capacidade pode envolver várias unidades;
* uma capacidade pode ser suportada por vários processos;
* uma capacidade pode ser suportada por vários sistemas;
* uma capacidade pode evoluir sem necessariamente alterar sua identidade;
* capacidades devem estar relacionadas aos objetivos do domínio;
* capacidades devem ser rastreáveis aos processos e serviços.

---

# 5. Visão Geral das Capacidades

O domínio de Gestão de Compras e Contratações será organizado inicialmente nos seguintes grupos:

```text
CAP-COMPRAS-01 – Planejamento

CAP-COMPRAS-02 – Gestão da Necessidade

CAP-COMPRAS-03 – Gestão da Requisição

CAP-COMPRAS-04 – Gestão da Especificação

CAP-COMPRAS-05 – Gestão de Preços

CAP-COMPRAS-06 – Gestão do Processo de Contratação

CAP-COMPRAS-07 – Gestão de Fornecedores

CAP-COMPRAS-08 – Gestão do Procedimento de Contratação

CAP-COMPRAS-09 – Gestão da Formalização

CAP-COMPRAS-10 – Gestão Contratual

CAP-COMPRAS-11 – Gestão da Execução

CAP-COMPRAS-12 – Fiscalização

CAP-COMPRAS-13 – Gestão do Recebimento

CAP-COMPRAS-14 – Gestão Documental

CAP-COMPRAS-15 – Gestão da Transparência

CAP-COMPRAS-16 – Controle e Auditoria

CAP-COMPRAS-17 – Gestão de Informações e Indicadores

CAP-COMPRAS-18 – Integração
```

---

# 6. Hierarquia de Capacidades

A estrutura inicial será:

```text
Gestão de Compras e Contratações
│
├── Planejamento
│
├── Gestão da Necessidade
│
├── Gestão da Requisição
│
├── Gestão da Especificação
│
├── Gestão de Preços
│
├── Gestão do Processo
│
├── Gestão de Fornecedores
│
├── Gestão do Procedimento
│
├── Gestão da Formalização
│
├── Gestão Contratual
│
├── Gestão da Execução
│
├── Fiscalização
│
├── Recebimento
│
├── Gestão Documental
│
├── Transparência
│
├── Controle e Auditoria
│
├── Informações e Indicadores
│
└── Integração
```

---

# 7. CAP-COMPRAS-01 – Planejamento

**Nome:** Planejamento de Compras e Contratações

**Descrição:**

Capacidade de planejar, consolidar, priorizar e acompanhar as necessidades futuras de compras e contratações do Município.

**Objetivo:**

Permitir que as contratações sejam planejadas de forma coordenada e alinhada às necessidades administrativas.

**Inclui:**

* identificação de necessidades futuras;
* consolidação de demandas;
* planejamento temporal;
* priorização;
* acompanhamento;
* revisão;
* consolidação das informações.

**Atores relacionados:**

* Unidade Requisitante;
* Gestor da Unidade;
* Unidade de Compras;
* Autoridade Competente.

**Processos relacionados:**

* `PROC-COMPRAS-001 – Planejamento de Contratações`

---

# 8. CAP-COMPRAS-02 – Gestão da Necessidade

**Nome:** Gestão da Necessidade

**Descrição:**

Capacidade de identificar, registrar, justificar, avaliar e acompanhar necessidades de aquisição ou contratação.

**Objetivo:**

Garantir que cada contratação tenha uma necessidade administrativa identificada e contextualizada.

**Inclui:**

* identificação;
* descrição;
* justificativa;
* origem;
* prioridade;
* classificação;
* análise;
* acompanhamento.

**Atores relacionados:**

* Servidor Solicitante;
* Unidade Requisitante;
* Gestor da Unidade;
* Unidade de Compras.

**Processos relacionados:**

* `PROC-COMPRAS-002 – Registro de Necessidade`

---

# 9. CAP-COMPRAS-03 – Gestão da Requisição

**Nome:** Gestão da Requisição de Compra ou Contratação

**Descrição:**

Capacidade de formalizar a necessidade por meio de uma requisição estruturada.

**Inclui:**

* criação;
* alteração;
* validação;
* encaminhamento;
* aprovação;
* devolução;
* acompanhamento;
* cancelamento.

**Resultado esperado:**

Uma requisição formalmente registrada e apta a seguir para as etapas subsequentes.

---

# 10. CAP-COMPRAS-04 – Gestão da Especificação

**Nome:** Gestão da Especificação do Objeto

**Descrição:**

Capacidade de definir e manter as características necessárias para identificar adequadamente o objeto pretendido.

**Inclui:**

* descrição;
* características;
* quantidades;
* unidades;
* requisitos técnicos;
* critérios de atendimento;
* documentação complementar.

**Princípio:**

A especificação deverá ser suficientemente clara para permitir a compreensão do objeto e a avaliação de seu atendimento.

---

# 11. CAP-COMPRAS-05 – Gestão de Preços

**Nome:** Gestão de Pesquisa e Estimativa de Preços

**Descrição:**

Capacidade de registrar, organizar, analisar e utilizar informações relacionadas à formação da estimativa de preços.

**Inclui:**

* fontes de preço;
* registros de pesquisa;
* propostas;
* referências;
* comparações;
* memória de cálculo;
* estimativa;
* evidências.

**Observação:**

Os métodos específicos deverão ser definidos de acordo com a legislação e regulamentação aplicáveis.

---

# 12. CAP-COMPRAS-06 – Gestão do Processo de Contratação

**Nome:** Gestão do Processo de Contratação

**Descrição:**

Capacidade de estruturar e acompanhar o processo administrativo relacionado à contratação.

**Inclui:**

* abertura;
* classificação;
* organização;
* tramitação;
* instrução;
* análise;
* encaminhamento;
* controle de pendências;
* encerramento.

**Resultado esperado:**

Processo administrativo íntegro, organizado e rastreável.

---

# 13. CAP-COMPRAS-07 – Gestão de Fornecedores

**Nome:** Gestão de Fornecedores

**Descrição:**

Capacidade de utilizar e manter informações necessárias sobre fornecedores e participantes das contratações.

**Inclui:**

* identificação;
* cadastro;
* documentação;
* contatos;
* participação;
* relacionamento contratual;
* histórico;
* situação.

**Princípio corporativo:**

Sempre que possível, deverá ser utilizado o cadastro corporativo existente, evitando duplicidade de registros.

---

# 14. CAP-COMPRAS-08 – Gestão do Procedimento de Contratação

**Nome:** Gestão do Procedimento de Contratação

**Descrição:**

Capacidade de conduzir e registrar as etapas do procedimento de contratação aplicável.

**Inclui:**

* definição do procedimento;
* preparação;
* participantes;
* documentação;
* etapas;
* atos;
* decisões;
* resultados;
* registros.

**Observação:**

A solução deverá permitir diferentes modalidades ou procedimentos conforme a legislação aplicável, sem assumir previamente uma única forma de contratação.

---

# 15. CAP-COMPRAS-09 – Gestão da Formalização

**Nome:** Gestão da Formalização da Contratação

**Descrição:**

Capacidade de transformar o resultado do procedimento em instrumento formal de contratação.

**Inclui:**

* elaboração;
* validação;
* aprovação;
* assinatura;
* publicação quando aplicável;
* registro;
* vinculação ao processo.

---

# 16. CAP-COMPRAS-10 – Gestão Contratual

**Nome:** Gestão de Contratos

**Descrição:**

Capacidade de registrar, acompanhar e administrar contratos e instrumentos relacionados.

**Inclui:**

* cadastro;
* vigência;
* valores;
* obrigações;
* responsáveis;
* prazos;
* alterações;
* aditivos;
* ocorrências;
* encerramento.

---

# 17. CAP-COMPRAS-11 – Gestão da Execução

**Nome:** Gestão da Execução Contratual

**Descrição:**

Capacidade de acompanhar a execução do objeto contratado.

**Inclui:**

* entregas;
* serviços;
* prazos;
* obrigações;
* ocorrências;
* não conformidades;
* evidências;
* providências.

---

# 18. CAP-COMPRAS-12 – Fiscalização

**Nome:** Fiscalização Contratual

**Descrição:**

Capacidade de acompanhar e registrar a conformidade da execução contratual.

**Inclui:**

* designação;
* registros;
* inspeções;
* ocorrências;
* evidências;
* não conformidades;
* notificações;
* providências;
* acompanhamento.

**Atores principais:**

* Fiscal do Contrato;
* Gestor do Contrato.

---

# 19. CAP-COMPRAS-13 – Gestão do Recebimento

**Nome:** Gestão do Recebimento

**Descrição:**

Capacidade de registrar e controlar o recebimento dos bens, serviços ou objetos contratados.

**Inclui:**

* recebimento;
* conferência;
* validação;
* aceite;
* rejeição;
* registro de divergências;
* evidências;
* encaminhamento.

---

# 20. CAP-COMPRAS-14 – Gestão Documental

**Nome:** Gestão Documental de Compras e Contratações

**Descrição:**

Capacidade de organizar, preservar, localizar e controlar documentos e evidências relacionados às contratações.

**Inclui:**

* classificação;
* vinculação;
* versionamento;
* armazenamento;
* consulta;
* controle de acesso;
* retenção;
* preservação;
* auditoria.

---

# 21. CAP-COMPRAS-15 – Gestão da Transparência

**Nome:** Transparência das Compras e Contratações

**Descrição:**

Capacidade de disponibilizar informações públicas relacionadas às compras e contratações, respeitando as políticas de classificação da informação.

**Inclui:**

* seleção das informações públicas;
* publicação;
* consulta;
* pesquisa;
* indicadores;
* documentos públicos;
* histórico.

**Princípio:**

> **Aberto sempre que possível, restrito sempre que necessário.**

---

# 22. CAP-COMPRAS-16 – Controle e Auditoria

**Nome:** Controle e Auditoria de Compras e Contratações

**Descrição:**

Capacidade de acompanhar, verificar e auditar os processos e registros relacionados às contratações.

**Inclui:**

* trilhas de auditoria;
* verificações;
* apontamentos;
* recomendações;
* acompanhamento;
* evidências;
* histórico;
* prestação de informações.

---

# 23. CAP-COMPRAS-17 – Gestão de Informações e Indicadores

**Nome:** Gestão de Informações e Indicadores

**Descrição:**

Capacidade de transformar os dados das compras e contratações em informações úteis para gestão, controle, transparência e tomada de decisão.

**Inclui:**

* consolidação;
* indicadores;
* painéis;
* relatórios;
* análises;
* tendências;
* comparações;
* alertas.

---

# 24. CAP-COMPRAS-18 – Integração

**Nome:** Integração de Compras e Contratações

**Descrição:**

Capacidade de integrar informações e processos do domínio com outros domínios e sistemas.

**Inclui:**

* integração de dados;
* APIs;
* eventos;
* sincronização;
* interoperabilidade;
* validações;
* troca de informações.

**Potenciais integrações:**

* orçamento;
* contabilidade;
* financeiro;
* patrimônio;
* almoxarifado;
* cadastro;
* identidade;
* gestão documental;
* transparência.

---

# 25. Matriz de Capacidades

| ID               | Capacidade                | Categoria   | Criticidade Inicial |
| ---------------- | ------------------------- | ----------- | ------------------- |
| `CAP-COMPRAS-01` | Planejamento              | Estratégica | Alta                |
| `CAP-COMPRAS-02` | Gestão da Necessidade     | Negócio     | Alta                |
| `CAP-COMPRAS-03` | Gestão da Requisição      | Negócio     | Alta                |
| `CAP-COMPRAS-04` | Gestão da Especificação   | Negócio     | Alta                |
| `CAP-COMPRAS-05` | Gestão de Preços          | Negócio     | Alta                |
| `CAP-COMPRAS-06` | Gestão do Processo        | Negócio     | Crítica             |
| `CAP-COMPRAS-07` | Gestão de Fornecedores    | Negócio     | Alta                |
| `CAP-COMPRAS-08` | Gestão do Procedimento    | Negócio     | Crítica             |
| `CAP-COMPRAS-09` | Gestão da Formalização    | Negócio     | Crítica             |
| `CAP-COMPRAS-10` | Gestão Contratual         | Negócio     | Crítica             |
| `CAP-COMPRAS-11` | Gestão da Execução        | Negócio     | Alta                |
| `CAP-COMPRAS-12` | Fiscalização              | Controle    | Crítica             |
| `CAP-COMPRAS-13` | Gestão do Recebimento     | Operacional | Alta                |
| `CAP-COMPRAS-14` | Gestão Documental         | Transversal | Crítica             |
| `CAP-COMPRAS-15` | Transparência             | Governança  | Alta                |
| `CAP-COMPRAS-16` | Controle e Auditoria      | Governança  | Crítica             |
| `CAP-COMPRAS-17` | Informações e Indicadores | Gestão      | Alta                |
| `CAP-COMPRAS-18` | Integração                | Transversal | Crítica             |

---

# 26. Categorias das Capacidades

As capacidades podem ser agrupadas em cinco grandes categorias.

## 26.1 Capacidades Estratégicas

* Planejamento;
* Informações e Indicadores.

## 26.2 Capacidades de Negócio

* Gestão da Necessidade;
* Gestão da Requisição;
* Gestão da Especificação;
* Gestão de Preços;
* Gestão do Processo;
* Gestão de Fornecedores;
* Gestão do Procedimento;
* Gestão da Formalização;
* Gestão Contratual;
* Gestão da Execução.

## 26.3 Capacidades Operacionais

* Gestão do Recebimento;
* Fiscalização.

## 26.4 Capacidades de Governança

* Transparência;
* Controle e Auditoria.

## 26.5 Capacidades Transversais

* Gestão Documental;
* Integração.

---

# 27. Cadeia de Capacidades

A cadeia principal poderá ser representada como:

```text
Planejar
   ↓
Identificar Necessidade
   ↓
Requisitar
   ↓
Especificar
   ↓
Estimar
   ↓
Instruir
   ↓
Contratar
   ↓
Formalizar
   ↓
Gerir Contrato
   ↓
Executar
   ↓
Fiscalizar
   ↓
Receber
   ↓
Encerrar
```

Capacidades transversais:

```text
Gestão Documental
        │
        ├── apoia todas as etapas
        │
Controle e Auditoria
        │
        ├── acompanha todas as etapas
        │
Transparência
        │
        ├── disponibiliza informações públicas
        │
Integração
        │
        └── conecta o domínio aos demais sistemas
```

---

# 28. Capacidade x Unidade Organizacional

Uma capacidade não deverá ser associada permanentemente a uma única secretaria ou departamento.

Exemplo:

```text
CAP-COMPRAS-10
Gestão Contratual

pode envolver:

├── Unidade de Compras
├── Unidade Requisitante
├── Gestor do Contrato
├── Fiscal do Contrato
├── Jurídico
├── Financeiro
└── Controle Interno
```

A capacidade pertence à organização, não exclusivamente à unidade.

---

# 29. Capacidade x Atores

As principais relações iniciais são:

| Capacidade    | Principais Atores                      |
| ------------- | -------------------------------------- |
| Planejamento  | Unidade Requisitante, Gestor, Compras  |
| Necessidade   | Servidor, Unidade Requisitante, Gestor |
| Requisição    | Servidor, Gestor, Compras              |
| Especificação | Unidade Requisitante, Compras          |
| Preços        | Compras, Agente, Fornecedor            |
| Processo      | Compras, Agente, Jurídico              |
| Fornecedor    | Compras, Agente, Fornecedor            |
| Procedimento  | Agente, Equipe de Apoio, Autoridade    |
| Formalização  | Autoridade, Jurídico, Compras          |
| Contrato      | Gestor, Fiscal, Fornecedor             |
| Execução      | Gestor, Fiscal, Fornecedor             |
| Fiscalização  | Fiscal, Gestor                         |
| Recebimento   | Unidade Requisitante, Fiscal           |
| Documental    | Todos os atores autorizados            |
| Transparência | Cidadão, Controle, Administração       |
| Controle      | Controle Interno, Órgãos de Controle   |
| Indicadores   | Gestão, Controle, Administração        |
| Integração    | Sistemas e domínios relacionados       |

---

# 30. Capacidade x Processos

A relação inicial é:

| Capacidade              | Processo Principal |
| ----------------------- | ------------------ |
| Planejamento            | `PROC-COMPRAS-001` |
| Gestão da Necessidade   | `PROC-COMPRAS-002` |
| Gestão da Requisição    | `PROC-COMPRAS-003` |
| Gestão da Especificação | `PROC-COMPRAS-004` |
| Gestão de Preços        | `PROC-COMPRAS-005` |
| Gestão do Processo      | `PROC-COMPRAS-006` |
| Gestão do Procedimento  | `PROC-COMPRAS-007` |
| Gestão da Formalização  | `PROC-COMPRAS-008` |
| Gestão Contratual       | `PROC-COMPRAS-009` |
| Fiscalização            | `PROC-COMPRAS-010` |
| Recebimento             | `PROC-COMPRAS-011` |
| Encerramento            | `PROC-COMPRAS-012` |

As capacidades transversais deverão estar relacionadas a múltiplos processos.

---

# 31. Capacidade x Serviços

Os serviços deverão materializar capacidades para seus consumidores.

Exemplo:

```text
CAP-COMPRAS-03
Gestão da Requisição
       ↓
SERV-COMPRAS-002
Solicitação de Compra
```

Outro exemplo:

```text
CAP-COMPRAS-10
Gestão Contratual
       ↓
SERV-COMPRAS-006
Gestão de Contrato
```

---

# 32. Capacidade x Dados

Cada capacidade deverá consumir e produzir informações.

Exemplos:

### Planejamento

Consome:

* necessidades;
* histórico;
* orçamento;
* prioridades.

Produz:

* planejamento;
* previsões;
* prioridades.

### Gestão Contratual

Consome:

* processo;
* fornecedor;
* instrumento;
* valores.

Produz:

* situação contratual;
* ocorrências;
* prazos;
* informações de execução.

---

# 33. Capacidade x Documentos

As capacidades poderão produzir ou utilizar:

* requisições;
* especificações;
* pesquisas;
* propostas;
* pareceres;
* atos;
* contratos;
* aditivos;
* relatórios;
* registros de fiscalização;
* evidências;
* documentos de recebimento.

Cada documento deverá possuir vínculo contextual com o processo.

---

# 34. Capacidade x Indicadores

As capacidades constituirão uma das dimensões para avaliação de desempenho.

Exemplos:

```text
Planejamento
→ percentual de demandas planejadas

Requisição
→ tempo médio de processamento

Pesquisa de Preços
→ tempo médio de elaboração

Processo
→ tempo médio de instrução

Contratação
→ tempo médio do procedimento

Contrato
→ contratos próximos do vencimento

Fiscalização
→ ocorrências por contrato

Recebimento
→ percentual de não conformidades
```

---

# 35. Avaliação da Maturidade da Capacidade

Cada capacidade poderá futuramente ser avaliada segundo um modelo de maturidade.

Exemplo conceitual:

```text
Nível 0 – Inexistente
Nível 1 – Inicial
Nível 2 – Repetível
Nível 3 – Padronizada
Nível 4 – Gerenciada
Nível 5 – Otimizada
```

Essa avaliação deverá ser integrada ao modelo nacional de maturidade digital municipal quando aplicável.

---

# 36. Capacidade Atual x Capacidade Alvo

A arquitetura poderá utilizar dois estados:

```text
AS-IS
Capacidade atualmente existente.

TO-BE
Capacidade desejada.
```

Exemplo:

```text
AS-IS
Gestão Contratual parcialmente manual.

TO-BE
Gestão Contratual integrada, rastreável e orientada por indicadores.
```

---

# 37. Lacunas de Capacidade

A análise de lacunas deverá identificar situações como:

```text
Capacidade necessária
        ↓
Capacidade existente?
        ↓
      NÃO
        ↓
GAP DE CAPACIDADE
```

ou:

```text
Capacidade existente
        ↓
Nível insuficiente
        ↓
GAP DE MATURIDADE
```

---

# 38. Priorização

As capacidades deverão ser priorizadas considerando:

* criticidade;
* impacto;
* risco;
* frequência;
* volume;
* dependências;
* obrigação legal;
* impacto financeiro;
* impacto na prestação do serviço público;
* possibilidade de ganho de eficiência.

---

# 39. Capacidades Críticas

Inicialmente são consideradas críticas:

```text
CAP-COMPRAS-06 – Gestão do Processo

CAP-COMPRAS-08 – Gestão do Procedimento

CAP-COMPRAS-09 – Gestão da Formalização

CAP-COMPRAS-10 – Gestão Contratual

CAP-COMPRAS-12 – Fiscalização

CAP-COMPRAS-14 – Gestão Documental

CAP-COMPRAS-16 – Controle e Auditoria

CAP-COMPRAS-18 – Integração
```

Essa classificação deverá ser validada.

---

# 40. Capacidades Transversais

Algumas capacidades não pertencem a uma única etapa.

São transversais:

```text
Gestão Documental
Controle e Auditoria
Transparência
Integração
Informações e Indicadores
```

Essas capacidades deverão ser consideradas desde o início da arquitetura.

---

# 41. Capacidades e Arquitetura de Software

O mapa de capacidades não determina diretamente os módulos do software.

Entretanto, poderá fornecer insumos para sua definição.

Exemplo:

```text
Capacidades
      ↓
Agrupamentos funcionais
      ↓
Serviços
      ↓
Componentes
      ↓
Módulos
```

O desenho final deverá ser realizado pela arquitetura de software.

---

# 42. Capacidades e Arquitetura de Dados

O mapa de capacidades também servirá como entrada para identificar:

* informações principais;
* entidades;
* domínios de dados;
* proprietários;
* consumidores;
* fontes;
* integrações.

---

# 43. Capacidades e Governança

Cada capacidade deverá possuir, quando aplicável:

* responsável institucional;
* proprietário do processo;
* indicadores;
* políticas;
* controles;
* riscos;
* requisitos legais.

---

# 44. Capacidades e Riscos

A avaliação de riscos poderá ser relacionada às capacidades.

Exemplos:

```text
CAP-COMPRAS-05
Gestão de Preços

Riscos:
- estimativa inadequada;
- dados insuficientes;
- fonte não confiável;
- ausência de evidências.
```

Outro exemplo:

```text
CAP-COMPRAS-12
Fiscalização

Riscos:
- ausência de fiscalização;
- registro insuficiente;
- atraso;
- não conformidade não tratada.
```

---

# 45. Capacidades e Controles

Cada capacidade crítica deverá possuir controles proporcionais ao seu risco.

Exemplo:

```text
Capacidade
    ↓
Risco
    ↓
Controle
    ↓
Evidência
```

---

# 46. Capacidades e LGPD

A identificação das capacidades também deverá considerar informações pessoais tratadas.

Especial atenção deverá ser dada a:

* representantes;
* contatos;
* usuários;
* servidores;
* fornecedores;
* documentos pessoais.

O tratamento deverá respeitar as políticas corporativas de proteção de dados.

---

# 47. Capacidades e Mobilidade

Algumas capacidades poderão exigir execução em campo.

Exemplo:

```text
Fiscalização
      ↓
Aplicativo Móvel
      ↓
Registro de Evidência
      ↓
Sincronização
      ↓
Gestão Contratual
```

A necessidade deverá ser confirmada no levantamento dos processos.

---

# 48. Capacidades e Automação

O SIGMUN poderá utilizar automação para apoiar determinadas capacidades.

Exemplos:

* validações;
* alertas;
* notificações;
* cálculo de prazos;
* identificação de inconsistências;
* consolidação de informações;
* geração de indicadores;
* classificação documental;
* apoio analítico.

A automação deverá apoiar o processo, não substituir indevidamente decisões que dependam de competência humana.

---

# 49. Capacidades e Inteligência Artificial

Quando aplicável, recursos de IA poderão apoiar:

* análise documental;
* identificação de inconsistências;
* classificação;
* busca semântica;
* análise histórica;
* identificação de padrões;
* apoio à elaboração;
* geração de indicadores analíticos.

O uso de IA deverá observar governança, segurança, transparência e responsabilidade humana.

---

# 50. Mapa Visual Consolidado

```text
                    GESTÃO DE COMPRAS
                    E CONTRATAÇÕES
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
  PLANEJAMENTO         EXECUÇÃO            GOVERNANÇA
       │                   │                    │
       ├─ Necessidade      ├─ Contrato          ├─ Transparência
       ├─ Requisição       ├─ Execução          ├─ Auditoria
       ├─ Especificação    ├─ Fiscalização      └─ Indicadores
       └─ Preços           └─ Recebimento
       │
       ▼
  CONTRATAÇÃO
       │
       ├─ Processo
       ├─ Fornecedor
       ├─ Procedimento
       └─ Formalização

CAPACIDADES TRANSVERSAIS
       │
       ├─ Gestão Documental
       ├─ Integração
       ├─ Segurança
       └─ Rastreabilidade
```

---

# 51. Relação com o Mapa Mestre

Este documento deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`CAP-MAP-COMPRAS-001`

Relação principal:

```text
DOM-COMPRAS-001
       ↓
CAP-MAP-COMPRAS-001
       ↓
CAP-COMPRAS-001...018
       ↓
PROC-COMPRAS-001...012
       ↓
SERV-COMPRAS-001...010
       ↓
UC-COMPRAS-001...
       ↓
RF-COMPRAS-001...
```

---

# 52. Critérios de Conclusão

O Mapa de Capacidades será considerado suficientemente definido quando:

* as principais capacidades do domínio estiverem identificadas;
* as capacidades estiverem diferenciadas de processos;
* as capacidades estiverem relacionadas aos objetivos;
* os atores relevantes estiverem relacionados;
* os processos estiverem relacionados;
* os serviços estiverem relacionados;
* as capacidades críticas estiverem identificadas;
* as capacidades transversais estiverem identificadas;
* as lacunas conhecidas estiverem registradas;
* as relações de rastreabilidade estiverem estabelecidas.

---

# 53. Evolução

O mapa deverá evoluir quando:

* novos processos forem identificados;
* novas responsabilidades forem descobertas;
* novas necessidades forem levantadas;
* novos serviços forem definidos;
* mudanças legais alterarem capacidades;
* novas integrações forem necessárias;
* mudanças organizacionais ocorrerem;
* novas capacidades digitais forem incorporadas.

---

# 54. Disposição Final

O **Mapa de Capacidades – Gestão de Compras e Contratações** estabelece a visão de **o que o Município precisa ser capaz de realizar** para executar adequadamente suas compras e contratações.

Ele deverá servir como ponte entre o modelo de negócio e os demais níveis da arquitetura do SIGMUN.

A cadeia de referência será:

```text
Objetivos
   ↓
Capacidades
   ↓
Processos
   ↓
Serviços
   ↓
Casos de Uso
   ↓
Requisitos
   ↓
Solução
   ↓
Testes
   ↓
Evidências
```

Essa separação deverá ser preservada durante todo o desenvolvimento do domínio.

---

# Controle de Versões

| Versão | Data       | Descrição                                                                     |
| ------ | ---------- | ----------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do Mapa de Capacidades do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
