# 026 – Modelo-de-Dominio – Governança Municipal

#### Modelo-de-Dominio – Governança Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GOV-026

**Domínio:** Governança Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Governanca-Municipal.md`
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

Este artefato descreve **o modelo de domínio** do domínio Governança Municipal (`DOM-GOV`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| controles_compliance | `` | 13 |
| deliberacoes | `` | 12 |
| politicas_governanca | `` | 13 |
| riscos_governanca | `` | 14 |

---

# 3. Domínios de valor

### TipoPolitica

| Membro | Valor |
| --- | --- |
| POLITICA | 'politica' |
| DIRETRIZ | 'diretriz' |
| NORMA | 'norma' |
| PROCEDIMENTO | 'procedimento' |
### NivelRisco

| Membro | Valor |
| --- | --- |
| BAIXO | 'baixo' |
| MEDIO | 'medio' |
| ALTO | 'alto' |
| CRITICO | 'critico' |
### SituacaoGovernanca

| Membro | Valor |
| --- | --- |
| RASCUNHO | 'rascunho' |
| EM_REVISAO | 'em_revisao' |
| VIGENTE | 'vigente' |
| REVOGADA | 'revogada' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-GOV-001 | toda política declara escopo, responsável, vigência e situação. |
| RN-GOV-002 | todo risco tem dono, classificação de probabilidade e impacto. |
| RN-GOV-003 | o controle de conformidade registra a evidência e o resultado da verificação. |
| RN-GOV-004 | a deliberação vincula-se à política, risco ou controle e guarda histórico. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Governanca-Municipal-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
