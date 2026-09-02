# 010 — Ética, Integridade e Compliance

**Projeto:** Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA (SIGMUN)  
**Classificação da Informação:** Pública  
**Natureza:** Arquitetura Corporativa / Governança  
**Versão:** 1.0  
**Data:** 2026-08-15  
**Status da revisão:** Vigente  
**Responsável:** Governança do SIGMUN

---

## 1. Objetivo

Este documento estabelece a **Arquitetura de Gestão da Ética, Integridade e Compliance do SIGMUN**, definindo princípios, responsabilidades, mecanismos de prevenção, controles, monitoramento e resposta destinados a assegurar que o desenvolvimento, a implantação, a operação e a evolução da plataforma ocorram em conformidade com a legislação aplicável, os princípios da Administração Pública e as diretrizes corporativas do SIGMUN.

A arquitetura busca fortalecer a cultura ética, prevenir irregularidades, reduzir riscos de fraude e corrupção, promover transparência, assegurar rastreabilidade e apoiar a responsabilização adequada dos agentes envolvidos nos processos administrativos, operacionais e tecnológicos.

A ética, a integridade e o compliance deverão ser considerados elementos estruturantes da governança do SIGMUN e não apenas mecanismos de controle posteriores à ocorrência de irregularidades.

---

## 2. Finalidade

A Arquitetura de Ética, Integridade e Compliance tem como finalidades:

- apoiar a prevenção de fraude, corrupção, conflito de interesses e outras irregularidades;
- promover comportamento ético na utilização e administração do SIGMUN;
- estabelecer mecanismos de prevenção, detecção, resposta e correção;
- fortalecer a transparência e a prestação de contas;
- assegurar rastreabilidade das operações relevantes;
- apoiar a segregação adequada de funções;
- reduzir riscos relacionados à concentração indevida de poderes;
- preservar evidências necessárias à auditoria e à fiscalização;
- integrar ética, integridade e compliance à gestão corporativa de riscos;
- integrar controles de integridade à segurança da informação e à proteção de dados;
- apoiar programas institucionais de integridade dos órgãos e entidades participantes;
- estabelecer mecanismos de monitoramento e melhoria contínua;
- promover conformidade com requisitos legais, regulamentares e institucionais.

---

## 3. Princípios

A gestão da ética, integridade e compliance observará, entre outros, os seguintes princípios:

### 3.1 Interesse público

As decisões e operações apoiadas pelo SIGMUN deverão priorizar o interesse coletivo e a finalidade pública.

### 3.2 Legalidade

As operações deverão observar a legislação aplicável e as competências legalmente estabelecidas para cada órgão, unidade, autoridade ou agente.

### 3.3 Impessoalidade

Os processos deverão ser conduzidos de forma objetiva, evitando favorecimentos, perseguições, privilégios ou discriminações indevidas.

### 3.4 Moralidade administrativa

As ações deverão observar padrões de honestidade, boa-fé, responsabilidade e comportamento compatíveis com o exercício da função pública.

### 3.5 Transparência

As informações públicas deverão ser disponibilizadas de forma transparente, observadas as restrições legais, a proteção de dados pessoais e a classificação da informação.

### 3.6 Rastreabilidade

Decisões e operações relevantes deverão permitir a identificação dos responsáveis, das alterações realizadas e das evidências correspondentes.

### 3.7 Prevenção

Os controles deverão priorizar a prevenção de irregularidades em vez de depender exclusivamente da detecção posterior.

### 3.8 Proporcionalidade

Os controles deverão ser proporcionais ao risco, à criticidade do processo e à natureza da operação.

### 3.9 Segregação de funções

Funções incompatíveis deverão ser separadas sempre que aplicável, reduzindo riscos de fraude, erro, conflito de interesses ou abuso de autoridade.

### 3.10 Evidência

Operações relevantes deverão possuir evidências suficientes para reconstrução posterior dos fatos e suporte a auditorias e fiscalizações.

### 3.11 Independência dos controles

As atividades de controle, auditoria e avaliação deverão preservar, sempre que aplicável, independência suficiente em relação às atividades avaliadas.

### 3.12 Melhoria contínua

As não conformidades, incidentes e resultados de auditoria deverão alimentar ciclos permanentes de melhoria.

### 3.13 Princípios corporativos do SIGMUN

