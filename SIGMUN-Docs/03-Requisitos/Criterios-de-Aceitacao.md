# Critérios-de-Aceitacao.md

#### Critérios de Aceitação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Negócio

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000G-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Casos-de-Uso.md
* Modelo-de-Competencias.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md
* 000F-Registro-de-Decisoes-Arquiteturais.md
* 000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md

---

# 1. Objetivo

Este documento estabelece o padrão corporativo para definição, documentação, validação e aprovação dos **Critérios de Aceitação do SIGMUN**.

Os critérios de aceitação têm como finalidade estabelecer, de forma objetiva e verificável, as condições que devem ser atendidas para que um requisito, caso de uso, serviço, funcionalidade ou entrega seja considerado **aceito**.

O documento busca garantir que:

* requisitos sejam verificáveis;
* expectativas sejam explicitadas antes da implementação;
* funcionalidades possam ser testadas objetivamente;
* usuários e equipes técnicas tenham entendimento comum;
* homologações sejam baseadas em evidências;
* defeitos sejam identificados de forma objetiva;
* entregas possam ser rastreadas;
* decisões de aceite sejam auditáveis.

---

# 2. Princípio Fundamental

Nenhuma funcionalidade deverá ser considerada concluída apenas porque foi implementada.

Para ser considerada aceita, deverá existir evidência de que os critérios previamente definidos foram atendidos.

A cadeia de qualidade deverá seguir:

```text
Necessidade
    ↓
Objetivo
    ↓
Processo
    ↓
Serviço
    ↓
Caso de Uso
    ↓
Requisito
    ↓
Critérios de Aceitação
    ↓
Implementação
    ↓
Teste
    ↓
Evidência
    ↓
Homologação
    ↓
Aceite
```

---

# 3. Escopo

Este documento se aplica a:

* requisitos funcionais;
* requisitos não funcionais;
* casos de uso;
* funcionalidades;
* serviços digitais;
* APIs;
* integrações;
* processos automatizados;
* aplicativos móveis;
* portais;
* dashboards;
* relatórios;
* componentes reutilizáveis;
* entregas de software;
* alterações relevantes em funcionalidades existentes.

---

# 4. Definição

## 4.1 Critério de Aceitação

Condição objetiva que deve ser satisfeita para que uma entrega seja considerada aceitável.

Um critério deve permitir responder:

> "Como saberemos, de forma objetiva, que isto está correto?"

---

# 5. Características dos Critérios

Todo critério de aceitação deve ser:

* **claro**;
* **objetivo**;
* **verificável**;
* **mensurável quando aplicável**;
* **testável**;
* **rastreável**;
* **compreensível para o negócio**;
* **independente de detalhes desnecessários de implementação**.

---

# 6. Critérios de Aceitação e Requisitos

Cada requisito relevante deverá possuir critérios de aceitação associados.

Exemplo:

```text
RF-001
  ↓
CA-001.01
CA-001.02
CA-001.03
CA-001.04
```

Onde:

* `RF` = Requisito Funcional;
* `CA` = Critério de Aceitação.

---

# 7. Convenção de Identificação

Os critérios deverão utilizar a seguinte convenção:

```text
CA-[ID DO REQUISITO].[SEQUENCIAL]
```

Exemplo:

```text
RF-001
├── CA-001.01
├── CA-001.02
├── CA-001.03
└── CA-001.04
```

Para casos de uso:

```text
UC-003
├── CA-003.01
├── CA-003.02
└── CA-003.03
```

---

# 8. Estrutura Padrão

Cada requisito deverá possuir, quando aplicável:

```markdown
## RF-XXX – Nome do Requisito

### Critérios de Aceitação

#### CA-XXX.01 – Nome

**Dado que:** condição inicial.

**Quando:** ação realizada.

**Então:** resultado esperado.

#### CA-XXX.02 – Nome

**Dado que:** condição inicial.

**Quando:** ação realizada.

**Então:** resultado esperado.
```

---

# 9. Padrão Given / When / Then

O SIGMUN adotará preferencialmente o padrão:

```text
Dado que
Quando
Então
```

Correspondente ao padrão internacional:

```text
Given
When
Then
```

### Exemplo

```text
Dado que o cidadão possui cadastro válido
Quando solicitar um serviço municipal
Então o SIGMUN deverá registrar a solicitação
e gerar um número de protocolo único.
```

Esse padrão facilita a comunicação entre:

* negócio;
* análise de requisitos;
* desenvolvimento;
* testes;
* usuários;
* homologação.

---

# 10. Tipos de Critérios de Aceitação

Os critérios poderão ser classificados como:

## 10.1 Funcionais

Validam o comportamento funcional.

Exemplo:

```text
Dado que o usuário esteja autenticado
Quando acessar o módulo de processos
Então deverá visualizar somente os processos autorizados.
```

## 10.2 Dados

Validam informações armazenadas ou processadas.

Exemplo:

```text
Dado que uma pessoa seja cadastrada
Quando o cadastro for concluído
Então os dados obrigatórios deverão estar armazenados corretamente.
```

## 10.3 Segurança

Validam controles de segurança.

Exemplo:

```text
Dado que o usuário não possua permissão
Quando tentar acessar determinada funcionalidade
Então o sistema deverá negar o acesso.
```

## 10.4 Auditoria

Validam rastreabilidade.

Exemplo:

```text
Dado que uma informação seja alterada
Quando a alteração for confirmada
Então o SIGMUN deverá registrar usuário, data, hora e alteração realizada.
```

## 10.5 Integração

Validam comunicação com sistemas externos.

## 10.6 Desempenho

Validam tempos de resposta e capacidade.

## 10.7 Disponibilidade

Validam disponibilidade do serviço.

## 10.8 Usabilidade

Validam facilidade e consistência de utilização.

## 10.9 Acessibilidade

Validam atendimento aos requisitos de acessibilidade.

## 10.10 Offline First

Validam funcionamento sem conectividade.

## 10.11 Conformidade

Validam requisitos legais, normativos e institucionais.

---

# 11. Critérios de Aceitação Funcional

Um critério funcional deve responder:

* quem executa;
* qual ação é executada;
* em qual condição;
* qual resultado é esperado.

Exemplo:

```text
Dado que o servidor esteja autenticado
Quando registrar um atendimento
Então o atendimento deverá ser associado ao usuário responsável,
à data, à hora e ao cidadão atendido.
```

---

# 12. Critérios de Dados

Os critérios deverão validar:

* obrigatoriedade;
* formato;
* domínio;
* consistência;
* unicidade;
* integridade;
* relacionamentos;
* histórico;
* origem;
* atualização.

Exemplo:

```text
Dado que o CPF informado já exista no Cadastro Único
Quando o usuário tentar criar um novo cadastro
Então o SIGMUN deverá informar a existência do cadastro
e impedir a criação de duplicidade.
```

---

# 13. Critérios de Segurança

Os critérios de segurança deverão verificar:

* autenticação;
* autorização;
* segregação de funções;
* controle de acesso;
* proteção de dados;
* criptografia quando aplicável;
* auditoria;
* gestão de sessão;
* prevenção contra acessos indevidos.

Exemplo:

```text
Dado que um usuário não possua permissão para consultar determinado processo
Quando tentar acessá-lo
Então o SIGMUN deverá impedir o acesso
e registrar o evento de segurança quando aplicável.
```

---

# 14. Critérios de Proteção de Dados

Quando houver dados pessoais, os critérios deverão considerar:

* finalidade;
* necessidade;
* acesso autorizado;
* minimização;
* rastreabilidade;
* retenção;
* descarte;
* direitos do titular;
* classificação da informação.

Os critérios deverão estar alinhados às políticas corporativas de proteção de dados e segurança da informação.

---

# 15. Critérios de Auditoria

Operações relevantes deverão possuir critérios de rastreabilidade.

Exemplo:

```text
Dado que um servidor altere uma informação relevante
Quando a alteração for concluída
Então o SIGMUN deverá registrar:
- usuário;
- data;
- hora;
- objeto alterado;
- operação realizada;
- origem da operação;
- informações necessárias à auditoria.
```

---

# 16. Critérios de Integração

Para integrações, deverão ser considerados:

* autenticação;
* autorização;
* formato dos dados;
* validação;
* disponibilidade;
* timeout;
* tratamento de erros;
* duplicidade;
* idempotência;
* sincronização;
* logs;
* rastreabilidade.

Exemplo:

```text
Dado que o sistema externo esteja disponível
Quando o SIGMUN enviar uma solicitação válida
Então o sistema externo deverá receber os dados
e o SIGMUN deverá registrar o resultado da operação.
```

---

# 17. Critérios de Offline First

Para funcionalidades móveis que possam operar sem conexão:

```text
Dado que o dispositivo esteja sem conexão
Quando o agente executar uma atividade autorizada
Então os dados deverão ser armazenados localmente
de forma segura.
```

E:

```text
Dado que existam registros pendentes de sincronização
Quando a conexão for restabelecida
Então o SIGMUN deverá sincronizar os registros
e informar o resultado da operação.
```

---

# 18. Critérios de Desempenho

Quando houver requisito de desempenho, os critérios deverão estabelecer valores objetivos.

Exemplo:

```text
Dado que o usuário esteja autenticado
Quando consultar um cadastro
Então a resposta deverá ser apresentada em até X segundos
em condições normais de operação.
```

Os valores de `X` deverão ser definidos pelo requisito correspondente.

---

# 19. Critérios de Disponibilidade

Exemplo:

```text
Dado que o serviço esteja em período normal de operação
Quando um usuário autorizado tentar acessá-lo
Então o serviço deverá estar disponível conforme o SLA definido.
```

---

# 20. Critérios de Usabilidade

Deverão considerar:

* clareza;
* consistência;
* feedback;
* prevenção de erros;
* mensagens compreensíveis;
* redução de etapas desnecessárias;
* acessibilidade;
* experiência nos diferentes dispositivos.

---

# 21. Critérios de Acessibilidade

As funcionalidades deverão observar os padrões de acessibilidade aplicáveis.

Critérios poderão verificar:

* navegação por teclado;
* contraste;
* leitura por tecnologias assistivas;
* identificação de campos;
* mensagens de erro;
* alternativas textuais;
* responsividade;
* acessibilidade em dispositivos móveis.

---

# 22. Critérios de Conformidade

Quando aplicável, os critérios deverão validar conformidade com:

* legislação;
* regulamentos;
* normas técnicas;
* políticas municipais;
* políticas corporativas;
* regras de órgãos de controle;
* requisitos de transparência;
* proteção de dados pessoais.

---

# 23. Critérios de Aceitação de APIs

Uma API deverá possuir critérios relacionados a:

* autenticação;
* autorização;
* contrato;
* versionamento;
* requisição;
* resposta;
* códigos HTTP;
* validação;
* tratamento de erros;
* idempotência;
* auditoria;
* documentação.

---

# 24. Critérios de Aceitação de Relatórios

Relatórios deverão possuir critérios para:

* origem dos dados;
* período;
* filtros;
* cálculos;
* totalizadores;
* permissões;
* exportação;
* atualização;
* consistência.

---

# 25. Critérios de Aceitação de Indicadores

Indicadores deverão possuir critérios relacionados a:

* fórmula;
* fonte;
* periodicidade;
* unidade de medida;
* população;
* filtros;
* período;
* atualização;
* histórico;
* interpretação.

---

# 26. Critérios de Aceitação de Dashboards

Deverão verificar:

* indicadores apresentados;
* filtros;
* atualização;
* permissões;
* consistência;
* responsividade;
* acessibilidade;
* origem dos dados.

---

# 27. Critérios de Aceitação de Documentos

Para documentos oficiais, deverão ser avaliados:

* conteúdo;
* identificação;
* numeração;
* data;
* responsável;
* assinatura;
* autenticidade;
* integridade;
* classificação;
* histórico.

---

# 28. Critérios de Aceitação de Processos

Quando uma funcionalidade automatizar um processo, os critérios deverão validar:

* entrada;
* regras;
* encaminhamento;
* responsáveis;
* prazos;
* transições;
* exceções;
* saída;
* auditoria.

---

# 29. Critérios de Aceitação Negativos

Os testes não deverão verificar apenas o caminho de sucesso.

Também deverão existir critérios para situações inválidas.

Exemplo:

```text
Dado que o CPF informado seja inválido
Quando o usuário tentar concluir o cadastro
Então o SIGMUN deverá rejeitar a informação
e apresentar mensagem orientativa.
```

---

# 30. Critérios de Exceção

Toda situação relevante de exceção deverá possuir comportamento definido.

Exemplos:

* serviço indisponível;
* dados inválidos;
* usuário sem permissão;
* conexão interrompida;
* duplicidade;
* conflito de sincronização;
* prazo expirado;
* documento inválido;
* integração indisponível.

---

# 31. Critérios de Aceitação de Erros

Mensagens de erro deverão:

* ser compreensíveis;
* identificar o problema;
* evitar informações sensíveis;
* orientar o usuário quando possível;
* possuir tratamento adequado no registro técnico.

---

# 32. Critérios de Homologação

A homologação deverá verificar se todos os critérios foram atendidos.

Um requisito somente poderá ser considerado homologado quando:

* todos os critérios obrigatórios estiverem atendidos;
* os testes correspondentes forem executados;
* as evidências estiverem disponíveis;
* defeitos impeditivos estiverem resolvidos;
* o responsável pela homologação aprovar a entrega.

---

# 33. Status dos Critérios

Cada critério deverá possuir um status.

| Status        | Significado                     |
| ------------- | ------------------------------- |
| Não Executado | Ainda não foi testado           |
| Em Teste      | Teste em execução               |
| Aprovado      | Critério atendido               |
| Reprovado     | Critério não atendido           |
| Bloqueado     | Não pode ser executado          |
| Dispensado    | Critério formalmente dispensado |
| Obsoleto      | Critério não mais aplicável     |

---

# 34. Evidências

Cada critério aprovado deverá possuir evidência quando aplicável.

Exemplos:

* captura de tela;
* vídeo;
* relatório;
* log;
* documento;
* resposta de API;
* resultado de teste automatizado;
* registro de auditoria;
* documento assinado;
* resultado de integração.

---

# 35. Matriz de Critérios

| ID        | Requisito | Caso de Uso | Critério              | Tipo      | Teste  | Status        |
| --------- | --------- | ----------- | --------------------- | --------- | ------ | ------------- |
| CA-001.01 | RF-001    | UC-001      | Autenticação válida   | Funcional | CT-001 | Não Executado |
| CA-001.02 | RF-001    | UC-001      | Credencial inválida   | Segurança | CT-002 | Não Executado |
| CA-003.01 | RF-003    | UC-003      | Cadastro válido       | Funcional | CT-003 | Não Executado |
| CA-003.02 | RF-003    | UC-003      | CPF duplicado         | Dados     | CT-004 | Não Executado |
| CA-017.01 | RF-017    | UC-017      | Registro de auditoria | Auditoria | CT-017 | Não Executado |

---

# 36. Critérios e Testes

A relação deverá ser:

```text
Critério de Aceitação
        ↓
Caso de Teste
        ↓
Execução
        ↓
Evidência
        ↓
Resultado
```

Um critério poderá possuir mais de um caso de teste.

Um caso de teste também poderá validar mais de um critério quando houver justificativa.

---

# 37. Critérios e Rastreabilidade

A rastreabilidade corporativa deverá permitir:

```text
Objetivo Estratégico
        ↓
Capacidade
        ↓
Domínio
        ↓
Processo
        ↓
Serviço
        ↓
Caso de Uso
        ↓
Requisito
        ↓
Critério de Aceitação
        ↓
Caso de Teste
        ↓
Evidência
        ↓
Homologação
```

Essa cadeia deverá ser mantida pelo **Framework Corporativo de Gestão de Requisitos e Rastreabilidade**.

---

# 38. Definition of Ready

Antes de um requisito entrar em desenvolvimento, deverá estar suficientemente definido.

Quando aplicável, deverá possuir:

* descrição;
* objetivo;
* ator;
* contexto;
* regras de negócio conhecidas;
* critérios de aceitação;
* dependências identificadas;
* dados necessários;
* integrações identificadas.

---

# 39. Definition of Done

Uma entrega poderá ser considerada concluída quando:

* implementação concluída;
* revisão realizada;
* testes executados;
* critérios atendidos;
* defeitos impeditivos resolvidos;
* documentação atualizada;
* evidências registradas;
* segurança validada quando aplicável;
* homologação realizada;
* rastreabilidade atualizada.

---

# 40. Rejeição de uma Entrega

Uma entrega deverá ser rejeitada quando:

* critério obrigatório não for atendido;
* comportamento divergente for identificado;
* requisito legal não for atendido;
* falha de segurança relevante existir;
* evidência necessária não estiver disponível;
* teste obrigatório falhar;
* documentação essencial estiver ausente.

---

# 41. Alteração de Critérios

Critérios de aceitação não deverão ser alterados informalmente após o início do desenvolvimento.

Alterações deverão considerar:

* motivo;
* impacto;
* requisito afetado;
* caso de uso afetado;
* testes afetados;
* documentação afetada;
* eventual impacto arquitetural.

Alterações significativas deverão ser registradas conforme o processo de gestão de mudanças.

---

# 42. Critérios de Aceitação e Gestão de Mudanças

Quando houver mudança em:

* legislação;
* processo;
* serviço;
* requisito;
* regra de negócio;
* arquitetura;
* integração;
* segurança;

os critérios de aceitação deverão ser reavaliados.

---

# 43. Critérios para Software Legado

Ao modernizar ou substituir funcionalidades existentes, os critérios deverão considerar:

* comportamento atual;
* regras existentes;
* requisitos legais;
* dados históricos;
* integrações;
* compatibilidade;
* melhorias esperadas.

O comportamento legado não deverá ser preservado automaticamente quando contrariar os objetivos arquiteturais ou de negócio aprovados.

---

# 44. Critérios para Desenvolvimento Ágil

Em equipes que utilizem Scrum, Kanban ou métodos ágeis, os critérios de aceitação deverão acompanhar as histórias de usuário.

Exemplo:

```text
Como cidadão
Quero solicitar um serviço municipal
Para acompanhar sua execução.
```

Critérios:

```text
Dado que o cidadão esteja autenticado
Quando preencher os dados obrigatórios
Então a solicitação deverá ser registrada.

Dado que a solicitação tenha sido registrada
Quando o protocolo for gerado
Então o cidadão deverá receber o número do protocolo.
```

---

# 45. Critérios para Desenvolvimento Tradicional

Em projetos conduzidos por etapas, os critérios deverão integrar:

* especificação;
* desenvolvimento;
* testes;
* homologação;
* implantação.

---

# 46. Critérios de Aceitação Corporativos Mínimos

Toda funcionalidade relevante deverá avaliar, conforme aplicabilidade:

* funcionalidade;
* dados;
* segurança;
* auditoria;
* usabilidade;
* acessibilidade;
* desempenho;
* integração;
* conformidade;
* tratamento de erros.

---

# 47. Governança

A definição dos critérios deverá envolver, conforme a natureza do requisito:

* área de negócio;
* analista de requisitos;
* arquitetura;
* desenvolvimento;
* segurança;
* dados;
* UX;
* qualidade;
* usuário responsável pela homologação.

Nenhum critério deverá ser criado de forma incompatível com regras de negócio, requisitos legais ou políticas corporativas.

---

# 48. Responsabilidades

## Área de Negócio

Define o resultado esperado.

## Analista de Requisitos

Formaliza os critérios.

## Arquitetura

Avalia impactos arquiteturais.

## Desenvolvimento

Implementa o comportamento esperado.

## Qualidade

Define e executa os testes necessários.

## Segurança

Avalia critérios relacionados à segurança.

## Dados

Avalia critérios relacionados à integridade e qualidade dos dados.

## Usuário Homologador

Valida o atendimento às necessidades de negócio.

---

# 49. Indicadores de Qualidade

O SIGMUN poderá acompanhar indicadores como:

* percentual de requisitos com critérios definidos;
* percentual de critérios aprovados;
* percentual de critérios reprovados;
* taxa de retrabalho;
* defeitos encontrados na homologação;
* defeitos encontrados em produção;
* requisitos sem evidência;
* tempo médio de homologação;
* percentual de requisitos rastreáveis.

---

# 50. Modelo Corporativo Resumido

O padrão recomendado para novos critérios é:

```text
CA-XXX.XX – Nome

Dado que [condição inicial]

Quando [ação/evento]

Então [resultado esperado]
```

Quando necessário:

```text
E [resultado complementar]
```

---

# 51. Exemplo Completo

## RF-003 – Cadastro de Pessoa

### CA-003.01 – Cadastro válido

**Dado que** o cidadão forneça todos os dados obrigatórios válidos

**Quando** confirmar o cadastro

**Então** o SIGMUN deverá registrar a pessoa no Cadastro Único Municipal

**E** deverá gerar ou identificar seu identificador único.

### CA-003.02 – Cadastro duplicado

**Dado que** já exista pessoa cadastrada com o mesmo identificador oficial

**Quando** o usuário tentar realizar novo cadastro

**Então** o SIGMUN deverá impedir a duplicidade

**E** deverá apresentar o cadastro existente conforme as permissões aplicáveis.

### CA-003.03 – Auditoria

**Dado que** o cadastro seja criado ou alterado

**Quando** a operação for concluída

**Então** o SIGMUN deverá registrar a operação para fins de auditoria.

---

# 52. Evolução

Este documento deverá evoluir conjuntamente com:

* Framework de Requisitos;
* Casos de Uso;
* Regras de Negócio;
* Modelo de Testes;
* Arquitetura;
* Políticas de Segurança;
* Políticas de Dados;
* Gestão de Mudanças;
* Gestão de Qualidade.

---

# 53. Disposição Final

Os critérios de aceitação constituem o **contrato verificável entre necessidade de negócio e entrega de software**.

O SIGMUN deverá evitar a definição de funcionalidades baseada exclusivamente em descrições subjetivas como:

* "deve funcionar corretamente";
* "deve ser rápido";
* "deve ser fácil";
* "deve permitir consultar";
* "deve atender ao usuário".

Sempre que possível, essas afirmações deverão ser transformadas em condições **objetivas, verificáveis e testáveis**.

O princípio corporativo será:

> **Se não conseguimos definir como verificar, ainda não definimos adequadamente o que deve ser entregue.**

---

**Documento:** Critérios-de-Aceitacao.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
