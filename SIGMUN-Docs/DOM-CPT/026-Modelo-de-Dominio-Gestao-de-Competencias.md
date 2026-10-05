# 026 – Modelo-de-Dominio – Gestão de Competências

#### Modelo-de-Dominio – Gestão de Competências

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CPT-026

**Domínio:** Gestão de Competências

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Competencias.md`
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

Este artefato descreve **o modelo de domínio** do domínio Gestão de Competências (`DOM-CPT`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| avaliacoes_competencia | `` | 12 |
| capacitacoes | `` | 13 |
| competencias | `` | 11 |
| planos_desenvolvimento | `` | 13 |

---

# 3. Domínios de valor

### CategoriaCompetencia

| Membro | Valor |
| --- | --- |
| TECNICA | 'tecnica' |
| COMPORTAMENTAL | 'comportamental' |
| GERENCIAL | 'gerencial' |
### ModalidadeCapacitacao

| Membro | Valor |
| --- | --- |
| PRESENCIAL | 'presencial' |
| EAD | 'ead' |
| BLENDED | 'blended' |
| MENTORIA | 'mentoria' |
### SituacaoCapacitacao

| Membro | Valor |
| --- | --- |
| PLANEJADA | 'planejada' |
| INSCRICOES_ABERTAS | 'inscricoes_abertas' |
| EM_ANDAMENTO | 'em_andamento' |
| CONCLUIDA | 'concluida' |
| CANCELADA | 'cancelada' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-CPT-001 | lacuna é a diferença entre o nível esperado e o nível avaliado da competência. |
| RN-CPT-002 | capacitação só recebe inscrição com inscrições abertas e vaga disponível. |
| RN-CPT-003 | a pessoa é referenciada por identificador opaco do DOM-PES. |
| RN-CPT-004 | a conclusão registra resultado e pode atualizar a avaliação da competência. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Gestao-de-Competencias-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
