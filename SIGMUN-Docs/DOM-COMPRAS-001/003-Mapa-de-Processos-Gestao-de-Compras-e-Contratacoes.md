# 003 – Mapa de Processos – Gestão de Compras e Contratações

#### Mapa de Processos – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
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

O **Mapa de Processos – Gestão de Compras e Contratações** identifica, organiza e estrutura os principais processos necessários para executar as capacidades do domínio.

O documento estabelece uma visão corporativa dos processos, sem detalhar ainda:

* tarefas;
* procedimentos operacionais;
* telas;
* regras específicas;
* requisitos funcionais;
* implementação tecnológica.

Esses elementos serão detalhados nos artefatos posteriores.

---

# 2. Conceito de Processo

Para o SIGMUN, processo é um conjunto organizado de atividades que transforma entradas em resultados para produzir determinado valor institucional.

A estrutura básica é:

```text
Entrada
   ↓
Processo
   ↓
Atividades
   ↓
Resultado
   ↓
Beneficiário
```

---

# 3. Princípio de Modelagem

Os processos deverão ser modelados independentemente da tecnologia.

O processo deverá existir conceitualmente mesmo que:

* seja executado manualmente;
* utilize documentos físicos;
* utilize sistemas diferentes;
* seja parcialmente automatizado;
* seja integralmente automatizado.

O SIGMUN deverá posteriormente fornecer suporte aos processos.

---

# 4. Arquitetura Geral dos Processos

O domínio será organizado em seis macroprocessos:

```text
GESTÃO DE COMPRAS E CONTRATAÇÕES
│
├── MP-01 – Planejamento
│
├── MP-02 – Preparação da Contratação
│
├── MP-03 – Seleção e Contratação
│
├── MP-04 – Gestão e Execução Contratual
│
├── MP-05 – Encerramento
│
└── MP-06 – Governança, Controle e Transparência
```

---

# 5. Visão da Cadeia Principal

A cadeia principal do domínio será:

```text
Planejar
   ↓
Identificar Necessidade
   ↓
Formalizar Requisição
   ↓
Especificar Objeto
   ↓
Estimar Preço
   ↓
Instruir Processo
   ↓
Realizar Contratação
   ↓
Formalizar Instrumento
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

Processos transversais apoiam todas as etapas:

```text
Gestão Documental
Controle
Auditoria
Transparência
Indicadores
Integrações
```

---

# 6. Macroprocesso MP-01 – Planejamento

**Objetivo:**

Organizar e antecipar as necessidades de compras e contratações do Município.

**Processos:**

```text
PROC-COMPRAS-001 – Planejamento de Contratações
PROC-COMPRAS-002 – Consolidação de Necessidades
PROC-COMPRAS-003 – Priorização de Contratações
```

---

# 7. PROC-COMPRAS-001 – Planejamento de Contratações

**Objetivo:**

Planejar as contratações necessárias para atender às demandas administrativas.

**Entradas:**

* necessidades previstas;
* histórico;
* planejamento institucional;
* informações orçamentárias;
* contratos vigentes;
* demandas das unidades.

**Principais atividades:**

1. identificar necessidades;
2. consolidar demandas;
3. analisar períodos;
4. verificar dependências;
5. avaliar prioridades;
6. registrar planejamento;
7. acompanhar execução.

**Saídas:**

* planejamento de contratações;
* calendário;
* prioridades;
* necessidades consolidadas.

**Atores principais:**

* Unidade Requisitante;
* Gestor da Unidade;
* Unidade de Compras.

**Capacidade relacionada:**

`CAP-COMPRAS-01 – Planejamento`

---

# 8. PROC-COMPRAS-002 – Consolidação de Necessidades

**Objetivo:**

Consolidar necessidades semelhantes ou relacionadas das unidades administrativas.

**Entradas:**

* necessidades;
* requisições;
* planejamento das unidades.

**Atividades:**

* identificar demandas semelhantes;
* agrupar necessidades;
* analisar quantidades;
* identificar oportunidades de contratação conjunta;
* encaminhar para avaliação.

**Saídas:**

* demandas consolidadas;
* agrupamentos;
* oportunidades identificadas.

**Capacidades:**

* `CAP-COMPRAS-01`
* `CAP-COMPRAS-02`
* `CAP-COMPRAS-03`

---

# 9. PROC-COMPRAS-003 – Priorização de Contratações

**Objetivo:**

Estabelecer a prioridade das contratações considerando critérios institucionais.

**Critérios potenciais:**

* urgência;
* criticidade;
* continuidade do serviço público;
* impacto financeiro;
* risco;
* planejamento;
* obrigação legal;
* disponibilidade de recursos.

**Saída:**

Lista priorizada de contratações.

---

# 10. Macroprocesso MP-02 – Preparação da Contratação

**Objetivo:**

Transformar uma necessidade administrativa em processo adequadamente estruturado para contratação.

**Processos:**

```text
PROC-COMPRAS-004 – Registro da Necessidade
PROC-COMPRAS-005 – Gestão da Requisição
PROC-COMPRAS-006 – Especificação do Objeto
PROC-COMPRAS-007 – Pesquisa e Estimativa de Preços
PROC-COMPRAS-008 – Instrução do Processo
```

---

# 11. PROC-COMPRAS-004 – Registro da Necessidade

**Objetivo:**

Registrar formalmente a necessidade de aquisição ou contratação.

**Entradas:**

* necessidade identificada;
* justificativa;
* unidade demandante.

**Atividades:**

1. registrar necessidade;
2. descrever problema ou demanda;
3. justificar;
4. informar prioridade;
5. encaminhar para análise.

**Saída:**

Necessidade registrada.

**Capacidade:**

`CAP-COMPRAS-02`

---

# 12. PROC-COMPRAS-005 – Gestão da Requisição

**Objetivo:**

Formalizar e validar a solicitação de compra ou contratação.

**Atividades:**

* criar requisição;
* informar objeto;
* informar quantidade;
* anexar documentação;
* encaminhar;
* validar;
* devolver;
* aprovar;
* cancelar.

**Atores:**

* Servidor Solicitante;
* Gestor da Unidade;
* Unidade de Compras.

**Capacidade:**

`CAP-COMPRAS-03`

---

# 13. PROC-COMPRAS-006 – Especificação do Objeto

**Objetivo:**

Definir claramente o objeto pretendido.

**Atividades:**

* elaborar descrição;
* definir características;
* definir quantidade;
* definir unidade;
* estabelecer requisitos;
* revisar especificação;
* validar.

**Saída:**

Objeto adequadamente especificado.

**Capacidade:**

`CAP-COMPRAS-04`

---

# 14. PROC-COMPRAS-007 – Pesquisa e Estimativa de Preços

**Objetivo:**

Estabelecer referência de preço para o objeto.

**Atividades potenciais:**

* identificar fontes;
* coletar informações;
* registrar evidências;
* comparar valores;
* analisar dados;
* estabelecer estimativa;
* documentar metodologia.

**Saída:**

Estimativa de preço documentada.

**Capacidade:**

`CAP-COMPRAS-05`

---

# 15. PROC-COMPRAS-008 – Instrução do Processo

**Objetivo:**

Organizar a documentação e as informações necessárias para prosseguimento do processo.

**Atividades:**

* verificar documentação;
* organizar processo;
* validar informações;
* registrar pendências;
* encaminhar análises;
* acompanhar manifestações.

**Atores:**

* Unidade de Compras;
* Jurídico;
* Financeiro;
* Contábil;
* Unidade Requisitante.

**Capacidade:**

`CAP-COMPRAS-06`

---

# 16. Macroprocesso MP-03 – Seleção e Contratação

**Objetivo:**

Conduzir o procedimento de contratação até sua formalização.

**Processos:**

```text
PROC-COMPRAS-009 – Preparação do Procedimento
PROC-COMPRAS-010 – Condução do Procedimento
PROC-COMPRAS-011 – Análise e Julgamento
PROC-COMPRAS-012 – Decisão
PROC-COMPRAS-013 – Formalização da Contratação
```

---

# 17. PROC-COMPRAS-009 – Preparação do Procedimento

**Objetivo:**

Preparar o procedimento de contratação aplicável.

**Atividades:**

* definir procedimento;
* preparar documentação;
* estabelecer cronograma;
* registrar participantes;
* publicar quando aplicável;
* preparar instrumentos.

**Capacidades:**

* `CAP-COMPRAS-06`
* `CAP-COMPRAS-08`

---

# 18. PROC-COMPRAS-010 – Condução do Procedimento

**Objetivo:**

Executar e registrar as etapas do procedimento de contratação.

**Atividades:**

* receber propostas;
* registrar participantes;
* registrar atos;
* analisar documentação;
* registrar ocorrências;
* controlar prazos;
* encaminhar resultados.

**Atores:**

* Agente do Procedimento;
* Equipe de Apoio;
* Fornecedor;
* Representante do Fornecedor.

---

# 19. PROC-COMPRAS-011 – Análise e Julgamento

**Objetivo:**

Analisar propostas e documentos conforme critérios estabelecidos.

**Atividades:**

* analisar documentação;
* analisar propostas;
* aplicar critérios;
* registrar resultados;
* solicitar esclarecimentos quando aplicável;
* registrar decisão técnica.

---

# 20. PROC-COMPRAS-012 – Decisão

**Objetivo:**

Submeter o resultado à autoridade competente quando necessário.

**Atividades:**

* analisar resultado;
* verificar documentação;
* decidir;
* aprovar;
* homologar quando aplicável;
* determinar providências.

**Ator principal:**

`ACT-COMPRAS-007 – Autoridade Competente`

---

# 21. PROC-COMPRAS-013 – Formalização da Contratação

**Objetivo:**

Formalizar o resultado do procedimento.

**Atividades:**

* preparar instrumento;
* validar;
* coletar assinaturas;
* registrar;
* publicar quando aplicável;
* vincular ao processo.

**Saída:**

Instrumento formal de contratação.

**Capacidade:**

`CAP-COMPRAS-09`

---

# 22. Macroprocesso MP-04 – Gestão e Execução Contratual

**Objetivo:**

Administrar a execução dos instrumentos contratados.

**Processos:**

```text
PROC-COMPRAS-014 – Cadastro e Gestão do Contrato
PROC-COMPRAS-015 – Gestão de Obrigações
PROC-COMPRAS-016 – Fiscalização Contratual
PROC-COMPRAS-017 – Gestão de Ocorrências
PROC-COMPRAS-018 – Gestão de Alterações
PROC-COMPRAS-019 – Gestão do Recebimento
```

---

# 23. PROC-COMPRAS-014 – Cadastro e Gestão do Contrato

**Objetivo:**

Registrar e acompanhar as informações essenciais do contrato.

**Informações:**

* fornecedor;
* objeto;
* valor;
* vigência;
* responsáveis;
* obrigações;
* documentos;
* situação.

**Capacidade:**

`CAP-COMPRAS-10`

---

# 24. PROC-COMPRAS-015 – Gestão de Obrigações

**Objetivo:**

Acompanhar as obrigações das partes.

**Atividades:**

* registrar obrigações;
* estabelecer prazos;
* acompanhar cumprimento;
* registrar evidências;
* gerar alertas;
* registrar pendências.

---

# 25. PROC-COMPRAS-016 – Fiscalização Contratual

**Objetivo:**

Verificar a execução do objeto contratado.

**Atividades:**

* realizar fiscalização;
* registrar evidências;
* registrar ocorrências;
* registrar não conformidades;
* emitir registros;
* acompanhar correções.

**Atores:**

* Fiscal do Contrato;
* Gestor do Contrato;
* Fornecedor.

**Capacidade:**

`CAP-COMPRAS-12`

---

# 26. PROC-COMPRAS-017 – Gestão de Ocorrências

**Objetivo:**

Registrar e acompanhar situações que afetem a execução contratual.

**Exemplos:**

* atraso;
* não conformidade;
* falha;
* descumprimento;
* ocorrência operacional;
* necessidade de providência.

**Saída:**

Ocorrência registrada e encaminhada.

---

# 27. PROC-COMPRAS-018 – Gestão de Alterações

**Objetivo:**

Controlar alterações nos instrumentos contratuais.

**Inclui:**

* aditivos;
* alterações;
* prorrogações;
* reajustes;
* revisões;
* alterações de responsáveis;
* outros instrumentos aplicáveis.

**Observação:**

As modalidades específicas deverão respeitar as normas aplicáveis.

---

# 28. PROC-COMPRAS-019 – Gestão do Recebimento

**Objetivo:**

Registrar a entrega ou execução e verificar sua conformidade.

**Atividades:**

* registrar entrega;
* conferir;
* validar;
* aceitar;
* rejeitar;
* registrar divergências;
* anexar evidências.

**Capacidade:**

`CAP-COMPRAS-13`

---

# 29. Macroprocesso MP-05 – Encerramento

**Objetivo:**

Concluir formalmente o ciclo da contratação.

**Processos:**

```text
PROC-COMPRAS-020 – Encerramento da Execução
PROC-COMPRAS-021 – Encerramento Contratual
PROC-COMPRAS-022 – Arquivamento
```

---

# 30. PROC-COMPRAS-020 – Encerramento da Execução

**Objetivo:**

Verificar o encerramento das obrigações relacionadas à execução.

**Atividades:**

* verificar entregas;
* verificar pendências;
* registrar conclusão;
* consolidar evidências;
* encaminhar encerramento.

---

# 31. PROC-COMPRAS-021 – Encerramento Contratual

**Objetivo:**

Formalizar o encerramento do contrato ou instrumento.

**Atividades:**

* verificar situação;
* verificar obrigações;
* registrar encerramento;
* consolidar informações;
* atualizar situação.

---

# 32. PROC-COMPRAS-022 – Arquivamento

**Objetivo:**

Preservar o processo e seus documentos após o encerramento.

**Atividades:**

* verificar integridade;
* classificar;
* arquivar;
* aplicar retenção;
* controlar acesso;
* manter rastreabilidade.

**Capacidade:**

`CAP-COMPRAS-14`

---

# 33. Macroprocesso MP-06 – Governança, Controle e Transparência

**Objetivo:**

Garantir controle, auditoria, transparência e utilização gerencial das informações.

**Processos:**

```text
PROC-COMPRAS-023 – Controle Interno
PROC-COMPRAS-024 – Auditoria
PROC-COMPRAS-025 – Transparência
PROC-COMPRAS-026 – Gestão de Indicadores
PROC-COMPRAS-027 – Gestão de Informações
```

---

# 34. PROC-COMPRAS-023 – Controle Interno

**Objetivo:**

Executar atividades de controle sobre os processos de compras e contratações.

**Atividades:**

* verificar processos;
* identificar riscos;
* registrar apontamentos;
* recomendar providências;
* acompanhar correções.

**Capacidade:**

`CAP-COMPRAS-16`

---

# 35. PROC-COMPRAS-024 – Auditoria

**Objetivo:**

Permitir análise estruturada dos processos e registros.

**Atividades:**

* selecionar processos;
* analisar evidências;
* verificar conformidade;
* registrar achados;
* acompanhar recomendações.

---

# 36. PROC-COMPRAS-025 – Transparência

**Objetivo:**

Disponibilizar informações públicas sobre compras e contratações.

**Atividades:**

* identificar dados publicáveis;
* aplicar classificação;
* publicar;
* atualizar;
* disponibilizar consulta;
* manter histórico.

**Capacidade:**

`CAP-COMPRAS-15`

---

# 37. PROC-COMPRAS-026 – Gestão de Indicadores

**Objetivo:**

Produzir indicadores para acompanhamento do desempenho do domínio.

**Indicadores potenciais:**

* tempo médio de contratação;
* quantidade de processos;
* valor contratado;
* percentual de processos concluídos;
* contratos vencendo;
* percentual de atrasos;
* ocorrências;
* não conformidades;
* economia estimada;
* concentração de fornecedores.

**Capacidade:**

`CAP-COMPRAS-17`

---

# 38. PROC-COMPRAS-027 – Gestão de Informações

**Objetivo:**

Disponibilizar informações para gestão e tomada de decisão.

**Saídas:**

* relatórios;
* painéis;
* análises;
* alertas;
* informações gerenciais.

---

# 39. Processos Transversais

Além dos processos principais, o domínio deverá possuir capacidades/processos transversais.

```text
Gestão Documental
Gestão de Identidade
Gestão de Acessos
Auditoria
Notificações
Integrações
Indicadores
Transparência
```

Esses elementos não deverão ser duplicados desnecessariamente em cada processo.

---

# 40. Gestão Documental Transversal

A gestão documental deverá acompanhar:

```text
Necessidade
   ↓