A gestão da ética, integridade e compliance deverá observar os princípios corporativos estabelecidos na Constituição do Projeto SIGMUN:

> **Transparência por padrão, Segurança por princípio e Classificação da Informação por política.**

Também será observado o princípio:

> **Aberto sempre que possível, restrito sempre que necessário.**

A transparência não deverá ser utilizada como justificativa para exposição indevida de informações protegidas, dados pessoais, informações classificadas ou evidências de natureza restrita.

---

## 4. Abrangência

Esta arquitetura aplica-se a:

- órgãos e unidades administrativas participantes do SIGMUN;
- gestores;
- servidores;
- agentes públicos;
- usuários internos;
- usuários externos autorizados;
- equipes técnicas;
- administradores da plataforma;
- desenvolvedores;
- fornecedores;
- prestadores de serviços;
- parceiros institucionais;
- processos administrativos;
- processos operacionais;
- módulos e serviços do SIGMUN;
- integrações;
- APIs;
- bancos de dados;
- infraestrutura tecnológica;
- dispositivos móveis;
- serviços de campo;
- mecanismos automatizados;
- recursos de Inteligência Artificial, quando utilizados.

As obrigações deverão observar a competência legal de cada órgão, unidade, função ou autoridade.

---

## 5. Referencial Legal e Normativo

Esta arquitetura deverá observar, conforme aplicabilidade e vigência, a legislação brasileira pertinente à Administração Pública, integridade, transparência, contratações, proteção de dados, segurança da informação, controle e responsabilização.

Entre os principais referenciais estão:

- Constituição Federal;
- Lei nº 8.429/1992 — Lei de Improbidade Administrativa, conforme alterações e legislação vigente;
- Lei nº 12.527/2011 — Lei de Acesso à Informação;
- Lei nº 12.846/2013 — Lei Anticorrupção;
- Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais;
- Lei nº 14.133/2021 — Lei de Licitações e Contratos Administrativos;
- legislação relacionada à transparência e ao controle da Administração Pública;
- normas e orientações dos órgãos de controle aplicáveis;
- políticas corporativas do SIGMUN;
- normas internas da Prefeitura Municipal de Camacan-BA;
- demais requisitos legais e regulamentares aplicáveis.

A identificação de requisitos legais específicos deverá ser mantida e atualizada conforme alterações legislativas, regulamentares ou institucionais.

---

## 6. Governança da Ética, Integridade e Compliance

A governança da integridade do SIGMUN deverá estar integrada à estrutura geral de governança corporativa.

Deverão ser definidos:

- responsabilidades;
- competências;
- níveis de autoridade;
- mecanismos de decisão;
- mecanismos de controle;
- mecanismos de monitoramento;
- mecanismos de prestação de contas;
- processos de tratamento de não conformidades;
- mecanismos de escalonamento;
- critérios para tratamento de exceções.

Cada instância deverá possuir responsabilidades e níveis de autoridade claramente definidos.

Nenhum mecanismo tecnológico deverá substituir a competência legal de uma autoridade pública.

---

## 7. Responsabilidades

### 7.1 Governança do SIGMUN

Compete à Governança do SIGMUN:

- estabelecer diretrizes corporativas;
- supervisionar a aplicação desta arquitetura;
- promover integração entre governança, riscos, auditoria e compliance;
- acompanhar indicadores;
- avaliar exceções relevantes;
- promover melhoria contínua.

### 7.2 Governança da Arquitetura

Compete à Governança da Arquitetura:

- garantir alinhamento desta arquitetura com a arquitetura corporativa;
- avaliar impactos arquiteturais de novos controles;
- manter rastreabilidade dos artefatos;
- assegurar coerência entre políticas, processos e soluções tecnológicas.

### 7.3 Gestores

Compete aos gestores:

- aplicar as políticas de integridade;
- assegurar que os processos sob sua responsabilidade possuam controles adequados;
- promover segregação de funções;
- tratar não conformidades;
- apoiar auditorias;
- assegurar capacitação das equipes.

### 7.4 Usuários

Os usuários deverão:

- utilizar o SIGMUN somente para finalidades autorizadas;
- proteger suas credenciais;
- respeitar as políticas corporativas;
- comunicar incidentes ou irregularidades;
- preservar informações sob sua responsabilidade.

### 7.5 Equipes técnicas

As equipes técnicas deverão:

- implementar controles definidos pela arquitetura;
- preservar registros de auditoria;
- evitar acessos incompatíveis com suas funções;
- aplicar princípios de segurança;
- manter rastreabilidade de alterações;
- comunicar vulnerabilidades e incidentes.

---

## 8. Conduta Ética na Utilização do SIGMUN

A utilização do SIGMUN deverá observar princípios de conduta compatíveis com a função pública.

É vedada a utilização do SIGMUN para:

- obtenção de vantagem indevida;
- favorecimento pessoal;
- perseguição;
- manipulação indevida de registros;
- ocultação de informações que deveriam ser preservadas;
- alteração não autorizada de dados;
- acesso incompatível com a função;
- compartilhamento indevido de credenciais;
- qualquer finalidade contrária à legislação ou às políticas institucionais.

As violações deverão ser tratadas conforme a legislação e os procedimentos institucionais aplicáveis.

---

## 9. Programa de Integridade

O Programa de Integridade do SIGMUN deverá estabelecer mecanismos permanentes para prevenir, detectar, responder e corrigir desvios éticos, irregularidades, fraudes e demais riscos relacionados à integridade.

O programa deverá contemplar, quando aplicável:

1. avaliação de riscos;
2. controles preventivos;
3. controles detectivos;
4. mecanismos de denúncia;
5. investigação;
6. tratamento de não conformidades;
7. aplicação de medidas corretivas;
8. monitoramento;
9. capacitação;
10. comunicação;
11. revisão periódica;
12. melhoria contínua.

O programa deverá ser baseado em melhoria contínua e considerar os riscos específicos dos processos municipais.

---

## 10. Prevenção de Fraudes e Corrupção

O SIGMUN deverá apoiar mecanismos de prevenção, detecção e tratamento de fraudes e corrupção.

Poderão ser utilizados, conforme aplicabilidade:

- regras de validação;
- controles de acesso;
- segregação de funções;
- trilhas de auditoria;
- alertas;
- análise de inconsistências;
- análise de padrões anômalos;
- bloqueios preventivos;
- aprovação em múltiplos níveis;
- registros de evidências;
- monitoramento de operações críticas.

Os controles deverão observar os princípios de proporcionalidade, necessidade e adequação.

---

## 11. Conflito de Interesses

A utilização do SIGMUN deverá apoiar mecanismos destinados a prevenir e identificar situações de conflito de interesses.

Quando aplicável, deverão ser observados:

- declaração de impedimentos;
- declaração de conflito de interesses;
- afastamento do agente impedido;
- substituição formal;
- segregação de funções;
- registro da decisão;
- preservação das evidências.

A existência de conflito deverá ser tratada conforme a legislação e as normas institucionais aplicáveis.

---

## 12. Segregação de Funções

O SIGMUN deverá apoiar mecanismos que reduzam concentrações indevidas de responsabilidades.

Como princípio geral:

- quem administra usuários não deve, por padrão, possuir autorização incompatível com essa função;
- quem homologa não deve realizar alterações diretamente em produção, salvo procedimento excepcional devidamente autorizado e registrado;
- quem desenvolve não deve possuir, por padrão, poderes irrestritos de homologação;
- quem aprova uma operação crítica não deve ser, quando aplicável, o mesmo responsável por executá-la;
- quem controla uma operação não deve concentrar indevidamente todas as etapas do processo.

A matriz de segregação de funções deverá ser parametrizável quando aplicável ao processo.

Exceções deverão possuir:

- justificativa;
- autorização;
- período de validade;
- responsável;
- evidência;
- avaliação de risco.

---

## 13. Rastreabilidade e Trilhas de Auditoria

Operações relevantes deverão possuir mecanismos de rastreabilidade compatíveis com sua criticidade.

A rastreabilidade deverá permitir, quando aplicável, reconstruir:

- quem realizou a operação;
- quando realizou;
- qual operação foi realizada;
- quais dados foram alterados;
- qual era o estado anterior;
- qual passou a ser o novo estado;
- qual autoridade autorizou;
- qual processo originou a operação;
- quais evidências estavam associadas;
- quais integrações participaram da operação.

As trilhas de auditoria deverão possuir mecanismos adequados de proteção contra alteração ou exclusão indevida.

---

## 14. Preservação de Evidências

A preservação das evidências deverá observar os requisitos de segurança, privacidade, proteção de dados e retenção documental.

Poderão constituir evidências:

