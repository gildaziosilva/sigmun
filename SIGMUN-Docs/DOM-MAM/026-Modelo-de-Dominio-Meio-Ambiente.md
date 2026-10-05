# 026 – Modelo-de-Dominio – Meio Ambiente

#### Modelo-de-Dominio – Meio Ambiente

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MAM-026

**Domínio:** Meio Ambiente

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Meio-Ambiente.md`
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

Este artefato descreve **o modelo de domínio** do domínio Meio Ambiente (`DOM-MAM`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| areas_protegidas | `` | 12 |
| fiscalizacoes_ambientais | `` | 13 |
| licencimentos_ambientais | `` | 13 |
| monitoramentos_ambientais | `` | 13 |

---

# 3. Domínios de valor

### TipoLicenciamento

| Membro | Valor |
| --- | --- |
| LICENCA | 'licenca' |
| AUTORIZACAO | 'autorizacao' |
| OUTORGA | 'outorga' |
| APROVACAO | 'aprovacao' |
### SituacaoLicenciamento

| Membro | Valor |
| --- | --- |
| SOLICITADO | 'solicitado' |
| EM_ANALISE | 'em_analise' |
| LICENCIADO | 'licenciado' |
| NEGADO | 'negado' |
| SUSPENSO | 'suspenso' |
| REVOGADO | 'revogado' |
### ResultadoFiscalizacao

| Membro | Valor |
| --- | --- |
| CONFORME | 'conforme' |
| NAO_CONFORME | 'nao_conforme' |
| PENDENTE | 'pendente' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-MAM-001 | a licença tem validade e condições; vencida, ela não autoriza a atividade. |
| RN-MAM-002 | resultado não conforme gera prazo de adequação e nova vistoria. |
| RN-MAM-003 | o monitoramento compara o valor medido com o limite legal. |
| RN-MAM-004 | a referência territorial vem do DOM-TEL ou DOM-GEO, sem cópia. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Meio-Ambiente-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
