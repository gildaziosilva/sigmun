# 022 – Plano de Migração de Dados – Gestão Documental

#### Plano de Migração de Dados – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-022

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Concluído

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- `000-Dominio-Gestao-Documental.md`
- `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
- `000A-Padrao-Corporativo-De-Documentacao-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
- `013-Modelo-De-Dados-Gestao-Documental.md`
- `020-Plano-De-Implantacao-Gestao-Documental.md`
- `021-Checklist-De-Prontidao-De-Producao-Gestao-Documental.md`

---

# 1. Finalidade

O **Plano de Migração de Dados – Gestão Documental** define a estratégia, escopo e procedimentos para migração de dados legados para o domínio `DOM-GDO`, garantindo integridade, consistência e rastreabilidade das informações durante a transição para o novo sistema SIGMUN.

---

# 2. Escopo

Inclui migração dos seguintes dados legados:

- Tipos documentais (12 categorias)
- Classificações documentais (9 níveis)
- Temporalidades (4 períodos)
- Documentos existentes (historical records)
- Metadados de tramitação e assinatura
- Registros de auditoria fundamentais

Fora de escopo: dados de sistemas integrados (DOM-IDN, DOM-CUM) — migrar em fases subsequentes.

---

# 3. Estratégia de Carga de Legado

## 3.1 Fases da Migração

| Fase | Descrição | Status |
|------|-----------|--------|
| Fase 1 | Exportação de estruturas de catálogo (tipos, classificações, temporalidades) | Concluída |
| Fase 2 | Carga de sementes (seed) — tipos documentais, classificações, temporalidades | Concluída |
| Fase 3 | Migração de documentos históricos com mapeamento de metadados | Pendente |
| Fase 4 | Validação de integridade pós-migração | Pendente |
| Fase 5 | Corte sobre go-live | Pendente |

## 3.2 Fonte e Destino

| Atributo | Fonte | Destino (DOM-GDO) |
|----------|-------|-------------------|
| `tipo_documental` | Catálogo de classificação | `tipos_documentais` table |
| `classificacao` | Tabela de classificação normativa | `classificacoes` table |
| `temporalidade` | Legislação municipal | `temporalidades` table |
| `conteudo_documento` | Arquivos físicos/digitais | `documentos` table + `conteudo_ref` |
| `metadados` | Sistemas de protocolo legacy | Metadados enriquecidos |

## 3.3 Procedimentos de Migração

1. **Backup completo** do banco de dados legacy antes de iniciar
2. **Aplicação de migrações Alembic** para criar schema `gdo` com 11 tabelas
3. **Execução de seed idempotente** com 12 tipos documentais, 9 classificações, 4 temporalidades
4. **Inserção de documentos históricos** via script de carga controlada
5. **Validação de integridade** — checksum SHA-256, unicidade de códigos, constraints de FK
6. **Verificação de consistência** — consulta de 23 casos de homologação E2E

---

# 4. Tratamento de Dados Específicos

## 4.1 Integridade SHA-256

- Dados legados sem hash SHA-256 receberão hash calculado do conteúdo original
- Documentos com hash inválido serão sinalizados para revisão manual (RN-GDO-002)

## 4.2 Unicidade de Código

- RN-GDO-001 aplicada: código documental deve ser único em todo o sistema
- Casos de código duplicado em legados serão resolvidos mediante sufixo sequencial

## 4.3 Temporalidade

- 4 tipos de temporalidade mapeados: TEMP-001 (12 meses), TEMP-002 (6 meses), TEMP-003 (30 dias), TEMP-004 (indeterminada)
- Dados legais sem temporalidade definida receberão TEMP-004 por default

---

# 5. Rastreabilidade

| Item | Origem | Destino | Validação |
|------|--------|---------|-----------|
| Modelos de dados | `013-Modelo-De-Dados` | Migrações Alembic | ✅ Validado |
| Casos de teste | `019-Casos-De-Teste` | Execução E2E | ✅ 23/23 aprovados |
| Matriz de rastreabilidade | `012-Matriz-De-Rastreabilidade` | Atualizada | ✅ Concluída |

---

# 6. Versionamento

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0 | 2026-08-20 | Esboço inicial padronizado |
| 2.0 | 2026-09-06 | Preenchimento com estratégia de carga definitiva e validação E2E |

---

# 7. Governança

- **Responsável:** Equipe SIGMUN
- **Aprovação:** Necessária prévia ao go-live (artefato 021, seção 27)
- **Riscos identificados:** Perda de integridade de hash, quebra de unicidade de código, dados incompletos de temporalidade

---

**Documento:** 022-Plano-de-Migracao-de-Dados-Gestao-Documental.md

**Última atualização:** 2026-09-06

**Responsável:** Equipe SIGMUN

**Status da revisão:** Concluído