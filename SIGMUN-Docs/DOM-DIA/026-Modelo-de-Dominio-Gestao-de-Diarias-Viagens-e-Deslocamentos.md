# 026 – Modelo-de-Dominio – Gestão de Diárias, Viagens e Deslocamentos

#### Modelo-de-Dominio – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-026

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

Este artefato detalha **o modelo de domínio** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| diarias | `DiariaModel` | 31 |
| eventos_diarias | `EventoDiariaModel` | 8 |
| prestacoes_contas | `PrestacaoContasModel` | 17 |
| viagens | `ViagemModel` | 15 |

---

# 3. Domínios de valor

### StatusDiaria

| Membro | Valor |
| --- | --- |
| SOLICITADA | "solicitada" |
| AUTORIZADA | "autorizada" |
| CALCULADA | "calculada" |
| CONCEDIDA | "concedida" |
| EM_PRESTACAO | "em_prestacao" |
| PAGA | "paga" |
| APROVADA | "aprovada" |
| GLOSA | "glosa" |
| RESTITUIDA | "restituida" |
| CANCELADA | "cancelada" |
### CategoriaDiaria

| Membro | Valor |
| --- | --- |
| EVENTO | "evento" |
| REUNIAO | "reuniao" |
| TREINAMENTO | "treinamento" |
| VIAGEM_OFICIAL | "viagem_oficial" |
| SERVICO_CONSULTIVO | "servico_consultivo" |
### TipoDeslocamento

| Membro | Valor |
| --- | --- |
| TERRESTRE | "terrestre" |
| AEREO | "aereo" |
| FLUVIAL | "fluvial" |
| MARITIMO | "maritimo" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-DIA-001 | A diária é criada com status SOLICITADA |
| RN-DIA-002 | A diária deve estar associada a uma viagem válida |
| RN-DIA-003 | SOLICITADA → AUTORIZADA → CALCULADA → CONCEDIDA → |
| RN-DIA-004 | Concede a diária (autorização final) |
| RN-DIA-005 | Inicia o período de prestação de contas |
| RN-DIA-006 | Finaliza o período de prestação de contas |
| RN-DIA-007 | Registra o pagamento da diária |
| RN-DIA-009 | Prestação de contas requer documento GDO anexado |
| RN-DIA-015 | Aprovação requer: |
| RN-DIA-016 | Glosa requer: |
| RN-DIA-017 | Restituição requer: |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Gestao-de-Diarias-Viagens-e-Deslocamentos-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
