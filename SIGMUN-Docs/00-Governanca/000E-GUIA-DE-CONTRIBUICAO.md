# 000E — GUIA DE CONTRIBUIÇÃO DO SIGMUN

**Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA — SIGMUN**

---

## 1. Identificação do Documento

| Campo                           | Informação                                                                 |
| ------------------------------- | -------------------------------------------------------------------------- |
| **Código**                      | 000E                                                                       |
| **Título**                      | Guia de Contribuição do SIGMUN                                             |
| **Projeto**                     | SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA |
| **Classificação da Informação** | Pública                                                                    |
| **Versão**                      | 2.0                                                                        |
| **Status**                      | Vigente                                                                    |
| **Tipo**                        | Governança / Engenharia de Software                                        |
| **Responsável**                 | Governança Técnica do SIGMUN                                               |
| **Periodicidade de Revisão**    | Conforme evolução do projeto ou necessidade de governança                  |
| **Documento Mestre**            | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`                                    |
| **Padrão Corporativo**          | `000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md`                               |

---

## 2. Finalidade

Este documento estabelece as regras, princípios, responsabilidades e procedimentos para contribuição ao projeto SIGMUN.

O objetivo é garantir que toda contribuição ao projeto seja:

* rastreável;
* tecnicamente justificável;
* documentada;
* testável;
* revisável;
* segura;
* compatível com a arquitetura do SIGMUN;
* aderente às políticas corporativas;
* alinhada aos requisitos de negócio;
* compatível com os princípios de governança do projeto.

O Guia aplica-se a contribuições realizadas por:

* mantenedores;
* desenvolvedores;
* colaboradores;
* bolsistas;
* pesquisadores;
* parceiros institucionais;
* prestadores de serviço;
* equipes municipais;
* colaboradores voluntários;
* agentes de inteligência artificial utilizados como apoio à engenharia;
* demais participantes autorizados do ecossistema SIGMUN.

---

# 3. Princípios de Contribuição

Toda contribuição deve observar os princípios fundamentais do SIGMUN.

## 3.1. Governança antes da implementação

Nenhuma alteração relevante deve ser iniciada apenas a partir de uma ideia informal quando ela exigir decisão funcional, arquitetural ou de negócio.

Sempre que aplicável, a necessidade deve ser registrada por meio de:

**Issue → análise → decisão → implementação → testes → Pull Request → revisão → merge → documentação.**

---

## 3.2. Rastreabilidade

Toda alteração significativa deve permitir responder:

> Por que esta alteração existe?

> Qual problema ela resolve?

> Qual requisito atende?

> Qual domínio é afetado?

> Qual decisão arquitetural a fundamenta?

> Como foi testada?

> Qual documentação foi atualizada?

A rastreabilidade deve ser preservada entre, quando aplicável:

```text
Issue
  ↓
Requisito
  ↓
Caso de Uso / User Story
  ↓
Critério de Aceitação
  ↓
Implementação
  ↓
Testes
  ↓
Pull Request
  ↓
Documentação
```

---

## 3.3. Segurança por princípio

Toda contribuição deve considerar segurança desde o início.

Não é aceitável implementar primeiro e deixar requisitos de segurança para uma etapa posterior quando a alteração já puder introduzir riscos.

Devem ser considerados, conforme aplicabilidade:

* autenticação;
* autorização;
* segregação de responsabilidades;
* proteção de dados;
* logs;
* auditoria;
* exposição de APIs;
* validação de entrada;
* gestão de segredos;
* controle de acesso;
* prevenção contra vazamento de informações;
* segurança de dependências;
* segurança de infraestrutura;
* segurança de integrações.

---

## 3.4. LGPD e proteção de dados

Contribuições que envolvam dados pessoais devem observar a política de proteção de dados do SIGMUN e os princípios aplicáveis da LGPD.

Dados pessoais não devem ser utilizados em:

* exemplos;
* fixtures;
* testes automatizados;
* documentação;
* screenshots;
* logs;
* commits;
* Issues;
* Pull Requests;

quando isso puder ser evitado.

Sempre que possível, utilizar:

* dados fictícios;
* dados anonimizados;
* dados sintéticos;
* identificadores artificiais.

---

## 3.5. Transparência por padrão

O SIGMUN adota o princípio:

> **Transparência por padrão, Segurança por princípio e Classificação da Informação por política.**

As contribuições devem respeitar a classificação da informação e os critérios de publicação definidos pelo projeto.

---

## 3.6. Aberto sempre que possível, restrito sempre que necessário

Documentação, código, decisões e conhecimento técnico devem ser disponibilizados de forma aberta sempre que isso não representar risco:

> **Aberto sempre que possível, restrito sempre que necessário.**

Informações sensíveis, credenciais, segredos, dados pessoais e informações classificadas não devem ser publicadas no repositório público.

---

# 4. Quem Pode Contribuir

O SIGMUN poderá receber contribuições de diferentes perfis.

## 4.1. Mantenedores

Responsáveis por:

* governança do repositório;
* aprovação de mudanças;
* revisão de Pull Requests;
* gestão de releases;
* proteção das branches;
* manutenção das políticas;
* gestão da arquitetura;
* gestão da qualidade.

---

## 4.2. Desenvolvedores

Responsáveis por:

* implementação;
* testes;
* documentação técnica;
* correção de defeitos;
* atualização de dependências;
* manutenção do código.

---

## 4.3. Colaboradores

Podem contribuir com:

* documentação;
* análise;
* requisitos;
* testes;
* UX/UI;
* arquitetura;
* código;
* pesquisa;
* estudos;
* revisão técnica.

---

## 4.4. Contribuições assistidas por IA

Ferramentas de Inteligência Artificial podem ser utilizadas como apoio à:

* análise;
* programação;
* documentação;
* revisão;
* testes;
* geração de código;
* investigação técnica;
* refatoração.

Entretanto:

> **A responsabilidade final pela contribuição permanece com o colaborador humano que a submeteu.**

Código gerado por IA não deve ser incorporado automaticamente ao projeto sem:

* revisão;
* entendimento do funcionamento;
* validação;
* testes;
* análise de segurança;
* verificação de licenciamento quando aplicável.

---

# 5. Antes de Começar

Antes de iniciar uma contribuição, o colaborador deve:

1. conhecer a documentação relevante;
2. consultar a arquitetura;
3. verificar se já existe Issue relacionada;
4. verificar se já existe implementação semelhante;
5. verificar requisitos existentes;
6. verificar decisões arquiteturais existentes;
7. verificar impactos em outros domínios;
8. verificar políticas corporativas aplicáveis.

Sempre que a alteração estiver relacionada a uma funcionalidade, defeito ou melhoria significativa, deve existir uma Issue correspondente.

---

# 6. Issue como Unidade de Trabalho

A Issue representa a unidade inicial de rastreabilidade da contribuição.

As Issues podem representar:

* funcionalidade;
* defeito;
* melhoria;
* refatoração;
* tarefa técnica;
* atualização documental;
* decisão necessária;
* débito técnico;
* requisito;
* investigação;
* risco;
* atividade de infraestrutura.

---

# 7. Template de Issue

O projeto utiliza o template:

```text
.github/ISSUE_TEMPLATE/feature_or_bug.md
```

O template deve orientar o colaborador a registrar, conforme aplicável:

* tipo da contribuição;
* título;
* descrição;
* domínio;
* problema;
* comportamento esperado;
* requisitos relacionados;
* casos de uso;
* critérios de aceitação;
* evidências;
* impacto;
* segurança;
* LGPD;
* dependências;
* riscos;
* documentação afetada.

Templates de Issue têm como finalidade padronizar as informações necessárias para que uma contribuição seja analisada adequadamente.

---

# 8. Tipos de Contribuição

As principais categorias são:

| Tipo           | Descrição                     |
| -------------- | ----------------------------- |
| `feature`      | Nova funcionalidade           |
| `bug`          | Correção de defeito           |
| `refactor`     | Refatoração                   |
| `docs`         | Documentação                  |
| `test`         | Testes                        |
| `security`     | Segurança                     |
| `performance`  | Desempenho                    |
| `chore`        | Manutenção técnica            |
| `build`        | Build/dependências            |
| `ci`           | Integração contínua           |
| `architecture` | Arquitetura                   |
| `data`         | Modelo ou tratamento de dados |
| `integration`  | Integrações                   |
| `ux`           | Experiência/interface         |
| `research`     | Pesquisa ou investigação      |

---

# 9. Domínio da Contribuição

Toda contribuição funcional deve identificar o domínio afetado.

Exemplos:

* Gestão de Compras e Contratações;
* Gestão de Pessoas;
* Gestão Financeira;
* Gestão Tributária;
* Gestão Patrimonial;
* Gestão Documental;
* Gestão de Saúde;
* Gestão de Educação;
* Gestão de Obras;
* Gestão Ambiental;
* Gestão de Serviços Urbanos;
* Administração;
* Transparência;
* BI;
* Inteligência Artificial;
* Integrações;
* Segurança;
* Infraestrutura.

Novos domínios devem seguir o padrão corporativo de estruturação documental e arquitetural do SIGMUN.

---

# 10. Branches

As alterações devem ser desenvolvidas em branches próprias.

A branch `main` deve representar código/documentação em condição controlada.

Não deve ser utilizada para desenvolvimento cotidiano.

## 10.1. Padrão recomendado

```text
feature/<descricao>
bugfix/<descricao>
hotfix/<descricao>
refactor/<descricao>
docs/<descricao>
test/<descricao>
security/<descricao>
chore/<descricao>
```

Exemplos:

```text
feature/gestao-compras-contratacoes
bugfix/validacao-fornecedor
docs/atualiza-guia-contribuicao
security/correcao-autorizacao-api
test/compras-contratacoes
```

---

# 11. Commits

Os commits devem ser:

* pequenos quando possível;
* objetivos;
* relacionados à alteração;
* compreensíveis;
* rastreáveis;
* sem informações sensíveis.

## 11.1. Padrão recomendado

Adotar Conventional Commits quando aplicável:

```text
feat:
fix:
docs:
test:
refactor:
perf:
build:
ci:
chore:
security:
```

Exemplos:

```text
feat(compras): adiciona cadastro de fornecedor

fix(compras): corrige validação de modalidade

docs(contribuicao): atualiza fluxo de pull request

test(compras): adiciona testes de contratação

security(api): reforça autorização do endpoint
```

---

# 12. O que Nunca Deve Ser Commitado

É proibido versionar:

```text
.env
.env.*
*.pem
*.key
*.crt
credentials.*
secrets.*
passwords.*
tokens.*
```

Também não devem ser enviados:

* senhas;
* tokens;
* chaves privadas;
* credenciais de banco;
* credenciais de APIs;
* dados pessoais reais;
* dados sensíveis;
* arquivos de produção;
* dumps reais de banco;
* arquivos temporários;
* artefatos locais;
* ambientes virtuais;
* caches;
* arquivos gerados automaticamente sem justificativa.

---

# 13. Desenvolvimento

Durante o desenvolvimento, o colaborador deve:

1. compreender a Issue;
2. analisar a arquitetura;
3. identificar dependências;
4. implementar a alteração;
5. manter o código organizado;
6. adicionar ou atualizar testes;
7. atualizar documentação;
8. verificar segurança;
9. verificar impactos em dados;
10. verificar impactos em integrações;
11. verificar impactos nos demais domínios.

---

# 14. Qualidade do Código

O código deve priorizar:

* legibilidade;
* simplicidade;
* coesão;
* baixo acoplamento;
* responsabilidade única;
* reutilização adequada;
* tratamento correto de erros;
* tipagem quando aplicável;
* testes automatizados;
* observabilidade;
* segurança.

Não devem ser introduzidas abstrações desnecessárias apenas para aumentar a complexidade arquitetural.

---

# 15. Dependências

A inclusão ou atualização de dependências deve considerar:

* necessidade real;
* licença;
* manutenção do projeto;
* segurança;
* compatibilidade;
* tamanho;
* impacto de desempenho;
* risco de dependência abandonada;
* vulnerabilidades conhecidas.

Dependências críticas devem ser registradas e avaliadas conforme o processo de gestão técnica do SIGMUN.

---

# 16. Banco de Dados e Migrations

Alterações no modelo de dados devem ser tratadas como alterações arquiteturalmente relevantes quando aplicável.

Devem ser considerados:

* migrations;
* compatibilidade;
* integridade referencial;
* índices;
* constraints;
* performance;
* dados existentes;
* rollback;
* migração;
* auditoria;
* segurança.

Não é permitido alterar diretamente estruturas de produção como substituto de migrations versionadas.

---

# 17. APIs e Integrações

Alterações em APIs ou integrações devem considerar:

* contrato;
* versionamento;
* autenticação;
* autorização;
* validação;
* tratamento de erros;
* idempotência;
* observabilidade;
* logs;
* compatibilidade retroativa;
* documentação.

Quando uma alteração quebrar um contrato existente, ela deve ser explicitamente identificada no Pull Request.

---

# 18. Testes

Toda contribuição deve possuir testes compatíveis com seu impacto.

Conforme o caso:

```text
Testes unitários
        ↓
Testes de integração
        ↓
Testes funcionais
        ↓
Testes de API
        ↓
Testes de segurança
        ↓
Testes de regressão
```

Não é necessário aplicar todos os níveis a toda alteração.

Entretanto, o Pull Request deve deixar claro quais testes foram executados e por quê.

---

# 19. Critérios de Aceitação

Antes de solicitar revisão, o colaborador deve verificar se todos os critérios de aceitação definidos na Issue foram atendidos.

Um critério de aceitação não deve ser considerado atendido apenas porque o código foi implementado.

Deve existir evidência compatível, como:

* teste;
* resultado automatizado;
* screenshot;
* log;
* demonstração;
* evidência funcional;
* documentação.

---

# 20. Documentação

Alterações que modifiquem comportamento, arquitetura, requisitos, APIs, modelo de dados, segurança ou operação devem avaliar a necessidade de atualização documental.

Podem ser afetados:

```text
SIGMUN-Docs/
├── 00-Governanca/
├── 01-Arquitetura/
├── 02-Modelo-de-Negocio/
├── 03-Requisitos/
├── 04-Modelo-de-Dados/
├── 05-Modulos/
├── 06-Integracoes/
├── 07-LGPD-e-Seguranca/
├── 08_Migracao/
├── 09-UX/
├── 10-Testes/
├── 11-Implantacao/
└── 99-Anexos/
```

A documentação não deve ser considerada uma atividade posterior opcional quando a alteração modifica o conhecimento oficial do sistema.

---

# 21. Pull Request

Toda alteração destinada à integração na branch principal deve ser submetida por Pull Request, salvo exceções administrativas devidamente justificadas.

O Pull Request deve permitir ao revisor compreender:

* qual problema está sendo resolvido;
* qual solução foi adotada;
* quais arquivos foram alterados;
* quais requisitos foram atendidos;
* quais testes foram realizados;
* quais impactos existem;
* quais riscos existem;
* quais documentos foram atualizados.

---

# 22. Template de Pull Request

O projeto utiliza:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

O template deve conter, conforme aplicabilidade:

* Issue relacionada;
* tipo da alteração;
* domínio;
* descrição;
* requisitos;
* casos de uso;
* critérios de aceitação;
* rastreabilidade;
* impactos arquiteturais;
* banco/migrations;
* APIs/integrações;
* segurança;
* LGPD;
* testes;
* documentação;
* riscos;
* evidências;
* checklist de qualidade.

O GitHub suporta templates de Pull Request no repositório e os disponibiliza automaticamente no corpo de novos Pull Requests após sua disponibilização na branch padrão.

---

# 23. Rastreabilidade no Pull Request

Sempre que aplicável, o Pull Request deve referenciar a Issue:

```text
Closes #123
```

ou:

```text
Fixes #123
```

Também devem ser registrados identificadores relevantes, por exemplo:

```text
REQ-GCC-001
UC-GCC-003
US-GCC-012
CA-GCC-012-01
ADR-0007
```

A nomenclatura efetiva deve respeitar os identificadores já definidos nos documentos do SIGMUN.

---

# 24. Revisão de Código

A revisão deve verificar, conforme aplicabilidade:

### Funcionalidade

* A solução resolve o problema?
* Os critérios de aceitação foram atendidos?

### Arquitetura

* A alteração respeita a arquitetura?
* Existe acoplamento indevido?
* Existe duplicação?

### Código

* O código é legível?
* Há tratamento adequado de erros?
* Há complexidade desnecessária?

### Testes

* Existem testes suficientes?
* Os testes cobrem cenários relevantes?

### Segurança

* Existe possibilidade de acesso indevido?
* Há exposição de dados?
* Existem segredos?
* Entradas são validadas?

### LGPD

* Há dados pessoais envolvidos?
* O tratamento é necessário?
* Os dados de teste estão adequadamente protegidos?

### Documentação

* A documentação continua correta?
* Novos comportamentos foram documentados?

---

# 25. Aprovação

Um Pull Request não deve ser aprovado apenas porque:

* compila;
* os testes básicos passam;
* o código funciona localmente.

A aprovação deve considerar o impacto global da alteração.

Alterações de alto impacto podem exigir revisão adicional de:

* arquitetura;
* segurança;
* dados;
* negócio;
* infraestrutura;
* governança.

---

# 26. Merge

O merge deve ocorrer somente quando:

* a Issue estiver adequadamente definida;
* a implementação estiver concluída;
* os testes necessários tiverem sido executados;
* o Pull Request estiver revisado;
* os critérios de aceitação estiverem atendidos;
* conflitos estiverem resolvidos;
* documentação estiver atualizada;
* requisitos de segurança estiverem atendidos.

---

# 27. Fluxo Oficial de Contribuição

O fluxo padrão do SIGMUN é:

```text
┌───────────────────────────┐
│        Necessidade        │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│          Issue            │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     Análise / Escopo      │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│       Branch própria      │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│       Implementação       │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│    Testes + Segurança     │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│       Documentação        │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     Pull Request          │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│         Revisão           │
└─────────────┬─────────────┘
              ↓
       ┌──────┴──────┐
       │             │
      NÃO           SIM
       │             │
       ↓             ↓
   Correções       Merge
       │             │
       └──────┐      ↓
              │  ┌───────────────┐
              └─→│ Atualização   │
                 │ documental   │
                 └───────────────┘
```

---

# 28. Contribuições Documentais

Contribuições exclusivamente documentais também devem seguir o fluxo de controle.

Exemplos:

```text
docs/atualiza-arquitetura
docs/corrige-requisito
docs/adiciona-dominio-dom-dia
docs/atualiza-guia-contribuicao
```

Uma alteração documental pode exigir revisão arquitetural quando modificar:

* princípios;
* decisões;
* requisitos;
* contratos;
* políticas;
* modelo de domínio;
* modelo de dados;
* arquitetura.

---

# 29. Alterações Arquiteturais

Alterações que modifiquem significativamente a arquitetura devem ser avaliadas quanto à necessidade de ADR.

Exemplos:

* mudança de tecnologia principal;
* alteração de padrão arquitetural;
* mudança de comunicação entre serviços;
* introdução de novo componente crítico;
* mudança de estratégia de persistência;
* mudança de segurança;
* alteração de integração crítica.

Quando necessário:

```text
Issue
  ↓
Análise arquitetural
  ↓
ADR
  ↓
Implementação
  ↓
Testes
  ↓
Pull Request
```

---

# 30. Celery e Tarefas Assíncronas

Quando uma contribuição introduzir ou alterar tarefas assíncronas, devem ser considerados:

* definição da tarefa;
* idempotência;
* retries;
* timeout;
* filas;
* prioridade;
* tratamento de falhas;
* observabilidade;
* logs;
* persistência do estado;
* concorrência;
* impacto operacional.

A implementação deve respeitar a arquitetura oficial do SIGMUN.

---

# 31. Inteligência Artificial no Desenvolvimento

O uso de IA é permitido como ferramenta de apoio.

Entretanto, é responsabilidade do colaborador:

* revisar o código;
* compreender a solução;
* validar dependências;
* executar testes;
* verificar segurança;
* verificar licenciamento;
* verificar coerência arquitetural;
* evitar inclusão de informações confidenciais nos prompts.

A IA não substitui:

* revisão humana;
* responsabilidade técnica;
* aprovação arquitetural;
* testes;
* governança.

---

# 32. Uso do SIGMUN-DEV-AGENT

Quando o projeto utilizar o `SIGMUN-DEV-AGENT`, suas instruções devem ser consideradas parte do processo de desenvolvimento.

O agente pode auxiliar em:

* análise;
* implementação;
* testes;
* documentação;
* revisão;
* diagnóstico.

Porém, suas sugestões devem ser tratadas como contribuições técnicas sujeitas ao mesmo processo de revisão das contribuições humanas.

---

# 33. Segurança da Cadeia de Desenvolvimento

Contribuintes devem evitar:

* dependências desconhecidas;
* scripts não auditados;
* comandos destrutivos sem validação;
* credenciais no código;
* downloads de origem desconhecida;
* execução automática de código não confiável;
* bibliotecas abandonadas.

Quando uma dependência for crítica, sua origem e necessidade devem ser avaliadas.

---

# 34. Dados de Teste

Os ambientes de desenvolvimento e testes devem utilizar preferencialmente:

* dados sintéticos;
* dados anonimizados;
* fixtures controladas.

Dados reais da Prefeitura ou de cidadãos não devem ser utilizados sem autorização e controles apropriados.

---

# 35. Evidências

Conforme o tipo de alteração, o Pull Request poderá incluir:

* saída dos testes;
* screenshot;
* gravação de demonstração;
* resposta de API;
* resultado de migration;
* logs;
* métricas;
* evidências de segurança.

Evidências não devem conter:

* senhas;
* tokens;
* dados pessoais;
* informações classificadas;
* credenciais;
* segredos.

---

# 36. Checklist do Contribuidor

Antes de abrir o Pull Request:

```text
[ ] Consultei a Issue existente.
[ ] Entendi o problema.
[ ] Identifiquei o domínio afetado.
[ ] Verifiquei requisitos relacionados.
[ ] Verifiquei casos de uso/user stories.
[ ] Verifiquei critérios de aceitação.
[ ] Verifiquei ADRs relacionados.
[ ] Criei branch adequada.
[ ] Fiz commits objetivos.
[ ] Não incluí segredos.
[ ] Não incluí dados pessoais reais.
[ ] Implementei a alteração.
[ ] Adicionei/atualizei testes.
[ ] Executei os testes necessários.
[ ] Verifiquei segurança.
[ ] Verifiquei impacto em LGPD.
[ ] Verifiquei impacto no banco de dados.
[ ] Verifiquei APIs/integrações.
[ ] Atualizei a documentação necessária.
[ ] Verifiquei riscos.
[ ] Preparei evidências.
[ ] Preenchi o Pull Request completamente.
```

---

# 37. Checklist do Revisor

O revisor deve verificar:

```text
[ ] Issue relacionada existe.
[ ] Escopo está claro.
[ ] Solução atende ao problema.
[ ] Critérios de aceitação foram atendidos.
[ ] Rastreabilidade está adequada.
[ ] Arquitetura está preservada.
[ ] Código está adequado.
[ ] Testes são suficientes.
[ ] Segurança foi considerada.
[ ] LGPD foi considerada.
[ ] Dados estão protegidos.
[ ] APIs estão documentadas.
[ ] Migrations estão adequadas.
[ ] Documentação foi atualizada.
[ ] Não existem segredos.
[ ] Não existem dados pessoais indevidos.
[ ] Riscos foram avaliados.
[ ] Evidências são suficientes.
[ ] O PR está pronto para merge.
```

---

# 38. Contribuições de Alta Criticidade

Contribuições que afetem componentes críticos devem receber avaliação adicional.

Exemplos:

* autenticação;
* autorização;
* dados pessoais;
* folha de pagamento;
* finanças;
* tributação;
* integrações governamentais;
* banco de dados principal;
* infraestrutura;
* segurança;
* auditoria;
* publicação de dados;
* componentes de IA críticos.

O nível de revisão deve ser proporcional ao risco.

---

# 39. Vulnerabilidades de Segurança

Vulnerabilidades de segurança não devem ser necessariamente abertas como Issues públicas.

Quando uma vulnerabilidade puder ser explorada, o colaborador deve utilizar o canal de segurança definido pelo projeto.

Não devem ser publicados em Issues públicas:

* exploits funcionais;
* credenciais;
* tokens;
* dados pessoais;
* informações que permitam exploração imediata;
* detalhes operacionais sensíveis.

---

# 40. Código de Conduta

Todos os colaboradores devem agir de maneira:

* respeitosa;
* profissional;
* colaborativa;
* técnica;
* transparente;
* inclusiva.

Discordâncias técnicas devem ser tratadas com base em:

* requisitos;
* evidências;
* arquitetura;
* segurança;
* testes;
* documentação;
* impacto.

Ataques pessoais não fazem parte do processo de engenharia do SIGMUN.

---

# 41. Contribuições Rejeitadas

Uma contribuição poderá ser rejeitada quando:

* não possuir justificativa;
* não atender aos requisitos;
* introduzir risco injustificado;
* quebrar arquitetura sem decisão;
* não possuir testes adequados;
* introduzir vulnerabilidade;
* expuser informações protegidas;
* ignorar políticas corporativas;
* duplicar funcionalidade existente sem justificativa;
* aumentar complexidade sem benefício proporcional;
* não possuir documentação necessária.

A rejeição deve, sempre que possível, apresentar justificativa técnica.

---

# 42. Débito Técnico

Débitos técnicos identificados durante uma contribuição não devem ser simplesmente ignorados.

Quando não puderem ser corrigidos no mesmo trabalho, devem ser registrados em Issue própria.

Exemplo:

```text
Durante a implementação da #123 foi identificado:
- necessidade de refatoração do serviço X;
- ausência de teste Y;
- melhoria de performance Z.
```

Cada débito relevante deve possuir rastreabilidade.

---

# 43. Compatibilidade

Alterações devem considerar compatibilidade com:

* módulos existentes;
* APIs;
* banco de dados;
* integrações;
* jobs;
* tarefas Celery;
* interfaces;
* relatórios;
* processos municipais;
* migrações existentes.

Alterações incompatíveis devem ser explicitamente identificadas.

---

# 44. Versionamento

O SIGMUN deve utilizar controle de versão para:

* código;
* documentação;
* configurações versionáveis;
* migrations;
* contratos;
* schemas;
* templates;
* políticas;
* decisões arquiteturais.

Arquivos gerados automaticamente somente devem ser versionados quando houver justificativa técnica ou operacional.

---

# 45. Releases

As releases devem ser precedidas por avaliação de:

* funcionalidades;
* correções;
* testes;
* segurança;
* migrations;
* documentação;
* compatibilidade;
* riscos.

Alterações críticas podem exigir plano específico de implantação e rollback.

---

# 46. Comunicação da Comunidade

Contribuições relevantes podem ser comunicadas por meio dos canais oficiais do projeto.

Devem ser valorizadas:

* transparência;
* documentação;
* compartilhamento de conhecimento;
* registro de decisões;
* colaboração;
* reconhecimento dos contribuidores.

---

# 47. Reconhecimento de Contribuidores

Contribuições relevantes poderão ser reconhecidas conforme as políticas do ecossistema SIGMUN.

O reconhecimento pode considerar:

* código;
* documentação;
* testes;
* arquitetura;
* pesquisa;
* segurança;
* suporte;
* UX;
* governança;
* revisão;
* educação;
* melhoria comunitária.

---

# 48. Relação com os Documentos Corporativos

Este documento deve ser interpretado em conjunto com os documentos de governança e arquitetura do SIGMUN.

Entre eles:

```text
000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md
000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS.md
```

Também devem ser observadas as políticas corporativas aplicáveis, incluindo:

```text
Política de Governança Digital
Política de Qualidade
Política de Segurança
Política de Gestão Documental
Política de Retenção e Descarte de Documentos
Política de Gestão de Riscos
Política de Proteção de Dados Pessoais
Manual de Governança do SIGMUN
Política de Classificação da Informação e Publicação de Artefatos
```

---

# 49. Relação com os Templates do Repositório

O processo de contribuição é apoiado pelos seguintes artefatos:

```text
.github/
├── PULL_REQUEST_TEMPLATE.md
└── ISSUE_TEMPLATE/
    └── feature_or_bug.md
```

Esses templates não substituem este Guia.

Eles são instrumentos operacionais para aplicar as regras definidas neste documento.

O GitHub permite manter templates de Issue no diretório `.github/ISSUE_TEMPLATE` e templates de Pull Request no `.github`, `docs` ou diretório equivalente suportado.

---

# 50. Evolução dos Templates

Os templates devem evoluir juntamente com o projeto.

Sempre que uma nova necessidade de governança for identificada, deve-se avaliar a atualização de:

```text
000E-GUIA-DE-CONTRIBUICAO.md
        ↓
PULL_REQUEST_TEMPLATE.md
        ↓
feature_or_bug.md
```

Alterações estruturais nos templates devem ser tratadas como alterações de governança do processo de contribuição.

---

# 51. Configuração Recomendada do GitHub

Quando o repositório estiver configurado no GitHub, recomenda-se manter:

```text
.github/
├── PULL_REQUEST_TEMPLATE.md
├── ISSUE_TEMPLATE/
│   ├── feature_or_bug.md
│   └── config.yml
└── ...
```

O `config.yml` pode ser utilizado para controlar o comportamento do seletor de Issues, inclusive restringindo Issues em branco quando essa política for adotada.

---

# 52. Regra de Ouro

Toda contribuição significativa ao SIGMUN deve responder:

> **O que mudou?**

> **Por que mudou?**

> **Qual requisito ou problema motivou a mudança?**

> **Qual domínio foi afetado?**

> **Como a mudança foi implementada?**

> **Como foi testada?**

> **Quais riscos foram avaliados?**

> **Qual impacto existe em segurança e LGPD?**

> **Qual documentação foi atualizada?**

> **Quem revisou?**

Essa regra representa o princípio central de rastreabilidade do processo de engenharia do SIGMUN.

---

# 53. Fluxo Resumido

```text
IDEIA
  ↓
ISSUE
  ↓
ANÁLISE
  ↓
REQUISITOS / UC / US / CA
  ↓
ADR — quando aplicável
  ↓
BRANCH
  ↓
IMPLEMENTAÇÃO
  ↓
TESTES
  ↓
SEGURANÇA / LGPD
  ↓
DOCUMENTAÇÃO
  ↓
PULL REQUEST
  ↓
REVISÃO
  ↓
CORREÇÕES — quando necessárias
  ↓
APROVAÇÃO
  ↓
MERGE
  ↓
VALIDAÇÃO
  ↓
DOCUMENTAÇÃO FINAL
  ↓
RELEASE / IMPLANTAÇÃO — quando aplicável
```

---

# 54. Controle de Versão deste Documento

| Versão | Data       | Alteração                                                                                                                                                                                                                | Responsável       |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| 1.0    | —          | Versão inicial                                                                                                                                                                                                           | Governança SIGMUN |
| 2.0    | 2026-08-25 | Revisão geral; inclusão do fluxo Issue → PR → revisão → merge; integração com templates; rastreabilidade; segurança; LGPD; IA; testes; documentação; banco; APIs; Celery; SIGMUN-DEV-AGENT e governança de contribuições | Governança SIGMUN |

---

# 55. Status

**Status:** Vigente

Este documento passa a ser a referência oficial para o processo de contribuição técnica e documental do SIGMUN, devendo ser utilizado em conjunto com a Constituição do Projeto, o Padrão Corporativo de Documentação, o Framework de Gestão de Requisitos, os registros de decisões arquiteturais e as políticas corporativas aplicáveis.

---

## 56. Declaração Final

O SIGMUN é construído como um projeto público, colaborativo, sustentável e orientado à melhoria contínua da gestão municipal.

Contribuir para o SIGMUN significa não apenas escrever código.

Significa contribuir para:

* uma arquitetura sustentável;
* uma administração pública mais integrada;
* dados mais confiáveis;
* processos mais eficientes;
* maior transparência;
* maior segurança;
* melhor prestação de serviços públicos;
* conhecimento técnico compartilhado.

Por isso, toda contribuição deve buscar o equilíbrio entre:

> **valor público + qualidade técnica + segurança + governança + sustentabilidade.**

---

**SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

**Transparência por padrão. Segurança por princípio. Classificação da Informação por política.**

**Aberto sempre que possível, restrito sempre que necessário.**
