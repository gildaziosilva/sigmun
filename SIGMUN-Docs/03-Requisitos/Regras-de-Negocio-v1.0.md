# Regras de Negócio

#### Regras de Negócio

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
* Historias-de-Usuario-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md
* Matriz-de-Rastreabilidade-v1.0.md

---

# 1. Finalidade

Este documento estabelece o padrão corporativo para identificação, documentação, classificação, validação, rastreabilidade, implementação e manutenção das **Regras de Negócio do SIGMUN**.

As Regras de Negócio representam políticas, condições, restrições, cálculos, critérios, obrigações e decisões que determinam como os processos municipais devem funcionar.

Elas constituem conhecimento do negócio e não devem ser confundidas com a implementação técnica utilizada para executá-las.

---

# 2. Objetivos

As Regras de Negócio deverão permitir:

* formalizar o conhecimento institucional;
* preservar regras administrativas;
* reduzir ambiguidades;
* orientar requisitos;
* orientar desenvolvimento;
* orientar testes;
* apoiar auditoria;
* facilitar mudanças;
* preservar conformidade;
* garantir consistência entre módulos;
* evitar duplicação de regras;
* permitir rastreabilidade.

---

# 3. Princípios

As Regras de Negócio deverão observar:

* clareza;
* objetividade;
* atomicidade;
* verificabilidade;
* rastreabilidade;
* consistência;
* independência tecnológica;
* reutilização;
* versionamento;
* governança.

---

# 4. Definição

Uma Regra de Negócio é uma declaração que define, restringe, orienta ou condiciona uma decisão, atividade, comportamento ou resultado do negócio municipal.

Exemplo:

```text
Somente fornecedores com cadastro ativo poderão ser utilizados
em novas contratações.
```

A regra existe independentemente de como o sistema será implementado.

---

# 5. Regra de Negócio x Requisito

Regra de Negócio e Requisito são conceitos relacionados, mas distintos.

### Regra de Negócio

Define **o que deve ser obedecido pelo negócio**.

### Requisito

Define **o que a solução deverá fazer ou atender** para suportar o negócio.

Exemplo:

```text
Regra de Negócio:

Somente fornecedores ativos podem participar de novas contratações.

Requisito:

O sistema deverá impedir a seleção de fornecedores inativos
em novas contratações.
```

---

# 6. Regra de Negócio x Implementação

Uma Regra de Negócio não deverá ser definida por uma implementação técnica.

Evitar:

```text
O sistema deverá executar a função validarFornecedor().
```

Preferir:

```text
Somente fornecedores com situação cadastral ativa poderão
ser utilizados em novas contratações.
```

A implementação poderá mudar sem alterar a regra.

---

# 7. Categorias de Regras

As regras poderão ser classificadas em:

* políticas;
* restrições;
* condições;
* validações;
* cálculos;
* classificações;
* elegibilidade;
* autorização;
* temporalidade;
* sequenciamento;
* obrigatoriedade;
* derivação;
* exceção;
* conformidade legal.

---

# 8. Regras de Política

Definem orientações institucionais.

Exemplo:

```text
Toda contratação deverá observar os procedimentos
estabelecidos pela legislação e pelas políticas municipais aplicáveis.
```

---

# 9. Regras de Restrição

Impedem determinada ação em condições específicas.

Exemplo:

```text
Um processo não poderá ser encerrado enquanto houver
pendências obrigatórias não resolvidas.
```

---

# 10. Regras de Condição

Definem comportamento condicionado.

Exemplo:

```text
Se o valor da contratação ultrapassar o limite definido
pela legislação aplicável, deverá ser iniciado o fluxo
de aprovação correspondente.
```

---

# 11. Regras de Validação

Determinam condições que um dado ou operação deverá atender.

Exemplo:

```text
O CNPJ informado deverá possuir formato válido.
```

---

# 12. Regras de Cálculo

Definem fórmulas ou critérios de cálculo.

Exemplo:

```text
O valor total deverá corresponder à soma dos valores
dos itens da contratação.
```

