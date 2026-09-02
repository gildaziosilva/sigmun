# 006 – Histórias de Usuário – Gestão de Compras e Contratações

#### Histórias de Usuário – Gestão de Compras e Contratações

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
* 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
* 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
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

Este documento define as **Histórias de Usuário do Domínio de Gestão de Compras e Contratações** do SIGMUN.

As histórias de usuário representam necessidades dos atores do domínio sob a perspectiva do valor que esperam obter do sistema.

Elas serão utilizadas como base para a elaboração de:

* requisitos funcionais;
* regras de negócio;
* especificações;
* critérios de aceitação;
* testes;
* planejamento de desenvolvimento.

---

# 2. Padrão das Histórias de Usuário

As histórias seguirão preferencialmente o formato:

> **Como** [ator], **quero** [ação ou necessidade], **para** [benefício ou resultado].

Exemplo:

> Como servidor de uma unidade requisitante, quero registrar uma necessidade de compra, para que a demanda possa ser formalizada e encaminhada para análise.

---

# 3. Convenção de Identificação

As histórias utilizarão o padrão:

```text
HU-COMPRAS-XXX
```

Exemplo:

```text
HU-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida da história.

---

# 4. Relação com Casos de Uso

A rastreabilidade seguirá:

```text
SERV-COMPRAS
      ↓
UC-COMPRAS
      ↓
HU-COMPRAS
      ↓
RF-COMPRAS
      ↓
RN-COMPRAS
      ↓
CA-COMPRAS
      ↓
TEST-COMPRAS
```

Uma história poderá originar mais de um requisito funcional.

Um caso de uso poderá possuir várias histórias de usuário.

---

# 5. Histórias de Usuário – Planejamento

## HU-COMPRAS-001 – Planejar Contratações

**Caso de Uso:** `UC-COMPRAS-001`

**Como** gestor ou servidor responsável pelo planejamento,

**quero** registrar e organizar as contratações previstas,

**para** que o Município possa planejar suas aquisições de forma antecipada e coordenada.

---

## HU-COMPRAS-002 – Consolidar Necessidades

**Caso de Uso:** `UC-COMPRAS-002`

**Como** servidor da Unidade de Compras,

**quero** identificar e consolidar necessidades semelhantes,

**para** evitar duplicidade de demandas e aproveitar oportunidades de contratação conjunta.

---

## HU-COMPRAS-003 – Priorizar Contratações

**Caso de Uso:** `UC-COMPRAS-003`

**Como** gestor,

**quero** definir a prioridade das contratações planejadas,

**para** direcionar os recursos administrativos para as necessidades mais relevantes.

---

# 6. Histórias de Usuário – Necessidades e Requisições

## HU-COMPRAS-004 – Registrar Necessidade

**Caso de Uso:** `UC-COMPRAS-004`

**Como** servidor de uma unidade requisitante,

**quero** registrar uma necessidade de aquisição ou contratação,

**para** formalizar uma demanda administrativa.

---

## HU-COMPRAS-005 – Solicitar Compra ou Contratação

**Caso de Uso:** `UC-COMPRAS-005`

**Como** servidor de uma unidade requisitante,

**quero** solicitar uma compra ou contratação,

**para** encaminhar formalmente minha demanda para processamento.

---

## HU-COMPRAS-006 – Aprovar Requisição

**Caso de Uso:** `UC-COMPRAS-006`

**Como** gestor ou autoridade competente,

**quero** analisar uma requisição,

**para** decidir se a demanda deve prosseguir.

---

## HU-COMPRAS-007 – Acompanhar Requisição

**Caso de Uso:** `UC-COMPRAS-007`

**Como** solicitante,

**quero** acompanhar a situação da minha requisição,

**para** saber em que etapa ela se encontra e identificar eventuais pendências.

---

# 7. Histórias de Usuário – Especificação

## HU-COMPRAS-008 – Especificar Objeto

**Caso de Uso:** `UC-COMPRAS-008`

**Como** servidor responsável pela demanda,

**quero** especificar o objeto da contratação,

**para** definir claramente aquilo que deverá ser adquirido ou contratado.

---

## HU-COMPRAS-009 – Validar Especificação

**Caso de Uso:** `UC-COMPRAS-009`

**Como** responsável pela contratação,

**quero** validar a especificação do objeto,

**para** garantir que a demanda esteja suficientemente definida antes do prosseguimento.

---

# 8. Histórias de Usuário – Pesquisa de Preços

## HU-COMPRAS-010 – Registrar Pesquisa de Preços

**Caso de Uso:** `UC-COMPRAS-010`

**Como** servidor responsável pela pesquisa de preços,

**quero** registrar as fontes e valores pesquisados,

**para** documentar a formação da estimativa de preços.

---

## HU-COMPRAS-011 – Calcular Estimativa de Preço

**Caso de Uso:** `UC-COMPRAS-011`

**Como** servidor da Unidade de Compras,

**quero** obter uma estimativa de preço com base nos dados disponíveis,

**para** apoiar o planejamento e a instrução da contratação.

---

## HU-COMPRAS-012 – Consultar Histórico de Preços

**Caso de Uso:** `UC-COMPRAS-012`

**Como** servidor da Unidade de Compras,

**quero** consultar preços históricos,

**para** utilizar informações anteriores como referência na análise de novas contratações.

---

# 9. Histórias de Usuário – Processo de Contratação

## HU-COMPRAS-013 – Abrir Processo de Contratação

**Caso de Uso:** `UC-COMPRAS-013`

**Como** servidor responsável pelas compras,

**quero** abrir um processo de contratação,

**para** formalizar e organizar os atos relacionados à contratação.

---

## HU-COMPRAS-014 – Instruir Processo

**Caso de Uso:** `UC-COMPRAS-014`

**Como** servidor responsável pelo processo,

**quero** incluir e organizar os documentos necessários,

**para** manter o processo devidamente instruído.

---

## HU-COMPRAS-015 – Preparar Procedimento de Contratação

**Caso de Uso:** `UC-COMPRAS-015`

**Como** agente responsável pela contratação,

**quero** preparar o procedimento adequado,

**para** iniciar sua execução de forma organizada.

---

## HU-COMPRAS-016 – Conduzir Procedimento

**Caso de Uso:** `UC-COMPRAS-016`

**Como** agente responsável pela contratação,

**quero** registrar e acompanhar os atos do procedimento,

**para** manter o histórico e a integridade do processo.

---

## HU-COMPRAS-017 – Analisar e Julgar Propostas

**Caso de Uso:** `UC-COMPRAS-017`

**Como** agente responsável,

**quero** registrar a análise e o julgamento das propostas,

**para** documentar a decisão relacionada à seleção.

---

## HU-COMPRAS-018 – Registrar Decisão

**Caso de Uso:** `UC-COMPRAS-018`

**Como** autoridade competente,

**quero** registrar minha decisão no processo,

**para** formalizar o resultado da análise administrativa.

---

# 10. Histórias de Usuário – Fornecedores

## HU-COMPRAS-019 – Cadastrar Fornecedor

**Caso de Uso:** `UC-COMPRAS-019`

**Como** servidor autorizado,

**quero** registrar os dados de um fornecedor,

**para** permitir seu relacionamento com os processos de contratação.

---

## HU-COMPRAS-020 – Consultar Fornecedor

**Caso de Uso:** `UC-COMPRAS-020`

**Como** servidor autorizado,

**quero** consultar os dados cadastrais de um fornecedor,

**para** obter informações necessárias à análise de uma contratação.

---

## HU-COMPRAS-021 – Consultar Histórico do Fornecedor

**Caso de Uso:** `UC-COMPRAS-021`

**Como** gestor ou servidor autorizado,

**quero** consultar o histórico do fornecedor,

**para** avaliar seu relacionamento anterior com o Município.

---

# 11. Histórias de Usuário – Formalização

## HU-COMPRAS-022 – Formalizar Contratação

**Caso de Uso:** `UC-COMPRAS-022`

**Como** autoridade responsável,

**quero** formalizar a contratação,

**para** registrar oficialmente o resultado do processo.

---

## HU-COMPRAS-023 – Gerenciar Instrumento de Contratação

**Caso de Uso:** `UC-COMPRAS-023`

**Como** servidor responsável pela contratação,

**quero** gerenciar as informações do instrumento contratual,

**para** manter atualizados seus dados e documentos.

---

# 12. Histórias de Usuário – Gestão Contratual

## HU-COMPRAS-024 – Registrar Contrato

**Caso de Uso:** `UC-COMPRAS-024`

**Como** servidor responsável,

**quero** registrar um contrato no SIGMUN,

**para** manter o instrumento integrado à gestão municipal.

---

## HU-COMPRAS-025 – Acompanhar Contrato

**Caso de Uso:** `UC-COMPRAS-025`

**Como** gestor ou fiscal,

**quero** acompanhar a execução de um contrato,

**para** verificar sua situação e evolução.

---

## HU-COMPRAS-026 – Gerenciar Obrigações Contratuais

**Caso de Uso:** `UC-COMPRAS-026`

**Como** gestor de contrato,

**quero** registrar e acompanhar as obrigações contratuais,

**para** controlar responsabilidades e prazos.

---

## HU-COMPRAS-027 – Controlar Vigência

**Caso de Uso:** `UC-COMPRAS-027`

**Como** gestor de contrato,

**quero** acompanhar a vigência dos instrumentos,

**para** evitar perda de prazos importantes.

---

# 13. Histórias de Usuário – Fiscalização

## HU-COMPRAS-028 – Designar Fiscal

**Caso de Uso:** `UC-COMPRAS-028`

**Como** autoridade ou gestor competente,

**quero** designar o fiscal do contrato,

**para** formalizar a responsabilidade pelo acompanhamento da execução.

---

## HU-COMPRAS-029 – Registrar Fiscalização

**Caso de Uso:** `UC-COMPRAS-029`

**Como** fiscal de contrato,

**quero** registrar minhas atividades de fiscalização,

**para** documentar o acompanhamento da execução contratual.

---

## HU-COMPRAS-030 – Registrar Não Conformidade

**Caso de Uso:** `UC-COMPRAS-030`

**Como** fiscal de contrato,

**quero** registrar uma não conformidade,

**para** formalizar problemas identificados durante a execução.

---

## HU-COMPRAS-031 – Acompanhar Correção

**Caso de Uso:** `UC-COMPRAS-031`

**Como** fiscal de contrato,

**quero** acompanhar a correção de uma não conformidade,

**para** verificar se a situação foi efetivamente solucionada.

---

# 14. Histórias de Usuário – Ocorrências

## HU-COMPRAS-032 – Registrar Ocorrência Contratual

**Caso de Uso:** `UC-COMPRAS-032`

**Como** fiscal ou gestor,

**quero** registrar uma ocorrência contratual,

**para** manter histórico dos fatos relevantes da execução.

---

## HU-COMPRAS-033 – Acompanhar Ocorrência

**Caso de Uso:** `UC-COMPRAS-033`

**Como** gestor ou fiscal,

**quero** acompanhar o tratamento de uma ocorrência,

**para** garantir que as providências necessárias sejam realizadas.

---

# 15. Histórias de Usuário – Alterações Contratuais

## HU-COMPRAS-034 – Solicitar Alteração Contratual

**Caso de Uso:** `UC-COMPRAS-034`

**Como** gestor ou fiscal,

**quero** solicitar uma alteração contratual,

**para** formalizar uma necessidade identificada durante a execução.

---

## HU-COMPRAS-035 – Gerenciar Aditivo

**Caso de Uso:** `UC-COMPRAS-035`

**Como** servidor responsável,

**quero** registrar e acompanhar um aditivo contratual,

**para** manter o histórico e a formalização das alterações.

---

## HU-COMPRAS-036 – Gerenciar Prorrogação

**Caso de Uso:** `UC-COMPRAS-036`

**Como** gestor,

**quero** acompanhar e formalizar solicitações de prorrogação,

**para** garantir o tratamento adequado das alterações de vigência.

---

## HU-COMPRAS-037 – Gerenciar Reajuste ou Revisão

**Caso de Uso:** `UC-COMPRAS-037`

**Como** servidor responsável,

**quero** registrar e acompanhar reajustes ou revisões,

**para** manter os valores contratuais devidamente documentados.

---

# 16. Histórias de Usuário – Recebimento

## HU-COMPRAS-038 – Registrar Entrega

**Caso de Uso:** `UC-COMPRAS-038`

**Como** servidor responsável pelo recebimento,

**quero** registrar a entrega de bens ou serviços,

**para** documentar o cumprimento da obrigação de entrega.

---

## HU-COMPRAS-039 – Conferir Entrega

**Caso de Uso:** `UC-COMPRAS-039`

**Como** servidor responsável,

**quero** conferir uma entrega,

**para** verificar se aquilo que foi entregue corresponde ao contratado.

---

## HU-COMPRAS-040 – Registrar Aceite

**Caso de Uso:** `UC-COMPRAS-040`

**Como** responsável pelo recebimento,

**quero** registrar o aceite da entrega,

**para** formalizar sua conformidade.

---

## HU-COMPRAS-041 – Registrar Recusa ou Divergência

**Caso de Uso:** `UC-COMPRAS-041`

**Como** responsável pelo recebimento,

**quero** registrar uma recusa ou divergência,

**para** documentar problemas encontrados na entrega.

---

# 17. Histórias de Usuário – Encerramento

## HU-COMPRAS-042 – Encerrar Execução

**Caso de Uso:** `UC-COMPRAS-042`

**Como** gestor ou fiscal,

**quero** registrar o encerramento da execução,

**para** formalizar a conclusão do objeto contratado.

---

## HU-COMPRAS-043 – Encerrar Contrato

**Caso de Uso:** `UC-COMPRAS-043`

**Como** gestor ou autoridade competente,

**quero** encerrar o contrato,

**para** registrar formalmente o término de sua execução.

---

## HU-COMPRAS-044 – Arquivar Processo

**Caso de Uso:** `UC-COMPRAS-044`

**Como** servidor responsável pelo processo,

**quero** arquivar o processo concluído,

**para** preservar sua documentação e histórico.

---

# 18. Histórias de Usuário – Gestão Documental

## HU-COMPRAS-045 – Anexar Documento

**Caso de Uso:** `UC-COMPRAS-045`

**Como** usuário autorizado,

**quero** anexar documentos ao processo,

**para** manter sua documentação organizada e vinculada.

---

## HU-COMPRAS-046 – Consultar Documentos

**Caso de Uso:** `UC-COMPRAS-046`

**Como** usuário autorizado,

**quero** consultar documentos do processo,

**para** obter as informações necessárias ao desempenho das minhas atividades.

---

## HU-COMPRAS-047 – Gerenciar Evidências

**Caso de Uso:** `UC-COMPRAS-047`

**Como** fiscal, gestor ou auditor,

**quero** registrar e consultar evidências,

**para** comprovar fatos e atividades relacionadas ao processo ou contrato.

---

# 19. Histórias de Usuário – Transparência

## HU-COMPRAS-048 – Consultar Contratações

**Caso de Uso:** `UC-COMPRAS-048`

**Como** cidadão,

**quero** consultar informações públicas sobre contratações,

**para** acompanhar a utilização dos recursos públicos.

---

## HU-COMPRAS-049 – Consultar Contratos

**Caso de Uso:** `UC-COMPRAS-049`

**Como** cidadão,

**quero** consultar informações públicas sobre contratos,

**para** acompanhar as contratações realizadas pelo Município.

---

## HU-COMPRAS-050 – Consultar Processos

**Caso de Uso:** `UC-COMPRAS-050`

**Como** cidadão ou órgão de controle,

**quero** consultar informações publicáveis dos processos,

**para** acompanhar sua tramitação e resultados.

---

## HU-COMPRAS-051 – Exportar Dados Públicos

**Caso de Uso:** `UC-COMPRAS-051`

**Como** cidadão ou consumidor de dados públicos,

**quero** exportar informações disponibilizadas pelo Município,

**para** analisá-las e reutilizá-las conforme permitido.

---

# 20. Histórias de Usuário – Controle e Auditoria

## HU-COMPRAS-052 – Consultar Trilha de Auditoria

**Caso de Uso:** `UC-COMPRAS-052`

**Como** auditor ou controlador interno,

**quero** consultar a trilha de auditoria,

**para** verificar as ações realizadas no sistema.

---

## HU-COMPRAS-053 – Executar Controle

**Caso de Uso:** `UC-COMPRAS-053`

**Como** servidor do Controle Interno,

**quero** realizar procedimentos de controle,

**para** avaliar a regularidade e conformidade dos processos.

---

## HU-COMPRAS-054 – Registrar Achado de Auditoria

**Caso de Uso:** `UC-COMPRAS-054`

**Como** auditor,

**quero** registrar um achado de auditoria,

**para** documentar situações que demandem análise ou providência.

---

## HU-COMPRAS-055 – Acompanhar Recomendação

**Caso de Uso:** `UC-COMPRAS-055`

**Como** servidor do Controle Interno,

**quero** acompanhar recomendações de auditoria,

**para** verificar sua implementação.

---

# 21. Histórias de Usuário – Indicadores

## HU-COMPRAS-056 – Consultar Indicadores

**Caso de Uso:** `UC-COMPRAS-056`

**Como** gestor,

**quero** consultar indicadores de compras e contratações,

**para** acompanhar o desempenho do domínio.

---

## HU-COMPRAS-057 – Gerar Relatório Gerencial

**Caso de Uso:** `UC-COMPRAS-057`

**Como** gestor,

**quero** gerar relatórios gerenciais,

**para** apoiar a tomada de decisões.

---

## HU-COMPRAS-058 – Consultar Painel Gerencial

**Caso de Uso:** `UC-COMPRAS-058`

**Como** gestor,

**quero** consultar um painel consolidado,

**para** visualizar rapidamente a situação das compras e contratações.

---

# 22. Histórias de Usuário – Alertas e Notificações

## HU-COMPRAS-059 – Gerenciar Alertas

**Caso de Uso:** `UC-COMPRAS-059`

**Como** gestor,

**quero** acompanhar alertas relacionados às contratações,

**para** agir antecipadamente diante de prazos, pendências ou ocorrências.

---

## HU-COMPRAS-060 – Receber Notificação

**Caso de Uso:** `UC-COMPRAS-060`

**Como** usuário do SIGMUN,

**quero** receber notificações relacionadas às minhas responsabilidades,

**para** tomar conhecimento de eventos ou pendências relevantes.

---

# 23. Histórias de Usuário – Integrações

## HU-COMPRAS-061 – Integrar com Orçamento

**Caso de Uso:** `UC-COMPRAS-061`

**Como** gestor ou servidor responsável,

**quero** que as informações de compras sejam integradas ao orçamento,

**para** evitar duplicidade de lançamentos e melhorar a consistência das informações.

---

## HU-COMPRAS-062 – Integrar com Financeiro

**Caso de Uso:** `UC-COMPRAS-062`

**Como** servidor responsável,

**quero** integrar informações de contratos e execução ao sistema financeiro,

**para** manter os dados financeiros sincronizados.

---

## HU-COMPRAS-063 – Integrar com Contabilidade

**Caso de Uso:** `UC-COMPRAS-063`

**Como** servidor da área contábil,

**quero** receber informações relacionadas às contratações,

**para** apoiar os registros e controles contábeis.

---

## HU-COMPRAS-064 – Integrar com Patrimônio

**Caso de Uso:** `UC-COMPRAS-064`

**Como** servidor responsável pelo patrimônio,

**quero** receber informações sobre bens adquiridos,

**para** manter o cadastro patrimonial atualizado.

---

## HU-COMPRAS-065 – Integrar com Almoxarifado

**Caso de Uso:** `UC-COMPRAS-065`

**Como** servidor do almoxarifado,

**quero** receber informações sobre materiais adquiridos,

**para** facilitar o recebimento e controle dos estoques.

---

## HU-COMPRAS-066 – Integrar com Gestão Documental

**Caso de Uso:** `UC-COMPRAS-066`

**Como** usuário do SIGMUN,

**quero** que os documentos dos processos estejam integrados à gestão documental,

**para** garantir organização, preservação e acesso controlado aos documentos.

---

## HU-COMPRAS-067 – Integrar com Transparência

**Caso de Uso:** `UC-COMPRAS-067`

**Como** responsável pela transparência,

**quero** que as informações publicáveis sejam disponibilizadas automaticamente,

**para** reduzir retrabalho e melhorar a transparência das contratações.

---

# 24. Critérios Gerais das Histórias

As histórias de usuário deverão ser consideradas candidatas à implementação somente após serem refinadas com:

* requisitos funcionais;
* regras de negócio;
* critérios de aceitação;
* requisitos não funcionais;
* dependências;
* dados necessários;
* integrações;
* permissões;
* impactos nos demais domínios.

---

# 25. Critérios de Aceitação

Os critérios de aceitação não serão detalhados integralmente neste documento.

Eles serão especificados no artefato:

`Criterrios-de-Aceitacao.md`

ou, para o domínio:

`011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md`

A estrutura recomendada será:

```text
História
    ↓
Critério de Aceitação
    ↓
Cenário
    ↓
Dado
    ↓
Quando
    ↓
Então
```

---

# 26. Exemplo de Refinamento

### HU-COMPRAS-005

**Como** servidor de uma unidade requisitante,

**quero** solicitar uma compra ou contratação,

**para** encaminhar formalmente minha demanda para processamento.

Essa história poderá gerar:

```text
HU-COMPRAS-005
      ↓
RF-COMPRAS-001 – Registrar requisição
RF-COMPRAS-002 – Informar itens
RF-COMPRAS-003 – Informar quantidades
RF-COMPRAS-004 – Anexar documentos
RF-COMPRAS-005 – Submeter requisição
      ↓
RN-COMPRAS-001...
      ↓
CA-COMPRAS-001...
      ↓
TEST-COMPRAS-001...
```

---

# 27. Priorização

As histórias deverão ser posteriormente classificadas conforme sua prioridade.

Sugestão:

| Código | Significado            |
| ------ | ---------------------- |
| P0     | Essencial / bloqueante |
| P1     | Alta                   |
| P2     | Média                  |
| P3     | Baixa                  |

A prioridade deverá ser definida considerando:

* obrigatoriedade legal;
* impacto operacional;
* risco;
* quantidade de usuários;
* dependências;
* valor público;
* urgência;
* complexidade;
* capacidade de implementação.

---

# 28. Dependências

As histórias poderão possuir dependências entre si.

Exemplo:

```text
HU-COMPRAS-004
Registrar Necessidade
       ↓
HU-COMPRAS-005
Solicitar Compra
       ↓
HU-COMPRAS-006
Aprovar Requisição
       ↓
HU-COMPRAS-013
Abrir Processo
```

Essas dependências deverão ser registradas posteriormente na matriz de rastreabilidade.

---

# 29. Histórias Transversais

Algumas necessidades não pertencem exclusivamente ao domínio.

Exemplos:

* autenticação;
* autorização;
* notificações;
* assinatura;
* gestão documental;
* auditoria;
* identidade;
* classificação da informação;
* integração.

Quando houver serviço corporativo equivalente, o domínio deverá reutilizá-lo em vez de criar uma implementação paralela.

---

# 30. Histórias para Operação Móvel

As atividades de campo deverão considerar histórias específicas quando necessário.

Exemplo:

> Como fiscal de contrato em atividade de campo, quero registrar uma fiscalização mesmo sem conexão com a internet, para que eu possa documentar a execução no local e sincronizar os dados posteriormente.

Essa necessidade deverá ser posteriormente refinada em requisitos relacionados à arquitetura **Offline First**.

---

# 31. Histórias e Transparência

As histórias relacionadas à transparência deverão considerar:

* publicidade;
* classificação da informação;
* proteção de dados pessoais;
* segurança;
* disponibilidade;
* reutilização de dados;
* rastreabilidade da origem.

---

# 32. Histórias e Valor Público

As histórias não deverão ser avaliadas apenas pelo benefício ao usuário interno.

Sempre que aplicável, deverá ser considerado o impacto para:

* cidadão;
* fornecedor;
* administração pública;
* controle interno;
* órgãos de controle;
* sociedade.

---

# 33. Matriz de Rastreabilidade

| História       | Caso de Uso    | Serviço          |
| -------------- | -------------- | ---------------- |
| HU-COMPRAS-001 | UC-COMPRAS-001 | SERV-COMPRAS-001 |
| HU-COMPRAS-002 | UC-COMPRAS-002 | SERV-COMPRAS-002 |
| HU-COMPRAS-003 | UC-COMPRAS-003 | SERV-COMPRAS-003 |
| HU-COMPRAS-004 | UC-COMPRAS-004 | SERV-COMPRAS-004 |
| HU-COMPRAS-005 | UC-COMPRAS-005 | SERV-COMPRAS-005 |
| HU-COMPRAS-006 | UC-COMPRAS-006 | SERV-COMPRAS-006 |
| HU-COMPRAS-007 | UC-COMPRAS-007 | SERV-COMPRAS-007 |
| HU-COMPRAS-008 | UC-COMPRAS-008 | SERV-COMPRAS-008 |
| HU-COMPRAS-009 | UC-COMPRAS-009 | SERV-COMPRAS-009 |
| HU-COMPRAS-010 | UC-COMPRAS-010 | SERV-COMPRAS-010 |
| HU-COMPRAS-011 | UC-COMPRAS-011 | SERV-COMPRAS-011 |
| HU-COMPRAS-012 | UC-COMPRAS-012 | SERV-COMPRAS-012 |
| HU-COMPRAS-013 | UC-COMPRAS-013 | SERV-COMPRAS-013 |
| HU-COMPRAS-014 | UC-COMPRAS-014 | SERV-COMPRAS-014 |
| HU-COMPRAS-015 | UC-COMPRAS-015 | SERV-COMPRAS-015 |
| HU-COMPRAS-016 | UC-COMPRAS-016 | SERV-COMPRAS-016 |
| HU-COMPRAS-017 | UC-COMPRAS-017 | SERV-COMPRAS-017 |
| HU-COMPRAS-018 | UC-COMPRAS-018 | SERV-COMPRAS-018 |
| HU-COMPRAS-019 | UC-COMPRAS-019 | SERV-COMPRAS-019 |
| HU-COMPRAS-020 | UC-COMPRAS-020 | SERV-COMPRAS-020 |
| HU-COMPRAS-021 | UC-COMPRAS-021 | SERV-COMPRAS-021 |
| HU-COMPRAS-022 | UC-COMPRAS-022 | SERV-COMPRAS-022 |
| HU-COMPRAS-023 | UC-COMPRAS-023 | SERV-COMPRAS-023 |
| HU-COMPRAS-024 | UC-COMPRAS-024 | SERV-COMPRAS-024 |
| HU-COMPRAS-025 | UC-COMPRAS-025 | SERV-COMPRAS-025 |
| HU-COMPRAS-026 | UC-COMPRAS-026 | SERV-COMPRAS-026 |
| HU-COMPRAS-027 | UC-COMPRAS-027 | SERV-COMPRAS-027 |
| HU-COMPRAS-028 | UC-COMPRAS-028 | SERV-COMPRAS-028 |
| HU-COMPRAS-029 | UC-COMPRAS-029 | SERV-COMPRAS-029 |
| HU-COMPRAS-030 | UC-COMPRAS-030 | SERV-COMPRAS-030 |
| HU-COMPRAS-031 | UC-COMPRAS-031 | SERV-COMPRAS-031 |
| HU-COMPRAS-032 | UC-COMPRAS-032 | SERV-COMPRAS-032 |
| HU-COMPRAS-033 | UC-COMPRAS-033 | SERV-COMPRAS-033 |
| HU-COMPRAS-034 | UC-COMPRAS-034 | SERV-COMPRAS-034 |
| HU-COMPRAS-035 | UC-COMPRAS-035 | SERV-COMPRAS-035 |
| HU-COMPRAS-036 | UC-COMPRAS-036 | SERV-COMPRAS-036 |
| HU-COMPRAS-037 | UC-COMPRAS-037 | SERV-COMPRAS-037 |
| HU-COMPRAS-038 | UC-COMPRAS-038 | SERV-COMPRAS-038 |
| HU-COMPRAS-039 | UC-COMPRAS-039 | SERV-COMPRAS-039 |
| HU-COMPRAS-040 | UC-COMPRAS-040 | SERV-COMPRAS-040 |
| HU-COMPRAS-041 | UC-COMPRAS-041 | SERV-COMPRAS-041 |
| HU-COMPRAS-042 | UC-COMPRAS-042 | SERV-COMPRAS-042 |
| HU-COMPRAS-043 | UC-COMPRAS-043 | SERV-COMPRAS-043 |
| HU-COMPRAS-044 | UC-COMPRAS-044 | SERV-COMPRAS-044 |
| HU-COMPRAS-045 | UC-COMPRAS-045 | SERV-COMPRAS-045 |
| HU-COMPRAS-046 | UC-COMPRAS-046 | SERV-COMPRAS-046 |
| HU-COMPRAS-047 | UC-COMPRAS-047 | SERV-COMPRAS-047 |
| HU-COMPRAS-048 | UC-COMPRAS-048 | SERV-COMPRAS-048 |
| HU-COMPRAS-049 | UC-COMPRAS-049 | SERV-COMPRAS-049 |
| HU-COMPRAS-050 | UC-COMPRAS-050 | SERV-COMPRAS-050 |
| HU-COMPRAS-051 | UC-COMPRAS-051 | SERV-COMPRAS-051 |
| HU-COMPRAS-052 | UC-COMPRAS-052 | SERV-COMPRAS-052 |
| HU-COMPRAS-053 | UC-COMPRAS-053 | SERV-COMPRAS-053 |
| HU-COMPRAS-054 | UC-COMPRAS-054 | SERV-COMPRAS-054 |
| HU-COMPRAS-055 | UC-COMPRAS-055 | SERV-COMPRAS-055 |
| HU-COMPRAS-056 | UC-COMPRAS-056 | SERV-COMPRAS-056 |
| HU-COMPRAS-057 | UC-COMPRAS-057 | SERV-COMPRAS-057 |
| HU-COMPRAS-058 | UC-COMPRAS-058 | SERV-COMPRAS-058 |
| HU-COMPRAS-059 | UC-COMPRAS-059 | SERV-COMPRAS-059 |
| HU-COMPRAS-060 | UC-COMPRAS-060 | SERV-COMPRAS-060 |
| HU-COMPRAS-061 | UC-COMPRAS-061 | SERV-COMPRAS-061 |
| HU-COMPRAS-062 | UC-COMPRAS-062 | SERV-COMPRAS-062 |
| HU-COMPRAS-063 | UC-COMPRAS-063 | SERV-COMPRAS-063 |
| HU-COMPRAS-064 | UC-COMPRAS-064 | SERV-COMPRAS-064 |
| HU-COMPRAS-065 | UC-COMPRAS-065 | SERV-COMPRAS-065 |
| HU-COMPRAS-066 | UC-COMPRAS-066 | SERV-COMPRAS-066 |
| HU-COMPRAS-067 | UC-COMPRAS-067 | SERV-COMPRAS-067 |

---

# 34. Refinamento Futuro

As histórias deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, uma história poderá:

* ser dividida em várias histórias;
* ser combinada com outra;
* ser descartada;
* ser transformada em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos requisitos;
* gerar múltiplos critérios de aceitação.

Nenhuma história deverá ser considerada tecnicamente implementada apenas pela sua existência neste documento.

---

# 35. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`HU-MAP-COMPRAS-001`

**Tipo:**

Mapa de Histórias de Usuário.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

---

# 36. Próximo Artefato

O próximo artefato recomendado é:

`007-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md`

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
007-Requisitos Funcionais
      ↓
008-Requisitos Não Funcionais
      ↓
009-Regras de Negócio
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
```

---

# 37. Controle de Versões

| Versão | Data       | Descrição                                                                       |
| ------ | ---------- | ------------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação das Histórias de Usuário do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
