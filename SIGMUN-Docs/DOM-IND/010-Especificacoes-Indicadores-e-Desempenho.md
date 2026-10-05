# 010 – Especificacoes – Indicadores e Desempenho

#### Especificacoes – Indicadores e Desempenho

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IND-010

**Domínio:** Indicadores e Desempenho

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Indicadores-e-Desempenho.md`
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

Este artefato descreve **as especificações** do domínio Indicadores e Desempenho (`DOM-IND`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Contratos previstos

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| PLANEJADO | `/api/v1/ind` | proposto | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-IND-001 | o indicador declara fórmula, unidade, periodicidade e fonte. |
| RN-IND-002 | a meta é anual e declara valor base, valor alvo, prazo e responsável. |
| RN-IND-003 | o valor coletado só é publicado após validação do responsável. |
| RN-IND-004 | a fonte é referenciada ao DOM-DAD por identificador; sem cópia. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Indicadores-e-Desempenho-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
