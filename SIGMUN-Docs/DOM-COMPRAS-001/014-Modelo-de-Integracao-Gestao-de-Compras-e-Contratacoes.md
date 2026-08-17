#### Modelo de Integração – Gestão de Compras e Contratações


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
- 015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
- 009-Arquitetura-de-Dados.md
- 010-Arquitetura-de-Integracao.md
- 018-Arquitetura-de-Notificacoes.md
- 021-Governanca-de-Dados.md
- 022-Arquitetura-de-BI-Analytics-IA.md


---


# 1. Finalidade


Este documento define o **Modelo de Integração do Domínio de Gestão de Compras e Contratações do SIGMUN**.


O modelo estabelece como o domínio deverá se comunicar com:


- outros domínios do SIGMUN;
- serviços corporativos;
- sistemas municipais;
- sistemas estaduais;
- sistemas federais;
- fornecedores;
- órgãos de controle;
- plataformas de transparência;
- serviços externos autorizados.


O objetivo é garantir que as integrações sejam:


- padronizadas;
- seguras;
- rastreáveis;
- resilientes;
- desacopladas;
- auditáveis;
- versionáveis;
- governáveis.


---


# 2. Objetivos



E não:

Domínio A
   ↓
Banco de Dados do Domínio B
3.3 Contratos Explícitos

Toda integração deverá possuir contrato conhecido pelas partes envolvidas.

3.4 API First

Quando a integração ocorrer por API, o contrato deverá ser definido antes da implementação.

3.5 Eventos para Desacoplamento

Quando apropriado, eventos deverão ser utilizados para comunicar mudanças de estado sem exigir dependência síncrona.

3.6 Segurança por Princípio

Toda integração deverá possuir autenticação, autorização e proteção adequadas ao risco.

3.7 Observabilidade

Toda integração relevante deverá permitir identificar:

origem;
destino;
operação;
data/hora;
resultado;
erro;
correlação.
4. Escopo

Este modelo abrange integrações relacionadas a:

demandas;
planejamento;
processos;
itens;
fornecedores;
procedimentos;
propostas;
resultados;
contratos;
execução contratual;
entregas;
medições;
fiscalização;
alterações contratuais;
encerramentos;
transparência;
orçamento;
finanças;
patrimônio;
almoxarifado;
gestão documental;
identidade;
notificações;
BI e Analytics.
5. Visão Geral

A arquitetura de integração deverá seguir o modelo:

                    SIGMUN
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   Domínios       Serviços       Integrações
   Internos       Corporativos   Externas
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              Gestão de Compras
              e Contratações
6. Tipos de Integração

Serão considerados os seguintes tipos:

Síncrona
Assíncrona
Orientada a Eventos
Batch
Consulta
Comando
Publicação
Importação
Exportação
7. Integrações Síncronas

Serão utilizadas quando o processo depender de uma resposta imediata.

Exemplo:

Gestão de Compras
       │
       │ consulta
       ▼
Gestão de Fornecedores
       │
       │ resposta
       ▼
Gestão de Compras
8. Integrações Assíncronas

Serão utilizadas quando a resposta não precisar ocorrer imediatamente.

Exemplos:

processamento de documentos;
publicação;
sincronização;
notificações;
processamento analítico;
integrações externas de longa duração.
9. Integrações Orientadas a Eventos

Eventos deverão ser utilizados quando houver necessidade de comunicar mudanças de estado.

Exemplo:

ContratoAssinado
       │
       ├──► Notificações
       ├──► Transparência
       ├──► BI
       └──► Gestão Financeira

O produtor do evento não deverá precisar conhecer todos os consumidores.

