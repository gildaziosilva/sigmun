# 000 – Domínio de Gestão de Compras e Contratações

#### Domínio de Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RASTREABILIDADE.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md
* Casos-de-Uso.md
* Historias-de-Usuario.md
* Regras-de-Negocio.md
* Requisitos-Funcionais.md
* Requisitos-Nao-Funcionais.md
* Especificacoes.md
* Criterios-de-Aceitacao.md
* Matriz-de-Rastreabilidade.md

---

# 1. Finalidade

O **Domínio de Gestão de Compras e Contratações** representa o conjunto de capacidades, processos, serviços, informações, regras e interações relacionadas ao planejamento, formalização, execução, acompanhamento e encerramento das compras e contratações realizadas pela Administração Pública Municipal.

Este domínio será utilizado como **domínio-piloto de implementação do SIGMUN**, permitindo validar a aplicação integrada dos modelos corporativos de negócio, requisitos, dados, arquitetura, segurança, experiência do usuário, integração e qualidade.

---

# 2. Objetivos do Domínio

São objetivos do domínio:

* estruturar o processo municipal de compras e contratações;
* promover padronização dos procedimentos;
* reduzir retrabalho;
* reduzir duplicidade de informações;
* aumentar a rastreabilidade dos processos;
* centralizar informações relevantes;
* apoiar o planejamento das contratações;
* apoiar a formalização dos processos;
* permitir acompanhamento das etapas;
* melhorar a transparência;
* apoiar controles internos;
* disponibilizar informações para gestão;
* permitir geração de indicadores;
* preservar documentos e evidências;
* integrar informações com outros domínios do SIGMUN.

---

# 3. Visão do Domínio

O domínio deverá permitir que uma necessidade administrativa seja transformada em uma contratação formalmente instruída, acompanhada e encerrada.

Visão conceitual:

```text
Necessidade
    ↓
Planejamento
    ↓
Solicitação
    ↓
Instrução
    ↓
Análise
    ↓
Contratação
    ↓
Formalização
    ↓
Execução
    ↓
Fiscalização
    ↓
Encerramento
    ↓
Avaliação
    ↓
Informação Gerencial
```

---

# 4. Escopo

O domínio compreende, em nível corporativo:

* planejamento de compras;
* identificação de necessidades;
* requisições de compras;
* especificação de objetos;
* estimativas;
* formação de processos;
* instrução processual;
* análise e validação;
* procedimentos de contratação;
* gestão de fornecedores;
* formalização;
* contratos;
* instrumentos relacionados;
* acompanhamento da execução;
* fiscalização;
* recebimento;
* encerramento;
* registros documentais;
* informações gerenciais;
* indicadores;
* trilhas de auditoria;
* integrações com outros domínios.

O detalhamento de cada processo será realizado nos respectivos artefatos de processos e requisitos.

---

# 5. Fora do Escopo Inicial

Não fazem parte da primeira definição detalhada deste domínio, salvo quando necessários para integração:

* contabilidade completa;
* execução orçamentária completa;
* gestão financeira completa;
* gestão patrimonial completa;
* gestão de estoque completa;
* gestão de recursos humanos;
* folha de pagamento;
* gestão tributária;
* gestão de obras completa.

Esses elementos poderão possuir domínios próprios.

O domínio de Compras e Contratações deverá, entretanto, possuir **integrações bem definidas** com esses domínios quando houver dependência de informação ou processo.

---

# 6. Fronteiras do Domínio

O domínio começa quando uma necessidade de aquisição ou contratação é identificada e formalmente encaminhada para tratamento administrativo.

O domínio termina quando:

* a contratação é encerrada;
* os registros necessários foram consolidados;
* os documentos foram preservados;
* as obrigações relacionadas foram encaminhadas aos domínios responsáveis;
* os indicadores e informações aplicáveis foram disponibilizados.

As fronteiras poderão ser refinadas durante o levantamento detalhado dos processos.

---

# 7. Capacidades Principais

O domínio deverá contemplar, entre outras, as seguintes capacidades:

## 7.1 Planejamento de Contratações

Capacidade de organizar e acompanhar necessidades futuras de aquisição e contratação.

---

## 7.2 Gestão de Necessidades

Capacidade de registrar, justificar e encaminhar necessidades administrativas.

---

## 7.3 Gestão de Requisições

Capacidade de registrar solicitações de aquisição ou contratação.

---

## 7.4 Especificação de Objetos

Capacidade de estruturar as informações necessárias à caracterização do objeto.

---

## 7.5 Pesquisa e Estimativa de Preços

Capacidade de registrar e tratar informações utilizadas para estimativa de preços.

---

## 7.6 Gestão de Processos de Contratação

Capacidade de organizar e acompanhar a instrução dos processos.

---

## 7.7 Gestão de Fornecedores

Capacidade de utilizar informações cadastrais e documentais de fornecedores.

---

## 7.8 Gestão dos Procedimentos de Contratação

Capacidade de apoiar a condução dos procedimentos aplicáveis.

---

## 7.9 Gestão de Contratos

Capacidade de registrar, acompanhar e controlar contratos e instrumentos relacionados.

---

## 7.10 Gestão da Execução Contratual

Capacidade de acompanhar a execução dos objetos contratados.

---

## 7.11 Fiscalização

Capacidade de registrar informações relacionadas à fiscalização e acompanhamento.

---

## 7.12 Recebimento

Capacidade de registrar o recebimento dos bens, serviços ou objetos contratados.

---

## 7.13 Gestão Documental

Capacidade de manter documentos e evidências vinculados aos processos.

---

## 7.14 Transparência e Prestação de Informações

Capacidade de disponibilizar informações para os públicos autorizados e para mecanismos de transparência.

---

## 7.15 Indicadores e Gestão

Capacidade de produzir informações gerenciais sobre compras e contratações.

---

# 8. Atores do Domínio

Os atores deverão ser detalhados posteriormente no **Mapa de Atores** e nos casos de uso.

Entre os atores potenciais estão:

* unidade requisitante;
* servidor solicitante;
* gestor da unidade;
* unidade responsável por compras;
* agente responsável pelo procedimento;
* equipe responsável pela contratação;
* autoridade competente;
* setor jurídico;
* controle interno;
* setor financeiro;
* setor contábil;
* fiscal do contrato;
* gestor do contrato;
* fornecedor;
* órgão de controle;
* cidadão;
* administrador do sistema.

A identificação definitiva dos atores deverá ocorrer durante o levantamento dos processos.

---

# 9. Informações Principais

O domínio poderá trabalhar com informações relacionadas a:

* necessidade;
* requisição;
* item;
* objeto;
* especificação;
* estimativa;
* fornecedor;
* proposta;
* processo;
* procedimento;
* decisão;
* documento;
* contrato;
* instrumento contratual;
* empenho ou referência financeira;
* entrega;
* fiscalização;
* ocorrência;
* recebimento;
* encerramento.

Essas informações deverão ser detalhadas no modelo corporativo de dados.

---

# 10. Entidades Conceituais Iniciais

Como ponto de partida, são identificadas as seguintes entidades conceituais:

```text
Necessidade
Requisição
Objeto
Item
Especificação
Estimativa
Fornecedor
Proposta
Processo
Procedimento
Documento
Contrato
Fiscalização
Entrega
Recebimento
Ocorrência
```

Essa lista é inicial e não representa ainda o modelo lógico ou físico de dados.

---

# 11. Processos Principais

Os processos deverão ser detalhados no **Mapa de Processos**.

Como visão inicial:

```text
PROC-COMPRAS-001 – Planejamento de Contratações

PROC-COMPRAS-002 – Registro de Necessidade

PROC-COMPRAS-003 – Requisição de Compra ou Contratação

PROC-COMPRAS-004 – Especificação do Objeto

PROC-COMPRAS-005 – Estimativa de Preços

PROC-COMPRAS-006 – Instrução do Processo

PROC-COMPRAS-007 – Procedimento de Contratação

PROC-COMPRAS-008 – Formalização da Contratação

PROC-COMPRAS-009 – Gestão do Contrato

PROC-COMPRAS-010 – Fiscalização da Execução

PROC-COMPRAS-011 – Recebimento

PROC-COMPRAS-012 – Encerramento da Contratação
```

A nomenclatura e a decomposição deverão ser validadas durante o mapeamento detalhado.

---

# 12. Serviços do Domínio

Os serviços serão detalhados no **Mapa de Serviços**.

Exemplos iniciais:

```text
SERV-COMPRAS-001 – Planejamento de Contratação

SERV-COMPRAS-002 – Solicitação de Compra

SERV-COMPRAS-003 – Formação de Processo

SERV-COMPRAS-004 – Pesquisa de Preços

SERV-COMPRAS-005 – Gestão do Procedimento

SERV-COMPRAS-006 – Gestão de Contrato

SERV-COMPRAS-007 – Fiscalização Contratual

SERV-COMPRAS-008 – Recebimento

SERV-COMPRAS-009 – Consulta de Contratações

SERV-COMPRAS-010 – Indicadores de Compras e Contratações
```

Os serviços deverão ser validados contra os processos e necessidades dos usuários.

---

# 13. Casos de Uso

Os casos de uso serão definidos posteriormente.

Exemplos iniciais:

```text
UC-COMPRAS-001 – Registrar Necessidade

UC-COMPRAS-002 – Criar Requisição

UC-COMPRAS-003 – Elaborar Especificação

UC-COMPRAS-004 – Registrar Pesquisa de Preços

UC-COMPRAS-005 – Instruir Processo

UC-COMPRAS-006 – Conduzir Procedimento

UC-COMPRAS-007 – Formalizar Contratação

UC-COMPRAS-008 – Registrar Contrato

UC-COMPRAS-009 – Acompanhar Execução

UC-COMPRAS-010 – Registrar Fiscalização

UC-COMPRAS-011 – Registrar Recebimento

UC-COMPRAS-012 – Encerrar Contratação
```

Esses casos de uso são hipóteses iniciais e deverão ser validados.

---

# 14. Regras de Negócio

O domínio deverá possuir regras específicas relacionadas a:

* autorização;
* competência;
* etapas;
* documentos obrigatórios;
* validações;
* fornecedores;
* procedimentos;
* contratos;
* prazos;
* fiscalização;
* recebimento;
* encerramento;
* transparência;
* auditoria.

As regras não deverão ser inventadas antecipadamente.

Deverão ser levantadas a partir:

* legislação aplicável;
* normas municipais;
* regulamentos;
* processos reais;
* políticas;
* decisões administrativas;
* práticas operacionais validadas.

---

# 15. Requisitos

Os requisitos do domínio serão derivados dos processos, serviços, casos de uso, regras e necessidades identificadas.

A cadeia deverá seguir:

```text
Processo
   ↓
Serviço
   ↓
Caso de Uso
   ↓
Regra de Negócio
   ↓
Requisito
```

Os requisitos deverão ser registrados nos documentos corporativos correspondentes.

---

# 16. Requisitos Não Funcionais

O domínio deverá observar os requisitos corporativos aplicáveis relacionados a:

* segurança;
* controle de acesso;
* auditoria;
* disponibilidade;
* desempenho;
* integridade;
* rastreabilidade;
* interoperabilidade;
* acessibilidade;
* usabilidade;
* privacidade;
* proteção de dados;
* continuidade;
* observabilidade.

Os requisitos específicos deverão ser definidos após o conhecimento dos processos.

---

# 17. Gestão Documental

Os documentos relacionados às compras e contratações deverão possuir:

* identificação;
* classificação;
* versionamento;
* autoria;
* data;
* vínculo ao processo;
* integridade;
* controle de acesso;
* histórico;
* retenção;
* possibilidade de auditoria.

A solução deverá evitar documentos sem contexto ou vínculo processual.

---

# 18. Segurança

O domínio deverá observar o princípio:

> **Segurança por princípio.**

Deverão ser considerados:

* autenticação;
* autorização;
* segregação de funções;
* controle de privilégios;
* registro de operações;
* trilhas de auditoria;
* proteção de documentos;
* proteção de dados;
* monitoramento.

---

# 19. Segregação de Funções

Quando aplicável, o domínio deverá impedir ou controlar conflitos entre funções.

Exemplos conceituais:

```text
Solicitar
    ≠
Aprovar
    ≠
Executar
    ≠
Fiscalizar
```

As regras efetivas de segregação deverão ser definidas com base nas normas aplicáveis e nos processos municipais.

---

# 20. Integrações

O domínio poderá possuir integrações com:

* orçamento;
* contabilidade;
* financeiro;
* patrimônio;
* almoxarifado;
* gestão documental;
* cadastro único municipal;
* gestão de fornecedores;
* identidade;
* notificações;
* portal de transparência;
* sistemas externos;
* órgãos de controle.

As integrações serão detalhadas na arquitetura de integração.

---

# 21. Cadastro Único

Sempre que aplicável, o domínio deverá utilizar informações provenientes do **Cadastro Único Municipal**, evitando duplicidade cadastral.

Exemplos:

```text
Pessoa
Organização
Fornecedor
Unidade Administrativa
Servidor
```

A modelagem definitiva deverá respeitar a arquitetura corporativa de dados.

---

# 22. Identidade e Acesso

O domínio deverá utilizar a arquitetura corporativa de identidade do SIGMUN.

As permissões deverão considerar:

* usuário;
* papel;
* função;
* unidade administrativa;
* responsabilidade;
* processo;
* nível de acesso;
* segregação de funções.

---

# 23. Transparência

O domínio deverá observar o princípio:

> **Transparência por padrão.**

Informações públicas deverão ser disponibilizadas conforme as políticas de classificação da informação e as regras aplicáveis.

Informações restritas deverão permanecer protegidas.

---

# 24. Auditoria

Operações relevantes deverão gerar trilha de auditoria.

A auditoria deverá permitir identificar, conforme aplicabilidade:

* quem;
* quando;
* o quê;
* onde;
* operação realizada;
* estado anterior;
* estado posterior;
* justificativa.

---

# 25. Indicadores

O domínio deverá produzir informações para indicadores relacionados a:

* quantidade de contratações;
* valores;
* prazos;
* tempo de processamento;
* atrasos;
* economia;
* fornecedores;
* contratos vigentes;
* contratos encerrados;
* execução;
* ocorrências;
* concentração;
* desempenho.

Os indicadores definitivos deverão ser definidos posteriormente.

---

# 26. Experiência do Usuário

A experiência deverá privilegiar:

* simplicidade;
* clareza;
* redução de etapas desnecessárias;
* orientação ao usuário;
* reutilização de informações;
* preenchimento assistido;
* validações antecipadas;
* acessibilidade;
* responsividade;
* transparência do status do processo.

---

# 27. Princípio "Informar Uma Vez"

Sempre que uma informação já existir no SIGMUN, o usuário não deverá ser obrigado a digitá-la novamente sem justificativa.

Exemplo:

```text
Cadastro do fornecedor
        ↓
Processo
        ↓
Contrato
        ↓
Fiscalização
```

As informações deverão ser reutilizadas quando apropriado.

---

# 28. Princípio "Processo Antes da Tela"

O domínio será modelado prioritariamente a partir dos processos e serviços.

Não será adotada abordagem de iniciar o projeto simplesmente pela criação de telas.

A sequência preferencial será:

```text
Necessidade
   ↓
Processo
   ↓
Serviço
   ↓
Caso de Uso
   ↓
Requisito
   ↓
Experiência
   ↓
Interface
```

---

# 29. Princípio "Documento como Evidência"

Documentos não deverão ser tratados apenas como anexos.

Quando aplicável, deverão possuir contexto dentro do processo.

```text
Documento
    ↓
Processo
    ↓
Etapa
    ↓
Responsável
    ↓
Finalidade
```

---

# 30. Princípio "Rastreabilidade Ponta a Ponta"

Cada requisito relevante deverá possuir rastreabilidade até sua origem e, quando aplicável, até sua validação.

```text
Necessidade
 ↓
Processo
 ↓
Serviço
 ↓
Requisito
 ↓
Implementação
 ↓
Teste
 ↓
Evidência
```

---

# 31. Critérios de Sucesso do Domínio

O domínio-piloto será considerado estruturalmente bem definido quando:

* os processos principais estiverem identificados;
* os atores estiverem identificados;
* as capacidades estiverem definidas;
* os serviços estiverem relacionados aos processos;
* os casos de uso estiverem relacionados aos serviços;
* as regras estiverem relacionadas aos requisitos;
* os requisitos estiverem rastreáveis;
* os critérios de aceitação estiverem definidos;
* os testes estiverem relacionados;
* as integrações estiverem identificadas;
* os dados principais estiverem identificados.