- registros de auditoria;
- documentos;
- atos administrativos;
- aprovações;
- versões;
- registros de alterações;
- logs;
- metadados;
- documentos eletrônicos;
- registros de integração;
- evidências coletadas por dispositivos móveis;
- fotografias e demais registros autorizados;
- registros de workflow.

Os períodos de retenção deverão observar as políticas corporativas e a legislação aplicável.

---

## 15. Canal de Denúncias e Comunicação de Irregularidades

O SIGMUN poderá apoiar a disponibilização de canal institucional destinado ao recebimento de denúncias, comunicações de irregularidades ou manifestações relacionadas à integridade.

Quando disponibilizado, o canal deverá observar:

- legislação aplicável;
- proteção de dados pessoais;
- confidencialidade;
- segurança da informação;
- preservação de evidências;
- tratamento adequado das informações;
- proteção contra acesso indevido;
- mecanismos de acompanhamento;
- procedimentos de encaminhamento.

A existência de mecanismos tecnológicos não deverá impedir outros canais oficiais estabelecidos pelo Município.

---

## 16. Transparência e Publicidade

A transparência deverá observar o princípio:

> **Aberto sempre que possível, restrito sempre que necessário.**

A publicação deverá observar a **Política de Classificação da Informação e Publicação de Artefatos**.

As informações públicas deverão ser disponibilizadas de forma adequada, acessível e rastreável, observadas:

- legislação de acesso à informação;
- proteção de dados pessoais;
- sigilos legalmente estabelecidos;
- segurança da informação;
- classificação da informação;
- direitos de terceiros.

---

## 17. Fornecedores e Terceiros

Sempre que aplicável e proporcional ao risco, fornecedores e terceiros poderão ser submetidos a requisitos de integridade.

Os critérios deverão observar a legislação de contratações públicas e as políticas corporativas.

Poderão ser considerados:

- requisitos de integridade;
- conflito de interesses;
- histórico de conformidade;
- controles de acesso;
- confidencialidade;
- proteção de dados;
- segurança da informação;
- responsabilidades contratuais;
- obrigação de comunicação de incidentes;
- auditoria e fiscalização;
- tratamento de subcontratados.

Contratos e instrumentos equivalentes deverão estabelecer responsabilidades compatíveis com os riscos envolvidos.

---

## 18. Controles de Acesso

Os acessos deverão observar os princípios de:

- necessidade de conhecer;
- menor privilégio;
- segregação de funções;
- responsabilidade individual;
- autenticação adequada;
- revisão periódica;
- rastreabilidade.

A concessão, alteração e revogação de acessos deverão ser registradas.

Acessos incompatíveis com a função deverão ser identificados e tratados.

---

## 19. Monitoramento de Compliance

Toda não conformidade relevante deverá possuir registro compatível com sua criticidade.

O programa de Compliance deverá utilizar mecanismos de monitoramento compatíveis com os riscos identificados.

Poderão ser utilizados:

- indicadores;
- auditorias;
- avaliações;
- testes de controles;
- relatórios;
- alertas;
- análises automatizadas;
- inspeções;
- revisões periódicas.

Sempre que tecnicamente viável, controles automatizados poderão produzir alertas para situações potencialmente incompatíveis com as regras estabelecidas.

Os alertas deverão ser tratados conforme procedimentos definidos.

---

## 20. Indicadores de Integridade

Os indicadores deverão ser integrados, quando aplicável, à arquitetura corporativa de indicadores.

Poderão ser monitorados, entre outros:

- quantidade de não conformidades;
- quantidade de incidentes;
- tempo de tratamento;
- reincidência;
- controles preventivos executados;
- exceções concedidas;
- acessos incompatíveis identificados;
- resultados de auditorias;
- treinamentos realizados;
- denúncias recebidas;
- denúncias tratadas;
- riscos de integridade;
- efetividade dos controles.

Os indicadores deverão ser utilizados para tomada de decisão e melhoria contínua.

---

## 21. Capacitação

Os usuários e equipes envolvidos no SIGMUN deverão receber capacitação compatível com suas responsabilidades.

A capacitação deverá contemplar, quando aplicável:

- ética;
- integridade;
- segurança;
- proteção de dados;
- uso adequado do SIGMUN;
- segregação de funções;
- prevenção de fraudes;
- responsabilidades;
- tratamento de incidentes;
- classificação da informação;
- transparência.

