# 001 – Mapa de Atores – Gestão de Compras e Contratações

#### Mapa de Atores – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md

---

# 1. Finalidade

O **Mapa de Atores – Gestão de Compras e Contratações** identifica as pessoas, unidades organizacionais, funções, entidades externas e demais participantes que interagem direta ou indiretamente com os processos e serviços do domínio.

O objetivo é estabelecer uma visão estruturada de:

* quem participa;
* qual é o papel de cada participante;
* quais responsabilidades possui;
* com quais processos interage;
* quais informações produz ou consome;
* quais decisões pode tomar;
* quais sistemas ou serviços utiliza;
* quais relações de dependência existem.

Este documento servirá de base para a elaboração dos processos, serviços, casos de uso, histórias de usuário, requisitos e controles de acesso do domínio.

---

# 2. Princípios

O mapeamento dos atores deverá observar os seguintes princípios:

* **Atores representam papéis, não necessariamente pessoas específicas.**
* **Uma mesma pessoa poderá exercer mais de um papel**, conforme suas atribuições.
* **Um ator poderá representar uma unidade organizacional**, quando a interação ocorrer institucionalmente.
* **Atores externos deverão ser identificados quando influenciarem ou participarem dos processos.**
* **Responsabilidade não deverá ser confundida com permissão de sistema.**
* **Permissões deverão ser derivadas posteriormente das responsabilidades e regras de negócio.**
* **Atores deverão ser relacionados aos processos e serviços nos quais efetivamente participam.**

---

# 3. Conceito de Ator

Para este domínio, considera-se ator qualquer pessoa, papel, unidade organizacional, organização ou sistema externo que:

* participe de um processo;
* forneça informação;
* consuma informação;
* execute uma atividade;
* tome uma decisão;
* aprove ou rejeite uma etapa;
* fiscalize;
* forneça um serviço;
* receba um resultado;
* integre-se com o SIGMUN.

---

# 4. Classificação dos Atores

Os atores serão classificados em:

```text
Atores Internos
Atores Externos
Atores Institucionais
Atores de Controle
Atores de Apoio
Sistemas Externos
```

---

# 5. Atores Internos

São os participantes pertencentes à estrutura administrativa municipal ou que atuam institucionalmente dentro da Prefeitura.

Atores inicialmente identificados:

* Unidade Requisitante;
* Servidor Solicitante;
* Gestor da Unidade;
* Unidade de Compras e Contratações;
* Agente responsável pelo procedimento;
* Equipe de apoio;
* Autoridade Competente;
* Gestor do Contrato;
* Fiscal do Contrato;
* Setor Jurídico;
* Setor Financeiro;
* Setor Contábil;
* Controle Interno;
* Administração do SIGMUN.

---

# 6. Atores Externos

Podem participar do domínio:

* fornecedor;
* representante do fornecedor;
* prestador de serviço;
* contratado;
* cidadão;
* órgãos externos;
* órgãos de controle;
* instituições participantes de mecanismos de contratação;
* sistemas externos.

A participação efetiva de cada ator deverá ser validada conforme o processo correspondente.

---

# 7. Unidade Requisitante

**Identificador:** `ACT-COMPRAS-001`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Unidade administrativa que identifica uma necessidade de aquisição ou contratação e inicia ou participa da solicitação correspondente.

**Responsabilidades potenciais:**

* identificar necessidades;
* justificar necessidades;
* informar características do objeto;
* participar da elaboração da especificação;
* acompanhar solicitações;
* fornecer informações complementares;
* validar o atendimento da necessidade.

**Interações principais:**

```text
Unidade Requisitante
        ↓
Necessidade
        ↓
Requisição
        ↓
Especificação
```

---

# 8. Servidor Solicitante

**Identificador:** `ACT-COMPRAS-002`

**Tipo:** Ator Humano

**Categoria:** Interno

**Descrição:**

