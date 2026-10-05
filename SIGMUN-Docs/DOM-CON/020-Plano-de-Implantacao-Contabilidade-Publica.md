# 020 – Plano de Implantação – Contabilidade Pública

#### Plano de Implantação – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-020

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato define o plano de implantação do domínio de Contabilidade Pública,
abrangendo pré-requisitos, sequência de implantação, validação e strategies de
retorno.

---

# 2. Pré-requisitos

| Pré-requisito | Situação | Responsável |
| --- | --- | --- |
| DOM-ORC operativo com dotação autorizada | **Não atendida** (C-02) | Equipe DOM-ORC |
| DOM-IDN com perfis de contabilidade | Parcial | Equipe DOM-IDN |
| DOM-GDO disponível para anexos | Não atendida | Equipe DOM-GDO |
| Schema `con` criado pelas migrations | Atendida | Deploy |
| Migrations `20260919_05` e `20260919_06` aplicadas | Atendida | Deploy |
| Plano de contas do PCASP carregado | Pendente | Contabilidade |

**Bloqueador crítico:** sem DOM-ORC exposto não há dotação a empenhar, portanto o
domínio **não pode entrar em produção** mesmo que o próprio código esteja correto.

---

# 3. Sequência de Implantação

```text
Etapa 1 — Persistência (Onda 1)
    migration com as 10 colunas ausentes
    UNIQUE (exercicio, numero)
    chaves estrangeiras
    índices
        │
        ▼
Etapa 2 — Exposição (Onda 2)
    registro dos routers em src/main.py
    declaração da tag no OpenAPI
    mapeamento correto dos códigos de erro
        │
        ▼
Etapa 3 — Integração (Onda 3)
    registro dos routers do DOM-ORC
    teste do ciclo ponta a ponta
        │
        ▼
Etapa 4 — Qualidade (Onda 5 e 6)
    suíte de testes completa
    mypy sem erros
        │
        ▼
Etapa 5 — Carga de dados
    plano de contas do PCASP
    dotações iniciais do DOM-ORC
```

**A ordem é obrigatória.** Expor as rotas antes da Etapa 1 tornaria o domínio
acessível com perda silenciosa de dados contábeis.

---

# 4. Ambientes

| Ambiente | Finalidade | Dados | Integração externa |
| --- | --- | --- | --- |
| Local | Desenvolvimento | Sintéticos | Dublês |
| Integração | Validação contínua | Sintéticos | DOM-ORC de teste |
| Homologação | Validação com negócio | Máscara | DOM-ORC homologação |
| Produção | Operação | Reais | DOM-ORC, DOM-GDO, DOM-IDN |

---

# 5. Implantação Inicial (Produção)

| Passo | Atividade | Responsável |
| --- | --- | --- |
| 1 | Confirmar head das migrations e estado do schema `con` | DBA |
| 2 | Aplicar migrations de correção (Onda 1) | DBA |
| 3 | Verificar integridade referencial e índices | DBA |
| 4 | Implantar aplicação com routers registrados | Operação |
| 5 | Confirmar as sete rotas no OpenAPI | Operação |
| 6 | Carregar o plano de contas do PCASP | Contabilidade |
| 7 | Validar dotações vigentes no DOM-ORC | Contabilidade e orçamento |
| 8 | Executar teste do ciclo com dotação de teste | Contabilidade |
| 9 | Liberar o primeiro empenho real | Ordenador de despesa |
| 10 | Acompanhar a primeira execução diária | Operação |

---

# 6. Validação Pós-Implantação

| Verificação | Critério de aprovação |
| --- | --- |
| Rotas no OpenAPI | Sete rotas sob `/api/v1/con` presentes |
| Empenho de teste | Empenho criado e saldo da dotação debitado |
| Ciclo completo | Dotação → empenho → liquidação → pagamento |
| Lançamento contábil | Lançamento balanceado gerado |
| Conciliação | Conciliação de competência registrada |
| Auditoria | Autor e data preenchidos na trilha |
| Não regressão | Demais domínios sem falha (26 routers ativos) |

---

# 7. Estratégia de Retorno

| Falha | Ação | Responsável |
| --- | --- | --- |
| Migration falha | Reverter com `alembic downgrade`; base permanece na versão anterior | DBA |
| Aplicação falha ao iniciar | Remover os routers registrados e retornar à versão anterior | Operação |
| Erro de integração com DOM-ORC | Suspender as operações de empenho; preservar o que já foi registrado | Contabilidade |
| Dados corrompidos em produção | **Não há correção automática** — restaurar do backup | DBA |

**Advertência:** por não haver transação atômica entre DOM-ORC e DOM-CON (RNF-CON-005),
um erro de integração pode deixar dotação debitada sem empenho registrado. O
procedimento é consultar as duas bases e estornar manualmente.

---

# 8. Plano de Comunicação aos Usuários

| Momento | Ação | Público |
| --- | --- | --- |
| Antes da implantação | Aviso sobre indisponibilidade | Todos |
| Na liberação | Comunicação de disponibilidade | Contabilidade, ordenador, tesoureiro |
| Na primeira semana | Acompanhamento diário das operações | Contabilidade |
| Após 30 dias | Avaliação de uso e incidentes | Todos |

---

# 9. Riscos de Implantação

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| DOM-ORC não disponível na data | Média | **Crítico** | Implantação conjunta ou posterior à do DOM-ORC |
| Migration corretiva em base com dados | Alta | Alto | Executar primeiro em homologação, com `downgrade` testado |
| PCASP não carregado | Média | Alto | Carregar antes de liberar empenhos |
| Divergência entre ORM e banco | Alta | Alto | Validar `information_schema` contra `Base.metadata` |
| Regressão em outros domínios | Baixa | Alto | Executar a suíte completa da aplicação |

---

# 10. Critérios de Go-Live

- [ ] Schema `con` íntegro e com as 10 colunas ausentes
- [ ] `UNIQUE (exercicio, numero)` ativa
- [ ] Chaves estrangeiras criadas
- [ ] Índices criados
- [ ] Sete rotas expostas e documentadas
- [ ] DOM-ORC com dotações vigentes
- [ ] PCASP carregado e validado
- [ ] Suíte de testes com cobertura ≥ 80 %
- [ ] `mypy` sem erros
- [ ] Ciclo completo validado em homologação
- [ ] Plano de retorno operacional documentado


---

Este artefato define o plano de implantação do domínio de Contabilidade Pública,
abrangendo pré-requisitos, sequência de implantação, validação e strategies de
retorno.

---

# 2. Pré-requisitos

| Pré-requisito | Situação | Responsável |
| --- | --- | --- |
| DOM-ORC operativo com dotação autorizada | **Não atendida** (C-02) | Equipe DOM-ORC |
| DOM-IDN com perfis de contabilidade | Parcial | Equipe DOM-IDN |
| DOM-GDO disponível para anexos | Não atendida | Equipe DOM-GDO |
| Schema `con` criado pelas migrations | Atendida | Deploy |
| Migrations `20260919_05` e `20260919_06` aplicadas | Atendida | Deploy |
| Plano de contas do PCASP carregado | Pendente | Contabilidade |

**Bloqueador crítico:** sem DOM-ORC exposto não há dotação a empenhar, portanto o
domínio **não pode entrar em produção** mesmo que o próprio código esteja correto.

---

# 3. Sequência de Implantação

```text
Etapa 1 — Persistência (Onda 1)
    migration com as 10 colunas ausentes
    UNIQUE (exercicio, numero)
    chaves estrangeiras
    índices
        │
        ▼
Etapa 2 — Exposição (Onda 2)
    registro dos routers em src/main.py
    declaração da tag no OpenAPI
    mapeamento correto dos códigos de erro
        │
        ▼
Etapa 3 — Integração (Onda 3)
    registro dos routers do DOM-ORC
    teste do ciclo ponta a ponta
        │
        ▼
Etapa 4 — Qualidade (Onda 5 e 6)
    suíte de testes completa
    mypy sem erros
        │
        ▼
Etapa 5 — Carga de dados
    plano de contas do PCASP
    dotações iniciais do DOM-ORC
```

**A ordem é obrigatória.** Expor as rotas antes da Etapa 1 tornaria o domínio
acessível com perda silenciosa de dados contábeis.

---

# 4. Ambientes

| Ambiente | Finalidade | Dados | Integração externa |
| --- | --- | --- | --- |
| Local | Desenvolvimento | Sintéticos | Dublês |
| Integração | Validação contínua | Sintéticos | DOM-ORC de teste |
| Homologação | Validação com negócio | Máscara | DOM-ORC homologação |
| Produção | Operação | Reais | DOM-ORC, DOM-GDO, DOM-IDN |

---

# 5. Implantação Inicial (Produção)

| Passo | Atividade | Responsável |
| --- | --- | --- |
| 1 | Confirmar head das migrations e estado do schema `con` | DBA |
| 2 | Aplicar migrations de correção (Onda 1) | DBA |
| 3 | Verificar integridade referencial e índices | DBA |
| 4 | Implantar aplicação com routers registrados | Operação |
| 5 | Confirmar as sete rotas no OpenAPI | Operação |
| 6 | Carregar o plano de contas do PCASP | Contabilidade |
| 7 | Validar dotações vigentes no DOM-ORC | Contabilidade e orçamento |
| 8 | Executar teste do ciclo com dotação de teste | Contabilidade |
| 9 | Liberar o primeiro empenho real | Ordenador de despesa |
| 10 | Acompanhar a primeira execução diária | Operação |

---

# 6. Validação Pós-Implantação

| Verificação | Critério de aprovação |
| --- | --- |
| Rotas no OpenAPI | Sete rotas sob `/api/v1/con` presentes |
| Empenho de teste | Empenho criado e saldo da dotação debitado |
| Ciclo completo | Dotação → empenho → liquidação → pagamento |
| Lançamento contábil | Lançamento balanceado gerado |
| Conciliação | Conciliação de competência registrada |
| Auditoria | Autor e data preenchidos na trilha |
| Não regressão | Demais domínios sem falha (26 routers ativos) |

---

# 7. Estratégia de Retorno

| Falha | Ação | Responsável |
| --- | --- | --- |
| Migration falha | Reverter com `alembic downgrade`; base permanece na versão anterior | DBA |
| Aplicação falha ao iniciar | Remover os routers registrados e retornar à versão anterior | Operação |
| Erro de integração com DOM-ORC | Suspender as operações de empenho; preservar o que já foi registrado | Contabilidade |
| Dados corrompidos em produção | **Não há correção automática** — restaurar do backup | DBA |

**Advertência:** por não haver transação atômica entre DOM-ORC e DOM-CON (RNF-CON-005),
um erro de integração pode deixar dotação debitada sem empenho registrado. O
procedimento é consultar as duas bases e estornar manualmente.

---

# 8. Plano de Comunicação aos Usuários

| Momento | Ação | Público |
| --- | --- | --- |
| Antes da implantação | Aviso sobre indisponibilidade | Todos |
| Na liberação | Comunicação de disponibilidade | Contabilidade, ordenador, tesoureiro |
| Na primeira semana | Acompanhamento diário das operações | Contabilidade |
| Após 30 dias | Avaliação de uso e incidentes | Todos |

---

# 9. Riscos de Implantação

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| DOM-ORC não disponível na data | Média | **Crítico** | Implantação conjunta ou posterior à do DOM-ORC |
| Migration corretiva em base com dados | Alta | Alto | Executar primeiro em homologação, com `downgrade` testado |
| PCASP não carregado | Média | Alto | Carregar antes de liberar empenhos |
| Divergência entre ORM e banco | Alta | Alto | Validar `information_schema` contra `Base.metadata` |
| Regressão em outros domínios | Baixa | Alto | Executar a suíte completa da aplicação |

---

# 10. Critérios de Go-Live

- [ ] Schema `con` íntegro e com as 10 colunas ausentes
- [ ] `UNIQUE (exercicio, numero)` ativa
- [ ] Chaves estrangeiras criadas
- [ ] Índices criados
- [ ] Sete rotas expostas e documentadas
- [ ] DOM-ORC com dotações vigentes
- [ ] PCASP carregado e validado
- [ ] Suíte de testes com cobertura ≥ 80 %
- [ ] `mypy` sem erros
- [ ] Ciclo completo validado em homologação
- [ ] Plano de retorno operacional documentado

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 020-Plano-de-Implantacao-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
