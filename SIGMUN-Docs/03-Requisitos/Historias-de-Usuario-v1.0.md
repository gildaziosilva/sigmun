# Histórias de Usuário

#### Histórias de Usuário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL-v1.0.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000E-GUIA-DE-CONTRIBUICAO.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
* Cadeia-de-Valor-v1.1.md
* Mapa-de-Atores-v1.0.md
* Mapa-de-Capacidades-v1.0.md
* Mapa-de-Dominios-v1.0.md
* Mapa-de-Processos-v1.0.md
* Mapa-de-Servicos-v1.0.md
* Modelo-de-Competencias-v1.0.md
* Modelo-de-Governanca-Administrativa-v1.0.md
* Glossario-de-Negocio-v1.0.md
* Casos-de-Uso-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md

---

# 1. Finalidade

Este documento estabelece o padrão corporativo para elaboração, identificação, organização, validação, priorização, rastreabilidade e manutenção das **Histórias de Usuário do SIGMUN**.

As Histórias de Usuário representam necessidades ou expectativas de usuários e partes interessadas sob uma perspectiva orientada ao valor produzido.

Seu objetivo é facilitar a comunicação entre:

* usuários;
* áreas de negócio;
* analistas;
* produto;
* arquitetura;
* desenvolvimento;
* testes;
* gestão;
* demais participantes do projeto.

As Histórias de Usuário não substituem requisitos, especificações, casos de uso ou critérios de aceitação.

Elas constituem um mecanismo complementar para representar necessidades de forma compreensível e orientada ao valor.

---

# 2. Objetivos

As Histórias de Usuário deverão contribuir para:

* compreender necessidades reais;
* representar valor para o usuário;
* facilitar comunicação;
* apoiar priorização;
* orientar detalhamento de requisitos;
* apoiar planejamento;
* facilitar validação;
* apoiar testes;
* preservar contexto;
* manter rastreabilidade;
* reduzir ambiguidades.

---

# 3. Princípios

As Histórias de Usuário deverão observar:

* foco no usuário;
* foco no valor;
* clareza;
* simplicidade;
* independência sempre que possível;
* testabilidade;
* rastreabilidade;
* colaboração;
* evolução contínua;
* alinhamento ao negócio.

---

# 4. Posição na Hierarquia Documental

As Histórias de Usuário integram o domínio de Requisitos e Especificações.

A cadeia poderá ser representada como:

```text
Objetivo Estratégico
        ↓
Capacidade
        ↓
Processo
        ↓
Serviço
        ↓
Ator
        ↓
História de Usuário
        ↓
Requisito
        ↓
Especificação
        ↓
Critério de Aceitação
        ↓
Teste
```

Uma História de Usuário poderá também originar ou complementar um Caso de Uso.

---

# 5. Definição

Uma História de Usuário é uma descrição curta de uma necessidade sob a perspectiva de um determinado usuário ou papel, indicando:

* quem necessita;
* o que necessita;
* por que necessita;
* qual valor espera obter.

---

# 6. Estrutura Fundamental

O formato padrão será:

```text
Como <papel>,
quero <objetivo ou capacidade>,
para <benefício ou valor>.
```

Exemplo:

```text
Como servidor responsável pelo cadastro de fornecedores,
quero consultar os dados cadastrais de um fornecedor,
para verificar suas informações antes de iniciar uma contratação.
```

---

# 7. Identificação

Cada História de Usuário deverá possuir identificador único.

Formato recomendado:

```text
HU-<DOMÍNIO>-<NÚMERO>
```

Exemplos:

```text
HU-COMPRAS-001
HU-TRIBUTOS-001
HU-SAUDE-001
HU-EDUCACAO-001
HU-RH-001
```

O identificador não deverá ser reutilizado.

---

# 8. Nome da História

O nome deverá ser curto e representar claramente a necessidade.

Exemplo:

```text
HU-COMPRAS-001 – Consultar Fornecedor
```

Evitar nomes vagos:

```text
HU-COMPRAS-001 – Tela de fornecedor
HU-COMPRAS-001 – Melhorar cadastro
```

---

# 9. Papel do Usuário

O papel deverá representar quem obtém o valor da funcionalidade.

Exemplos:

* servidor municipal;
* gestor;
* fiscal;
* cidadão;
* fornecedor;
* profissional de saúde;
* professor;
* administrador;
* auditor;
* responsável por processo.

Quando apropriado, deverá ser utilizado um papel previamente definido no **Mapa de Atores** ou no **Modelo de Competências**.

---

# 10. Objetivo

Deverá indicar o que o usuário deseja realizar.

O objetivo deverá representar uma capacidade ou resultado, e não simplesmente uma característica técnica.

Preferir:

```text
quero acompanhar a situação da solicitação
```

em vez de:

```text
quero um botão de acompanhamento
```

---

# 11. Valor

O campo "para" deverá representar o benefício esperado.

Exemplo:

```text
para saber se a solicitação já foi analisada.
```

O valor deverá estar relacionado ao resultado do negócio ou à necessidade do usuário.

---

# 12. Critérios de Qualidade

Uma História de Usuário deverá, quando possível, atender ao conceito de qualidade conhecido como INVEST:

* **I – Independente**
* **N – Negociável**
* **V – Valiosa**
* **E – Estimável**
* **S – Pequena**
* **T – Testável**

O INVEST deverá ser utilizado como orientação, não como regra mecânica.

---

# 13. Independência

Uma História deverá possuir o mínimo possível de dependências com outras histórias.

Quando uma dependência for inevitável, deverá ser registrada.

---

# 14. Negociabilidade

A História de Usuário não deverá ser tratada automaticamente como uma especificação técnica definitiva.

Ela representa uma necessidade que poderá ser detalhada por meio de colaboração entre negócio, produto, arquitetura e equipe técnica.

---

# 15. Valor

Toda História deverá possuir valor identificável.

Histórias puramente técnicas deverão ser tratadas como tarefas técnicas, requisitos técnicos, débito técnico ou outro artefato apropriado, quando não houver benefício de negócio identificável.

---

# 16. Estimabilidade

A História deverá possuir informação suficiente para permitir estimativa.

Quando não for possível estimar, deverá ser identificada a necessidade de investigação ou refinamento.

---

# 17. Tamanho

Uma História deverá ser suficientemente pequena para ser compreendida, estimada, desenvolvida e testada dentro do ciclo de trabalho aplicável.

Histórias excessivamente grandes deverão ser decompostas.

---

# 18. Testabilidade

Uma História deverá possuir critérios de aceitação verificáveis.

Exemplo:

```text
Dado que o usuário esteja autenticado,
quando consultar um fornecedor existente,
então os dados autorizados deverão ser apresentados.
```

---

# 19. Critérios de Aceitação

Os critérios de aceitação deverão complementar a História de Usuário.

A História descreve a necessidade.

Os critérios descrevem como verificar se a necessidade foi atendida.

Exemplo:

```text
HU-COMPRAS-001 – Consultar Fornecedor

Como servidor responsável pelas contratações,
quero consultar os dados de um fornecedor,
para verificar suas informações antes de iniciar uma contratação.

Critérios:

CA-001 – O sistema deverá permitir localizar fornecedor por CNPJ.

CA-002 – O sistema deverá apresentar somente dados aos quais o usuário
possua permissão de acesso.

CA-003 – O sistema deverá informar quando nenhum fornecedor for encontrado.
```

---

# 20. Formato Dado-Quando-Então

Quando apropriado, os critérios poderão utilizar:

```text
Dado que <contexto>,
quando <ação>,
então <resultado esperado>.
```

Exemplo:

```text
Dado que o fornecedor esteja cadastrado,
quando o usuário informar o CNPJ correto,
então o sistema deverá apresentar o cadastro correspondente.
```

---

# 21. Relação com Casos de Uso

Uma História de Usuário poderá estar relacionada a um Caso de Uso.

Exemplo:

```text
HU-COMPRAS-001
        ↓
UC-COMPRAS-003 – Consultar Fornecedor
```

Uma História poderá:

* originar um Caso de Uso;
* representar parte de um Caso de Uso;
* complementar um Caso de Uso existente.

---

# 22. Relação com Requisitos

Uma História de Usuário poderá originar um ou mais requisitos.

Exemplo:

```text
HU-COMPRAS-001
       ↓
RF-COMPRAS-001
RF-COMPRAS-002
```

A relação deverá ser explicitamente registrada.

---

# 23. Relação com Especificações

Quando o requisito derivado precisar de detalhamento, poderá ser relacionado a uma ou mais especificações.

Exemplo:

```text
HU-COMPRAS-001
       ↓
RF-COMPRAS-001
       ↓
ESP-COMPRAS-001
```

---

# 24. Relação com Testes

A História deverá poder ser rastreada até os testes correspondentes.

Exemplo:

```text
HU-COMPRAS-001
       ↓
CA-001
       ↓
TEST-COMPRAS-001
```

---

# 25. Relação com Processos

Quando aplicável, deverá ser indicado o processo de negócio relacionado.

Exemplo:

```text
**Processo:** Gestão de Contratações
```

---

# 26. Relação com Serviços

Quando aplicável, deverá ser indicado o serviço municipal relacionado.

Exemplo:

```text
**Serviço:** Gestão de Fornecedores
```

---

# 27. Relação com Capacidades

Quando aplicável, deverá ser indicada a capacidade organizacional relacionada.

Exemplo:

```text
**Capacidade:** Gestão de Contratações
```

---

# 28. Relação com Atores

O papel da História deverá estar relacionado aos atores definidos no modelo corporativo quando possível.

Exemplo:

```text
**Ator:** Servidor Municipal
```

---

# 29. Prioridade

Cada História deverá possuir prioridade quando estiver sendo utilizada para planejamento.

Sugestão:

```text
Crítica
Alta
Média
Baixa
```

A prioridade deverá refletir valor, urgência, risco, obrigação legal ou dependências.

---

# 30. Valor de Negócio

Quando aplicável, deverá ser registrado o valor de negócio.

Exemplos:

* redução de tempo;
* redução de retrabalho;
* conformidade;
* melhoria do serviço;
* transparência;
* redução de custo;
* aumento de controle;
* melhoria da experiência do cidadão.

---

# 31. Risco

Histórias relacionadas a riscos relevantes deverão registrar o risco associado.

Exemplo:

```text
**Risco:** atraso na implantação do processo de contratação.
```

---

# 32. Dependências

Deverão ser registradas dependências relevantes.

Exemplo:

```text
**Dependências:**

- Cadastro Único Municipal;
- Gestão de Identidade;
- Cadastro de Fornecedores.
```

---

# 33. Premissas

Quando necessário, deverão ser registradas premissas.

Exemplo:

```text
**Premissa:**
O usuário deverá possuir identidade municipal válida.
```

---

# 34. Restrições

Deverão ser registradas restrições relevantes.

Exemplos:

* legislação;
* segurança;
* orçamento;
* infraestrutura;
* interoperabilidade;
* disponibilidade de dados;
* políticas municipais.

---

# 35. Regras de Negócio

Quando uma História depender de regras de negócio, deverá indicar as regras relacionadas.

Exemplo:

```text
RN-COMPRAS-003 – Somente fornecedores ativos poderão ser selecionados
para novas contratações.
```

As regras deverão ser mantidas como artefatos rastreáveis quando forem reutilizadas.

---

# 36. Dados

Quando aplicável, deverá indicar os dados utilizados.

Exemplos:

* CPF;
* CNPJ;
* endereço;
* matrícula;
* processo;
* contrato;
* protocolo.

Dados pessoais deverão ser tratados conforme as políticas de segurança e proteção de dados do SIGMUN.

---

# 37. Segurança

Histórias que envolvam operações protegidas deverão indicar requisitos de acesso.

Exemplo:

```text
Somente usuários com permissão de consulta de fornecedores
poderão acessar os dados cadastrais.
```

---

# 38. Privacidade

Quando envolver dados pessoais, deverá ser avaliado:

* finalidade;
* necessidade;
* acesso;
* compartilhamento;
* retenção;
* proteção;
* auditoria.

---

# 39. Auditoria

Histórias que envolvam alterações relevantes deverão considerar a necessidade de auditoria.

Exemplo:

```text
Toda alteração cadastral deverá registrar usuário,
data, hora e operação realizada.
```

---

# 40. Interface

A História não deverá definir prematuramente a solução visual.

Quando a interface for relevante, poderá indicar a necessidade funcional sem restringir desnecessariamente a solução.

Preferir:

```text
quero acompanhar o andamento da solicitação
```

em vez de:

```text
quero um botão azul no canto superior direito.
```

---

# 41. Dispositivos Móveis

Quando a História for destinada a atividades de campo, deverá indicar essa condição.

Poderão ser considerados:

* smartphone;
* tablet;
* dispositivo corporativo;
* captura offline;
* sincronização;
* evidências;
* localização;
* câmera.

---

# 42. Offline First

Para atividades de campo, a História deverá considerar, quando aplicável:

```text
Como agente de campo,
quero registrar uma visita mesmo sem conexão,
para continuar realizando o trabalho quando estiver em área sem internet.
```

Os requisitos técnicos de sincronização deverão ser detalhados em artefatos apropriados.

---

# 43. Evidências

Quando a História envolver comprovação de execução, poderão ser consideradas:

* fotografia;
* assinatura;
* localização;
* data;
* hora;
* documento;
* formulário;
* leitura de equipamento.

---

# 44. Notificações

Quando houver necessidade de comunicação, a História poderá especificar o resultado esperado.

Exemplo:

```text
Como gestor,
quero ser notificado quando uma solicitação estiver pronta para aprovação,
para analisar a solicitação dentro do prazo.
```

O canal específico deverá ser definido posteriormente quando apropriado.

---

# 45. História Técnica

Nem toda necessidade deverá ser transformada artificialmente em História de Usuário.

Itens técnicos poderão ser representados como:

* requisito técnico;
* especificação técnica;
* tarefa;
* débito técnico;
* melhoria arquitetural;
* ADR.

Uma História Técnica somente deverá ser utilizada quando houver benefício compreensível relacionado ao sistema ou ao produto.

---

# 46. Épicos

Histórias muito grandes poderão ser agrupadas em Épicos.

Exemplo:

```text
ÉPICO: Gestão de Contratos

    HU-CONTRATOS-001 – Cadastrar contrato
    HU-CONTRATOS-002 – Consultar contrato
    HU-CONTRATOS-003 – Alterar contrato
    HU-CONTRATOS-004 – Acompanhar vigência
    HU-CONTRATOS-005 – Encerrar contrato
```

---

# 47. Decomposição

Quando uma História for grande demais, poderá ser decomposta por:

* fluxo;
* regra;
* papel;
* resultado;
* dados;
* variação do processo;
* prioridade;
* cenário.

A decomposição deverá preservar o valor de negócio.

---

# 48. Exemplo de Decomposição

História original:

```text
Como gestor,
quero gerenciar contratos,
para acompanhar sua execução.
```

Possíveis histórias menores:

```text
HU-CONTRATOS-001 – Consultar contrato
HU-CONTRATOS-002 – Registrar contrato
HU-CONTRATOS-003 – Acompanhar vigência
HU-CONTRATOS-004 – Registrar execução
HU-CONTRATOS-005 – Encerrar contrato
```

---

# 49. Refinamento

As Histórias poderão evoluir durante o ciclo de análise.

O refinamento poderá acrescentar:

* critérios;
* regras;
* dependências;
* exemplos;
* exceções;
* dados;
* riscos;
* restrições.

O refinamento não deverá eliminar a rastreabilidade da História original.

---

# 50. Estado da História

As Histórias poderão possuir os seguintes estados:

```text
Proposta
Em Refinamento
Pronta
Priorizada
Em Desenvolvimento
Em Teste
Aceita
Rejeitada
Cancelada
Superada
```

---

# 51. Definition of Ready

Quando utilizado no processo de desenvolvimento, uma História poderá ser considerada **Pronta** quando:

* possui identificador;
* possui usuário/papel;
* possui objetivo;
* possui valor;
* possui contexto suficiente;
* possui critérios de aceitação;
* possui dependências conhecidas;
* possui informações suficientes para estimativa.

---

# 52. Definition of Done

Uma História poderá ser considerada concluída quando:

* implementação concluída;
* testes executados;
* critérios de aceitação atendidos;
* segurança validada quando aplicável;
* documentação atualizada quando necessária;
* evidências registradas;
* aceite realizado.

---

# 53. Priorização

A priorização deverá considerar:

* valor público;
* valor para o usuário;
* obrigação legal;
* urgência;
* risco;
* dependências;
* esforço;
* impacto;
* disponibilidade de recursos.

---

# 54. Valor Público

No contexto municipal, o valor deverá considerar não apenas o usuário interno, mas também o cidadão e o interesse público.

Exemplos:

* melhoria do atendimento;
* transparência;
* redução de burocracia;
* redução de deslocamentos;
* maior eficiência;
* inclusão;
* acesso a serviços;
* controle social.

---

# 55. Critérios de Priorização

Quando necessário, poderá ser utilizado:

```text
Valor Público
Valor para o Usuário
Urgência
Risco
Obrigação Legal
Complexidade
Dependência
```

A metodologia específica de priorização deverá ser definida pelo processo de gestão de requisitos/produto aplicável.

---

# 56. Rastreabilidade Corporativa

Cada História relevante deverá permitir rastrear:

```text
Objetivo
   ↓
Capacidade
   ↓
Processo
   ↓
Serviço
   ↓
Ator
   ↓
História de Usuário
   ↓
Requisito
   ↓
Especificação
   ↓
Critério de Aceitação
   ↓
Teste
   ↓
Entrega
```

---

# 57. Matriz de Rastreabilidade

Exemplo:

| Elemento      | ID       | Relação            |
| ------------- | -------- | ------------------ |
| Objetivo      | OBJ-001  | Contribui          |
| Capacidade    | CAP-001  | Utiliza            |
| Processo      | PROC-001 | Apoia              |
| Serviço       | SERV-001 | Melhora            |
| Ator          | ATOR-001 | Representa         |
| História      | HU-001   | Define necessidade |
| Requisito     | RF-001   | Deriva             |
| Especificação | ESP-001  | Detalha            |
| Critério      | CA-001   | Valida             |
| Teste         | TEST-001 | Verifica           |

---

# 58. Gestão de Mudanças

Alterações em Histórias deverão considerar impacto em:

* requisitos;
* especificações;
* critérios de aceitação;
* testes;
* processos;
* dados;
* integrações;
* arquitetura.

---

# 59. Quando uma História Exige ADR

Uma História de Usuário não deverá gerar automaticamente um ADR.

Entretanto, uma decisão arquitetural decorrente de sua implementação poderá exigir registro no:

```text
000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
```

---

# 60. Qualidade

Uma História deverá ser revisada quanto a:

* clareza;
* valor;
* completude;
* consistência;
* testabilidade;
* rastreabilidade;
* ausência de ambiguidade.

---

# 61. Checklist

Antes de considerar uma História pronta:

* [ ] Possui ID?
* [ ] Possui nome?
* [ ] Identifica o usuário?
* [ ] Identifica o objetivo?
* [ ] Identifica o valor?
* [ ] Está relacionada a um processo quando aplicável?
* [ ] Está relacionada a um serviço quando aplicável?
* [ ] Está relacionada a um ator?
* [ ] Possui critérios de aceitação?
* [ ] É testável?
* [ ] Possui dependências conhecidas?
* [ ] Possui restrições relevantes?
* [ ] Possui regras de negócio relacionadas?
* [ ] Considera segurança quando aplicável?
* [ ] Considera privacidade quando aplicável?
* [ ] Possui rastreabilidade?
* [ ] Possui prioridade quando necessário?

---

# 62. Modelo Corporativo

O modelo padrão será:

```markdown
# HU-XXXX-001 – Nome da História

#### Nome da História

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** HU-XXXX-001

**Versão:** 1.0

**Status:** Proposta

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- <Documento>

---

# 1. História

**Como** <papel>,

**quero** <objetivo>,

**para** <valor>.

# 2. Contexto

<Contexto>

# 3. Ator / Papel

<Ator>

# 4. Processo Relacionado

<Processo>

# 5. Serviço Relacionado

<Serviço>

# 6. Capacidade Relacionada

<Capacidade>

# 7. Requisitos Relacionados

<Requisitos>

# 8. Regras de Negócio

<Regras>

# 9. Critérios de Aceitação

### CA-001

Dado que <contexto>,

quando <ação>,

então <resultado>.

# 10. Dependências

<Dependências>

# 11. Restrições

<Restrições>

# 12. Segurança

<Segurança>

# 13. Privacidade

<Privacidade>

# 14. Dados

<Dados>

# 15. Riscos

<Riscos>

# 16. Prioridade

<Prioridade>

# 17. Rastreabilidade

<Rastreabilidade>

# 18. Testes

<Testes>

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |

---

**Documento:** HU-XXXX-001-v1.0.md

**Última atualização:** AAAA-MM-DD

**Responsável:** Equipe SIGMUN

**Status da revisão:** <Status>
```

---

# 63. Exemplo Completo

## HU-COMPRAS-001 – Consultar Fornecedor

**Como** servidor responsável pelas contratações,

**quero** consultar os dados cadastrais de um fornecedor,

**para** verificar suas informações antes de iniciar uma contratação.

### Contexto

A consulta será utilizada durante o processo de contratação municipal.

### Processo

Gestão de Contratações.

### Serviço

Gestão de Fornecedores.

### Critérios de Aceitação

**CA-001**

Dado que o usuário esteja autenticado e autorizado,

quando informar um CNPJ válido,

então o sistema deverá localizar o fornecedor correspondente.

**CA-002**

Dado que o fornecedor exista,

quando a consulta for realizada,

então o sistema deverá apresentar os dados permitidos ao usuário.

**CA-003**

Dado que o fornecedor não exista,

quando a consulta for realizada,

então o sistema deverá informar que nenhum fornecedor foi localizado.

### Segurança

O acesso deverá respeitar as permissões atribuídas ao usuário.

### Auditoria

Quando a política de auditoria determinar, a consulta deverá ser registrada.

### Rastreabilidade

```text
Processo
  ↓
Gestão de Contratações

Serviço
  ↓
Gestão de Fornecedores

História
  ↓
HU-COMPRAS-001

Requisito
  ↓
RF-COMPRAS-001

Especificação
  ↓
ESP-COMPRAS-001

Critérios
  ↓
CA-001
CA-002
CA-003

Teste
  ↓
TEST-COMPRAS-001
```

---

# 64. Relação com o Framework de Requisitos

As Histórias de Usuário deverão ser gerenciadas em conformidade com:

```text
000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
```

O Framework estabelece o processo de gestão.

Este documento estabelece o padrão para Histórias de Usuário.

---

# 65. Regra Fundamental

Toda História de Usuário deverá responder:

> **Quem precisa?**

> **O que precisa?**

> **Por que precisa?**

> **Como saberemos que foi atendido?**

---

# 66. Disposições Finais

As Histórias de Usuário constituem um mecanismo de comunicação entre o negócio e as equipes responsáveis pela evolução do SIGMUN.

Elas deverão ser utilizadas para representar necessidades de forma simples e orientada ao valor, sem substituir os demais artefatos formais de requisitos e arquitetura.

A qualidade de uma História será determinada não apenas pela sua redação, mas pela capacidade de manter uma cadeia de rastreabilidade completa até a entrega e validação do resultado.

No SIGMUN, a História de Usuário deverá contribuir para garantir que cada funcionalidade implementada possua uma justificativa de negócio, um usuário ou parte interessada identificável e um resultado verificável.

---

# Controle de Versões

| Versão | Data       | Descrição                                             |
| ------ | ---------- | ----------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do padrão corporativo de Histórias de Usuário |

---

**Documento:** Historias-de-Usuario-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
