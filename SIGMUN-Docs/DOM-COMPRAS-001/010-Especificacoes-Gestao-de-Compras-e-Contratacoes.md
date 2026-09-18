# 010 – Especificações – Gestão de Compras e Contratações

#### Especificações – Gestão de Compras e Contratações

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
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS-ADR.md
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
* 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
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

Este documento define as **Especificações do Domínio de Gestão de Compras e Contratações** do SIGMUN.

As especificações representam o nível de detalhamento necessário para transformar:

* capacidades;
* processos;
* serviços;
* casos de uso;
* histórias de usuário;
* regras de negócio;
* requisitos funcionais;
* requisitos não funcionais;

em definições suficientemente precisas para orientar:

* arquitetura;
* desenvolvimento;
* configuração;
* integração;
* testes;
* homologação;
* implantação;
* operação.

Este documento não substitui os requisitos. Ele os **detalha e operacionaliza**.

---

# 2. Objetivos

As especificações deverão:

1. eliminar ambiguidades dos requisitos;
2. definir comportamentos esperados;
3. estabelecer entradas e saídas;
4. definir validações;
5. definir estados e transições;
6. estabelecer integrações;
7. definir eventos;
8. estabelecer regras de persistência;
9. definir requisitos de segurança;
10. permitir elaboração dos critérios de aceitação;
11. permitir implementação técnica;
12. preservar rastreabilidade.

---

# 3. Princípios

As especificações deverão observar:

* simplicidade;
* clareza;
* consistência;
* rastreabilidade;
* segurança;
* auditabilidade;
* interoperabilidade;
* reutilização;
* parametrização;
* baixa acoplagem;
* alta coesão;
* preservação histórica;
* transparência;
* conformidade normativa.

---

# 4. Estrutura das Especificações

Cada especificação deverá possuir, quando aplicável:

```text
Identificador
Título
Objetivo
Origem
Atores
Pré-condições
Entradas
Validações
Processamento
Regras
Saídas
Estados
Eventos
Integrações
Persistência
Auditoria
Segurança
Exceções
Pós-condições
Requisitos relacionados
Critérios de aceitação
```

---

# 5. Convenção de Identificação

As especificações utilizarão o padrão:

```text
ESP-COMPRAS-XXX
```

Exemplo:

```text
ESP-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida da especificação.

---

# 6. Níveis de Especificação

As especificações serão organizadas em cinco níveis:

| Nível   | Descrição                      |
| ------- | ------------------------------ |
| Nível 1 | Especificação de domínio       |
| Nível 2 | Especificação de capacidade    |
| Nível 3 | Especificação de processo      |
| Nível 4 | Especificação de serviço       |
| Nível 5 | Especificação de comportamento |

A especificação de comportamento deverá possuir detalhamento suficiente para permitir implementação e teste.

---

# 7. Especificação de Domínio

## ESP-COMPRAS-001 – Estrutura Geral do Domínio

O domínio deverá organizar as funcionalidades relacionadas ao planejamento, solicitação, processamento, formalização, execução, acompanhamento e encerramento dos processos de compras e contratações municipais.

O domínio deverá manter separação entre:

* planejamento;
* demanda;
* contratação;
* fornecedor;
* processo;
* contrato;
* execução;
* fiscalização;
* documentos;
* integração financeira;
* transparência.

---

# 8. Especificação de Capacidades

## ESP-COMPRAS-002 – Gestão da Demanda

A solução deverá permitir registrar, organizar, avaliar e acompanhar demandas de aquisição de bens e contratação de serviços.

### Entradas

* unidade solicitante;
* responsável;
* objeto;
* justificativa;
* quantidade;
* unidade de medida;
* estimativa;
* prioridade;
* prazo desejado.

### Saídas

* demanda registrada;
* identificação única;
* situação;
* histórico;
* encaminhamentos.

---

## ESP-COMPRAS-003 – Planejamento de Contratações

A solução deverá permitir consolidar demandas em planejamento de contratações.

O planejamento deverá permitir:

* inclusão de demandas;
* agrupamento;
* priorização;
* estimativa;
* programação temporal;
* acompanhamento;
* revisão;
* aprovação.

---

## ESP-COMPRAS-004 – Gestão do Processo de Contratação

O sistema deverá permitir controlar o ciclo de vida do processo de contratação desde sua abertura até seu encerramento.

---

## ESP-COMPRAS-005 – Gestão de Fornecedores

O domínio deverá consumir e/ou integrar dados cadastrais de fornecedores conforme o modelo corporativo de dados.

Deverá permitir:

* identificação;
* situação cadastral;
* documentação;
* histórico;
* relacionamentos;
* participação em processos.

---

## ESP-COMPRAS-006 – Gestão Contratual

O sistema deverá permitir registrar e acompanhar contratos decorrentes dos processos de contratação.

---

## ESP-COMPRAS-007 – Gestão da Execução

A solução deverá permitir acompanhar a execução contratual, incluindo:

* medições;
* entregas;
* ocorrências;
* documentos;
* responsabilidades;
* fiscalização;
* prazos;
* alterações.

---

# 9. Especificação de Processos

## ESP-COMPRAS-008 – Abertura de Processo

### Pré-condições

* demanda válida;
* usuário autorizado;
* informações mínimas preenchidas.

### Processamento

1. validar demanda;
2. criar processo;
3. gerar identificador;
4. registrar unidade responsável;
5. registrar responsável;
6. registrar data de abertura;
7. registrar evento de auditoria.

### Saída

Processo criado e disponível para tramitação.

---

# 10. Especificação de Estados

## ESP-COMPRAS-009 – Ciclo de Vida do Processo

O processo deverá possuir estados controlados.

Modelo inicial:

```text
RASCUNHO
    ↓
