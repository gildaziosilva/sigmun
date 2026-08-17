# 004 – Mapa de Serviços – Gestão de Compras e Contratações

#### Mapa de Serviços – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
* 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Modelo-de-Competencias.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md

---

# 1. Finalidade

O **Mapa de Serviços – Gestão de Compras e Contratações** identifica os serviços disponibilizados pelo domínio para apoiar os processos administrativos, as unidades organizacionais, os agentes públicos, fornecedores, órgãos de controle e demais partes interessadas.

O mapa estabelece uma visão funcional dos serviços, sem detalhar ainda:

* telas;
* APIs;
* requisitos funcionais;
* regras de negócio;
* fluxos detalhados;
* casos de uso;
* histórias de usuário;
* implementação tecnológica.

Esses elementos serão detalhados nos artefatos subsequentes.

---

# 2. Conceito de Serviço

No SIGMUN, um serviço representa uma capacidade disponibilizada de forma organizada para atender uma necessidade de negócio.

Um serviço pode:

* receber uma solicitação;
* executar uma operação;
* produzir uma informação;
* alterar o estado de um objeto de negócio;
* disponibilizar uma consulta;
* gerar uma decisão;
* produzir uma evidência;
* emitir uma notificação;
* integrar informações entre domínios.

A relação conceitual será:

```text
Necessidade
     ↓
Capacidade
     ↓
Processo
     ↓
Serviço
     ↓
Resultado
```

---

# 3. Princípio de Modelagem

Os serviços deverão ser definidos a partir das necessidades do negócio e não a partir das telas ou estruturas internas do software.

O serviço deverá representar uma entrega reconhecível pelo consumidor.

Exemplo:

```text
"Registrar Requisição de Compra"
```

é um serviço de negócio.

Já:

```text
"Executar INSERT na tabela requisicao"
```

é uma implementação técnica e não deverá ser tratada como serviço de negócio.

---

# 4. Arquitetura Geral dos Serviços

O domínio será organizado nos seguintes grupos:

```text
GESTÃO DE COMPRAS E CONTRATAÇÕES
│
├── Serviços de Planejamento
├── Serviços de Requisição
├── Serviços de Especificação
├── Serviços de Pesquisa de Preços
├── Serviços de Processos de Contratação
├── Serviços de Fornecedores
├── Serviços de Contratos
├── Serviços de Execução Contratual
├── Serviços de Fiscalização
├── Serviços de Recebimento
├── Serviços de Encerramento
├── Serviços de Documentação
├── Serviços de Transparência
├── Serviços de Controle e Auditoria
├── Serviços de Indicadores
└── Serviços de Integração
```

---

# 5. Identificação dos Serviços

Os serviços do domínio utilizarão o padrão:

```text
SERV-COMPRAS-XXX
```

Exemplo:

```text
SERV-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida do serviço.

Alterações de nome ou descrição não deverão provocar alteração desnecessária do identificador.

---

# 6. Serviços de Planejamento

## 6.1 SERV-COMPRAS-001 – Planejar Contratações

**Objetivo:**

Permitir o planejamento das necessidades futuras de compras e contratações.

**Consumidores:**

* Unidade de Compras;
* Gestores;
* Unidades Requisitantes.

**Principais resultados:**

* planejamento registrado;
* calendário;
* prioridades;
* necessidades previstas.

**Processos relacionados:**

* PROC-COMPRAS-001.

**Capacidade relacionada:**

* CAP-COMPRAS-01.

---

## 6.2 SERV-COMPRAS-002 – Consolidar Necessidades

**Objetivo:**

Consolidar necessidades semelhantes ou relacionadas das unidades administrativas.

**Consumidores:**

* Unidade de Compras;
* Gestores.

**Resultados:**

* demandas consolidadas;
* agrupamentos;
* oportunidades de contratação conjunta.

**Processos relacionados:**

* PROC-COMPRAS-002.

---

## 6.3 SERV-COMPRAS-003 – Priorizar Contratações

**Objetivo:**

Permitir a definição de prioridades para as contratações planejadas.

**Resultados:**

* lista priorizada;
* classificação de criticidade;
* justificativas.

**Processos relacionados:**

* PROC-COMPRAS-003.

---

# 7. Serviços de Necessidade e Requisição

## 7.1 SERV-COMPRAS-004 – Registrar Necessidade

**Objetivo:**

Registrar uma necessidade de aquisição ou contratação.

**Consumidores:**

* Servidores;
* Unidades Requisitantes.

**Resultados:**

* necessidade registrada;
* justificativa;
* prioridade.

**Processo relacionado:**

* PROC-COMPRAS-004.

---

## 7.2 SERV-COMPRAS-005 – Solicitar Compra ou Contratação

**Objetivo:**

Permitir a formalização de uma solicitação de compra ou contratação.

**Resultados:**

* requisição;
* itens;
* quantidades;
* justificativas;
* documentos.

**Processo relacionado:**

* PROC-COMPRAS-005.

---

## 7.3 SERV-COMPRAS-006 – Aprovar Requisição

**Objetivo:**

Permitir a análise e aprovação das requisições pelas autoridades responsáveis.

**Resultados:**

* requisição aprovada;
* requisição devolvida;
* requisição rejeitada.

**Processo relacionado:**

* PROC-COMPRAS-005.

---

## 7.4 SERV-COMPRAS-007 – Acompanhar Requisição

**Objetivo:**

Permitir o acompanhamento do ciclo de vida da requisição.

**Informações:**

* situação;
* responsável;
* histórico;
* pendências;
* encaminhamentos.

---

# 8. Serviços de Especificação

## 8.1 SERV-COMPRAS-008 – Especificar Objeto

**Objetivo:**

Permitir a definição das características do objeto a ser contratado.

**Resultados:**

* descrição;
* requisitos;
* quantidade;
* unidade de medida;
* especificação técnica.

**Processo relacionado:**

* PROC-COMPRAS-006.

---

## 8.2 SERV-COMPRAS-009 – Validar Especificação

**Objetivo:**

Permitir a validação da especificação antes do prosseguimento do processo.

**Resultados:**

* especificação validada;
* pendências;
* solicitação de ajustes.

---

# 9. Serviços de Pesquisa de Preços

## 9.1 SERV-COMPRAS-010 – Registrar Pesquisa de Preços

**Objetivo:**

Registrar informações utilizadas na formação da estimativa de preços.

**Resultados:**

* fontes;
* referências;
* valores;
* documentos comprobatórios.

**Processo relacionado:**

* PROC-COMPRAS-007.

---

## 9.2 SERV-COMPRAS-011 – Calcular Estimativa de Preço

**Objetivo:**

Apoiar a determinação do valor estimado do objeto.

**Resultados:**

* estimativa;
* metodologia;
* memória de cálculo;
* evidências.

---

## 9.3 SERV-COMPRAS-012 – Consultar Histórico de Preços

**Objetivo:**

Permitir consulta a informações históricas relacionadas a preços.

**Resultados:**

* histórico;
* comparações;
* referências.

---

# 10. Serviços de Processos de Contratação

## 10.1 SERV-COMPRAS-013 – Abrir Processo de Contratação

**Objetivo:**

Criar e formalizar o processo administrativo de contratação.

**Resultados:**

* processo;
* identificação;
* vínculo com a necessidade;
* documentação inicial.

**Processo relacionado:**

* PROC-COMPRAS-008.

---

## 10.2 SERV-COMPRAS-014 – Instruir Processo

**Objetivo:**

Organizar e complementar a documentação necessária ao processo.

**Resultados:**

* processo instruído;
* pendências identificadas;
* documentos vinculados.

---

## 10.3 SERV-COMPRAS-015 – Preparar Procedimento de Contratação

**Objetivo:**

Preparar o procedimento aplicável à contratação.

**Resultados:**

* procedimento configurado;
* cronograma;
* documentação.

**Processo relacionado:**

* PROC-COMPRAS-009.

---

## 10.4 SERV-COMPRAS-016 – Conduzir Procedimento

**Objetivo:**

Apoiar a execução e o registro dos atos do procedimento de contratação.

**Resultados:**

* participantes;
* propostas;
* atos;
* ocorrências;
* resultados.

**Processo relacionado:**

* PROC-COMPRAS-010.

---

## 10.5 SERV-COMPRAS-017 – Analisar e Julgar Propostas

**Objetivo:**

Registrar a análise e o julgamento das propostas e documentos.

**Resultados:**

* análises;
* classificação;
* julgamento;
* justificativas.

**Processo relacionado:**

* PROC-COMPRAS-011.

---

## 10.6 SERV-COMPRAS-018 – Registrar Decisão

**Objetivo:**

Registrar decisões das autoridades competentes.

**Resultados:**

* decisão;
* aprovação;
* homologação quando aplicável;
* encaminhamentos.

**Processo relacionado:**

* PROC-COMPRAS-012.

---

# 11. Serviços de Fornecedores

## 11.1 SERV-COMPRAS-019 – Cadastrar Fornecedor

**Objetivo:**

Registrar ou integrar informações cadastrais de fornecedores.

**Resultados:**

* fornecedor identificado;
* dados cadastrais;
* situação cadastral.

---

## 11.2 SERV-COMPRAS-020 – Consultar Fornecedor

**Objetivo:**

Permitir consulta às informações do fornecedor.

**Resultados:**

* dados cadastrais;
* histórico;
* contratos relacionados;
* situação.

---

## 11.3 SERV-COMPRAS-021 – Consultar Histórico do Fornecedor

**Objetivo:**

Permitir análise do relacionamento histórico do fornecedor com o Município.

**Informações potenciais:**

* contratos;
* valores;
* ocorrências;
* entregas;
* desempenho;
* sanções ou registros pertinentes.

---

# 12. Serviços de Formalização

## 12.1 SERV-COMPRAS-022 – Formalizar Contratação

**Objetivo:**

Formalizar a contratação decorrente do processo.

**Resultados:**

* instrumento;
* assinaturas;
* registro;
* publicação quando aplicável.

**Processo relacionado:**

* PROC-COMPRAS-013.

---

## 12.2 SERV-COMPRAS-023 – Gerenciar Instrumento de Contratação

**Objetivo:**

Manter as informações do instrumento contratado.

**Informações:**

* objeto;
* fornecedor;
* valor;
* vigência;
* responsáveis;
* obrigações;
* documentos.

---

# 13. Serviços de Gestão Contratual

## 13.1 SERV-COMPRAS-024 – Registrar Contrato

**Objetivo:**

Registrar contrato ou instrumento equivalente no SIGMUN.

**Resultados:**

* contrato cadastrado;
* vínculos;
* responsáveis;
* vigência.

---

## 13.2 SERV-COMPRAS-025 – Acompanhar Contrato

**Objetivo:**

Permitir o acompanhamento do ciclo de vida contratual.

**Informações:**

* situação;
* vigência;
* valor;
* execução;
* obrigações;
* ocorrências.

---

## 13.3 SERV-COMPRAS-026 – Gerenciar Obrigações Contratuais

**Objetivo:**

Controlar obrigações atribuídas às partes.

**Resultados:**

* obrigações;
* prazos;
* responsáveis;
* evidências;
* pendências.

**Processo relacionado:**

* PROC-COMPRAS-015.

---

## 13.4 SERV-COMPRAS-027 – Controlar Vigência

**Objetivo:**

Acompanhar prazos e vigência dos instrumentos.

**Resultados:**

* alertas;
* vencimentos;
* prorrogações potenciais;
* pendências.

---

# 14. Serviços de Fiscalização

## 14.1 SERV-COMPRAS-028 – Designar Fiscal

**Objetivo:**

Registrar o responsável pela fiscalização do contrato.

**Resultados:**

* fiscal designado;
* período;
* responsabilidades.

---

## 14.2 SERV-COMPRAS-029 – Registrar Fiscalização

**Objetivo:**

Registrar as atividades de fiscalização contratual.

**Resultados:**

* fiscalização;
* observações;
* evidências;
* conformidade;
* ocorrências.

**Processo relacionado:**

* PROC-COMPRAS-016.

---

## 14.3 SERV-COMPRAS-030 – Registrar Não Conformidade

**Objetivo:**

Registrar situações em que a execução não esteja conforme o esperado.

**Resultados:**

* não conformidade;
* evidências;
* responsável;
* prazo de correção;
* acompanhamento.

---

## 14.4 SERV-COMPRAS-031 – Acompanhar Correção

**Objetivo:**

Acompanhar as providências relacionadas às não conformidades.

---

# 15. Serviços de Ocorrências

## 15.1 SERV-COMPRAS-032 – Registrar Ocorrência Contratual

**Objetivo:**

Registrar fatos relevantes ocorridos durante a execução.

**Exemplos:**

* atraso;
* falha;
* descumprimento;
* divergência;
* ocorrência operacional.

---

## 15.2 SERV-COMPRAS-033 – Acompanhar Ocorrência

**Objetivo:**

Controlar o tratamento das ocorrências.

**Resultados:**

* providências;
* responsáveis;
* prazos;
* situação;
* evidências.

---

# 16. Serviços de Alterações Contratuais

## 16.1 SERV-COMPRAS-034 – Solicitar Alteração Contratual

**Objetivo:**

Registrar a necessidade de alteração do instrumento.

---

## 16.2 SERV-COMPRAS-035 – Gerenciar Aditivo

**Objetivo:**

Controlar os instrumentos de alteração contratual.

**Resultados:**

* solicitação;
* análise;
* aprovação;
* instrumento;
* histórico.

---

## 16.3 SERV-COMPRAS-036 – Gerenciar Prorrogação

**Objetivo:**

Acompanhar solicitações e registros relacionados à extensão da vigência quando aplicável.

---

## 16.4 SERV-COMPRAS-037 – Gerenciar Reajuste ou Revisão

**Objetivo:**

Registrar e acompanhar alterações de valores quando aplicáveis.

---

# 17. Serviços de Recebimento

## 17.1 SERV-COMPRAS-038 – Registrar Entrega

**Objetivo:**

Registrar a entrega de bens ou a prestação do serviço.

**Resultados:**

* entrega;
* data;
* quantidade;
* documentos;
* evidências.

**Processo relacionado:**

* PROC-COMPRAS-019.

---

## 17.2 SERV-COMPRAS-039 – Conferir Entrega

**Objetivo:**

Permitir a verificação da conformidade da entrega.

---

## 17.3 SERV-COMPRAS-040 – Registrar Aceite

**Objetivo:**

Registrar a aceitação da entrega ou execução quando aplicável.

---

## 17.4 SERV-COMPRAS-041 – Registrar Recusa ou Divergência

**Objetivo:**

Registrar situações em que a entrega ou execução não esteja conforme.

---

# 18. Serviços de Encerramento

## 18.1 SERV-COMPRAS-042 – Encerrar Execução

**Objetivo:**

Registrar a conclusão da execução do objeto.

**Processo relacionado:**

* PROC-COMPRAS-020.

---

## 18.2 SERV-COMPRAS-043 – Encerrar Contrato

**Objetivo:**

Formalizar o encerramento do instrumento contratual.

**Processo relacionado:**

* PROC-COMPRAS-021.

---

## 18.3 SERV-COMPRAS-044 – Arquivar Processo

**Objetivo:**

Realizar o encerramento e arquivamento do processo conforme as políticas aplicáveis.

**Processo relacionado:**

* PROC-COMPRAS-022.

---

# 19. Serviços de Gestão Documental

## 19.1 SERV-COMPRAS-045 – Anexar Documento

**Objetivo:**

Vincular documentos ao processo ou objeto de negócio.

---

## 19.2 SERV-COMPRAS-046 – Consultar Documentos

**Objetivo:**

Permitir acesso aos documentos conforme autorização.

---

## 19.3 SERV-COMPRAS-047 – Gerenciar Evidências

**Objetivo:**

Registrar e preservar evidências relacionadas às atividades do domínio.

**Exemplos:**

* fotografias;
* documentos;
* registros de fiscalização;
* comprovantes;
* manifestações;
* relatórios.

---

# 20. Serviços de Transparência

## 20.1 SERV-COMPRAS-048 – Consultar Contratações

**Objetivo:**

Disponibilizar consulta às informações públicas das contratações.

**Consumidores:**

* Cidadãos;
* Órgãos de controle;
* Imprensa;
* Pesquisadores.

---

## 20.2 SERV-COMPRAS-049 – Consultar Contratos

**Objetivo:**

Disponibilizar informações públicas sobre contratos.

---

## 20.3 SERV-COMPRAS-050 – Consultar Processos

**Objetivo:**

Disponibilizar informações publicáveis sobre os processos.

---

## 20.4 SERV-COMPRAS-051 – Exportar Dados Públicos

**Objetivo:**

Disponibilizar dados em formatos apropriados para reutilização.

---

# 21. Serviços de Controle e Auditoria

## 21.1 SERV-COMPRAS-052 – Consultar Trilha de Auditoria

**Objetivo:**

Permitir consulta aos registros de atividades realizadas no sistema.

**Informações mínimas:**

* usuário;
* data;
* hora;
* operação;
* objeto;
* situação anterior;
* situação posterior.

---

## 21.2 SERV-COMPRAS-053 – Executar Controle

**Objetivo:**

Apoiar atividades de controle interno.

---

## 21.3 SERV-COMPRAS-054 – Registrar Achado de Auditoria

**Objetivo:**

Registrar achados, recomendações e providências de auditoria.

---

## 21.4 SERV-COMPRAS-055 – Acompanhar Recomendação

**Objetivo:**

Acompanhar o tratamento das recomendações.

---

# 22. Serviços de Indicadores

## 22.1 SERV-COMPRAS-056 – Consultar Indicadores

**Objetivo:**

Disponibilizar indicadores de desempenho do domínio.

**Exemplos:**

* tempo médio de contratação;
* quantidade de processos;
* valor contratado;
* contratos vigentes;
* contratos próximos do vencimento;
* atrasos;
* ocorrências.

---

## 22.2 SERV-COMPRAS-057 – Gerar Relatório Gerencial

**Objetivo:**

Disponibilizar informações consolidadas para tomada de decisão.

---

## 22.3 SERV-COMPRAS-058 – Consultar Painel Gerencial

**Objetivo:**

Disponibilizar visão analítica do domínio.

---

# 23. Serviços de Alertas e Notificações

## 23.1 SERV-COMPRAS-059 – Gerenciar Alertas

**Objetivo:**

Gerenciar alertas relacionados a eventos importantes.

**Exemplos:**

* vencimento;
* pendência;
* atraso;
* não conformidade;
* aprovação pendente.

---

## 23.2 SERV-COMPRAS-060 – Enviar Notificação

**Objetivo:**

Notificar os responsáveis sobre eventos ou pendências.

---

# 24. Serviços de Integração

## 24.1 SERV-COMPRAS-061 – Integrar com Orçamento

**Objetivo:**

Disponibilizar integração com informações orçamentárias.

---

## 24.2 SERV-COMPRAS-062 – Integrar com Financeiro

**Objetivo:**

Permitir integração com informações financeiras relacionadas.

---

## 24.3 SERV-COMPRAS-063 – Integrar com Contabilidade

**Objetivo:**

Permitir integração com informações contábeis.

---

## 24.4 SERV-COMPRAS-064 – Integrar com Patrimônio

**Objetivo:**

Permitir integração de bens adquiridos com a gestão patrimonial.

---

## 24.5 SERV-COMPRAS-065 – Integrar com Almoxarifado

**Objetivo:**

Permitir integração entre aquisição e recebimento/estoque.

---

## 24.6 SERV-COMPRAS-066 – Integrar com Gestão Documental

**Objetivo:**

Garantir o vínculo documental entre os domínios.

---

## 24.7 SERV-COMPRAS-067 – Integrar com Transparência

**Objetivo:**

Disponibilizar automaticamente informações publicáveis.

---

# 25. Matriz de Serviços

| ID               | Serviço                           | Grupo         |
| ---------------- | --------------------------------- | ------------- |
| SERV-COMPRAS-001 | Planejar Contratações             | Planejamento  |
| SERV-COMPRAS-002 | Consolidar Necessidades           | Planejamento  |
| SERV-COMPRAS-003 | Priorizar Contratações            | Planejamento  |
| SERV-COMPRAS-004 | Registrar Necessidade             | Requisição    |
| SERV-COMPRAS-005 | Solicitar Compra ou Contratação   | Requisição    |
| SERV-COMPRAS-006 | Aprovar Requisição                | Requisição    |
| SERV-COMPRAS-007 | Acompanhar Requisição             | Requisição    |
| SERV-COMPRAS-008 | Especificar Objeto                | Especificação |
| SERV-COMPRAS-009 | Validar Especificação             | Especificação |
| SERV-COMPRAS-010 | Registrar Pesquisa de Preços      | Preços        |
| SERV-COMPRAS-011 | Calcular Estimativa de Preço      | Preços        |
| SERV-COMPRAS-012 | Consultar Histórico de Preços     | Preços        |
| SERV-COMPRAS-013 | Abrir Processo de Contratação     | Processo      |
| SERV-COMPRAS-014 | Instruir Processo                 | Processo      |
| SERV-COMPRAS-015 | Preparar Procedimento             | Contratação   |
| SERV-COMPRAS-016 | Conduzir Procedimento             | Contratação   |
| SERV-COMPRAS-017 | Analisar e Julgar Propostas       | Contratação   |
| SERV-COMPRAS-018 | Registrar Decisão                 | Contratação   |
| SERV-COMPRAS-019 | Cadastrar Fornecedor              | Fornecedores  |
| SERV-COMPRAS-020 | Consultar Fornecedor              | Fornecedores  |
| SERV-COMPRAS-021 | Consultar Histórico do Fornecedor | Fornecedores  |
| SERV-COMPRAS-022 | Formalizar Contratação            | Formalização  |
| SERV-COMPRAS-023 | Gerenciar Instrumento             | Formalização  |
| SERV-COMPRAS-024 | Registrar Contrato                | Contratos     |
| SERV-COMPRAS-025 | Acompanhar Contrato               | Contratos     |
| SERV-COMPRAS-026 | Gerenciar Obrigações              | Contratos     |
| SERV-COMPRAS-027 | Controlar Vigência                | Contratos     |
| SERV-COMPRAS-028 | Designar Fiscal                   | Fiscalização  |
| SERV-COMPRAS-029 | Registrar Fiscalização            | Fiscalização  |
| SERV-COMPRAS-030 | Registrar Não Conformidade        | Fiscalização  |
| SERV-COMPRAS-031 | Acompanhar Correção               | Fiscalização  |
| SERV-COMPRAS-032 | Registrar Ocorrência              | Ocorrências   |
| SERV-COMPRAS-033 | Acompanhar Ocorrência             | Ocorrências   |
| SERV-COMPRAS-034 | Solicitar Alteração               | Alterações    |
| SERV-COMPRAS-035 | Gerenciar Aditivo                 | Alterações    |
| SERV-COMPRAS-036 | Gerenciar Prorrogação             | Alterações    |
| SERV-COMPRAS-037 | Gerenciar Reajuste ou Revisão     | Alterações    |
| SERV-COMPRAS-038 | Registrar Entrega                 | Recebimento   |
| SERV-COMPRAS-039 | Conferir Entrega                  | Recebimento   |
| SERV-COMPRAS-040 | Registrar Aceite                  | Recebimento   |
| SERV-COMPRAS-041 | Registrar Recusa ou Divergência   | Recebimento   |
| SERV-COMPRAS-042 | Encerrar Execução                 | Encerramento  |
| SERV-COMPRAS-043 | Encerrar Contrato                 | Encerramento  |
| SERV-COMPRAS-044 | Arquivar Processo                 | Encerramento  |
| SERV-COMPRAS-045 | Anexar Documento                  | Documentação  |
| SERV-COMPRAS-046 | Consultar Documentos              | Documentação  |
| SERV-COMPRAS-047 | Gerenciar Evidências              | Documentação  |
| SERV-COMPRAS-048 | Consultar Contratações            | Transparência |
| SERV-COMPRAS-049 | Consultar Contratos               | Transparência |
| SERV-COMPRAS-050 | Consultar Processos               | Transparência |
| SERV-COMPRAS-051 | Exportar Dados Públicos           | Transparência |
| SERV-COMPRAS-052 | Consultar Trilha de Auditoria     | Controle      |
| SERV-COMPRAS-053 | Executar Controle                 | Controle      |
| SERV-COMPRAS-054 | Registrar Achado de Auditoria     | Auditoria     |
| SERV-COMPRAS-055 | Acompanhar Recomendação           | Auditoria     |
| SERV-COMPRAS-056 | Consultar Indicadores             | Indicadores   |
| SERV-COMPRAS-057 | Gerar Relatório Gerencial         | Indicadores   |
| SERV-COMPRAS-058 | Consultar Painel Gerencial        | Indicadores   |
| SERV-COMPRAS-059 | Gerenciar Alertas                 | Notificações  |
| SERV-COMPRAS-060 | Enviar Notificação                | Notificações  |
| SERV-COMPRAS-061 | Integrar com Orçamento            | Integração    |
| SERV-COMPRAS-062 | Integrar com Financeiro           | Integração    |
| SERV-COMPRAS-063 | Integrar com Contabilidade        | Integração    |
| SERV-COMPRAS-064 | Integrar com Patrimônio           | Integração    |
| SERV-COMPRAS-065 | Integrar com Almoxarifado         | Integração    |
| SERV-COMPRAS-066 | Integrar com Gestão Documental    | Integração    |
| SERV-COMPRAS-067 | Integrar com Transparência        | Integração    |

---

# 26. Matriz Serviço × Processo

| Serviço          | Processo         |
| ---------------- | ---------------- |
| SERV-COMPRAS-001 | PROC-COMPRAS-001 |
| SERV-COMPRAS-002 | PROC-COMPRAS-002 |
| SERV-COMPRAS-003 | PROC-COMPRAS-003 |
| SERV-COMPRAS-004 | PROC-COMPRAS-004 |
| SERV-COMPRAS-005 | PROC-COMPRAS-005 |
| SERV-COMPRAS-006 | PROC-COMPRAS-005 |
| SERV-COMPRAS-008 | PROC-COMPRAS-006 |
| SERV-COMPRAS-010 | PROC-COMPRAS-007 |
| SERV-COMPRAS-013 | PROC-COMPRAS-008 |
| SERV-COMPRAS-015 | PROC-COMPRAS-009 |
| SERV-COMPRAS-016 | PROC-COMPRAS-010 |
| SERV-COMPRAS-017 | PROC-COMPRAS-011 |
| SERV-COMPRAS-018 | PROC-COMPRAS-012 |
| SERV-COMPRAS-022 | PROC-COMPRAS-013 |
| SERV-COMPRAS-024 | PROC-COMPRAS-014 |
| SERV-COMPRAS-026 | PROC-COMPRAS-015 |
| SERV-COMPRAS-029 | PROC-COMPRAS-016 |
| SERV-COMPRAS-032 | PROC-COMPRAS-017 |
| SERV-COMPRAS-035 | PROC-COMPRAS-018 |
| SERV-COMPRAS-038 | PROC-COMPRAS-019 |
| SERV-COMPRAS-042 | PROC-COMPRAS-020 |
| SERV-COMPRAS-043 | PROC-COMPRAS-021 |
| SERV-COMPRAS-044 | PROC-COMPRAS-022 |
| SERV-COMPRAS-053 | PROC-COMPRAS-023 |
| SERV-COMPRAS-054 | PROC-COMPRAS-024 |
| SERV-COMPRAS-048 | PROC-COMPRAS-025 |
| SERV-COMPRAS-056 | PROC-COMPRAS-026 |
| SERV-COMPRAS-057 | PROC-COMPRAS-027 |

Os demais serviços complementam, apoiam ou atravessam os processos principais.

---

# 27. Matriz Serviço × Atores

| Grupo         | Consumidores Principais |
| ------------- | ----------------------- |
| Planejamento  | Compras, Gestores       |
| Requisição    | Servidores, Gestores    |
| Especificação | Unidades Requisitantes  |
| Preços        | Compras                 |
| Contratação   | Agentes, Equipes        |
| Fornecedores  | Compras, Gestores       |
| Contratos     | Gestores, Fiscais       |
| Fiscalização  | Fiscais                 |
| Recebimento   | Unidades Requisitantes  |
| Transparência | Cidadãos, Controle      |
| Auditoria     | Controle Interno        |
| Indicadores   | Gestores                |
| Integrações   | Sistemas Corporativos   |

---

# 28. Serviços Internos e Serviços Externos

Os serviços deverão ser classificados conforme seus consumidores.

## 28.1 Serviços Internos

Consumidos por usuários e unidades administrativas.

Exemplos:

* registrar necessidade;
* solicitar contratação;
* aprovar requisição;
* instruir processo;
* fiscalizar contrato;
* registrar recebimento.

## 28.2 Serviços Externos

Disponibilizados para partes externas.

Exemplos:

* consultar contratações;
* consultar contratos;
* consultar processos;
* consultar dados públicos;
* exportar dados.

---

# 29. Serviços Digitais

Sempre que aplicável, os serviços deverão possuir representação digital.

A experiência poderá ocorrer por:

* portal web;
* aplicativo;
* dispositivo móvel;
* API;
* integração entre sistemas;
* portal de transparência.

---

# 30. Serviços Móveis

Serviços que envolvam atividades em campo deverão considerar o modelo de mobilidade do SIGMUN.

Exemplo:

```text
SERV-COMPRAS-029
Registrar Fiscalização
        ↓
Aplicativo móvel
        ↓
Operação Offline First
        ↓
Evidências
        ↓
Sincronização
        ↓
Processo Contratual
```

---

# 31. Serviços e Evidências

Serviços que alterem ou comprovem estados relevantes deverão permitir registro de evidências quando aplicável.

Exemplos:

* fiscalização;
* entrega;
* aceite;
* não conformidade;
* ocorrência;
* decisão.

---

# 32. Serviços e Segurança

O acesso aos serviços deverá respeitar:

* identidade;
* autenticação;
* autorização;
* perfil;
* função;
* unidade organizacional;
* segregação de funções;
* classificação da informação;
* auditoria.

---

# 33. Serviços e Transparência

A existência de um serviço interno não implica necessariamente publicação integral de seus dados.

Deverá ser aplicada a política:

> **Aberto sempre que possível, restrito sempre que necessário.**

A exposição pública deverá respeitar:

* classificação da informação;
* legislação aplicável;
* proteção de dados;
* transparência pública;
* segurança.

---

# 34. Serviços e Integração

Os serviços deverão ser projetados considerando reutilização e integração.

Um serviço poderá ser consumido por:

```text
Usuário
   │
   ├── Web
   ├── Mobile
   └── Portal
        │
        ▼
     Serviço
        │
        ├── Processo
        ├── Documento
        ├── Dados
        └── Integrações
```

---

# 35. Relação com Casos de Uso

Os serviços deverão servir como base para identificação dos casos de uso.

Exemplo:

```text
SERV-COMPRAS-005
Solicitar Compra ou Contratação
             ↓
UC-COMPRAS-001
Solicitar Compra
             ↓
HU-COMPRAS-001
Como servidor...
             ↓
RF-COMPRAS-001...
```

---

# 36. Relação com Requisitos

Cada serviço poderá gerar um ou mais requisitos funcionais.

Exemplo:

```text
SERV-COMPRAS-029
Registrar Fiscalização
        ↓
RF-COMPRAS-XXX
O sistema deve permitir registrar fiscalização.
        ↓
RN-COMPRAS-XXX
Somente usuários autorizados poderão registrar fiscalização.
        ↓
CA-COMPRAS-XXX
Critérios de aceitação
        ↓
TEST-COMPRAS-XXX
Teste correspondente
```

---

# 37. Relação com Indicadores

Os serviços deverão produzir dados que possam alimentar os indicadores do domínio.

Exemplo:

```text
Serviço
   ↓
Evento
   ↓
Registro
   ↓
Indicador
   ↓
Dashboard
```

---

# 38. Relação com o Mapa Mestre

Este documento deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`SERV-MAP-COMPRAS-001`

Rastreabilidade principal:

```text
DOM-COMPRAS-001
       ↓
CAP-MAP-COMPRAS-001
       ↓
PROC-MAP-COMPRAS-001
       ↓
SERV-MAP-COMPRAS-001
       ↓
SERV-COMPRAS-001...067
       ↓
UC-COMPRAS-001...
       ↓
HU-COMPRAS-001...
       ↓
RF-COMPRAS-001...
       ↓
RN-COMPRAS-001...
       ↓
CA-COMPRAS-001...
       ↓
TEST-COMPRAS-001...
```

---

# 39. Princípio de Não Duplicação

O SIGMUN deverá evitar a criação de serviços duplicados em diferentes domínios.

Quando um serviço possuir caráter corporativo, deverá ser avaliada sua centralização.

Exemplos:

* identidade;
* notificações;
* gestão documental;
* auditoria;
* assinatura;
* classificação da informação.

O domínio de Compras e Contratações deverá consumir esses serviços corporativos sempre que disponíveis.

---

# 40. Critérios de Conclusão

O Mapa de Serviços será considerado suficientemente definido quando:

* os serviços principais estiverem identificados;
* os consumidores estiverem identificados;
* os resultados estiverem definidos;
* os serviços estiverem relacionados aos processos;
* as capacidades estiverem relacionadas;
* os serviços corporativos estiverem identificados;
* serviços internos e externos estiverem diferenciados;
* requisitos de segurança forem considerados;
* transparência estiver contemplada;
* integrações relevantes estiverem identificadas;
* rastreabilidade estiver estabelecida.

---

# 41. Evolução

Este documento deverá evoluir conforme:

* novos processos forem identificados;
* novos serviços forem necessários;
* serviços forem consolidados;
* serviços corporativos forem criados;
* novas integrações forem implantadas;
* novas necessidades dos usuários forem identificadas;
* o modelo de negócio do Município evoluir.

---

# 42. Próximo Nível de Detalhamento

A partir deste mapa, os serviços deverão ser detalhados progressivamente em:

```text
Serviço
   ↓
Caso de Uso
   ↓
História de Usuário
   ↓
Requisito Funcional
   ↓
Regra de Negócio
   ↓
Especificação
   ↓
Critério de Aceitação
   ↓
Teste
```

---

# 43. Disposição Final

O **Mapa de Serviços – Gestão de Compras e Contratações** estabelece a camada intermediária entre os processos de negócio e a futura especificação funcional do SIGMUN.

A arquitetura de referência do domínio passa a ser:

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
CRITÉRIOS DE ACEITAÇÃO
   ↓
TESTES
```

Essa estrutura deverá garantir rastreabilidade desde a necessidade institucional até a implementação e validação da solução.

---

# Controle de Versões

| Versão | Data       | Descrição                                                                  |
| ------ | ---------- | -------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do Mapa de Serviços do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
