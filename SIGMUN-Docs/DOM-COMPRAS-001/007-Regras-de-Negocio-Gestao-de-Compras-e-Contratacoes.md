# 007 – Regras de Negócio – Gestão de Compras e Contratações

#### Regras de Negócio – Gestão de Compras e Contratações

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
* 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
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

Este documento estabelece as **Regras de Negócio do Domínio de Gestão de Compras e Contratações** do SIGMUN.

As regras de negócio representam condições, restrições, políticas, validações e comportamentos que devem ser respeitados pelos processos de compras e contratações municipais.

As regras aqui definidas deverão orientar:

* requisitos funcionais;
* requisitos não funcionais;
* especificações;
* fluxos de processos;
* casos de uso;
* histórias de usuário;
* critérios de aceitação;
* testes;
* integrações;
* controles;
* auditoria;
* relatórios;
* indicadores.

---

# 2. Princípios das Regras de Negócio

As regras deste domínio deverão observar os princípios de:

* legalidade;
* impessoalidade;
* moralidade;
* publicidade;
* eficiência;
* planejamento;
* transparência;
* segregação de funções;
* rastreabilidade;
* controle;
* economicidade;
* segurança;
* integridade;
* responsabilização;
* proteção de dados;
* interoperabilidade.

---

# 3. Convenção de Identificação

As regras utilizarão o padrão:

```text
RN-COMPRAS-XXX
```

Exemplo:

```text
RN-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida da regra.

---

# 4. Classificação das Regras

As regras poderão ser classificadas como:

| Tipo   | Descrição                                        |
| ------ | ------------------------------------------------ |
| RN-LEG | Regra decorrente de obrigação legal ou normativa |
| RN-PRO | Regra relacionada a processo                     |
| RN-VAL | Regra de validação                               |
| RN-SEG | Regra de segurança ou segregação                 |
| RN-CON | Regra de controle                                |
| RN-TRA | Regra de transparência                           |
| RN-DAD | Regra relacionada a dados                        |
| RN-INT | Regra de integração                              |
| RN-FIN | Regra relacionada a aspectos financeiros         |
| RN-DOC | Regra relacionada à documentação                 |
| RN-AUD | Regra relacionada à auditoria                    |

---

# 5. Regras Gerais

## RN-COMPRAS-001 – Formalização das Demandas

Toda demanda de compra ou contratação deverá ser formalmente registrada antes de seu processamento.

---

## RN-COMPRAS-002 – Identificação Única

Cada demanda, processo, contratação e instrumento contratual deverá possuir identificador único dentro do contexto municipal.

---

## RN-COMPRAS-003 – Rastreabilidade

Toda contratação deverá permitir rastrear, quando aplicável:

```text
Necessidade
    ↓
Requisição
    ↓
Planejamento
    ↓
Processo
    ↓
Procedimento
    ↓
Decisão
    ↓
Contratação
    ↓
Execução
    ↓
Fiscalização
    ↓
Pagamento
    ↓
