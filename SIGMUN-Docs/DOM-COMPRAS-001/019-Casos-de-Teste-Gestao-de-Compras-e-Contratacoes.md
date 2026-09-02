#### Casos de Teste – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
- 000C-HIERARQUIA-DOCUMENTAL.md
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
- 018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md

---

# 1. Finalidade

Este documento define os **Casos de Teste do Domínio de Gestão de Compras e Contratações do SIGMUN**.

Os casos de teste representam verificações executáveis destinadas a comprovar o comportamento esperado do sistema em relação aos:

- requisitos funcionais;
- requisitos não funcionais;
- regras de negócio;
- casos de uso;
- histórias de usuário;
- critérios de aceitação;
- integrações;
- controles de segurança;
- controles de auditoria.

---

# 2. Objetivos

Os casos de teste têm como objetivos:

1. verificar o comportamento esperado das funcionalidades;
2. validar regras de negócio;
3. validar fluxos positivos;
4. validar fluxos negativos;
5. verificar permissões;
6. verificar transições de estado;
7. verificar integrações;
8. verificar auditoria;
9. verificar consistência dos dados;
10. fornecer evidências para homologação;
11. apoiar testes de regressão;
12. manter rastreabilidade entre requisitos e execução.

---

# 3. Convenção de Identificação

Cada caso de teste deverá possuir identificador único.

Formato:

```text
CT-GCC-XXX

Onde:

CT  = Caso de Teste
GCC = Gestão de Compras e Contratações
XXX = Número sequencial

Exemplos:

CT-GCC-001
CT-GCC-002
CT-GCC-003
4. Estrutura do Caso de Teste

Cada caso deverá possuir:

Código:
Título:
Objetivo:
Tipo:
Prioridade:
Pré-condições:
Dados de Entrada:
Passos:
Resultado Esperado:
Resultado Obtido:
Status:
Evidência:
Defeito:
Requisitos Relacionados:
Regras Relacionadas:
Critérios de Aceitação:
5. Classificação dos Casos de Teste

Os casos poderão ser classificados como:

Funcional;
Negativo;
Regra de Negócio;
Integração;
API;
Segurança;
Auditoria;
Dados;
Workflow;
Performance;
Usabilidade;
Regressão;
Recuperação;
Offline;
Sincronização.
6. Classificação de Prioridade
Prioridade	Descrição
P0	Crítica / impeditiva
P1	Alta
P2	Média
P3	Baixa
7. Status

Os casos poderão assumir os seguintes estados:

Não Executado
Em Execução
Aprovado
Reprovado
Bloqueado
Dispensado
8. Casos de Teste – Demandas
CT-GCC-001 – Criar Demanda

Objetivo: Verificar a criação de uma demanda válida.

Tipo: Funcional

Prioridade: P0

Pré-condições:

usuário autenticado;
usuário possui permissão;
dados obrigatórios disponíveis.

Passos:

acessar o módulo;
selecionar criação de demanda;
informar os dados obrigatórios;
salvar.

Resultado Esperado:

A demanda deverá ser criada com sucesso e receber identificador único.

CT-GCC-002 – Criar Demanda com Dados Obrigatórios Ausentes

Objetivo: Verificar a validação de campos obrigatórios.

Tipo: Negativo

Prioridade: P1

Passos:

iniciar criação de demanda;
deixar campo obrigatório vazio;
tentar salvar.

Resultado Esperado:

O sistema deverá impedir a gravação e informar os campos pendentes.

CT-GCC-003 – Alterar Demanda

Objetivo: Verificar alteração de uma demanda existente.

Tipo: Funcional

Prioridade: P1

Resultado Esperado:

Os dados permitidos deverão ser alterados e a operação deverá ser registrada.

CT-GCC-004 – Usuário Sem Permissão Alterar Demanda

Objetivo: Validar controle de acesso.

Tipo: Segurança

Prioridade: P0

Resultado Esperado:

O sistema deverá negar a operação.

CT-GCC-005 – Registrar Auditoria da Demanda

Objetivo: Verificar geração de trilha de auditoria.

Tipo: Auditoria

Prioridade: P0

Resultado Esperado:

A operação deverá gerar registro contendo, quando aplicável:

usuário;
data/hora;
operação;
entidade;
identificador;
resultado;
correlation_id.
9. Casos de Teste – Planejamento
CT-GCC-006 – Criar Planejamento

Objetivo: Validar criação de planejamento.

Tipo: Funcional

Prioridade: P0

Resultado Esperado:

Planejamento válido deverá ser criado.

CT-GCC-007 – Associar Demanda ao Planejamento

Objetivo: Verificar relacionamento entre demanda e planejamento.

Tipo: Integração

Prioridade: P1

Resultado Esperado:

A associação deverá ser registrada corretamente.

CT-GCC-008 – Impedir Associação Inválida

Objetivo: Verificar rejeição de associação incompatível.

Tipo: Regra de Negócio

Prioridade: P1

Resultado Esperado:

A operação deverá ser rejeitada conforme regra aplicável.

10. Casos de Teste – Processo de Contratação
CT-GCC-009 – Criar Processo

Objetivo: Validar criação de processo de contratação.

Tipo: Funcional

Prioridade: P0

Resultado Esperado:

Processo deverá ser criado com identificador único.

CT-GCC-010 – Criar Processo com Dados Inválidos

Objetivo: Validar rejeição de dados inválidos.

Tipo: Negativo

Prioridade: P1

Resultado Esperado:

Sistema deverá rejeitar a operação e informar o problema.

CT-GCC-011 – Alterar Processo

Objetivo: Validar alteração de dados permitidos.

Tipo: Funcional

Prioridade: P1

CT-GCC-012 – Impedir Alteração Não Autorizada

Objetivo: Validar autorização.

Tipo: Segurança

Prioridade: P0

11. Casos de Teste – Fornecedores
CT-GCC-013 – Cadastrar Fornecedor

Objetivo: Validar cadastro.

Tipo: Funcional

Prioridade: P0

CT-GCC-014 – Impedir Cadastro Duplicado

Objetivo: Validar unicidade.

Tipo: Regra de Negócio

Prioridade: P0

Resultado Esperado:

Sistema deverá impedir duplicidade conforme regra de identificação definida.

CT-GCC-015 – Consultar Fornecedor

Objetivo: Validar consulta.

Tipo: Funcional

Prioridade: P1

CT-GCC-016 – Alterar Fornecedor

Objetivo: Validar alteração permitida.

Tipo: Funcional

Prioridade: P1

CT-GCC-017 – Acesso Restrito aos Dados do Fornecedor

Objetivo: Validar permissões.

Tipo: Segurança

Prioridade: P0

12. Casos de Teste – Itens e Objetos
CT-GCC-018 – Cadastrar Item

Objetivo: Validar cadastro de item.

Tipo: Funcional

Prioridade: P1

CT-GCC-019 – Validar Unidade de Medida

Objetivo: Verificar consistência da unidade.

Tipo: Regra de Negócio

Prioridade: P1

CT-GCC-020 – Impedir Item Inconsistente

Objetivo: Validar integridade dos dados.

Tipo: Negativo

Prioridade: P1

13. Casos de Teste – Propostas
CT-GCC-021 – Registrar Proposta

Objetivo: Validar registro de proposta.

Tipo: Funcional

Prioridade: P0

CT-GCC-022 – Registrar Proposta com Dados Incompletos

Objetivo: Validar obrigatoriedade.

Tipo: Negativo

Prioridade: P1

CT-GCC-023 – Associar Proposta ao Fornecedor

Objetivo: Validar relacionamento.

Tipo: Integração

Prioridade: P1

CT-GCC-024 – Impedir Proposta para Fornecedor Inválido

Objetivo: Validar integridade referencial.

Tipo: Regra de Negócio

Prioridade: P0

14. Casos de Teste – Resultado
CT-GCC-025 – Registrar Resultado

Objetivo: Validar registro do resultado do processo.

Tipo: Funcional

Prioridade: P0

CT-GCC-026 – Registrar Resultado sem Processo Válido

Objetivo: Validar integridade.

Tipo: Negativo

Prioridade: P0

Resultado Esperado:

Operação deverá ser rejeitada.

15. Casos de Teste – Contratos
CT-GCC-027 – Criar Contrato

Objetivo: Validar criação de contrato.

Tipo: Funcional

Prioridade: P0

CT-GCC-028 – Criar Contrato sem Processo de Origem

Objetivo: Validar consistência do processo.

Tipo: Regra de Negócio

Prioridade: P0

Resultado Esperado:

O sistema deverá rejeitar a criação quando a associação for obrigatória.

CT-GCC-029 – Alterar Contrato

Objetivo: Validar alteração permitida.

Tipo: Funcional

Prioridade: P0

CT-GCC-030 – Impedir Alteração Não Autorizada

Objetivo: Validar segurança.

Tipo: Segurança

Prioridade: P0

CT-GCC-031 – Registrar Auditoria do Contrato

Objetivo: Validar trilha de auditoria.

Tipo: Auditoria

Prioridade: P0

16. Casos de Teste – Estados do Contrato
CT-GCC-032 – Contrato em Estado Inicial

Objetivo: Validar estado inicial.

Tipo: Workflow

Prioridade: P0

CT-GCC-033 – Transição de Estado Válida

Objetivo: Validar transição autorizada.

Tipo: Workflow

Prioridade: P0

CT-GCC-034 – Transição de Estado Inválida

Objetivo: Impedir transição não autorizada.

Tipo: Regra de Negócio

Prioridade: P0

Resultado Esperado:

A transição deverá ser rejeitada.

17. Casos de Teste – Documentos
CT-GCC-035 – Anexar Documento

Objetivo: Validar anexação.

Tipo: Funcional

Prioridade: P1

CT-GCC-036 – Anexar Arquivo Inválido

Objetivo: Validar restrições de arquivo.

Tipo: Negativo

Prioridade: P1

CT-GCC-037 – Consultar Documento

Objetivo: Validar consulta conforme permissão.

Tipo: Funcional

Prioridade: P1

CT-GCC-038 – Versionar Documento

Objetivo: Validar versionamento.

Tipo: Funcional

Prioridade: P1

18. Casos de Teste – Assinaturas
CT-GCC-039 – Solicitar Assinatura

Objetivo: Validar solicitação.

Tipo: Funcional

Prioridade: P0

CT-GCC-040 – Assinar Documento

Objetivo: Validar assinatura.

Tipo: Integração

Prioridade: P0

CT-GCC-041 – Recusar Assinatura

Objetivo: Validar recusa.

Tipo: Funcional

Prioridade: P1

CT-GCC-042 – Validar Documento Assinado

Objetivo: Verificar integridade do documento após assinatura.

Tipo: Segurança

Prioridade: P0

19. Casos de Teste – Execução Contratual
CT-GCC-043 – Registrar Execução

Objetivo: Validar registro da execução.

Tipo: Funcional

Prioridade: P0

CT-GCC-044 – Registrar Entrega

Objetivo: Validar registro de entrega.

Tipo: Funcional

Prioridade: P0

CT-GCC-045 – Registrar Medição

Objetivo: Validar medição contratual.

Tipo: Funcional

Prioridade: P0

CT-GCC-046 – Registrar Medição sem Contrato Válido

Objetivo: Validar integridade.

Tipo: Negativo

Prioridade: P0

CT-GCC-047 – Registrar Ocorrência Contratual

Objetivo: Validar registro de ocorrência.

Tipo: Funcional

Prioridade: P1

20. Casos de Teste – Fiscalização
CT-GCC-048 – Registrar Fiscal

Objetivo: Validar associação de responsável pela fiscalização.

Tipo: Funcional

Prioridade: P0

CT-GCC-049 – Registrar Fiscalização

Objetivo: Validar registro de fiscalização.

Tipo: Funcional

Prioridade: P0

CT-GCC-050 – Usuário Não Autorizado Registrar Fiscalização

Objetivo: Validar autorização.

Tipo: Segurança

Prioridade: P0

21. Casos de Teste – Alterações Contratuais
CT-GCC-051 – Registrar Alteração

Objetivo: Validar alteração contratual.

Tipo: Funcional

Prioridade: P0

CT-GCC-052 – Impedir Alteração Sem Autorização

Objetivo: Validar controle de acesso.

Tipo: Segurança

Prioridade: P0

CT-GCC-053 – Registrar Auditoria da Alteração

Objetivo: Garantir rastreabilidade.

Tipo: Auditoria

Prioridade: P0

22. Casos de Teste – Encerramento
CT-GCC-054 – Encerrar Contrato

Objetivo: Validar encerramento regular.

Tipo: Funcional

Prioridade: P0

CT-GCC-055 – Impedir Encerramento com Pendências

Objetivo: Validar regra de negócio.

Tipo: Regra de Negócio

Prioridade: P0

CT-GCC-056 – Registrar Auditoria do Encerramento

Objetivo: Validar trilha de auditoria.

Tipo: Auditoria

Prioridade: P0

23. Casos de Teste – APIs
CT-GCC-057 – Autenticar API

Objetivo: Validar autenticação.

Tipo: API

Prioridade: P0

CT-GCC-058 – Rejeitar API sem Autenticação

Objetivo: Validar proteção.

Tipo: Segurança

Prioridade: P0

CT-GCC-059 – Rejeitar API sem Autorização

Objetivo: Validar autorização.

Tipo: Segurança

Prioridade: P0

CT-GCC-060 – Validar Resposta de API

Objetivo: Validar contrato da API.

Tipo: API

Prioridade: P1

24. Casos de Teste – Integrações
CT-GCC-061 – Integração com Orçamento

Objetivo: Validar comunicação com o domínio de orçamento.

Tipo: Integração

Prioridade: P0

CT-GCC-062 – Integração com Financeiro

Objetivo: Validar integração financeira.

Tipo: Integração

Prioridade: P0

CT-GCC-063 – Falha de Integração

Objetivo: Validar tratamento de falha.

Tipo: Integração

Prioridade: P0

CT-GCC-064 – Timeout de Integração

Objetivo: Validar comportamento em timeout.

Tipo: Resiliência

Prioridade: P1

CT-GCC-065 – Retry de Integração

Objetivo: Validar mecanismo de retry.

Tipo: Resiliência

Prioridade: P1

CT-GCC-066 – Impedir Duplicidade no Retry

Objetivo: Validar idempotência.

Tipo: Integração

Prioridade: P0

25. Casos de Teste – Auditoria
CT-GCC-067 – Registrar Operação Crítica

Objetivo: Verificar auditoria.

Tipo: Auditoria

Prioridade: P0

CT-GCC-068 – Impedir Alteração Indevida do Registro de Auditoria

Objetivo: Validar proteção da trilha.

Tipo: Segurança

Prioridade: P0

CT-GCC-069 – Consultar Auditoria

Objetivo: Validar consulta autorizada.

Tipo: Auditoria

Prioridade: P1

26. Casos de Teste – Segurança
CT-GCC-070 – Login Válido

Objetivo: Validar autenticação.

Tipo: Segurança

Prioridade: P0

CT-GCC-071 – Login Inválido

Objetivo: Validar rejeição de credenciais inválidas.

Tipo: Segurança

Prioridade: P0

CT-GCC-072 – Controle de Acesso por Perfil

Objetivo: Validar autorização.

Tipo: Segurança

Prioridade: P0

CT-GCC-073 – Segregação de Funções

Objetivo: Validar impedimento de conflito de responsabilidades.

Tipo: Segurança

Prioridade: P0

27. Casos de Teste – Notificações
CT-GCC-074 – Gerar Notificação

Objetivo: Validar geração de notificação.

Tipo: Integração

Prioridade: P1

CT-GCC-075 – Notificação de Vencimento

Objetivo: Validar aviso relacionado ao vencimento contratual.

Tipo: Funcional

Prioridade: P1

CT-GCC-076 – Impedir Notificação Duplicada

Objetivo: Validar idempotência.

Tipo: Regra de Negócio

Prioridade: P1

28. Casos de Teste – Relatórios
CT-GCC-077 – Gerar Relatório

Objetivo: Validar geração.

Tipo: Funcional

Prioridade: P1

CT-GCC-078 – Filtrar Relatório

Objetivo: Validar filtros.

Tipo: Funcional

Prioridade: P1

CT-GCC-079 – Exportar Relatório

Objetivo: Validar exportação.

Tipo: Funcional

Prioridade: P2

CT-GCC-080 – Restringir Relatório por Permissão

Objetivo: Validar segurança das informações.

Tipo: Segurança

Prioridade: P0

29. Casos de Teste – Transparência
CT-GCC-081 – Publicar Informação Pública

Objetivo: Validar publicação de informação classificada como pública.

Tipo: Transparência

Prioridade: P1

CT-GCC-082 – Impedir Publicação de Informação Restrita

Objetivo: Validar classificação da informação.

Tipo: Segurança

Prioridade: P0

30. Casos de Teste – Dados
CT-GCC-083 – Validar Integridade Referencial

Objetivo: Verificar relacionamentos.

Tipo: Dados

Prioridade: P0

CT-GCC-084 – Impedir Registro Órfão

Objetivo: Validar consistência.

Tipo: Dados

Prioridade: P0

CT-GCC-085 – Validar Unicidade

Objetivo: Validar restrições de unicidade.

Tipo: Dados

Prioridade: P1

31. Casos de Teste – Concorrência
CT-GCC-086 – Alterações Concorrentes

Objetivo: Validar comportamento diante de alterações simultâneas.

Tipo: Concorrência

Prioridade: P1

CT-GCC-087 – Prevenir Perda de Atualização

Objetivo: Validar controle de concorrência.

Tipo: Concorrência

Prioridade: P0

32. Casos de Teste – Performance
CT-GCC-088 – Tempo de Resposta

Objetivo: Validar tempo de resposta de operações críticas.

Tipo: Performance

Prioridade: P1

CT-GCC-089 – Carga Concorrente

Objetivo: Validar comportamento sob carga.

Tipo: Performance

Prioridade: P1

CT-GCC-090 – Consulta com Grande Volume

Objetivo: Avaliar desempenho com grande quantidade de registros.

Tipo: Performance

Prioridade: P1

33. Casos de Teste – Recuperação
CT-GCC-091 – Recuperação após Falha de Serviço

Objetivo: Validar recuperação.

Tipo: Recuperação

Prioridade: P0

CT-GCC-092 – Recuperação após Falha de Integração

Objetivo: Validar retomada da comunicação.

Tipo: Recuperação

Prioridade: P1

34. Casos de Teste – Offline First
CT-GCC-093 – Operação Offline

Objetivo: Validar funcionamento offline quando aplicável.

Tipo: Offline

Prioridade: P1

CT-GCC-094 – Sincronização após Reconexão

Objetivo: Validar sincronização.

Tipo: Sincronização

Prioridade: P1

CT-GCC-095 – Resolver Conflito de Sincronização

Objetivo: Validar estratégia de conflitos.

Tipo: Sincronização

Prioridade: P1

35. Casos de Teste – Backup e Restauração
CT-GCC-096 – Restaurar Dados

Objetivo: Validar restauração.

Tipo: Recuperação

Prioridade: P0

CT-GCC-097 – Validar Integridade após Restauração

Objetivo: Garantir consistência após recuperação.

Tipo: Recuperação

Prioridade: P0

36. Casos de Teste – Regressão
CT-GCC-098 – Executar Suíte de Regressão

Objetivo: Garantir que alterações não introduzam regressões.

Tipo: Regressão

Prioridade: P0

CT-GCC-099 – Regressão após Alteração de Regra

Objetivo: Validar impactos de alteração de regra de negócio.

Tipo: Regressão

Prioridade: P0

CT-GCC-100 – Regressão após Alteração de Integração

Objetivo: Validar impactos de alteração de integração.

Tipo: Regressão

Prioridade: P0

37. Matriz Resumida
Código	Área	Tipo	Prioridade
CT-GCC-001	Demandas	Funcional	P0
CT-GCC-009	Processos	Funcional	P0
CT-GCC-013	Fornecedores	Funcional	P0
CT-GCC-021	Propostas	Funcional	P0
CT-GCC-027	Contratos	Funcional	P0
CT-GCC-043	Execução	Funcional	P0
CT-GCC-049	Fiscalização	Funcional	P0
CT-GCC-054	Encerramento	Funcional	P0
CT-GCC-057	API	Segurança	P0
CT-GCC-061	Integrações	Integração	P0
CT-GCC-067	Auditoria	Auditoria	P0
CT-GCC-070	Segurança	Segurança	P0
CT-GCC-083	Dados	Dados	P0
CT-GCC-086	Concorrência	Concorrência	P1
CT-GCC-088	Performance	Performance	P1
CT-GCC-091	Recuperação	Recuperação	P0
CT-GCC-093	Offline	Offline	P1
CT-GCC-098	Regressão	Regressão	P0
38. Rastreabilidade

Os casos de teste deverão ser relacionados aos artefatos correspondentes.

Caso de Uso
     ↓
História de Usuário
     ↓
Regra de Negócio
     ↓
Requisito
     ↓
Critério de Aceitação
     ↓
Caso de Teste
     ↓
Execução
     ↓
Evidência

A relação definitiva deverá ser mantida na:

012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md

e no mapa mestre:

000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
39. Critérios para Aprovação

Um caso de teste será considerado Aprovado quando:

todas as pré-condições forem atendidas;
os passos forem executados;
o resultado obtido corresponder ao esperado;
não houver defeito impeditivo;
a evidência estiver registrada quando necessária.
40. Critérios para Reprovação

Um caso será considerado Reprovado quando:

resultado esperado não for obtido;
regra de negócio for violada;
requisito não for atendido;
comportamento de segurança estiver incorreto;
integração produzir resultado incompatível;
auditoria obrigatória não for registrada.
41. Critérios para Bloqueio

Um caso poderá ser marcado como Bloqueado quando:

ambiente estiver indisponível;
dependência externa estiver indisponível;
dados necessários não estiverem disponíveis;
defeito impeditivo impedir a execução;
requisito ainda estiver indefinido.
42. Evidências

As evidências poderão incluir:

screenshots;
logs;
respostas de API;
registros de auditoria;
relatórios;
arquivos;
vídeos;
resultados automatizados.
43. Gestão de Defeitos

Quando um caso falhar, deverá ser registrado defeito contendo, no mínimo:

Identificador:
Caso de Teste:
Descrição:
Passos para Reprodução:
Resultado Esperado:
Resultado Obtido:
Severidade:
Prioridade:
Ambiente:
Versão:
Evidência:
Responsável:
Status:
44. Execução Automatizada

Os casos que forem candidatos à automação deverão possuir referência para o teste automatizado correspondente.

Exemplo:

CT-GCC-001
      ↓
teste_demanda_criacao
45. Execução Manual

Casos não automatizados deverão possuir registro da execução.

Exemplo:

Caso: CT-GCC-049
Executor: Equipe de Testes
Data: YYYY-MM-DD
Resultado: Aprovado
Evidência: referência correspondente
46. Casos Críticos

Os seguintes grupos deverão possuir prioridade máxima de cobertura:

contratos;
valores;
permissões;
segurança;
auditoria;
integridade dos dados;
integrações financeiras;
transições de estado;
encerramento;
publicação de informações.
47. Evolução dos Casos de Teste

Este documento deverá evoluir continuamente.

Novos casos deverão ser acrescentados quando houver:

novo requisito;
nova regra de negócio;
nova integração;
novo risco;
novo incidente;
nova vulnerabilidade;
alteração arquitetural;
alteração de processo;
defeito recorrente.
48. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação dos Casos de Teste do Domínio de Gestão de Compras e Contratações

Documento: 019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente
