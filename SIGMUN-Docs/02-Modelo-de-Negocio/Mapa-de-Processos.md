# Mapa de Processos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Negócio

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `Cadeia-de-Valor.md`
* `Mapa-de-Atores.md`
* `Mapa-de-Capacidades.md`
* `Mapa-de-Dominios.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`
* `014-Processos.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md`

---

# 1. Finalidade

Este documento estabelece o **Mapa Corporativo de Processos do SIGMUN**, organizando os principais processos necessários para o funcionamento da administração municipal e para a entrega de valor público à sociedade.

O Mapa de Processos constitui uma visão corporativa dos processos municipais e servirá como referência para:

* arquitetura de negócio;
* modelagem de processos;
* identificação de capacidades;
* definição de serviços;
* levantamento de requisitos;
* definição de módulos;
* automação;
* indicadores;
* gestão de riscos;
* gestão documental;
* integração de sistemas;
* melhoria contínua.

---

# 2. Conceito de Processo

Para fins do SIGMUN, um **processo** é um conjunto estruturado de atividades relacionadas que transforma entradas em resultados para produzir determinado valor.

Um processo possui, no mínimo:

* objetivo;
* entrada;
* atividades;
* responsáveis;
* regras;
* informações;
* saída;
* resultado;
* indicadores.

---

# 3. Processo não é Departamento

Um processo não deverá ser definido exclusivamente com base na estrutura organizacional.

Um processo poderá:

* atravessar várias secretarias;
* envolver diferentes departamentos;
* envolver diferentes sistemas;
* envolver cidadãos;
* envolver fornecedores;
* envolver órgãos externos.

Portanto:

> **Processo representa como o trabalho acontece; organização representa quem está estruturado para executá-lo.**

---

# 4. Princípio Fundamental

O SIGMUN deverá adotar o princípio:

> **Processos antes de sistemas.**

A existência de um sistema ou módulo não deverá determinar como o processo municipal deve ser concebido.

O processo deverá ser definido a partir:

* do objetivo;
* da legislação;
* da necessidade;
* do valor público;
* dos atores;
* das regras de negócio.

A tecnologia deverá suportar o processo e não o contrário.

---

# 5. Relação entre os Elementos da Arquitetura

A relação conceitual adotada é:

```text id="w7q1cx"
Estratégia
   ↓
Valor Público
   ↓
Domínio
   ↓
Capacidade
   ↓
Processo
   ↓
Serviço
   ↓
Requisito
   ↓
Aplicação
   ↓
Dados
   ↓
Tecnologia
   ↓
Resultado
```

---

# 6. Classificação dos Processos

Os processos municipais serão classificados em:

1. **Processos Estratégicos;**
2. **Processos de Governança;**
3. **Processos de Gestão;**
4. **Processos Administrativos;**
5. **Processos Financeiros;**
6. **Processos de Pessoas;**
7. **Processos Patrimoniais;**
8. **Processos Territoriais;**
9. **Processos Finalísticos;**
10. **Processos de Atendimento;**
11. **Processos de Dados e Informação;**
12. **Processos Tecnológicos;**
13. **Processos de Controle.**

---

# 7. Processos Estratégicos

Os processos estratégicos são aqueles relacionados à direção e ao planejamento do município.

Incluem:

* Planejamento Estratégico;
* Planejamento Governamental;
* Gestão de Programas;
* Gestão de Projetos;
* Gestão de Portfólio;
* Gestão de Indicadores;
* Avaliação de Resultados;
* Gestão de Políticas Públicas.

---

# 8. Processo de Planejamento Estratégico

**Código:** `PRC-EST-001`

**Nome:** Planejamento Estratégico Municipal

### Objetivo

Definir direcionadores estratégicos para a administração municipal.

### Entradas

* diagnóstico municipal;
* dados socioeconômicos;
* demandas da população;
* legislação;
* prioridades políticas.

### Principais atividades

* análise de contexto;
* definição de objetivos;
* definição de metas;
* definição de indicadores;
* priorização de iniciativas.

### Saídas

* plano estratégico;
* objetivos;
* metas;
* indicadores;
* iniciativas.

---

# 9. Processo de Planejamento Governamental

**Código:** `PRC-EST-002`

