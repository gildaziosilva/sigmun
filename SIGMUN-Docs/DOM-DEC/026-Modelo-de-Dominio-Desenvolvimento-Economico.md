# 026 – Modelo-de-Dominio – Desenvolvimento Econômico

#### Modelo-de-Dominio – Desenvolvimento Econômico

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DEC-026

**Domínio:** Desenvolvimento Econômico

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Desenvolvimento-Economico.md`
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

Este artefato descreve **o modelo de domínio** do domínio Desenvolvimento Econômico (`DOM-DEC`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| empreendimentos | `` | 13 |
| participacoes_programa | `` | 10 |
| programas_desenvolvimento | `` | 13 |
| projetos_investimento | `` | 12 |

---

# 3. Domínios de valor

### SetorEconomico

| Membro | Valor |
| --- | --- |
| AGROPECUARIA | 'agropecuaria' |
| INDUSTRIA | 'industria' |
| SERVICOS | 'servicos' |
| COMERCIO | 'comercio' |
### PorteEmpresa

| Membro | Valor |
| --- | --- |
| ME | 'me' |
| EPP | 'epp' |
| DEMAIS | 'demais' |
### SituacaoPrograma

| Membro | Valor |
| --- | --- |
| PROPOSTO | 'proposto' |
| APROVADO | 'aprovado' |
| EM_EXECUCAO | 'em_execucao' |
| CONCLUIDO | 'concluido' |
| CANCELADO | 'cancelado' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-DEC-001 | o empreendimento referencia a pessoa jurídica do DOM-CUM por identificador opaco. |
| RN-DEC-002 | a adesão ao programa exige programa em execução e vaga disponível. |
| RN-DEC-003 | o projeto registra investimento e empregos previstos e realizados. |
| RN-DEC-004 | os resultados são repassados ao DOM-IND como valores de indicador econômico. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Desenvolvimento-Economico-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