A fórmula oficial deverá ser documentada quando necessária.

---

# 13. Regras de Classificação

Determinam como elementos deverão ser classificados.

Exemplo:

```text
Os municípios deverão ser classificados por porte
conforme os critérios definidos pela metodologia institucional aplicável.
```

---

# 14. Regras de Elegibilidade

Determinam quem ou o que pode participar de determinado processo.

Exemplo:

```text
Somente servidores com vínculo ativo poderão participar
do procedimento definido.
```

---

# 15. Regras de Autorização

Determinam quem poderá executar determinada operação.

Exemplo:

```text
Somente usuários com perfil autorizado poderão aprovar
a etapa correspondente do processo.
```

---

# 16. Regras Temporais

Determinam condições relacionadas a datas ou períodos.

Exemplo:

```text
A solicitação deverá ser apresentada dentro do prazo
definido para o procedimento.
```

---

# 17. Regras de Sequenciamento

Determinam a ordem das atividades.

Exemplo:

```text
A aprovação deverá ocorrer antes da emissão da ordem
correspondente.
```

---

# 18. Regras de Obrigatoriedade

Determinam elementos que necessariamente deverão existir.

Exemplo:

```text
Toda contratação deverá possuir fornecedor identificado.
```

---

# 19. Regras de Derivação

Definem como uma informação é obtida a partir de outras.

Exemplo:

```text
O valor total do contrato será derivado da soma dos
valores contratados para seus itens.
```

---

# 20. Regras de Exceção

Definem situações que alteram o comportamento normal.

Exemplo:

```text
Em situações excepcionais previstas em legislação,
poderá ser utilizado procedimento específico.
```

A exceção deverá possuir justificativa e fundamento identificável.

---

# 21. Regras Legais

Quando uma regra decorrer de legislação, deverá ser registrada sua origem.

Exemplo:

```text
**Fundamento:**
Lei / Decreto / Regulamento / Norma aplicável.
```

A regra deverá ser atualizada quando houver alteração normativa relevante.

---

# 22. Identificação

Cada regra deverá possuir identificador único.

Formato recomendado:

```text
RN-<DOMÍNIO>-<NÚMERO>
```

Exemplos:

```text
RN-COMPRAS-001
RN-TRIBUTOS-001
RN-RH-001
RN-SAUDE-001
RN-EDUCACAO-001
```

---

# 23. Nome da Regra

O nome deverá ser curto e representar claramente a regra.

Exemplo:

```text
RN-COMPRAS-001 – Fornecedor Ativo
```

---

# 24. Enunciado

O enunciado deverá ser objetivo, afirmativo e verificável.

Preferir:

```text
Somente fornecedores ativos poderão ser selecionados
para novas contratações.
```

Evitar:

```text
Talvez o sistema possa verificar se o fornecedor está ativo.
```

---

# 25. Contexto

Toda regra relevante deverá possuir contexto suficiente para que seja compreendida.

Exemplo:

```text
A regra aplica-se à seleção de fornecedores durante
a criação de novas contratações.
```

---

# 26. Escopo

Deverá ser indicado onde a regra se aplica.

Exemplos:

```text
**Escopo:** Gestão de Contratações
```

ou:

```text
**Escopo:** Município / Secretaria / Processo / Serviço
```

---

# 27. Fonte da Regra

A origem deverá ser registrada quando conhecida.

Possíveis fontes:

* legislação;
* regulamento;
* política;
* procedimento;
* contrato;
* decisão administrativa;
* norma interna;
* conhecimento institucional;
* requisito estratégico.

---

# 28. Fundamento Legal

Quando aplicável, deverá ser registrado:

* norma;
* artigo;
* inciso;
* parágrafo;
* órgão emissor;
* data;
* versão.

Exemplo:

```text
**Fundamento Legal:**
<Norma aplicável>
```

---

# 29. Proprietário da Regra

Cada regra deverá possuir, quando possível, um responsável pelo negócio.

Exemplo:

```text
**Proprietário:** Secretaria responsável pelo processo.
```