Abrange:

* planejamento de programas;
* definição de ações;
* metas;
* orçamento;
* acompanhamento.

---

# 10. Processos de Governança

Incluem:

* Governança Corporativa;
* Governança Digital;
* Gestão de Riscos;
* Gestão de Compliance;
* Gestão de Políticas;
* Gestão de Decisões;
* Gestão de Auditoria.

---

# 11. Processo de Gestão de Riscos

**Código:** `PRC-GOV-001`

### Objetivo

Identificar, avaliar, tratar e monitorar riscos municipais.

### Entradas

* processos;
* projetos;
* incidentes;
* legislação;
* avaliações.

### Saídas

* registro de riscos;
* planos de tratamento;
* controles;
* indicadores.

---

# 12. Processos Administrativos

Incluem:

* Protocolo;
* Processos Administrativos;
* Gestão Documental;
* Comunicação Administrativa;
* Compras;
* Licitações;
* Contratações;
* Gestão de Contratos.

---

# 13. Processo de Protocolo

**Código:** `PRC-ADM-001`

### Objetivo

Registrar e controlar solicitações, documentos e processos administrativos.

### Principais atividades

* receber;
* registrar;
* classificar;
* encaminhar;
* tramitar;
* acompanhar;
* concluir;
* arquivar.

---

# 14. Processo de Gestão Documental

**Código:** `PRC-ADM-002`

Abrange:

* produção documental;
* classificação;
* armazenamento;
* versionamento;
* tramitação;
* assinatura;
* arquivamento;
* preservação;
* descarte.

---

# 15. Processo de Compras

**Código:** `PRC-ADM-003`

Abrange:

* identificação da necessidade;
* planejamento;
* solicitação;
* análise;
* autorização;
* contratação;
* recebimento.

---

# 16. Processo de Contratação

**Código:** `PRC-ADM-004`

Abrange:

* preparação;
* seleção;
* formalização;
* execução;
* fiscalização;
* encerramento.

---

# 17. Processos Financeiros

Incluem:

* Planejamento Orçamentário;
* Gestão de Receitas;
* Gestão de Despesas;
* Contabilidade;
* Tesouraria;
* Dívida Ativa;
* Tributação;
* Prestação de Contas.

---

# 18. Processo de Planejamento Orçamentário

**Código:** `PRC-FIN-001`

Abrange:

* elaboração;
* análise;
* aprovação;
* execução;
* revisão;
* acompanhamento.

---

# 19. Processo de Gestão da Receita

**Código:** `PRC-FIN-002`

Abrange:

* cadastro;
* lançamento;
* arrecadação;
* conciliação;
* cobrança;
* acompanhamento.

---

# 20. Processo de Gestão da Despesa

**Código:** `PRC-FIN-003`

Abrange:

* solicitação;
* empenho;
* liquidação;
* pagamento;
* contabilização;
* acompanhamento.

---

# 21. Processo Tributário

**Código:** `PRC-FIN-004`

Abrange:

* cadastro;
* lançamento;
* fiscalização;
* arrecadação;
* cobrança;
* dívida ativa.

---

# 22. Processos de Pessoas

Incluem:

* Recrutamento;
* Admissão;
* Gestão Funcional;
* Folha;
* Benefícios;
* Férias;
* Afastamentos;
* Avaliação;
* Capacitação;
* Desligamento.

---

# 23. Processo de Gestão Funcional

**Código:** `PRC-PES-001`

Abrange:

* cadastro;
* vínculo;
* lotação;
* movimentação;
* jornada;
* afastamentos;
* desligamento.

---

# 24. Processo de Folha de Pagamento

**Código:** `PRC-PES-002`

Abrange:

* preparação;
* cálculo;
* conferência;
* aprovação;
* fechamento;
* pagamento;
* obrigações.

---

# 25. Processos Patrimoniais

Incluem:

* Aquisição de Bens;
* Registro Patrimonial;
* Movimentação;
* Inventário;
* Depreciação;
* Manutenção;
* Baixa;
* Gestão de Estoques;
* Gestão de Frota.

---

# 26. Processo de Gestão Patrimonial

**Código:** `PRC-PAT-001`

Abrange:

* aquisição;
* registro;
* identificação;
* movimentação;
* inventário;
* manutenção;
* baixa.

---

# 27. Processo de Gestão de Frota

**Código:** `PRC-PAT-002`

Abrange:

* cadastro;
* alocação;
* utilização;
* abastecimento;
* manutenção;
* controle de custos;
* encerramento.

---

# 28. Processos Territoriais

Incluem:

* Cadastro Territorial;
* Cadastro Imobiliário;
* Geoprocessamento;
* Licenciamento;
* Fiscalização;
* Obras;
* Manutenção Urbana;
* Gestão de Resíduos.

---

# 29. Processo de Cadastro Imobiliário

**Código:** `PRC-TER-001`

Abrange:

* cadastro;
* atualização;
* identificação;
* avaliação;
* vinculação;
* fiscalização;
* histórico.

---

# 30. Processo de Gestão de Obras

**Código:** `PRC-TER-002`

Abrange:

* planejamento;
* projeto;
* contratação;
* execução;
* fiscalização;
* medição;
* pagamento;
* encerramento.

---

# 31. Processos Finalísticos

Os processos finalísticos são aqueles diretamente relacionados à prestação de políticas e serviços públicos.

Incluem:

* Saúde;
* Educação;
* Assistência Social;
* Cultura;
* Esporte;
* Turismo;
* Meio Ambiente;
* Agricultura;
* Desenvolvimento Econômico;
* Habitação;
* Mobilidade;
* Defesa Civil.

---

# 32. Processos de Saúde

Incluem:

* Atendimento em Saúde;
* Atenção Básica;
* Regulação;
* Vacinação;
* Farmácia;
* Vigilância;
* Gestão de Unidades;
* Gestão de Profissionais.

---

# 33. Processo de Atendimento em Saúde

**Código:** `PRC-SAU-001`

Fluxo conceitual:

```text id="c0j0s7"
Agendamento
   ↓
Recepção
   ↓
Atendimento
   ↓
Registro
   ↓
Conduta
   ↓
Encaminhamento
   ↓
Acompanhamento
```

---

# 34. Processos de Educação

Incluem:

* Matrícula;
* Gestão Escolar;
* Gestão de Turmas;
* Frequência;
* Avaliação;
* Transporte Escolar;
* Alimentação Escolar;
* Gestão de Profissionais.

---

# 35. Processo de Matrícula

**Código:** `PRC-EDU-001`

Abrange:

* solicitação;
* análise;
* alocação;
* confirmação;
* registro;
* acompanhamento.

---

# 36. Processos de Assistência Social

Incluem:

* Cadastro Social;
* Atendimento;
* Benefícios;
* Acompanhamento Familiar;
* Programas;
* Encaminhamentos.

---

# 37. Processo de Atendimento Socioassistencial

**Código:** `PRC-ASS-001`

Abrange:

* identificação;
* atendimento;
* avaliação;
* encaminhamento;
* acompanhamento;
* encerramento.

---

# 38. Processos de Meio Ambiente

Incluem:

* Licenciamento;
* Fiscalização;
* Monitoramento;
* Gestão de Resíduos;
* Educação Ambiental.

---

# 39. Processos de Desenvolvimento Econômico

Incluem:

* Atendimento Empresarial;
* Licenciamento Econômico;
* Apoio ao Empreendedor;
* Programas de Desenvolvimento;
* Gestão de Incentivos.

---

# 40. Processos de Atendimento ao Cidadão

Incluem:

* Atendimento;
* Solicitação de Serviços;
* Protocolo;
* Agendamento;
* Ouvidoria;
* Reclamações;
* Denúncias;
* Sugestões;
* Acompanhamento.

---

# 41. Processo de Solicitação de Serviço

**Código:** `PRC-ATE-001`

Fluxo conceitual:

```text id="fjw9zq"
Cidadão
   ↓
Solicitação
   ↓
Classificação
   ↓
Triagem
   ↓
Encaminhamento
   ↓
Execução
   ↓
Validação
   ↓
Resposta
   ↓
Encerramento
```

---

# 42. Processo de Ouvidoria

**Código:** `PRC-ATE-002`

Abrange:

* recebimento;
* classificação;
* análise;
* encaminhamento;
* resposta;
* acompanhamento;
* encerramento;
* geração de indicadores.

---

# 43. Processos de Dados e Informação

Incluem:

* Gestão de Dados;
* Gestão de Metadados;
* Qualidade de Dados;
* Integração de Dados;
* Produção de Indicadores;
* BI;
* Analytics;
* IA.

---

# 44. Processo de Gestão de Dados

**Código:** `PRC-DAD-001`

Abrange:

* criação;
* captura;
* validação;
* armazenamento;
* utilização;
* compartilhamento;
* arquivamento;
* descarte.

---

# 45. Processo de Gestão de Metadados

**Código:** `PRC-DAD-002`

Abrange:

* identificação;
* definição;
* classificação;
* registro;
* atualização;
* governança.

---

# 46. Processo de Qualidade de Dados

**Código:** `PRC-DAD-003`

Avalia:

* completude;
* consistência;
* precisão;
* atualidade;
* unicidade;
* validade.

---

# 47. Processo de Gestão de Indicadores

**Código:** `PRC-DAD-004`

Abrange:

* definição;
* cálculo;
* validação;
* publicação;
* acompanhamento;
* análise.

---

# 48. Processos Tecnológicos

Incluem:

* Gestão de Identidade;
* Gestão de Acessos;
* Desenvolvimento;
* Gestão de Aplicações;
* Integração;
* Infraestrutura;
* Segurança;
* Backup;
* Continuidade;
* Monitoramento;
* Gestão de Incidentes.

---

# 49. Processo de Gestão de Identidade

**Código:** `PRC-TEC-001`

Abrange:

* criação;
* autenticação;
* autorização;
* alteração;
* bloqueio;
* encerramento.

---

# 50. Processo de Gestão de Incidentes

**Código:** `PRC-TEC-002`

Abrange:

* identificação;
* registro;
* classificação;
* priorização;
* tratamento;
* resolução;
* encerramento;
* análise posterior.

---

# 51. Processo de Desenvolvimento de Software

**Código:** `PRC-TEC-003`

Abrange:

* levantamento;
* análise;
* arquitetura;
* desenvolvimento;
* testes;
* implantação;
* monitoramento;
* evolução.

---

# 52. Processos de Controle

Incluem:

* Auditoria;
* Controle Interno;
* Fiscalização;
* Compliance;
* Transparência;
* Prestação de Contas.

---

# 53. Processo de Auditoria

**Código:** `PRC-CON-001`

Abrange:

* planejamento;
* execução;
* coleta de evidências;
* análise;
* relatório;
* recomendações;
* acompanhamento.

---

# 54. Processo de Transparência

**Código:** `PRC-CON-002`

Abrange:

* identificação da informação;
* classificação;
* validação;
* publicação;
* atualização;
* controle.

Deverá observar a política corporativa de publicação.

---

# 55. Hierarquia de Processos

Os processos deverão ser organizados em níveis.

```text id="wqzqis"
Nível 0
Cadeia de Valor

Nível 1
Macroprocesso

Nível 2
Processo

Nível 3
Subprocesso

Nível 4
Atividade

Nível 5
Tarefa
```

---

# 56. Macroprocessos

Um macroprocesso representa um conjunto de processos relacionados que contribuem para um objetivo comum.

Exemplo:

```text id="w1rygz"
Macroprocesso:
Gestão Financeira

├── Planejamento Orçamentário
├── Gestão da Receita
├── Gestão da Despesa
├── Tesouraria
└── Contabilidade
```

---

# 57. Subprocessos

Os subprocessos representam partes especializadas de um processo.

Exemplo:

```text id="qg6rkg"
Processo:
Gestão da Despesa

├── Solicitação
├── Empenho
├── Liquidação
├── Pagamento
└── Prestação de Contas
```

---

# 58. Atividades

Atividades representam conjuntos de tarefas executadas para produzir determinado resultado.

Exemplo:

```text id="7n5s1u"
Liquidação

├── Conferir documento
├── Conferir entrega
├── Validar valores
├── Registrar liquidação
└── Autorizar pagamento
```

---

# 59. Tarefas

Tarefas representam unidades operacionais específicas de execução.

As tarefas deverão ser detalhadas nos modelos de processos quando houver necessidade de automação ou controle operacional.