Servidor que registra ou encaminha uma necessidade de aquisição ou contratação em nome da unidade administrativa.

**Responsabilidades potenciais:**

* registrar solicitação;
* informar dados necessários;
* anexar documentação;
* acompanhar o andamento;
* responder solicitações de complementação.

**Observação:**

O servidor solicitante poderá possuir diferentes níveis de responsabilidade conforme sua função.

---

# 9. Gestor da Unidade

**Identificador:** `ACT-COMPRAS-003`

**Tipo:** Ator Humano / Institucional

**Categoria:** Interno

**Descrição:**

Responsável pela unidade administrativa que valida ou autoriza necessidades e solicitações de sua área, conforme suas competências.

**Responsabilidades potenciais:**

* validar necessidade;
* priorizar demandas;
* autorizar encaminhamento;
* fornecer justificativas;
* acompanhar processos da unidade.

---

# 10. Unidade de Compras e Contratações

**Identificador:** `ACT-COMPRAS-004`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Unidade responsável pela condução ou coordenação das atividades administrativas relacionadas às compras e contratações.

**Responsabilidades potenciais:**

* receber solicitações;
* verificar instrução;
* orientar unidades;
* organizar processos;
* conduzir etapas sob sua competência;
* controlar prazos;
* acompanhar procedimentos;
* registrar informações no SIGMUN.

---

# 11. Agente Responsável pelo Procedimento

**Identificador:** `ACT-COMPRAS-005`

**Tipo:** Ator Humano

**Categoria:** Interno

**Descrição:**

Servidor ou agente formalmente responsável pela condução de determinado procedimento de contratação, conforme as competências atribuídas.

**Responsabilidades potenciais:**

* conduzir etapas do procedimento;
* registrar atos;
* analisar documentação;
* solicitar complementações;
* registrar resultados;
* encaminhar decisões;
* manter a integridade do processo.

---

# 12. Equipe de Apoio

**Identificador:** `ACT-COMPRAS-006`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Equipe que auxilia a condução das atividades relacionadas aos procedimentos de contratação.

**Responsabilidades potenciais:**

* apoiar análises;
* organizar documentação;
* apoiar sessões ou procedimentos;
* registrar informações;
* executar atividades delegadas.

---

# 13. Autoridade Competente

**Identificador:** `ACT-COMPRAS-007`

**Tipo:** Ator Humano / Institucional

**Categoria:** Interno

**Descrição:**

Autoridade com competência formal para tomar decisões, aprovar atos ou autorizar etapas do processo, conforme legislação e regulamentação aplicáveis.

**Responsabilidades potenciais:**

* autorizar;
* aprovar;
* decidir;
* homologar quando aplicável;
* determinar providências;
* deliberar sobre situações específicas.

**Observação:**

As competências deverão ser configuráveis e vinculadas à estrutura administrativa e normativa aplicável.

---

# 14. Setor Jurídico

**Identificador:** `ACT-COMPRAS-008`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Unidade responsável pelas análises e manifestações jurídicas que sejam necessárias ou aplicáveis ao processo.

**Responsabilidades potenciais:**

* analisar processos;
* emitir manifestação;
* analisar instrumentos;
* avaliar questões jurídicas;
* registrar pareceres;
* solicitar complementações.

---

# 15. Setor Financeiro

**Identificador:** `ACT-COMPRAS-009`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Unidade que participa dos processos quando houver necessidade de informações ou providências financeiras.

**Responsabilidades potenciais:**

* fornecer informações;
* verificar disponibilidade ou condições financeiras conforme sua competência;
* participar da execução financeira;
* informar situações relacionadas aos pagamentos.

---

# 16. Setor Contábil

**Identificador:** `ACT-COMPRAS-010`

**Tipo:** Ator Institucional

**Categoria:** Interno

**Descrição:**

Unidade responsável pelas atividades contábeis relacionadas aos processos de contratação.

**Responsabilidades potenciais:**

* fornecer informações;
* realizar registros de sua competência;
* validar informações contábeis;
* participar das integrações contábeis.

---

# 17. Controle Interno

**Identificador:** `ACT-COMPRAS-011`

**Tipo:** Ator Institucional

**Categoria:** Controle

**Descrição:**

Unidade responsável pelas atividades de controle interno e acompanhamento dos processos administrativos, conforme suas competências.

**Responsabilidades potenciais:**

* realizar controles;
* analisar processos;
* emitir recomendações;
* registrar apontamentos;
* acompanhar providências;
* realizar auditorias ou verificações.

---

# 18. Gestor do Contrato

**Identificador:** `ACT-COMPRAS-012`

**Tipo:** Ator Humano

**Categoria:** Interno

**Descrição:**

Responsável pelo acompanhamento gerencial do contrato, conforme atribuições formalmente estabelecidas.

**Responsabilidades potenciais:**

* acompanhar execução;
* controlar prazos;
* acompanhar obrigações;
* registrar ocorrências;
* encaminhar providências;
* acompanhar alterações;
* apoiar o encerramento.

---

# 19. Fiscal do Contrato

**Identificador:** `ACT-COMPRAS-013`

**Tipo:** Ator Humano

**Categoria:** Interno

**Descrição:**

Responsável pelo acompanhamento e fiscalização da execução do objeto contratado, conforme sua designação e competência.

**Responsabilidades potenciais:**

* fiscalizar execução;
* registrar ocorrências;
* verificar entregas;
* registrar não conformidades;
* produzir evidências;
* informar situações relevantes;
* acompanhar correções.

---

# 20. Administração do SIGMUN

**Identificador:** `ACT-COMPRAS-014`

**Tipo:** Ator Técnico

**Categoria:** Apoio

**Descrição:**

Responsável pela administração técnica e funcional da plataforma SIGMUN.

**Responsabilidades potenciais:**

* administrar usuários;
* administrar perfis;
* configurar parâmetros;
* manter integrações;
* administrar permissões;
* monitorar funcionamento;
* apoiar auditorias técnicas.

**Observação:**

O administrador técnico não deverá receber automaticamente permissões de negócio.

---

# 21. Fornecedor

**Identificador:** `ACT-COMPRAS-015`

**Tipo:** Ator Organizacional

**Categoria:** Externo

**Descrição:**

Pessoa jurídica ou pessoa física que participa de processos de contratação ou mantém relação contratual com o Município.

**Responsabilidades potenciais:**

* fornecer informações;
* apresentar propostas;
* apresentar documentação;
* responder solicitações;
* executar objeto contratado;
* apresentar documentos;
* cumprir obrigações.

---

# 22. Representante do Fornecedor

**Identificador:** `ACT-COMPRAS-016`

**Tipo:** Ator Humano

**Categoria:** Externo

**Descrição:**

Pessoa que representa o fornecedor perante a Administração.

**Responsabilidades potenciais:**

* apresentar documentação;
* participar de procedimentos;
* responder comunicações;
* apresentar propostas;
* acompanhar contratos;
* prestar informações.

---

# 23. Órgão de Controle

**Identificador:** `ACT-COMPRAS-017`

**Tipo:** Ator Institucional

**Categoria:** Controle Externo

**Descrição:**

Órgão externo que possua competência legal para fiscalizar, controlar ou receber informações relacionadas às contratações municipais.

**Interações potenciais:**

* recebimento de informações;
* consultas;
* auditorias;
* solicitações de documentos;
* fiscalização;
* prestação de contas.

---

# 24. Cidadão

**Identificador:** `ACT-COMPRAS-018`

**Tipo:** Ator Humano

**Categoria:** Externo

**Descrição:**

Cidadão que consulta informações públicas relacionadas às compras e contratações municipais.

**Interações potenciais:**