ABERTO
    ↓
EM_ANALISE
    ↓
EM_INSTRUCAO
    ↓
AGUARDANDO_DECISAO
    ↓
APROVADO
    ↓
EM_CONTRATACAO
    ↓
CONTRATADO
    ↓
EM_EXECUCAO
    ↓
ENCERRADO
```

Também deverão existir estados de exceção quando aplicáveis:

```text
SUSPENSO
CANCELADO
REVOGADO
ANULADO
ARQUIVADO
```

As transições deverão ser controladas por regras de negócio.

---

# 11. Especificação de Demanda

## ESP-COMPRAS-010 – Registro de Demanda

A demanda deverá possuir:

* identificador;
* unidade solicitante;
* responsável;
* objeto;
* justificativa;
* quantidade;
* unidade de medida;
* estimativa de valor;
* prioridade;
* prazo;
* situação;
* data de criação;
* histórico.

---

## ESP-COMPRAS-011 – Validação de Demanda

Antes da submissão, o sistema deverá validar:

* campos obrigatórios;
* unidade solicitante;
* responsável;
* descrição do objeto;
* quantidade;
* justificativa;
* classificação;
* estimativa, quando obrigatória.

---

# 12. Especificação do Objeto

## ESP-COMPRAS-012 – Cadastro do Objeto

O objeto deverá ser descrito de maneira estruturada e suficientemente precisa para permitir:

* planejamento;
* pesquisa;
* estimativa;
* contratação;
* acompanhamento;
* análise histórica.

Sempre que aplicável, deverão ser utilizados cadastros corporativos padronizados.

---

# 13. Especificação da Pesquisa e Estimativa

## ESP-COMPRAS-013 – Formação da Estimativa

A solução deverá permitir registrar informações utilizadas para formação da estimativa de contratação.

Deverá permitir registrar:

* fonte;
* fornecedor;
* data;
* valor;
* unidade;
* quantidade;
* metodologia;
* documento comprobatório.

---

## ESP-COMPRAS-014 – Histórico da Estimativa

Alterações na estimativa deverão preservar histórico suficiente para auditoria.

---

# 14. Especificação da Instrução Processual

## ESP-COMPRAS-015 – Documentação do Processo

O processo deverá permitir associação de documentos aos respectivos contextos.

Exemplos:

* documentos preparatórios;
* justificativas;
* estudos;
* pesquisas;
* pareceres;
* autorizações;
* decisões;
* propostas;
* documentos contratuais.

---

## ESP-COMPRAS-016 – Controle de Documentos Obrigatórios

O sistema deverá permitir configurar documentos obrigatórios conforme o tipo de processo.

A ausência de documentos obrigatórios deverá impedir o avanço quando a regra de negócio determinar bloqueio.

---

# 15. Especificação da Aprovação

## ESP-COMPRAS-017 – Fluxo de Aprovação

A aprovação deverá respeitar:

* competência;
* autoridade;
* unidade;
* tipo de processo;
* valor;
* regras configuradas.

Cada aprovação deverá produzir registro de auditoria.

---

# 16. Especificação da Contratação

## ESP-COMPRAS-018 – Formalização

Após a conclusão do procedimento aplicável, o sistema deverá permitir formalizar a contratação.

A formalização deverá registrar:

* fornecedor;
* objeto;
* valor;
* prazo;
* condições;
* documentos;
* responsáveis;
* processo de origem.

---

# 17. Especificação do Contrato

## ESP-COMPRAS-019 – Cadastro do Contrato

O contrato deverá possuir, no mínimo:

* identificador;
* número;
* processo de origem;
* fornecedor;
* objeto;
* valor;
* vigência;
* unidade responsável;
* gestor;
* fiscal;
* situação;
* documentos;
* histórico.

---

# 18. Especificação de Vigência

## ESP-COMPRAS-020 – Controle de Vigência

O sistema deverá controlar:

* início;
* término;
* alterações;
* prorrogações;
* suspensões;
* encerramento.

Deverá permitir geração de alertas para prazos relevantes.

---

# 19. Especificação da Fiscalização

## ESP-COMPRAS-021 – Registro de Fiscalização

O sistema deverá permitir registrar atividades de fiscalização.

Deverá permitir:

* fiscal responsável;
* data;
* objeto fiscalizado;
* ocorrência;
* evidência;
* conclusão;
* encaminhamento.

---

# 20. Especificação de Entregas

## ESP-COMPRAS-022 – Registro de Entrega

O sistema deverá permitir registrar:

* item;
* quantidade;
* data;
* fornecedor;
* documento;
* responsável pelo recebimento;
* situação;
* evidências.

---

# 21. Especificação de Medição

## ESP-COMPRAS-023 – Medição

Quando aplicável, deverá permitir registrar:

* período;
* objeto;
* quantidade;
* valor;
* responsável;
* documentos;
* aprovação;
* ocorrências.

---

# 22. Especificação de Aditivos

## ESP-COMPRAS-024 – Alteração Contratual

O sistema deverá permitir registrar alterações contratuais.

Deverá manter:

* contrato de origem;
* tipo de alteração;
* justificativa;
* impacto financeiro;
* impacto temporal;
* documentos;
* aprovação;
* histórico.

---

# 23. Especificação de Ocorrências

## ESP-COMPRAS-025 – Registro de Ocorrência

Deverá ser possível registrar ocorrências relacionadas à execução.

Uma ocorrência deverá possuir:

* identificador;
* contrato;
* data;
* responsável;
* descrição;
* classificação;
* evidências;
* encaminhamento;
* situação.

---

# 24. Especificação de Encerramento

## ESP-COMPRAS-026 – Encerramento de Contrato

O encerramento deverá verificar os requisitos necessários antes da mudança de estado.

Quando aplicável, deverão ser verificados:

* execução;
* entregas;
* pendências;
* documentos;
* medições;
* ocorrências;
* obrigações;
* encerramento administrativo.

---

# 25. Especificação de Auditoria

## ESP-COMPRAS-027 – Registro de Eventos

Deverão ser auditados, no mínimo:

* criação;
* alteração;
* aprovação;
* rejeição;
* cancelamento;
* suspensão;
* contratação;
* alteração contratual;
* encerramento;
* publicação;
* acesso a informações protegidas.

---

# 26. Especificação de Segurança

## ESP-COMPRAS-028 – Autorização por Contexto

As permissões deverão considerar, quando aplicável:

* usuário;
* perfil;
* função;
* unidade;
* processo;
* situação;
* operação.

---

# 27. Especificação de Integrações

## ESP-COMPRAS-029 – Integração com Identidade

O domínio deverá utilizar o serviço corporativo de identidade.

---

## ESP-COMPRAS-030 – Integração com Cadastro

O domínio deverá consumir dados cadastrais corporativos sempre que disponíveis.

---

## ESP-COMPRAS-031 – Integração Orçamentária

Quando aplicável, o domínio deverá integrar-se ao domínio responsável por orçamento.

---

## ESP-COMPRAS-032 – Integração Financeira

Quando aplicável, informações necessárias à execução financeira deverão ser integradas ao domínio financeiro.

---

## ESP-COMPRAS-033 – Integração Contábil

Quando aplicável, eventos que produzam reflexos contábeis deverão ser disponibilizados ao domínio contábil.

---

## ESP-COMPRAS-034 – Integração com Gestão Documental

Documentos deverão utilizar o serviço corporativo de gestão documental sempre que disponível.

---

## ESP-COMPRAS-035 – Integração com Transparência

Informações classificadas como públicas deverão poder alimentar os mecanismos corporativos de transparência.

---

# 28. Especificação de Eventos

Eventos relevantes deverão ser publicados conforme a arquitetura de integração.

Eventos candidatos:

```text
DemandaCriada
DemandaAprovada
ProcessoAberto
ProcessoAprovado
ProcessoCancelado
ContratacaoFormalizada
ContratoCriado
ContratoAlterado
ContratoSuspenso
ContratoEncerrado
EntregaRegistrada
MedicaoRegistrada
OcorrenciaRegistrada
DocumentoAnexado
DocumentoPublicado
```

---

# 29. Especificação de Notificações

## ESP-COMPRAS-036 – Notificações

O domínio deverá utilizar o serviço corporativo de notificações.

Poderão ser configuradas notificações para:

* vencimentos;
* pendências;
* aprovações;
* rejeições;
* atrasos;
* ocorrências;
* alterações;
* falhas de integração.

---

# 30. Especificação de Documentos

## ESP-COMPRAS-037 – Metadados

Os documentos deverão possuir metadados compatíveis com o modelo corporativo.

---

## ESP-COMPRAS-038 – Classificação

Os documentos deverão possuir classificação da informação quando aplicável.

---

## ESP-COMPRAS-039 – Integridade

Documentos críticos deverão possuir mecanismos de verificação de integridade.

---

# 31. Especificação de Dados

## ESP-COMPRAS-040 – Identificação

As entidades deverão possuir identificadores únicos.

---

## ESP-COMPRAS-041 – Histórico

Entidades críticas deverão possuir histórico de alterações.

---

## ESP-COMPRAS-042 – Integridade Referencial

Relacionamentos entre entidades deverão ser validados.

---

# 32. Especificação de Parametrização

## ESP-COMPRAS-043 – Parâmetros Administrativos

O sistema deverá permitir parametrizar, quando aplicável:

* fluxos;
* prazos;
* níveis de aprovação;
* documentos obrigatórios;
* tipos de processo;
* categorias;
* classificações;
* notificações;
* regras de encaminhamento.

A parametrização não deverá permitir violar regras legais ou controles de segurança.

---

# 33. Especificação de Configuração

## ESP-COMPRAS-044 – Configuração por Município

O domínio deverá permitir configuração das características administrativas de cada município sem necessidade de alteração do núcleo do sistema.

---

# 34. Especificação Multiunidade

## ESP-COMPRAS-045 – Unidades Administrativas

O domínio deverá suportar múltiplas:

* secretarias;
* órgãos;
* unidades;
* setores;
* fundos;
* entidades vinculadas;

conforme o modelo organizacional do município.

---

# 35. Especificação Multi-Município

## ESP-COMPRAS-046 – Isolamento entre Municípios

Quando implantado como plataforma multi-município, os dados de cada município deverão permanecer logicamente isolados.

Nenhum município deverá acessar dados de outro sem autorização explícita e mecanismo institucional apropriado.

---

# 36. Especificação de Transparência

## ESP-COMPRAS-047 – Dados Públicos

O sistema deverá identificar dados elegíveis para publicação.

A publicação deverá observar:

* classificação;
* proteção de dados;
* integridade;
* atualização;
* rastreabilidade.

---

# 37. Especificação de Operação Offline

## ESP-COMPRAS-048 – Captura Offline

Funcionalidades explicitamente habilitadas para campo poderão permitir captura offline.

Os dados deverão ser armazenados temporariamente de forma segura.

---

## ESP-COMPRAS-049 – Sincronização

Após recuperação da conectividade, os dados deverão ser sincronizados.

Falhas deverão permitir reprocessamento.

---

# 38. Especificação de Exceções

## ESP-COMPRAS-050 – Tratamento de Exceções

As exceções deverão:

* possuir identificação;
* produzir mensagem apropriada;
* não expor informações sensíveis;
* produzir logs quando necessário;
* preservar consistência transacional;
* permitir recuperação quando possível.

---

# 39. Especificação de Concorrência

## ESP-COMPRAS-051 – Controle de Concorrência

O sistema deverá controlar alterações concorrentes em entidades críticas.

Deverá evitar sobrescrita silenciosa de alterações.

---

# 40. Especificação de Idempotência

## ESP-COMPRAS-052 – Operações Idempotentes

Operações de integração e sincronização deverão possuir identificadores de correlação ou mecanismos equivalentes para evitar processamento duplicado.

---

# 41. Especificação de Desempenho

## ESP-COMPRAS-053 – Operações Interativas

Os parâmetros quantitativos de desempenho deverão ser definidos nos critérios de aceitação e SLAs correspondentes.

Este documento não fixa valores arbitrários sem validação arquitetural.

---

# 42. Especificação de Observabilidade

## ESP-COMPRAS-054 – Correlação

Operações distribuídas deverão possuir identificador de correlação.

---

## ESP-COMPRAS-055 – Métricas

Deverão ser monitoradas, quando aplicável:

* quantidade de processos;
* tempo de processamento;
* processos pendentes;
* falhas;
* integrações;
* sincronizações;
* notificações;
* erros.

---

# 43. Especificação de Testes

## ESP-COMPRAS-056 – Testabilidade

Cada especificação deverá poder ser validada por pelo menos um método de teste ou verificação.

Métodos possíveis:

* teste automatizado;
* teste manual;
* teste de integração;
* teste de segurança;
* inspeção;
* análise de logs;
* teste de carga;
* teste de recuperação.

---

# 44. Especificação de APIs

## ESP-COMPRAS-057 – API de Processos

A API deverá permitir operações autorizadas sobre processos.

Operações candidatas:

```text
Criar
Consultar
Atualizar
Tramitar
Aprovar
Rejeitar
Suspender
Cancelar
Encerrar
```

---

## ESP-COMPRAS-058 – API de Contratos

A API deverá permitir operações autorizadas sobre contratos.

---

## ESP-COMPRAS-059 – API de Fornecedores

A API deverá consumir ou disponibilizar informações conforme o modelo corporativo e as permissões aplicáveis.

---

# 45. Especificação de Segurança das APIs

## ESP-COMPRAS-060 – APIs Protegidas

As APIs deverão possuir:

* autenticação;
* autorização;
* validação;
* controle de acesso;
* proteção contra abuso;
* registro de auditoria quando aplicável.

---

# 46. Especificação de Versionamento

## ESP-COMPRAS-061 – Versionamento de Interfaces

Interfaces externas deverão possuir estratégia de versionamento.

Alterações incompatíveis deverão gerar nova versão.

---

# 47. Especificação de Retenção

## ESP-COMPRAS-062 – Retenção

Dados e documentos deverão observar as políticas corporativas de retenção e as exigências aplicáveis ao domínio.

---

# 48. Especificação de Exclusão

## ESP-COMPRAS-063 – Exclusão Controlada

Dados críticos não deverão ser eliminados fisicamente quando a preservação histórica for necessária.

A exclusão deverá ser submetida às políticas corporativas.

---

# 49. Especificação de Recuperação

## ESP-COMPRAS-064 – Recuperação

O domínio deverá ser contemplado pelas estratégias corporativas de:

* backup;
* restauração;
* recuperação de desastre;
* continuidade.

---

# 50. Especificação de Rastreabilidade

## ESP-COMPRAS-065 – Rastreabilidade Integral

Cada especificação deverá possuir relacionamento com:

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

# 51. Matriz Inicial de Rastreabilidade

| Especificação         | Artefato de origem              | Próximo artefato |
| --------------------- | ------------------------------- | ---------------- |
| ESP-COMPRAS-001       | Domínio                         | Critérios        |
| ESP-COMPRAS-002       | Capacidade                      | Critérios        |
| ESP-COMPRAS-003       | Capacidade                      | Critérios        |
| ESP-COMPRAS-004       | Processo                        | Critérios        |
| ESP-COMPRAS-005       | Capacidade                      | Critérios        |
| ESP-COMPRAS-006       | Capacidade                      | Critérios        |
| ESP-COMPRAS-007       | Processo                        | Critérios        |
| ESP-COMPRAS-008       | Processo                        | Critérios        |
| ESP-COMPRAS-009       | Requisito Funcional             | Critérios        |
| ESP-COMPRAS-010       | Requisito Funcional             | Critérios        |
| ESP-COMPRAS-018       | Requisito Funcional             | Critérios        |
| ESP-COMPRAS-019       | Requisito Funcional             | Critérios        |
| ESP-COMPRAS-021       | Requisito Funcional             | Critérios        |
| ESP-COMPRAS-027       | Requisito Não Funcional         | Critérios        |
| ESP-COMPRAS-028       | Requisito Não Funcional         | Critérios        |
| ESP-COMPRAS-029 a 035 | Integrações                     | Critérios        |
| ESP-COMPRAS-040 a 046 | Requisitos de Dados/Arquitetura | Critérios        |
| ESP-COMPRAS-048 a 049 | RNF Offline/Sincronização       | Critérios        |
| ESP-COMPRAS-053 a 055 | RNF Desempenho/Observabilidade  | Critérios        |
| ESP-COMPRAS-056       | RNF Testabilidade               | Critérios        |

A matriz deverá ser refinada durante a elaboração da matriz completa de rastreabilidade do domínio.

---

# 52. Critérios para Considerar uma Especificação Completa

Uma especificação será considerada suficientemente detalhada quando:

* possuir identificador;
* possuir objetivo;
* possuir origem;
* possuir entradas;
* possuir comportamento esperado;
* possuir validações;
* possuir saídas;
* possuir tratamento de exceções;
* possuir requisitos de segurança aplicáveis;
* possuir integrações aplicáveis;
* possuir critérios de auditoria aplicáveis;
* possuir rastreabilidade;
* puder ser transformada em critério de aceitação.

---

# 53. Regras para Evolução

Alterações nas especificações deverão:

1. preservar os identificadores existentes;
2. registrar a mudança;
3. avaliar impacto;
4. atualizar a rastreabilidade;
5. atualizar critérios de aceitação;
6. atualizar testes afetados;
7. atualizar documentação relacionada.

---

# 54. Pendências

As seguintes definições deverão ser refinadas antes da implementação definitiva:

* parâmetros quantitativos de desempenho;
* SLAs;
* SLOs;
* RTO;
* RPO;
* políticas de retenção;
* contratos de APIs;
* eventos definitivos;
* schemas de integração;
* modelos de dados;
* regras de autorização;
* documentos obrigatórios por modalidade;
* fluxos específicos;
* estados definitivos;
* regras de parametrização.

Essas pendências deverão ser tratadas nos artefatos técnicos correspondentes.

---

# 55. Próximos Artefatos

A sequência recomendada para o domínio é:

```text
009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
                    ↓
010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
                    ↓
011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
                    ↓
012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
```

Posteriormente, deverão ser elaborados os artefatos técnicos necessários à implementação, incluindo:

* modelo de dados;
* APIs;
* eventos;
* integrações;
* arquitetura de componentes;
* segurança;
* testes;
* implantação.

---

# 56. Registro no Mapa Mestre

**Identificador do artefato:**

`ESP-MAP-COMPRAS-001`

**Tipo:**

Especificações.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

**Status:**

Vigente.

---

# 57. Controle de Versões

| Versão | Data       | Descrição                                                                 |
| ------ | ---------- | ------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação das Especificações do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