Requisição
   ↓
Processo
   ↓
Procedimento
   ↓
Contrato
   ↓
Fiscalização
   ↓
Encerramento
```

Cada documento deverá possuir contexto e vínculo com seu objeto.

---

# 41. Gestão de Notificações

O domínio deverá permitir notificações relacionadas a:

* pendências;
* prazos;
* aprovações;
* vencimentos;
* ocorrências;
* contratos;
* fiscalizações;
* solicitações de complementação.

---

# 42. Gestão de Integrações

Os processos deverão poder integrar-se com:

```text
Orçamento
Contabilidade
Financeiro
Patrimônio
Almoxarifado
Cadastro Corporativo
Gestão Documental
Identidade
Transparência
BI
```

---

# 43. Mapa Geral de Processos

```text
                    GESTÃO DE COMPRAS
                    E CONTRATAÇÕES
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
  PLANEJAMENTO       PREPARAÇÃO          SELEÇÃO
        │                  │                  │
        ├─ Planejar        ├─ Necessidade     ├─ Preparar
        ├─ Consolidar      ├─ Requisição      ├─ Conduzir
        └─ Priorizar       ├─ Especificar     ├─ Analisar
                           ├─ Pesquisar       ├─ Decidir
                           └─ Instruir        └─ Formalizar
                                                │
                                                ▼
                                      GESTÃO CONTRATUAL
                                                │
                                      ├─ Gerir contrato
                                      ├─ Gerir obrigações
                                      ├─ Fiscalizar
                                      ├─ Ocorrências
                                      ├─ Alterações
                                      └─ Receber
                                                │
                                                ▼
                                          ENCERRAMENTO
                                                │
                                      ├─ Encerrar execução
                                      ├─ Encerrar contrato
                                      └─ Arquivar

                    GOVERNANÇA TRANSVERSAL
        ┌──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
    Controle      Auditoria    Transparência   Indicadores