* consulta de contratações;
* consulta de fornecedores;
* consulta de contratos;
* consulta de valores;
* consulta de documentos públicos;
* consulta de indicadores.

---

# 25. Sistema Financeiro

**Identificador:** `ACT-COMPRAS-019`

**Tipo:** Sistema Externo ou Domínio Integrado

**Categoria:** Sistema

**Descrição:**

Sistema ou domínio responsável por informações e processos financeiros relacionados às contratações.

**Interações potenciais:**

* disponibilidade;
* empenhos;
* pagamentos;
* liquidações;
* informações financeiras;
* situação financeira.

A classificação definitiva dependerá da arquitetura do SIGMUN.

---

# 26. Sistema Contábil

**Identificador:** `ACT-COMPRAS-020`

**Tipo:** Sistema Externo ou Domínio Integrado

**Categoria:** Sistema

**Descrição:**

Sistema ou domínio responsável pelas informações contábeis relacionadas às contratações.

**Interações potenciais:**

* registros contábeis;
* classificações;
* informações de execução;
* integrações.

---

# 27. Sistema de Transparência

**Identificador:** `ACT-COMPRAS-021`

**Tipo:** Sistema

**Categoria:** Sistema Integrado

**Descrição:**

Serviço responsável pela disponibilização de informações públicas.

**Interações potenciais:**

* contratos;
* processos;
* fornecedores;
* valores;
* documentos públicos;
* indicadores.

---

# 28. Sistema de Identidade

**Identificador:** `ACT-COMPRAS-022`

**Tipo:** Sistema

**Categoria:** Sistema Corporativo

**Descrição:**

Serviço corporativo responsável pela autenticação e identificação dos usuários.

**Interações potenciais:**

* autenticação;
* identificação;
* perfis;
* sessões;
* informações de usuário.

---

# 29. Matriz Geral de Atores

| ID                | Ator                                 | Categoria        | Participação              |
| ----------------- | ------------------------------------ | ---------------- | ------------------------- |
| `ACT-COMPRAS-001` | Unidade Requisitante                 | Interno          | Necessidade e requisição  |
| `ACT-COMPRAS-002` | Servidor Solicitante                 | Interno          | Registro e acompanhamento |
| `ACT-COMPRAS-003` | Gestor da Unidade                    | Interno          | Validação e autorização   |
| `ACT-COMPRAS-004` | Unidade de Compras e Contratações    | Interno          | Condução administrativa   |
| `ACT-COMPRAS-005` | Agente Responsável pelo Procedimento | Interno          | Condução do procedimento  |
| `ACT-COMPRAS-006` | Equipe de Apoio                      | Interno          | Apoio                     |
| `ACT-COMPRAS-007` | Autoridade Competente                | Interno          | Decisão e aprovação       |
| `ACT-COMPRAS-008` | Setor Jurídico                       | Interno          | Análise jurídica          |
| `ACT-COMPRAS-009` | Setor Financeiro                     | Interno          | Informações financeiras   |
| `ACT-COMPRAS-010` | Setor Contábil                       | Interno          | Informações contábeis     |
| `ACT-COMPRAS-011` | Controle Interno                     | Controle         | Controle e auditoria      |
| `ACT-COMPRAS-012` | Gestor do Contrato                   | Interno          | Gestão contratual         |
| `ACT-COMPRAS-013` | Fiscal do Contrato                   | Interno          | Fiscalização              |
| `ACT-COMPRAS-014` | Administração do SIGMUN              | Técnico          | Administração do sistema  |
| `ACT-COMPRAS-015` | Fornecedor                           | Externo          | Participação e execução   |
| `ACT-COMPRAS-016` | Representante do Fornecedor          | Externo          | Representação             |
| `ACT-COMPRAS-017` | Órgão de Controle                    | Controle Externo | Fiscalização              |
| `ACT-COMPRAS-018` | Cidadão                              | Externo          | Consulta                  |
| `ACT-COMPRAS-019` | Sistema Financeiro                   | Sistema          | Integração                |
| `ACT-COMPRAS-020` | Sistema Contábil                     | Sistema          | Integração                |
| `ACT-COMPRAS-021` | Sistema de Transparência             | Sistema          | Publicação                |
| `ACT-COMPRAS-022` | Sistema de Identidade                | Sistema          | Autenticação              |