Encerramento
```

---

## RN-COMPRAS-004 – Integridade do Histórico

O histórico dos atos relevantes não deverá ser apagado de forma que comprometa a rastreabilidade.

Alterações relevantes deverão permanecer registradas conforme as políticas de auditoria e gestão documental.

---

# 6. Regras de Planejamento

## RN-COMPRAS-005 – Planejamento Prévio

As contratações deverão ser planejadas conforme os instrumentos e procedimentos de planejamento adotados pelo Município.

---

## RN-COMPRAS-006 – Consolidação de Necessidades

Necessidades semelhantes deverão ser identificadas para avaliação de eventual consolidação.

---

## RN-COMPRAS-007 – Priorização

As demandas poderão receber classificação de prioridade conforme critérios previamente definidos pela Administração.

---

## RN-COMPRAS-008 – Compatibilidade com Planejamento

Uma contratação planejada deverá ser compatível com os instrumentos de planejamento aplicáveis ao Município.

---

# 7. Regras de Requisição

## RN-COMPRAS-009 – Identificação do Requisitante

Toda requisição deverá identificar a unidade e o usuário responsável por sua elaboração.

---

## RN-COMPRAS-010 – Justificativa da Necessidade

A requisição deverá apresentar justificativa suficiente para demonstrar a necessidade da contratação.

---

## RN-COMPRAS-011 – Especificação do Objeto

A requisição deverá conter descrição adequada do objeto pretendido.

---

## RN-COMPRAS-012 – Quantificação

Quando aplicável, a demanda deverá informar as quantidades necessárias.

---

## RN-COMPRAS-013 – Unidade de Medida

Os itens quantificáveis deverão possuir unidade de medida definida.

---

## RN-COMPRAS-014 – Documentação

Os documentos necessários à instrução da demanda deverão ser vinculados ao respectivo registro.

---

## RN-COMPRAS-015 – Aprovação

Quando exigido pelo fluxo administrativo, a requisição deverá ser submetida à aprovação da autoridade competente antes de prosseguir.

---

# 8. Regras de Especificação

## RN-COMPRAS-016 – Clareza da Especificação

A especificação do objeto deverá ser suficientemente clara para permitir sua compreensão e avaliação.

---

## RN-COMPRAS-017 – Neutralidade

As especificações deverão evitar direcionamentos indevidos que restrinjam injustificadamente a competitividade.

---

## RN-COMPRAS-018 – Requisitos Técnicos

Requisitos técnicos deverão estar relacionados à necessidade efetiva da contratação.

---

## RN-COMPRAS-019 – Validação da Especificação

A especificação deverá ser validada pela unidade responsável antes da continuidade do processo, quando aplicável.

---

# 9. Regras de Pesquisa e Estimativa de Preços

## RN-COMPRAS-020 – Registro da Fonte

Toda informação utilizada para formação da estimativa deverá possuir identificação de sua fonte.

---

## RN-COMPRAS-021 – Rastreabilidade dos Preços

Os valores utilizados na estimativa deverão permanecer associados às respectivas fontes.

---

## RN-COMPRAS-022 – Data da Pesquisa

A pesquisa de preços deverá registrar a data de obtenção da informação.

---

## RN-COMPRAS-023 – Metodologia de Estimativa

A estimativa deverá utilizar metodologia compatível com as regras e procedimentos adotados pelo Município.

---

## RN-COMPRAS-024 – Histórico de Preços

Quando disponível, o histórico de preços poderá ser utilizado como elemento de apoio à análise.

---

# 10. Regras de Processo de Contratação

## RN-COMPRAS-025 – Processo Único

Os atos relativos a uma contratação deverão estar vinculados ao respectivo processo administrativo.

---

## RN-COMPRAS-026 – Sequenciamento

Os atos deverão respeitar a sequência processual estabelecida para cada modalidade ou procedimento.

---

## RN-COMPRAS-027 – Pendências

O processo não deverá avançar para etapas incompatíveis enquanto existirem pendências impeditivas.

---

## RN-COMPRAS-028 – Responsabilidade

Cada ato relevante deverá possuir identificação do responsável por sua realização.

---

## RN-COMPRAS-029 – Registro de Data e Hora

Os atos realizados no sistema deverão possuir registro temporal adequado.

---

# 11. Regras de Fornecedores

## RN-COMPRAS-030 – Identificação do Fornecedor

O fornecedor deverá possuir identificação suficiente para permitir sua correta individualização.

---

## RN-COMPRAS-031 – Unicidade Cadastral

O cadastro deverá evitar registros duplicados para o mesmo fornecedor.

---

## RN-COMPRAS-032 – Histórico

Informações relevantes do relacionamento do fornecedor com o Município deverão permanecer rastreáveis.

---

## RN-COMPRAS-033 – Dados Cadastrais

Alterações relevantes nos dados cadastrais deverão preservar o histórico necessário à auditoria.

---

# 12. Regras de Formalização

## RN-COMPRAS-034 – Formalização da Contratação

A contratação somente deverá ser considerada formalizada após o cumprimento das etapas necessárias para sua formalização.

---

## RN-COMPRAS-035 – Instrumento Contratual

Quando aplicável, a contratação deverá possuir instrumento formal correspondente.

---

## RN-COMPRAS-036 – Identificação do Contrato

Cada contrato deverá possuir identificação única.

---

## RN-COMPRAS-037 – Vigência

O contrato deverá possuir período de vigência quando essa informação for aplicável.

---

## RN-COMPRAS-038 – Objeto Contratual

O contrato deverá possuir vínculo com o objeto contratado.

---

## RN-COMPRAS-039 – Valor Contratual

Quando aplicável, o contrato deverá possuir informação sobre seu valor.

---

# 13. Regras de Execução Contratual

## RN-COMPRAS-040 – Acompanhamento

Os contratos deverão possuir acompanhamento de sua execução conforme as responsabilidades definidas.

---

## RN-COMPRAS-041 – Fiscalização

Quando exigido, deverá existir responsável formalmente designado para fiscalização.

---

## RN-COMPRAS-042 – Registro das Atividades

Atividades relevantes de fiscalização deverão ser registradas.

---

## RN-COMPRAS-043 – Evidências

As atividades de fiscalização poderão ser acompanhadas de documentos, registros ou outras evidências pertinentes.

---

## RN-COMPRAS-044 – Não Conformidade

Não conformidades identificadas deverão ser registradas e vinculadas ao contrato correspondente.

---

## RN-COMPRAS-045 – Tratamento de Não Conformidade

Não conformidades deverão possuir acompanhamento de seu tratamento quando houver necessidade de providência.

---

# 14. Regras de Vigência

## RN-COMPRAS-046 – Controle de Vigência

O sistema deverá permitir o acompanhamento da vigência dos contratos.

---

## RN-COMPRAS-047 – Alertas de Prazo

Quando configurado, o sistema deverá gerar alertas relacionados a prazos relevantes.

---

## RN-COMPRAS-048 – Prorrogação

A prorrogação deverá ser tratada como evento formal relacionado ao instrumento contratual.

---

# 15. Regras de Alterações Contratuais

## RN-COMPRAS-049 – Registro de Alterações

Toda alteração formal deverá ser registrada e vinculada ao contrato correspondente.

---

## RN-COMPRAS-050 – Histórico de Alterações

O contrato deverá manter histórico das alterações realizadas.

---

## RN-COMPRAS-051 – Aditivos

Cada instrumento aditivo deverá possuir identificação própria e vínculo com o contrato de origem.

---

## RN-COMPRAS-052 – Reajustes

Reajustes ou revisões deverão manter vínculo com o contrato e com o respectivo fundamento.

---

# 16. Regras de Recebimento

## RN-COMPRAS-053 – Registro de Entrega

As entregas relevantes deverão ser registradas quando aplicável.

---

## RN-COMPRAS-054 – Conferência

A entrega deverá ser conferida conforme os critérios definidos para o objeto.

---

## RN-COMPRAS-055 – Aceite

O aceite deverá ser registrado por usuário autorizado.

---

## RN-COMPRAS-056 – Divergência

Divergências entre o contratado e o recebido deverão ser registradas.

---

# 17. Regras de Encerramento

## RN-COMPRAS-057 – Encerramento da Execução

O encerramento da execução deverá registrar a situação final do objeto.

---

## RN-COMPRAS-058 – Encerramento Contratual

O contrato deverá possuir registro de encerramento quando sua execução for concluída ou ocorrer outra forma de término.

---

## RN-COMPRAS-059 – Arquivamento

Processos concluídos deverão seguir as regras de arquivamento e preservação documental aplicáveis.

---

# 18. Regras Documentais

## RN-COMPRAS-060 – Vinculação Documental

Documentos relacionados à contratação deverão estar vinculados ao respectivo processo ou instrumento.

---

## RN-COMPRAS-061 – Integridade Documental

Documentos deverão ser preservados de forma a garantir sua integridade.

---

## RN-COMPRAS-062 – Classificação da Informação

Os documentos deverão possuir classificação da informação conforme a política corporativa aplicável.

---

## RN-COMPRAS-063 – Controle de Acesso

O acesso a documentos deverá respeitar as permissões e restrições aplicáveis.

---

# 19. Regras de Transparência

## RN-COMPRAS-064 – Publicidade

Informações classificadas como públicas deverão ser disponibilizadas conforme as políticas de transparência do Município.

---

## RN-COMPRAS-065 – Proteção de Dados

Informações pessoais protegidas não deverão ser publicadas indevidamente.

---

## RN-COMPRAS-066 – Origem dos Dados

Informações disponibilizadas para transparência deverão possuir origem rastreável no sistema.

---

## RN-COMPRAS-067 – Atualização

Dados publicados deverão ser atualizados conforme a periodicidade e os mecanismos definidos para cada informação.

---

# 20. Regras de Auditoria

## RN-COMPRAS-068 – Trilha de Auditoria

Operações relevantes deverão gerar registros suficientes para permitir auditoria.

---

## RN-COMPRAS-069 – Identificação do Usuário

Os registros de auditoria deverão identificar o usuário responsável pela operação, conforme as políticas de segurança.

---

## RN-COMPRAS-070 – Imutabilidade da Auditoria

Registros de auditoria deverão ser protegidos contra alterações não autorizadas.

---

## RN-COMPRAS-071 – Consulta Controlada

O acesso às informações de auditoria deverá ser controlado conforme o perfil do usuário.

---

# 21. Regras de Segregação de Funções

## RN-COMPRAS-072 – Segregação

Funções incompatíveis deverão ser segregadas sempre que aplicável.

---

## RN-COMPRAS-073 – Conflito de Responsabilidades

O sistema deverá impedir ou sinalizar combinações de responsabilidades incompatíveis quando essas regras forem configuradas.

---

## RN-COMPRAS-074 – Aprovação Independente

Atos que exigirem aprovação deverão ser realizados por usuário com autoridade compatível.

---

# 22. Regras de Permissões

## RN-COMPRAS-075 – Controle por Perfil

As operações disponíveis deverão respeitar o perfil e as permissões do usuário.

---

## RN-COMPRAS-076 – Privilégio Mínimo

Os usuários deverão possuir somente os privilégios necessários ao desempenho de suas funções.

---

## RN-COMPRAS-077 – Responsabilidade Institucional

As permissões deverão considerar a unidade administrativa, função e responsabilidade do usuário quando aplicável.

---

# 23. Regras de Integração

## RN-COMPRAS-078 – Integração Orçamentária

Informações necessárias à execução orçamentária deverão ser disponibilizadas aos sistemas ou módulos responsáveis.

---

## RN-COMPRAS-079 – Integração Financeira

Informações necessárias à execução financeira deverão ser disponibilizadas aos componentes responsáveis.

---

## RN-COMPRAS-080 – Integração Contábil

Informações necessárias aos registros contábeis deverão ser disponibilizadas aos componentes responsáveis.

---

## RN-COMPRAS-081 – Integração Patrimonial

Bens adquiridos deverão poder gerar informações necessárias ao controle patrimonial.

---

## RN-COMPRAS-082 – Integração com Almoxarifado

Materiais recebidos deverão poder ser encaminhados ao controle de estoque quando aplicável.

---

## RN-COMPRAS-083 – Integração Documental

Documentos deverão poder ser integrados à gestão documental corporativa.

---

## RN-COMPRAS-084 – Integração com Transparência

Informações classificadas como publicáveis deverão poder alimentar os mecanismos de transparência.

---

# 24. Regras de Indicadores

## RN-COMPRAS-085 – Indicadores de Gestão

O domínio deverá disponibilizar dados necessários à geração de indicadores de compras e contratações.

---

## RN-COMPRAS-086 – Origem dos Indicadores

Os indicadores deverão possuir origem de dados identificável.

---

## RN-COMPRAS-087 – Periodicidade

Cada indicador deverá possuir periodicidade de atualização definida.

---

# 25. Regras de Notificação

## RN-COMPRAS-088 – Eventos Notificáveis

Eventos que demandem atuação ou conhecimento de usuários poderão gerar notificações.

---

## RN-COMPRAS-089 – Destinatário

A notificação deverá ser direcionada aos usuários ou grupos responsáveis pelo tratamento do evento.

---

## RN-COMPRAS-090 – Histórico de Notificações

Quando necessário, as notificações deverão possuir histórico de envio e situação.

---

# 26. Regras para Operação Offline

## RN-COMPRAS-091 – Operação sem Conectividade

Funcionalidades de campo previamente habilitadas poderão operar sem conexão com a rede.

---

## RN-COMPRAS-092 – Sincronização

Informações registradas offline deverão ser sincronizadas posteriormente.

---

## RN-COMPRAS-093 – Integridade da Sincronização

A sincronização deverá preservar a integridade e a rastreabilidade dos registros.

---

## RN-COMPRAS-094 – Conflitos

Conflitos decorrentes de sincronização deverão possuir mecanismo definido de tratamento.

---

# 27. Regras de Dados

## RN-COMPRAS-095 – Dados Obrigatórios

Campos classificados como obrigatórios deverão ser preenchidos antes da conclusão da etapa correspondente.

---

## RN-COMPRAS-096 – Consistência

Os dados registrados deverão respeitar as regras de consistência definidas para cada entidade.

---

## RN-COMPRAS-097 – Histórico

Alterações relevantes deverão preservar o histórico necessário à gestão e auditoria.

---

## RN-COMPRAS-098 – Referencial Corporativo

Quando existir cadastro corporativo correspondente, o domínio deverá utilizar o registro corporativo em vez de criar duplicidade.

---

# 28. Regras Financeiras

## RN-COMPRAS-099 – Valores

Valores financeiros deverão possuir tratamento compatível com os padrões corporativos de dados financeiros.

---

## RN-COMPRAS-100 – Consistência Financeira

Informações financeiras relacionadas à contratação deverão permanecer consistentes entre os componentes integrados.

---

## RN-COMPRAS-101 – Histórico Financeiro

Alterações relevantes nos valores deverão preservar histórico suficiente para análise.

---

# 29. Regras de Exceção

## RN-COMPRAS-102 – Tratamento de Exceções

Exceções ao fluxo normal deverão ser formalmente registradas quando permitidas.

---

## RN-COMPRAS-103 – Justificativa

Exceções relevantes deverão possuir justificativa registrada.

---

## RN-COMPRAS-104 – Autoridade Competente

Exceções que dependam de autorização deverão ser aprovadas por autoridade competente.

---

# 30. Regras de Controle de Estado

Os principais objetos do domínio deverão possuir estados controlados.

Exemplo:

```text
Rascunho
   ↓
Submetido
   ↓
Em Análise
   ↓
Aprovado
   ↓
Em Execução
   ↓
Concluído
   ↓
Arquivado
```

## RN-COMPRAS-105 – Transição de Estado

Uma entidade não deverá mudar de estado sem atender às condições necessárias para a transição.

---

## RN-COMPRAS-106 – Transições Permitidas

As transições deverão seguir o fluxo definido para cada processo.

---

## RN-COMPRAS-107 – Registro da Transição

Mudanças relevantes de estado deverão ser rastreáveis.

---

# 31. Regras de Responsabilidade

## RN-COMPRAS-108 – Responsável pelo Processo

Todo processo deverá possuir identificação do responsável ou unidade responsável quando aplicável.

---

## RN-COMPRAS-109 – Responsável pelo Contrato

Todo contrato sujeito a acompanhamento deverá possuir responsável definido conforme as regras aplicáveis.

---

## RN-COMPRAS-110 – Responsabilidade pelo Ato

Atos relevantes deverão possuir identificação do usuário responsável por sua execução.

---

# 32. Regras de Não Replicação

## RN-COMPRAS-111 – Cadastro Único

O domínio não deverá criar cadastros paralelos para entidades já mantidas por serviços corporativos.

---

## RN-COMPRAS-112 – Fonte Oficial

Quando existir fonte corporativa oficial para determinada informação, esta deverá ser utilizada como referência.

---

# 33. Regras de Governança

## RN-COMPRAS-113 – Conformidade Corporativa

O domínio deverá observar as políticas, padrões e normas corporativas do SIGMUN.

---

## RN-COMPRAS-114 – Registro de Decisões

Decisões relevantes relacionadas às regras do domínio deverão ser registradas conforme o modelo corporativo de decisões.

---

## RN-COMPRAS-115 – Mudanças de Regra

Alterações relevantes nas regras de negócio deverão possuir histórico de alteração e justificativa.

---

# 34. Regras Derivadas de Legislação

As regras deste documento não deverão ser utilizadas como substitutas da legislação vigente.

Quando uma regra decorrer de norma legal ou regulamentar, deverá ser registrada posteriormente sua respectiva referência normativa.

Estrutura recomendada:

| Regra          | Base normativa | Dispositivo   | Situação |
| -------------- | -------------- | ------------- | -------- |
| RN-COMPRAS-XXX | Norma          | Artigo/Inciso | Vigente  |

A identificação normativa deverá ser validada antes da transformação da regra em requisito obrigatório.

---

# 35. Rastreabilidade

A cadeia de rastreabilidade recomendada é:

```text
Serviço
   ↓
Caso de Uso
   ↓
História de Usuário
   ↓
Regra de Negócio
   ↓
Requisito Funcional
   ↓
Critério de Aceitação
   ↓
Caso de Teste
```

Uma regra poderá estar relacionada a:

* uma ou várias histórias;
* um ou vários requisitos;
* um ou vários casos de uso;
* vários critérios de aceitação;
* vários testes.

---

# 36. Matriz Inicial de Rastreabilidade

| Regra                | Área                         |
| -------------------- | ---------------------------- |
| RN-COMPRAS-001 a 004 | Governança e rastreabilidade |
| RN-COMPRAS-005 a 008 | Planejamento                 |
| RN-COMPRAS-009 a 015 | Requisições                  |
| RN-COMPRAS-016 a 019 | Especificação                |
| RN-COMPRAS-020 a 024 | Pesquisa de preços           |
| RN-COMPRAS-025 a 029 | Processo de contratação      |
| RN-COMPRAS-030 a 033 | Fornecedores                 |
| RN-COMPRAS-034 a 039 | Formalização                 |
| RN-COMPRAS-040 a 045 | Execução e fiscalização      |
| RN-COMPRAS-046 a 048 | Vigência                     |
| RN-COMPRAS-049 a 052 | Alterações contratuais       |
| RN-COMPRAS-053 a 056 | Recebimento                  |
| RN-COMPRAS-057 a 059 | Encerramento                 |
| RN-COMPRAS-060 a 063 | Gestão documental            |
| RN-COMPRAS-064 a 067 | Transparência                |
| RN-COMPRAS-068 a 071 | Auditoria                    |
| RN-COMPRAS-072 a 074 | Segregação de funções        |
| RN-COMPRAS-075 a 077 | Permissões                   |
| RN-COMPRAS-078 a 084 | Integrações                  |
| RN-COMPRAS-085 a 087 | Indicadores                  |
| RN-COMPRAS-088 a 090 | Notificações                 |
| RN-COMPRAS-091 a 094 | Operação offline             |
| RN-COMPRAS-095 a 098 | Dados                        |
| RN-COMPRAS-099 a 101 | Financeiro                   |
| RN-COMPRAS-102 a 104 | Exceções                     |
| RN-COMPRAS-105 a 107 | Estados                      |
| RN-COMPRAS-108 a 110 | Responsabilidades            |
| RN-COMPRAS-111 a 112 | Não replicação               |
| RN-COMPRAS-113 a 115 | Governança                   |

---

# 37. Regras e Critérios de Aceitação

Cada regra que produzir comportamento observável no sistema deverá posteriormente possuir critérios de aceitação.

Exemplo:

```text
RN-COMPRAS-047
Controle de Vigência
        ↓
