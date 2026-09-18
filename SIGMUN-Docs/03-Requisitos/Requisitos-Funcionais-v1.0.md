# Requisitos Funcionais

#### Requisitos Funcionais

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
* Regras-de-Negocio-v1.0.md
* Casos-de-Uso-v1.0.md
* Historias-de-Usuario-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md
* Matriz-de-Rastreabilidade-v1.0.md

---

# 1. Finalidade

Este documento estabelece o padrão corporativo para identificação, documentação, validação, rastreabilidade, versionamento e governança dos **Requisitos Funcionais do SIGMUN**.

Os Requisitos Funcionais descrevem **comportamentos, serviços, operações, funcionalidades e respostas que o SIGMUN deverá disponibilizar** para atender às necessidades do negócio.

---

# 2. Objetivos

Os Requisitos Funcionais deverão:

* transformar necessidades de negócio em comportamentos verificáveis;
* orientar o desenvolvimento;
* orientar a especificação;
* orientar testes;
* permitir validação pelos usuários;
* preservar o conhecimento funcional;
* permitir estimativa e planejamento;
* facilitar análise de impacto;
* permitir rastreabilidade;
* reduzir ambiguidades;
* apoiar manutenção e evolução.

---

# 3. Definição

Um Requisito Funcional especifica uma função que o sistema deverá executar ou um comportamento que deverá apresentar.

Exemplo:

> O sistema deverá permitir cadastrar um fornecedor.

O requisito não define necessariamente como a função será implementada.

---

# 4. Requisito Funcional x Regra de Negócio

Os conceitos são complementares.

**Regra de Negócio:**

> Somente fornecedores ativos poderão participar de novas contratações.

**Requisito Funcional:**

> O sistema deverá impedir a seleção de fornecedores inativos durante a criação de uma contratação.

A regra define a obrigação do negócio.

O requisito define o comportamento esperado da solução.

---

# 5. Requisito Funcional x Requisito Não Funcional

### Requisito Funcional

Define **o que o sistema deverá fazer**.

### Requisito Não Funcional

Define **como uma característica da solução deverá se comportar ou qual restrição deverá atender**.

Exemplo:

```text
RF-001
O sistema deverá permitir consultar contratos.

RNF-001
A consulta deverá apresentar os resultados em até 2 segundos
nas condições definidas para o serviço.
```

---

# 6. Princípios

Os Requisitos Funcionais deverão ser:

* claros;
* objetivos;
* necessários;
* verificáveis;
* rastreáveis;
* consistentes;
* completos;
* não ambíguos;
* independentes de implementação quando possível;
* versionados.

---

# 7. Identificação

Cada requisito deverá possuir identificador único.

Formato recomendado:

```text
RF-<DOMÍNIO>-<NÚMERO>
```

Exemplos:

```text
RF-COMPRAS-001
RF-RH-001
RF-TRIBUTOS-001
RF-SAÚDE-001
RF-EDUCACAO-001
```

---

# 8. Nome do Requisito

O nome deverá identificar de forma objetiva a função.

Exemplo:

```text
RF-COMPRAS-001 – Cadastrar Fornecedor
```

---

# 9. Enunciado

O enunciado deverá ser escrito de forma normativa.

Preferencialmente:

> O sistema deverá permitir cadastrar fornecedores.

Evitar:

> O sistema poderá ter uma tela para cadastro de fornecedores.

---

# 10. Estrutura Padrão

Cada Requisito Funcional deverá conter, quando aplicável:

* identificador;
* nome;
* descrição;
* finalidade;
* origem;
* processo;
* serviço;
* atores;
* pré-condições;
* entradas;
* processamento;
* saídas;
* regras de negócio;
* exceções;
* pós-condições;
* requisitos relacionados;
* critérios de aceitação;
* testes;
* prioridade;
* criticidade;
* dependências;
* versão;
* status.

---

# 11. Origem

Deverá ser identificada a origem do requisito.

Possíveis origens:

* objetivo estratégico;
* capacidade;
* processo;
* serviço;
* caso de uso;
* história de usuário;
* regra de negócio;
* legislação;
* necessidade operacional;
* decisão administrativa;
* requisito de integração.

---

# 12. Processo Relacionado

Quando aplicável, deverá ser informado o processo que o requisito suporta.

Exemplo:

```text
**Processo:** PROC-COMPRAS-001 – Gestão de Contratações
```

---

# 13. Serviço Relacionado

Quando aplicável:

```text
**Serviço:** SERV-COMPRAS-001 – Gestão de Contratações
```

---

# 14. Atores

Deverão ser identificados os atores que interagem diretamente com a funcionalidade.

Exemplo:

```text
- Servidor responsável;
- Gestor;
- Fiscal;
- Administrador.
```

---

# 15. Pré-Condições

As condições necessárias antes da execução deverão ser registradas.

Exemplo:

```text
- Usuário autenticado;
- Usuário autorizado;
- Cadastro do município ativo.
```

---

# 16. Entradas

Deverão ser identificadas as informações necessárias.

Exemplo:

```text
- CNPJ;
- Razão social;
- Endereço;
- Contatos;
- Situação cadastral.
```

---

# 17. Processamento

Deverá ser descrito o comportamento funcional esperado.

Exemplo:

```text
O sistema deverá validar os dados obrigatórios,
verificar a existência de cadastro duplicado e,
estando os dados válidos, registrar o fornecedor.
```

Detalhes técnicos deverão permanecer nas especificações apropriadas.

---

# 18. Saídas

Deverão ser identificados os resultados produzidos.

Exemplo:

```text
- Fornecedor cadastrado;
- Identificador do fornecedor;
- Registro de auditoria.
```

---

# 19. Regras de Negócio Relacionadas

Os requisitos deverão referenciar as regras aplicáveis.

Exemplo:

```text
- RN-COMPRAS-001 – Fornecedor Ativo
- RN-COMPRAS-002 – Unicidade do Fornecedor
```

---

# 20. Exceções

Deverão ser descritas as situações que alteram o fluxo normal.

Exemplo:

```text
Se o fornecedor já estiver cadastrado,
o sistema deverá informar a duplicidade e impedir
a criação de novo registro.
```

---

# 21. Pós-Condições

Deverão indicar o estado esperado após execução bem-sucedida.

Exemplo:

```text
- Fornecedor registrado;
- Dados persistidos;
- Histórico de operação registrado.
```

---

# 22. Critérios de Aceitação

Todo requisito funcional relevante deverá possuir critérios objetivos de aceitação.

Exemplo:

```text
CA-COMPRAS-001

Dado que o usuário possua autorização,
quando informar os dados obrigatórios válidos,
então o sistema deverá registrar o fornecedor.
```

---

# 23. Testes

Quando aplicável, cada requisito deverá possuir testes relacionados.

Exemplo:

```text
TEST-COMPRAS-001
```

A relação deverá ser mantida na Matriz de Rastreabilidade.

---

# 24. Prioridade

Os requisitos poderão ser classificados como:

```text
Crítica
Alta
Média
Baixa
```

A classificação deverá considerar valor, risco, dependências e necessidade institucional.

---

# 25. Criticidade

A criticidade poderá considerar:

* impacto ao cidadão;
* impacto financeiro;
* impacto legal;
* impacto operacional;
* impacto à segurança;
* impacto à continuidade;
* impacto à proteção de dados.

---

# 26. Dependências

Deverão ser identificadas dependências relevantes.

Exemplo:

```text
RF-COMPRAS-002 depende de:

RF-CADASTRO-001
RF-USUARIO-001
RN-COMPRAS-001
```

---

# 27. Requisitos Dependentes

Também deverá ser possível identificar requisitos que dependem do requisito atual.

---

# 28. Estado

Os requisitos poderão possuir:

```text
Proposto
Em Análise
Em Validação
Aprovado
Em Desenvolvimento
Em Teste
Homologado
Vigente
Suspenso
Superado
Cancelado
```

---

# 29. Versionamento

Alterações significativas deverão produzir nova versão do requisito.

Exemplo:

```text
RF-COMPRAS-001
Versão 1.0

RF-COMPRAS-001
Versão 1.1
```

O identificador permanece o mesmo quando o requisito continua sendo semanticamente o mesmo.

---

# 30. Alteração de Significado

Quando uma alteração modificar significativamente o significado do requisito, deverá ser avaliada a criação de um novo requisito.

---

# 31. Histórico

| Versão | Data       | Alteração | Responsável   |
| ------ | ---------- | --------- | ------------- |
| 1.0    | AAAA-MM-DD | Criação   | Equipe SIGMUN |
| 1.1    | AAAA-MM-DD | Alteração | Equipe SIGMUN |

---

# 32. Rastreabilidade

O requisito deverá possuir rastreabilidade bidirecional.

Fluxo mínimo:

```text
Origem
   ↓
RF
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

# 33. Rastreabilidade para a Origem

Deverá ser possível identificar:

```text
Objetivo
   ↓
Capacidade
   ↓
Processo
   ↓
Serviço
   ↓
Caso de Uso / História
   ↓
RF
```

---

# 34. Rastreabilidade para a Implementação

Deverá ser possível identificar:

```text
RF
   ↓
Especificação
   ↓
Componente
   ↓
Implementação
   ↓
Teste
```

---

# 35. Rastreabilidade com Regras

Quando houver regra de negócio:

```text
RN
   ↓
RF
   ↓
CA
   ↓
TEST
```

---

# 36. Rastreabilidade com Casos de Uso

```text
UC
   ↓
RF
```

Um caso de uso poderá estar associado a vários requisitos.

---

# 37. Rastreabilidade com Histórias de Usuário

```text
HU
   ↓
RF
```

Uma história poderá gerar um ou mais requisitos funcionais.

---

# 38. Rastreabilidade com Serviços

```text
SERV
   ↓
RF
```

Essa relação permite identificar quais funcionalidades sustentam determinado serviço municipal.

---

# 39. Rastreabilidade com Processos

```text
PROC
   ↓
RF
```

Essa relação permite avaliar o impacto de alterações funcionais nos processos municipais.

---

# 40. Requisitos Funcionais Corporativos

Alguns requisitos poderão ser compartilhados por vários módulos.

Exemplos:

```text
RF-CORPORATIVO-001 – Autenticar Usuário
RF-CORPORATIVO-002 – Registrar Auditoria
RF-CORPORATIVO-003 – Consultar Pessoa
RF-CORPORATIVO-004 – Gerenciar Documentos
```

Esses requisitos deverão ser reutilizados sempre que aplicável.

---

# 41. Requisitos Funcionais de Domínio

Requisitos específicos deverão ser associados ao domínio correspondente.

Exemplos:

```text
RF-SAÚDE-001
RF-EDUCACAO-001
RF-TRIBUTOS-001
RF-COMPRAS-001
RF-RH-001
```

---

# 42. Requisitos Funcionais Transversais

Algumas funcionalidades atravessam vários domínios.

Exemplos:

* identidade;
* notificações;
* documentos;
* auditoria;
* relatórios;
* pesquisa;
* permissões;
* integrações.

Esses requisitos deverão ser tratados de forma corporativa quando houver reutilização.

---

# 43. Requisitos de Consulta

Deverão especificar:

* informações disponíveis;
* filtros;
* ordenação;
* paginação;
* permissões;
* resultados;
* exportações quando aplicável.

---

# 44. Requisitos de Cadastro

Deverão especificar:

* dados obrigatórios;
* dados opcionais;
* validações;
* duplicidade;
* criação;
* alteração;
* cancelamento;
* histórico.

---

# 45. Requisitos de Alteração

Deverão definir:

* quem pode alterar;
* quais campos podem ser alterados;
* condições;
* histórico;
* auditoria;
* impacto.

---

# 46. Requisitos de Exclusão

A exclusão deverá ser tratada explicitamente.

Deverá ser definido se o comportamento será:

* exclusão física;
* exclusão lógica;
* cancelamento;
* inativação;
* arquivamento.

A decisão deverá respeitar as políticas de dados e retenção.

---

# 47. Requisitos de Workflow

Quando houver fluxo:

```text
Estado Inicial
    ↓