O proprietário deverá possuir autoridade para validar a regra.

---

# 30. Responsável pela Manutenção

Deverá ser indicado quem mantém o registro atualizado.

Exemplo:

```text
**Responsável pela manutenção:** Área de Processos / Requisitos.
```

---

# 31. Prioridade

Quando necessário, a regra poderá possuir prioridade:

```text
Crítica
Alta
Média
Baixa
```

Regras legais ou de segurança poderão ser classificadas como críticas conforme o contexto.

---

# 32. Criticidade

A criticidade poderá considerar:

* impacto legal;
* impacto financeiro;
* impacto operacional;
* impacto ao cidadão;
* impacto à segurança;
* impacto à privacidade;
* risco institucional.

---

# 33. Versionamento

As regras deverão possuir controle de versão.

Exemplo:

```text
RN-COMPRAS-001
Versão: 1.2
```

Uma alteração que modifique o significado da regra deverá gerar nova versão.

---

# 34. Histórico

Cada regra deverá manter histórico.

| Versão | Data       | Alteração   | Responsável      |
| ------ | ---------- | ----------- | ---------------- |
| 1.0    | AAAA-MM-DD | Criação     | Equipe SIGMUN    |
| 1.1    | AAAA-MM-DD | Atualização | Área responsável |

---

# 35. Estado

As regras poderão possuir os seguintes estados:

```text
Proposta
Em Validação
Vigente
Suspensa
Superada
Cancelada
```

---

# 36. Regra Vigente

Uma regra somente deverá ser considerada vigente quando:

* estiver validada;
* possuir proprietário definido quando aplicável;
* estiver suficientemente documentada;
* não tiver sido substituída;
* estiver alinhada às normas aplicáveis.

---

# 37. Regras Conflitantes

Duas regras não deverão produzir comportamentos contraditórios sem que exista uma regra explícita de precedência.

Quando houver conflito:

1. identificar as regras;
2. identificar a origem;
3. avaliar autoridade;
4. verificar legislação;
5. definir precedência;
6. registrar a decisão;
7. atualizar os artefatos afetados.

---

# 38. Precedência

Quando aplicável, a precedência deverá ser definida.

Exemplo:

```text
Legislação
   ↓
Regulamentação
   ↓
Política institucional
   ↓
Procedimento
   ↓
Configuração operacional
```

A hierarquia efetiva deverá respeitar o ordenamento jurídico e as normas aplicáveis.

---

# 39. Regras Compartilhadas

Uma regra utilizada por vários módulos deverá ser mantida como regra corporativa ou de domínio, evitando duplicação.

Exemplo:

```text
RN-CORPORATIVA-001 – Identificação de Pessoa
```

Essa regra poderá ser referenciada por:

* RH;
* Saúde;
* Educação;
* Tributação;
* Assistência Social;
* outros domínios.

---

# 40. Regras Específicas

Regras aplicáveis somente a determinado domínio deverão permanecer vinculadas ao domínio correspondente.

Exemplo:

```text
RN-SAÚDE-001
```

---

# 41. Reutilização

Quando a mesma regra for necessária em diferentes processos, deverá ser criada uma única regra oficial sempre que possível.

Os processos deverão referenciá-la.

---

# 42. Duplicidade

Regras semanticamente equivalentes não deverão ser cadastradas repetidamente sem justificativa.

Antes de criar uma nova regra, deverá ser realizada busca por regras existentes.

---

# 43. Relação com Processos

Cada regra deverá indicar os processos afetados quando aplicável.

```text
RN-COMPRAS-001
       ↓
PROC-COMPRAS-001
PROC-CONTRATOS-001
```

---

# 44. Relação com Serviços

Quando aplicável:

```text
RN-COMPRAS-001
       ↓
SERV-COMPRAS-001
```

---

# 45. Relação com Capacidades

Quando aplicável:

```text
RN-COMPRAS-001
       ↓
CAP-COMPRAS-001
```

---

# 46. Relação com Atores

Deverá ser possível identificar os atores sujeitos à regra.

Exemplo:

```text
**Atores afetados:**

- Servidor responsável pela contratação;
- Gestor;
- Fiscal.
```

---

# 47. Relação com Casos de Uso

Uma regra poderá ser utilizada por um ou mais Casos de Uso.

```text
RN-COMPRAS-001
       ↓
UC-COMPRAS-001
UC-COMPRAS-003
```

---

# 48. Relação com Histórias de Usuário

Uma regra poderá complementar uma História de Usuário.

```text
HU-COMPRAS-001
       ↓
RN-COMPRAS-001
```

---

# 49. Relação com Requisitos

Um requisito poderá derivar de uma ou mais regras.

```text
RN-COMPRAS-001
       ↓
REQ-COMPRAS-001
```

---

# 50. Relação com Especificações

A especificação deverá demonstrar como a solução atenderá à regra quando necessário.

```text
RN-COMPRAS-001
       ↓
REQ-COMPRAS-001
       ↓
ESP-COMPRAS-001
```

---

# 51. Relação com Critérios de Aceitação

A regra deverá ser verificável por critérios de aceitação quando aplicável.

```text
RN-COMPRAS-001
       ↓
CA-COMPRAS-001
```

---

# 52. Relação com Testes

As regras críticas deverão possuir testes correspondentes.

```text
RN-COMPRAS-001
       ↓
TEST-COMPRAS-001
```

---

# 53. Matriz de Rastreabilidade

A relação completa poderá ser representada como:

```text
Regra
   ↓
Processo
   ↓
Serviço
   ↓
História / Caso de Uso
   ↓
Requisito
   ↓
Especificação
   ↓
Critério
   ↓
Teste
```

---

# 54. Regras e Dados

Quando uma regra depender de dados, deverão ser identificados os elementos relevantes.

Exemplo:

```text
RN-COMPRAS-001
       ↓
Fornecedor
       ↓
Situação Cadastral
```

---

# 55. Regras e Dados Pessoais

Quando envolver dados pessoais, deverá ser avaliado:

* finalidade;
* necessidade;
* acesso;
* base legal quando aplicável;
* retenção;
* compartilhamento;
* segurança;
* auditoria.

---

# 56. Regras e Segurança

Regras relacionadas à segurança deverão identificar, quando necessário:

* perfil;
* permissão;
* condição;
* recurso;
* operação;
* auditoria.

Exemplo:

```text
Somente usuários autorizados poderão aprovar contratos.
```

---

# 57. Regras e Auditoria

Regras críticas poderão exigir registro das decisões tomadas com base nelas.

Exemplo:

```text
A aprovação deverá registrar usuário, data, hora e resultado.
```

---

# 58. Regras e Notificações

Quando uma regra determinar comunicação:

```text
Quando uma solicitação ultrapassar o prazo definido,
o responsável deverá ser notificado.
```

A regra determina a obrigação.

O mecanismo técnico de notificação deverá ser tratado na especificação.

---

# 59. Regras Temporais

Deverão ser explicitadas quando houver:

* prazo;
* vencimento;
* período;
* janela;
* recorrência;
* calendário;
* dia útil;
* feriado.

Exemplo:

```text
O prazo deverá considerar os dias úteis definidos
pelo calendário oficial aplicável.
```

---

# 60. Regras de Cálculo

Quando houver cálculo, recomenda-se apresentar:

```text
**Entradas:**

- Valor;
- Quantidade;
- Percentual.

**Fórmula:**

Resultado = Valor × Percentual

**Arredondamento:**

<Regra>

**Precisão:**

<Regra>
```

---

# 61. Regras de Aprovação

Deverão identificar:

* quem aprova;
* em quais condições;
* limites;
* sequência;
* substituição;
* delegação;
* registro da decisão.

---

# 62. Regras de Alçada

Quando houver limites financeiros ou administrativos:

```text
Valor da operação
       ↓
Faixa de alçada
       ↓
Responsável pela aprovação
```

Os valores deverão possuir fonte e vigência.

---

# 63. Regras de Exceção

Toda exceção deverá indicar:

* condição;
* autoridade;
* justificativa;
* período;
* consequência;
* registro.

---

# 64. Regras Configuráveis

Quando uma regra puder variar entre municípios, secretarias ou contextos, deverá ser avaliada a possibilidade de parametrização.

Exemplo:

```text
Prazo para análise = parâmetro configurável.
```

A regra de negócio continua existindo independentemente da configuração.

---

# 65. Parametrização

Quando parametrizada, deverá ser possível identificar:

```text
Regra
   ↓
Parâmetro
   ↓
Valor
   ↓
Vigência
   ↓
Contexto
```

---

# 66. Regras Municipalizáveis

Como o SIGMUN poderá ser utilizado por diferentes municípios, regras que variem entre municípios deverão ser identificadas.

Exemplo:

```text
RN-TRIBUTOS-001

Tipo: Parametrizável

Escopo:
Município

Parâmetro:
Alíquota aplicável.
```

---

# 67. Regras Federais, Estaduais e Municipais

Quando aplicável, deverá ser indicada a esfera normativa:

```text
Federal
Estadual
Municipal
Institucional
Operacional
```

---

# 68. Regras de Integração

Quando uma regra depender de sistema externo, deverá ser identificada a dependência.

```text
Regra
   ↓
Fonte externa
   ↓
Integração
   ↓
Validação
```

---

# 69. Regras de Offline First

Para atividades de campo, deverá ser avaliado se a regra deverá ser aplicada:

* localmente;
* após sincronização;
* nos dois momentos.

Exemplo:

```text
A validação que impedir registro inconsistente deverá ocorrer
localmente quando os dados necessários estiverem disponíveis.
```

---

# 70. Regras de Conflito de Sincronização

Quando aplicável, deverão existir regras para:

* precedência;
* resolução;
* rejeição;
* reconciliação;
* auditoria.

---

# 71. Regras de Qualidade

Uma regra deverá ser:

* clara;
* atômica;
* necessária;
* verificável;
* rastreável;
* não ambígua;
* atualizada.

---

# 72. Regra Atômica

Uma regra deverá representar uma decisão principal.

Evitar:

```text
O fornecedor deverá estar ativo, possuir documentação válida,
não possuir pendências, estar habilitado e possuir autorização.
```

Quando as condições forem independentes, deverão ser separadas.

---

# 73. Linguagem

Recomenda-se utilizar linguagem normativa e objetiva:

* deverá;
* não poderá;
* somente poderá;
* será permitido;
* será obrigatório;
* deverá ser considerado;
* deverá ser rejeitado.

Evitar termos vagos:

* preferencialmente;
* normalmente;
* quando possível;
* talvez;
* adequado;
* rapidamente.

Quando esses termos forem necessários, deverão ser definidos objetivamente.

---

# 74. Exemplo Completo

````markdown
# RN-COMPRAS-001 – Fornecedor Ativo

#### Regra de Negócio

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RN-COMPRAS-001

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

---

# 1. Enunciado

Somente fornecedores com situação cadastral ativa poderão
ser selecionados para novas contratações.

# 2. Contexto

A regra aplica-se ao processo de Gestão de Contratações.

# 3. Escopo

Gestão de Fornecedores e Contratações.

# 4. Fonte

Cadastro Corporativo de Fornecedores.

# 5. Proprietário

Área responsável pela Gestão de Contratações.

# 6. Atores Afetados

- Servidor responsável pela contratação;
- Gestor;
- Fiscal.

# 7. Exceções

Exceções somente poderão ocorrer quando houver fundamento
legal ou procedimento formal que as autorize.

# 8. Requisitos Relacionados

- REQ-COMPRAS-001

# 9. Critérios de Aceitação

- CA-COMPRAS-001

# 10. Testes

- TEST-COMPRAS-001

# 11. Rastreabilidade

```text
PROC-COMPRAS-001
        ↓
RN-COMPRAS-001
        ↓
REQ-COMPRAS-001
        ↓
ESP-COMPRAS-001
        ↓
CA-COMPRAS-001
        ↓
TEST-COMPRAS-001
````

````

---

# 75. Modelo Corporativo

O modelo padrão para registro de uma regra será:

```markdown
# RN-XXXX-001 – Nome da Regra

#### Regra de Negócio

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RN-XXXX-001

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- <Documento>

---

# 1. Enunciado

<Regra>

# 2. Finalidade

<Finalidade>

# 3. Contexto

<Contexto>

# 4. Escopo

<Escopo>

# 5. Categoria

<Categoria>

# 6. Fonte

<Fonte>

# 7. Fundamento Legal

<Fundamento>

# 8. Proprietário

<Proprietário>

# 9. Responsável pela Manutenção

<Responsável>

# 10. Atores Afetados

<Atores>

# 11. Condições

<Condições>

# 12. Exceções

<Exceções>

# 13. Parâmetros

<Parâmetros>

# 14. Dados Relacionados

<Dados>

# 15. Requisitos Relacionados

<Requisitos>

# 16. Histórias de Usuário Relacionadas

<Histórias>

# 17. Casos de Uso Relacionados

<Casos de Uso>

# 18. Processos Relacionados

<Processos>

# 19. Serviços Relacionados

<Serviços>

# 20. Critérios de Aceitação

<Critérios>

# 21. Testes

<Testes>

# 22. Segurança

<Segurança>

# 23. Privacidade

<Privacidade>

# 24. Auditoria

<Auditoria>

# 25. Rastreabilidade

<Rastreabilidade>

# 26. Impactos

<Impactos>

# 27. Observações

<Observações>

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |
````

---

# 76. Checklist

Antes de considerar uma regra pronta:

* [ ] Possui identificador único?
* [ ] Possui nome?
* [ ] Possui enunciado claro?
* [ ] Possui contexto?
* [ ] Possui escopo?
* [ ] Possui categoria?
* [ ] Possui fonte?
* [ ] Possui fundamento legal quando aplicável?
* [ ] Possui proprietário?
* [ ] Possui responsável pela manutenção?
* [ ] Possui atores afetados?
* [ ] Possui condições?
* [ ] Possui exceções quando necessárias?
* [ ] Possui parâmetros quando aplicável?
* [ ] Está relacionada aos processos?
* [ ] Está relacionada aos serviços?
* [ ] Está relacionada aos requisitos?
* [ ] Possui critérios de aceitação?
* [ ] Possui testes quando aplicável?
* [ ] Possui rastreabilidade?
* [ ] Possui versão?
* [ ] Está validada?

---

# 77. Governança

As Regras de Negócio deverão ser tratadas como ativos de conhecimento institucional.

Sua alteração deverá considerar impactos sobre:

* processos;
* serviços;
* requisitos;
* especificações;
* dados;
* integrações;
* testes;
* treinamento;
* documentação;
* operação.

Alterações relevantes deverão seguir o processo corporativo de gestão de mudanças.

---

# 78. Regra Fundamental

Toda Regra de Negócio deverá permitir responder:

> **O que deve ser obedecido?**

> **Por que essa regra existe?**

> **Onde ela se aplica?**

> **Quem é responsável por ela?**

> **Qual é sua origem?**

> **Quais requisitos dependem dela?**

> **Como sua aplicação será verificada?**

> **O que será impactado se ela mudar?**

---

# 79. Disposições Finais

As Regras de Negócio constituem parte fundamental do conhecimento corporativo do SIGMUN.

Elas deverão preservar o conhecimento institucional independentemente das tecnologias utilizadas na implementação do sistema.

O SIGMUN deverá evitar que regras importantes existam exclusivamente em código-fonte, configurações ou conhecimento informal de indivíduos.

A regra deverá existir como conhecimento governado, rastreável e versionado, enquanto sua implementação deverá ser tratada como consequência técnica dessa regra.

---

# Controle de Versões

| Versão | Data       | Descrição                                          |
| ------ | ---------- | -------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação do padrão corporativo de Regras de Negócio |

---

**Documento:** Regras-de-Negocio-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
