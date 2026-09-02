#### Arquitetura de Serviços – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
- 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
- 000C-HIERARQUIA-DOCUMENTAL.md
- 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS-ADR.md
- 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
- 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
- 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
- 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
- 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
- 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
- 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
- 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
- 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
- 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
- 012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
- 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md
- 009-Arquitetura-de-Dados.md
- 010-Arquitetura-de-Integracao.md

---

# 1. Finalidade

Este documento define a **Arquitetura de Serviços do Domínio de Gestão de Compras e Contratações do SIGMUN**.

A arquitetura estabelece a organização dos serviços de negócio, serviços de aplicação e interfaces necessárias para disponibilizar as capacidades do domínio de forma modular, segura, rastreável e integrada à arquitetura corporativa do SIGMUN.

O documento serve como referência para:

- arquitetura de software;
- desenvolvimento de APIs;
- serviços de aplicação;
- integrações;
- interfaces de usuário;
- automações;
- eventos;
- segurança;
- auditoria;
- testes;
- implantação;
- evolução do domínio.

---

# 2. Objetivos

A arquitetura de serviços tem como objetivos:

1. transformar capacidades de negócio em serviços reutilizáveis;
2. separar regras de negócio de interfaces;
3. reduzir acoplamento entre componentes;
4. permitir integração entre domínios;
5. disponibilizar APIs padronizadas;
6. permitir processamento síncrono e assíncrono;
7. garantir segurança e rastreabilidade;
8. permitir evolução independente dos serviços;
9. apoiar diferentes canais de acesso;
10. preservar a governança arquitetural do SIGMUN.

---

# 3. Princípios

A arquitetura deverá observar os seguintes princípios.

## 3.1 Serviços Orientados ao Negócio

Os serviços deverão representar capacidades e responsabilidades reais do domínio.

---

## 3.2 Baixo Acoplamento

Serviços deverão possuir o menor acoplamento possível entre si.

---

## 3.3 Alta Coesão

Cada serviço deverá possuir responsabilidade claramente definida.

---

## 3.4 Contratos Explícitos

As interfaces deverão possuir contratos claramente definidos.

---

## 3.5 API First

Quando houver necessidade de exposição externa ou integração, a definição do contrato deverá preceder a implementação.

---

## 3.6 Segurança por Padrão

Todo serviço deverá considerar:

- autenticação;
- autorização;
- auditoria;
- proteção de dados;
- validação de entrada;
- controle de acesso.

---

## 3.7 Observabilidade

Os serviços deverão permitir:

- logs estruturados;
- métricas;
- rastreamento distribuído;
- identificação de correlação;
- monitoramento de erros.

---

# 4. Visão Geral da Arquitetura

A arquitetura conceitual será organizada em camadas:

```text
Canais
   │
   ▼
APIs / Interfaces
   │
   ▼
Serviços de Aplicação
   │
   ▼
Serviços de Domínio
   │
   ▼
Modelo de Domínio
   │
   ▼
Persistência

Integrações externas deverão utilizar os mecanismos definidos pela Arquitetura de Integração do SIGMUN.

5. Camadas
5.1 Camada de Canais

Responsável pelos canais que utilizam os serviços.

Exemplos:

aplicação web;
aplicação móvel;
portal administrativo;
portal público;
integrações externas;
processos automatizados.
5.2 Camada de API

Responsável pela exposição dos serviços.

Funções:

autenticação;
autorização;
validação;
versionamento;
transformação de dados;
controle de requisições;
documentação.
5.3 Camada de Serviços de Aplicação

Coordena os casos de uso do domínio.

Responsabilidades:

receber comandos;
validar contexto;
coordenar operações;
chamar serviços de domínio;
iniciar transações;
publicar eventos;
retornar resultados.
5.4 Camada de Domínio

Contém:

regras de negócio;
entidades;
objetos de valor;
políticas;
serviços de domínio;
eventos de domínio.
5.5 Camada de Persistência

Responsável pelo armazenamento e recuperação dos dados.

Deverá seguir o Modelo de Dados definido em:

013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md

6. Catálogo de Serviços

Os serviços principais do domínio são:

Código	Serviço
SRV-COMPRAS-001	Gestão de Demandas
SRV-COMPRAS-002	Gestão do Planejamento
SRV-COMPRAS-003	Gestão de Processos
SRV-COMPRAS-004	Gestão de Itens
SRV-COMPRAS-005	Gestão de Procedimentos
SRV-COMPRAS-006	Gestão de Propostas
SRV-COMPRAS-007	Gestão de Fornecedores
SRV-COMPRAS-008	Gestão de Resultados
SRV-COMPRAS-009	Gestão de Contratos
SRV-COMPRAS-010	Gestão de Execução Contratual
SRV-COMPRAS-011	Gestão de Entregas
SRV-COMPRAS-012	Gestão de Medições
SRV-COMPRAS-013	Gestão de Fiscalização
SRV-COMPRAS-014	Gestão de Ocorrências
SRV-COMPRAS-015	Gestão de Alterações Contratuais
SRV-COMPRAS-016	Gestão de Encerramentos
SRV-COMPRAS-017	Consulta e Pesquisa
SRV-COMPRAS-018	Auditoria
SRV-COMPRAS-019	Notificações
SRV-COMPRAS-020	Integração
7. SRV-COMPRAS-001 – Gestão de Demandas

Responsável pelo ciclo de vida das demandas de contratação.

Operações
criarDemanda()
consultarDemanda()
listarDemandas()
atualizarDemanda()
aprovarDemanda()
rejeitarDemanda()
cancelarDemanda()
Eventos
DemandaCriada
DemandaAtualizada
DemandaAprovada
DemandaRejeitada
DemandaCancelada
8. SRV-COMPRAS-002 – Gestão do Planejamento

Responsável pelo planejamento das contratações.

Operações
criarPlanejamento()
consultarPlanejamento()
atualizarPlanejamento()
aprovarPlanejamento()
rejeitarPlanejamento()
Eventos
PlanejamentoCriado
PlanejamentoAtualizado
PlanejamentoAprovado
PlanejamentoRejeitado
9. SRV-COMPRAS-003 – Gestão de Processos

Responsável pela criação e gerenciamento dos processos de contratação.

Operações
abrirProcesso()
consultarProcesso()
atualizarProcesso()
encaminharProcesso()
aprovarProcesso()
cancelarProcesso()
encerrarProcesso()
Eventos
ProcessoAberto
ProcessoAtualizado
ProcessoEncaminhado
ProcessoAprovado
ProcessoCancelado
ProcessoEncerrado
10. SRV-COMPRAS-004 – Gestão de Itens

Responsável pelos itens de contratação.

Operações
adicionarItem()
consultarItem()
atualizarItem()
removerItem()
validarItem()

O serviço deverá controlar:

descrição;
unidade;
quantidade;
especificação;
estimativa;
classificação;
situação.
11. SRV-COMPRAS-005 – Gestão de Procedimentos

Responsável pela condução do procedimento de contratação.

Operações
iniciarProcedimento()
consultarProcedimento()
registrarEtapa()
encerrarProcedimento()
cancelarProcedimento()
12. SRV-COMPRAS-006 – Gestão de Propostas

Responsável pelo recebimento e gerenciamento das propostas.

Operações
registrarProposta()
consultarProposta()
atualizarProposta()
classificarProposta()
desclassificarProposta()
13. SRV-COMPRAS-007 – Gestão de Fornecedores

Responsável pela utilização dos fornecedores no domínio.

O serviço deverá preferencialmente consumir dados do cadastro corporativo.

Operações
consultarFornecedor()
validarFornecedor()
consultarSituacaoFornecedor()

O cadastro mestre do fornecedor não deverá ser duplicado neste domínio.

14. SRV-COMPRAS-008 – Gestão de Resultados

Responsável pelo registro do resultado do procedimento.

Operações
registrarResultado()
consultarResultado()
adjudicar()
homologar()
cancelarResultado()
15. SRV-COMPRAS-009 – Gestão de Contratos

Responsável pelo ciclo de vida do contrato.

Operações
criarContrato()
consultarContrato()
atualizarContrato()
assinarContrato()
iniciarVigencia()
suspenderContrato()
retomarContrato()
encerrarContrato()
Eventos
ContratoCriado
ContratoAssinado
ContratoIniciado
ContratoSuspenso
ContratoRetomado
ContratoEncerrado
16. SRV-COMPRAS-010 – Gestão da Execução Contratual

Responsável pelo acompanhamento da execução do objeto contratado.

Operações
consultarExecucao()
registrarExecucao()
consultarSaldo()
consultarPercentualExecucao()
17. SRV-COMPRAS-011 – Gestão de Entregas

Responsável pelo registro e acompanhamento das entregas.

Operações
registrarEntrega()
consultarEntrega()
aprovarRecebimento()
rejeitarEntrega()
Eventos
EntregaRegistrada
EntregaAprovada
EntregaRejeitada
18. SRV-COMPRAS-012 – Gestão de Medições

Responsável pelo registro das medições contratuais.

Operações
criarMedicao()
consultarMedicao()
submeterMedicao()
aprovarMedicao()
rejeitarMedicao()
cancelarMedicao()
Eventos
MedicaoCriada
MedicaoSubmetida
MedicaoAprovada
MedicaoRejeitada
MedicaoCancelada
19. SRV-COMPRAS-013 – Gestão de Fiscalização

Responsável pelo acompanhamento formal da execução.

Operações
registrarFiscalizacao()
consultarFiscalizacoes()
registrarRelatorio()
registrarParecer()
20. SRV-COMPRAS-014 – Gestão de Ocorrências

Responsável pelo registro de ocorrências.

Operações
registrarOcorrencia()
consultarOcorrencia()
classificarOcorrencia()
encaminharOcorrencia()
resolverOcorrencia()
21. SRV-COMPRAS-015 – Gestão de Alterações Contratuais

Responsável pelas alterações contratuais.

Operações
solicitarAlteracao()
analisarAlteracao()
aprovarAlteracao()
registrarAlteracao()
cancelarAlteracao()

Tipos possíveis:

acréscimo;
supressão;
prorrogação;
reajuste;
repactuação;
revisão;
alteração de responsável;
suspensão;
outras alterações legalmente previstas.
22. SRV-COMPRAS-016 – Gestão de Encerramentos

Responsável pelo encerramento do contrato.

Operações
solicitarEncerramento()
analisarEncerramento()
aprovarEncerramento()
registrarEncerramento()
23. SRV-COMPRAS-017 – Consulta e Pesquisa

Serviço transversal para consultas.

Exemplos:

buscarProcessos()
buscarContratos()
buscarFornecedores()
buscarItens()
buscarDemandas()
buscarMedicoes()
buscarOcorrencias()

Esse serviço deverá evitar que diferentes módulos implementem mecanismos de pesquisa inconsistentes.

24. SRV-COMPRAS-018 – Auditoria

Responsável pela disponibilização dos registros de auditoria.

Operações
consultarAuditoria()
consultarHistorico()
consultarEventos()

O serviço de auditoria deverá ser preferencialmente integrado à infraestrutura corporativa de auditoria do SIGMUN.

25. SRV-COMPRAS-019 – Notificações

Responsável pela geração de notificações relacionadas ao domínio.

Exemplos:

notificarVencimentoContrato()
notificarMedicaoPendente()
notificarEntregaPendente()
notificarOcorrencia()
notificarAlteracao()

A entrega das notificações deverá utilizar o serviço corporativo de notificações.

26. SRV-COMPRAS-020 – Integração

Responsável pela comunicação com outros domínios e sistemas externos.

Exemplos:

sincronizarFornecedor()
consultarDotacao()
registrarEmpenho()
consultarPagamento()
publicarContrato()
publicarTransparencia()

O serviço deverá seguir a Arquitetura de Integração do SIGMUN.

27. APIs

As APIs deverão ser organizadas por recursos de negócio.

Exemplo conceitual:

/api/v1/compras/demandas
/api/v1/compras/planejamentos
/api/v1/compras/processos
/api/v1/compras/itens
/api/v1/compras/procedimentos
/api/v1/compras/propostas
/api/v1/compras/resultados
/api/v1/compras/contratos
/api/v1/compras/entregas
/api/v1/compras/medicoes
/api/v1/compras/fiscalizacoes
/api/v1/compras/ocorrencias
/api/v1/compras/alteracoes
/api/v1/compras/encerramentos

Os caminhos são referências arquiteturais e não representam ainda o contrato definitivo das APIs.

28. Versionamento de APIs

As APIs deverão utilizar versionamento explícito.

Exemplo:

/v1/

Alterações incompatíveis deverão gerar nova versão.

Exemplo:

/v1/compras/contratos
/v2/compras/contratos

A política corporativa de versionamento deverá prevalecer sobre este modelo.

29. Padrão de Operações

As operações deverão seguir padrões REST ou outro padrão corporativo aprovado.

Exemplo:

GET    /demandas
GET    /demandas/{id}
POST   /demandas
PUT    /demandas/{id}
PATCH  /demandas/{id}
DELETE /demandas/{id}

Operações de negócio que representam transições deverão possuir comandos explícitos quando necessário.

Exemplo:

POST /demandas/{id}/aprovar
POST /contratos/{id}/assinar
POST /contratos/{id}/suspender
POST /contratos/{id}/encerrar
30. Idempotência

Operações críticas deverão considerar idempotência.

Especialmente:

criação de registros;
integração financeira;
publicação de contratos;
registro de pagamentos;
processamento de eventos.

O uso de idempotency-key poderá ser adotado para operações apropriadas.

31. Processamento Assíncrono

Operações que não necessitam de resposta imediata poderão utilizar processamento assíncrono.

Exemplos:

publicação em sistemas externos;
geração de relatórios;
notificações;
processamento de grandes volumes;
sincronização;
atualização de indicadores.

Fluxo:

Solicitação
    ↓
Comando
    ↓
Fila/Event Bus
    ↓
Processador
    ↓
Resultado
32. Eventos de Domínio

Os serviços poderão publicar eventos de domínio.

Exemplos:

DemandaCriada
ProcessoAberto
ProcedimentoIniciado
ResultadoHomologado
ContratoAssinado
EntregaRegistrada
MedicaoAprovada
OcorrenciaRegistrada
ContratoAlterado
ContratoEncerrado

Eventos deverão possuir:

identificador;
tipo;
versão;
data/hora;
origem;
identificador de correlação;
entidade relacionada;
payload;
metadados.
33. Correlação

As chamadas entre serviços deverão permitir rastreamento por identificador de correlação.

Exemplo:

correlation_id

Esse identificador deverá acompanhar:

API
 ↓
Serviço
 ↓
Banco
 ↓
Evento
 ↓
Integração externa
34. Autenticação

Os serviços deverão utilizar o mecanismo corporativo de identidade do SIGMUN.

O domínio não deverá implementar mecanismo próprio de autenticação sem justificativa arquitetural.

35. Autorização

A autorização deverá considerar:

usuário;
perfil;
função;
unidade administrativa;
responsabilidade;
processo;
contrato;
operação;
contexto.

Exemplo:

Usuário
   ↓
Perfil
   ↓
Permissão
   ↓
Operação
   ↓
Recurso
36. Segregação de Funções

Os serviços deverão suportar controles de segregação.

Exemplo:

Solicitar
   ≠
Aprovar
   ≠
Homologar
   ≠
Fiscalizar
   ≠
Liquidar
   ≠
Pagar

As regras efetivas deverão ser definidas pelos artefatos de negócio e segurança.

37. Auditoria

Operações relevantes deverão produzir registros de auditoria.

Exemplos:

CREATE
UPDATE
DELETE
APPROVE
REJECT
CANCEL
SIGN
SUSPEND
RESUME
CLOSE

Cada registro deverá permitir identificar:

quem;
quando;
o quê;
onde;
antes;
depois;
motivo, quando aplicável.
38. Tratamento de Erros

As APIs deverão utilizar estrutura padronizada de erros.

Exemplo conceitual:

{
  "codigo": "COMPRAS_CONTRATO_NAO_ENCONTRADO",
  "mensagem": "Contrato não encontrado.",
  "correlationId": "uuid",
  "detalhes": []
}

Os códigos deverão ser estáveis e documentados.

39. Validação

A validação deverá ocorrer em diferentes níveis:

API
 ↓
Aplicação
 ↓
Domínio
 ↓
Persistência

A validação de regras de negócio não deverá ficar exclusivamente na interface do usuário.

40. Transações

Operações que alterem múltiplas entidades relacionadas deverão preservar consistência transacional.

Exemplo:

Aprovar Resultado
       ↓
Atualizar Resultado
       ↓
Atualizar Processo
       ↓
Registrar Evento

A estratégia transacional deverá ser definida conforme o desenho técnico definitivo.

41. Comunicação entre Serviços

Quando serviços estiverem no mesmo contexto transacional, deverá ser evitado o uso desnecessário de chamadas remotas.

Quando houver necessidade de comunicação entre domínios, deverão ser considerados:

APIs;
eventos;
filas;
mensageria;
integração assíncrona.
42. Integração com Gestão de Identidade

Serviços deverão consultar a infraestrutura corporativa para:

identidade do usuário;
perfil;
permissões;
unidade;
sessão;
autenticação.
43. Integração com Gestão Documental

Documentos deverão ser armazenados no serviço corporativo correspondente.

O domínio deverá manter referências aos documentos.

Exemplo:

Contrato
   │
   └── documento_id
44. Integração com Orçamento e Finanças

O domínio poderá consumir serviços relacionados a:

orçamento;
dotação;
empenho;
liquidação;
pagamento.

A responsabilidade financeira continuará pertencendo ao domínio financeiro correspondente.

45. Integração com Transparência

Dados definidos como publicáveis poderão ser disponibilizados ao Portal da Transparência.

Fluxo conceitual:

Gestão de Compras
       ↓
Serviço de Publicação
       ↓
Portal da Transparência
46. Integração com BI e Analytics

Os serviços poderão publicar eventos ou disponibilizar dados para o ambiente analítico.

O domínio analítico não deverá consultar diretamente tabelas transacionais sem uma arquitetura previamente definida.

47. Observabilidade

Todos os serviços deverão disponibilizar:

Logs
estruturados;
pesquisáveis;
correlacionáveis.
Métricas

Exemplos:

quantidade de requisições;
tempo de resposta;
erros;
disponibilidade;
filas;
eventos processados.
Rastreamento

Deverá permitir acompanhar uma operação entre serviços.

48. Desempenho

Os serviços deverão ser projetados para:

baixa latência nas operações interativas;
processamento assíncrono para operações pesadas;
paginação;
filtros;
ordenação;
consultas eficientes;
cache quando justificável.
49. Paginação

Consultas que possam retornar grandes volumes deverão utilizar paginação.

Exemplo:

GET /contratos?page=1&pageSize=50

O padrão definitivo deverá ser estabelecido pela arquitetura corporativa de APIs.

50. Segurança contra Abusos

As APIs deverão considerar:

rate limiting;
proteção contra requisições excessivas;
validação de payload;
proteção contra injeção;
proteção contra enumeração indevida;
controle de tamanho de requisição;
políticas de CORS quando aplicáveis.
51. Resiliência

Integrações externas deverão considerar:

timeout;
retry;
circuit breaker;
idempotência;
dead-letter queue;
monitoramento;
compensação.
52. Disponibilidade

Serviços críticos deverão ser projetados considerando:

redundância;
recuperação;
monitoramento;
backups;
tolerância a falhas;
recuperação de desastres.

As metas definitivas deverão seguir os requisitos não funcionais corporativos.

53. Contratos de Serviço

Cada serviço deverá possuir contrato documentado contendo:

Nome
Objetivo
Responsabilidade
Entradas
Saídas
Erros
Permissões
Eventos
Dependências
SLA
Versionamento
54. Matriz Serviço × Capacidade
Serviço	Capacidade
SRV-COMPRAS-001	CAP-COMPRAS-001
SRV-COMPRAS-002	CAP-COMPRAS-002
SRV-COMPRAS-003	CAP-COMPRAS-003
SRV-COMPRAS-004	CAP-COMPRAS-004
SRV-COMPRAS-005	CAP-COMPRAS-005
SRV-COMPRAS-006	CAP-COMPRAS-006
SRV-COMPRAS-007	CAP-COMPRAS-007
SRV-COMPRAS-008	CAP-COMPRAS-008
SRV-COMPRAS-009	CAP-COMPRAS-005
SRV-COMPRAS-010	CAP-COMPRAS-006
SRV-COMPRAS-011	CAP-COMPRAS-007
SRV-COMPRAS-012	CAP-COMPRAS-008
SRV-COMPRAS-013	CAP-COMPRAS-006
SRV-COMPRAS-014	CAP-COMPRAS-006
SRV-COMPRAS-015	CAP-COMPRAS-009
SRV-COMPRAS-016	CAP-COMPRAS-010
55. Matriz Serviço × Processo
Serviço	Processos
SRV-COMPRAS-001	PROC-COMPRAS-001
SRV-COMPRAS-002	PROC-COMPRAS-002
SRV-COMPRAS-003	PROC-COMPRAS-003
SRV-COMPRAS-004	PROC-COMPRAS-003
SRV-COMPRAS-005	PROC-COMPRAS-004
SRV-COMPRAS-006	PROC-COMPRAS-004
SRV-COMPRAS-007	PROC-COMPRAS-004
SRV-COMPRAS-008	PROC-COMPRAS-004
SRV-COMPRAS-009	PROC-COMPRAS-005
SRV-COMPRAS-010	PROC-COMPRAS-005
SRV-COMPRAS-011	PROC-COMPRAS-007
SRV-COMPRAS-012	PROC-COMPRAS-008
SRV-COMPRAS-013	PROC-COMPRAS-006
SRV-COMPRAS-014	PROC-COMPRAS-006
SRV-COMPRAS-015	PROC-COMPRAS-009
SRV-COMPRAS-016	PROC-COMPRAS-010
56. Matriz Serviço × Caso de Uso
Serviço	Casos de Uso
SRV-COMPRAS-001	UC-COMPRAS-001
SRV-COMPRAS-002	UC-COMPRAS-002
SRV-COMPRAS-003	UC-COMPRAS-003
SRV-COMPRAS-004	UC-COMPRAS-003
SRV-COMPRAS-005	UC-COMPRAS-004
SRV-COMPRAS-006	UC-COMPRAS-004
SRV-COMPRAS-007	UC-COMPRAS-004
SRV-COMPRAS-008	UC-COMPRAS-004
SRV-COMPRAS-009	UC-COMPRAS-005
SRV-COMPRAS-010	UC-COMPRAS-005
SRV-COMPRAS-011	UC-COMPRAS-007
SRV-COMPRAS-012	UC-COMPRAS-008
SRV-COMPRAS-013	UC-COMPRAS-006
SRV-COMPRAS-014	UC-COMPRAS-006
SRV-COMPRAS-015	UC-COMPRAS-009
SRV-COMPRAS-016	UC-COMPRAS-010
57. Dependências Externas

Os principais serviços externos esperados são:

Gestão de Identidade
Gestão Documental
Cadastro Único
Gestão Orçamentária
Gestão Financeira
Gestão Patrimonial
Almoxarifado
Notificações
BI / Analytics
Portal da Transparência
Integrações Governamentais
58. Limites do Domínio

O domínio de Gestão de Compras e Contratações não deverá assumir responsabilidades pertencentes a outros domínios.

Exemplos:

Compras
   ├── solicita informação financeira
   ├── não executa pagamento
   │
   ├── consulta fornecedor
   ├── não é necessariamente o cadastro mestre
   │
   ├── referencia documentos
   ├── não substitui Gestão Documental
   │
   └── disponibiliza dados
       └── não substitui BI
59. Critérios de Qualidade

A arquitetura será considerada adequada quando:

os serviços possuírem responsabilidades claras;
não houver duplicação significativa de responsabilidades;
os serviços estiverem relacionados às capacidades;
os serviços estiverem relacionados aos processos;
os serviços estiverem relacionados aos casos de uso;
as interfaces forem documentáveis;
as dependências estiverem identificadas;
os mecanismos de segurança estiverem definidos;
os mecanismos de auditoria estiverem previstos;
os serviços puderem ser testados independentemente.
60. Critérios de Aceitação

A arquitetura será considerada aprovada quando:

todos os serviços principais do domínio estiverem identificados;
cada serviço possuir responsabilidade definida;
cada serviço estiver associado a pelo menos uma capacidade;
os principais processos estiverem cobertos;
os casos de uso estiverem associados aos serviços;
as principais integrações estiverem identificadas;
APIs puderem ser derivadas dos serviços;
eventos principais estiverem identificados;
segurança estiver contemplada;
auditoria estiver contemplada;
observabilidade estiver contemplada;
versionamento estiver contemplado;
resiliência estiver contemplada;
o modelo estiver alinhado à arquitetura corporativa.
61. Rastreabilidade

A arquitetura deverá manter a seguinte cadeia:

Capacidade
    ↓
Processo
    ↓
Serviço
    ↓
Caso de Uso
    ↓
Requisito
    ↓
Especificação
    ↓
API
    ↓
Implementação
    ↓
Teste

O identificador do serviço deverá ser utilizado nos artefatos técnicos relacionados.

62. Evolução

Novos serviços deverão ser criados somente quando:

existir necessidade de negócio;
a responsabilidade estiver claramente delimitada;
houver ganho de coesão;
houver necessidade de reutilização;
houver necessidade de integração;
houver justificativa arquitetural.

A criação indiscriminada de microserviços deverá ser evitada.

63. Observação Arquitetural

O SIGMUN não deverá adotar automaticamente uma arquitetura de microserviços apenas porque os componentes são chamados de "serviços".

A decomposição deverá ser orientada principalmente por:

domínio;
capacidades;
responsabilidades;
limites de contexto;
necessidade de escala;
necessidade de autonomia;
requisitos de disponibilidade;
integração;
governança.

A tecnologia de implantação poderá variar sem alterar necessariamente o modelo conceitual de serviços.

64. Próximos Artefatos

Após este documento, recomenda-se continuar com:

016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md
65. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-12	Criação da Arquitetura de Serviços do Domínio de Gestão de Compras e Contratações
