# 026 – Modelo-de-Dominio – Analytics e Inteligência

#### Modelo-de-Dominio – Analytics e Inteligência

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ANA-026

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

Este artefato descreve **o modelo de domínio** do domínio Analytics e Inteligência (`DOM-ANA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| analises | `` | 14 |
| fontes_analiticas | `` | 13 |
| modelos_analiticos | `` | 14 |
| recomendacoes | `` | 11 |

---

# 3. Domínios de valor

### TipoModeloAnalitico

| Membro | Valor |
| --- | --- |
| ESTATISTICO | 'estatistico' |
| PREDITIVO | 'preditivo' |
| CLUSTERIZACAO | 'clusterizacao' |
| IA | 'ia' |
### SituacaoAnalitica

| Membro | Valor |
| --- | --- |
| RASCUNHO | 'rascunho' |
| EM_VALIDACAO | 'em_validacao' |
| EM_PRODUCAO | 'em_producao' |
| DESCONTINUADO | 'descontinuado' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-ANA-001 | a fonte referencia ativo do DOM-DAD por identificador; sem cópia. |
| RN-ANA-002 | modelo em produção declara versão, métrica e data de treinamento. |
| RN-ANA-003 | a análise registra fonte, modelo quando houver, responsável e data. |
| RN-ANA-004 | resultado aplicado a decisão pública é rastreável até a análise que o originou. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Analytics-e-Inteligencia-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