RF-COMPRAS-XXX
        ↓
CA-COMPRAS-XXX
        ↓
TEST-COMPRAS-XXX
```

---

# 38. Regras e Requisitos Não Funcionais

Algumas regras poderão originar requisitos não funcionais relacionados a:

* segurança;
* disponibilidade;
* desempenho;
* auditoria;
* integridade;
* interoperabilidade;
* acessibilidade;
* rastreabilidade;
* privacidade;
* continuidade.

---

# 39. Regras e Integrações

As regras de integração deverão ser refinadas posteriormente em contratos de integração.

A arquitetura deverá evitar dependência indevida entre domínios e privilegiar:

* serviços corporativos;
* APIs;
* eventos;
* contratos de dados;
* mecanismos de sincronização;
* padrões de interoperabilidade.

---

# 40. Regras e Legislação

A legislação aplicável deverá ser tratada como fonte normativa externa e versionada independentemente.

Quando uma norma for alterada, deverá ser avaliado o impacto sobre:

* regras de negócio;
* requisitos;
* processos;
* casos de uso;
* histórias;
* critérios de aceitação;
* testes;
* integrações;
* relatórios.

---

# 41. Gestão de Mudanças

Uma alteração de regra de negócio deverá gerar, quando aplicável:

1. identificação da mudança;
2. justificativa;
3. análise de impacto;
4. aprovação;
5. atualização da regra;
6. atualização dos requisitos afetados;
7. atualização dos critérios de aceitação;
8. atualização dos testes;
9. registro da versão.

---

# 42. Controle de Versões

| Versão | Data       | Descrição                                                                    |
| ------ | ---------- | ---------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação das Regras de Negócio do Domínio de Gestão de Compras e Contratações |

---

# 43. Próximo Artefato

Após este documento, recomenda-se criar:

`008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md`

A sequência do domínio passa a ser:

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
```

---

**Documento:** 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
