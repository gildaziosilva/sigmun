#### Plano de Testes – Gestão de Compras e Contratações


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
- 014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md
- 015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
- 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
- 010-Arquitetura-de-Testes.md
- 015-Plano-de-Auditoria.md
- 016-Plano-de-Gestao-de-Conformidade.md
- 017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md


---


# 1. Finalidade


Este documento define o **Plano de Testes do Domínio de Gestão de Compras e Contratações do SIGMUN**.


O plano estabelece a estratégia, os níveis, tipos, ambientes, dados, responsabilidades, critérios e evidências necessários para verificar se o domínio atende aos requisitos definidos.


O objetivo é garantir que o domínio seja:


- funcionalmente correto;
- seguro;
- integrado;
- auditável;
- resiliente;
- performático;
- utilizável;
- rastreável;
- compatível com as regras de negócio.


---


# 2. Objetivos


São objetivos deste plano:


1. validar os requisitos funcionais;
2. validar os requisitos não funcionais;
3. verificar as regras de negócio;
4. validar os critérios de aceitação;
5. verificar as integrações;
6. validar o modelo de segurança;
7. verificar a trilha de auditoria;
8. validar o modelo de dados;
9. identificar defeitos;
10. reduzir riscos de implantação;
11. garantir rastreabilidade entre requisitos e testes;
12. produzir evidências de qualidade;
13. apoiar homologação;
14. apoiar implantação;
15. garantir regressão controlada.


---


# 3. Princípios de Testes


## 3.1 Qualidade desde o Início


Os testes deverão ser considerados desde a definição dos requisitos.


---


## 3.2 Rastreabilidade


Todo requisito relevante deverá possuir testes correspondentes.


3.3 Automação Sempre que Viável

Testes repetitivos deverão ser automatizados quando houver viabilidade técnica e benefício.

3.4 Testes Baseados em Risco

Funcionalidades críticas deverão receber maior cobertura.

3.5 Independência

Sempre que possível, a validação deverá possuir independência em relação ao desenvolvimento.

3.6 Evidência

Toda execução relevante deverá gerar evidência suficiente para demonstrar o resultado.

4. Escopo

O plano contempla:

demandas;
planejamento;
processos;
procedimentos;
itens;
fornecedores;
propostas;
resultados;
contratos;
documentos;
assinaturas;
execução contratual;
entregas;
medições;
fiscalização;
ocorrências;
alterações;
encerramentos;
integrações;
segurança;
auditoria;
notificações;
relatórios;
APIs;
eventos;
importação;
exportação.
5. Fora do Escopo

Não fazem parte deste plano, salvo quando diretamente necessários para validar o domínio:

testes de sistemas externos sob responsabilidade exclusiva de terceiros;
infraestrutura física não relacionada ao sistema;
funcionalidades não pertencentes ao domínio;
alterações em sistemas legados que não estejam sob responsabilidade do SIGMUN.

Quando uma integração externa for necessária para o teste, poderá ser utilizado ambiente simulado.

6. Estratégia Geral

A estratégia seguirá uma abordagem em camadas:

Testes Unitários
       ↓
Testes de Componentes
       ↓
Testes de Integração
       ↓
Testes de API
       ↓
Testes de Sistema
       ↓
Testes de Segurança
       ↓
Testes de Performance
       ↓
Testes de Aceitação
       ↓
Homologação
7. Pirâmide de Testes

A estratégia deverá priorizar maior quantidade de testes rápidos e automatizados nas camadas inferiores.

          Aceitação
             ▲
          Sistema
             ▲
        Integração
             ▲
         Componentes
             ▲
           Unitário
8. Níveis de Teste

Serão utilizados os seguintes níveis:

teste unitário;
teste de componente;
teste de integração;
teste de API;
teste de sistema;
teste de segurança;
teste de performance;
teste de usabilidade;
teste de aceitação;
teste de regressão.
9. Testes Unitários

Os testes unitários deverão validar unidades isoladas de código.

Exemplos:

validações;
cálculos;
regras;
conversões;
serviços;
componentes;
funções.

Deverão ser priorizadas regras de negócio críticas.