A capacitação deverá ser periódica e poderá ser diferenciada por perfil de usuário.

---

## 22. Tratamento de Incidentes de Integridade

Incidentes relacionados à ética, integridade ou compliance deverão ser tratados conforme sua natureza e criticidade.

O tratamento poderá envolver:

1. identificação;
2. registro;
3. classificação;
4. contenção;
5. preservação de evidências;
6. análise;
7. encaminhamento;
8. decisão;
9. correção;
10. monitoramento;
11. encerramento;
12. lições aprendidas.

Quando aplicável, o incidente deverá resultar na revisão do registro corporativo de riscos, controles, políticas ou procedimentos.

---

## 23. Exceções

Exceções permanentes deverão ser evitadas sempre que houver possibilidade de tratamento estrutural.

Quando uma exceção for necessária, deverá possuir:

- justificativa;
- avaliação de risco;
- autoridade competente;
- período de validade;
- responsável;
- controles compensatórios;
- registro;
- revisão periódica.

Exceções deverão ser rastreáveis e auditáveis.

---

## 24. Automação e Controles Inteligentes

Sempre que tecnicamente viável e juridicamente adequado, os controles poderão ser automatizados.

A automação deverá apoiar:

- prevenção;
- validação;
- detecção;
- monitoramento;
- geração de alertas;
- análise;
- auditoria;
- prestação de contas.

A automação deverá apoiar a decisão institucional, não substituindo a autoridade legalmente competente.

---

## 25. Inteligência Artificial

Quando recursos de Inteligência Artificial forem utilizados no SIGMUN, deverão ser observados requisitos adicionais de:

- transparência;
- rastreabilidade;
- segurança;
- proteção de dados;
- supervisão humana;
- avaliação de riscos;
- explicabilidade compatível com a finalidade;
- controle de acesso;
- registro de decisões relevantes.

Decisões administrativas relevantes não deverão ser delegadas exclusivamente a mecanismos automatizados quando a legislação ou a natureza da decisão exigir atuação humana competente.

Modelos de IA deverão ser utilizados de forma compatível com as políticas corporativas e com os requisitos legais aplicáveis.

---

## 26. Integração com Gestão de Riscos

A ética, integridade e compliance deverão estar integrados à Gestão de Riscos Corporativos.

Riscos relacionados a:

- fraude;
- corrupção;
- conflito de interesses;
- acesso indevido;
- manipulação de dados;
- falhas de controle;
- indisponibilidade de evidências;
- descumprimento legal;
- abuso de privilégios;

deverão ser identificados e tratados no processo corporativo de gestão de riscos.

Os controles de integridade deverão ser vinculados aos riscos correspondentes sempre que aplicável.

---

## 27. Integração com Segurança da Informação

A gestão de integridade deverá manter integração com a Arquitetura de Segurança da Informação.

Os controles deverão observar requisitos de:

- confidencialidade;
- integridade;
- disponibilidade;
- autenticidade;
- rastreabilidade;
- controle de acesso;
- gestão de vulnerabilidades;
- resposta a incidentes.

A integridade dos registros deverá ser protegida contra alteração não autorizada.

---

## 28. Integração com Proteção de Dados Pessoais

Os mecanismos de integridade deverão respeitar os princípios e requisitos aplicáveis à proteção de dados pessoais.

O tratamento de informações relacionadas a denúncias, investigações, usuários ou agentes deverá observar:

- finalidade;
- adequação;
- necessidade;
- segurança;
- prevenção;
- responsabilização;
- direitos dos titulares;
- controles de acesso;
- retenção adequada.

A busca por transparência não deverá resultar em exposição indevida de dados pessoais.

---

## 29. Integração com Auditoria e Controle

Resultados de auditorias e avaliações deverão alimentar a melhoria dos controles.

A arquitetura deverá apoiar:

- auditoria interna;
- auditoria externa;
- controle interno;
- fiscalização;
- inspeções;
- avaliações de conformidade;
- prestação de contas.

As evidências necessárias deverão ser preservadas durante o período definido pelas políticas e normas aplicáveis.

---

## 30. Integração com Continuidade e Gestão de Crises

Os mecanismos de ética, integridade e compliance deverão considerar cenários de:

- indisponibilidade;
- perda de dados;
- comprometimento de credenciais;
- incidentes de segurança;
- indisponibilidade de sistemas críticos;
- crises institucionais;
- comprometimento de evidências.

Os controles deverão permanecer compatíveis com os planos corporativos de continuidade de negócios, recuperação de desastres e gestão de crises.

---

## 31. Aplicação aos Domínios do SIGMUN

As diretrizes desta arquitetura deverão ser consideradas pelos demais domínios e módulos do SIGMUN, respeitando as responsabilidades e competências de cada área.

O domínio **Gestão de Compras e Contratações**, por exemplo, deverá aplicar essas diretrizes especialmente em processos de:

- planejamento de contratações;
- compras;
- licitações;
- contratação direta;
- gestão contratual;
- fiscalização;
- recebimento;
- pagamento;
- gestão de fornecedores;
- aplicação de sanções.

Os controles de integridade deverão ser incorporados aos processos desde sua concepção.

---

## 32. Gestão Documental e Integridade

Os documentos e evidências relacionados à ética, integridade e compliance deverão observar as políticas corporativas de gestão documental.

Deverão ser preservados, quando aplicável:

- documentos oficiais;
- versões;
- registros de aprovação;
- evidências de execução;
- pareceres;
- relatórios;
- decisões;
- registros de auditoria;
- registros de exceções.

A retenção e o descarte deverão observar os critérios corporativos e legais.

---

## 33. Gestão de Mudanças

Alterações em processos, sistemas, regras ou controles que possam afetar a integridade deverão ser avaliadas antes da implantação.

A avaliação poderá considerar:

- impacto nos controles;
- impacto nos riscos;
- impacto na segregação de funções;
- impacto na rastreabilidade;
- impacto na proteção de dados;
- impacto na segurança;
- necessidade de atualização documental.

As alterações deverão ser registradas no histórico de versões e, quando aplicável, relacionadas a decisões arquiteturais ou documentos corporativos correspondentes.

---

## 34. Conflitos entre Normas e Requisitos

Quando houver conflito entre regras, políticas ou requisitos, deverá ser realizada análise formal considerando:

1. legislação aplicável;
2. competência institucional;
3. hierarquia normativa;
4. risco;
5. segurança;
6. proteção de dados;
7. transparência;
8. interesse público.

A decisão deverá ser registrada e, quando aplicável, submetida à instância competente.

---

## 35. Rastreabilidade Corporativa

A Arquitetura de Ética, Integridade e Compliance deverá manter rastreabilidade com os demais artefatos corporativos do SIGMUN.

Essa rastreabilidade deverá estar integrada ao:

- Mapa Mestre de Artefatos e Rastreabilidade;
- Framework Corporativo de Gestão de Requisitos e Rastreabilidade;
- Registro de Decisões Arquiteturais;
- políticas corporativas;
- modelos de processos;
- requisitos;
- controles;
- riscos;
- indicadores;
- evidências.

Cada requisito relevante deverá possuir vínculo com o controle, processo ou artefato correspondente quando aplicável.

---

## 36. Critério de Conformidade

Um processo ou componente será considerado adequadamente alinhado a esta arquitetura quando:

- possuir requisitos de integridade identificados;
- possuir riscos avaliados;
- possuir controles proporcionais;
- possuir responsabilidades definidas;
- possuir segregação adequada;
- possuir rastreabilidade;
- possuir evidências;
- possuir tratamento de exceções;
- possuir mecanismos de monitoramento;
- estiver alinhado às políticas corporativas;
- possuir documentação compatível;
- estiver sujeito à revisão periódica.

---

## 37. Auditoria da Arquitetura

A aplicação desta arquitetura poderá ser avaliada por meio de auditorias e avaliações periódicas.

A avaliação poderá verificar:

- aderência aos princípios;
- efetividade dos controles;
- segregação de funções;
- rastreabilidade;
- tratamento de exceções;
- gestão de incidentes;
- capacitação;
- indicadores;
- conformidade documental;
- integração com riscos;
- integração com segurança;
- integração com proteção de dados.

Os resultados deverão alimentar a melhoria contínua.

---

## 38. Gestão de Não Conformidades

Não conformidades identificadas deverão ser:

1. registradas;
2. classificadas;
3. avaliadas;
4. atribuídas a responsável;
5. tratadas;
6. acompanhadas;
7. encerradas mediante evidência;
8. utilizadas para melhoria quando aplicável.

Não conformidades críticas deverão ser escaladas para a autoridade competente.

