# 000 — Especificação do SIGMUN-DEV-AGENT

**Projeto:** SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA

**Classificação da Informação:** Pública

**Documento:** Especificação do SIGMUN-DEV-AGENT

**Código:** SIGMUN-DEV-AGENT-000

**Versão:** 1.0

**Status:** Proposto

**Data:** 2026-08-25

**Responsável:** Arquitetura Corporativa do SIGMUN

---

# 1. Objetivo

O SIGMUN-DEV-AGENT é uma capacidade técnica destinada a apoiar, automatizar e orquestrar atividades de desenvolvimento, manutenção, análise, testes e evolução do projeto SIGMUN por meio de modelos de inteligência artificial executados localmente.

O componente utilizará inicialmente o Ollama como infraestrutura local de execução de modelos de linguagem, permitindo a utilização de modelos gratuitos e/ou de código aberto compatíveis com o ambiente técnico do projeto.

O objetivo não é substituir o desenvolvedor ou a governança técnica do SIGMUN.

O objetivo é criar um agente de engenharia controlado, contextualizado pela documentação oficial do projeto e submetido às políticas de segurança, rastreabilidade e governança do SIGMUN.

---

# 2. Motivação

O SIGMUN possui uma grande base documental composta por:

- arquitetura corporativa;
- requisitos;
- modelos de domínio;
- modelos de dados;
- processos;
- serviços;
- regras de negócio;
- segurança;
- auditoria;
- testes;
- implantação;
- operação;
- ADRs;
- políticas corporativas;
- documentação técnica.

A quantidade e a interdependência desses artefatos tornam importante a existência de uma capacidade automatizada capaz de:

- localizar informações relevantes;
- interpretar documentação;
- analisar o código;
- identificar inconsistências;
- apoiar implementação;
- executar verificações;
- executar testes;
- analisar resultados;
- sugerir correções;
- manter rastreabilidade;
- auxiliar na evolução do projeto.

---

# 3. Princípios

O SIGMUN-DEV-AGENT deverá obedecer aos seguintes princípios:

1. **Documentação antes da implementação.**
2. **Contexto antes da decisão.**
3. **Proposta antes da execução.**
4. **Autorização antes de operações sensíveis.**
5. **Rastreabilidade de todas as ações relevantes.**
6. **Segurança por padrão.**
7. **Privilégio mínimo.**
8. **Execução local sempre que possível.**
9. **Nenhuma alteração destrutiva sem autorização explícita.**
10. **Testes antes da conclusão de uma tarefa.**
11. **Código e documentação devem permanecer coerentes.**
12. **Decisões arquiteturais devem ser registradas.**
13. **O agente não deve substituir a governança humana.**
14. **Toda automação deve ser reversível sempre que possível.**
15. **O agente deve respeitar os padrões corporativos do SIGMUN.**

---

# 4. Escopo

O SIGMUN-DEV-AGENT poderá atuar nas seguintes áreas:

- análise do projeto;
- análise da documentação;
- busca contextual;
- análise de requisitos;
- análise de código;
- geração de código;
- refatoração;
- geração de testes;
- execução de testes;
- análise de falhas;
- análise de logs;
- validação de migrações;
- análise de APIs;
- análise de contratos;
- verificação de padrões;
- documentação técnica;
- análise de dependências;
- análise de Git;
- preparação de commits;
- preparação de ADRs;
- apoio à revisão de código;
- apoio à manutenção.

---

# 5. Fora do Escopo Inicial

Na primeira versão o agente não deverá:

- realizar `git push` automaticamente;
- excluir o repositório;
- executar comandos destrutivos sem autorização;
- alterar produção automaticamente;
- realizar deploy em produção autonomamente;
- modificar políticas corporativas;
- alterar documentos normativos sem aprovação;
- alterar arquitetura sem registro de decisão;
- acessar credenciais secretas sem mecanismo formal de autorização;
- executar comandos arbitrários fornecidos pelo modelo;
- conceder privilégios a si próprio.

---

# 6. Arquitetura Conceitual

A arquitetura inicial será:

```text
                    DESENVOLVEDOR
                         │
                         ▼
                ┌──────────────────┐
                │ SIGMUN-DEV-AGENT │
                └────────┬─────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     Contexto        Policy Engine    Tool Registry
          │              │              │
          ▼              ▼              ▼
    SIGMUN-Docs       Permissões      Git
    Código            Segurança       Python
    ADRs              Autorização     Pytest
    Requisitos        Auditoria       Ruff
    Roadmap                           Alembic
                                      Docker
                                      etc.
                         │
                         ▼
                     OLLAMA
                         │
                         ▼
                 MODELO LOCAL DE IA

7. Componentes
7.1 Interface do Agente

Responsável pela interação com o desenvolvedor.

Inicialmente poderá existir como:

CLI;
API local;
integração com ambiente de desenvolvimento.

A primeira implementação deverá priorizar CLI para reduzir complexidade.

7.2 Context Manager

Responsável por fornecer contexto relevante ao modelo.

Fontes:

SIGMUN-Docs/;
código-fonte;
configurações;
ADRs;
ROADMAP;
Mapa de Domínios;
requisitos;
testes;
documentação técnica.

O contexto deverá ser selecionado conforme a tarefa.

O agente não deverá carregar indiscriminadamente toda a documentação em cada interação.

7.3 Policy Engine

Responsável por determinar o que o agente pode executar.

Exemplo:

READ
  permitido

ANALYZE
  permitido

PROPOSE
  permitido

WRITE
  requer autorização

TEST
  permitido

GIT DIFF
  permitido

GIT COMMIT
  requer autorização

GIT PUSH
  proibido inicialmente

DEPLOY
  requer autorização explícita
7.4 Tool Registry

As ferramentas disponíveis ao agente deverão ser registradas formalmente.

Exemplos:

read_file
search_docs
search_code
git_status
git_diff
git_log
run_pytest
run_ruff
run_mypy
run_alembic_check
inspect_database
run_docker
inspect_logs

Cada ferramenta deverá possuir:

nome;
finalidade;
parâmetros;
permissões;
nível de risco;
resultado esperado;
mecanismo de auditoria.
8. Ollama

O Ollama será utilizado como infraestrutura local para execução dos modelos de IA.

A arquitetura deverá permitir a substituição do modelo sem alteração significativa da camada de ferramentas.

Conceitualmente:

SIGMUN-DEV-AGENT
       │
       ▼
   Model Adapter
       │
       ▼
     Ollama
       │
       ├── Modelo geral
       │
       └── Modelo especializado em código

A configuração deverá permitir definir o modelo por função.

Exemplo:

provider: ollama

models:
  general: qwen3
  coding: qwen3-coder

Os modelos efetivamente adotados deverão ser definidos posteriormente conforme:

memória disponível;
CPU;
GPU;
desempenho;
qualidade;
capacidade de tool calling;
contexto;
licença;
estabilidade.
9. Tool Calling

O SIGMUN-DEV-AGENT deverá utilizar mecanismos de tool calling quando suportados pelo modelo selecionado.

O fluxo esperado será:

Tarefa
  ↓
Modelo
  ↓
Solicitação de ferramenta
  ↓
Policy Engine
  ↓
Autorização
  ↓
Execução
  ↓
Resultado
  ↓
Modelo
  ↓
Próxima decisão

O modelo nunca deverá executar diretamente comandos do sistema.

Todas as operações deverão passar pelo Tool Registry e pelo Policy Engine.

10. Níveis de Autonomia

O agente deverá possuir níveis progressivos de autonomia.

Nível 0 — Consulta

Pode:

ler;
pesquisar;
explicar;
analisar.

Não pode alterar arquivos.

Nível 1 — Proposição

Pode:

analisar;
gerar código;
propor alterações;
produzir diffs.

As alterações ainda não são aplicadas automaticamente.

Nível 2 — Execução Controlada

Pode:

criar arquivos;
alterar arquivos autorizados;
executar testes;
executar ferramentas de qualidade.

Operações sensíveis exigem autorização.

Nível 3 — Desenvolvimento Assistido

Pode executar uma sequência de tarefas previamente autorizadas.

Exemplo:

analisar
→ implementar
→ testar
→ corrigir
→ testar novamente
Nível 4 — Orquestração

Poderá futuramente:

coordenar múltiplas ferramentas;
acompanhar tarefas;
executar pipelines;
preparar commits;
atualizar documentação;
produzir relatórios.

Este nível não faz parte da implementação inicial.

11. Segurança

O SIGMUN-DEV-AGENT deverá aplicar:

princípio do menor privilégio;
isolamento de processos quando possível;
allowlist de ferramentas;
allowlist de diretórios;
bloqueio de comandos perigosos;
proteção de segredos;
auditoria;
logs;
aprovação humana para operações críticas.
12. Operações de Alto Risco

Deverão exigir aprovação explícita:

git commit
git push
git reset
git checkout destrutivo
rm
alterações de banco destrutivas
alembic downgrade
docker prune
deploy
alterações de infraestrutura
alterações de secrets

O agente deverá informar:

operação;
arquivos afetados;
impacto esperado;
riscos;
comando ou ação;
necessidade de autorização.
13. Rastreabilidade

Cada tarefa relevante deverá possuir:

Tarefa
  ↓
Contexto utilizado
  ↓
Requisitos relacionados
  ↓
Arquivos alterados
  ↓
Ferramentas executadas
  ↓
Testes executados
  ↓
Resultado

Quando aplicável, deverá ser possível relacionar:

Requisito
    ↓
Caso de Uso
    ↓
Código
    ↓
Teste
    ↓
Evidência
14. Integração com SIGMUN-Docs

A documentação oficial será considerada fonte primária para decisões de implementação.

O agente deverá priorizar:

documentação normativa;
arquitetura corporativa;
ADRs;
requisitos;
documentação do domínio;
código existente;
testes;
demais artefatos técnicos.

Quando houver conflito entre documentação e código, o agente deverá sinalizar a inconsistência em vez de assumir silenciosamente qual está correto.

15. RAG e Busca Contextual

O agente poderá utilizar uma camada de recuperação contextual sobre SIGMUN-Docs.

Arquitetura:

SIGMUN-Docs
     │
     ▼
Indexação
     │
     ▼
Embeddings
     │
     ▼
Vector Store
     │
     ▼
Busca contextual
     │
     ▼
Contexto
     │
     ▼
Ollama

A tecnologia específica da camada vetorial será definida posteriormente.

16. Integração com Git

O agente deverá inicialmente possuir acesso de leitura a:

git status
git log
git diff
git branch
git show

Operações de escrita deverão ser controladas.

Inicialmente:

git commit  → aprovação
git push    → bloqueado
17. Integração com Testes

O agente deverá ser capaz de executar, quando autorizadas:

pytest
ruff
mypy
alembic

O resultado deverá ser incorporado ao contexto do agente.

Exemplo:

Implementação
      ↓
Testes
      ↓
Falha
      ↓
Análise
      ↓
Correção
      ↓
Novo teste
18. Integração com Banco de Dados

O agente poderá futuramente:

verificar estrutura;
validar migrações;
analisar modelos;
verificar índices;
validar constraints;
comparar modelo lógico e físico.

Operações destrutivas deverão permanecer protegidas.

19. Integração com Docker

O agente poderá:

analisar Dockerfile;
analisar docker-compose;
executar containers de desenvolvimento;
verificar logs;
executar testes em containers.

Operações destrutivas deverão exigir autorização.

20. Auditoria do Agente

Todas as ações relevantes deverão gerar registro.

Exemplo:

{
  "timestamp": "...",
  "agent": "SIGMUN-DEV-AGENT",
  "task": "...",
  "tool": "run_pytest",
  "authorization": "automatic",
  "result": "success"
}

A auditoria deverá permitir reconstruir a sequência de execução.

21. Estrutura Inicial do Componente

Sugestão:

sigmun-dev-agent/
├── README.md
├── pyproject.toml
├── src/
│   └── sigmun_dev_agent/
│       ├── __init__.py
│       ├── cli.py
│       ├── agent.py
│       ├── config.py
│       ├── context/
│       ├── models/
│       ├── policies/
│       ├── tools/
│       ├── ollama/
│       ├── git/
│       ├── testing/
│       ├── audit/
│       └── security/
└── tests/

A estrutura definitiva deverá ser compatibilizada com a arquitetura técnica vigente do SIGMUN.

22. Primeiro MVP

O primeiro MVP deverá possuir somente:

conexão com Ollama;
seleção de modelo;
leitura de SIGMUN-Docs;
leitura controlada do código;
busca textual;
git status;
git diff;
execução de pytest;
execução de ruff;
geração de propostas;
registro de ações;
autorização para escrita.

Não deverá possuir autonomia de produção.

23. Primeiro Caso de Uso

O primeiro caso de uso recomendado será:

Analisar uma tarefa de desenvolvimento do SIGMUN, consultar a documentação correspondente, analisar o código existente, propor uma implementação, executar testes autorizados e apresentar um relatório de resultado.

Exemplo:

Usuário:

"Analise o estado atual do DOM-COMPRAS-001
e diga qual é a próxima implementação recomendada."

Fluxo:

SIGMUN-DEV-AGENT
        │
        ├── consulta ROADMAP
        ├── consulta domínio
        ├── consulta requisitos
        ├── consulta modelo de dados
        ├── analisa código
        ├── verifica Git
        ├── identifica lacunas
        │
        ▼
Relatório
        │
        ├── situação atual
        ├── documentação relevante
        ├── próxima tarefa
        ├── arquivos envolvidos
        ├── dependências
        └── riscos
24. Evolução Planejada

A evolução deverá ocorrer em etapas.

Fase 1

Agente consultivo.

Fase 2

Agente analítico.

Fase 3

Agente de desenvolvimento controlado.

Fase 4

Agente de testes e validação.

Fase 5

Agente de documentação e rastreabilidade.

Fase 6

Orquestração de ferramentas.

Fase 7

Integração com CI/CD.

Fase 8

Orquestração avançada do ambiente de desenvolvimento.

25. Critérios de Aceitação do MVP

O MVP será considerado concluído quando:

conseguir conectar-se ao Ollama;
conseguir selecionar um modelo;
conseguir consultar a documentação;
conseguir analisar código;
conseguir executar ferramentas autorizadas;
conseguir executar testes;
conseguir analisar resultados;
conseguir gerar propostas;
impedir operações proibidas;
registrar ações;
preservar rastreabilidade;
não executar operações destrutivas sem autorização.
26. Riscos

Principais riscos:

alucinação do modelo;
interpretação incorreta da documentação;
execução de comandos inadequados;
alterações indevidas;
exposição de segredos;
excesso de autonomia;
dependência excessiva do modelo;
degradação da qualidade do código;
contexto insuficiente;
inconsistência entre documentação e código;
consumo elevado de recursos locais.
27. Mitigações

Os riscos deverão ser tratados por:

contexto documental;
RAG;
validação humana;
testes automatizados;
Policy Engine;
allowlists;
isolamento;
auditoria;
logs;
revisão de código;
quality gates;
ADRs;
princípio do menor privilégio.
28. Governança

O SIGMUN-DEV-AGENT estará subordinado à governança arquitetural do SIGMUN.

Alterações significativas em:

arquitetura;
permissões;
níveis de autonomia;
integração com infraestrutura;
segurança;
execução em produção;

deverão ser avaliadas e, quando necessário, registradas como ADR.

29. Relação com os Domínios do SIGMUN

O SIGMUN-DEV-AGENT não será considerado domínio de negócio.

Ele será uma capacidade técnica transversal.

Sua finalidade é apoiar a implementação dos domínios existentes, incluindo:

DOM-COM
DOM-CUM
DOM-IDN
DOM-DAD
DOM-GDO
DOM-SEG
DOM-INT
DOM-GOV
DOM-DIA
...

A implementação do agente deverá respeitar a documentação específica de cada domínio.

30. Relação com o DOM-DIA

O SIGMUN-DEV-AGENT não substitui o DOM-DIA — Gestão de Diárias.

O DOM-DIA é um domínio funcional do SIGMUN.

O SIGMUN-DEV-AGENT é uma capacidade tecnológica destinada a apoiar o desenvolvimento e a manutenção dos domínios.

Assim:

                 SIGMUN
                    │
        ┌───────────┴───────────┐
        │                       │
  Domínios de Negócio     Capacidades Técnicas
        │                       │
        ├── DOM-COM             └── SIGMUN-DEV-AGENT
        ├── DOM-DIA
        ├── DOM-PES
        ├── DOM-CON
        └── ...
31. Diretriz Arquitetural

O SIGMUN-DEV-AGENT deverá ser tratado como infraestrutura de apoio à engenharia do SIGMUN.

Seu objetivo final é permitir que o projeto evolua de:

Desenvolvimento manual

para:

Desenvolvimento assistido

e posteriormente:

Engenharia de software assistida por agentes

sem comprometer:

segurança;
governança;
rastreabilidade;
qualidade;
arquitetura;
soberania dos dados;
controle humano.
32. Diretriz Final

A inteligência artificial utilizada pelo SIGMUN deverá ampliar a capacidade da equipe, e não substituir a responsabilidade técnica e institucional.

O agente deverá sempre operar dentro dos limites definidos pelo projeto.

A autonomia deverá crescer somente à medida que:

a confiabilidade for comprovada;
os testes forem suficientes;
os mecanismos de segurança estiverem implementados;
a auditoria estiver funcionando;
os processos de governança estiverem maduros.

O princípio fundamental será:

O agente pode propor, executar e verificar; a governança continua humana.


### Próximo passo

Eu sugiro **não começar ainda instalando o Ollama e escrevendo o agente inteiro**. Primeiro devemos transformar essa especificação em uma pequena arquitetura executável.

A sequência que eu seguiria é:

```text
000-Especificacao-SIGMUN-DEV-AGENT.md
              ↓
001-Arquitetura-do-Agente.md
              ↓
002-Modelo-de-Permissoes-e-Autonomia.md
              ↓
003-Catalogo-de-Ferramentas.md
              ↓
004-Modelo-de-Contexto-e-RAG.md
              ↓
005-Modelo-de-Auditoria-do-Agente.md
              ↓
006-Plano-de-Implementacao-do-MVP.md
              ↓
código
              ↓
Ollama
              ↓
primeiro agente local