10. Testes de Componentes

Deverão validar componentes do domínio de forma isolada.

Exemplos:

Serviço de Demandas
Serviço de Processos
Serviço de Contratos
Serviço de Medições
Serviço de Fornecedores
11. Testes de Integração

Deverão validar a comunicação entre componentes e domínios.

Exemplos:

Compras ↔ Orçamento
Compras ↔ Financeiro
Compras ↔ Documentos
Compras ↔ Notificações
Compras ↔ Patrimônio
Compras ↔ Almoxarifado
12. Testes de API

As APIs deverão ser testadas quanto a:

contrato;
autenticação;
autorização;
validação;
resposta;
códigos HTTP;
erros;
paginação;
filtros;
ordenação;
versionamento;
idempotência.
13. Testes de Eventos

Eventos deverão ser validados quanto a:

estrutura;
produtor;
consumidor;
conteúdo;
versão;
duplicidade;
ordem, quando necessária;
retry;
dead-letter queue.
14. Testes de Sistema

Os testes de sistema deverão validar o comportamento completo do domínio.

Exemplo:

Demanda
 ↓
Planejamento
 ↓
Processo
 ↓
Procedimento
 ↓
Resultado
 ↓
Contrato
 ↓
Execução
 ↓
Encerramento
15. Testes Funcionais

Deverão verificar se cada funcionalidade atende ao requisito correspondente.

Exemplos:

criar demanda;
alterar demanda;
aprovar demanda;
criar processo;
registrar proposta;
registrar resultado;
criar contrato;
assinar contrato;
registrar entrega;
registrar medição;
encerrar contrato.
16. Testes de Regras de Negócio

Cada regra de negócio deverá possuir cenários positivos e negativos.

Exemplo:

Regra:
Contrato não pode ser encerrado
sem que as obrigações obrigatórias
tenham sido verificadas.

Testes:

Cenário 1 → obrigações concluídas → permitido


Cenário 2 → obrigações pendentes → rejeitado
17. Testes de Validação

Deverão ser testadas:

campos obrigatórios;
formatos;
limites;
valores;
datas;
relacionamentos;
unicidade;
consistência.
18. Testes de Fluxo

Os principais fluxos deverão ser testados de ponta a ponta.

Exemplo:

Demanda
   ↓
Processo
   ↓
Contratação
   ↓
Contrato
   ↓
Execução
   ↓
Pagamento
   ↓
Encerramento
19. Testes de Cenários Positivos

Deverão validar operações esperadas.

Exemplo:

Usuário autorizado
+
Dados válidos
+
Estado correto
=
Operação concluída
20. Testes de Cenários Negativos

Deverão validar situações inválidas.

Exemplo:

Usuário sem permissão
+
Operação crítica
=
Acesso negado
21. Testes de Exceção

Deverão validar:

dados inválidos;
serviço indisponível;
timeout;
duplicidade;
inconsistência;
falha de integração;
erro de autenticação;
conflito.
22. Testes de Segurança

Os testes de segurança deverão validar:

autenticação;
autorização;
segregação de funções;
proteção de dados;
sessões;
APIs;
tokens;
logs;
auditoria;
acesso indevido.
23. Testes de Controle de Acesso

Deverão ser testados diferentes perfis.

Exemplo:

Solicitante
Analista
Gestor
Fiscal
Administrador
Auditor

Cada perfil deverá acessar somente as funcionalidades autorizadas.

24. Testes de Segregação de Funções

Deverão ser testados conflitos de responsabilidade.

Exemplo:

Usuário que solicita
não deve automaticamente
aprovar sua própria solicitação,
quando a regra de segregação exigir
aprovação independente.
25. Testes de Auditoria

Deverão verificar se as operações críticas geram registros.

Exemplo:

Operação
   ↓
Registro de Auditoria
   ↓
Usuário
   ↓
Data/Hora
   ↓
Entidade
   ↓
Resultado
26. Testes de Integridade da Auditoria

Deverão ser realizados testes para verificar se registros de auditoria:

não podem ser alterados indevidamente;
não podem ser apagados por usuários comuns;
possuem identificação;
possuem timestamp;
possuem correlation_id.
27. Testes de Dados

O modelo de dados deverá ser validado quanto a:

integridade referencial;
constraints;
unicidade;
obrigatoriedade;
relacionamentos;
índices;
consistência;
concorrência.
28. Testes de Migração

Quando houver migração de dados, deverão ser validados:

quantidade;
integridade;
consistência;
relacionamentos;
valores;
identificadores;
histórico;
rastreabilidade.
29. Testes de Importação

Importações deverão validar:

formato;
estrutura;
registros válidos;
registros inválidos;
duplicidade;
limites;
erros;
rollback quando aplicável.
30. Testes de Exportação

Exportações deverão verificar:

filtros;
quantidade;
conteúdo;
formato;
permissões;
classificação da informação;
proteção de dados.
31. Testes de Integração Externa

Deverão validar:

SIGMUN
   ↓
Integração
   ↓
Sistema Externo
   ↓
Resposta

Deverão ser considerados:

sucesso;
timeout;
indisponibilidade;
resposta inválida;
autenticação;
rate limit;
retry.
32. Testes de Resiliência

Deverão ser testadas falhas como:

indisponibilidade de serviço;
perda de conexão;
timeout;
mensagens duplicadas;
mensagens fora de ordem;
falhas temporárias.
33. Testes de Retry

Deverá ser verificado se o mecanismo de retry:

possui limite;
respeita intervalo;
não duplica operações;
encaminha falhas persistentes para DLQ.
34. Testes de Idempotência

Operações repetidas deverão produzir resultado consistente quando definidas como idempotentes.

Exemplo:

Requisição 1 → contrato registrado


Requisição 2 igual
        ↓
Não deverá criar contrato duplicado.
35. Testes de Performance

Deverão avaliar:

tempo de resposta;
throughput;
concorrência;
consumo de recursos;
consultas;
relatórios;
APIs.
36. Testes de Carga

Deverão simular volume esperado de utilização.

Exemplos:

Usuários simultâneos
Processos simultâneos
Consultas simultâneas
Uploads simultâneos
APIs simultâneas
37. Testes de Estresse

Deverão avaliar o comportamento acima da carga normal.

Objetivo:

identificar limite;
observar degradação;
validar recuperação;
identificar gargalos.
38. Testes de Recuperação

Deverão validar recuperação após:

falha do serviço;
reinicialização;
indisponibilidade do banco;
falha de integração;
interrupção de processamento.
39. Testes de Continuidade

Deverão validar os mecanismos definidos para continuidade do domínio.

Quando aplicável:

Falha
 ↓
Contingência
 ↓
Recuperação
 ↓
Reconciliação
 ↓
Operação normal
40. Testes Offline First

Quando houver aplicações móveis ou de campo, deverão ser testados:

operação offline;
armazenamento local;
sincronização;
conflitos;
duplicidade;
recuperação de conexão;
autenticação;
proteção local.
41. Testes de Sincronização

Deverão validar:

Operação local
 ↓
Fila local
 ↓
Sincronização
 ↓
Servidor
 ↓
Confirmação
42. Testes de Conflito

Deverão ser simulados conflitos como:

Dispositivo A altera registro
Dispositivo B altera o mesmo registro
        ↓
Sincronização
        ↓
Conflito

A estratégia definida pelo domínio deverá ser aplicada.

43. Testes de Usabilidade

Deverão avaliar:

clareza;
navegação;
mensagens;
formulários;
acessibilidade;
consistência;
compreensão das tarefas.
44. Testes de Acessibilidade

Deverão considerar:

teclado;
contraste;
leitores de tela;
foco;
labels;
mensagens;
navegação.
45. Testes de Compatibilidade

Quando aplicável, deverão ser avaliados:

navegadores;
dispositivos;
resoluções;
sistemas operacionais;
versões suportadas.
46. Testes de Notificações

Deverão verificar:

geração;
destinatário;
conteúdo;
prioridade;
duplicidade;
entrega;
falha;
retry.
47. Testes de Documentos

Deverão validar:

criação;
anexação;
versionamento;
visualização;
assinatura;
publicação;
arquivamento.
48. Testes de Assinatura

Deverão validar:

Solicitação
 ↓
Envio
 ↓
Assinatura
 ↓
Validação
 ↓
Conclusão

Também deverão ser testados:

recusa;
cancelamento;
expiração;
falha.
49. Testes de Relatórios

Relatórios deverão ser verificados quanto a:

filtros;
cálculos;
agrupamentos;
totais;
permissões;
consistência dos dados;
exportação.
50. Testes de Transparência

Deverão verificar se informações classificadas como públicas são corretamente disponibilizadas.

Deverão ser testados:

publicação;
atualização;
retirada;
consistência;
proteção de dados pessoais.
51. Testes de LGPD

Deverão verificar:

acesso mínimo;
proteção de dados;
minimização;
exportação;
exposição indevida;
logs;
permissões.
52. Testes de Observabilidade

Deverão verificar se o sistema produz:

logs;
métricas;
traces, quando aplicável;
correlation_id;
alertas;
indicadores.
53. Testes de API de Observabilidade

Quando houver APIs técnicas, deverão ser avaliados:

/health
/readiness
/liveness
/metrics

conforme arquitetura adotada.

54. Testes de Regressão

Toda alteração relevante deverá executar conjunto de testes de regressão.

A suíte deverá crescer continuamente.

55. Testes Automatizados

Deverão ser priorizados para automação:

regras de negócio;
validações;
APIs;
integrações;
segurança repetitiva;
regressão;
cálculos;
fluxos críticos.
56. Testes Manuais

Serão utilizados quando:

automação não for economicamente viável;
houver avaliação visual;
houver avaliação de usabilidade;
houver cenário exploratório;
houver necessidade de julgamento humano.
57. Testes Exploratórios

Testes exploratórios poderão ser utilizados para descobrir comportamentos não previstos.

Deverão registrar:

objetivo;
cenário;
comportamento observado;
evidência;
resultado.
58. Dados de Teste

Os dados deverão ser controlados.

Categorias:

Dados sintéticos
Dados anonimizados
Dados de referência
Dados de massa
Dados de exceção

Dados reais contendo informações pessoais deverão ser evitados nos ambientes de teste.

59. Dados Sintéticos

Deverão ser utilizados sempre que possível.

Exemplos:

Fornecedores fictícios
Processos fictícios
Contratos fictícios
Usuários fictícios
Documentos fictícios
60. Dados Sensíveis

Dados pessoais ou informações restritas deverão ser protegidos.

Quando houver necessidade de utilizar dados derivados de produção, deverão ser aplicadas técnicas adequadas de:

anonimização;
mascaramento;
pseudonimização.
61. Ambiente de Desenvolvimento

Utilizado para:

testes unitários;
testes de componentes;
testes iniciais.
62. Ambiente de Testes

Utilizado para:

integração;
API;
segurança;
regressão;
sistema.
63. Ambiente de Homologação

Utilizado para:

testes de aceitação;
validação pelos usuários;
testes de negócio;
homologação.
64. Ambiente de Produção

Não deverá ser utilizado como ambiente normal de testes.

Testes em produção somente poderão ocorrer mediante autorização e procedimento controlado.

65. Critérios de Entrada

Uma execução de testes poderá iniciar quando:

requisitos estiverem definidos;
ambiente estiver disponível;
versão estiver identificada;
dados de teste estiverem preparados;
casos de teste estiverem disponíveis;
dependências estiverem disponíveis;
critérios de entrada forem atendidos.
66. Critérios de Saída

Uma etapa poderá ser encerrada quando:

testes planejados forem executados;
defeitos críticos forem tratados;
defeitos impeditivos forem resolvidos;
cobertura mínima for atingida;
evidências estiverem registradas;
riscos residuais forem conhecidos;
aprovação for obtida.
67. Classificação de Defeitos

Os defeitos deverão ser classificados.

Crítico
Alto
Médio
Baixo
68. Defeito Crítico

Exemplos:

perda de dados;
fraude possível;
acesso indevido grave;
corrupção de contrato;
falha de segurança crítica;
impossibilidade de operação principal.
69. Defeito Alto

Exemplos:

falha de funcionalidade essencial;
cálculo incorreto;
inconsistência financeira;
perda de rastreabilidade;
falha de integração crítica.
70. Defeito Médio

Afeta funcionalidade relevante sem impedir completamente o processo.

71. Defeito Baixo

Problemas menores:

apresentação;
textos;
pequenos comportamentos;
questões cosméticas.
72. Ciclo de Defeitos
Identificado
     ↓
Registrado
     ↓
Classificado
     ↓
Priorizado
     ↓
Corrigido
     ↓
Retestado
     ↓
Aprovado
     ↓
Encerrado
73. Evidências de Teste

As evidências poderão incluir:

screenshots;
logs;
respostas de API;
relatórios;
registros de banco;
vídeos;
documentos;
resultados automatizados.
74. Identificação da Execução

Cada execução deverá possuir identificação.

Exemplo:

TEST-2026-0001
75. Registro de Caso de Teste

Modelo:

Código:
Objetivo:
Pré-condições:
Dados:
Passos:
Resultado Esperado:
Resultado Obtido:
Status:
Evidência:
Defeito:
Responsável:
Data:
76. Matriz Requisito × Teste
Requisito	Caso de Teste	Tipo
RF	CT	Funcional
RNF	CT	Não funcional
RN	CT	Regra de negócio
Segurança	CT	Segurança
Integração	CT	Integração
Auditoria	CT	Auditoria

A matriz detalhada deverá ser mantida no documento específico de rastreabilidade de testes quando este for criado.

77. Cobertura

A cobertura deverá ser acompanhada por:

requisito;
funcionalidade;
regra;
serviço;
API;
integração;
risco.
78. Cobertura de Requisitos

Meta recomendada:

100% dos requisitos críticos
100% das regras críticas
100% dos critérios de aceitação críticos

Os demais percentuais deverão ser definidos conforme criticidade.

79. Cobertura de Código

Quando houver testes automatizados, deverá ser acompanhada a cobertura de código.

A cobertura não deverá ser considerada isoladamente como indicador de qualidade.

80. Cobertura de Segurança

Deverão ser cobertos:

autenticação;
autorização;
permissões;
segregação;
APIs;
dados;
auditoria;
sessões.
81. Cobertura de Auditoria

As operações classificadas como críticas deverão possuir testes que comprovem a geração da trilha de auditoria.

82. Cobertura de Integração

Integrações críticas deverão possuir pelo menos:

cenário de sucesso;
cenário de erro;
timeout;
indisponibilidade;
retry;
comportamento após recuperação.
83. Testes de Aceitação

Os testes de aceitação deverão validar se o sistema atende à necessidade do usuário.

Deverão utilizar os critérios definidos em:

011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
84. Homologação

A homologação deverá envolver representantes das áreas responsáveis pelo processo.

Poderão participar:

área requisitante;
compras;
contratos;
fiscalização;
administração;
tecnologia;
controle interno.
85. Critério de Homologação

A funcionalidade será considerada homologada quando:

critérios de aceitação forem atendidos;
testes críticos forem aprovados;
defeitos impeditivos forem resolvidos;
riscos residuais forem conhecidos;
responsável pelo negócio aprovar.
86. Testes de Rejeição

Deverão ser testadas situações em que o sistema deve impedir operações.

Exemplos:

Dados inválidos
Usuário não autorizado
Estado incompatível
Regra violada
Documento obrigatório ausente
87. Testes de Concorrência

Deverão ser avaliados cenários em que múltiplos usuários alteram recursos simultaneamente.

Exemplo:

Usuário A → altera contrato
Usuário B → altera contrato
          ↓
Controle de concorrência
88. Testes de Transação

Operações que envolvam múltiplas alterações deverão ser testadas para garantir consistência.

Em caso de falha:

Operação
   ↓
Etapa 1 ✓
Etapa 2 ✓
Etapa 3 ✗
   ↓
Rollback / Compensação
89. Testes de Consistência