Ação
    ↓
Validação
    ↓
Aprovação
    ↓
Estado Final
```

Deverão ser identificados os estados e transições.

---

# 48. Requisitos de Aprovação

Deverão definir:

* aprovador;
* condições;
* alçada;
* sequência;
* rejeição;
* retorno;
* delegação;
* registro da decisão.

---

# 49. Requisitos de Notificação

Deverão definir:

* evento;
* destinatário;
* canal;
* conteúdo;
* prazo;
* condição de envio;
* registro.

A tecnologia utilizada será definida posteriormente.

---

# 50. Requisitos de Relatórios

Deverão especificar:

* finalidade;
* público;
* filtros;
* informações;
* período;
* agrupamentos;
* permissões;
* formato;
* exportação quando aplicável.

---

# 51. Requisitos de Pesquisa

Deverão especificar:

* campos pesquisáveis;
* filtros;
* critérios;
* ordenação;
* paginação;
* permissões.

---

# 52. Requisitos de Integração

Quando uma funcionalidade depender de integração:

```text
RF
   ↓
Integração
   ↓
Sistema Externo
```

Deverão ser identificados:

* origem;
* destino;
* evento;
* dados;
* frequência;
* resposta;
* erros;
* contingência.

---

# 53. Requisitos Offline First

Para funcionalidades de campo, deverá ser definido se a operação:

* exige conexão;
* pode ocorrer offline;
* precisa sincronizar posteriormente;
* exige validação local;
* exige validação no servidor;
* possui conflito de sincronização.

---

# 54. Requisitos de Auditoria

Quando necessário, deverá ser definido o registro de:

* usuário;
* data;
* hora;
* operação;
* entidade;
* valores anteriores;
* valores posteriores;
* resultado.

---

# 55. Requisitos de Dados

Deverão identificar os dados necessários à funcionalidade.

Exemplo:

```text
Pessoa
Fornecedor
Contrato
Item
Documento
```

As estruturas físicas deverão permanecer no Modelo de Dados e nas Especificações.

---

# 56. Requisitos de Proteção de Dados

Quando houver dados pessoais, o requisito deverá considerar:

* finalidade;
* necessidade;
* acesso;
* tratamento;
* compartilhamento;
* retenção;
* segurança;
* rastreabilidade.

---

# 57. Requisitos de Segurança Funcional

Deverão ser considerados:

* autenticação;
* autorização;
* segregação de funções;
* aprovação;
* auditoria;
* controle de acesso.

---

# 58. Requisitos de Acessibilidade

Quando aplicável, as funcionalidades deverão atender às diretrizes de acessibilidade estabelecidas pelo SIGMUN e pela legislação aplicável.

---

# 59. Requisitos de Internacionalização e Localização

Quando aplicável, deverão ser consideradas:

* idioma;
* moeda;
* formato de data;
* calendário;
* timezone;
* formatos municipais.

---

# 60. Requisitos Parametrizáveis

Quando o comportamento variar entre municípios ou órgãos, deverá ser avaliada a parametrização.

Exemplo:

```text
RF-TRIBUTOS-001

O sistema deverá permitir configurar os parâmetros
tributários aplicáveis ao município.
```

---

# 61. Requisitos Multi-Tenant

Quando aplicável, deverá ser considerado o isolamento entre municípios, órgãos ou unidades administrativas.

A regra arquitetural correspondente deverá ser tratada nos documentos de arquitetura.

---

# 62. Requisitos de Continuidade

Funcionalidades críticas deverão considerar:

* indisponibilidade;
* recuperação;
* contingência;
* operação degradada;
* sincronização posterior.

---

# 63. Requisitos de Observabilidade

Quando necessário, deverá ser possível identificar eventos funcionais relevantes para monitoramento e diagnóstico.

---

# 64. Requisitos de Configuração

Quando a funcionalidade depender de configuração, deverão ser identificados:

* parâmetro;
* valor;
* unidade;
* escopo;
* vigência;
* responsável.

---

# 65. Requisitos de Busca e Navegação

Quando aplicável, deverão definir:

* critérios de busca;
* resultados;
* navegação;
* filtros;
* paginação;
* permissões.

---

# 66. Requisitos de Importação

Deverão especificar:

* origem;
* formato;
* campos;
* validações;
* duplicidades;
* erros;
* resultado;
* auditoria.

---

# 67. Requisitos de Exportação

Deverão definir:

* dados exportáveis;
* permissões;
* formatos;
* filtros;
* período;
* auditoria.

---

# 68. Requisitos de Anexos

Quando houver documentos associados:

* tipos permitidos;
* tamanho;
* quantidade;
* classificação;
* retenção;
* segurança;
* versionamento.

---

# 69. Requisitos de Busca Documental

Deverão considerar:

* metadados;
* conteúdo;
* classificação;
* permissões;
* indexação;
* histórico.

---

# 70. Requisitos de Workflow Municipal

Os fluxos deverão permitir representar, quando necessário:

```text
Rascunho
   ↓
Submetido
   ↓
Em Análise
   ↓
Aprovado
   ↓
Executado
   ↓
Concluído
```

Os estados reais deverão ser definidos pelo processo de negócio.

---

# 71. Requisitos de Exceção

Cada funcionalidade relevante deverá identificar comportamentos para situações excepcionais.

Exemplo:

```text
Se a validação externa estiver indisponível,
o sistema deverá aplicar o procedimento de contingência definido.
```

---

# 72. Requisitos de Erro

Os erros funcionais deverão possuir comportamento definido.

Exemplo:

```text
Quando os dados obrigatórios não forem informados,
o sistema deverá impedir a conclusão da operação e informar
quais dados precisam ser corrigidos.
```

---

# 73. Requisitos de Mensagens

Mensagens funcionais relevantes deverão ser compreensíveis e orientadas à ação.

Evitar:

```text
Erro 409.
```

Preferir:

```text
Não foi possível concluir a operação porque o registro
já existe.
```

---

# 74. Requisitos de Histórico

Quando uma entidade possuir histórico funcional, deverá ser definido:

* eventos registrados;
* usuário;
* data;
* alteração;
* motivo;
* consulta do histórico.

---

# 75. Requisitos de Estado

Entidades com ciclo de vida deverão possuir estados claramente definidos.

Exemplo:

```text
Ativo
Inativo
Suspenso
Cancelado
Encerrado
```

Os estados deverão possuir significado de negócio.

---

# 76. Requisitos de Relacionamento

Quando uma entidade depender de outra, o requisito deverá deixar essa dependência clara.

Exemplo:

```text
Uma contratação deverá possuir fornecedor.
```

---

# 77. Requisitos de Consistência

O sistema deverá preservar as regras de consistência definidas pelo negócio.

---

# 78. Requisitos de Transação

Quando uma operação envolver múltiplas alterações relacionadas, deverá ser definido o resultado esperado em caso de sucesso ou falha.

---

# 79. Requisitos de Concorrência

Quando dois usuários puderem atuar simultaneamente sobre o mesmo processo, deverá ser definido o comportamento esperado.

---

# 80. Requisitos de Idempotência

Quando a mesma operação puder ser enviada mais de uma vez, deverá ser definido se o processamento deverá ser idempotente.

---

# 81. Requisitos de Sincronização

Para operações distribuídas ou offline:

```text
Operação local
   ↓
Fila
   ↓
Sincronização
   ↓
Validação
   ↓
Confirmação
```

---

# 82. Requisitos de Integração Assíncrona

Quando uma operação ocorrer de forma assíncrona, deverão ser definidos:

* evento;
* origem;
* destino;
* estado;
* confirmação;
* erro;
* reprocessamento.

---

# 83. Requisitos de Reprocessamento

Quando uma operação puder falhar temporariamente, deverá ser definido:

* condição;
* quantidade de tentativas;
* intervalo;
* comportamento final;
* registro.

---

# 84. Requisitos de Cancelamento

Deverão definir:

* quem pode cancelar;
* quando pode cancelar;
* motivo;
* efeitos;
* histórico;
* notificações.

---

# 85. Requisitos de Aprovação em Cadeia

Quando houver múltiplos níveis:

```text
Solicitante
   ↓
Responsável
   ↓
Gestor
   ↓
Autoridade Superior
```

As condições deverão ser definidas pelas regras de negócio.

---

# 86. Requisitos de Delegação

Quando permitido, deverá ser definido:

* quem pode delegar;
* para quem;
* período;
* escopo;
* registro;
* revogação.

---

# 87. Requisitos de Segregação de Funções

Quando necessário, o sistema deverá impedir que um mesmo usuário execute funções incompatíveis.

Exemplo:

```text
Usuário que solicita
≠
Usuário que aprova
```

---

# 88. Requisitos de Compliance

Quando uma função estiver relacionada a obrigação normativa, deverá existir rastreabilidade para sua origem.

---

# 89. Requisitos de Evidência

Processos críticos poderão exigir evidências:

* documentos;
* anexos;
* registros;
* aprovações;
* logs;
* justificativas.

---

# 90. Requisitos de Valor Público

Quando aplicável, deverá ser possível relacionar a funcionalidade ao resultado público esperado.

```text
Necessidade
   ↓
RF
   ↓
Serviço
   ↓
Resultado
```

---

# 91. Qualidade dos Requisitos

Um Requisito Funcional deverá ser:

### Claro

Não possuir interpretações conflitantes.

### Completo

Conter informações suficientes.

### Consistente

Não contradizer outros requisitos.

### Verificável

Poder ser testado.

### Rastreável

Possuir origem e destino identificáveis.

### Atômico

Representar uma necessidade funcional principal.

### Necessário

Possuir justificativa.

---

# 92. Antipadrões

Evitar requisitos:

* vagos;
* subjetivos;
* excessivamente técnicos;
* duplicados;
* sem origem;
* sem critério de aceitação;
* sem responsável;
* contraditórios;
* dependentes de tecnologia sem necessidade.

---

# 93. Exemplo Completo

````markdown
# RF-COMPRAS-001 – Cadastrar Fornecedor

#### Requisito Funcional

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RF-COMPRAS-001

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

---

# 1. Descrição

O sistema deverá permitir cadastrar fornecedores.

# 2. Finalidade

Permitir o registro e gerenciamento dos fornecedores
utilizados nos processos de contratação.

# 3. Processo

PROC-COMPRAS-001 – Gestão de Contratações.

# 4. Serviço

SERV-COMPRAS-001 – Gestão de Fornecedores.

# 5. Atores

- Servidor autorizado;
- Gestor.

# 6. Pré-Condições

- Usuário autenticado;
- Usuário autorizado.

# 7. Entradas

- CNPJ;
- Razão social;
- Nome fantasia;
- Endereço;
- Contatos.

# 8. Regras de Negócio

- RN-COMPRAS-001 – Fornecedor Ativo;
- RN-COMPRAS-002 – Unicidade do Fornecedor.

# 9. Processamento

O sistema deverá validar os dados obrigatórios,
verificar duplicidade e registrar o fornecedor
quando todas as condições forem atendidas.

# 10. Saídas

- Fornecedor cadastrado;
- Identificador do fornecedor;
- Registro de auditoria.

# 11. Exceções

Caso o fornecedor já exista, o sistema deverá impedir
novo cadastro e informar a existência do registro.

# 12. Critérios de Aceitação

- CA-COMPRAS-001.

# 13. Testes

- TEST-COMPRAS-001.

# 14. Especificação

- ESP-COMPRAS-001.

# 15. Rastreabilidade

```text
PROC-COMPRAS-001
        ↓
SERV-COMPRAS-001
        ↓
RN-COMPRAS-001
        ↓
RF-COMPRAS-001
        ↓
ESP-COMPRAS-001
        ↓
CA-COMPRAS-001
        ↓
TEST-COMPRAS-001
````

````

---

# 94. Modelo Corporativo

```markdown
# RF-XXXX-001 – Nome do Requisito

#### Requisito Funcional

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RF-XXXX-001

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- <Documento>

---

# 1. Descrição

<Descrição>

# 2. Finalidade

<Finalidade>

# 3. Origem

<Origem>

# 4. Processo

<Processo>

# 5. Serviço

<Serviço>

# 6. Atores

<Atores>

# 7. Pré-Condições

<Pré-Condições>

# 8. Entradas

<Entradas>

# 9. Regras de Negócio

<Regras>

# 10. Processamento

<Processamento>

# 11. Saídas

<Saídas>

# 12. Pós-Condições

<Pós-Condições>

# 13. Exceções

<Exceções>

# 14. Dependências

<Dependências>

# 15. Especificação Relacionada

<Especificação>

# 16. Critérios de Aceitação

<Critérios>

# 17. Testes

<Testes>

# 18. Segurança

<Segurança>

# 19. Privacidade

<Privacidade>

# 20. Auditoria

<Auditoria>

# 21. Prioridade

<Prioridade>

# 22. Criticidade

<Criticidade>

# 23. Rastreabilidade

<Rastreabilidade>

# 24. Impactos

<Impactos>

# 25. Observações

<Observações>

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |
````

---

# 95. Checklist

Antes de considerar um Requisito Funcional aprovado:

* [ ] Possui identificador único?
* [ ] Possui nome?
* [ ] Possui descrição objetiva?
* [ ] Possui finalidade?
* [ ] Possui origem?
* [ ] Possui processo relacionado?
* [ ] Possui serviço relacionado?
* [ ] Possui atores?
* [ ] Possui pré-condições?
* [ ] Possui entradas?
* [ ] Possui regras de negócio?
* [ ] Possui processamento?
* [ ] Possui saídas?
* [ ] Possui pós-condições?
* [ ] Possui exceções?
* [ ] Possui dependências?
* [ ] Possui especificação?
* [ ] Possui critérios de aceitação?
* [ ] Possui testes?
* [ ] Possui rastreabilidade?
* [ ] Possui prioridade?
* [ ] Possui criticidade quando aplicável?
* [ ] Está validado?

---

# 96. Governança

Os Requisitos Funcionais constituem artefatos oficiais do ciclo de vida de requisitos do SIGMUN.

Nenhum requisito funcional relevante deverá ser implementado sem possuir identificação, origem e rastreabilidade adequadas.

Alterações deverão seguir o processo corporativo de gestão de requisitos e mudanças.

---

# 97. Regra Fundamental

Todo Requisito Funcional deverá permitir responder:

> **O que o sistema deverá fazer?**

> **Por que essa funcionalidade é necessária?**

> **Quem utiliza?**

> **Qual processo e serviço ela suporta?**

> **Quais regras de negócio condicionam seu comportamento?**

> **Como será aceita?**

> **Como será testada?**

> **Qual será o impacto se ela mudar?**

---

# 98. Disposições Finais

Os Requisitos Funcionais representam a ponte formal entre as necessidades do negócio e as funcionalidades do SIGMUN.

Eles deverão ser mantidos independentes de detalhes de implementação sempre que possível, permitindo que a arquitetura e a tecnologia evoluam sem perda do significado funcional.

A implementação deverá demonstrar conformidade com os requisitos aprovados, e os testes deverão fornecer evidências de seu atendimento.

---

# Controle de Versões

| Versão | Data       | Descrição                                              |
| ------ | ---------- | ------------------------------------------------------ |
| 1.0    | 2026-08-11 | Criação do padrão corporativo de Requisitos Funcionais |

---

**Documento:** Requisitos-Funcionais-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