---

# 30. Matriz Ator × Processo

A matriz inicial deverá ser refinada após o mapeamento detalhado dos processos.

| Ator                   | Planejamento | Requisição | Procedimento | Formalização | Gestão Contratual | Fiscalização | Encerramento |
| ---------------------- | -----------: | ---------: | -----------: | -----------: | ----------------: | -----------: | -----------: |
| Unidade Requisitante   |            ● |          ● |            ○ |            ○ |                 ○ |            ○ |            ○ |
| Servidor Solicitante   |            ○ |          ● |            ○ |            ○ |                 ○ |            ○ |            ○ |
| Gestor da Unidade      |            ● |          ● |            ○ |            ○ |                 ○ |            ○ |            ○ |
| Unidade de Compras     |            ● |          ● |            ● |            ● |                 ● |            ○ |            ● |
| Agente do Procedimento |            ○ |          ○ |            ● |            ● |                 ○ |            ○ |            ○ |
| Equipe de Apoio        |            ○ |          ○ |            ● |            ● |                 ○ |            ○ |            ○ |
| Autoridade Competente  |            ● |          ○ |            ● |            ● |                 ○ |            ○ |            ● |
| Setor Jurídico         |            ○ |          ○ |            ● |            ● |                 ○ |            ○ |            ○ |
| Setor Financeiro       |            ○ |          ○ |            ○ |            ● |                 ● |            ○ |            ○ |
| Setor Contábil         |            ○ |          ○ |            ○ |            ● |                 ● |            ○ |            ● |
| Controle Interno       |            ○ |          ○ |            ○ |            ○ |                 ○ |            ● |            ● |
| Gestor do Contrato     |            ○ |          ○ |            ○ |            ● |                 ● |            ● |            ● |
| Fiscal do Contrato     |            ○ |          ○ |            ○ |            ○ |                 ● |            ● |            ● |
| Fornecedor             |            ○ |          ○ |            ● |            ● |                 ● |            ● |            ● |
| Órgão de Controle      |            ○ |          ○ |            ○ |            ○ |                 ○ |            ○ |            ● |
| Cidadão                |            ○ |          ○ |            ○ |            ○ |                 ○ |            ○ |            ○ |

**Legenda:**

* `●` Participação principal
* `○` Participação eventual ou dependente do processo
* vazio = sem participação identificada

Esta matriz deverá ser validada após o detalhamento dos processos.

---

# 31. Matriz Ator × Serviço

| Ator                   | Planejamento | Solicitação | Pesquisa de Preços | Processo | Contrato | Fiscalização | Consulta |
| ---------------------- | -----------: | ----------: | -----------------: | -------: | -------: | -----------: | -------: |
| Unidade Requisitante   |            ● |           ● |                  ○ |        ● |        ○ |            ○ |        ● |
| Gestor da Unidade      |            ● |           ● |                  ○ |        ● |        ○ |            ○ |        ● |
| Unidade de Compras     |            ● |           ● |                  ● |        ● |        ● |            ○ |        ● |
| Agente do Procedimento |            ○ |           ○ |                  ● |        ● |        ● |            ○ |        ● |
| Autoridade Competente  |            ● |           ○ |                  ○ |        ● |        ● |            ○ |        ● |
| Setor Jurídico         |            ○ |           ○ |                  ○ |        ● |        ● |            ○ |        ● |
| Gestor do Contrato     |            ○ |           ○ |                  ○ |        ○ |        ● |            ● |        ● |
| Fiscal do Contrato     |            ○ |           ○ |                  ○ |        ○ |        ● |            ● |        ● |
| Fornecedor             |            ○ |           ○ |                  ● |        ● |        ● |            ● |        ● |
| Controle Interno       |            ○ |           ○ |                  ○ |        ● |        ● |            ● |        ● |
| Cidadão                |            ○ |           ○ |                  ○ |        ○ |        ● |            ○ |        ● |

