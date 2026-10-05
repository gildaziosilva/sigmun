# 026 – Modelo-de-Dominio – Planejamento Governamental

#### Modelo-de-Dominio – Planejamento Governamental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PLA-026

**Domínio:** Planejamento Governamental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Planejamento-Governamental.md`
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

Este artefato descreve **o modelo de domínio** do domínio Planejamento Governamental (`DOM-PLA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| metas | `` | 13 |
| planos_estrategicos | `` | 13 |
| programas | `` | 12 |
| projetos | `` | 14 |

---

# 3. Domínios de valor

### SituacaoPlanejamento

| Membro | Valor |
| --- | --- |
| RASCUNHO | 'rascunho' |
| EM_APROVACAO | 'em_aprovacao' |
| APROVADO | 'aprovado' |
| EM_EXECUCAO | 'em_execucao' |
| SUSPENSO | 'suspenso' |
| CONCLUIDO | 'concluido' |
| CANCELADO | 'cancelado' |
### TipoMeta

| Membro | Valor |
| --- | --- |
| PERCENTUAL | 'percentual' |
| VALOR | 'valor' |
| QUANTIDADE | 'quantidade' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-PLA-001 | programa pertence a um plano estratégico e projeto pertence a um programa. |
| RN-PLA-002 | meta declara indicador de referência, valor base, valor alvo e prazo. |
| RN-PLA-003 | projeto concluído exige encerramento formal com o resultado registrado. |
| RN-PLA-004 | resultados vão ao DOM-IND como valores, sem duplicar o indicador. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Planejamento-Governamental-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
