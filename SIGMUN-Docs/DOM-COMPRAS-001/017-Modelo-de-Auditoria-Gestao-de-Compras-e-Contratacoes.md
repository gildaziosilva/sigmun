#### Modelo de Auditoria – Gestão de Compras e Contratações


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
- 015-Plano-de-Auditoria.md
- 021-Governanca-de-Dados.md
- 025-Politica-de-Protecao-de-Dados-Pessoais.md


---


# 1. Finalidade


Este documento define o **Modelo de Auditoria do Domínio de Gestão de Compras e Contratações do SIGMUN**.


O modelo estabelece os princípios, mecanismos, eventos, registros, controles e responsabilidades necessários para garantir a rastreabilidade das operações realizadas no domínio.


A auditoria deverá permitir reconstruir, quando necessário:


```text
Quem
 ↓
Fez o quê
 ↓
Quando
 ↓
Onde
 ↓
Sobre qual recurso
 ↓
Qual era o estado anterior
 ↓
Qual foi o novo estado
 ↓
Qual foi o resultado
2. Objetivos

São objetivos deste modelo:

garantir rastreabilidade;
registrar operações relevantes;
preservar evidências;
apoiar controles internos;
apoiar auditorias administrativas;
apoiar auditorias de segurança;
detectar operações indevidas;
permitir investigação de incidentes;
apoiar prestação de contas;
aumentar a transparência;
apoiar conformidade;
preservar histórico dos processos;
permitir reconstrução da linha do tempo dos eventos.
3. Princípios de Auditoria
3.1 Rastreabilidade

Toda operação relevante deverá ser rastreável até o usuário, serviço ou sistema responsável.

3.2 Integridade

Os registros de auditoria deverão ser protegidos contra alterações indevidas.

3.3 Imutabilidade

Sempre que tecnicamente possível, os registros deverão ser armazenados de forma que alterações posteriores sejam impedidas ou detectáveis.

3.4 Responsabilização

As operações deverão permitir identificar o responsável pela sua execução.

3.5 Segregação

Os mecanismos de auditoria deverão possuir controles independentes dos mecanismos de operação do processo.

3.6 Evidência

Os registros deverão possuir informações suficientes para demonstrar a ocorrência da operação.

3.7 Necessidade

A auditoria deverá registrar as informações necessárias para rastreabilidade sem armazenar dados pessoais ou informações desnecessárias.

3.8 Transparência

As informações de auditoria deverão ser disponibilizadas conforme sua classificação e as políticas corporativas.

4. Escopo

O modelo abrange auditoria de:

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
medições;
fiscalização;
ocorrências;
alterações;
encerramentos;
integrações;
usuários;
permissões;
acessos.
5. Modelo Conceitual

A auditoria deverá seguir o modelo:

Evento de Negócio
       ↓
Evento de Auditoria
       ↓
Registro
       ↓
Armazenamento Protegido
       ↓
Consulta
       ↓
Análise
       ↓
Evidência
6. Evento de Auditoria

Um evento de auditoria representa uma operação relevante realizada no sistema.

Exemplo:

ContratoAlterado

O evento deverá identificar:

origem;
usuário;
recurso;
operação;
data/hora;
resultado.
7. Categorias de Eventos

Os eventos poderão ser classificados em:

AUTENTICACAO
AUTORIZACAO
ACESSO
CRIACAO
ALTERACAO
EXCLUSAO
APROVACAO
REJEICAO
CANCELAMENTO
ASSINATURA
PUBLICACAO
EXECUCAO
INTEGRACAO
EXPORTACAO
IMPORTACAO
SEGURANCA
ADMINISTRACAO
8. Eventos de Autenticação

Deverão ser registrados eventos como:

login realizado;
login recusado;
logout;
sessão expirada;
autenticação multifator;
falha de segundo fator;
bloqueio de usuário.
9. Eventos de Autorização

Deverão ser auditados:

acesso autorizado;
acesso negado;
alteração de perfil;
concessão de permissão;
revogação de permissão;
tentativa de operação sem autorização.
10. Eventos de Cadastro

Deverão ser registrados:

criação;
alteração;
inativação;
reativação;
exclusão lógica.
11. Eventos de Processo

Exemplos:

ProcessoCriado
ProcessoAlterado
ProcessoEnviado
ProcessoAprovado
ProcessoRejeitado
ProcessoCancelado
ProcessoEncerrado
12. Eventos de Demanda

Exemplos:

DemandaCriada
DemandaAlterada
DemandaEnviada
DemandaAprovada
DemandaRejeitada
DemandaCancelada
13. Eventos de Planejamento

Exemplos:

PlanejamentoCriado
PlanejamentoAlterado
PlanejamentoAprovado
PlanejamentoRejeitado
14. Eventos de Procedimento

Exemplos:

ProcedimentoCriado
ProcedimentoAlterado
ProcedimentoPublicado
ProcedimentoCancelado
ProcedimentoEncerrado
15. Eventos de Fornecedor

Exemplos:

FornecedorConsultado
FornecedorVinculado
FornecedorDesvinculado
FornecedorAtualizado

Quando o cadastro for de responsabilidade de outro domínio, a auditoria deverá respeitar a propriedade do dado.

16. Eventos de Proposta

Exemplos:

PropostaRecebida
PropostaAtualizada
PropostaClassificada
PropostaDesclassificada
PropostaAceita
PropostaRejeitada
17. Eventos de Resultado

Exemplos:

ResultadoRegistrado
ResultadoHomologado
ResultadoAnulado
ResultadoPublicado
18. Eventos de Contrato

Os contratos deverão possuir auditoria reforçada.

Exemplos:

ContratoCriado
ContratoAlterado
ContratoAprovado
ContratoAssinado
ContratoPublicado
ContratoSuspenso
ContratoRetomado
ContratoProrrogado
ContratoReajustado
ContratoAlterado
ContratoEncerrado
ContratoCancelado
19. Eventos de Execução Contratual

Exemplos:

ExecucaoIniciada
EntregaRegistrada
RecebimentoRegistrado
MedicaoCriada
MedicaoAprovada
MedicaoRejeitada
OcorrenciaRegistrada
FiscalizacaoRegistrada
20. Eventos de Alteração Contratual

Alterações contratuais deverão possuir rastreabilidade completa.

Deverão ser registrados:

usuário;
data/hora;
justificativa;
campo alterado;
valor anterior;
valor novo;
documento associado;
aprovação.
21. Eventos de Documentos

Exemplos:

DocumentoCriado
DocumentoAnexado
DocumentoVisualizado
DocumentoAtualizado
DocumentoVersionado
DocumentoAssinado
DocumentoPublicado
DocumentoArquivado

A visualização deverá ser auditada quando o nível de proteção do documento exigir.

22. Eventos de Assinatura

Deverão ser registrados:

solicitação;
envio;
assinatura;
recusa;
cancelamento;
conclusão.
23. Eventos de Publicação

Exemplos:

PublicacaoSolicitada
PublicacaoValidada
PublicacaoRealizada
PublicacaoAtualizada
PublicacaoRetirada
24. Eventos de Integração

Deverão ser registrados:

requisição;
resposta;
sucesso;
falha;
timeout;
retry;
rejeição;
mensagem enviada;
mensagem recebida.
25. Eventos de Exportação

Exportações deverão possuir rastreabilidade.

Exemplo:

ExportacaoSolicitada
ExportacaoProcessada
ExportacaoConcluida
ExportacaoFalhou

Quando aplicável, deverão ser registrados:

usuário;
finalidade;
filtros;
quantidade de registros;
formato;
horário.
26. Estrutura do Registro de Auditoria

Modelo conceitual:

{
  "auditId": "uuid",
  "timestamp": "2026-08-13T20:00:00Z",
  "eventType": "ContratoAlterado",
  "category": "ALTERACAO",
  "actor": {
    "userId": "uuid",
    "profile": "Gestor de Contratos"
  },
  "source": {
    "service": "gestao-compras",
    "operation": "alterarContrato"
  },
  "resource": {
    "type": "Contrato",
    "id": "uuid"
  },
  "result": "SUCCESS",
  "correlationId": "uuid",
  "reason": "Justificativa da alteração"
}
27. Identificação do Usuário

Quando a operação for executada por usuário, deverão ser registrados:

identificador do usuário;
perfil;
unidade administrativa, quando aplicável;
sessão;
origem da operação.
28. Operações Automatizadas

Quando uma operação for executada automaticamente, deverá ser identificada a identidade técnica responsável.

Exemplo:

actorType: SERVICE
actorId: servico-notificacoes

Não deverá ser utilizada identidade humana para representar operações automáticas.

29. Integrações Externas

Operações provenientes de sistemas externos deverão identificar:

sistema de origem;
integração;
credencial ou identidade técnica;
operação;
correlation_id;
resultado.
30. Data e Hora

Os registros deverão utilizar padrão temporal consistente.

Recomenda-se:

UTC

A apresentação ao usuário poderá utilizar o fuso horário configurado para o Município.

31. Correlation ID

Toda operação relevante deverá possuir identificador de correlação.

Exemplo:

correlation_id

Isso permitirá reconstruir operações distribuídas entre:

API
 ↓
Serviço
 ↓
Integração
 ↓
Sistema Externo
32. Identificador de Negócio

Além do identificador técnico, o registro deverá permitir localizar a entidade de negócio.

Exemplo:

entityId = UUID
businessKey = número do processo
33. Estado Anterior e Posterior

Para operações críticas, recomenda-se registrar:

before
after

Exemplo:

{
  "field": "vigencia",
  "before": "2026-12-31",
  "after": "2027-12-31"
}

Dados pessoais desnecessários não deverão ser replicados na trilha de auditoria.

34. Justificativa

Operações críticas poderão exigir justificativa.

Exemplos:

cancelamento;
rejeição;
alteração;
exclusão;
suspensão;
prorrogação;
alteração de valor.
35. Auditoria de Alterações

Alterações deverão permitir identificar:

Campo
Valor anterior
Valor posterior
Usuário
Data/hora
Motivo
36. Auditoria de Exclusões

Sempre que possível, o domínio deverá utilizar exclusão lógica para entidades que necessitem de histórico.

Exemplo:

ATIVO
   ↓
INATIVO

A exclusão física deverá ser restrita a situações autorizadas.

37. Imutabilidade

Os registros de auditoria deverão ser protegidos contra:

alteração;
exclusão;
sobrescrita;
acesso não autorizado.
38. Proteção dos Logs

Os logs e registros de auditoria deverão possuir controles de:

acesso;
retenção;
integridade;
backup;
monitoramento.
39. Separação entre Dados Operacionais e Auditoria

Sempre que possível, os registros de auditoria deverão possuir armazenamento separado ou logicamente protegido dos dados transacionais.

Objetivo:

Operação
   ↓
Dados Operacionais


Operação
   ↓
Trilha de Auditoria

A alteração dos dados operacionais não deverá permitir alterar retroativamente a trilha de auditoria.

40. Controle de Acesso à Auditoria

O acesso aos registros de auditoria deverá ser restrito.

Perfis possíveis:

Auditor
Controladoria
Administrador de Segurança
Gestor Autorizado
Administrador Técnico

O acesso deverá ser concedido conforme necessidade.

41. Auditoria da Própria Auditoria

O acesso aos registros de auditoria também deverá ser auditado.

Exemplo:

Auditor consultou registro
       ↓
Evento de auditoria
       ↓
Registro protegido
42. Consulta de Auditoria

A consulta deverá permitir filtros por:

período;
usuário;
evento;
recurso;
processo;
contrato;
secretaria;
resultado;
sistema;
integração;
correlation_id.
43. Linha do Tempo

O sistema deverá permitir reconstruir a linha do tempo de entidades relevantes.

Exemplo:

13/08 08:00  Processo criado
13/08 09:15  Processo enviado
13/08 10:30  Processo aprovado
14/08 14:00  Contrato criado
15/08 11:00  Contrato assinado
16/08 08:00  Contrato publicado
44. Auditoria de Contratos

Para cada contrato deverá ser possível reconstruir:

Origem
 ↓
Processo
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
Medições
 ↓
Alterações
 ↓
Encerramento
45. Auditoria de Fornecedores

Deverão ser rastreáveis as operações de:

vinculação;
consulta;
atualização;
participação;
proposta;
contratação;
execução.
46. Auditoria de Permissões

Deverão ser registrados:

concessão;
alteração;
revogação;
mudança de perfil;
acesso privilegiado.
47. Auditoria de Acesso

Deverão ser considerados:

acesso autorizado;
acesso negado;
tentativas repetidas;
acesso privilegiado;
acesso fora de padrão.
48. Auditoria de Segurança

Eventos de segurança deverão ser integrados ao modelo corporativo de segurança.

Exemplos:

TentativaDeAcessoNegada
CredencialBloqueada
PermissaoAlterada
SessaoEncerrada
OperacaoSuspeita
49. Retenção

A retenção dos registros deverá observar:

legislação aplicável;
políticas corporativas;
requisitos de auditoria;
necessidades administrativas;
requisitos de segurança.

O prazo definitivo deverá ser definido pela Governança Documental e pelas normas aplicáveis.

50. Descarte

O descarte deverá ser:

autorizado;
rastreável;
seguro;
compatível com a política de retenção.

Não deverá ocorrer descarte quando houver obrigação de preservação da evidência.

51. Preservação de Evidências

Quando um evento estiver relacionado a investigação, auditoria ou incidente, os registros deverão ser preservados.

O processo poderá envolver:

Identificação
 ↓
Preservação
 ↓
Cópia controlada
 ↓
Análise
 ↓
Conclusão
52. Integridade dos Registros

Poderão ser utilizados mecanismos como:

hash;
assinatura digital;
armazenamento imutável;
cadeia de hashes;
controle de versão;
mecanismos equivalentes.

A tecnologia adotada deverá ser definida pela arquitetura corporativa.

53. Sincronização Temporal

Sistemas integrantes deverão manter sincronização temporal adequada.

A divergência significativa de horário deverá ser identificável.

54. Monitoramento

Deverão ser monitorados:

volume de eventos;
falhas de gravação;
ausência de registros;
acesso aos logs;
tentativas de alteração;
crescimento de armazenamento.
55. Disponibilidade

A trilha de auditoria deverá possuir disponibilidade compatível com sua importância.

Falhas na gravação de eventos críticos deverão ser tratadas como eventos relevantes.

56. Auditoria Offline

Em aplicações Offline First, eventos deverão ser registrados localmente até a sincronização.

Fluxo:

Operação Offline
      ↓
Registro Local
      ↓
Sincronização
      ↓
Servidor
      ↓
Auditoria Corporativa

Deverão ser preservados:

horário da operação;
dispositivo;
usuário;
identificador do evento;
sincronização;
conflitos.
57. Auditoria de Dispositivos

Quando aplicável, poderão ser registrados:

dispositivo;
aplicação;
versão;
sistema operacional;
identificador técnico.

Não deverão ser armazenados dados desnecessários de localização ou do dispositivo.

58. Indicadores de Auditoria

Indicadores recomendados:

Indicador	Objetivo
Eventos registrados	Volume de auditoria
Falhas de registro	Identificar problemas
Acessos negados	Avaliar tentativas indevidas
Alterações críticas	Monitorar mudanças
Operações privilegiadas	Monitorar privilégios
Eventos suspeitos	Apoiar segurança
Tempo de retenção	Controle documental
Consultas de auditoria	Avaliar utilização
59. Indicadores de Conformidade

Poderão ser utilizados:

% de operações críticas auditadas
% de usuários revisados
% de permissões revisadas
% de contratos com trilha completa
% de eventos críticos preservados
% de incidentes rastreáveis
60. Relatórios de Auditoria

O domínio poderá disponibilizar relatórios como:

histórico do processo;
histórico do contrato;
histórico do fornecedor;
histórico de alterações;
histórico de aprovações;
histórico de acessos;
histórico de permissões;
histórico de integrações.
61. Evidências

Uma evidência poderá ser composta por:

Registro de Auditoria
+
Documento
+
Assinatura
+
Evento
+
Identificação do Usuário
+
Timestamp
62. Não Repúdio

Operações críticas deverão possuir mecanismos suficientes para demonstrar:

autoria;
integridade;
ocorrência;
momento da operação.

Quando necessário, deverão ser utilizados mecanismos de assinatura eletrônica ou digital.

63. Auditoria e Transparência

A trilha interna de auditoria não deverá ser automaticamente publicada.

A publicação deverá considerar:

classificação;
proteção de dados;
segurança;
requisitos legais;
transparência pública.
64. Auditoria e LGPD

O modelo deverá observar os princípios de proteção de dados pessoais.

A auditoria não deverá utilizar a finalidade de rastreabilidade como justificativa para armazenar dados pessoais desnecessários.

Quando possível:

minimizar;
pseudonimizar;
controlar;
restringir;
proteger.
65. Auditoria e Governança

Os registros deverão apoiar:

Governança de Dados;
Governança de Segurança;
Governança de Arquitetura;
Governança Corporativa;
Gestão de Riscos;
Gestão de Conformidade;
Auditoria Interna.
66. Responsabilidades
66.1 Equipe do Domínio

Responsável por:

implementar eventos;
garantir cobertura;
corrigir falhas;
manter contratos;
validar registros.
66.2 Segurança da Informação

Responsável por:

definir controles;
monitorar eventos de segurança;
investigar incidentes;
proteger registros.
66.3 Auditoria

Responsável por:

analisar evidências;
realizar consultas;
produzir relatórios;
identificar desvios;
recomendar melhorias.
66.4 Gestores

Responsáveis por:

analisar ocorrências;
validar responsabilidades;
responder a auditorias;
implementar correções.
67. Matriz de Eventos Auditáveis
Área	Evento	Criticidade
Acesso	Login	Média
Acesso	Login recusado	Alta
Segurança	Alteração de permissão	Alta
Demanda	Criação	Média
Demanda	Aprovação	Alta
Processo	Criação	Média
Processo	Aprovação	Alta
Processo	Cancelamento	Alta
Contrato	Criação	Alta
Contrato	Alteração	Alta
Contrato	Assinatura	Crítica
Contrato	Suspensão	Alta
Contrato	Encerramento	Alta
Execução	Medição	Alta
Execução	Fiscalização	Alta
Documento	Assinatura	Crítica
Publicação	Publicação	Alta
Integração	Falha	Média
Exportação	Exportação de dados	Alta
68. Níveis de Criticidade
Baixa
Média
Alta
Crítica

Operações críticas deverão receber controles de auditoria reforçados.

69. Auditoria de Operações Críticas

Operações críticas poderão exigir:

registro detalhado;
justificativa;
usuário;
perfil;
IP;
dispositivo;
timestamp;
estado anterior;
estado posterior;
documento associado;
assinatura;
correlation_id.
70. Matriz Risco × Auditoria
Risco	Controle de Auditoria
Alteração indevida	Histórico de alterações
Fraude	Segregação + auditoria
Acesso indevido	Logs de acesso
Vazamento	Auditoria de consultas/exportações
Manipulação de contrato	Histórico completo
Exclusão indevida	Exclusão lógica + auditoria
Alteração de permissões	Auditoria administrativa
Falha de integração	Logs de integração
Não conformidade	Relatórios de auditoria
Perda de evidência	Retenção + armazenamento protegido
71. Rastreabilidade

A cadeia de rastreabilidade deverá ser:

Ator
 ↓
Ação
 ↓
Processo
 ↓
Serviço
 ↓
Entidade
 ↓
Evento
 ↓
Registro de Auditoria
 ↓
Evidência
72. Integração com Segurança

O Modelo de Auditoria deverá complementar o:

016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md

A segurança deverá identificar e proteger os eventos, enquanto a auditoria deverá preservar sua rastreabilidade.

73. Integração com Modelo de Dados

Os eventos de auditoria deverão possuir relacionamento com as entidades definidas no:

013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md
74. Integração com Serviços

Os serviços definidos no:

015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md

deverão produzir eventos de auditoria conforme sua criticidade.

75. Integração

Os eventos provenientes de integrações deverão utilizar o modelo definido no:

014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md

Especialmente:

correlation_id;
identificadores;
origem;
destino;
resultado;
erro.
76. Critérios de Aceitação

O modelo será considerado implementado quando:

os principais eventos do domínio estiverem identificados;
operações críticas forem auditáveis;
usuários puderem ser identificados;
operações automatizadas puderem ser identificadas;
alterações relevantes possuírem histórico;
eventos de segurança estiverem registrados;
integrações puderem ser rastreadas;
documentos críticos possuírem rastreabilidade;
contratos possuírem linha do tempo;
registros possuírem proteção contra alteração indevida;
acessos aos registros forem controlados;
retenção estiver definida;
descarte estiver controlado;
indicadores puderem ser calculados;
evidências puderem ser preservadas.
77. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Modelo de Auditoria do Domínio de Gestão de Compras e Contratações

Documento: 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente
