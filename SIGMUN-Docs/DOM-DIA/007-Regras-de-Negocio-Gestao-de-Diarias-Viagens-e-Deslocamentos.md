# 007 – Regras-de-Negocio – Gestão de Diárias, Viagens e Deslocamentos

#### Regras-de-Negocio – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-007

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **as regras de negócio** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Regras implementadas

| Identificador | Descrição | Fonte |
| --- | --- | --- |
| RN-DIA-001 | A diária é criada com status SOLICITADA | `src/modules/sigmun_dia` |
| RN-DIA-002 | A diária deve estar associada a uma viagem válida | `src/modules/sigmun_dia` |
| RN-DIA-003 | SOLICITADA → AUTORIZADA → CALCULADA → CONCEDIDA → | `src/modules/sigmun_dia` |
| RN-DIA-004 | Concede a diária (autorização final) | `src/modules/sigmun_dia` |
| RN-DIA-005 | Inicia o período de prestação de contas | `src/modules/sigmun_dia` |
| RN-DIA-006 | Finaliza o período de prestação de contas | `src/modules/sigmun_dia` |
| RN-DIA-007 | Registra o pagamento da diária | `src/modules/sigmun_dia` |
| RN-DIA-009 | Prestação de contas requer documento GDO anexado | `src/modules/sigmun_dia` |
| RN-DIA-015 | Aprovação requer: | `src/modules/sigmun_dia` |
| RN-DIA-016 | Glosa requer: | `src/modules/sigmun_dia` |
| RN-DIA-017 | Restituição requer: | `src/modules/sigmun_dia` |

---

# 3. Cobertura

Regras referenciadas no código: **11**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 007-Gestao-de-Diarias-Viagens-e-Deslocamentos-Regras-de-Negocio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
