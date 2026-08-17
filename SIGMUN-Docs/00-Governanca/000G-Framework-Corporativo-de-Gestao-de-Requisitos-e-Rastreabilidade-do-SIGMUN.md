# FRAMEWORK CORPORATIVO DE ENGENHARIA DE REQUISITOS E RASTREABILIDADE

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Governança
**Versão:** 1.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Documento(s) Relacionado(s):**
- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

---

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

---

# FRAMEWORK CORPORATIVO DE ENGENHARIA DE REQUISITOS E RASTREABILIDADE

## Projeto
SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** 00 – Governança

**Documento:** 000G – Framework Corporativo de Engenharia de Requisitos e Rastreabilidade

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

---

# Controle de Versões

| Versão | Data | Autor | Descrição |
|---------|------|--------|-----------|
| 1.0 | AAAA-MM-DD | Equipe SIGMUN | Emissão inicial |

---

# Documentos Relacionados

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO.md
- 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
- Plano-de-Trabalho.md
- Arquiteturas Corporativas do SIGMUN
- Políticas Corporativas

---

# 1. Finalidade

Estabelecer o framework corporativo para engenharia de requisitos, rastreabilidade e gerenciamento do ciclo de vida dos requisitos do SIGMUN, assegurando alinhamento entre objetivos estratégicos, arquitetura corporativa, desenvolvimento, testes, implantação e operação.

---

# 2. Objetivos

Este framework tem como objetivos:

- padronizar a engenharia de requisitos;
- garantir rastreabilidade ponta a ponta;
- reduzir ambiguidades;
- apoiar auditorias;
- facilitar análise de impacto;
- apoiar gestão de mudanças;
- fortalecer a Governança da Arquitetura;
- preservar a memória institucional.

---

# 3. Princípios

Todo requisito deverá observar os princípios constitucionais do SIGMUN, incluindo:

- interesse público;
- foco no cidadão;
- transparência por padrão;
- segurança por princípio;
- classificação da informação por política;
- interoperabilidade;
- reutilização;
- simplicidade;
- melhoria contínua;
- conformidade legal;
- neutralidade tecnológica.

---

# 4. Escopo

Aplica-se a:

- requisitos estratégicos;
- requisitos de negócio;
- requisitos funcionais;
- requisitos não funcionais;
- requisitos regulatórios;
- requisitos de integração;
- requisitos de segurança;
- requisitos de dados;
- requisitos de infraestrutura;
- requisitos de usabilidade;
- requisitos de observabilidade;
- requisitos de inteligência artificial.

---

# 5. Ciclo de Vida dos Requisitos

Todo requisito seguirá o ciclo:

1. Identificação.
2. Elicitação.
3. Análise.
4. Priorização.
5. Especificação.
6. Validação.
7. Aprovação.
8. Implementação.
9. Testes.
10. Implantação.
11. Operação.
12. Evolução ou descontinuação.

---

# 6. Classificação dos Requisitos

## Estratégicos

Relacionados aos objetivos institucionais.

## Negócio

Relacionados aos processos municipais.

## Funcionais

Descrevem o comportamento esperado do sistema.

## Não Funcionais

Desempenho, disponibilidade, segurança, escalabilidade, acessibilidade etc.

## Regulatórios

Relacionados à legislação e normas.

## Técnicos

Necessários para implementação e sustentação da plataforma.

---

# 7. Estrutura de Identificação

Cada requisito possuirá identificador único.

Exemplos:

REQ-EST-0001

REQ-NEG-0105

REQ-FUN-0234

REQ-NFR-0045

REQ-SEC-0012

REQ-INT-0008

REQ-DAD-0031

---

# 8. Hierarquia de Rastreabilidade

Todo requisito deverá possuir vínculos com os artefatos relacionados.

```text
Constituição
      │
      ▼
Políticas Corporativas
      │
      ▼
Arquiteturas
      │
      ▼
ADR
      │
      ▼
Objetivo Estratégico
      │
      ▼
Processo de Negócio
      │
      ▼
Requisito
      │
      ▼
Caso de Uso
      │
      ▼
História de Usuário
      │
      ▼
Modelo de Dados
      │
      ▼
API
      │
      ▼
Código
      │
      ▼
Teste
      │
      ▼
Implantação
      │
      ▼
Operação
```

---

# 9. Matriz de Rastreabilidade

Cada requisito deverá indicar:

- objetivo estratégico;
- processo de negócio;
- módulo;
- domínio;
- ADR relacionado;
- arquitetura relacionada;
- entidades de dados;
- APIs;
- casos de uso;
- histórias de usuário;
- casos de teste;
- documentação;
- versão.

---

# 10. Modelo de Matriz

| Requisito | Objetivo | Processo | ADR | Módulo | API | Teste | Status |
|-----------|-----------|-----------|------|---------|------|--------|--------|

---

# 11. Controle de Mudanças

Toda alteração deverá registrar:

- motivo;
- origem;
- solicitante;
- análise de impacto;
- decisão;
- data;
- aprovador;
- versão.

---

# 12. Critérios de Qualidade

Todo requisito deverá ser:

- claro;
- completo;
- consistente;
- verificável;
- necessário;
- viável;
- rastreável;
- atômico;
- testável.

---

# 13. Papéis e Responsabilidades

## Comitê de Governança

Define prioridades estratégicas.

## Governança da Arquitetura

Avalia impactos arquiteturais.

## Analistas de Negócio

Modelam os requisitos.

## Arquitetos

Validam aderência técnica.

## Desenvolvimento

Implementa.

## QA

Valida.

## Product Owner

Prioriza.

---

# 14. Integração com ADR

Quando um requisito implicar decisão arquitetural relevante:

- deverá ser criado ou atualizado um ADR;
- o requisito deverá referenciar esse ADR;
- o ADR deverá listar os requisitos impactados.

---

# 15. Integração com Testes

Todo requisito deverá possuir critérios de aceitação e casos de teste correspondentes.

Nenhum requisito poderá ser considerado concluído sem evidência de validação.

---

# 16. Ferramentas

O framework é independente de ferramentas.

Poderão ser utilizados, conforme decisão da Governança:

- GitHub;
- GitLab;
- Azure DevOps;
- Jira;
- OpenProject;
- Redmine;
- outras soluções compatíveis.

---

# 17. Indicadores

Serão monitorados indicadores como:

- requisitos implementados;
- requisitos aprovados;
- cobertura de testes;
- rastreabilidade completa;
- requisitos alterados;
- tempo médio de aprovação;
- requisitos rejeitados;
- retrabalho.

---

# 18. Auditoria

A rastreabilidade poderá ser auditada a qualquer momento.

Toda evidência deverá permanecer preservada.

---

# 19. Revisão

Este framework será revisado sempre que houver mudanças relevantes na arquitetura, nos processos ou na estratégia institucional.

---

# 20. Disposições Finais

Este Framework integra o conjunto de documentos fundacionais do SIGMUN e deverá ser observado por todas as equipes envolvidas na concepção, desenvolvimento, implantação e evolução da plataforma.

Nenhum requisito crítico poderá ser implementado sem sua correspondente documentação, rastreabilidade e aprovação conforme as políticas de governança estabelecidas.

---

# Anexo A – Fluxo Simplificado de Engenharia de Requisitos

```text
Necessidade
      │
      ▼
Elicitação
      │
      ▼
Análise
      │
      ▼
Especificação
      │
      ▼
Validação
      │
      ▼
ADR (quando aplicável)
      │
      ▼
Implementação
      │
      ▼
Testes
      │
      ▼
Implantação
      │
      ▼
Operação
      │
      ▼
Melhoria Contínua
```

---

# Anexo B – Convenções de Identificação

| Prefixo | Tipo |
|----------|------|
| REQ-EST | Estratégico |
| REQ-NEG | Negócio |
| REQ-FUN | Funcional |
| REQ-NFR | Não Funcional |
| REQ-SEC | Segurança |
| REQ-INT | Integração |
| REQ-DAD | Dados |
| REQ-UX | Experiência do Usuário |
| REQ-OBS | Observabilidade |
| REQ-IA | Inteligência Artificial |

# Anexo C – Modelo de Cadeia de Rastreabilidade, onde cada funcionalidade do sistema possa ser acompanhada desde sua origem até sua operação. Por exemplo:

| Camada                   | Exemplo                                                |
| ------------------------ | ------------------------------------------------------ |
| Princípio Constitucional | Transparência por padrão                               |
| Objetivo Estratégico     | Digitalizar a arrecadação municipal                    |
| Processo de Negócio      | Lançamento de tributos                                 |
| Requisito                | REQ-FUN-0123                                           |
| ADR                      | ADR-0015 – Estratégia de emissão de documentos fiscais |
| Módulo                   | Tributação                                             |
| Caso de Uso              | Emitir guia de pagamento                               |
| API                      | `/api/v1/tributos/guias`                               |
| Entidade                 | GuiaPagamento                                          |
| Teste                    | CT-0456                                                |
| Implantação              | Release 2.1                                            |
| Indicador                | Tempo médio de emissão                                 |

---

**Documento:**000G–Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