---

## 39. Revisão da Arquitetura

Esta arquitetura deverá ser revisada periodicamente ou sempre que ocorrer:

- alteração legislativa relevante;
- alteração na estrutura de governança;
- alteração significativa da plataforma;
- identificação de novo risco;
- ocorrência de incidente relevante;
- resultado de auditoria que exija mudança;
- alteração de políticas corporativas;
- adoção de nova tecnologia relevante.

As alterações deverão preservar o histórico das versões anteriores.

---

## 40. Artefatos Relacionados

Esta arquitetura possui relação direta ou complementar com os seguintes artefatos do SIGMUN:

### Governança

- `009-Governanca-da-Arquitetura.md`
- `013-Plano-de-Governanca-de-Dados.md`
- `014-Plano-de-Governanca-de-Indicadores.md`
- `015-Plano-de-Auditoria.md`
- `016-Plano-de-Gestao-de-Conformidade.md`
- `017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md`
- `018-Plano-de-Gestao-de-Crises.md`
- `019-Plano-de-Comunicacao-Engajamento-e-Colaboracao-da-Comunidade-SIGMUN.md`
- `020-Politica-de-Classificacao-da-Informacao-e-Publicacao-de-Artefatos.md`

### Políticas Corporativas

- `019-Politica-de-Governanca-Digital.md`
- `020-Politica-de-Qualidade.md`
- `021-Politica-de-Seguranca.md`
- `022-Politica-de-Gestao-Documental.md`
- `023-Politica-de-Retencao-e-Descarte-de-Documentos.md`
- `024-Politica-de-Gestao-de-Riscos.md`
- `025-Politica-de-Protecao-de-Dados-Pessoais.md`
- `026-Manual-de-Governanca-do-SIGMUN.md`

### Artefatos Corporativos

- `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
- `000F-Registro-de-Decisoes-Arquiteturais(ADR-Arqhiteture-Decision-Records).md`
- `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

## 41. Matriz Resumida de Controles

| Área | Controle | Objetivo |
|---|---|---|
| Ética | Código e diretrizes de conduta | Promover comportamento ético |
| Integridade | Programa de Integridade | Prevenir e tratar irregularidades |
| Riscos | Avaliação de riscos de integridade | Identificar vulnerabilidades |
| Acesso | Menor privilégio | Reduzir acessos indevidos |
| Segregação | Separação de funções incompatíveis | Reduzir risco de fraude |
| Auditoria | Trilhas de auditoria | Preservar rastreabilidade |
| Evidências | Preservação de registros | Apoiar fiscalização |
| Transparência | Publicação adequada | Promover prestação de contas |
| Proteção de dados | Controles de acesso e tratamento | Proteger dados pessoais |
| Segurança | Controles técnicos | Preservar integridade e segurança |
| Compliance | Monitoramento | Detectar desvios |
| Incidentes | Tratamento estruturado | Responder a irregularidades |
| Capacitação | Treinamento | Fortalecer cultura de integridade |
| Fornecedores | Requisitos de integridade | Reduzir riscos de terceiros |
| Mudanças | Avaliação de impacto | Evitar degradação dos controles |

---

## 42. Conclusão

A Arquitetura de Gestão da Ética, Integridade e Compliance estabelece princípios, responsabilidades e mecanismos destinados a assegurar que o SIGMUN seja desenvolvido, implantado, operado e evoluído com elevados padrões de ética, transparência, responsabilidade e conformidade.

Ao integrar mecanismos de prevenção, detecção e tratamento de irregularidades com governança, gestão de riscos, segurança da informação, proteção de dados, auditoria e controle interno, o SIGMUN fortalece a capacidade institucional de prevenir desvios, preservar evidências, promover a prestação de contas e apoiar uma Administração Pública mais íntegra, eficiente e transparente.

Esta arquitetura deverá ser observada como referência corporativa para os demais domínios, processos, módulos, serviços e componentes do SIGMUN.

---

## 43. Controle de Versão

| Versão | Data | Descrição | Responsável |
|---|---|---|---|
| 1.0 | 2026-08-15 | Criação/reconsolidação da Arquitetura de Gestão da Ética, Integridade e Compliance | Governança do SIGMUN |

---

**Status:** Vigente  
**Classificação:** Pública  
**Próxima revisão:** Conforme ciclo de revisão da Governança do SIGMUN