10. Catálogo de Integrações
Código	Integração	Tipo
INT-COMPRAS-001	Gestão de Identidade	Síncrona
INT-COMPRAS-002	Gestão de Usuários e Permissões	Síncrona
INT-COMPRAS-003	Cadastro de Fornecedores	Síncrona
INT-COMPRAS-004	Gestão Orçamentária	Síncrona
INT-COMPRAS-005	Gestão Financeira	Síncrona/Assíncrona
INT-COMPRAS-006	Gestão Documental	Síncrona
INT-COMPRAS-007	Notificações	Assíncrona
INT-COMPRAS-008	Transparência	Assíncrona
INT-COMPRAS-009	BI e Analytics	Assíncrona
INT-COMPRAS-010	Gestão Patrimonial	Síncrona/Assíncrona
INT-COMPRAS-011	Almoxarifado	Síncrona/Assíncrona
INT-COMPRAS-012	Sistemas Governamentais	Síncrona/Assíncrona
INT-COMPRAS-013	Portal Público	Assíncrona
INT-COMPRAS-014	Serviços de Assinatura	Síncrona
INT-COMPRAS-015	Serviço de Auditoria	Assíncrona
11. Integração com Gestão de Identidade

O domínio deverá utilizar o serviço corporativo de identidade para:

autenticação;
identificação do usuário;
consulta de perfis;
consulta de permissões;
encerramento de sessão.

O domínio não deverá manter cadastro independente de credenciais.

12. Integração com Cadastro de Fornecedores

O domínio deverá consumir o cadastro corporativo de fornecedores quando este existir.

Deverão ser evitadas duplicações do cadastro mestre.

Informações possíveis:

Fornecedor
CNPJ/CPF
Razão Social
Nome Fantasia
Situação
Endereço
Contatos
Representantes

Os dados efetivamente disponibilizados deverão respeitar a governança de dados.

13. Integração com Gestão Orçamentária

A Gestão de Compras poderá consultar:

orçamento;
programa;
ação;
fonte;
natureza da despesa;
dotação;
saldo disponível.

Exemplo:

Processo de Compra
       ↓
Consulta Orçamentária
       ↓
Dotação
       ↓
Saldo
14. Integração com Gestão Financeira

A integração poderá envolver:

empenho;
liquidação;
pagamento;
retenções;
situação financeira.

O domínio de Compras não deverá executar diretamente responsabilidades pertencentes ao domínio financeiro.

15. Integração com Gestão Documental

Documentos do processo deverão utilizar o serviço corporativo de Gestão Documental.

Exemplo:

Processo
   │
   ├── Documento de Demanda
   ├── Documento Técnico
   ├── Propostas
   ├── Pareceres
   ├── Contrato
   └── Relatórios

O domínio deverá manter referências aos documentos, e não necessariamente seus conteúdos binários.

16. Integração com Notificações

Eventos relevantes poderão gerar notificações.

Exemplos:

Contrato próximo do vencimento
Medição pendente
Entrega pendente
Aprovação pendente
Ocorrência registrada
Alteração contratual solicitada

Fluxo:

Gestão de Compras
       ↓
Evento
       ↓
Serviço de Notificações
       ↓
E-mail / Aplicativo / Portal / Outros
17. Integração com Transparência

Informações classificadas como públicas poderão ser encaminhadas ao ambiente de transparência.

Exemplos:

processos;
contratos;
fornecedores;
valores;
objetos;
vigências;
alterações;
resultados;
pagamentos, quando provenientes do domínio financeiro.

A publicação deverá respeitar:

classificação da informação;
proteção de dados pessoais;
regras de transparência;
requisitos legais.
18. Integração com BI e Analytics

O domínio deverá disponibilizar dados para análise gerencial.

Exemplos:

quantidade de processos;
valores contratados;
tempo médio;
fornecedores;
contratos vigentes;
contratos próximos do vencimento;
execução contratual;
economia obtida;
quantidade de ocorrências.

Preferencialmente:

Transacional
     ↓
Eventos / ETL / ELT
     ↓
Camada Analítica
     ↓
BI / Analytics / IA
19. Integração com Patrimônio

Quando uma contratação resultar em aquisição de bens permanentes, poderá ocorrer integração com Gestão Patrimonial.

Fluxo:

Contrato
   ↓
Entrega
   ↓
Recebimento
   ↓
Bem
   ↓
Patrimônio

A gestão patrimonial deverá permanecer sob responsabilidade do domínio correspondente.

20. Integração com Almoxarifado

Quando houver aquisição de materiais de consumo:

Contrato
   ↓
Entrega
   ↓
Recebimento
   ↓
Entrada no Estoque

A gestão de estoque deverá permanecer no domínio de Almoxarifado.

21. Integração com Assinatura Eletrônica

Quando aplicável:

Contrato
   ↓
Serviço de Assinatura
   ↓
Documento Assinado
   ↓
Gestão Documental

O domínio deverá armazenar as referências necessárias para rastrear a assinatura.

22. Integração com Auditoria

Operações críticas poderão gerar eventos de auditoria.

Exemplo:

ContratoAlterado
       ↓
Serviço de Auditoria

O serviço de auditoria deverá possuir mecanismo corporativo próprio.

23. Integrações Governamentais

O domínio poderá integrar-se a plataformas e sistemas governamentais conforme necessidade e regulamentação.

Exemplos genéricos:

Sistemas Federais
Sistemas Estaduais
Órgãos de Controle
Plataformas de Compras
Portais Oficiais
Serviços de Validação

Cada integração deverá possuir contrato e documentação próprios.

24. Gateway de Integração

Quando apropriado, integrações externas deverão utilizar infraestrutura corporativa de integração.

Modelo:

SIGMUN
   ↓
API Gateway / Integration Layer
   ↓
Sistema Externo

O objetivo é evitar que cada serviço implemente diretamente mecanismos distintos de comunicação externa.

25. APIs

As APIs deverão possuir:

identificação;
versionamento;
documentação;
autenticação;
autorização;
limites de uso;
tratamento de erros;
rastreabilidade.

Exemplo:

/api/v1/compras/demandas
/api/v1/compras/processos
/api/v1/compras/contratos
/api/v1/compras/medicoes
26. Webhooks

Webhooks poderão ser utilizados quando sistemas externos necessitarem receber notificações de eventos.

Exemplo:

ContratoAssinado
       ↓
Webhook
       ↓
Sistema Consumidor

Webhooks deverão possuir:

autenticação;
assinatura;
retry;
idempotência;
controle de origem;
registro de entrega.
27. Mensageria

Quando adotada mensageria, deverão ser considerados:

filas;
tópicos;
consumidores;
produtores;
dead-letter queue;
retry;
idempotência;
ordenação quando necessária.
28. Contratos de Integração

Cada integração deverá possuir:

Código
Nome
Objetivo
Sistema Origem
Sistema Destino
Responsável
Tipo
Protocolo
Formato
Autenticação
Dados
Frequência
Timeout
Retry
SLA
Auditoria
Versionamento
29. Formatos de Dados

Os formatos preferenciais serão:

JSON
XML
CSV
PDF

A escolha deverá considerar o contrato e a natureza da integração.

Para APIs modernas, JSON deverá ser preferencial quando não houver requisito contrário.

30. Padronização de Identificadores

Os sistemas deverão utilizar identificadores estáveis.

Exemplos:

UUID
Código do Processo
Código do Contrato
Código do Fornecedor
Código do Documento

Não deverão ser utilizados identificadores locais incompatíveis sem mecanismo de correspondência.

31. Correlação

Toda integração relevante deverá possuir identificador de correlação.

Exemplo:

correlation_id

Fluxo:

Requisição
   ↓
Serviço
   ↓
Integração
   ↓
Sistema Externo
   ↓
Resposta

Todos os registros deverão permitir relacionar a operação original.

32. Idempotência

Operações que possam ser repetidas deverão ser idempotentes quando aplicável.

Exemplos:

envio de contrato;
registro de empenho;
publicação;
eventos;
notificações.
33. Retry

Falhas transitórias poderão ser tratadas utilizando retry.

