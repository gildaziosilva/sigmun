#### Modelo de Segurança – Gestão de Compras e Contratações

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
- 021-Politica-de-Seguranca.md
- 025-Politica-de-Protecao-de-Dados-Pessoais.md

---

# 1. Finalidade

Este documento define o **Modelo de Segurança do Domínio de Gestão de Compras e Contratações do SIGMUN**.

O modelo estabelece os princípios, controles, responsabilidades e mecanismos necessários para proteger informações, processos, serviços, documentos, operações e integrações relacionados ao domínio.

O modelo deverá garantir, de forma integrada:

- confidencialidade;
- integridade;
- disponibilidade;
- autenticidade;
- rastreabilidade;
- responsabilização;
- proteção de dados pessoais;
- segregação de funções;
- prevenção de alterações indevidas;
- identificação de acessos e operações.

---

# 2. Objetivos

São objetivos deste modelo:

1. proteger os dados do domínio;
2. proteger os serviços e APIs;
3. controlar o acesso às funcionalidades;
4. impedir operações não autorizadas;
5. preservar a integridade dos processos;
6. garantir rastreabilidade das operações;
7. aplicar segregação de funções;
8. proteger dados pessoais;
9. proteger documentos e evidências;
10. reduzir riscos de fraude, erro e abuso;
11. permitir auditoria;
12. apoiar conformidade com as políticas corporativas do SIGMUN;
13. permitir integração segura com outros domínios e sistemas externos.

---

# 3. Princípios de Segurança

## 3.1 Segurança por Princípio

A segurança deverá ser considerada desde a definição do processo, requisito, serviço, modelo de dados e interface.

---

## 3.2 Privilégio Mínimo

Cada usuário deverá possuir somente as permissões necessárias para executar suas responsabilidades.

---

## 3.3 Necessidade de Saber

O acesso a informações deverá considerar a necessidade efetiva de utilização.

---

## 3.4 Segregação de Funções

Operações incompatíveis deverão ser separadas entre diferentes responsabilidades.

Exemplo:

```text
Solicitar
   ≠
Autorizar
   ≠
Executar
   ≠
Fiscalizar
   ≠
Liquidar
   ≠
Pagar

3.5 Defesa em Profundidade

A proteção deverá ocorrer em múltiplas camadas:

Identidade
   ↓
Autenticação
   ↓
Autorização
   ↓
Aplicação
   ↓
Serviço
   ↓
Dados
   ↓
Auditoria
3.6 Rastreabilidade

Toda operação relevante deverá permitir identificar:

quem executou;
quando executou;
qual operação executou;
sobre qual recurso;
qual foi o resultado;
origem da operação.
3.7 Transparência por Padrão

Informações classificadas como públicas deverão ser disponibilizadas de acordo com as políticas de transparência do SIGMUN.

3.8 Restrição Quando Necessária

Informações que necessitem de proteção deverão possuir controles de acesso compatíveis com sua classificação.

4. Escopo

Este modelo abrange:

usuários;
perfis;
permissões;
processos;
serviços;
APIs;
dados;
documentos;
fornecedores;
contratos;
propostas;
medições;
fiscalizações;
integrações;
eventos;
auditoria;
registros de acesso.
5. Classificação da Informação

As informações do domínio deverão utilizar a classificação corporativa do SIGMUN.

Categorias possíveis:

Pública
Interna
Restrita
Confidencial

A classificação efetiva deverá ser determinada conforme a Política de Classificação da Informação do SIGMUN.

6. Segurança dos Dados

Os dados deverão ser protegidos durante:

armazenamento;
processamento;
transmissão;
integração;
exportação;
visualização;
descarte.
7. Dados Pessoais

O domínio poderá tratar dados pessoais relacionados a:

servidores;
fornecedores;
representantes;
fiscais;
gestores;
usuários;
contatos;
participantes de procedimentos.

O tratamento deverá observar:

finalidade;
necessidade;
adequação;
segurança;
controle de acesso;
rastreabilidade;
retenção;
descarte.
8. Dados Sensíveis

Caso o domínio venha a processar dados pessoais sensíveis, deverá ser realizada avaliação específica de segurança e privacidade.

O tratamento não deverá ocorrer sem justificativa legal e controles adequados.

9. Autenticação

A autenticação deverá utilizar a infraestrutura corporativa de identidade do SIGMUN.

O domínio não deverá manter mecanismos independentes de autenticação sem justificativa arquitetural.

10. Autenticação Multifator

A autenticação multifator deverá ser adotada para operações e perfis considerados de maior risco, conforme política corporativa.

Exemplos:

administradores;
gestores;
operadores de funções críticas;
acesso privilegiado;
operações administrativas sensíveis.
11. Autorização

A autorização deverá ser baseada nas responsabilidades do usuário.

Modelo conceitual:

Usuário
   ↓
Identidade
   ↓
Perfil
   ↓
Função
   ↓
Permissão
   ↓
Recurso
   ↓
Operação
12. Modelo de Controle de Acesso

O SIGMUN poderá utilizar combinação de:

RBAC;
ABAC;
regras contextuais;
segregação de funções.
RBAC

Controle baseado em papéis.

Exemplo:

Perfil: Gestor de Compras
ABAC

Controle baseado em atributos.

Exemplo:

Usuário
+
Secretaria
+
Unidade
+
Processo
+
Operação
13. Perfis de Acesso

Perfis conceituais:

Código	Perfil
PERF-COMPRAS-001	Solicitante
PERF-COMPRAS-002	Analista de Compras
PERF-COMPRAS-003	Gestor de Compras
PERF-COMPRAS-004	Autoridade Competente
PERF-COMPRAS-005	Agente Responsável
PERF-COMPRAS-006	Fiscal de Contrato
PERF-COMPRAS-007	Gestor de Contrato
PERF-COMPRAS-008	Auditor
PERF-COMPRAS-009	Consulta
PERF-COMPRAS-010	Administrador Técnico

Os perfis definitivos deverão ser definidos pela Governança de Segurança e pelos responsáveis pelo domínio.

14. Permissões

As permissões deverão ser granulares.

Exemplos:

COMPRAS.DEMANDA.CRIAR
COMPRAS.DEMANDA.CONSULTAR
COMPRAS.DEMANDA.APROVAR


COMPRAS.PROCESSO.CRIAR
COMPRAS.PROCESSO.CONSULTAR
COMPRAS.PROCESSO.EDITAR
COMPRAS.PROCESSO.ENCERRAR


COMPRAS.CONTRATO.CRIAR
COMPRAS.CONTRATO.CONSULTAR
COMPRAS.CONTRATO.EDITAR
COMPRAS.CONTRATO.ASSINAR
COMPRAS.CONTRATO.ENCERRAR
15. Segregação de Funções

O sistema deverá impedir ou sinalizar combinações de funções incompatíveis.

Exemplo:

Solicitante
   ↓
não deve aprovar sua própria solicitação

Outro exemplo:

Fiscal
   ↓
não deve aprovar sozinho operação que ele próprio fiscalizou

As regras definitivas deverão ser estabelecidas conforme legislação e políticas municipais.

16. Controle de Acesso por Unidade Administrativa

Quando aplicável, o acesso deverá considerar a unidade administrativa.

Exemplo:

Usuário
   ↓
Secretaria
   ↓
Unidade
   ↓
Processos autorizados

Isso permite restringir o acesso aos processos pertencentes à unidade de responsabilidade do usuário.

17. Controle por Processo

Operações poderão ser condicionadas ao estado do processo.

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

Um usuário não deverá executar operações incompatíveis com o estado atual.

18. Controle por Estado do Contrato

Exemplo:

RASCUNHO
   ↓
APROVAÇÃO
   ↓
ASSINADO
   ↓
VIGENTE
   ↓
SUSPENSO
   ↓
RETOMADO
   ↓
ENCERRADO

Cada estado deverá possuir operações permitidas e proibidas.

19. Proteção das APIs

As APIs deverão implementar:

autenticação;
autorização;
validação;
rate limiting;
controle de payload;
logs;
correlação;
proteção contra abuso;
versionamento.
20. Proteção contra Injeção

As aplicações deverão utilizar mecanismos seguros de acesso aos dados.

Deverão ser evitadas:

concatenação insegura de SQL;
comandos não parametrizados;
execução direta de conteúdo fornecido pelo usuário;
consultas sem validação.
21. Proteção contra Alterações Indevidas

Operações críticas deverão exigir controles adicionais quando apropriado.

Exemplos:

confirmação explícita;
autorização adicional;
justificativa;
autenticação adicional;
registro de auditoria.
22. Integridade dos Dados

O sistema deverá proteger a integridade por meio de:

validações;
constraints;
transações;
regras de negócio;
controle de concorrência;
auditoria;
versionamento quando necessário.
23. Integridade Referencial

Os relacionamentos definidos no Modelo de Dados deverão possuir mecanismos de integridade apropriados.

Exemplo:

Contrato
   ↓
Processo
   ↓
Resultado

Um contrato não deverá existir sem vínculo válido com seu contexto de origem, quando essa relação for obrigatória.

24. Controle de Concorrência

O sistema deverá evitar conflitos quando múltiplos usuários alterarem simultaneamente o mesmo recurso.

Poderão ser utilizados:

controle otimista;
controle pessimista;
versionamento;
bloqueio;
verificação de versão.
25. Criptografia

Informações que necessitem de proteção deverão utilizar criptografia adequada.

A proteção deverá considerar:

Em trânsito
Cliente
   ↓ HTTPS/TLS
API
Em repouso
Banco
Arquivos
Backups

Os algoritmos e parâmetros criptográficos deverão seguir os padrões corporativos de segurança do SIGMUN.

26. Gestão de Segredos

Segredos não deverão ser armazenados diretamente no código-fonte.

Exemplos:

senhas;
tokens;
chaves;
certificados;
credenciais;
strings de conexão.

Deverão ser utilizados mecanismos apropriados de gestão de segredos.

27. Gestão de Sessões

As sessões deverão possuir:

expiração;
invalidação;
proteção contra sequestro;
controle de renovação;
identificação do usuário.
28. Auditoria de Segurança

As seguintes operações deverão ser auditáveis:

login;
logout;
tentativa de acesso negada;
alteração de permissões;
criação;
alteração;
exclusão;
aprovação;
rejeição;
cancelamento;
assinatura;
suspensão;
retomada;
encerramento.
29. Registro de Auditoria

Cada registro deverá conter, quando aplicável:

id
timestamp
usuario_id
acao
recurso
recurso_id
resultado
ip
user_agent
correlation_id
dados_anteriores
dados_posteriores
motivo
30. Imutabilidade da Auditoria

Registros de auditoria deverão possuir proteção contra alteração ou exclusão indevida.

Quando tecnicamente possível, deverão ser utilizados mecanismos de:

armazenamento append-only;
trilhas protegidas;
retenção;
controle de acesso;
hash;
assinatura ou mecanismos equivalentes.
31. Monitoramento

Deverão ser monitorados eventos como:

excesso de tentativas de login;
acessos negados;
alterações de privilégios;
operações fora do padrão;
erros repetitivos;
falhas de integração;
alterações críticas.
32. Detecção de Anomalias

O SIGMUN poderá utilizar mecanismos analíticos para identificar:

volume incomum de operações;
acessos fora do horário esperado;
alterações repetitivas;
tentativas de acesso indevido;
padrões suspeitos.

A detecção não deverá substituir a análise humana quando esta for necessária.

33. Segurança dos Documentos

Documentos relacionados ao domínio deverão respeitar:

classificação;
autorização;
integridade;
versionamento;
rastreabilidade;
retenção;
descarte.

Os documentos deverão preferencialmente utilizar o serviço corporativo de Gestão Documental.

34. Upload de Arquivos

Arquivos enviados ao sistema deverão ser submetidos a controles como:

validação de extensão;
validação de MIME type;
limite de tamanho;
antivírus;
armazenamento seguro;
controle de acesso;
identificação do usuário;
auditoria.
35. Exportação de Dados

Exportações deverão respeitar as permissões do usuário.

Operações de exportação de grande volume poderão exigir:

autorização adicional;
justificativa;
registro de auditoria;
processamento assíncrono.
36. Relatórios

Relatórios deverão respeitar:

classificação da informação;
permissões;
escopo organizacional;
proteção de dados pessoais.
37. APIs Públicas

Dados destinados à transparência poderão ser publicados por APIs públicas.

Antes da publicação deverão ser aplicados controles para evitar exposição indevida de:

dados pessoais;
informações restritas;
credenciais;
dados internos;
informações protegidas.
38. Integrações Externas

Integrações deverão utilizar mecanismos seguros.

Poderão incluir:

OAuth;
certificados;
tokens;
chaves de API;
assinatura de mensagens;
TLS;
controle de origem;
controle de escopo.
39. Segurança de Mensageria

Eventos e mensagens deverão possuir:

identificação da origem;
autenticação;
autorização;
integridade;
rastreabilidade;
controle de duplicidade;
proteção contra replay quando aplicável.
40. Idempotência

Operações críticas deverão possuir mecanismos de idempotência.

Especialmente:

integrações;
registros financeiros;
publicação;
processamento de eventos;
atualização de contratos.
41. Proteção contra Replay

Operações sensíveis deverão considerar proteção contra repetição indevida de mensagens ou requisições.

Poderão ser utilizados:

nonce;
timestamp;
identificador único;
janela de validade;
controle de idempotência.
42. Segurança de Backups

Backups deverão:

ser protegidos;
possuir controle de acesso;
ser criptografados quando necessário;
possuir retenção definida;
ser testados quanto à restauração.
43. Recuperação

Os serviços deverão estar contemplados nos mecanismos corporativos de:

continuidade;
recuperação de desastres;
backup;
restauração.
44. Disponibilidade

Serviços críticos deverão possuir mecanismos compatíveis com os níveis de disponibilidade definidos pelo SIGMUN.

Deverão ser considerados:

redundância;
monitoramento;
recuperação automática;
contingência.
45. Segurança no Desenvolvimento

O desenvolvimento deverá considerar:

revisão de código;
análise de dependências;
análise estática;
testes de segurança;
gerenciamento de vulnerabilidades;
controle de segredos;
atualização de bibliotecas.
46. Dependências de Software

Dependências utilizadas pelo domínio deverão ser:

identificadas;
versionadas;
monitoradas;
atualizadas;
avaliadas quanto a vulnerabilidades.
47. Segurança de Terceiros

Bibliotecas, APIs e serviços externos deverão ser avaliados considerando:

origem;
confiabilidade;
segurança;
manutenção;
vulnerabilidades;
licença;
continuidade.
48. Ambiente de Desenvolvimento

Credenciais e dados reais de produção não deverão ser utilizados diretamente no ambiente de desenvolvimento.

Quando necessário, deverão ser utilizados:

dados fictícios;
dados anonimizados;
dados mascarados.
49. Ambiente de Testes

O ambiente de testes deverá possuir controles equivalentes aos necessários para validar os mecanismos de segurança.

Testes deverão considerar:

autenticação;
autorização;
privilégios;
segregação;
APIs;
auditoria;
exposição de dados.
50. Testes de Segurança

Deverão ser considerados:

testes de autenticação;
testes de autorização;
testes de acesso indevido;
testes de injeção;
testes de exposição de dados;
testes de sessão;
testes de upload;
testes de APIs.
51. Gestão de Vulnerabilidades

Vulnerabilidades identificadas deverão ser:

registradas;
classificadas;
avaliadas;
priorizadas;
corrigidas;
validadas.
52. Gestão de Incidentes

Incidentes relacionados ao domínio deverão seguir o processo corporativo de Gestão de Incidentes de Segurança.

Exemplos:

acesso indevido;
vazamento;
alteração não autorizada;
indisponibilidade provocada;
comprometimento de credenciais;
malware.
53. Resposta a Incidentes

Quando ocorrer incidente relevante, deverão ser considerados:

Detecção
   ↓
Classificação
   ↓
Contenção
   ↓
Investigação
   ↓
Erradicação
   ↓
Recuperação
   ↓
Lições Aprendidas
54. Responsabilidades
54.1 Equipe de Segurança

Responsável por:

políticas;
padrões;
controles;
avaliação de riscos;
monitoramento;
incidentes.
54.2 Equipe do Domínio

Responsável por:

implementar os controles;
manter configurações;
corrigir vulnerabilidades;
garantir conformidade.
54.3 Gestores

Responsáveis por:

aprovar acessos;
revisar permissões;
validar segregação;
comunicar alterações de responsabilidade.
54.4 Usuários

Responsáveis por:

proteger suas credenciais;
utilizar o sistema corretamente;
comunicar incidentes;
não compartilhar acessos.
55. Revisão de Acessos

Acessos deverão ser revisados periodicamente.

Deverão ser considerados:

mudança de função;
mudança de secretaria;
afastamento;
desligamento;
alteração de responsabilidade;
necessidade de acesso.
56. Revogação

Acessos deverão ser revogados quando:

o usuário deixar de necessitar da permissão;
houver mudança de função;
houver desligamento;
houver risco identificado;
houver determinação administrativa.
57. Acesso Privilegiado

Contas administrativas deverão possuir:

controle reforçado;
autenticação forte;
rastreabilidade;
monitoramento;
revisão periódica.

Contas privilegiadas não deverão ser utilizadas para operações administrativas comuns quando houver alternativa apropriada.

58. Princípio de Não Repúdio

Operações críticas deverão possuir mecanismos suficientes para demonstrar sua autoria e ocorrência.

Poderão ser utilizados:

autenticação;
registros de auditoria;
assinatura eletrônica;
certificados;
carimbo de tempo;
evidências documentais.
59. Segurança das Assinaturas

Quando houver assinatura eletrônica de documentos ou atos, o mecanismo utilizado deverá atender aos requisitos corporativos e legais aplicáveis.

O domínio deverá manter apenas a referência necessária ao serviço de assinatura, quando este for corporativo.

60. Segurança por Ciclo de Vida

A segurança deverá acompanhar todo o ciclo:

Planejamento
   ↓
Desenvolvimento
   ↓
Testes
   ↓
Implantação
   ↓
Operação
   ↓
Manutenção
   ↓
Descontinuação
61. Descontinuação

Quando um serviço ou funcionalidade for descontinuado, deverão ser considerados:

revogação de acessos;
encerramento de credenciais;
retenção dos registros;
migração dos dados;
preservação das evidências;
descarte seguro.
62. Matriz de Controle de Segurança
Controle	Aplicação
Autenticação	Todos os serviços protegidos
Autorização	Todas as operações
Privilégio mínimo	Todos os usuários
Segregação de funções	Operações críticas
Auditoria	Operações relevantes
Criptografia em trânsito	APIs e integrações
Criptografia em repouso	Dados protegidos
Gestão de sessão	Aplicações interativas
Proteção de APIs	APIs expostas
Gestão de segredos	Serviços e integrações
Backup	Dados persistentes
Monitoramento	Serviços críticos
Gestão de vulnerabilidades	Componentes de software
Gestão de incidentes	Eventos de segurança
63. Matriz de Risco × Controle
Risco	Controle
Acesso indevido	Autenticação + autorização
Privilégio excessivo	Privilégio mínimo
Fraude interna	Segregação de funções
Alteração indevida	Auditoria + autorização
Vazamento de dados	Classificação + controle de acesso
Comprometimento de API	TLS + autenticação + rate limiting
Perda de dados	Backup
Indisponibilidade	Continuidade
Alteração de documentos	Controle documental + auditoria
Uso indevido de credenciais	MFA + gestão de identidade
Vulnerabilidade de software	Gestão de vulnerabilidades
Ataque por integração	Autenticação + validação + monitoramento
64. Rastreabilidade de Segurança

A segurança deverá ser rastreável através da seguinte cadeia:

Risco
   ↓
Controle
   ↓
Requisito Não Funcional
   ↓
Serviço
   ↓
Permissão
   ↓
Implementação
   ↓
Teste
   ↓
Evidência
65. Critérios de Aceitação

O modelo será considerado implementado quando:

os usuários forem autenticados;
as permissões forem controladas;
o princípio do menor privilégio for aplicado;
as funções críticas possuírem segregação;
as operações relevantes forem auditadas;
os dados protegidos possuírem controles apropriados;
as APIs possuírem proteção;
as integrações forem autenticadas;
os documentos possuírem controle de acesso;
os mecanismos de backup estiverem definidos;
os incidentes puderem ser rastreados;
os acessos puderem ser revistos e revogados;
vulnerabilidades puderem ser identificadas e tratadas;
os controles estiverem associados aos requisitos correspondentes.
66. Conformidade

O domínio deverá observar:

políticas corporativas do SIGMUN;
princípios de segurança da informação;
requisitos de proteção de dados pessoais;
requisitos de transparência;
normas e legislação aplicáveis à Administração Pública;
controles internos do Município.

Este documento não substitui normas jurídicas, políticas corporativas ou pareceres especializados.

67. Evolução do Modelo

Este modelo deverá ser revisado quando houver:

alteração significativa da arquitetura;
alteração legislativa relevante;
novo risco;
incidente de segurança;
alteração de processo;
nova integração;
alteração do modelo de dados;
mudança significativa de tecnologia.
68. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Modelo de Segurança do Domínio de Gestão de Compras e Contratações

Documento: 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente

