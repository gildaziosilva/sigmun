# 009 – Requisitos Não Funcionais – Gestão de Compras e Contratações

#### Requisitos Não Funcionais – Gestão de Compras e Contratações

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
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
* 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
* 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
* 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
* 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
* 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
* 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
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

Este documento define os **Requisitos Não Funcionais do Domínio de Gestão de Compras e Contratações** do SIGMUN.

Os requisitos não funcionais estabelecem características, restrições, atributos de qualidade, condições operacionais e requisitos técnicos que deverão ser observados na implementação das funcionalidades do domínio.

Eles complementam os requisitos funcionais e estabelecem **como o sistema deverá operar**, além de definir características relacionadas a:

* segurança;
* desempenho;
* disponibilidade;
* confiabilidade;
* escalabilidade;
* usabilidade;
* acessibilidade;
* interoperabilidade;
* auditabilidade;
* rastreabilidade;
* manutenção;
* observabilidade;
* portabilidade;
* recuperação;
* continuidade;
* proteção de dados;
* operação offline.

---

# 2. Princípios

Os requisitos não funcionais deste domínio deverão observar os princípios corporativos do SIGMUN:

* Segurança por princípio.
* Privacidade e proteção de dados desde a concepção.
* Transparência por padrão.
* Classificação da informação por política.
* Aberto sempre que possível, restrito sempre que necessário.
* Interoperabilidade por padrão.
* Reutilização de serviços corporativos.
* Rastreabilidade integral.
* Auditabilidade.
* Configurabilidade.
* Evolução incremental.
* Arquitetura orientada a domínios.
* Independência tecnológica sempre que possível.

---

# 3. Convenção de Identificação

Os requisitos não funcionais utilizarão o padrão:

```text
RNF-COMPRAS-XXX
```

Exemplo:

```text
RNF-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida do requisito.

---

# 4. Classificação

Os requisitos não funcionais serão agrupados nas seguintes categorias:

| Código    | Categoria                       |
| --------- | ------------------------------- |
| RNF-SEG   | Segurança                       |
| RNF-PRIV  | Privacidade e Proteção de Dados |
| RNF-PERF  | Desempenho                      |
| RNF-DISP  | Disponibilidade                 |
| RNF-CONF  | Confiabilidade                  |
| RNF-ESC   | Escalabilidade                  |
| RNF-USAB  | Usabilidade                     |
| RNF-ACESS | Acessibilidade                  |
| RNF-INT   | Interoperabilidade              |
| RNF-AUD   | Auditoria                       |
| RNF-OBS   | Observabilidade                 |
| RNF-DOC   | Gestão Documental               |
| RNF-OFF   | Operação Offline                |
| RNF-SINC  | Sincronização                   |
| RNF-MAN   | Manutenibilidade                |
| RNF-EVOL  | Evolução                        |
| RNF-PORT  | Portabilidade                   |
| RNF-REC   | Recuperação                     |
| RNF-CONT  | Continuidade                    |
| RNF-DADOS | Qualidade de Dados              |
| RNF-TRANS | Transparência                   |

---

# 5. Segurança

## RNF-COMPRAS-001 – Controle de Acesso

O sistema deverá controlar o acesso às funcionalidades e informações do domínio conforme identidade, perfil, função, unidade administrativa e permissões atribuídas.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-002 – Autenticação

O acesso às funcionalidades protegidas deverá exigir autenticação válida conforme o serviço corporativo de identidade do SIGMUN.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-003 – Autorização

As operações deverão ser autorizadas antes de sua execução.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-004 – Segregação de Funções

O sistema deverá suportar segregação de funções para impedir combinações indevidas de responsabilidades.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-005 – Privilégio Mínimo

Os usuários deverão possuir somente as permissões necessárias para execução de suas atribuições.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-006 – Proteção contra Acesso Indevido

O sistema deverá impedir acesso a processos, documentos, contratos e informações não autorizadas.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-007 – Proteção das Sessões

As sessões autenticadas deverão possuir mecanismos adequados de proteção, expiração e invalidação.

**Categoria:** Segurança

**Prioridade:** P1

---

## RNF-COMPRAS-008 – Proteção das Comunicações

As comunicações entre cliente, servidores, APIs e integrações deverão utilizar mecanismos seguros de transporte.

**Categoria:** Segurança

**Prioridade:** P0

---

# 6. Privacidade e Proteção de Dados

## RNF-COMPRAS-009 – Proteção de Dados Pessoais

O domínio deverá tratar dados pessoais de acordo com as políticas corporativas de proteção de dados e legislação aplicável.

**Categoria:** Privacidade

**Prioridade:** P0

---

## RNF-COMPRAS-010 – Minimização de Dados

O sistema deverá coletar e armazenar somente os dados necessários para as finalidades definidas.

**Categoria:** Privacidade

**Prioridade:** P0

---

## RNF-COMPRAS-011 – Classificação da Informação

As informações deverão possuir classificação conforme a política corporativa de classificação da informação.

**Categoria:** Privacidade

**Prioridade:** P0

---

## RNF-COMPRAS-012 – Controle de Exposição

Dados classificados como restritos, confidenciais ou protegidos não deverão ser disponibilizados em mecanismos públicos.

**Categoria:** Privacidade

**Prioridade:** P0

---

## RNF-COMPRAS-013 – Mascaramento

Quando aplicável, informações sensíveis deverão ser mascaradas em telas, relatórios, logs e ambientes de diagnóstico.

**Categoria:** Privacidade

**Prioridade:** P1

---

# 7. Desempenho

## RNF-COMPRAS-014 – Tempo de Resposta

As operações interativas deverão apresentar tempo de resposta compatível com os padrões corporativos do SIGMUN.

**Categoria:** Desempenho

**Prioridade:** P1

---

## RNF-COMPRAS-015 – Consultas

Consultas frequentes deverão ser projetadas para evitar degradação desnecessária do desempenho.

**Categoria:** Desempenho

**Prioridade:** P1

---

## RNF-COMPRAS-016 – Processamentos Assíncronos

Processamentos potencialmente demorados deverão utilizar mecanismos assíncronos quando apropriado.

Exemplos:

* geração de relatórios extensos;
* processamento documental;
* sincronização;
* integrações;
* consolidação de indicadores.

**Categoria:** Desempenho

**Prioridade:** P1

---

## RNF-COMPRAS-017 – Paginação

Listagens potencialmente extensas deverão utilizar paginação ou mecanismo equivalente.

**Categoria:** Desempenho

**Prioridade:** P1

---

## RNF-COMPRAS-018 – Cache

Mecanismos de cache poderão ser utilizados quando tecnicamente apropriados, sem comprometer consistência, segurança ou rastreabilidade.

**Categoria:** Desempenho

**Prioridade:** P2

---

# 8. Disponibilidade

## RNF-COMPRAS-019 – Disponibilidade

As funcionalidades críticas deverão observar os níveis de disponibilidade definidos pela arquitetura de implantação do SIGMUN.

**Categoria:** Disponibilidade

**Prioridade:** P0

---

## RNF-COMPRAS-020 – Detecção de Indisponibilidade

O sistema deverá permitir identificar indisponibilidade de componentes críticos.

**Categoria:** Disponibilidade

**Prioridade:** P1

---

## RNF-COMPRAS-021 – Degradação Controlada

Quando uma dependência não crítica estiver indisponível, o domínio deverá degradar de forma controlada sempre que tecnicamente possível.

**Categoria:** Disponibilidade

**Prioridade:** P1

---

# 9. Confiabilidade

## RNF-COMPRAS-022 – Integridade das Operações

As operações deverão preservar a consistência dos dados mesmo diante de falhas.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-023 – Idempotência

Operações sujeitas a repetição, especialmente integrações e sincronizações, deverão ser idempotentes quando aplicável.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-024 – Prevenção de Duplicidade

O sistema deverá possuir mecanismos para impedir registros duplicados quando a natureza da entidade exigir unicidade.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-025 – Transações

Operações que envolvam múltiplas alterações dependentes deverão utilizar mecanismos transacionais adequados.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

# 10. Escalabilidade

## RNF-COMPRAS-026 – Escalabilidade Horizontal

A arquitetura deverá permitir expansão horizontal dos componentes quando necessária.

**Categoria:** Escalabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-027 – Crescimento do Volume de Dados

O domínio deverá suportar crescimento progressivo do volume de:

* processos;
* documentos;
* contratos;
* fornecedores;
* itens;
* registros de auditoria;
* evidências.

**Categoria:** Escalabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-028 – Crescimento de Usuários

O domínio deverá suportar aumento do número de usuários e unidades administrativas sem necessidade de alteração estrutural das funcionalidades.

**Categoria:** Escalabilidade

**Prioridade:** P1

---

# 11. Usabilidade

## RNF-COMPRAS-029 – Consistência de Interface

As interfaces deverão seguir os padrões corporativos de UX/UI do SIGMUN.

**Categoria:** Usabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-030 – Fluxos Orientados a Tarefas

As interfaces deverão organizar funcionalidades de acordo com as tarefas executadas pelos usuários.

**Categoria:** Usabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-031 – Validação Antecipada

O sistema deverá informar erros e inconsistências tão próximo quanto possível do momento em que forem produzidos.

**Categoria:** Usabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-032 – Mensagens Compreensíveis

As mensagens apresentadas aos usuários deverão ser claras e orientadas à resolução do problema.

**Categoria:** Usabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-033 – Recuperação de Erros

O usuário deverá conseguir recuperar-se de erros operacionais sem perder informações já registradas, quando tecnicamente possível.

**Categoria:** Usabilidade

**Prioridade:** P1

---

# 12. Acessibilidade

## RNF-COMPRAS-034 – Acessibilidade

As interfaces deverão observar os padrões corporativos de acessibilidade adotados pelo SIGMUN.

**Categoria:** Acessibilidade

**Prioridade:** P0

---

## RNF-COMPRAS-035 – Navegação por Teclado

As funcionalidades deverão ser utilizáveis por teclado quando aplicável.

**Categoria:** Acessibilidade

**Prioridade:** P1

---

## RNF-COMPRAS-036 – Compatibilidade com Tecnologias Assistivas

As interfaces deverão ser projetadas para compatibilidade com tecnologias assistivas aplicáveis.

**Categoria:** Acessibilidade

**Prioridade:** P1

---

# 13. Interoperabilidade

## RNF-COMPRAS-037 – APIs Padronizadas

As integrações deverão utilizar APIs e padrões corporativos definidos pelo SIGMUN.

**Categoria:** Interoperabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-038 – Contratos de Integração

As interfaces de integração deverão possuir contratos claramente definidos.

**Categoria:** Interoperabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-039 – Versionamento de APIs

As APIs deverão possuir estratégia de versionamento que permita evolução controlada.

**Categoria:** Interoperabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-040 – Compatibilidade

Alterações nos serviços deverão preservar compatibilidade com consumidores existentes sempre que possível.

**Categoria:** Interoperabilidade

**Prioridade:** P1

---

# 14. Auditoria

## RNF-COMPRAS-041 – Trilha de Auditoria

Operações relevantes deverão produzir registros de auditoria.

**Categoria:** Auditoria

**Prioridade:** P0

---

## RNF-COMPRAS-042 – Identificação do Usuário

Os registros de auditoria deverão identificar o usuário ou processo responsável pela operação.

**Categoria:** Auditoria

**Prioridade:** P0

---

## RNF-COMPRAS-043 – Registro Temporal

Os eventos auditáveis deverão registrar data e hora.

**Categoria:** Auditoria

**Prioridade:** P0

---

## RNF-COMPRAS-044 – Histórico de Alterações

Alterações relevantes deverão preservar histórico suficiente para reconstrução dos eventos.

**Categoria:** Auditoria

**Prioridade:** P0

---

## RNF-COMPRAS-045 – Proteção dos Logs de Auditoria

Registros de auditoria deverão possuir proteção contra alteração ou exclusão não autorizada.

**Categoria:** Auditoria

**Prioridade:** P0

---

# 15. Observabilidade

## RNF-COMPRAS-046 – Logs Estruturados

Os componentes deverão produzir logs estruturados conforme os padrões corporativos.

**Categoria:** Observabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-047 – Métricas

O domínio deverá disponibilizar métricas operacionais e técnicas relevantes.

**Categoria:** Observabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-048 – Rastreamento Distribuído

As operações que atravessem múltiplos serviços deverão permitir rastreamento distribuído quando aplicável.

**Categoria:** Observabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-049 – Alertas Técnicos

Falhas críticas deverão gerar alertas para os responsáveis técnicos.

**Categoria:** Observabilidade

**Prioridade:** P1

---

# 16. Gestão Documental

## RNF-COMPRAS-050 – Integridade Documental

Documentos associados a processos e contratos deverão manter integridade durante todo o ciclo de vida.

**Categoria:** Gestão Documental

**Prioridade:** P0

---

## RNF-COMPRAS-051 – Versionamento Documental

Documentos que possuam versões deverão manter histórico das versões relevantes.

**Categoria:** Gestão Documental

**Prioridade:** P1

---

## RNF-COMPRAS-052 – Metadados Documentais

Os documentos deverão possuir metadados suficientes para identificação, classificação e recuperação.

**Categoria:** Gestão Documental

**Prioridade:** P1

---

## RNF-COMPRAS-053 – Associação Documental

Os documentos deverão poder ser associados aos objetos correspondentes, tais como:

* requisição;
* processo;
* contratação;
* contrato;
* aditivo;
* fiscalização;
* ocorrência.

**Categoria:** Gestão Documental

**Prioridade:** P0

---

# 17. Operação Offline

## RNF-COMPRAS-054 – Suporte Offline

Funcionalidades de campo previamente definidas deverão suportar operação offline conforme a arquitetura corporativa de mobilidade.

**Categoria:** Operação Offline

**Prioridade:** P1

---

## RNF-COMPRAS-055 – Armazenamento Local Seguro

Dados armazenados temporariamente no dispositivo deverão possuir proteção adequada.

**Categoria:** Operação Offline

**Prioridade:** P0

---

## RNF-COMPRAS-056 – Identificação de Estado Offline

O usuário deverá conseguir identificar claramente quando estiver operando sem conectividade.

**Categoria:** Operação Offline

**Prioridade:** P1

---

## RNF-COMPRAS-057 – Continuidade da Captura

A ausência temporária de conectividade não deverá impedir a captura das informações previamente autorizadas para operação offline.

**Categoria:** Operação Offline

**Prioridade:** P1

---

# 18. Sincronização

## RNF-COMPRAS-058 – Sincronização Segura

Os registros offline deverão ser sincronizados por mecanismos seguros.

**Categoria:** Sincronização

**Prioridade:** P0

---

## RNF-COMPRAS-059 – Detecção de Conflitos

O mecanismo de sincronização deverá identificar conflitos de dados.

**Categoria:** Sincronização

**Prioridade:** P1

---

## RNF-COMPRAS-060 – Tratamento de Conflitos

Os conflitos deverão ser tratados conforme política definida, sem perda silenciosa de informações.

**Categoria:** Sincronização

**Prioridade:** P0

---

## RNF-COMPRAS-061 – Reprocessamento

Falhas temporárias de sincronização deverão permitir reprocessamento.

**Categoria:** Sincronização

**Prioridade:** P1

---

# 19. Manutenibilidade

## RNF-COMPRAS-062 – Arquitetura Modular

Os componentes deverão possuir baixo acoplamento e responsabilidades bem definidas.

**Categoria:** Manutenibilidade

**Prioridade:** P0

---

## RNF-COMPRAS-063 – Código Padronizado

O desenvolvimento deverá observar os padrões corporativos de engenharia de software.

**Categoria:** Manutenibilidade

**Prioridade:** P1

---

## RNF-COMPRAS-064 – Testabilidade

As funcionalidades deverão ser projetadas de forma a permitir testes automatizados sempre que aplicável.

**Categoria:** Manutenibilidade

**Prioridade:** P0

---

## RNF-COMPRAS-065 – Documentação Técnica

Componentes relevantes deverão possuir documentação técnica suficiente para manutenção.

**Categoria:** Manutenibilidade

**Prioridade:** P1

---

# 20. Evolução

## RNF-COMPRAS-066 – Evolução Incremental

O domínio deverá permitir evolução incremental sem necessidade de reestruturação completa.

**Categoria:** Evolução

**Prioridade:** P1

---

## RNF-COMPRAS-067 – Configurabilidade

Comportamentos sujeitos a variações administrativas deverão ser parametrizáveis quando apropriado.

**Categoria:** Evolução

**Prioridade:** P0

---

## RNF-COMPRAS-068 – Compatibilidade Retroativa

Alterações deverão evitar impactos desnecessários sobre processos, integrações e dados existentes.

**Categoria:** Evolução

**Prioridade:** P1

---

# 21. Portabilidade

## RNF-COMPRAS-069 – Independência de Plataforma

Sempre que tecnicamente viável, os componentes deverão evitar dependência desnecessária de plataforma específica.

**Categoria:** Portabilidade

**Prioridade:** P2

---

## RNF-COMPRAS-070 – Compatibilidade entre Ambientes

O domínio deverá poder ser executado nos ambientes homologados pelo SIGMUN.

**Categoria:** Portabilidade

**Prioridade:** P1

---

# 22. Recuperação

## RNF-COMPRAS-071 – Backup

Os dados críticos do domínio deverão ser contemplados pelas políticas corporativas de backup.

**Categoria:** Recuperação

**Prioridade:** P0

---

## RNF-COMPRAS-072 – Restauração

Deverá ser possível restaurar dados conforme os procedimentos corporativos de recuperação.

**Categoria:** Recuperação

**Prioridade:** P0

---

## RNF-COMPRAS-073 – Teste de Restauração

Os mecanismos de restauração deverão ser periodicamente testados conforme o plano corporativo.

**Categoria:** Recuperação

**Prioridade:** P1

---

# 23. Continuidade de Negócios

## RNF-COMPRAS-074 – Continuidade

As funcionalidades críticas deverão ser contempladas pelo Plano de Continuidade de Negócios do SIGMUN.

**Categoria:** Continuidade

**Prioridade:** P0

---

## RNF-COMPRAS-075 – Recuperação de Desastres

Os componentes críticos deverão possuir mecanismos compatíveis com a estratégia corporativa de recuperação de desastres.

**Categoria:** Continuidade

**Prioridade:** P0

---

## RNF-COMPRAS-076 – Priorização de Serviços

Os serviços críticos do domínio deverão possuir classificação de criticidade.

**Categoria:** Continuidade

**Prioridade:** P1

---

# 24. Qualidade de Dados

## RNF-COMPRAS-077 – Integridade Referencial

Os dados deverão preservar relacionamentos válidos entre as entidades.

**Categoria:** Qualidade de Dados

**Prioridade:** P0

---

## RNF-COMPRAS-078 – Unicidade

As entidades que exigirem identificação única deverão possuir mecanismos de controle de unicidade.

**Categoria:** Qualidade de Dados

**Prioridade:** P0

---

## RNF-COMPRAS-079 – Consistência

Os dados deverão obedecer às regras de consistência definidas pelo domínio.

**Categoria:** Qualidade de Dados

**Prioridade:** P0

---

## RNF-COMPRAS-080 – Completude

Os dados essenciais deverão possuir mecanismos para evitar registros incompletos.

**Categoria:** Qualidade de Dados

**Prioridade:** P0

---

## RNF-COMPRAS-081 – Rastreabilidade dos Dados

Deverá ser possível identificar a origem e as alterações relevantes dos dados críticos.

**Categoria:** Qualidade de Dados

**Prioridade:** P0

---

# 25. Transparência

## RNF-COMPRAS-082 – Publicação Controlada

Informações públicas deverão ser disponibilizadas de acordo com a política corporativa de publicação.

**Categoria:** Transparência

**Prioridade:** P0

---

## RNF-COMPRAS-083 – Atualização das Informações Públicas

As informações disponibilizadas publicamente deverão ser atualizadas dentro dos prazos e mecanismos definidos.

**Categoria:** Transparência

**Prioridade:** P1

---

## RNF-COMPRAS-084 – Integridade das Informações Publicadas

As informações disponibilizadas em mecanismos públicos deverão corresponder aos dados oficiais do SIGMUN.

**Categoria:** Transparência

**Prioridade:** P0

---

## RNF-COMPRAS-085 – Proteção de Informações Restritas

A publicação automática deverá impedir exposição de informações classificadas como restritas ou protegidas.

**Categoria:** Transparência

**Prioridade:** P0

---

# 26. Governança

## RNF-COMPRAS-086 – Conformidade Arquitetural

A implementação deverá observar os padrões e princípios da arquitetura corporativa do SIGMUN.

**Categoria:** Governança

**Prioridade:** P0

---

## RNF-COMPRAS-087 – Registro de Decisões Arquiteturais

Decisões arquiteturais relevantes deverão ser registradas conforme o mecanismo corporativo de ADR.

**Categoria:** Governança

**Prioridade:** P1

---

## RNF-COMPRAS-088 – Rastreabilidade de Requisitos

Os requisitos deverão possuir rastreabilidade até sua origem e aos artefatos de validação correspondentes.

**Categoria:** Governança

**Prioridade:** P0

---

## RNF-COMPRAS-089 – Controle de Mudanças

Alterações relevantes nos requisitos deverão possuir controle formal de mudança.

**Categoria:** Governança

**Prioridade:** P1

---

# 27. Conformidade

## RNF-COMPRAS-090 – Conformidade Normativa

O domínio deverá permitir implementação das exigências normativas aplicáveis ao processo de compras e contratações.

**Categoria:** Conformidade

**Prioridade:** P0

---

## RNF-COMPRAS-091 – Parametrização Normativa

Quando houver variações normativas ou administrativas aplicáveis, o sistema deverá permitir parametrização quando tecnicamente viável.

**Categoria:** Conformidade

**Prioridade:** P0

---

## RNF-COMPRAS-092 – Evidência de Conformidade

O sistema deverá preservar evidências necessárias à demonstração de conformidade.

**Categoria:** Conformidade

**Prioridade:** P0

---

# 28. Requisitos de Segurança Operacional

## RNF-COMPRAS-093 – Proteção contra Exclusão Indevida

Operações de exclusão deverão ser controladas conforme as regras de retenção e auditoria.

**Categoria:** Segurança

**Prioridade:** P0

---

## RNF-COMPRAS-094 – Exclusão Lógica

Quando necessário para preservação histórica e auditabilidade, o sistema deverá utilizar exclusão lógica em vez de exclusão física.

**Categoria:** Segurança

**Prioridade:** P1

---

## RNF-COMPRAS-095 – Controle de Operações Críticas

Operações críticas deverão possuir autorização adequada e registro de auditoria.

**Categoria:** Segurança

**Prioridade:** P0

---

# 29. Requisitos de Integridade Transacional

## RNF-COMPRAS-096 – Consistência entre Domínios

Integrações com orçamento, financeiro, contabilidade, patrimônio, almoxarifado e demais domínios deverão preservar consistência dos dados.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-097 – Falhas de Integração

Falhas de integração não deverão produzir inconsistências silenciosas.

**Categoria:** Confiabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-098 – Reprocessamento de Integrações

Integrações deverão possuir mecanismos de reprocessamento quando aplicável.

**Categoria:** Confiabilidade

**Prioridade:** P1

---

# 30. Requisitos de Dados Históricos

## RNF-COMPRAS-099 – Preservação Histórica

Informações necessárias à reconstrução do histórico dos processos e contratos deverão ser preservadas conforme políticas corporativas.

**Categoria:** Dados

**Prioridade:** P0

---

## RNF-COMPRAS-100 – Imutabilidade de Registros Críticos

Registros críticos deverão possuir mecanismos que impeçam alterações não autorizadas.

**Categoria:** Dados

**Prioridade:** P0

---

# 31. Requisitos de Escopo e Domínio

## RNF-COMPRAS-101 – Separação de Responsabilidades

O domínio deverá manter separação clara entre responsabilidades de negócio e responsabilidades de infraestrutura.

**Categoria:** Arquitetura

**Prioridade:** P1

---

## RNF-COMPRAS-102 – Baixo Acoplamento

A implementação deverá minimizar dependências diretas entre componentes.

**Categoria:** Arquitetura

**Prioridade:** P0

---

## RNF-COMPRAS-103 – Alta Coesão

Cada componente deverá possuir responsabilidades coerentes e bem delimitadas.

**Categoria:** Arquitetura

**Prioridade:** P1

---

# 32. Requisitos de Testabilidade

## RNF-COMPRAS-104 – Testes Automatizados

As funcionalidades críticas deverão possuir testes automatizados.

**Categoria:** Testabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-105 – Testes de Integração

As integrações críticas deverão possuir testes automatizados de integração.

**Categoria:** Testabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-106 – Testes de Segurança

Funcionalidades críticas deverão ser submetidas a testes de segurança apropriados.

**Categoria:** Testabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-107 – Testes de Recuperação

Os mecanismos de recuperação deverão ser testados conforme o planejamento corporativo.

**Categoria:** Testabilidade

**Prioridade:** P1

---

# 33. Requisitos de Monitoramento

## RNF-COMPRAS-108 – Monitoramento de Serviços

Os serviços críticos deverão possuir monitoramento operacional.

**Categoria:** Observabilidade

**Prioridade:** P0

---

## RNF-COMPRAS-109 – Monitoramento de Integrações

As integrações críticas deverão possuir indicadores de sucesso, falha, latência e processamento.

**Categoria:** Observabilidade

**Prioridade:** P1

---

## RNF-COMPRAS-110 – Monitoramento de Processos

Processos críticos deverão possuir indicadores de andamento e pendências.

**Categoria:** Observabilidade

**Prioridade:** P1

---

# 34. Matriz Consolidada

| Faixa                 | Categoria                |
| --------------------- | ------------------------ |
| RNF-COMPRAS-001 a 008 | Segurança                |
| RNF-COMPRAS-009 a 013 | Privacidade              |
| RNF-COMPRAS-014 a 018 | Desempenho               |
| RNF-COMPRAS-019 a 021 | Disponibilidade          |
| RNF-COMPRAS-022 a 025 | Confiabilidade           |
| RNF-COMPRAS-026 a 028 | Escalabilidade           |
| RNF-COMPRAS-029 a 033 | Usabilidade              |
| RNF-COMPRAS-034 a 036 | Acessibilidade           |
| RNF-COMPRAS-037 a 040 | Interoperabilidade       |
| RNF-COMPRAS-041 a 045 | Auditoria                |
| RNF-COMPRAS-046 a 049 | Observabilidade          |
| RNF-COMPRAS-050 a 053 | Gestão Documental        |
| RNF-COMPRAS-054 a 057 | Operação Offline         |
| RNF-COMPRAS-058 a 061 | Sincronização            |
| RNF-COMPRAS-062 a 065 | Manutenibilidade         |
| RNF-COMPRAS-066 a 068 | Evolução                 |
| RNF-COMPRAS-069 a 070 | Portabilidade            |
| RNF-COMPRAS-071 a 073 | Recuperação              |
| RNF-COMPRAS-074 a 076 | Continuidade             |
| RNF-COMPRAS-077 a 081 | Qualidade de Dados       |
| RNF-COMPRAS-082 a 085 | Transparência            |
| RNF-COMPRAS-086 a 089 | Governança               |
| RNF-COMPRAS-090 a 092 | Conformidade             |
| RNF-COMPRAS-093 a 095 | Segurança Operacional    |
| RNF-COMPRAS-096 a 098 | Integridade Transacional |
| RNF-COMPRAS-099 a 100 | Dados Históricos         |
| RNF-COMPRAS-101 a 103 | Arquitetura              |
| RNF-COMPRAS-104 a 107 | Testabilidade            |
| RNF-COMPRAS-108 a 110 | Monitoramento            |

---

# 35. Critérios de Qualidade

Todo requisito não funcional deverá, sempre que possível, possuir:

* identificador;
* categoria;
* prioridade;
* origem;
* métrica ou critério verificável;
* método de validação;
* relação com requisitos funcionais;
* relação com atributos de qualidade.

Requisitos não funcionais vagos deverão ser refinados antes da implementação.

Exemplo inadequado:

```text
O sistema deverá ser rápido.
```

Exemplo adequado:

```text
O tempo de resposta de uma consulta deverá atender
ao SLA definido para a operação correspondente.
```

---

# 36. Critérios de Aceitação dos Requisitos Não Funcionais

A validação deverá considerar:

* testes funcionais;
* testes de desempenho;
* testes de segurança;
* testes de carga;
* testes de disponibilidade;
* testes de recuperação;
* testes de acessibilidade;
* testes de integração;
* testes de sincronização;
* inspeção arquitetural;
* análise de logs;
* análise de métricas.

Os valores quantitativos deverão ser definidos nas especificações técnicas e nos critérios de aceitação correspondentes.

---

# 37. Relação com Requisitos Funcionais

Os requisitos não funcionais não substituem os requisitos funcionais.

A relação esperada é:

```text
Requisito Funcional
        ↓
Requisitos Não Funcionais aplicáveis
        ↓
Especificação Técnica
        ↓
Critério de Aceitação
        ↓
Teste
```

Um único requisito funcional poderá estar relacionado a vários requisitos não funcionais.

---

# 38. Rastreabilidade

A rastreabilidade deverá seguir o modelo corporativo:

```text
Capacidade
    ↓
Processo
    ↓
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
Requisito Não Funcional
    ↓
Especificação
    ↓
Critério de Aceitação
    ↓
Teste
```

---

# 39. Requisitos Quantitativos Pendentes

Os seguintes valores deverão ser definidos posteriormente:

* tempo máximo de resposta;
* throughput;
* quantidade máxima de usuários simultâneos;
* volume máximo de processos;
* volume máximo de documentos;
* disponibilidade mínima;
* RTO;
* RPO;
* tempo máximo de sincronização;
* limites de armazenamento;
* retenção de logs;
* limites de integração;
* metas de recuperação.

Esses valores não deverão ser inventados neste documento sem validação arquitetural e operacional.

---

# 40. Dependências Corporativas

A implementação destes requisitos deverá considerar os serviços corporativos do SIGMUN, incluindo, quando existentes:

* gestão de identidade;
* autorização;
* gestão documental;
* notificações;
* auditoria;
* observabilidade;
* integração;
* cadastro único;
* dados;
* segurança;
* infraestrutura;
* backup;
* continuidade;
* transparência.

O domínio não deverá duplicar serviços corporativos sem justificativa arquitetural.

---

# 41. Premissas

Este documento considera que:

1. O SIGMUN possuirá arquitetura corporativa compartilhada.
2. Existirão mecanismos corporativos de identidade.
3. Existirão políticas corporativas de segurança.
4. Existirão mecanismos corporativos de auditoria.
5. Existirão padrões de integração.
6. Existirão políticas de continuidade e recuperação.
7. O domínio poderá consumir serviços corporativos.
8. Os requisitos quantitativos serão refinados posteriormente.

---

# 42. Pendências para Especificação

Os seguintes aspectos deverão ser detalhados no próximo nível de especificação:

* SLAs;
* SLOs;
* métricas;
* limites;
* protocolos;
* padrões de API;
* mecanismos de autenticação;
* mecanismos de autorização;
* criptografia;
* armazenamento;
* estratégia de cache;
* estratégia de sincronização;
* estratégia offline;
* observabilidade;
* arquitetura de implantação;
* políticas de retenção;
* requisitos de infraestrutura;
* requisitos de banco de dados;
* requisitos de segurança;
* requisitos de continuidade.

---

# 43. Próximos Artefatos

A sequência recomendada é:

```text
008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
                    ↓
009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
                    ↓
010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
                    ↓
011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
                    ↓
012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
```

---

# 44. Registro no Mapa Mestre

**Identificador do artefato:**

`RNF-MAP-COMPRAS-001`

**Tipo:**

Requisitos Não Funcionais.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

**Status:**

Vigente.

---

# 45. Controle de Versões

| Versão | Data       | Descrição                                                                            |
| ------ | ---------- | ------------------------------------------------------------------------------------ |
| 1.0    | 2026-08-11 | Criação dos Requisitos Não Funcionais do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