Exemplo:

Tentativa 1
   ↓
Falha
   ↓
Tentativa 2
   ↓
Falha
   ↓
Tentativa 3
   ↓
Dead Letter

O retry deverá possuir limites para evitar tempestades de requisições.

34. Circuit Breaker

Integrações críticas deverão considerar circuit breaker quando apropriado.

Estados conceituais:

CLOSED
   ↓
OPEN
   ↓
HALF-OPEN
   ↓
CLOSED
35. Timeout

Toda chamada externa deverá possuir timeout definido.

Não deverão existir chamadas indefinidamente bloqueadas.

36. Dead Letter Queue

Mensagens que não puderem ser processadas após as tentativas previstas deverão ser encaminhadas para mecanismo de tratamento.

Exemplo:

Fila
 ↓
Processamento
 ↓
Erro
 ↓
Retry
 ↓
Erro
 ↓
DLQ
37. Segurança das Integrações

Integrações deverão utilizar mecanismos adequados de:

autenticação;
autorização;
criptografia;
validação;
assinatura;
controle de origem.
38. Gestão de Credenciais

Credenciais de integração deverão ser armazenadas em mecanismos seguros.

Não deverão ser armazenadas diretamente:

no código;
em arquivos versionados;
em repositórios públicos;
em scripts sem proteção.
39. Controle de Acesso

Cada integração deverá possuir somente as permissões necessárias.

Exemplo:

Integração Financeira
   ↓
pode consultar empenho
   ↓
não pode administrar usuários
40. Proteção de Dados Pessoais

Dados pessoais transmitidos entre sistemas deverão respeitar:

finalidade;
necessidade;
minimização;
segurança;
controle de acesso;
rastreabilidade.

Sempre que possível, deverá ser transmitido somente o conjunto mínimo de dados necessário.

41. Classificação dos Dados Integrados

Cada integração deverá identificar a classificação das informações transmitidas.

Exemplo:

Informação	Classificação
Número do processo	Pública/Conforme política
Objeto	Pública/Conforme política
Valor contratado	Pública/Conforme política
Dados de contato	Conforme classificação
Credenciais	Restrita
Tokens	Confidencial

A classificação definitiva deverá seguir a Política de Classificação da Informação.

42. Publicação de Eventos

Eventos deverão possuir estrutura padronizada.

Exemplo:

{
  "eventId": "uuid",
  "eventType": "ContratoAssinado",
  "version": "1.0",
  "occurredAt": "2026-08-13T20:00:00Z",
  "source": "gestao-compras",
  "correlationId": "uuid",
  "entityId": "uuid",
  "payload": {}
}
43. Versionamento de Eventos

Alterações incompatíveis deverão gerar nova versão do evento.

Exemplo:

ContratoAssinado.v1
ContratoAssinado.v2

Consumidores deverão possuir estratégia de compatibilidade.

44. Compatibilidade

Mudanças nos contratos de integração deverão priorizar compatibilidade retroativa.

Alterações incompatíveis deverão:

possuir nova versão;
ser comunicadas;
possuir período de transição;
possuir documentação.
45. Monitoramento

Deverão ser monitorados:

disponibilidade;
latência;
erros;
timeout;
quantidade de chamadas;
mensagens pendentes;
mensagens rejeitadas;
retries;
DLQ;
indisponibilidade externa.
46. Indicadores de Integração

Indicadores recomendados:

Indicador	Objetivo
Disponibilidade	Medir disponibilidade
Latência	Medir tempo de resposta
Taxa de erro	Identificar falhas
Taxa de retry	Identificar instabilidade
Mensagens pendentes	Avaliar backlog
Mensagens em DLQ	Identificar falhas persistentes
Tempo de processamento	Avaliar desempenho
Taxa de sucesso	Avaliar qualidade
47. Tratamento de Erros

Erros deverão ser classificados.

Exemplos:

VALIDATION_ERROR
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
NOT_FOUND
TIMEOUT
RATE_LIMIT
EXTERNAL_SERVICE_ERROR
INTERNAL_ERROR
48. Registro de Erros

Cada falha relevante deverá possuir:

timestamp
integration_id
operation
source
target
status
error_code
message
correlation_id

Informações sensíveis não deverão ser gravadas indevidamente nos logs.

49. Integração com Ambiente Offline

Quando aplicações de campo ou móveis participarem do domínio, poderá ser utilizado o princípio Offline First definido na arquitetura corporativa do SIGMUN.

O mecanismo deverá considerar:

Dispositivo
   ↓
Operação Offline
   ↓
Armazenamento Local
   ↓
Sincronização
   ↓
SIGMUN

Deverão existir mecanismos para:

identificação de conflitos;
sincronização;
idempotência;
autenticação;
proteção local;
auditoria.
50. Sincronização

Processos de sincronização deverão identificar:

origem;
destino;
versão;
timestamp;
identificador;
situação;
resultado.
51. Conflitos de Dados

Quando houver conflito entre versões, o sistema deverá possuir política definida.

Possibilidades:

Última versão válida
Prioridade do servidor
Resolução manual
Mesclagem
Rejeição

A estratégia deverá ser definida conforme o tipo de dado.

52. Integração com Serviços Corporativos

O domínio deverá preferencialmente consumir serviços corporativos existentes para:

identidade;
usuários;
notificações;
documentos;
auditoria;
classificação;
indicadores;
BI;
integrações.

A criação de serviços duplicados deverá ser evitada.

53. Integrações Proibidas

Não deverão ser adotadas, salvo justificativa arquitetural:

acesso direto ao banco de outro domínio;
compartilhamento indiscriminado de tabelas;
compartilhamento de credenciais;
APIs sem autenticação;
dependência de telas para integração;
scraping de interfaces quando houver API oficial;
duplicação desnecessária de cadastros mestres.
54. Matriz Sistema × Integração
Sistema/Serviço	Compras	Tipo
Identidade	Sim	Síncrona
Usuários	Sim	Síncrona
Fornecedores	Sim	Síncrona
Orçamento	Sim	Síncrona
Financeiro	Sim	Síncrona/Assíncrona
Gestão Documental	Sim	Síncrona
Notificações	Sim	Assíncrona
Transparência	Sim	Assíncrona
BI/Analytics	Sim	Assíncrona
Patrimônio	Condicional	Síncrona/Assíncrona
Almoxarifado	Condicional	Síncrona/Assíncrona
Assinatura Eletrônica	Condicional	Síncrona
Auditoria	Sim	Assíncrona
Sistemas Governamentais	Condicional	Síncrona/Assíncrona
55. Matriz Serviço × Integração
Serviço de Compras	Integrações Principais
Gestão de Demandas	Identidade, Orçamento
Gestão de Planejamento	Orçamento
Gestão de Processos	Identidade, Documentos
Gestão de Itens	Cadastro, Almoxarifado
Gestão de Procedimentos	Documentos, Identidade
Gestão de Propostas	Documentos
Gestão de Fornecedores	Cadastro de Fornecedores
Gestão de Resultados	Identidade, Auditoria
Gestão de Contratos	Documentos, Assinatura, Transparência
Execução Contratual	Financeiro, Patrimônio, Almoxarifado
Entregas	Almoxarifado, Patrimônio
Medições	Financeiro
Fiscalização	Documentos, Notificações
Ocorrências	Notificações, Auditoria
Alterações Contratuais	Documentos, Assinatura
Encerramentos	Financeiro, Documentos
56. Fluxo Integrado de Contratação

Fluxo conceitual:

Demanda
   ↓
Planejamento
   ↓
Processo
   ↓
Procedimento
   ↓
Propostas
   ↓
Resultado
   ↓
Contrato
   ↓
Assinatura
   ↓
Publicação
   ↓
Execução
   ↓
Entrega
   ↓
Medição
   ↓
Financeiro
   ↓
Encerramento
57. Fluxo de Publicação
Contrato Aprovado
       ↓
Validação
       ↓
Classificação
       ↓
Proteção de Dados
       ↓
Publicação
       ↓
Portal da Transparência
58. Fluxo Financeiro
Contrato
   ↓
Execução
   ↓
Medição
   ↓
Aprovação
   ↓
Empenho
   ↓
Liquidação
   ↓
Pagamento

As etapas financeiras deverão permanecer sob responsabilidade do domínio financeiro correspondente.

59. Fluxo Patrimonial
Contrato
   ↓
Entrega
   ↓
Recebimento
   ↓
Identificação do Bem
   ↓
Patrimônio
60. Fluxo de Almoxarifado
Contrato
   ↓
Entrega
   ↓
Recebimento
   ↓
Conferência
   ↓
Entrada no Estoque
61. Rastreabilidade

Toda integração deverá permitir rastrear:

Origem
 ↓
Operação
 ↓
Mensagem
 ↓
Destino
 ↓
Resposta
 ↓
Resultado

A rastreabilidade deverá utilizar correlation_id e identificadores de negócio.

62. Governança das Integrações

Cada integração deverá possuir responsável definido.

Responsabilidades:

manter contrato;
acompanhar disponibilidade;
tratar incidentes;
revisar segurança;
controlar versões;
acompanhar indicadores.
63. Catálogo Corporativo

As integrações deverão ser registradas no catálogo corporativo de integrações do SIGMUN.

O catálogo deverá permitir identificar:

sistema;
serviço;
proprietário;
consumidor;
produtor;
contrato;
versão;
situação;
criticidade.
64. Criticidade

Cada integração deverá possuir classificação de criticidade.

Sugestão:

Crítica
Alta
Média
Baixa

A classificação deverá considerar:

impacto operacional;
impacto financeiro;
impacto legal;
impacto ao cidadão;
dependência;
disponibilidade.
65. Continuidade

Integrações críticas deverão possuir estratégia de continuidade.

Possibilidades:

retry;
fila;
cache;
contingência;
processamento posterior;
operação manual;
fallback.
66. Critérios de Aceitação

O modelo será considerado aprovado quando:

os principais sistemas integrados estiverem identificados;
cada integração possuir finalidade;
os responsáveis estiverem identificados;
os protocolos puderem ser definidos;
os mecanismos de segurança estiverem previstos;
as integrações síncronas e assíncronas estiverem diferenciadas;
os eventos relevantes estiverem identificados;
os mecanismos de retry estiverem previstos;
idempotência estiver contemplada;
auditoria estiver contemplada;
observabilidade estiver contemplada;
versionamento estiver contemplado;
proteção de dados estiver contemplada;
os limites entre domínios estiverem preservados.
67. Rastreabilidade Arquitetural

A cadeia de rastreabilidade deverá ser:

Capacidade
   ↓
Processo
   ↓
Serviço
   ↓
Integração
   ↓
Contrato de Integração
   ↓
API / Evento
   ↓
Implementação
   ↓
Teste
68. Evolução

Novas integrações deverão ser avaliadas antes de sua implementação.

A avaliação deverá considerar:

existência de serviço corporativo;
necessidade de negócio;
impacto;
segurança;
custo;
manutenção;
criticidade;
volume;
desempenho;
interoperabilidade.
69. Decisões Arquiteturais

Decisões relevantes sobre integração deverão ser registradas em ADR.

Exemplos:

ADR-XXX – Escolha de API REST
ADR-XXX – Uso de Eventos
ADR-XXX – Estratégia de Mensageria
ADR-XXX – Integração com Sistema Externo
ADR-XXX – Estratégia Offline First
70. Próximos Artefatos

Recomenda-se que os próximos documentos aprofundem:

015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md
71. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Modelo de Integração do Domínio de Gestão de Compras e Contratações

Documento: 014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente
