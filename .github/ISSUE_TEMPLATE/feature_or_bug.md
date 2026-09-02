---

name: Feature ou Bug

about: Registrar uma nova funcionalidade, correção, melhoria, necessidade técnica ou alteração de arquitetura do SIGMUN

title: ""

labels: ""

assignees: ""

---

# Issue — SIGMUN

> Template oficial para registro de demandas do SIGMUN.
>
> Esta Issue representa o ponto inicial de rastreabilidade da demanda e deve ser utilizada em conjunto com o `000E-GUIA-DE-CONTRIBUICAO.md`.

---

# 1. Classificação

**Tipo da demanda:**

* [ ] Feature / Nova funcionalidade
* [ ] Bug / Defeito
* [ ] Melhoria
* [ ] Refatoração
* [ ] Documentação
* [ ] Segurança
* [ ] Arquitetura
* [ ] Infraestrutura / DevOps
* [ ] CI/CD
* [ ] Build / Dependências
* [ ] Banco de dados
* [ ] Integração
* [ ] Mensageria / Eventos
* [ ] Tarefas assíncronas / Celery
* [ ] Testes
* [ ] Performance
* [ ] Dados
* [ ] UX/UI
* [ ] Pesquisa / Investigação
* [ ] Manutenção técnica

**Domínio SIGMUN:**

**Código do domínio:**

**Prioridade:**

* [ ] Crítica
* [ ] Alta
* [ ] Média
* [ ] Baixa

---

# 2. Resumo

**Título da demanda:**

<!-- Descreva resumidamente a necessidade. -->

**Resumo:**

```text
```

---

# 3. Contexto

## Problema ou necessidade

Descreva o problema que precisa ser resolvido ou a capacidade que precisa ser criada.

```text
```

## Motivação

Por que esta alteração é necessária para o SIGMUN?

```text
```

## Objetivo

Qual resultado esta demanda pretende alcançar?

```text
```

---

# 4. Comportamento Atual

Para bugs, descreva o comportamento atualmente observado.

Para novas funcionalidades, descreva como o processo funciona atualmente, quando aplicável.

```text
```

**Passos para reproduzir — quando aplicável:**

1.
2.
3.

**Resultado atual:**

```text
```

---

# 5. Comportamento Esperado

Descreva claramente o resultado esperado.

```text
```

**Resultado esperado:**

```text
```

---

# 6. Escopo

## Incluído

Liste o que faz parte desta demanda.

```text
```

## Não incluído

Liste explicitamente o que não faz parte desta demanda.

```text
```

## Dependências

Informe outras Issues, requisitos, módulos, domínios ou componentes dos quais esta demanda depende.

```text
#123
REQ-...
Domínio:
Componente:

```

---

# 7. Proposta Inicial

Caso já exista uma proposta de solução, descreva-a aqui.

```text
```

> A proposta inicial não representa necessariamente a solução arquitetural definitiva. A solução deverá ser validada durante a análise técnica.

---

# 8. Requisitos e Rastreabilidade

## Documento SIGMUN relacionado

```text
SIGMUN-Docs/...

```

## Requisito relacionado

```text
REQ-...

```

## Caso de uso relacionado

```text
UC-...

```

## História de usuário

**Como** [ator]

**Quero** [capacidade]

**Para** [benefício]

## Critérios de aceitação

Os critérios devem ser objetivos, verificáveis e testáveis.

* [ ]
* [ ]
* [ ]
* [ ]

## Regras de negócio

Quando aplicável:

```text
```

---

# 9. Domínios e Impacto

## Domínios afetados

```text
```

## Componentes afetados

* [ ] Backend
* [ ] Frontend
* [ ] API
* [ ] Banco de dados
* [ ] Integrações
* [ ] Mensageria / Eventos
* [ ] Tarefas assíncronas / Celery
* [ ] Segurança
* [ ] Auditoria
* [ ] Documentação
* [ ] Infraestrutura
* [ ] Observabilidade
* [ ] Outro

**Componentes específicos:**

```text
```

## Dependências entre domínios

* [ ] Não identificadas
* [ ] Existem
* [ ] Necessitam análise arquitetural

Descrição:

```text
```

## Riscos conhecidos

```text
```

---

# 10. Compatibilidade

## Esta demanda pode afetar compatibilidade existente?

* [ ] Não
* [ ] Sim
* [ ] Não identificado

## Breaking Change potencial?

* [ ] Não
* [ ] Sim
* [ ] A avaliar

Se aplicável:

```text
Componente afetado:
Contrato afetado:
Versão atual:
Impacto esperado:

```

---

# 11. Dados

## Esta Issue envolve dados?

* [ ] Não
* [ ] Sim
* [ ] A avaliar

Se sim:

**Entidades envolvidas:**

```text
```

**Alteração de modelo de dados?**

* [ ] Não
* [ ] Sim
* [ ] A avaliar

**Tipo de alteração:**

* [ ] Nova entidade
* [ ] Nova tabela
* [ ] Alteração de tabela
* [ ] Novo campo
* [ ] Alteração de campo
* [ ] Novo relacionamento
* [ ] Alteração de relacionamento
* [ ] Índice
* [ ] Constraint
* [ ] Dados existentes
* [ ] Auditoria

---

# 12. Dados Pessoais e LGPD

**Dados pessoais envolvidos?**

* [ ] Não
* [ ] Sim
* [ ] Não identificado
* [ ] A avaliar

**Dados pessoais sensíveis envolvidos?**

* [ ] Não
* [ ] Sim
* [ ] Não identificado
* [ ] A avaliar

**Classificação da informação:**

* [ ] Pública
* [ ] Interna
* [ ] Restrita
* [ ] Confidencial
* [ ] A avaliar

**Tratamento envolvido:**

* [ ] Coleta
* [ ] Processamento
* [ ] Armazenamento
* [ ] Consulta
* [ ] Compartilhamento
* [ ] Exportação
* [ ] Retenção
* [ ] Descarte
* [ ] Não aplicável

**Necessidade de análise de LGPD/classificação:**

```text
```

---

# 13. API e Integrações

* [ ] Não se aplica
* [ ] Nova API
* [ ] Alteração de API
* [ ] Remoção de API
* [ ] Nova integração
* [ ] Alteração de integração
* [ ] Evento publicado
* [ ] Evento consumido
* [ ] Mensageria
* [ ] Contrato de integração

**Endpoints envolvidos:**

```text
```

**Sistemas/domínios envolvidos:**

```text
```

**Contratos envolvidos:**

```text
```

---

# 14. Tarefas Assíncronas / Celery

* [ ] Não se aplica
* [ ] Nova tarefa
* [ ] Alteração de tarefa
* [ ] Nova fila
* [ ] Alteração de fila
* [ ] Retry
* [ ] Timeout
* [ ] Prioridade
* [ ] Periodicidade
* [ ] Worker
* [ ] A avaliar

**Tarefas relacionadas:**

```text
```

**Comportamento esperado em caso de falha:**

```text
```

**Requisito de idempotência:**

```text
```

---

# 15. Segurança

* [ ] Não há impacto conhecido
* [ ] Autenticação
* [ ] Autorização
* [ ] Permissões
* [ ] Auditoria
* [ ] Validação de entrada
* [ ] Dados pessoais
* [ ] Dados sensíveis
* [ ] Segredos
* [ ] Segurança de API
* [ ] Criptografia
* [ ] Dependências
* [ ] Infraestrutura
* [ ] Outro
* [ ] A avaliar

**Descrição:**

```text
```

---

# 16. Dependências Técnicas

## Dependências novas ou alteradas

* [ ] Não se aplica
* [ ] Nova dependência
* [ ] Atualização de dependência
* [ ] Remoção de dependência
* [ ] A avaliar

**Dependências:**

```text
Nome:
Versão:
Motivo:
Licença:
Impacto:

```

---

# 17. Arquitetura e ADR

## A demanda pode alterar a arquitetura?

* [ ] Não
* [ ] Sim
* [ ] A avaliar

## ADR necessária?

* [ ] Não
* [ ] Talvez — avaliar durante análise
* [ ] Sim
* [ ] ADR existente

**ADR relacionada:**

```text
SIGMUN-Docs/.../ADR-...

```

**Descrição do impacto arquitetural:**

```text
```

---

# 18. Observabilidade e Operação

## Há impacto operacional?

* [ ] Não
* [ ] Sim
* [ ] A avaliar

## Aspectos envolvidos

* [ ] Logs
* [ ] Métricas
* [ ] Tracing
* [ ] Health checks
* [ ] Alertas
* [ ] Monitoramento
* [ ] Configuração
* [ ] Variáveis de ambiente
* [ ] Workers
* [ ] Filas
* [ ] Infraestrutura

**Observações:**

```text
```

---

# 19. Segurança da Informação e Segredos

A demanda poderá envolver:

* [ ] Nenhum segredo
* [ ] Variáveis de ambiente
* [ ] Credenciais
* [ ] Tokens
* [ ] Certificados
* [ ] Chaves
* [ ] Outro

> Segredos, senhas, tokens e chaves privadas nunca devem ser inseridos nesta Issue.

**Observações:**

```text
```

---

# 20. Testes e Validação

## Estratégia de testes prevista

* [ ] Testes unitários
* [ ] Testes de integração
* [ ] Testes de API
* [ ] Testes de contrato
* [ ] Testes de aceitação
* [ ] Testes de segurança
* [ ] Testes de migração
* [ ] Testes de regressão
* [ ] Testes de performance
* [ ] Testes de tarefas assíncronas
* [ ] Testes entre domínios
* [ ] A definir durante implementação

**Cenários principais:**

```text
```

---

# 21. Dados de Teste

**Dados de teste previstos:**

* [ ] Dados sintéticos
* [ ] Dados anonimizados
* [ ] Não haverá dados reais
* [ ] Dados reais — requer avaliação/autorização
* [ ] A definir
* [ ] Não aplicável

**Observações:**

```text
```

---

# 22. Documentação

## Documentos que deverão ser atualizados

```text
SIGMUN-Docs/...

```

## Tipos de documentação potencialmente afetados

* [ ] Requisitos
* [ ] Casos de uso
* [ ] Histórias de usuário
* [ ] Critérios de aceitação
* [ ] Modelo de domínio
* [ ] Modelo de dados
* [ ] Arquitetura
* [ ] APIs
* [ ] Integrações
* [ ] Segurança
* [ ] Testes
* [ ] Implantação
* [ ] Operação
* [ ] Matriz de rastreabilidade
* [ ] README
* [ ] Outro
* [ ] Nenhuma alteração necessária

---

# 23. SIGMUN-DEV-AGENT e Inteligência Artificial

## Esta demanda poderá utilizar IA?

* [ ] Sim
* [ ] Não
* [ ] Avaliar durante a implementação

## SIGMUN-DEV-AGENT

* [ ] Sim
* [ ] Não
* [ ] Avaliar durante a implementação

**Orientações para o agente:**

```text
```

## Restrições

Registrar, quando aplicável:

* componentes que não devem ser alterados;
* arquivos que não devem ser modificados;
* regras arquiteturais;
* requisitos específicos;
* restrições de segurança;
* restrições de dados.

```text
```

> A utilização de IA não elimina a responsabilidade técnica do colaborador. Toda implementação assistida por IA deve ser revisada, compreendida, testada e validada.

---

# 24. Evidências

Quando aplicável, anexar:

* screenshots;
* logs;
* exemplos de entrada;
* exemplos de saída;
* payloads;
* respostas de API;
* arquivos de teste;
* evidências de homologação;
* diagramas;
* métricas;
* outros artefatos relevantes.

```text
```

> Evidências não devem conter senhas, tokens, credenciais, dados pessoais reais ou informações classificadas.

---

# 25. Plano de Implementação

Quando aplicável, descreva uma sequência inicial de implementação.

```text
1.
2.
3.
4.
5.

```

---

# 26. Plano de Validação

Descreva como será verificado que a demanda foi atendida.

```text
1.
2.
3.
4.

```

---

# 27. Critérios de Pronto

A Issue somente poderá ser considerada concluída quando os critérios aplicáveis tiverem sido atendidos:

* [ ] Implementação realizada
* [ ] Critérios de aceitação atendidos
* [ ] Testes implementados
* [ ] Testes aprovados
* [ ] Segurança validada
* [ ] LGPD avaliada quando aplicável
* [ ] Auditoria validada quando aplicável
* [ ] Migrações validadas quando aplicável
* [ ] API validada quando aplicável
* [ ] Integrações validadas quando aplicável
* [ ] Tarefas Celery validadas quando aplicável
* [ ] Documentação atualizada
* [ ] Rastreabilidade atualizada
* [ ] Pull Request criado
* [ ] Pull Request aprovado
* [ ] Homologação realizada quando aplicável
* [ ] Implantação realizada quando aplicável
* [ ] Evidências registradas
* [ ] Nenhum risco crítico pendente

---

# 28. Observações

```text
```

---

# 29. Checklist de Encerramento

* [ ] Problema/necessidade resolvido
* [ ] Escopo atendido
* [ ] Critérios de aceitação atendidos
* [ ] Código revisado
* [ ] Testes aprovados
* [ ] Segurança avaliada
* [ ] LGPD avaliada quando aplicável
* [ ] Documentação atualizada
* [ ] Rastreabilidade preservada
* [ ] Impactos avaliados
* [ ] Dependências avaliadas
* [ ] Issue vinculada ao Pull Request
* [ ] Pull Request aprovado
* [ ] Homologação concluída quando aplicável
* [ ] Implantação concluída quando aplicável

---

# 30. Referências

Documentos, Issues, PRs, ADRs ou outras referências relevantes:

```text
SIGMUN-Docs/...
#123
#456
ADR-...
REQ-...

```

---

**SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

**Transparência por padrão. Segurança por princípio. Classificação da Informação por política.**

**Aberto sempre que possível, restrito sempre que necessário.**
