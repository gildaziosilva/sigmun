# GUIA DO COLABORADOR — SIGMUN

**Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA — SIGMUN**

---

# 1. Identificação do Documento

| Campo                           | Informação                                                                 |
| ------------------------------- | -------------------------------------------------------------------------- |
| **Título**                      | Guia do Colaborador do SIGMUN                                              |
| **Projeto**                     | SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA |
| **Classificação da Informação** | Pública                                                                    |
| **Versão**                      | 1.0                                                                        |
| **Status**                      | Vigente                                                                    |
| **Tipo**                        | Governança / Colaboração / Engenharia de Software                          |
| **Documento relacionado**       | `000E-GUIA-DE-CONTRIBUICAO.md`                                             |
| **Documento Mestre**            | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`                                    |
| **Padrão Corporativo**          | `000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md`                               |

---

# 2. Apresentação

Bem-vindo ao SIGMUN.

O SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA — é concebido como uma plataforma integrada de gestão pública municipal, orientada à integração de processos, dados, serviços, pessoas e tecnologias.

O projeto busca reduzir:

* retrabalho;
* duplicidade de informações;
* processos isolados;
* sistemas desconectados;
* inconsistências de dados;
* dependência de processos manuais;
* perda de conhecimento institucional.

Ao mesmo tempo, busca ampliar:

* eficiência administrativa;
* transparência;
* segurança;
* qualidade dos dados;
* rastreabilidade;
* integração;
* capacidade de decisão;
* qualidade dos serviços públicos.

Este Guia foi criado para ajudar novos e atuais colaboradores a compreenderem **como participar do projeto de forma segura, organizada, produtiva e alinhada à governança do SIGMUN**.

---

# 3. Para Quem Este Guia É Destinado

Este documento aplica-se a:

* desenvolvedores;
* arquitetos;
* analistas;
* especialistas de domínio;
* analistas de requisitos;
* profissionais de dados;
* profissionais de segurança;
* profissionais de UX/UI;
* profissionais de infraestrutura;
* profissionais de DevOps;
* profissionais de testes;
* pesquisadores;
* bolsistas;
* colaboradores voluntários;
* parceiros técnicos;
* colaboradores institucionais;
* revisores;
* mantenedores;
* colaboradores que utilizem Inteligência Artificial como ferramenta de apoio.

---

# 4. O Que Significa Ser Colaborador

Ser colaborador do SIGMUN não significa apenas produzir código.

Uma contribuição pode ser:

* uma funcionalidade;
* uma correção;
* uma análise;
* uma decisão arquitetural;
* um requisito;
* uma documentação;
* um teste;
* uma melhoria de segurança;
* uma melhoria de desempenho;
* uma pesquisa;
* uma integração;
* uma melhoria de UX;
* uma análise de dados;
* uma proposta de melhoria;
* uma revisão técnica.

O colaborador contribui para o **conhecimento e para a evolução do sistema**, não apenas para o código-fonte.

---

# 5. Princípios do Colaborador SIGMUN

Todo colaborador deve conhecer e respeitar os princípios fundamentais do projeto.

## 5.1. Transparência por padrão

As decisões e informações do projeto devem ser registradas e compartilhadas de maneira transparente sempre que possível.

---

## 5.2. Segurança por princípio

Segurança não deve ser tratada como etapa posterior.

Toda contribuição deve considerar segurança desde sua concepção.

---

## 5.3. Classificação da Informação por política

Nem toda informação pode ser publicada.

Antes de compartilhar qualquer informação, o colaborador deve considerar sua classificação.

---

## 5.4. Aberto sempre que possível, restrito sempre que necessário

O conhecimento técnico deve ser aberto sempre que isso não representar risco ao projeto, à Prefeitura, aos cidadãos ou à segurança institucional.

---

## 5.5. Rastreabilidade

Uma decisão importante deve poder ser explicada posteriormente.

Sempre que possível:

```text
Necessidade
    ↓
Issue
    ↓
Requisito
    ↓
Implementação
    ↓
Teste
    ↓
Pull Request
    ↓
Revisão
    ↓
Merge
```

---

## 5.6. Qualidade antes da velocidade

Uma solução rápida que introduz dívida técnica, risco de segurança ou inconsistência arquitetural pode gerar mais trabalho posteriormente.

O objetivo é produzir valor sustentável.

---

# 6. Conhecendo o SIGMUN

Antes de iniciar uma contribuição significativa, o colaborador deve compreender pelo menos:

1. a finalidade do SIGMUN;
2. a arquitetura geral;
3. os princípios do projeto;
4. a estrutura documental;
5. o domínio no qual pretende atuar;
6. as regras de contribuição;
7. as políticas de segurança;
8. os requisitos aplicáveis.

---

# 7. Primeiros Documentos a Ler

Recomenda-se a seguinte ordem inicial:

```text
01. 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
02. 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md
03. 000E-GUIA-DE-CONTRIBUICAO.md
04. GUIA-DO-COLABORADOR.md
05. 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
06. 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS.md
07. Políticas corporativas aplicáveis
08. Documentação do domínio de atuação
```

A ordem pode variar conforme a atividade do colaborador.

---

# 8. Estrutura da Documentação

A documentação principal está organizada em:

```text
SIGMUN-Docs/
│
├── 00-Governanca/
│
├── 01-Arquitetura/
│
├── 02-Modelo-de-Negocio/
│
├── 03-Requisitos/
│
├── 04-Modelo-de-Dados/
│
├── 05-Modulos/
│
├── 06-Integracoes/
│
├── 07-LGPD-e-Seguranca/
│
├── 08_Migracao/
│
├── 09-UX/
│
├── 10-Testes/
│
├── 11-Implantacao/
│
└── 99-Anexos/
```

O colaborador deve evitar criar documentos fora da estrutura definida sem necessidade.

---

# 9. Antes de Começar uma Tarefa

Antes de iniciar uma tarefa, faça:

* [ ] Verifique se existe uma Issue relacionada.
* [ ] Leia a documentação do domínio.
* [ ] Verifique requisitos existentes.
* [ ] Verifique casos de uso.
* [ ] Verifique histórias de usuário.
* [ ] Verifique critérios de aceitação.
* [ ] Verifique ADRs relacionadas.
* [ ] Verifique alterações ou implementações existentes.
* [ ] Verifique dependências.
* [ ] Avalie impacto em outros domínios.
* [ ] Avalie segurança e LGPD quando aplicável.

---

# 10. Não Comece Pelo Código

Uma das principais orientações deste Guia é:

> **Antes de implementar, compreenda o problema.**

Evite começar diretamente criando arquivos ou escrevendo código.

Primeiro descubra:

```text
Qual problema estamos resolvendo?
        ↓
Quem é afetado?
        ↓
Qual requisito está relacionado?
        ↓
Qual domínio é responsável?
        ↓
Qual comportamento é esperado?
        ↓
Quais regras de negócio existem?
        ↓
Como a arquitetura deve tratar o problema?
```

Somente então comece a implementação.

---

# 11. Issues

A Issue é o ponto de entrada padrão para demandas do projeto.

O SIGMUN utiliza:

```text
.github/ISSUE_TEMPLATE/feature_or_bug.md
```

A Issue deve registrar, conforme aplicável:

* problema;
* contexto;
* objetivo;
* escopo;
* requisitos;
* casos de uso;
* histórias de usuário;
* critérios de aceitação;
* domínio;
* impactos;
* riscos;
* segurança;
* dados;
* integrações;
* arquitetura;
* documentação.

---

# 12. Como Criar uma Boa Issue

Uma boa Issue deve permitir que outra pessoa compreenda a demanda sem precisar perguntar repetidamente:

> O que está acontecendo?

> Por que isso é necessário?

> O que deve acontecer?

> Como saberemos que está correto?

Evite Issues vagas como:

```text
"Melhorar compras"

"Arrumar cadastro"

"Fazer API"

"Corrigir sistema"
```

Prefira:

```text
"Permitir validação automática da modalidade de contratação
antes da criação do processo de compra."
```

Quanto mais clara a demanda, menor a ambiguidade durante a implementação.

---

# 13. Priorização

As prioridades devem ser utilizadas de forma responsável.

## Crítica

Problema que:

* impede operação essencial;
* compromete segurança;
* pode causar perda significativa de dados;
* causa indisponibilidade crítica;
* apresenta risco institucional elevado.

## Alta

Problema ou necessidade com impacto relevante no negócio ou na operação.

## Média

Importante, mas sem impacto imediato crítico.

## Baixa

Melhoria ou necessidade que pode aguardar priorização posterior.

A prioridade pode ser alterada conforme novas informações.

---

# 14. Branches

Cada colaborador deve trabalhar preferencialmente em branch própria.

Exemplos:

```text
feature/descricao
bugfix/descricao
hotfix/descricao
refactor/descricao
docs/descricao
test/descricao
security/descricao
chore/descricao
```

Exemplo:

```text
feature/cadastro-fornecedor
```

---

# 15. Commits

Os commits devem ser objetivos e representar mudanças compreensíveis.

Quando adotado pelo projeto, utilizar Conventional Commits.

Exemplos:

```text
feat(compras): adiciona cadastro de fornecedor

fix(compras): corrige validação de fornecedor

test(compras): adiciona testes de cadastro

docs(compras): atualiza documentação do domínio

security(api): corrige validação de autorização
```

Evite:

```text
mudanças
ajustes
teste
coisas
final
final2
agora vai
```

---

# 16. Código Limpo

O colaborador deve buscar código:

* simples;
* legível;
* testável;
* coeso;
* previsível;
* documentado quando necessário.

Evite complexidade sem benefício claro.

---

# 17. Respeito aos Domínios

O SIGMUN é organizado por domínios.

Cada domínio deve manter suas responsabilidades.

Evite:

* regras de negócio espalhadas;
* acesso direto ao banco de outro domínio;
* dependências ocultas;
* duplicação de regras;
* integração informal entre componentes.

Quando dois domínios precisarem conversar, utilize mecanismos arquiteturalmente definidos.

---

# 18. Alterações de Arquitetura

Nem toda alteração precisa de ADR.

Entretanto, mudanças significativas devem ser avaliadas.

Exemplos:

* mudança de padrão arquitetural;
* introdução de componente crítico;
* alteração de comunicação entre domínios;
* alteração importante de persistência;
* alteração de segurança;
* nova tecnologia estratégica;
* mudança de estratégia de integração.

Quando necessário:

```text
Issue
  ↓
Análise
  ↓
ADR
  ↓
Implementação
```

---

# 19. Banco de Dados

Alterações no banco devem ser feitas de maneira versionada.

Sempre que aplicável:

```text
Modelo de dados
      ↓
Migration
      ↓
Teste
      ↓
Pull Request
```

Não utilize alterações manuais em produção como substituição das migrations versionadas.

Considere:

* compatibilidade;
* integridade;
* índices;
* constraints;
* performance;
* dados existentes;
* rollback;
* auditoria.

---

# 20. APIs

Toda API deve possuir contrato claro.

O colaborador deve considerar:

* endpoint;
* método;
* entrada;
* saída;
* erros;
* autenticação;
* autorização;
* versionamento;
* compatibilidade.

Alterações incompatíveis devem ser identificadas claramente.

---

# 21. Integrações

Integrações devem possuir:

* contrato;
* responsável;
* autenticação;
* tratamento de erros;
* observabilidade;
* documentação.

Nunca introduza uma integração crítica sem compreender seus impactos.

---

# 22. Tarefas Assíncronas e Celery

Quando trabalhar com tarefas Celery, considere:

* idempotência;
* retries;
* timeout;
* filas;
* workers;
* prioridade;
* periodicidade;
* tratamento de falhas;
* observabilidade;
* concorrência.

Uma tarefa assíncrona deve poder falhar de maneira controlada.

Evite criar tarefas que executem operações duplicadas quando forem reprocessadas.

---

# 23. Testes

O colaborador é responsável por testar suas alterações.

Dependendo da situação:

* testes unitários;
* testes de integração;
* testes de API;
* testes de contrato;
* testes de aceitação;
* testes de segurança;
* testes de migração;
* testes de regressão;
* testes de performance.

Não basta afirmar:

> "Funcionou na minha máquina."

A alteração deve possuir evidência adequada.

---

# 24. Dados de Teste

Utilize preferencialmente:

* dados sintéticos;
* dados fictícios;
* dados anonimizados.

Nunca publique inadvertidamente:

* CPF;
* RG;
* endereço pessoal;
* telefone pessoal;
* informações funcionais;
* dados financeiros;
* dados de saúde;
* credenciais;
* outros dados protegidos.

---

# 25. Segurança

Todo colaborador deve pensar em segurança.

Verifique:

* autenticação;
* autorização;
* permissões;
* validação;
* exposição de dados;
* logs;
* dependências;
* APIs;
* configurações;
* segredos.

---

# 26. Segredos

Nunca coloque no Git:

```text
.env
passwords
tokens
API keys
private keys
certificados privados
credenciais
```

Também não coloque segredos em:

* Issues;
* Pull Requests;
* documentação pública;
* screenshots;
* logs;
* exemplos de API.

---

# 27. LGPD

Ao trabalhar com dados pessoais:

1. identifique os dados;
2. avalie a finalidade;
3. minimize os dados;
4. evite exposição desnecessária;
5. utilize dados sintéticos em testes;
6. considere retenção e descarte;
7. avalie classificação da informação.

Em caso de dúvida, interrompa a publicação e solicite avaliação adequada.

---

# 28. Documentação

Documentação faz parte da implementação.

Se uma alteração modificar o comportamento do sistema, pergunte:

> A documentação ainda está correta?

Se não estiver, atualize-a no mesmo trabalho quando possível.

---

# 29. Pull Requests

Toda contribuição significativa deve passar pelo Pull Request.

O SIGMUN utiliza:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

O colaborador deve preencher o template completamente.

Não deixe campos importantes vazios sem justificativa.

---

# 30. Revisão de Código

A revisão não é uma crítica pessoal.

É uma etapa de qualidade.

O revisor deve avaliar:

* funcionalidade;
* arquitetura;
* código;
* testes;
* segurança;
* LGPD;
* documentação;
* riscos;
* operação.

O autor deve receber comentários como contribuição para melhoria.

---

# 31. Como Receber uma Revisão

Ao receber uma sugestão:

1. leia com atenção;
2. procure compreender a preocupação;
3. responda tecnicamente;
4. faça a alteração quando apropriado;
5. explique quando discordar;
6. evite discussões pessoais.

Uma discordância técnica deve ser resolvida por:

* requisitos;
* arquitetura;
* testes;
* evidências;
* segurança;
* decisão registrada.

---

# 32. Inteligência Artificial

O uso de IA é permitido como ferramenta de apoio.

Pode ser utilizada para:

* estudar tecnologias;
* pesquisar alternativas;
* gerar rascunhos;
* auxiliar programação;
* gerar testes;
* revisar código;
* produzir documentação;
* explicar erros;
* auxiliar refatorações.

Entretanto:

> **IA não substitui a responsabilidade técnica do colaborador.**

---

# 33. SIGMUN-DEV-AGENT

O `SIGMUN-DEV-AGENT` pode ser utilizado como agente especializado de apoio ao desenvolvimento.

Antes de aceitar uma alteração produzida ou sugerida pelo agente:

* leia o código;
* compreenda a solução;
* valide a arquitetura;
* execute os testes;
* verifique segurança;
* verifique dependências;
* confira a documentação.

---

# 34. O Que Não Enviar Para Uma IA

Não forneça a ferramentas de IA:

* senhas;
* tokens;
* chaves privadas;
* credenciais;
* dados pessoais reais;
* dados classificados;
* dumps reais de banco;
* informações institucionais protegidas.

Quando necessário, substitua os dados por exemplos fictícios.

---

# 35. Comunicação

O colaborador deve utilizar comunicação:

* clara;
* objetiva;
* respeitosa;
* técnica;
* construtiva.

Evite:

* ataques pessoais;
* sarcasmo destrutivo;
* acusações sem evidências;
* discussões improdutivas;
* decisões importantes apenas por conversa privada.

Decisões relevantes devem ser registradas no local apropriado.

---

# 36. Comunicação Pública

Antes de publicar qualquer conteúdo relacionado ao SIGMUN:

* verifique a classificação da informação;
* remova dados pessoais;
* remova segredos;
* remova informações operacionais sensíveis;
* confirme se a publicação é permitida.

O fato de uma informação estar disponível internamente não significa automaticamente que ela possa ser publicada externamente.

---

# 37. Dúvidas

Ter dúvidas é normal.

Quando não souber como proceder:

1. consulte a documentação;
2. procure Issues existentes;
3. procure ADRs;
4. procure implementações semelhantes;
5. consulte o responsável pelo domínio;
6. registre a dúvida na Issue quando ela for relevante.

Não tenha receio de perguntar.

Uma dúvida registrada pode evitar dezenas de horas de retrabalho.

---

# 38. Quando Criar uma Nova Issue

Crie uma nova Issue quando identificar:

* bug;
* nova funcionalidade;
* melhoria;
* débito técnico relevante;
* risco;
* necessidade arquitetural;
* necessidade documental;
* vulnerabilidade;
* necessidade de pesquisa;
* problema operacional.

Não esconda problemas para "resolver depois".

Problemas relevantes devem possuir rastreabilidade.

---

# 39. Débito Técnico

Se durante uma tarefa você encontrar algo que não possa ser corrigido naquele momento:

1. registre o problema;
2. avalie sua criticidade;
3. crie Issue quando necessário;
4. relacione-a à tarefa atual.

Exemplo:

```text
Durante a implementação da #123 foi identificado
um problema de performance no componente X.

Nova Issue: #145
```

---

# 40. Não Faça Alterações Fora do Escopo

Evite transformar uma Issue simples em uma grande refatoração sem planejamento.

Se encontrar algo que merece outra alteração:

```text
Issue atual
    ↓
Problema adicional
    ↓
Nova Issue
```

A exceção é quando a alteração adicional for necessária para implementar corretamente a demanda original.

---

# 41. Dependências

Antes de adicionar uma biblioteca:

* verifique se ela é realmente necessária;
* verifique manutenção;
* verifique licença;
* verifique segurança;
* verifique compatibilidade;
* verifique impacto no projeto.

Evite adicionar dependências para resolver problemas simples que podem ser resolvidos com recursos já disponíveis.

---

# 42. Performance

Performance deve ser considerada quando relevante.

Observe:

* consultas ao banco;
* chamadas externas;
* processamento em lote;
* memória;
* concorrência;
* filas;
* tarefas assíncronas;
* APIs;
* índices.

Não faça otimizações prematuras sem evidências.

Quando o problema for performance, procure medir antes e depois.

---

# 43. Observabilidade

Sistemas públicos precisam ser observáveis.

Considere:

* logs;
* métricas;
* tracing;
* health checks;
* alertas;
* monitoramento.

Logs devem ajudar a diagnosticar problemas sem expor informações protegidas.

---

# 44. Homologação

Quando a alteração exigir homologação:

1. prepare ambiente adequado;
2. utilize dados apropriados;
3. execute os cenários previstos;
4. registre evidências;
5. registre problemas encontrados;
6. atualize a Issue/PR.

---

# 45. Produção

Nenhum colaborador deve realizar alterações de produção fora dos procedimentos definidos pelo projeto.

Alterações de produção devem considerar:

* autorização;
* janela de implantação;
* backup quando aplicável;
* migration;
* monitoramento;
* rollback;
* evidências.

---

# 46. Rollback

Antes de uma alteração relevante, pergunte:

> Se algo der errado, como voltaremos ao estado anterior?

Quando necessário, documente:

* procedimento;
* dependências;
* migrations;
* configuração;
* impacto;
* responsáveis.

---

# 47. Regras para Emergências

Em situações críticas, pode ser necessário utilizar procedimentos excepcionais.

Mesmo assim:

> **Emergência não significa ausência de rastreabilidade.**

Após uma intervenção emergencial, deve ser registrada:

* causa;
* alteração;
* responsável;
* impacto;
* solução;
* ações corretivas;
* documentação necessária.

---

# 48. Contribuições de Documentação

Documentação também é contribuição técnica.

Você pode contribuir corrigindo:

* erros;
* links;
* conceitos;
* requisitos;
* diagramas;
* exemplos;
* procedimentos;
* arquitetura.

Não é necessário ser desenvolvedor para contribuir com o SIGMUN.

---

# 49. Contribuições de Pesquisa

Pesquisas podem ajudar o projeto a avaliar:

* tecnologias;
* padrões;
* legislação;
* soluções;
* arquitetura;
* interoperabilidade;
* segurança;
* dados;
* IA;
* transformação digital.

Resultados relevantes devem ser documentados para evitar perda de conhecimento.

---

# 50. Conhecimento Institucional

O SIGMUN deve evitar depender exclusivamente da memória de uma pessoa.

Quando um colaborador descobrir algo importante:

> **Documente.**

Conhecimento relevante deve ser transformado em:

* documentação;
* Issue;
* ADR;
* requisito;
* procedimento;
* exemplo;
* teste.

---

# 51. Reconhecimento

O projeto valoriza contribuições em diferentes áreas.

Podem ser reconhecidas contribuições de:

* código;
* arquitetura;
* requisitos;
* documentação;
* testes;
* segurança;
* UX;
* dados;
* infraestrutura;
* pesquisa;
* suporte;
* revisão;
* educação;
* governança.

Contribuir não significa necessariamente escrever código.

---

# 52. Conduta

Espera-se de todos os colaboradores:

* respeito;
* honestidade;
* responsabilidade;
* colaboração;
* transparência;
* profissionalismo;
* compromisso com a qualidade.

Problemas técnicos devem ser discutidos tecnicamente.

---

# 53. Checklist do Novo Colaborador

Ao entrar no projeto:

* [ ] Li a Constituição do SIGMUN.
* [ ] Li o Padrão Corporativo de Documentação.
* [ ] Li o Guia de Contribuição.
* [ ] Li este Guia do Colaborador.
* [ ] Conheci a estrutura do repositório.
* [ ] Conheci a estrutura documental.
* [ ] Identifiquei o domínio em que vou atuar.
* [ ] Li a documentação do domínio.
* [ ] Conheci o fluxo de Issue.
* [ ] Conheci o fluxo de Pull Request.
* [ ] Conheci as regras de segurança.
* [ ] Conheci as regras de LGPD.
* [ ] Conheci as regras de uso de IA.
* [ ] Configurei meu ambiente de desenvolvimento.
* [ ] Executei os testes básicos do projeto.
* [ ] Sei onde pedir ajuda.

---

# 54. Checklist Antes da Primeira Contribuição

* [ ] Existe uma Issue?
* [ ] O problema está claramente descrito?
* [ ] O domínio está identificado?
* [ ] Os requisitos foram consultados?
* [ ] Os critérios de aceitação estão claros?
* [ ] A arquitetura foi consultada?
* [ ] Existe ADR relacionada?
* [ ] Os impactos foram avaliados?
* [ ] Segurança foi considerada?
* [ ] LGPD foi considerada?
* [ ] Criei uma branch própria?
* [ ] Sei quais testes preciso executar?

---

# 55. Checklist Antes do Pull Request

* [ ] Implementação concluída.
* [ ] Critérios de aceitação atendidos.
* [ ] Testes executados.
* [ ] Código revisado pelo próprio autor.
* [ ] Segurança avaliada.
* [ ] LGPD avaliada quando aplicável.
* [ ] Migrations verificadas quando aplicável.
* [ ] APIs verificadas quando aplicável.
* [ ] Integrações verificadas quando aplicável.
* [ ] Celery/tarefas assíncronas verificadas quando aplicável.
* [ ] Documentação atualizada.
* [ ] Rastreabilidade preservada.
* [ ] Evidências preparadas.
* [ ] Riscos identificados.
* [ ] `PULL_REQUEST_TEMPLATE.md` preenchido.

---

# 56. Checklist Antes do Merge

* [ ] PR revisado.
* [ ] Comentários resolvidos.
* [ ] Testes aprovados.
* [ ] Segurança aprovada quando aplicável.
* [ ] Documentação aprovada quando necessária.
* [ ] ADR criada/atualizada quando necessária.
* [ ] Migration validada quando aplicável.
* [ ] Rollback considerado.
* [ ] Homologação concluída quando aplicável.
* [ ] Não existem pendências críticas.
* [ ] Issue corretamente vinculada.

---

# 57. Fluxo Completo do Colaborador

O fluxo recomendado é:

```text
ENTENDER
   ↓
DOCUMENTAR
   ↓
ISSUE
   ↓
ANALISAR
   ↓
PLANEJAR
   ↓
BRANCH
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
DOCUMENTAR
   ↓
PULL REQUEST
   ↓
REVISAR
   ↓
CORRIGIR
   ↓
APROVAR
   ↓
MERGE
   ↓
HOMOLOGAR
   ↓
IMPLANTAR
   ↓
OBSERVAR
   ↓
APRENDER
```

---

# 58. O Ciclo de Melhoria Contínua

O trabalho não termina necessariamente no merge.

Após a implantação:

```text
Implantar
    ↓
Observar
    ↓
Medir
    ↓
Identificar problemas
    ↓
Aprender
    ↓
Documentar
    ↓
Melhorar
```

O SIGMUN deve evoluir continuamente com base em evidências.

---

# 59. Relação com o Guia de Contribuição

Este Guia explica **como trabalhar como colaborador**.

O `000E-GUIA-DE-CONTRIBUICAO.md` define **as regras formais para contribuir**.

Portanto:

```text
GUIA DO COLABORADOR
        │
        │ Como participar
        ▼
000E — GUIA DE CONTRIBUIÇÃO
        │
        │ Regras do processo
        ▼
ISSUE
        │
        ▼
IMPLEMENTAÇÃO
        │
        ▼
PULL REQUEST
        │
        ▼
REVISÃO
        │
        ▼
MERGE
```

---

# 60. Relação com os Templates

Os principais instrumentos operacionais são:

```text
.github/
│
├── PULL_REQUEST_TEMPLATE.md
│
└── ISSUE_TEMPLATE/
    └── feature_or_bug.md
```

O colaborador deve utilizar esses templates para manter a padronização do projeto.

---

# 61. Regra de Ouro do Colaborador

Antes de alterar qualquer coisa, pergunte:

> **Eu entendo o problema?**

Antes de implementar:

> **Eu sei qual requisito estou atendendo?**

Antes de abrir o PR:

> **Eu consigo provar que funciona?**

Antes do merge:

> **Outra pessoa consegue compreender o que foi feito e por quê?**

Antes de publicar:

> **Esta informação pode ser divulgada?**

Antes de usar IA:

> **Estou protegendo as informações do projeto?**

---

# 62. Cultura SIGMUN

O SIGMUN deve ser construído como uma comunidade de conhecimento.

Por isso:

> **Não esconda conhecimento. Documente.**

> **Não esconda problemas. Registre.**

> **Não esconda riscos. Comunique.**

> **Não copie soluções sem compreender. Estude.**

> **Não aceite código que você não entende. Revise.**

> **Não publique informações sem verificar sua classificação.**

> **Não confunda velocidade com qualidade.**

---

# 63. Encerramento

O SIGMUN é maior que seu código-fonte.

É um conjunto de:

* processos;
* dados;
* regras;
* documentos;
* decisões;
* tecnologias;
* pessoas;
* conhecimento;
* experiências;
* políticas;
* serviços públicos.

Cada colaborador ajuda a construir esse patrimônio.

Uma boa contribuição não é apenas aquela que funciona.

É aquela que:

* resolve o problema correto;
* respeita a arquitetura;
* pode ser testada;
* pode ser compreendida;
* pode ser mantida;
* é segura;
* é documentada;
* possui rastreabilidade;
* gera conhecimento para os próximos colaboradores.

---

# 64. Referências

Documentos principais:

```text
000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md

000E-GUIA-DE-CONTRIBUICAO.md

000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md

000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS.md
```

Templates:

```text
.github/PULL_REQUEST_TEMPLATE.md

.github/ISSUE_TEMPLATE/feature_or_bug.md
```

Políticas corporativas aplicáveis:

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

# 65. Controle de Versão

| Versão | Data       | Alteração                      |
| ------ | ---------- | ------------------------------ |
| 1.0    | 2026-08-26 | Criação do Guia do Colaborador |

---

# 66. Declaração Final

**SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

**Transparência por padrão. Segurança por princípio. Classificação da Informação por política.**

**Aberto sempre que possível, restrito sempre que necessário.**

> **Construir o SIGMUN é construir conhecimento, tecnologia e capacidade institucional para o município.**
