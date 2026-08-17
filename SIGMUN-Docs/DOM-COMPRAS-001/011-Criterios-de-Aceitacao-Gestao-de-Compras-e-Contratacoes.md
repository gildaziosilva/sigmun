# 011 – Critérios de Aceitação – Gestão de Compras e Contratações

#### Critérios de Aceitação – Gestão de Compras e Contratações

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
* 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
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

Este documento define os **Critérios de Aceitação do Domínio de Gestão de Compras e Contratações** do SIGMUN.

Os critérios de aceitação estabelecem as condições objetivas que deverão ser satisfeitas para que uma funcionalidade, serviço, processo ou requisito seja considerado **aceito**.

Os critérios deverão transformar os requisitos e especificações em condições:

* verificáveis;
* mensuráveis quando aplicável;
* testáveis;
* rastreáveis;
* reproduzíveis;
* compreensíveis pelas áreas de negócio e pelas equipes técnicas.

---

# 2. Objetivos

Os critérios de aceitação têm como objetivos:

1. definir claramente o resultado esperado;
2. reduzir ambiguidades;
3. estabelecer condições de aprovação;
4. apoiar homologação;
5. orientar testes;
6. permitir rastreabilidade;
7. evitar interpretação subjetiva;
8. estabelecer condições mínimas para entrada em produção;
9. apoiar auditoria;
10. preservar conhecimento institucional.

---

# 3. Princípios

Os critérios deverão observar:

* clareza;
* objetividade;
* verificabilidade;
* rastreabilidade;
* independência de implementação quando possível;
* foco no resultado;
* consistência;
* segurança;
* acessibilidade;
* conformidade;
* auditabilidade.

---

# 4. Convenção de Identificação

Os critérios utilizarão o padrão:

```text
CA-COMPRAS-XXX
```

Exemplo:

```text
CA-COMPRAS-001
```

Quando necessário, poderão existir critérios derivados:

```text
CA-COMPRAS-001.1
CA-COMPRAS-001.2
CA-COMPRAS-001.3
```

---

# 5. Estrutura de um Critério de Aceitação

Cada critério deverá possuir:

```text
Identificador
Título
Objetivo
Origem
Pré-condições
Dados de entrada
Condição
Resultado esperado
Método de validação
Prioridade
Rastreabilidade
```

Quando aplicável, deverá utilizar o formato:

```text
Dado que...
Quando...
Então...
```

---

# 6. Estados de Aceitação

Cada critério poderá assumir os seguintes estados:

| Estado        | Descrição                              |
| ------------- | -------------------------------------- |
| Pendente      | Ainda não executado                    |
| Em execução   | Validação em andamento                 |
| Aprovado      | Critério atendido                      |
| Reprovado     | Critério não atendido                  |
| Bloqueado     | Não pode ser executado por dependência |
| Não aplicável | Critério não se aplica ao cenário      |

---

# 7. Critérios Gerais do Domínio

## CA-COMPRAS-001 – Acesso Autorizado

**Dado que** o usuário possui credencial válida e permissão para acessar o domínio.

**Quando** acessar uma funcionalidade autorizada.

**Então** o sistema deverá permitir o acesso.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

**Rastreabilidade:** RNF-COMPRAS-001, RNF-COMPRAS-002.

---

## CA-COMPRAS-002 – Acesso Não Autorizado

**Dado que** o usuário não possui permissão para determinada funcionalidade.

**Quando** tentar acessá-la.

**Então** o sistema deverá impedir o acesso.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

**Rastreabilidade:** RNF-COMPRAS-003, RNF-COMPRAS-006.

---

## CA-COMPRAS-003 – Identificação do Usuário

**Dado que** uma operação autenticada é realizada.

**Quando** a operação for registrada.

**Então** deverá ser possível identificar o usuário responsável.

**Método de validação:** Inspeção de auditoria.

**Prioridade:** P0.

---

# 8. Critérios de Demanda

## CA-COMPRAS-004 – Criar Demanda

**Dado que** o usuário possui permissão para registrar demandas.

**Quando** informar os campos obrigatórios e confirmar o cadastro.

**Então** o sistema deverá criar uma demanda com identificador único.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

**Rastreabilidade:** ESP-COMPRAS-002, ESP-COMPRAS-010.

---

## CA-COMPRAS-005 – Campos Obrigatórios da Demanda

**Dado que** o usuário está criando uma demanda.

**Quando** deixar um campo obrigatório sem preenchimento.

**Então** o sistema deverá impedir a conclusão e informar o campo que necessita de preenchimento.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-006 – Identificação da Demanda

**Dado que** uma demanda foi criada com sucesso.

**Então** ela deverá possuir identificador único e permanecer rastreável durante seu ciclo de vida.

**Método de validação:** Teste funcional e inspeção de dados.

**Prioridade:** P0.

---

## CA-COMPRAS-007 – Histórico da Demanda

**Dado que** uma demanda existente sofre alteração relevante.

**Quando** a alteração for confirmada.

**Então** o sistema deverá preservar o histórico correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 9. Critérios de Planejamento

## CA-COMPRAS-008 – Inclusão no Planejamento

**Dado que** uma demanda está apta ao planejamento.

**Quando** for incluída no planejamento de contratações.

**Então** deverá ficar associada ao planejamento correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-009 – Priorização

**Dado que** o planejamento permite priorização.

**Quando** uma prioridade for atribuída.

**Então** o sistema deverá preservar a prioridade definida e registrá-la no histórico quando aplicável.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 10. Critérios de Processo

## CA-COMPRAS-010 – Abertura de Processo

**Dado que** existem informações mínimas necessárias.

**Quando** o usuário autorizado confirmar a abertura.

**Então** o sistema deverá criar o processo e registrar sua abertura.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

**Rastreabilidade:** ESP-COMPRAS-008.

---

## CA-COMPRAS-011 – Identificador do Processo

Após a abertura, o processo deverá possuir identificador único.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-012 – Estado Inicial

Após sua criação, o processo deverá assumir o estado inicial definido para o fluxo correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-013 – Transição Válida

**Dado que** um processo está em determinado estado.

**Quando** o usuário executar uma transição permitida.

**Então** o processo deverá assumir o próximo estado válido.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-014 – Transição Inválida

**Dado que** uma transição não é permitida no estado atual.

**Quando** o usuário tentar executá-la.

**Então** o sistema deverá impedir a operação.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 11. Critérios de Instrução

## CA-COMPRAS-015 – Inclusão de Documento

**Dado que** o usuário possui permissão para anexar documentos.

**Quando** inserir um documento válido.

**Então** o documento deverá ser associado ao processo correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-016 – Documento Obrigatório

**Dado que** determinado tipo de processo exige um documento obrigatório.

**Quando** o usuário tentar avançar sem o documento.

**Então** o sistema deverá aplicar a regra configurada.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-017 – Integridade Documental

Um documento anexado deverá permanecer íntegro e recuperável conforme as políticas de gestão documental.

**Método de validação:** Teste de integridade.

**Prioridade:** P0.

---

# 12. Critérios de Aprovação

## CA-COMPRAS-018 – Aprovação Autorizada

**Dado que** o processo está apto à aprovação.

**Quando** um usuário com competência adequada aprová-lo.

**Então** o sistema deverá registrar a aprovação e atualizar o estado correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-019 – Aprovação Não Autorizada

**Dado que** o usuário não possui competência para aprovar.

**Quando** tentar aprovar o processo.

**Então** o sistema deverá impedir a operação.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

## CA-COMPRAS-020 – Registro da Aprovação

Toda aprovação deverá possuir:

* usuário;
* data;
* hora;
* decisão;
* processo;
* contexto da aprovação.

**Método de validação:** Inspeção de auditoria.

**Prioridade:** P0.

---

# 13. Critérios de Contratação

## CA-COMPRAS-021 – Formalização da Contratação

**Dado que** o processo está apto à formalização.

**Quando** a contratação for formalizada.

**Então** o sistema deverá registrar a contratação e associá-la ao processo de origem.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-022 – Associação com Fornecedor

A contratação deverá possuir fornecedor identificado conforme o cadastro corporativo.

**Método de validação:** Teste funcional e integração.

**Prioridade:** P0.

---

## CA-COMPRAS-023 – Valor da Contratação

O sistema deverá registrar o valor da contratação conforme os dados oficiais informados.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 14. Critérios de Contrato

## CA-COMPRAS-024 – Criação do Contrato

**Dado que** uma contratação foi formalizada.

**Quando** o contrato for criado.

**Então** deverá possuir identificação única e associação ao processo de origem.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-025 – Dados Mínimos do Contrato

O contrato deverá possuir, quando aplicável:

* número;
* fornecedor;
* objeto;
* valor;
* vigência;
* unidade responsável;
* gestor;
* fiscal.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-026 – Controle de Vigência

O sistema deverá impedir inconsistências nas datas de vigência conforme as regras configuradas.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-027 – Alerta de Vencimento

**Dado que** um contrato possui prazo de vencimento configurado.

**Quando** atingir o período de alerta.

**Então** o sistema deverá gerar a notificação correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 15. Critérios de Fiscalização

## CA-COMPRAS-028 – Registro de Fiscalização

O usuário autorizado deverá conseguir registrar uma atividade de fiscalização vinculada ao contrato.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-029 – Responsável pela Fiscalização

Cada registro de fiscalização deverá identificar o responsável correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-030 – Evidências

O sistema deverá permitir associar evidências à atividade de fiscalização quando previsto.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 16. Critérios de Entrega

## CA-COMPRAS-031 – Registro de Entrega

O sistema deverá permitir registrar uma entrega vinculada ao contrato.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-032 – Dados da Entrega

O registro deverá permitir identificar:

* item;
* quantidade;
* data;
* fornecedor;
* responsável;
* situação.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 17. Critérios de Medição

## CA-COMPRAS-033 – Registro de Medição

Quando aplicável, o sistema deverá permitir registrar uma medição vinculada ao contrato.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-034 – Aprovação da Medição

Quando houver fluxo de aprovação configurado, a medição somente deverá avançar após a aprovação correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 18. Critérios de Alteração Contratual

## CA-COMPRAS-035 – Registro de Aditivo

O sistema deverá permitir registrar alteração contratual vinculada ao contrato de origem.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-036 – Histórico do Contrato

Após uma alteração contratual, o sistema deverá preservar o histórico necessário para reconstrução da evolução do contrato.

**Método de validação:** Teste funcional e auditoria.

**Prioridade:** P0.

---

# 19. Critérios de Ocorrência

## CA-COMPRAS-037 – Registro de Ocorrência

O sistema deverá permitir registrar ocorrência vinculada ao contrato.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-038 – Evidência de Ocorrência

Quando aplicável, o sistema deverá permitir anexar evidências à ocorrência.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 20. Critérios de Encerramento

## CA-COMPRAS-039 – Encerramento Válido

**Dado que** todas as condições obrigatórias de encerramento foram satisfeitas.

**Quando** o usuário autorizado solicitar o encerramento.

**Então** o contrato deverá assumir o estado de encerrado.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-040 – Encerramento com Pendências

**Dado que** existem pendências que impedem o encerramento.

**Quando** o usuário tentar encerrar.

**Então** o sistema deverá aplicar a regra configurada e impedir o encerramento quando houver bloqueio.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

# 21. Critérios de Auditoria

## CA-COMPRAS-041 – Auditoria de Criação

A criação de entidades críticas deverá gerar evento de auditoria.

**Método de validação:** Inspeção de logs.

**Prioridade:** P0.

---

## CA-COMPRAS-042 – Auditoria de Alteração

Alterações relevantes deverão gerar registro de auditoria.

**Método de validação:** Inspeção de logs.

**Prioridade:** P0.

---

## CA-COMPRAS-043 – Auditoria de Decisão

Aprovações, rejeições e decisões relevantes deverão ser auditadas.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

## CA-COMPRAS-044 – Proteção da Auditoria

Um usuário sem permissão adequada não deverá conseguir alterar ou excluir registros de auditoria.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

# 22. Critérios de Segurança

## CA-COMPRAS-045 – Segregação de Funções

O sistema deverá impedir operações incompatíveis quando a política de segregação de funções assim determinar.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

## CA-COMPRAS-046 – Privilégio Mínimo

O usuário deverá visualizar e executar somente operações compatíveis com suas permissões.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

## CA-COMPRAS-047 – Dados Protegidos

Informações protegidas não deverão ser apresentadas a usuários sem autorização.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

# 23. Critérios de Privacidade

## CA-COMPRAS-048 – Minimização

O sistema não deverá exigir dados pessoais além daqueles necessários para o processo correspondente.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

## CA-COMPRAS-049 – Classificação da Informação

Informações deverão possuir classificação adequada quando exigida pela política corporativa.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

# 24. Critérios de Integração

## CA-COMPRAS-050 – Integração com Identidade

O acesso ao domínio deverá utilizar o mecanismo corporativo de identidade definido para o SIGMUN.

**Método de validação:** Teste de integração.

**Prioridade:** P0.

---

## CA-COMPRAS-051 – Integração com Cadastro

Quando houver cadastro corporativo aplicável, o domínio deverá utilizar a informação oficial disponibilizada pelo serviço correspondente.

**Método de validação:** Teste de integração.

**Prioridade:** P0.

---

## CA-COMPRAS-052 – Falha de Integração

**Dado que** uma integração externa está indisponível.

**Quando** uma operação dependente for executada.

**Então** o sistema deverá tratar a falha de forma controlada, sem produzir inconsistência silenciosa.

**Método de validação:** Teste de integração.

**Prioridade:** P0.

---

## CA-COMPRAS-053 – Reprocessamento

Quando uma integração suportar reprocessamento, uma operação falha deverá poder ser reprocessada sem duplicação indevida.

**Método de validação:** Teste de integração.

**Prioridade:** P1.

---

# 25. Critérios de Idempotência

## CA-COMPRAS-054 – Processamento Duplicado

**Dado que** uma mesma mensagem ou operação seja recebida mais de uma vez.

**Quando** o processamento for executado.

**Então** o sistema não deverá produzir duplicação indevida.

**Método de validação:** Teste de integração.

**Prioridade:** P0.

---

# 26. Critérios de Dados

## CA-COMPRAS-055 – Identificador Único

Entidades críticas deverão possuir identificador único.

**Método de validação:** Teste de dados.

**Prioridade:** P0.

---

## CA-COMPRAS-056 – Integridade Referencial

O sistema não deverá permitir relacionamentos inválidos entre entidades.

**Método de validação:** Teste de dados.

**Prioridade:** P0.

---

## CA-COMPRAS-057 – Consistência

Operações transacionais deverão preservar a consistência dos dados.

**Método de validação:** Teste funcional e de integração.

**Prioridade:** P0.

---

# 27. Critérios de Desempenho

## CA-COMPRAS-058 – Tempo de Resposta

As operações deverão atender aos tempos definidos nos respectivos SLAs/SLOs.

**Método de validação:** Teste de desempenho.

**Prioridade:** P1.

**Observação:** Os valores quantitativos deverão ser definidos após validação arquitetural.

---

## CA-COMPRAS-059 – Carga

O domínio deverá suportar os volumes de usuários e operações definidos para o ambiente correspondente.

**Método de validação:** Teste de carga.

**Prioridade:** P1.

---

# 28. Critérios de Disponibilidade

## CA-COMPRAS-060 – Disponibilidade

Os serviços classificados como críticos deverão atender ao nível de disponibilidade estabelecido pelo SIGMUN.

**Método de validação:** Monitoramento e teste.

**Prioridade:** P0.

---

# 29. Critérios de Operação Offline

## CA-COMPRAS-061 – Captura Offline

**Dado que** a funcionalidade está habilitada para operação offline.

**Quando** o dispositivo estiver sem conectividade.

**Então** o usuário deverá conseguir executar as operações permitidas.

**Método de validação:** Teste offline.

**Prioridade:** P1.

---

## CA-COMPRAS-062 – Sincronização Posterior

**Dado que** dados foram registrados offline.

**Quando** a conectividade for restabelecida.

**Então** os dados deverão ser sincronizados conforme as regras definidas.

**Método de validação:** Teste de sincronização.

**Prioridade:** P1.

---

## CA-COMPRAS-063 – Conflito de Sincronização

**Dado que** existe conflito entre dados locais e dados do servidor.

**Quando** ocorrer a sincronização.

**Então** o sistema deverá identificar o conflito e aplicar a estratégia definida.

**Método de validação:** Teste de sincronização.

**Prioridade:** P0.

---

# 30. Critérios de Observabilidade

## CA-COMPRAS-064 – Logs

Eventos técnicos relevantes deverão gerar logs conforme os padrões corporativos.

**Método de validação:** Inspeção.

**Prioridade:** P1.

---

## CA-COMPRAS-065 – Métricas

Serviços críticos deverão disponibilizar as métricas definidas para monitoramento.

**Método de validação:** Inspeção de observabilidade.

**Prioridade:** P1.

---

## CA-COMPRAS-066 – Correlação

Operações distribuídas deverão permitir rastreamento por identificador de correlação.

**Método de validação:** Teste de integração.

**Prioridade:** P1.

---

# 31. Critérios de Usabilidade

## CA-COMPRAS-067 – Mensagens

Erros e alertas deverão apresentar mensagens compreensíveis ao usuário.

**Método de validação:** Teste de usabilidade.

**Prioridade:** P1.

---

## CA-COMPRAS-068 – Preservação de Dados

Quando ocorrer erro recuperável, os dados já informados deverão ser preservados sempre que tecnicamente possível.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 32. Critérios de Acessibilidade

## CA-COMPRAS-069 – Acessibilidade

As funcionalidades deverão atender aos padrões de acessibilidade adotados pelo SIGMUN.

**Método de validação:** Teste de acessibilidade.

**Prioridade:** P0.

---

## CA-COMPRAS-070 – Navegação por Teclado

As funcionalidades aplicáveis deverão ser utilizáveis por teclado.

**Método de validação:** Teste de acessibilidade.

**Prioridade:** P1.

---

# 33. Critérios de Transparência

## CA-COMPRAS-071 – Publicação de Dados Públicos

Informações classificadas como públicas e elegíveis para publicação deverão poder ser disponibilizadas nos mecanismos de transparência correspondentes.

**Método de validação:** Teste funcional.

**Prioridade:** P0.

---

## CA-COMPRAS-072 – Proteção de Dados Restritos

Dados restritos não deverão ser publicados automaticamente.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

## CA-COMPRAS-073 – Integridade da Publicação

Informações publicadas deverão corresponder aos dados oficiais autorizados para publicação.

**Método de validação:** Teste de integração.

**Prioridade:** P0.

---

# 34. Critérios de Parametrização

## CA-COMPRAS-074 – Configuração de Fluxos

Quando o fluxo for parametrizável, uma alteração de configuração autorizada deverá produzir o comportamento correspondente sem alteração do código.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

## CA-COMPRAS-075 – Documentos Obrigatórios

Quando documentos obrigatórios forem configuráveis, a alteração autorizada deverá ser refletida no processo correspondente.

**Método de validação:** Teste funcional.

**Prioridade:** P1.

---

# 35. Critérios de Multiunidade

## CA-COMPRAS-076 – Isolamento Organizacional

Usuários deverão acessar somente processos das unidades às quais possuem autorização.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

# 36. Critérios de Multi-Município

## CA-COMPRAS-077 – Isolamento entre Municípios

Quando a plataforma estiver configurada para múltiplos municípios, dados de um município não deverão ser acessíveis por outro sem autorização institucional específica.

**Método de validação:** Teste de segurança.

**Prioridade:** P0.

---

# 37. Critérios de Recuperação

## CA-COMPRAS-078 – Backup

Os dados críticos deverão estar incluídos na estratégia de backup definida.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

## CA-COMPRAS-079 – Restauração

Deverá ser possível restaurar os dados conforme os procedimentos corporativos.

**Método de validação:** Teste de recuperação.

**Prioridade:** P0.

---

# 38. Critérios de Continuidade

## CA-COMPRAS-080 – Recuperação de Desastre

Os componentes críticos deverão participar dos testes corporativos de recuperação de desastre.

**Método de validação:** Teste de continuidade.

**Prioridade:** P0.

---

# 39. Critérios de Testabilidade

## CA-COMPRAS-081 – Cobertura de Funcionalidades Críticas

Funcionalidades críticas deverão possuir testes correspondentes.

**Método de validação:** Inspeção de testes.

**Prioridade:** P0.

---

## CA-COMPRAS-082 – Testes de Integração

Integrações críticas deverão possuir testes de integração.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

## CA-COMPRAS-083 – Testes de Segurança

Operações críticas deverão possuir testes de segurança apropriados.

**Método de validação:** Inspeção e execução de testes.

**Prioridade:** P0.

---

# 40. Critérios de Conformidade

## CA-COMPRAS-084 – Conformidade Normativa

Os processos deverão respeitar as regras normativas configuradas e aplicáveis ao município.

**Método de validação:** Teste funcional e inspeção.

**Prioridade:** P0.

---

## CA-COMPRAS-085 – Evidências

O sistema deverá preservar as evidências necessárias à comprovação das operações realizadas.

**Método de validação:** Inspeção.

**Prioridade:** P0.

---

# 41. Critérios de Rastreabilidade

## CA-COMPRAS-086 – Rastreabilidade do Requisito

Todo requisito funcional crítico deverá possuir pelo menos um critério de aceitação.

**Método de validação:** Inspeção documental.

**Prioridade:** P0.

---

## CA-COMPRAS-087 – Rastreabilidade da Especificação

Toda especificação relevante deverá possuir pelo menos um critério de aceitação aplicável.

**Método de validação:** Inspeção documental.

**Prioridade:** P0.

---

## CA-COMPRAS-088 – Rastreabilidade até Teste

Critérios aprovados deverão possuir vínculo com os testes correspondentes.

**Método de validação:** Inspeção de rastreabilidade.

**Prioridade:** P0.

---

# 42. Critérios de Rejeição

Uma funcionalidade deverá ser considerada **não aceita** quando ocorrer qualquer uma das seguintes condições:

* requisito crítico não atendido;
* critério P0 reprovado;
* violação de segurança;
* perda de dados;
* inconsistência transacional;
* falha de auditoria obrigatória;
* exposição indevida de dados;
* violação de segregação de funções;
* falha de integridade documental;
* falha de integração crítica;
* impossibilidade de rastrear operação crítica;
* descumprimento de requisito legal aplicável.

---

# 43. Critérios para Aceitação Parcial

A aceitação parcial poderá ocorrer somente quando:

1. os critérios críticos estiverem aprovados;
2. os critérios pendentes não impedirem a operação;
3. os riscos estiverem formalmente registrados;
4. houver autorização da governança responsável;
5. existir plano para correção das pendências.

---

# 44. Critérios de Homologação

A homologação deverá envolver, quando aplicável:

* área requisitante;
* área de compras;
* área administrativa;
* responsáveis pelo processo;
* gestores;
* fiscalização;
* equipe técnica;
* segurança;
* governança.

---

# 45. Evidências de Aceitação

Cada critério aprovado deverá possuir evidência adequada.

Exemplos:

* captura de tela;
* resultado de teste;
* relatório;
* log;
* registro de auditoria;
* evidência de integração;
* relatório de desempenho;
* documento de homologação;
* resultado de teste de segurança.

---

# 46. Matriz Consolidada

| Faixa                | Grupo                 |
| -------------------- | --------------------- |
| CA-COMPRAS-001 a 003 | Acesso                |
| CA-COMPRAS-004 a 007 | Demanda               |
| CA-COMPRAS-008 a 009 | Planejamento          |
| CA-COMPRAS-010 a 014 | Processo              |
| CA-COMPRAS-015 a 017 | Instrução             |
| CA-COMPRAS-018 a 020 | Aprovação             |
| CA-COMPRAS-021 a 023 | Contratação           |
| CA-COMPRAS-024 a 027 | Contratos             |
| CA-COMPRAS-028 a 030 | Fiscalização          |
| CA-COMPRAS-031 a 032 | Entregas              |
| CA-COMPRAS-033 a 034 | Medições              |
| CA-COMPRAS-035 a 036 | Alterações            |
| CA-COMPRAS-037 a 038 | Ocorrências           |
| CA-COMPRAS-039 a 040 | Encerramento          |
| CA-COMPRAS-041 a 044 | Auditoria             |
| CA-COMPRAS-045 a 047 | Segurança             |
| CA-COMPRAS-048 a 049 | Privacidade           |
| CA-COMPRAS-050 a 053 | Integrações           |
| CA-COMPRAS-054       | Idempotência          |
| CA-COMPRAS-055 a 057 | Dados                 |
| CA-COMPRAS-058 a 059 | Desempenho            |
| CA-COMPRAS-060       | Disponibilidade       |
| CA-COMPRAS-061 a 063 | Offline/Sincronização |
| CA-COMPRAS-064 a 066 | Observabilidade       |
| CA-COMPRAS-067 a 068 | Usabilidade           |
| CA-COMPRAS-069 a 070 | Acessibilidade        |
| CA-COMPRAS-071 a 073 | Transparência         |
| CA-COMPRAS-074 a 075 | Parametrização        |
| CA-COMPRAS-076       | Multiunidade          |
| CA-COMPRAS-077       | Multi-Município       |
| CA-COMPRAS-078 a 079 | Recuperação           |
| CA-COMPRAS-080       | Continuidade          |
| CA-COMPRAS-081 a 083 | Testabilidade         |
| CA-COMPRAS-084 a 085 | Conformidade          |
| CA-COMPRAS-086 a 088 | Rastreabilidade       |

---

# 47. Matriz Inicial de Rastreabilidade

| Critério       | Especificação       | Requisito   |
| -------------- | ------------------- | ----------- |
| CA-COMPRAS-004 | ESP-COMPRAS-002/010 | RF-COMPRAS  |
| CA-COMPRAS-010 | ESP-COMPRAS-008     | RF-COMPRAS  |
| CA-COMPRAS-013 | ESP-COMPRAS-009     | RF-COMPRAS  |
| CA-COMPRAS-015 | ESP-COMPRAS-015     | RF-COMPRAS  |
| CA-COMPRAS-018 | ESP-COMPRAS-017     | RF-COMPRAS  |
| CA-COMPRAS-021 | ESP-COMPRAS-018     | RF-COMPRAS  |
| CA-COMPRAS-024 | ESP-COMPRAS-019     | RF-COMPRAS  |
| CA-COMPRAS-028 | ESP-COMPRAS-021     | RF-COMPRAS  |
| CA-COMPRAS-033 | ESP-COMPRAS-023     | RF-COMPRAS  |
| CA-COMPRAS-035 | ESP-COMPRAS-024     | RF-COMPRAS  |
| CA-COMPRAS-041 | ESP-COMPRAS-027     | RNF-COMPRAS |
| CA-COMPRAS-045 | ESP-COMPRAS-028     | RNF-COMPRAS |
| CA-COMPRAS-050 | ESP-COMPRAS-029     | RNF-COMPRAS |
| CA-COMPRAS-054 | ESP-COMPRAS-052     | RNF-COMPRAS |
| CA-COMPRAS-058 | ESP-COMPRAS-053     | RNF-COMPRAS |
| CA-COMPRAS-061 | ESP-COMPRAS-048     | RNF-COMPRAS |
| CA-COMPRAS-064 | ESP-COMPRAS-054/055 | RNF-COMPRAS |
| CA-COMPRAS-069 | RNF-COMPRAS-034     | RNF-COMPRAS |
| CA-COMPRAS-071 | ESP-COMPRAS-047     | RNF-COMPRAS |
| CA-COMPRAS-078 | ESP-COMPRAS-064     | RNF-COMPRAS |
| CA-COMPRAS-086 | ESP-COMPRAS-065     | RNF-COMPRAS |

A matriz completa deverá ser mantida no artefato de rastreabilidade do domínio.

---

# 48. Processo de Homologação

O fluxo recomendado será:

```text
Desenvolvimento
      ↓
Testes automatizados
      ↓
Testes de integração
      ↓
Testes de segurança
      ↓
Homologação
      ↓
Correção de não conformidades
      ↓
Revalidação
      ↓
Aprovação
      ↓
Implantação
```

---

# 49. Condição para Entrada em Produção

Uma funcionalidade somente deverá ser considerada apta à produção quando:

* critérios P0 aprovados;
* testes críticos aprovados;
* segurança validada;
* integrações críticas validadas;
* rastreabilidade atualizada;
* documentação atualizada;
* pendências críticas inexistentes;
* riscos residuais formalmente tratados.

---

# 50. Gestão de Não Conformidades

Critérios reprovados deverão gerar registro de não conformidade contendo:

* identificador;
* critério afetado;
* descrição;
* severidade;
* evidência;
* responsável;
* ação corretiva;
* prazo;
* situação;
* revalidação.

---

# 51. Severidade

| Severidade | Descrição                                           |
| ---------- | --------------------------------------------------- |
| Crítica    | Impede operação ou compromete segurança/integridade |
| Alta       | Compromete funcionalidade importante                |
| Média      | Impacta operação, mas possui alternativa            |
| Baixa      | Impacto limitado                                    |
| Cosmética  | Não compromete operação                             |

---

# 52. Critério de Pronto

Uma funcionalidade será considerada **Pronta para Homologação** quando:

* implementação concluída;
* testes unitários concluídos;
* testes de integração concluídos;
* documentação atualizada;
* critérios de aceitação preparados;
* evidências disponíveis;
* nenhum bloqueio técnico conhecido.

---

# 53. Critério de Pronto para Produção

Uma funcionalidade será considerada **Pronta para Produção** quando:

* critérios de aceitação aprovados;
* homologação concluída;
* segurança validada;
* desempenho compatível;
* observabilidade configurada;
* backup e recuperação contemplados;
* documentação operacional disponível;
* riscos tratados;
* aprovação formal registrada.

---

# 54. Próximo Artefato

Após este documento, a sequência deverá prosseguir para:

```text
012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
```

Esse documento consolidará:

```text
Atores
↓
Capacidades
↓
Processos
↓
Serviços
↓
Casos de Uso
↓
Histórias de Usuário
↓
Regras de Negócio
↓
Requisitos Funcionais
↓
Requisitos Não Funcionais
↓
Especificações
↓
Critérios de Aceitação
↓
Testes
```

---

# 55. Registro no Mapa Mestre

**Identificador do artefato:**

`CA-MAP-COMPRAS-001`

**Tipo:**

Critérios de Aceitação.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

**Status:**

Vigente.

---

# 56. Controle de Versões

| Versão | Data       | Descrição                                                                         |
| ------ | ---------- | --------------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação dos Critérios de Aceitação do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