---

# 32. Critérios para Implementação

A implementação deverá ocorrer somente após o nível adequado de definição do processo e dos requisitos.

A profundidade necessária dependerá da criticidade e complexidade da funcionalidade.

Não será necessário produzir documentação excessiva para funcionalidades simples.

---

# 33. Estratégia de Implementação do Domínio

A implementação será incremental.

Sugestão inicial:

```text
Fase 1
Planejamento e Necessidade

        ↓

Fase 2
Requisição e Instrução

        ↓

Fase 3
Procedimento de Contratação

        ↓

Fase 4
Formalização

        ↓

Fase 5
Gestão Contratual

        ↓

Fase 6
Fiscalização e Recebimento

        ↓

Fase 7
Indicadores e Inteligência
```

---

# 34. Domínio como Projeto-Piloto

Este domínio será utilizado para validar:

* modelo de negócio;
* arquitetura corporativa;
* framework de requisitos;
* modelo de dados;
* arquitetura de software;
* arquitetura de integração;
* segurança;
* UX;
* testes;
* rastreabilidade;
* governança.

Os aprendizados deverão retroalimentar os modelos corporativos.

---

# 35. Relação com o Mapa Mestre

Este domínio deverá manter seus artefatos registrados no:

**`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`**

A cadeia inicial deverá evoluir para:

```text
DOM-COMPRAS
      ↓
CAP-COMPRAS
      ↓
PROC-COMPRAS
      ↓
SERV-COMPRAS
      ↓
UC-COMPRAS
      ↓
HU-COMPRAS
      ↓
RN-COMPRAS
      ↓
RF-COMPRAS
      ↓
RNF-COMPRAS
      ↓
ESP-COMPRAS
      ↓
CA-COMPRAS
      ↓
TST-COMPRAS
      ↓
EVD-COMPRAS
```

---

# 36. Próximos Artefatos

Após a aprovação deste documento, deverão ser produzidos progressivamente:

1. `001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md`
2. `002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md`
3. `003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md`
4. `004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md`
5. `005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md`
6. `006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md`
7. `007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md`
8. `008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md`
9. `009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md`
10. `010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md`
11. `011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md`
12. `012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md`

Os nomes poderão ser ajustados caso a estrutura definitiva do diretório do domínio adote outra convenção.

---

# 37. Governança do Domínio

O domínio deverá ser governado de acordo com os princípios e políticas corporativas do SIGMUN.

Alterações que afetem:

* arquitetura;
* segurança;
* dados;
* integrações;
* regras corporativas;
* requisitos transversais;
* governança;

deverão ser avaliadas nos respectivos fóruns e mecanismos de governança.

---

# 38. Evolução do Domínio

A primeira versão deste documento representa uma **definição inicial e estrutural do domínio**.

O documento deverá evoluir conforme:

* processos forem levantados;
* atores forem validados;
* legislação for analisada;
* requisitos forem identificados;
* decisões arquiteturais forem tomadas;
* necessidades municipais forem conhecidas;
* protótipos forem validados;
* implementação produzir novos conhecimentos.

---

# 39. Observação Metodológica

Este documento **não pretende antecipar todas as regras jurídicas ou operacionais de compras e contratações**.

A definição detalhada deverá ser construída a partir de fontes oficiais, legislação aplicável, regulamentação municipal, processos reais e validação pelos responsáveis pelo negócio.

Quando uma informação ainda não estiver validada, ela deverá ser tratada como **hipótese de modelagem**, e não como regra definitiva.

---

# 40. Disposição Final

O **Domínio de Gestão de Compras e Contratações** será o primeiro domínio utilizado para validar, de forma integrada, o modelo de engenharia do SIGMUN.

O objetivo não é apenas produzir documentação sobre compras.

O objetivo é demonstrar que o SIGMUN consegue transformar uma necessidade administrativa municipal em:

```text
processo
   ↓
serviço
   ↓
requisito
   ↓
software
   ↓
teste
   ↓
evidência
```

com rastreabilidade, governança, segurança, integração e capacidade de evolução.

---

# Controle de Versões

| Versão | Data       | Descrição                                                                        |
| ------ | ---------- | -------------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do documento de definição do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 000-Dominio-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
