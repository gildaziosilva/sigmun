# 022 – Plano-de-Migracao-de-Dados – Analytics e Inteligência

#### Plano-de-Migracao-de-Dados – Analytics e Inteligência

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ANA-022

**Domínio:** Analytics e Inteligência

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Analytics-e-Inteligencia.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato descreve **o plano de migração de dados** do domínio Analytics e Inteligência (`DOM-ANA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Tabelas

| Tabela | Colunas | Classe ORM |
| --- | --- | --- |
| analises | 14 | `` |
| fontes_analiticas | 13 | `` |
| modelos_analiticos | 14 | `` |
| recomendacoes | 11 | `` |

---

# 3. Estratégia

Carga inicial por migração Alembic; sem conversão de legado.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 022-Analytics-e-Inteligencia-Plano-de-Migracao-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