Deverão ser verificadas situações como:

contrato sem processo;
medição sem contrato;
fornecedor inexistente;
documento órfão;
pagamento sem referência;
item inconsistente.

As regras efetivamente aplicáveis deverão ser determinadas pelo modelo de dados e regras de negócio.

90. Testes de Workflow

Os estados das entidades deverão ser testados.

Exemplo:

RASCUNHO
   ↓
EM_ANALISE
   ↓
APROVADO
   ↓
EM_EXECUCAO
   ↓
ENCERRADO

Transições inválidas deverão ser rejeitadas.

91. Testes de Máquina de Estados

Para cada entidade relevante deverá ser validado:

estado inicial;
estados possíveis;
transições válidas;
transições inválidas;
permissões;
eventos gerados.
92. Testes de Notificação

Eventos que exigem comunicação deverão gerar a notificação correspondente.

Exemplo:

Contrato próximo do vencimento
        ↓
Evento
        ↓
Notificação
        ↓
Destinatário
93. Testes de Performance de Relatórios

Relatórios complexos deverão ser testados com volumes representativos.

Deverão ser avaliados:

tempo de consulta;
consumo de memória;
banco de dados;
concorrência.
94. Testes de Volume

Deverão ser utilizados dados suficientes para simular cenários reais.

Exemplos:

10 processos
1.000 processos
10.000 processos
100.000 registros

Os volumes definitivos deverão ser definidos conforme capacidade esperada do município e arquitetura corporativa.

95. Testes de Escalabilidade

Quando aplicável, deverá ser avaliado o comportamento com aumento de:

usuários;
processos;
contratos;
documentos;
integrações;
eventos.
96. Testes de Backup e Restauração

Deverão ser validados:

backup;
restauração;
integridade;
tempo de recuperação;
perda aceitável de dados;
funcionamento após restauração.
97. Testes de Recuperação de Desastre

Quando aplicável, deverão validar os procedimentos definidos no plano corporativo de continuidade.

98. Testes de Segurança Automatizados

Quando tecnicamente viável, deverão ser utilizados:

análise estática;
análise de dependências;
testes de API;
testes de vulnerabilidades;
verificação de configuração.
99. Testes de Regressão Automatizada

A cada alteração relevante, a suíte automatizada deverá ser executada.

O conjunto deverá evoluir junto com o domínio.

100. Pipeline de Qualidade

Quando houver CI/CD, recomenda-se:

Commit
 ↓
Lint
 ↓
Testes Unitários
 ↓
Análise Estática
 ↓
Build
 ↓
Testes de Integração
 ↓
Testes de Segurança
 ↓
Testes de API
 ↓
Deploy de Teste
 ↓
Testes de Sistema
101. Quality Gate

Uma versão não deverá avançar quando houver:

teste crítico falhando;
vulnerabilidade crítica;
defeito impeditivo;
erro de build;
cobertura mínima não atingida;
requisito crítico sem evidência.
102. Testes em Pull Request

Alterações de código deverão, quando aplicável, executar automaticamente:

lint;
testes unitários;
testes de componentes;
análise estática;
testes de segurança básicos.
103. Testes antes da Implantação

Antes da implantação deverão ser executados:

regressão;
integração;
segurança;
performance necessária;
aceitação;
smoke test.
104. Smoke Test

Após implantação deverá ser validado o funcionamento básico.

Exemplo:

Login
 ↓
Acesso ao domínio
 ↓
Criar registro
 ↓
Consultar registro
 ↓
Alterar registro
 ↓
Auditoria
105. Testes Pós-Implantação

Após implantação deverão ser verificados:

disponibilidade;
erros;
integrações;
logs;
métricas;
notificações;
auditoria;
funcionalidades críticas.
106. Plano de Rollback

Quando houver risco relevante, a implantação deverá possuir procedimento de rollback.

Nova versão
    ↓
Problema
    ↓
Avaliação
    ↓
Rollback
    ↓
Validação
107. Responsabilidades
107.1 Equipe de Desenvolvimento

Responsável por:

testes unitários;
testes de componentes;
correção de defeitos;
suporte aos testes de integração.
107.2 QA/Testes

Responsável por:

estratégia;
casos de teste;
execução;
evidências;
defeitos;
regressão;
relatórios.
107.3 Área de Negócio

Responsável por:

validação funcional;
critérios de aceitação;
homologação.
107.4 Segurança

Responsável por:

testes de segurança;
vulnerabilidades;
controles de acesso;
validação de proteção.
107.5 Arquitetura

Responsável por:

estratégia técnica;
integração;
performance;
qualidade arquitetural.
108. Ferramentas

As ferramentas deverão ser escolhidas conforme a arquitetura tecnológica do SIGMUN.

Categorias:

Testes Unitários
Testes de API
Testes E2E
Testes de Performance
Testes de Segurança
CI/CD
Cobertura
Relatórios

A ferramenta específica deverá ser definida nos artefatos técnicos de implementação.

109. Ambiente Tecnológico

O ambiente de desenvolvimento atual considera:

Sistema Operacional:
Ubuntu Jammy


Editor:
VSCodium

O ambiente de desenvolvimento deverá permanecer separado dos ambientes de teste e homologação.

110. Gestão de Evidências

As evidências deverão ser armazenadas de forma organizada.

Sugestão:

10-Testes/
├── casos/
├── evidencias/
├── resultados/
├── defeitos/
└── relatorios/

A estrutura definitiva deverá seguir a hierarquia documental do SIGMUN.

111. Relatório de Execução

Cada ciclo deverá gerar relatório contendo:

versão testada;
ambiente;
período;
testes planejados;
testes executados;
aprovados;
reprovados;
bloqueados;
defeitos;
riscos;
conclusão.
112. Indicadores

Indicadores recomendados:

Indicador	Objetivo
Taxa de aprovação	Medir qualidade
Taxa de reprovação	Identificar problemas
Cobertura de requisitos	Medir rastreabilidade
Cobertura automatizada	Medir automação
Defeitos críticos	Medir risco
Defeitos por versão	Medir estabilidade
Tempo médio de correção	Medir eficiência
Taxa de regressão	Medir qualidade das correções
Cobertura de segurança	Medir proteção
Cobertura de auditoria	Medir rastreabilidade
113. Critérios de Aceitação do Plano

O plano será considerado adequado quando:

níveis de testes estiverem definidos;
tipos de testes estiverem definidos;
responsabilidades estiverem definidas;
ambientes estiverem definidos;
dados de teste estiverem definidos;
critérios de entrada estiverem definidos;
critérios de saída estiverem definidos;
defeitos possuírem classificação;
evidências forem previstas;
requisitos forem rastreáveis;
segurança estiver contemplada;
auditoria estiver contemplada;
integração estiver contemplada;
performance estiver contemplada;
regressão estiver contemplada;
homologação estiver contemplada.
114. Rastreabilidade

A cadeia deverá ser:

Requisito
   ↓
Regra de Negócio
   ↓
Critério de Aceitação
   ↓
Caso de Teste
   ↓
Execução
   ↓
Evidência
   ↓
Defeito, quando houver
   ↓
Correção
   ↓
Reteste
115. Artefatos de Teste

O domínio deverá produzir, quando aplicável:

Plano de Testes
Casos de Teste
Cenários de Teste
Dados de Teste
Scripts Automatizados
Evidências
Registro de Defeitos
Relatórios
Relatório de Homologação
Relatório de Regressão
116. Próximos Artefatos

Recomenda-se a criação dos seguintes documentos:

019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
020-Cenarios-de-Teste-Gestao-de-Compras-e-Contratacoes.md
021-Dados-de-Teste-Gestao-de-Compras-e-Contratacoes.md
022-Matriz-de-Cobertura-de-Testes-Gestao-de-Compras-e-Contratacoes.md
023-Plano-de-Homologacao-Gestao-de-Compras-e-Contratacoes.md
024-Relatorio-de-Testes-Gestao-de-Compras-e-Contratacoes.md
117. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Plano de Testes do Domínio de Gestão de Compras e Contratações

Documento: 018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente
