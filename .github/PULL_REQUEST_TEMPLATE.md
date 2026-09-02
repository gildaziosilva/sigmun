# Pull Request — SIGMUN

> Template oficial para Pull Requests do SIGMUN.
>
> Este template operacionaliza o processo definido no `000E-GUIA-DE-CONTRIBUICAO.md`.

---

# 1. Identificação

**Título da alteração:**

<!-- Descreva objetivamente a alteração. -->

**Tipo de alteração:**

* [ ] Feature / Nova funcionalidade
* [ ] Correção de bug
* [ ] Refatoração
* [ ] Melhoria técnica
* [ ] Performance
* [ ] Documentação
* [ ] Segurança
* [ ] Arquitetura
* [ ] Banco de dados / Migração
* [ ] Integração
* [ ] Testes
* [ ] Infraestrutura / DevOps
* [ ] CI/CD
* [ ] Build / Dependências
* [ ] Dados
* [ ] UX/UI
* [ ] Pesquisa / Investigação
* [ ] Manutenção técnica

**Domínio SIGMUN:**

**Código do domínio:**

**Issue relacionada:**

```text
#123
```

**Branch de origem:**

```text
feature/...
```

**Responsável pela implementação:**

---

# 2. Descrição

## O que foi alterado?

Descreva objetivamente as alterações realizadas.

```text
```

## Por que esta alteração é necessária?

Descreva o problema, necessidade ou objetivo que motivou a alteração.

```text
```

## Como a solução foi implementada?

Descreva resumidamente a abordagem técnica adotada.

```text
```

## Critérios de aceitação atendidos

Liste ou referencie os critérios de aceitação atendidos por este PR.

```text
CA-...

```

---

# 3. Rastreabilidade SIGMUN

## Documentação relacionada

* [ ] Existe documentação correspondente em `SIGMUN-Docs/`
* [ ] A documentação foi atualizada
* [ ] A documentação não precisou ser alterada

**Documentos relacionados:**

```text
SIGMUN-Docs/...

```

## Requisitos relacionados

```text
REQ-...

```

## Casos de uso relacionados

```text
UC-...

```

## Histórias de usuário relacionadas

```text
US-...

```

## Critérios de aceitação relacionados

```text
CA-...

```

## ADR relacionada

* [ ] Não se aplica
* [ ] ADR existente
* [ ] Nova ADR criada
* [ ] ADR atualizada

**ADR:**

```text
SIGMUN-Docs/.../ADR-...

```

---

# 4. Impacto Arquitetural

## Esta alteração modifica a arquitetura?

* [ ] Não
* [ ] Sim

Se sim, descreva:

```text
```

## Componentes afetados

* [ ] Backend
* [ ] Frontend
* [ ] API
* [ ] Banco de dados
* [ ] Mensageria / Eventos
* [ ] Tarefas assíncronas / Celery
* [ ] Integrações
* [ ] Infraestrutura
* [ ] Observabilidade
* [ ] Segurança
* [ ] Documentação
* [ ] Outro

**Componentes específicos:**

```text
```

## Impacto em outros domínios

* [ ] Não há impacto
* [ ] Há impacto

Se houver:

```text
Domínio:
Componente:
Tipo de dependência:
Impacto:

```

## Dependências entre domínios

* [ ] Não existem
* [ ] Existem e estão documentadas

Descrição:

```text
```

---

# 5. Compatibilidade

## Esta alteração quebra compatibilidade existente?

* [ ] Não
* [ ] Sim
* [ ] Não aplicável

Se sim, descreva:

```text
```

## Breaking Change

* [ ] Não
* [ ] Sim

Se sim, descreva:

```text
Componente afetado:
Versão anterior:
Nova versão:
Impacto:
Plano de migração:

```

---

# 6. Banco de Dados

* [ ] Não há alteração de banco
* [ ] Nova migration
* [ ] Alteração de tabela
* [ ] Alteração de índice
* [ ] Alteração de relacionamento
* [ ] Alteração de dados
* [ ] Alteração de auditoria
* [ ] Alteração de constraint
* [ ] Alteração de performance

**Migration relacionada:**

```text
alembic revision ...

```

## Compatibilidade com dados existentes

* [ ] Não aplicável
* [ ] Compatível
* [ ] Requer migração
* [ ] Requer transformação de dados
* [ ] Requer procedimento de rollback

**Observações:**

```text
```

---

# 7. API e Integrações

* [ ] Não há alteração de API
* [ ] Novo endpoint
* [ ] Alteração de endpoint
* [ ] Remoção de endpoint
* [ ] Alteração de contrato
* [ ] Breaking change
* [ ] Nova integração
* [ ] Alteração de integração
* [ ] Evento publicado
* [ ] Evento consumido
* [ ] Alteração de autenticação/autorização

**Endpoints afetados:**

```text
```

**Integrações afetadas:**

```text
```

**Contratos afetados:**

```text
```

## Compatibilidade de integração

* [ ] Compatibilidade mantida
* [ ] Compatibilidade alterada
* [ ] Nova versão de contrato necessária
* [ ] Não aplicável

Observações:

```text
```

---

# 8. Tarefas Assíncronas / Celery

* [ ] Não há alteração relacionada a tarefas assíncronas
* [ ] Nova tarefa Celery
* [ ] Alteração de tarefa Celery
* [ ] Nova fila
* [ ] Alteração de fila
* [ ] Alteração de retry
* [ ] Alteração de timeout
* [ ] Alteração de prioridade
* [ ] Alteração de periodicidade
* [ ] Alteração de worker

**Tarefas afetadas:**

```text
```

## Idempotência

* [ ] Não aplicável
* [ ] Avaliada
* [ ] Implementada
* [ ] Necessita melhoria

## Falhas / Retry

* [ ] Não aplicável
* [ ] Avaliado
* [ ] Implementado
* [ ] Necessita melhoria

**Observações:**

```text
```

---

# 9. Segurança e LGPD

## Segurança

* [ ] Não há impacto de segurança
* [ ] Autenticação
* [ ] Autorização
* [ ] Perfis / Papéis / Permissões
* [ ] Auditoria
* [ ] Validação de entrada
* [ ] Logs
* [ ] Segredos / Credenciais
* [ ] Criptografia
* [ ] API
* [ ] Infraestrutura
* [ ] Dependências
* [ ] Outro

## Dados

* [ ] Não envolve dados pessoais
* [ ] Dados pessoais
* [ ] Dados pessoais sensíveis
* [ ] Dados classificados
* [ ] Dados de auditoria

## Tratamento

* [ ] Não aplicável
* [ ] Coleta
* [ ] Processamento
* [ ] Armazenamento
* [ ] Compartilhamento
* [ ] Exportação
* [ ] Exclusão
* [ ] Retenção / descarte

**Avaliação do impacto:**

```text
```

## Segurança de dependências

* [ ] Não foram adicionadas dependências
* [ ] Dependências avaliadas
* [ ] Dependências atualizadas
* [ ] Vulnerabilidades verificadas

**Dependências afetadas:**

```text
```

---

# 10. Dados de Teste

* [ ] Foram utilizados apenas dados sintéticos
* [ ] Foram utilizados dados anonimizados
* [ ] Não foram utilizados dados reais
* [ ] Dados reais foram utilizados mediante procedimento/autorização aplicável
* [ ] Não aplicável

**Observações:**

```text
```

---

# 11. Testes

## Testes implementados

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
* [ ] Testes de integração entre domínios
* [ ] Não aplicável

## Resultado

```text
Comando(s) executado(s):

Resultado:

Cobertura, quando aplicável:

```

## Critérios de aceitação

* [ ] Todos os critérios de aceitação foram atendidos
* [ ] Alguns critérios não se aplicam
* [ ] Existem critérios pendentes

Se houver pendências:

```text
```

---

# 12. Documentação

* [ ] Código documentado quando necessário
* [ ] API/OpenAPI atualizada
* [ ] Documentação arquitetural atualizada
* [ ] Documentação do domínio atualizada
* [ ] Requisitos atualizados
* [ ] Casos de uso atualizados
* [ ] Histórias de usuário atualizadas
* [ ] Critérios de aceitação atualizados
* [ ] Matriz de rastreabilidade atualizada
* [ ] Modelo de dados atualizado
* [ ] Documentação de integração atualizada
* [ ] Documentação de segurança atualizada
* [ ] README atualizado quando necessário
* [ ] Nenhuma documentação adicional necessária

**Documentos atualizados:**

```text
SIGMUN-Docs/...

```

---

# 13. Inteligência Artificial / SIGMUN-DEV-AGENT

## Utilização de IA

* [ ] Não foi utilizada IA
* [ ] IA utilizada como apoio à análise
* [ ] IA utilizada como apoio à implementação
* [ ] IA utilizada para testes
* [ ] IA utilizada para documentação
* [ ] IA utilizada para revisão
* [ ] IA utilizada para refatoração

## SIGMUN-DEV-AGENT

* [ ] Alteração analisada pelo SIGMUN-DEV-AGENT
* [ ] Alteração executada com apoio do SIGMUN-DEV-AGENT
* [ ] Não utilizado
* [ ] Não aplicável

## Validação humana

* [ ] O código gerado/sugerido por IA foi revisado
* [ ] A solução foi compreendida pelo autor
* [ ] Testes foram executados
* [ ] Segurança foi avaliada
* [ ] Dependências foram verificadas
* [ ] Não foram fornecidos dados confidenciais ou segredos à ferramenta de IA

**Observações:**

```text
```

---

# 14. Dependências

## Dependências adicionadas ou alteradas

* [ ] Não há alteração
* [ ] Nova dependência
* [ ] Atualização de dependência
* [ ] Remoção de dependência

**Dependências:**

```text
Nome:
Versão anterior:
Nova versão:
Motivo:
Licença:
Impacto:

```

---

# 15. Observabilidade e Operação

* [ ] Não há impacto operacional
* [ ] Logs atualizados
* [ ] Métricas atualizadas
* [ ] Tracing considerado
* [ ] Health checks verificados
* [ ] Alertas considerados
* [ ] Monitoramento atualizado
* [ ] Configuração necessária
* [ ] Variáveis de ambiente alteradas

**Observações operacionais:**

```text
```

---

# 16. Rollback e Implantação

## Rollback

* [ ] Não aplicável
* [ ] Rollback simples
* [ ] Rollback requer procedimento específico
* [ ] Rollback de migration necessário
* [ ] Rollback de configuração necessário
* [ ] Rollback de integração necessário

**Procedimento de rollback:**

```text
```

## Implantação

* [ ] Não requer procedimento especial
* [ ] Requer migration
* [ ] Requer alteração de configuração
* [ ] Requer atualização de infraestrutura
* [ ] Requer atualização de worker
* [ ] Requer atualização de documentação operacional
* [ ] Requer janela de implantação
* [ ] Requer homologação

**Procedimento de implantação:**

```text
```

---

# 17. Checklist de Qualidade

## Código

* [ ] Código segue os padrões do SIGMUN
* [ ] Código é legível e compreensível
* [ ] Não foram introduzidas duplicações desnecessárias
* [ ] Não existem dependências ocultas entre domínios
* [ ] Não há acesso direto ao banco de outro domínio
* [ ] Regras de negócio permanecem no domínio correto
* [ ] Tratamento de erros adequado
* [ ] Logs adequados
* [ ] Configurações sensíveis não foram versionadas
* [ ] Não foram incluídos dados pessoais reais
* [ ] Não foram incluídos segredos ou credenciais
* [ ] Complexidade introduzida é justificável

## Arquitetura

* [ ] Alteração respeita a arquitetura definida
* [ ] Dependências entre domínios estão documentadas
* [ ] Contratos de integração estão definidos
* [ ] Alterações arquiteturais possuem ADR quando necessário
* [ ] Breaking changes foram identificados
* [ ] Compatibilidade foi avaliada

## Banco de Dados

* [ ] Migrations são reproduzíveis
* [ ] Integridade dos dados foi preservada
* [ ] Compatibilidade com dados existentes foi avaliada
* [ ] Rollback foi considerado
* [ ] Impacto de performance foi avaliado quando necessário

## Segurança

* [ ] Autenticação/autorização foram avaliadas
* [ ] Entrada de dados foi validada
* [ ] Dados pessoais foram avaliados
* [ ] Logs não expõem informações indevidas
* [ ] Segredos não foram versionados
* [ ] Dependências foram avaliadas

## Operação

* [ ] Health checks permanecem funcionais
* [ ] Observabilidade foi considerada
* [ ] Rollback foi considerado quando necessário
* [ ] Implantação pode ser automatizada
* [ ] Configurações necessárias foram documentadas
* [ ] Jobs/workers foram avaliados quando aplicável

---

# 18. Evidências

Inclua, quando aplicável:

* logs;
* resultados de testes;
* screenshots;
* respostas de API;
* métricas;
* evidências de homologação;
* resultados de migrations;
* evidências de segurança;
* evidências de performance;
* outros artefatos relevantes.

**Evidências:**

```text
```

> **Importante:** as evidências não devem conter senhas, tokens, credenciais, dados pessoais reais ou informações classificadas.

---

# 19. Riscos e Impactos

**Riscos identificados:**

```text
```

**Impactos conhecidos:**

```text
```

**Impactos em outros domínios:**

```text
```

**Impactos operacionais:**

```text
```

**Plano de mitigação:**

```text
```

---

# 20. Checklist Final do Autor

* [ ] Li e respeitei o `000E-GUIA-DE-CONTRIBUICAO.md`
* [ ] A Issue relacionada está corretamente identificada
* [ ] O domínio SIGMUN está identificado
* [ ] A documentação `SIGMUN-Docs/` foi consultada
* [ ] A rastreabilidade foi preservada
* [ ] Os requisitos relacionados foram identificados
* [ ] Os casos de uso/histórias de usuário foram avaliados
* [ ] Os critérios de aceitação foram atendidos
* [ ] ADR foi avaliada quando necessário
* [ ] O impacto arquitetural foi avaliado
* [ ] O impacto em outros domínios foi avaliado
* [ ] O impacto no banco foi avaliado
* [ ] As migrations foram verificadas, quando aplicável
* [ ] APIs e integrações foram avaliadas
* [ ] Tarefas Celery foram avaliadas, quando aplicável
* [ ] Segurança e LGPD foram avaliadas
* [ ] Os dados de teste são apropriados
* [ ] Não foram introduzidos segredos ou credenciais
* [ ] Não foram incluídos dados pessoais indevidos
* [ ] As dependências foram avaliadas
* [ ] Os testes foram executados
* [ ] A documentação foi atualizada quando necessário
* [ ] O rollback foi considerado quando necessário
* [ ] As evidências foram verificadas
* [ ] Os riscos foram registrados
* [ ] O PR está pronto para revisão

---

# 21. Observações dos Revisores

```text
```

---

# 22. Decisão da Revisão

* [ ] Aprovado
* [ ] Aprovado com ajustes
* [ ] Alterações solicitadas
* [ ] Rejeitado
* [ ] Necessita avaliação arquitetural
* [ ] Necessita avaliação de segurança
* [ ] Necessita avaliação de dados/LGPD

**Observações:**

```text
```

---

# 23. Declaração do Autor

Confirmo que esta alteração foi desenvolvida de acordo com os padrões técnicos, arquiteturais, de segurança, documentação e governança definidos pelo SIGMUN.

Confirmo também que:

* a rastreabilidade da alteração foi preservada;
* os testes necessários foram executados;
* os impactos relevantes foram avaliados;
* segurança e proteção de dados foram consideradas;
* não foram incluídos segredos ou credenciais;
* a documentação foi atualizada quando necessária;
* as informações apresentadas neste Pull Request são verdadeiras e suficientes para sua revisão.

---

**SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

**Transparência por padrão. Segurança por princípio. Classificação da Informação por política.**

**Aberto sempre que possível, restrito sempre que necessário.**