---

# 60. Processos Transversais

Alguns processos atravessam diversos domínios.

Exemplos:

* Gestão de Pessoas;
* Gestão Documental;
* Gestão de Dados;
* Segurança;
* Atendimento;
* Gestão de Riscos;
* Gestão de Indicadores.

Esses processos deverão possuir governança corporativa.

---

# 61. Processos Compartilhados

Um processo poderá ser executado por múltiplas unidades.

Exemplo:

```text id="c8e7h2"
Processo:
Contratação

Planejamento
     ↓
Secretaria demandante
     ↓
Compras
     ↓
Jurídico
     ↓
Licitação
     ↓
Contratos
     ↓
Fiscalização
```

O processo deverá ser modelado de ponta a ponta.

---

# 62. Processos de Ponta a Ponta

O SIGMUN deverá priorizar a visão **end-to-end**.

Exemplo:

```text id="5b5vop"
Necessidade do cidadão
        ↓
Solicitação
        ↓
Triagem
        ↓
Execução
        ↓
Fiscalização
        ↓
Resposta
        ↓
Indicador
        ↓
Melhoria
```

---

# 63. Processos Críticos

São processos cuja interrupção pode provocar:

* interrupção de serviços essenciais;
* impacto financeiro;
* risco à população;
* risco jurídico;
* perda de informações;
* comprometimento institucional.

Processos críticos deverão possuir:

* plano de continuidade;
* responsáveis;
* indicadores;
* controles;
* riscos identificados.

---

# 64. Avaliação de Maturidade dos Processos

Os processos poderão ser classificados em:

| Nível | Classificação | Característica                           |
| ----- | ------------- | ---------------------------------------- |
| 1     | Inicial       | Processo informal                        |
| 2     | Repetível     | Processo parcialmente definido           |
| 3     | Gerenciado    | Processo documentado e controlado        |
| 4     | Integrado     | Processo integrado e orientado por dados |
| 5     | Otimizado     | Processo continuamente melhorado         |

---

# 65. Avaliação de Processos

A avaliação deverá considerar:

* documentação;
* padronização;
* automação;
* integração;
* indicadores;
* qualidade;
* riscos;
* experiência do usuário;
* tempo de execução;
* custo;
* resultados.

---

# 66. Indicadores de Processos

Cada processo relevante deverá possuir indicadores apropriados.

Exemplos:

* tempo de ciclo;
* volume;
* custo;
* taxa de erro;
* retrabalho;
* cumprimento de prazo;
* produtividade;
* satisfação;
* taxa de automação;
* taxa de resolução.

---

# 67. Processos e Requisitos

Todo requisito deverá possuir rastreabilidade, quando aplicável, até o processo que origina a necessidade.

```text id="x1b7tq"
Objetivo
   ↓
Domínio
   ↓
Capacidade
   ↓
Processo
   ↓
Necessidade
   ↓
Requisito
```

---

# 68. Processos e Aplicações

Um processo poderá ser suportado por:

* uma aplicação;
* vários módulos;
* vários serviços;
* sistemas externos;
* atividades manuais.

O SIGMUN deverá buscar reduzir atividades manuais desnecessárias, mas não deverá automatizar processos sem antes avaliar sua necessidade e qualidade.

---

# 69. Processos e Dados

Cada processo deverá identificar:

* dados de entrada;
* dados utilizados;
* dados produzidos;
* dados alterados;
* dados compartilhados;
* dados arquivados.

---

# 70. Processos e Documentos

Quando aplicável, cada processo deverá identificar:

* documentos de entrada;
* documentos produzidos;
* evidências;
* registros;
* assinaturas;
* retenção;
* descarte.

---

# 71. Processos e Riscos

Cada processo crítico deverá possuir avaliação de riscos.

```text id="4x7l2c"
Processo
   ↓
Riscos
   ↓
Controles
   ↓
Indicadores
   ↓
Monitoramento
```

---

# 72. Processos e Controles

Os controles poderão ser:

* preventivos;
* detectivos;
* corretivos;
* automatizados;
* manuais.

O SIGMUN deverá priorizar controles automatizados quando isso reduzir riscos sem criar complexidade desnecessária.

---

# 73. Processos e Experiência do Usuário

Processos que envolvam cidadãos deverão considerar:

* simplicidade;
* acessibilidade;
* transparência;
* tempo de resposta;
* comunicação;
* acompanhamento;
* canais digitais;
* canais presenciais.

---

# 74. Processos Digitais

Sempre que possível, os processos deverão permitir execução digital.

Exemplos:

* assinatura eletrônica;
* notificações;
* formulários digitais;
* workflow;
* integração;
* pagamentos digitais;
* acompanhamento online.

---

# 75. Processos Offline e de Campo

Processos executados em áreas com conectividade limitada deverão considerar arquitetura **Offline First**, quando aplicável.

O processo deverá prever:

* captura local;
* armazenamento temporário;
* evidências;
* sincronização;
* resolução de conflitos;
* auditoria.

---

# 76. Processos e Automação

A automação deverá ser considerada quando houver:

* alto volume;
* repetitividade;
* regras claras;
* necessidade de velocidade;
* necessidade de controle;
* redução de erros.

Não deverá ser automatizado um processo simplesmente porque é possível fazê-lo.

---

# 77. Processos e Inteligência Artificial

A IA poderá ser utilizada em processos para:

* classificação;
* previsão;
* recomendação;
* detecção de anomalias;
* análise documental;
* apoio à decisão.

Quando utilizada, deverá observar:

* transparência;
* segurança;
* governança;
* supervisão humana;
* proteção de dados;
* auditabilidade.

---

# 78. Modelo de Registro de Processo

Cada processo deverá possuir uma ficha padronizada.

```markdown id="e1k7z3"
## PRC-XXX – Nome do Processo

**Código:** PRC-XXX

**Nome:** Nome do processo

**Categoria:** Estratégico / Governança / Gestão / Administrativo / Finalístico / Tecnológico / Controle

**Domínio:** Domínio relacionado.

**Capacidade:** Capacidade suportada.

**Objetivo:** Objetivo do processo.

**Dono do processo:** Responsável institucional.

**Atores:** Principais envolvidos.

**Entradas:** Principais entradas.

**Saídas:** Principais saídas.

**Serviços:** Serviços relacionados.

**Dados:** Dados utilizados.

**Documentos:** Documentos relacionados.

**Regras de negócio:** Regras aplicáveis.

**Riscos:** Principais riscos.

**Controles:** Controles existentes.

**Indicadores:** Indicadores.

**Aplicações:** Sistemas e módulos.

**Integrações:** Integrações.

**Maturidade atual:** Nível 1–5.

**Maturidade desejada:** Nível 1–5.

**Criticidade:** Baixa / Média / Alta / Crítica.

**Prioridade:** Baixa / Média / Alta / Muito Alta.

**Observações:** Informações adicionais.
```

---

# 79. Modelagem dos Processos

Quando necessário, os processos deverão ser modelados utilizando notação adequada, preferencialmente **BPMN**, respeitando o padrão corporativo de documentação do SIGMUN.

A modelagem deverá permitir representar:

* eventos;
* atividades;
* decisões;
* participantes;
* fluxos;
* mensagens;
* exceções;
* subprocessos.

---

# 80. Governança dos Processos

Cada processo relevante deverá possuir:

* dono do processo;
* responsável operacional;
* participantes;
* indicadores;
* regras;
* documentação;
* periodicidade de revisão.

---

# 81. Ciclo de Vida dos Processos

Os processos poderão assumir os estados:

```text id="8afw1x"
Identificado
    ↓
Em Análise
    ↓
Modelado
    ↓
Aprovado
    ↓
Implementado
    ↓
Monitorado
    ↓
Em Melhoria
    ↓
Redesenhado
    ↓
Descontinuado
```

---

# 82. Melhoria Contínua

O SIGMUN deverá promover melhoria contínua dos processos.

A melhoria poderá ocorrer por:

* simplificação;
* eliminação de etapas;
* automação;
* integração;
* padronização;
* redução de retrabalho;
* redução de custos;
* melhoria da experiência;
* melhoria dos resultados.

---

# 83. Priorização de Processos

A priorização deverá considerar:

| Critério                | Avaliação |
| ----------------------- | --------- |
| Impacto público         | 1–5       |
| Criticidade             | 1–5       |
| Volume                  | 1–5       |
| Custo                   | 1–5       |
| Retrabalho              | 1–5       |
| Risco                   | 1–5       |
| Potencial de automação  | 1–5       |
| Potencial de integração | 1–5       |

---

# 84. Catálogo Corporativo de Processos

O SIGMUN deverá manter um catálogo corporativo contendo:

* código;
* nome;
* domínio;
* capacidade;
* proprietário;
* descrição;
* maturidade;
* criticidade;
* indicadores;
* sistemas;
* versão;
* status.

---

# 85. Relacionamento com o Catálogo Corporativo do Conhecimento

Cada processo deverá estar relacionado aos elementos existentes no:

`04-Conhecimento-Corporativo/000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`

Isso permitirá relacionar:

```text id="z2a9x8"
Processo
 ↓
Conceitos
 ↓
Termos
 ↓
Dados
 ↓
Documentos
 ↓
Regras
 ↓
Indicadores
 ↓
Conhecimento
```

---

# 86. Governança de Mudanças

Alterações relevantes em processos deverão avaliar impactos sobre:

* pessoas;
* legislação;
* sistemas;
* dados;
* documentos;
* indicadores;
* integrações;
* segurança;
* treinamento.

Mudanças relevantes deverão possuir registro e rastreabilidade.

---

# 87. Princípio da Rastreabilidade

Todo processo relevante deverá permitir rastrear:

```text id="k2x8wb"
Estratégia
 ↓
Objetivo
 ↓
Domínio
 ↓
Capacidade
 ↓
Processo
 ↓
Serviço
 ↓
Requisito
 ↓
Implementação
 ↓
Resultado
```

---

# 88. Princípio da Transparência

Os processos que produzam informações públicas deverão considerar a publicação dos resultados e indicadores, respeitando:

* legislação;
* classificação da informação;
* proteção de dados;
* segurança.

Aplicando:

> **Transparência por padrão.**

---

# 89. Princípio da Segurança

A segurança deverá ser considerada desde a modelagem do processo.

Aplicando:

> **Segurança por princípio.**

---

# 90. Princípio da Classificação da Informação

A informação produzida, utilizada ou compartilhada pelos processos deverá ser classificada conforme política corporativa.

Aplicando:

> **Classificação da Informação por política.**

---

# 91. Princípio de Abertura

O SIGMUN deverá adotar:

> **Aberto sempre que possível, restrito sempre que necessário.**

---

# 92. Disposições Finais

O **Mapa de Processos do SIGMUN** constitui referência corporativa para organizar e compreender como a administração municipal transforma recursos, informações e necessidades em serviços e resultados para a sociedade.

O mapa deverá ser utilizado como fundamento para:

* arquitetura de negócio;
* arquitetura de aplicações;
* arquitetura de dados;
* levantamento de requisitos;
* automação;
* indicadores;
* gestão de riscos;
* melhoria contínua;
* transformação digital.

A relação fundamental permanece:

```text id="gq9d8m"
Valor Público
    ↓
Domínios
    ↓
Capacidades
    ↓
Processos
    ↓
Serviços
    ↓
Requisitos
    ↓
Aplicações
    ↓
Dados
    ↓
Tecnologia
    ↓
Resultados
```

O documento deverá ser utilizado conjuntamente com:

* `Cadeia-de-Valor.md`;
* `Mapa-de-Atores.md`;
* `Mapa-de-Capacidades.md`;
* `Mapa-de-Dominios.md`;
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`;
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`;
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md`;
* `014-Processos.md`.

---

# 93. Princípios Arquiteturais Relacionados

O Mapa de Processos deverá observar os princípios fundamentais do SIGMUN:

> **Transparência por padrão.**

> **Segurança por princípio.**

> **Classificação da Informação por política.**

> **Aberto sempre que possível, restrito sempre que necessário.**

> **Tecnologia como meio. Pessoas, processos, conhecimento, capacidades e valor público como finalidade.**

---

**Documento:** `Mapa-de-Processos.md`

**Última atualização:** `2026-08-11`

**Responsável:** `Equipe SIGMUN`

**Status da revisão:** `Vigente`