---

# 32. Responsabilidades x Permissões

A identificação do ator não determina automaticamente suas permissões no sistema.

A matriz de permissões deverá ser derivada posteriormente a partir de:

```text
Ator
  ↓
Responsabilidade
  ↓
Processo
  ↓
Atividade
  ↓
Regra de Negócio
  ↓
Permissão
```

---

# 33. Segregação de Funções

O domínio deverá considerar possíveis conflitos entre responsabilidades.

Exemplo conceitual:

```text
Solicitar
   ≠
Aprovar
   ≠
Conduzir
   ≠
Fiscalizar
```

A matriz definitiva deverá ser construída a partir das competências legais e administrativas.

---

# 34. Atores e Identidade

Os atores humanos internos deverão, quando aplicável, ser vinculados à identidade corporativa do SIGMUN.

A relação deverá considerar:

```text
Pessoa
  ↓
Servidor
  ↓
Lotação
  ↓
Função
  ↓
Papel
  ↓
Permissão
```

---

# 35. Atores Externos e Identidade

Atores externos deverão possuir mecanismos de identificação compatíveis com sua forma de participação.

Exemplos:

* fornecedor;
* representante;
* cidadão;
* órgão externo.

A solução deverá evitar criação de identidades externas desnecessárias.

---

# 36. Atores e Dados

Cada ator deverá ser relacionado às informações que:

* cria;
* consulta;
* altera;
* aprova;
* valida;
* recebe;
* publica.

Essa matriz será desenvolvida durante a especificação dos processos e requisitos.

---

# 37. Atores e Documentos

Os atores poderão:

```text
Criar
Consultar
Analisar
Aprovar
Assinar
Anexar
Validar
Publicar
Arquivar
```

documentos relacionados aos processos.

As permissões deverão respeitar classificação da informação.

---

# 38. Atores e Auditoria

As operações relevantes deverão registrar o ator responsável pela ação.

O registro deverá permitir identificar, conforme aplicabilidade:

* usuário;
* papel;
* unidade;
* data;
* horário;
* operação;
* objeto afetado;
* resultado.

---

# 39. Atores e Notificações

O domínio deverá identificar quais atores precisam receber notificações relacionadas a:

* pendências;
* aprovações;
* prazos;
* alterações;
* ocorrências;
* vencimentos;
* solicitações de complementação;
* decisões.

---

# 40. Atores e Indicadores

Os indicadores poderão ser segmentados por:

* unidade;
* papel;
* processo;
* responsável;
* fornecedor;
* período;
* tipo de contratação.

O uso de informações pessoais deverá respeitar as políticas de proteção de dados aplicáveis.

---

# 41. Atores Críticos

Atores com maior influência sobre o processo deverão receber atenção especial na modelagem.

Inicialmente:

```text
Unidade Requisitante
Unidade de Compras
Agente do Procedimento
Autoridade Competente
Gestor do Contrato
Fiscal do Contrato
Fornecedor
Controle Interno
```

---

# 42. Atores de Alta Dependência

São atores cuja participação poderá bloquear ou liberar etapas relevantes.

Exemplos:

* autoridade competente;
* unidade de compras;
* setor jurídico;
* gestor do contrato;
* fiscal do contrato.

A criticidade deverá ser validada durante o mapeamento dos processos.

---

# 43. Atores de Informação

Alguns atores poderão atuar predominantemente como consumidores ou fornecedores de informação.

Exemplos:

```text
Setor Financeiro
Setor Contábil
Controle Interno
Cidadão
Órgão de Controle
```

---

# 44. Atores de Execução

Atores que executam atividades operacionais:

```text
Servidor Solicitante
Unidade de Compras
Agente do Procedimento
Equipe de Apoio
Gestor do Contrato
Fiscal do Contrato
Fornecedor
```

---

# 45. Atores de Decisão

Atores que poderão tomar decisões formais:

```text
Gestor da Unidade
Autoridade Competente
```

A definição exata dependerá da estrutura administrativa e normativa municipal.

---

# 46. Atores de Controle

```text
Controle Interno
Órgãos de Controle
Setor Jurídico
```

Cada um deverá ser diferenciado por sua competência e finalidade.

---

# 47. Atores de Suporte

```text
Administração do SIGMUN
Setor Financeiro
Setor Contábil
Equipe de Apoio
```

---

# 48. Atores e Canais

Os atores poderão interagir por:

* aplicação web;
* aplicação móvel;
* portal externo;
* notificações;
* APIs;
* integrações;
* documentos digitais;
* mecanismos de consulta pública.

---

# 49. Atores e Offline First

Quando atividades de fiscalização, recebimento ou execução ocorrerem em ambientes com conectividade limitada, os atores de campo deverão ser considerados na arquitetura **Offline First** do SIGMUN.

Exemplo:

```text
Fiscal
  ↓
Aplicativo de Campo
  ↓
Registro Offline
  ↓
Sincronização
  ↓
SIGMUN
```

---

# 50. Atores e Mobilidade

Os seguintes atores poderão potencialmente utilizar dispositivos móveis:

* fiscal;
* gestor do contrato;
* servidor requisitante;
* responsável pelo recebimento;
* outros agentes de campo.

A necessidade real deverá ser validada durante o desenho dos processos.

---

# 51. Mapa Conceitual dos Atores

```text
                         ┌─────────────────────┐
                         │ Autoridade Competente│
                         └──────────┬──────────┘
                                    │
                                    ▼
┌──────────────────┐       ┌──────────────────────┐
│ Unidade          │──────▶│ Unidade de Compras   │
│ Requisitante     │       └──────────┬───────────┘
└──────────────────┘                  │
                                     ▼
                           ┌──────────────────────┐
                           │ Agente do Procedimento│
                           └──────────┬───────────┘
                                      │
                         ┌────────────┼────────────┐
                         ▼            ▼            ▼
                    ┌────────┐  ┌─────────┐  ┌────────────┐
                    │Jurídico│  │Financeiro│ │Fornecedor  │
                    └────────┘  └─────────┘  └─────┬──────┘
                                                    │
                                                    ▼
                                             ┌────────────┐
                                             │ Contrato   │
                                             └─────┬──────┘
                                                   │
                              ┌────────────────────┼─────────────────┐
                              ▼                    ▼                 ▼
                       ┌────────────┐       ┌────────────┐    ┌──────────────┐
                       │Gestor      │       │Fiscal      │    │Controle      │
                       │Contrato    │       │Contrato    │    │Interno       │
                       └────────────┘       └────────────┘    └──────────────┘
```

---

# 52. Lacunas a Validar

O mapa ainda deverá validar:

* estrutura real das unidades de compras;
* papéis administrativos existentes;
* competências;
* autoridade de aprovação;
* responsabilidades de fiscalização;
* responsabilidades jurídicas;
* responsabilidades financeiras;
* responsabilidades contábeis;
* participação do controle interno;
* participação dos fornecedores;
* participação dos órgãos de controle;
* canais de interação;
* necessidade de mobilidade;
* necessidade de acesso externo.

---

# 53. Questões para Levantamento

Durante o levantamento do domínio deverão ser respondidas:

1. Quem identifica a necessidade?
2. Quem registra a solicitação?
3. Quem valida a solicitação?
4. Quem pode devolver uma solicitação?
5. Quem elabora a especificação?
6. Quem realiza ou valida a pesquisa de preços?
7. Quem instrui o processo?
8. Quem conduz o procedimento?
9. Quem analisa juridicamente?
10. Quem aprova?
11. Quem formaliza?
12. Quem acompanha o contrato?
13. Quem fiscaliza?
14. Quem registra o recebimento?
15. Quem encerra?
16. Quem audita?
17. Quem consulta?
18. Quem recebe notificações?
19. Quem pode alterar cada informação?
20. Quem pode visualizar cada informação?

---

# 54. Relação com Casos de Uso

Cada caso de uso deverá possuir pelo menos um ator principal.

Exemplo:

```text
UC-COMPRAS-001 – Registrar Necessidade

Ator Principal:
ACT-COMPRAS-002 – Servidor Solicitante

Atores Secundários:
ACT-COMPRAS-003 – Gestor da Unidade
ACT-COMPRAS-004 – Unidade de Compras
```

---

# 55. Relação com Histórias de Usuário

As histórias deverão utilizar papéis de negócio.

Exemplo:

```text
Como servidor solicitante,
quero registrar uma necessidade de contratação,
para que minha unidade possa iniciar o processo de aquisição.
```

---

# 56. Relação com Requisitos

Os requisitos deverão indicar quais atores serão impactados.

Exemplo:

```text
RF-COMPRAS-001

Atores:
- ACT-COMPRAS-002
- ACT-COMPRAS-003
- ACT-COMPRAS-004
```

---

# 57. Relação com Segurança

Os atores constituirão uma das entradas para a definição de:

* perfis;
* papéis;
* permissões;
* segregação;
* controles;
* auditoria.

---

# 58. Relação com o Mapa Mestre

Este documento deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

Identificador do artefato:

`ACT-MAP-COMPRAS-001`

Relações principais:

```text
DOM-COMPRAS-001
       ↓
ACT-MAP-COMPRAS-001
       ↓
PROC-COMPRAS-001...012
       ↓
SERV-COMPRAS-001...010
       ↓
UC-COMPRAS-001...
```

---

# 59. Critérios de Conclusão

O Mapa de Atores será considerado suficientemente definido quando:

* os atores internos estiverem identificados;
* os atores externos relevantes estiverem identificados;
* os sistemas envolvidos estiverem identificados;
* as responsabilidades principais estiverem descritas;
* os atores estiverem relacionados aos processos;
* os atores estiverem relacionados aos serviços;
* os conflitos de responsabilidade estiverem identificados;
* as lacunas estiverem registradas;
* as informações ainda não validadas estiverem explicitamente marcadas.

---

# 60. Evolução

Este documento deverá ser atualizado quando:

* novos processos forem identificados;
* novos serviços forem criados;
* responsabilidades forem alteradas;
* novos sistemas forem integrados;
* a estrutura administrativa mudar;
* novos canais forem disponibilizados;
* novas necessidades forem identificadas.

---

# 61. Disposição Final

O Mapa de Atores constitui a base para compreender **quem participa do domínio de Gestão de Compras e Contratações**.

Nenhum caso de uso deverá ser definido sem considerar seus atores.

Nenhum requisito de autorização deverá ser definido sem considerar a responsabilidade do ator.

Nenhuma permissão deverá ser concedida apenas com base no nome de um cargo, sem considerar a função efetivamente exercida no processo.

O objetivo é estabelecer uma relação consistente entre:

```text
Ator
  ↓
Responsabilidade
  ↓
Processo
  ↓
Atividade
  ↓
Serviço
  ↓
Caso de Uso
  ↓
Requisito
  ↓
Permissão
```

---

# Controle de Versões

| Versão | Data       | Descrição                                                                |
| ------ | ---------- | ------------------------------------------------------------------------ |
| 1.0    | 2026-08-11 | Criação do Mapa de Atores do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
