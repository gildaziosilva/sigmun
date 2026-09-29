# 021 – Checklist de Prontidão para Produção – Gestão Territorial

#### Checklist de Prontidão para Produção – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-021

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato consolida as condições de prontidão do domínio de Gestão Territorial
para o ambiente de produção.

---

# 2. Checklist Funcional

| Item | Situação | Evidência |
| --- | --- | --- |
| Regras de negócio implementadas | Concluído | 6 regras no artefato 007 |
| Casos de uso implementados | Concluído | Artefato 005 |
| Requisitos funcionais atendidos | Concluído | Artefato 008 |
| Contrato de API publicado | Concluído | 15 paths sob `/api/v1/tel` |

---

# 3. Checklist de Qualidade

| Item | Situação | Evidência |
| --- | --- | --- |
| Testes unitários | Concluído | 62 casos de teste |
| Testes de integração | Concluído | `tests/integration/` |
| Análise estática | Concluído | `ruff check` e `mypy` sem erros |
| Build do frontend | Concluído | `npm run build` sem erros |
| Banco de dados | Concluído | Migração aplicada com cabeça única |

---

# 4. Checklist Operacional

| Item | Situação |
| --- | --- |
| Seed DEMO disponível | Concluído |
| Exclusão do seed | Concluído |
| Guia de suporte | Artefato 024 |
| Plano de treinamento | Artefato 023 |

---

# 5. Pendências Bloqueantes

> As pendências abaixo foram verificadas no código em 2026-09-29 e **impedem a
> promoção do domínio para produção** enquanto não forem resolvidas.

| # | Pendência | Impacto | Situação |
| --- | --- | --- | --- |
| PB-01 | Autenticação não aplicada às rotas de `/api/v1/tel` | Qualquer cliente alcançável pode ler e alterar dados cadastrais | **Bloqueante** |
| PB-02 | Autorização por papel não aplicada | Não há distinção entre `admin` e `servidor` | **Bloqueante** |
| PB-03 | Autorização de Destino (BOLA) não implementada | Identificadores opacos não confersem propriedade do objeto | **Bloqueante** |
| PB-04 | `created_by` não deriva de sessão autenticada | A trilha de auditoria não identifica um usuário real | Alta |

---

# 6. Pendências Não Bloqueantes

* A promoção da correspondência `MOD-*` foi concluída em 2026-09-29.
* Os diagramas de sequência e de classes em PlantUML ainda são esboços
  textuais e devem ser validados pelo time de arquitetura.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 021-Checklist-de-Prontidao-para-Producao-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
