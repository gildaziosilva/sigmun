# 024 – Plano de Suporte e Operação – Gestão Documental

#### Plano de Suporte e Operação – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-024

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Concluído

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- `000-Dominio-Gestao-Documental.md`
- `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
- `000A-Padrao-Corporativo-De-Documentacao-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
- `021-Checklist-De-Prontidao-De-Producao-Gestao-Documental.md`
- `023-Plano-De-Treinamento-Gestao-Documental.md`
- `025-Estrutura-Tecnica-Gestao-Documental.md`
- `020-Plano-De-Implantacao-Gestao-Documental.md`

---

# 1. Finalidade

O **Plano de Suporte e Operação – Gestão Documental** define os procedimentos de sustentação, canais de suporte, escalonamento e operações rotineiras para garantir a disponibilidade, integridade e performance do domínio `DOM-GDO` em produção.

---

# 2. Canais de Suporte

| Canal | Canal de Contato | Horário | Escopo |
|-------|-----------------|---------|--------|
| Suporte Nível 1 | `#sigmun-support` (Slack/Teams) | 08:00–18:00 (UTC-3) | Dúvidas operacionais, reset de senha, acesso ao sistema |
| Suporte Nível 2 | `support@sigmun.gov.br` | 08:00–18:00 (UTC-3) | Incidentes de banco de dados, erros de API, migrações |
| Suporte Nível 3 | `gestor@sigmun.gov.br` | Sob demanda | Falhas críticas, perda de dados, correções de domínio |
| Emergência | Telefone: +55 (xx) 9XXXX-XXXX | 24/7 | Falha de produção com impacto institucional |

---

# 3. Procedimentos de Sustentação

## 3.1 Rotina Diária

- [ ] Verificação de health check: `GET /health` — status 200
- [ ] Revisão de logs de erro em `logs/`

## 3.2 Rotina Semanal

- [ ] Consumo de métricas operacionais (throughput, taxa de erro)
- [ ] Validação de backup recente (`scripts/backup_postgres.py`)
- [ ] Atualização de dependências (`requirements.txt`, `requirements-dev.txt`)

## 3.3 Rotina de Deploy

1. **Branch de feature** → `main` (gatilho CI/CD)
2. **Execução de migrações Alembic:** `alembic upgrade head`
3. **Testes automatizados:** `pytest tests/ -x --tb=short`
4. **Deploy em ambiente de homologação:** verificação de 23/23 E2E
5. **Deploy em produção:** monitoramento por 30 minutos

## 3.4 Rollback

- Comando: `alembic downgrade -1`
- Verificação de integridade pós-rollback
- Notificação ao Suporte Nível 3 se inconsistências detectadas

---

# 4. Tratamento de Incidentes

| Severidade | Definição | Tempo de Resposta | Tempo de Solução | Comunicação |
|------------|-----------|-------------------|------------------|-------------|
| P1 — Crítico | Sistema fora do ar, perda de dados | 30 min | 4h | Comunicação direta a gestores |
| P2 — Alto | Funcionalidade crítica indisponível | 1h | 8h | Aviso via canal oficial |
| P3 — Médio | Funcionalidade com limitações | 4h | 24h | Relatório diario |
| P4 — Baixo | Sugestão ou questão cosmética | 24h | 5 dias | Backlog de melhorias |

---

# 5. Monitoramento e Métricas

- **Health check:** `GET /health` (PostgreSQL status, API respondendo)
- **Logs operacionais:** `logs/` — rotação diária, retenção 30 dias
- **Métricas Prometheus/Grafana:** fase X.4 (pendente — P-GDO-002)
- **Alertas 5xx:** pendente de configuração formal

---

# 6. Backup e Recuperação

- **Backup automático:** em desenvolvimento (cron/agendamento — P-GDO-004)
- **Backup manual:** `scripts/backup_postgres.py` — execução under demanda
- **Restauração:** procedimento documentado, teste pendente (P-GDO-004)
- **Dados persistentes:** volume `postgres_data` no docker-compose

---

# 7. Usuários e Permissões

- **Operador de protocolo:** criar, classificar, tramitar próprio documento
- **Arquivista:** arquivar, versionar, consultar, destinar
- **Gestor documental:** aprovar classificações, consultar relatórios
- **Autoridade homologadora:** homologar eliminação (RN-GDO-011)
- **Administrador:** configuração de usuários, permissões, deploy

---

# 8. Versãoamento

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0 | 2026-08-20 | Esboço inicial padronizado |
| 2.0 | 2026-09-06 | Procedimentos completos com validação de homologação (23/23) e rotinas de deploy/rollback |

---

# 9. Pendências

| ID | Descrição | Impacto | Responsável |
|----|-----------|---------|-------------|
| P-GDO-002 | Política de retenção de logs / agregação centralizada | Baixo | Equipe SIGMUN |
| P-GDO-004 | Rotina de backup e teste de restauração | Médio | Equipe SIGMUN |
| SLA de atendimento formalizado | Pendência institucional | Médio | Prefeitura/Equipe |

---

**Documento:** 024-Plano-de-Suporte-e-Operacao-Gestao-Documental.md

**Última atualização:** 2026-09-06

**Responsável:** Equipe SIGMUN

**Status da revisão:** Concluído