```

---

# 44. Matriz de Processos

| ID                 | Processo                        | Macroprocesso | Capacidade Principal |
| ------------------ | ------------------------------- | ------------- | -------------------- |
| `PROC-COMPRAS-001` | Planejamento de Contratações    | MP-01         | CAP-01               |
| `PROC-COMPRAS-002` | Consolidação de Necessidades    | MP-01         | CAP-01               |
| `PROC-COMPRAS-003` | Priorização de Contratações     | MP-01         | CAP-01               |
| `PROC-COMPRAS-004` | Registro da Necessidade         | MP-02         | CAP-02               |
| `PROC-COMPRAS-005` | Gestão da Requisição            | MP-02         | CAP-03               |
| `PROC-COMPRAS-006` | Especificação do Objeto         | MP-02         | CAP-04               |
| `PROC-COMPRAS-007` | Pesquisa e Estimativa de Preços | MP-02         | CAP-05               |
| `PROC-COMPRAS-008` | Instrução do Processo           | MP-02         | CAP-06               |
| `PROC-COMPRAS-009` | Preparação do Procedimento      | MP-03         | CAP-08               |
| `PROC-COMPRAS-010` | Condução do Procedimento        | MP-03         | CAP-08               |
| `PROC-COMPRAS-011` | Análise e Julgamento            | MP-03         | CAP-08               |
| `PROC-COMPRAS-012` | Decisão                         | MP-03         | CAP-08               |
| `PROC-COMPRAS-013` | Formalização da Contratação     | MP-03         | CAP-09               |
| `PROC-COMPRAS-014` | Cadastro e Gestão do Contrato   | MP-04         | CAP-10               |
| `PROC-COMPRAS-015` | Gestão de Obrigações            | MP-04         | CAP-10               |
| `PROC-COMPRAS-016` | Fiscalização Contratual         | MP-04         | CAP-12               |
| `PROC-COMPRAS-017` | Gestão de Ocorrências           | MP-04         | CAP-11               |
| `PROC-COMPRAS-018` | Gestão de Alterações            | MP-04         | CAP-10               |
| `PROC-COMPRAS-019` | Gestão do Recebimento           | MP-04         | CAP-13               |
| `PROC-COMPRAS-020` | Encerramento da Execução        | MP-05         | CAP-11               |
| `PROC-COMPRAS-021` | Encerramento Contratual         | MP-05         | CAP-10               |
| `PROC-COMPRAS-022` | Arquivamento                    | MP-05         | CAP-14               |
| `PROC-COMPRAS-023` | Controle Interno                | MP-06         | CAP-16               |
| `PROC-COMPRAS-024` | Auditoria                       | MP-06         | CAP-16               |
| `PROC-COMPRAS-025` | Transparência                   | MP-06         | CAP-15               |
| `PROC-COMPRAS-026` | Gestão de Indicadores           | MP-06         | CAP-17               |
| `PROC-COMPRAS-027` | Gestão de Informações           | MP-06         | CAP-17               |

---

# 45. Matriz Processo × Atores

| Processo          | Principal            | Secundários                    |
| ----------------- | -------------------- | ------------------------------ |
| Planejamento      | Unidade de Compras   | Gestor, Requisitante           |
| Necessidade       | Servidor Solicitante | Gestor                         |
| Requisição        | Servidor Solicitante | Gestor, Compras                |
| Especificação     | Unidade Requisitante | Compras                        |
| Preços            | Compras              | Agente, Fornecedor             |
| Instrução         | Compras              | Jurídico, Financeiro, Contábil |
| Procedimento      | Agente               | Equipe, Fornecedores           |
| Julgamento        | Agente               | Equipe                         |
| Decisão           | Autoridade           | Jurídico, Compras              |
| Formalização      | Compras              | Autoridade, Fornecedor         |
| Gestão Contratual | Gestor               | Fiscal, Fornecedor             |
| Fiscalização      | Fiscal               | Gestor, Fornecedor             |
| Recebimento       | Unidade Requisitante | Fiscal, Fornecedor             |
| Encerramento      | Gestor               | Fiscal, Compras                |
| Controle          | Controle Interno     | Unidades                       |
| Auditoria         | Controle             | Unidades                       |
| Transparência     | Administração        | Cidadão                        |
| Indicadores       | Gestão               | Controle                       |

---

# 46. Matriz Processo × Capacidade

| Processo      | Capacidade     |
| ------------- | -------------- |
| Planejamento  | CAP-COMPRAS-01 |
| Necessidade   | CAP-COMPRAS-02 |
| Requisição    | CAP-COMPRAS-03 |
| Especificação | CAP-COMPRAS-04 |
| Preços        | CAP-COMPRAS-05 |
| Processo      | CAP-COMPRAS-06 |
| Fornecedores  | CAP-COMPRAS-07 |
| Procedimento  | CAP-COMPRAS-08 |
| Formalização  | CAP-COMPRAS-09 |
| Contrato      | CAP-COMPRAS-10 |
| Execução      | CAP-COMPRAS-11 |
| Fiscalização  | CAP-COMPRAS-12 |
| Recebimento   | CAP-COMPRAS-13 |
| Documentos    | CAP-COMPRAS-14 |
| Transparência | CAP-COMPRAS-15 |
| Controle      | CAP-COMPRAS-16 |
| Indicadores   | CAP-COMPRAS-17 |
| Integração    | CAP-COMPRAS-18 |

---

# 47. Eventos Principais do Domínio

Eventos relevantes poderão iniciar ou alterar processos.

Exemplos:

```text
Necessidade identificada
Requisição criada
Requisição aprovada
Processo aberto
Documentação pendente
Processo instruído
Procedimento iniciado
Proposta recebida
Resultado definido
Contratação aprovada
Contrato formalizado
Contrato iniciado
Entrega registrada
Ocorrência registrada
Fiscalização realizada
Contrato alterado
Contrato encerrado
Processo arquivado
```

---

# 48. Estados do Processo

Os processos poderão possuir estados controlados.

Exemplo:

```text
Rascunho
   ↓
Aberto
   ↓
Em análise
   ↓
Pendente
   ↓
Aprovado
   ↓
Em execução
   ↓
Concluído
   ↓
Encerrado
   ↓
Arquivado
```

Os estados específicos deverão ser definidos em cada processo.

---

# 49. Indicadores de Processos

Os principais indicadores deverão considerar:

### Eficiência

* tempo de ciclo;
* tempo de cada etapa;
* volume processado;
* retrabalho.

### Qualidade

* processos devolvidos;
* erros;
* pendências;
* não conformidades.

### Conformidade

* processos dentro dos prazos;
* documentos obrigatórios;
* controles realizados.

### Resultado

* contratações concluídas;
* contratos executados;
* economia;
* atendimento das necessidades.

---

# 50. Riscos de Processo

Os processos deverão possuir riscos identificados.

Exemplos:

* atraso;
* ausência de documentação;
* especificação inadequada;
* estimativa inadequada;
* falha de comunicação;
* perda de prazo;
* ausência de fiscalização;
* registro incompleto;
* inconsistência de dados;
* ausência de evidência.

---

# 51. Automação dos Processos

A automação deverá ser definida somente após o entendimento do processo.

Possíveis automações:

```text
Validação
↓
Alertas
↓
Notificações
↓
Controle de prazos
↓
Integrações
↓
Geração de documentos
↓
Indicadores
↓
Análises
```

---

# 52. Processo e Offline First

Processos que possuam atividades em campo deverão considerar o modelo **Offline First** do SIGMUN.

Exemplo:

```text
Fiscalização
     ↓
Dispositivo móvel
     ↓
Registro offline
     ↓
Evidências
     ↓
Sincronização
     ↓
Processo
```

---

# 53. Processo e Gestão Documental

Todo processo deverá possuir uma estrutura documental coerente.

Exemplo:

```text
Processo
│
├── Necessidade
├── Requisição
├── Especificação
├── Pesquisa de Preços
├── Documentação
├── Procedimento
├── Contrato
├── Fiscalização
├── Recebimento
├── Ocorrências
└── Encerramento
```

---

# 54. Processo e Rastreabilidade

Cada etapa deverá ser rastreável.

A trilha mínima deverá permitir identificar:

* quem;
* quando;
* o quê;
* em qual processo;
* qual informação;
* qual documento;
* qual decisão;
* qual resultado.

---

# 55. Processo e Segregação de Funções

Os processos deverão permitir a aplicação de segregação de funções.

Exemplo:

```text
Solicitar
   ≠
Aprovar
   ≠
Conduzir
   ≠
Fiscalizar
```

A configuração final deverá respeitar as competências legais e administrativas.

---

# 56. Processo e Integração

Os processos deverão ser integrados aos demais domínios quando houver dependência.

Exemplo:

```text
Gestão de Compras
        │
        ├── Orçamento
        ├── Financeiro
        ├── Contabilidade
        ├── Patrimônio
        ├── Almoxarifado
        ├── Documentos
        ├── Identidade
        └── Transparência
```

---

# 57. Lacunas a Validar

Antes da especificação detalhada deverão ser validados:

* processos efetivamente existentes;
* processos obrigatórios;
* responsabilidades;
* fluxos;
* exceções;
* documentos;
* aprovações;
* prazos;
* integrações;
* controles;
* indicadores;
* regras de negócio.

---

# 58. Próximo Nível de Detalhamento

Este mapa deverá ser decomposto posteriormente em:

```text
Processo
   ↓
Subprocesso
   ↓
Atividade
   ↓
Tarefa
   ↓
Regra de Negócio
   ↓
Caso de Uso
   ↓
Requisito
```

O detalhamento operacional não deverá ser incorporado prematuramente neste documento.

---

# 59. Relação com o Mapa Mestre

Este documento deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`PROC-MAP-COMPRAS-001`

Rastreabilidade principal:

```text
DOM-COMPRAS-001
       ↓
CAP-MAP-COMPRAS-001
       ↓
PROC-MAP-COMPRAS-001
       ↓
PROC-COMPRAS-001...027
       ↓
SERV-COMPRAS-001...
       ↓
UC-COMPRAS-001...
       ↓
RF-COMPRAS-001...
       ↓
TEST-COMPRAS-001...
```

---

# 60. Critérios de Conclusão

O Mapa de Processos será considerado suficientemente definido quando:

* os macroprocessos estiverem identificados;
* os processos principais estiverem identificados;
* cada processo possuir objetivo;
* entradas e saídas principais estiverem identificadas;
* atores principais estiverem definidos;
* capacidades estiverem relacionadas;
* processos transversais estiverem identificados;
* dependências relevantes estiverem registradas;
* lacunas estiverem explicitadas;
* rastreabilidade estiver estabelecida.

---

# 61. Evolução

O mapa deverá ser revisado quando:

* processos forem descobertos;
* processos forem eliminados;
* processos forem consolidados;
* legislação alterar procedimentos;
* responsabilidades forem modificadas;
* novos serviços forem criados;
* integrações forem incorporadas;
* o modelo organizacional mudar.

---

# 62. Disposição Final

O **Mapa de Processos – Gestão de Compras e Contratações** constitui a ponte entre as capacidades institucionais e a futura especificação funcional do SIGMUN.

A arquitetura de referência será:

```text
DOMÍNIO
   ↓
ATORES
   ↓
CAPACIDADES
   ↓
PROCESSOS
   ↓
SERVIÇOS
   ↓
CASOS DE USO
   ↓
HISTÓRIAS DE USUÁRIO
   ↓
REQUISITOS
   ↓
REGRAS DE NEGÓCIO
   ↓
ESPECIFICAÇÕES
   ↓
IMPLEMENTAÇÃO
   ↓
TESTES
   ↓
EVIDÊNCIAS
```

Essa cadeia deverá ser preservada para garantir rastreabilidade integral entre a necessidade institucional e a solução tecnológica.

---

# Controle de Versões

| Versão | Data       | Descrição                                                                   |
| ------ | ---------- | --------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do Mapa de Processos do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
