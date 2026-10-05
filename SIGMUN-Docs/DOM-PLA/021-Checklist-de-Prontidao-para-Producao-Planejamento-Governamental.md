# 021 – Checklist-de-Prontidao-para-Producao – Planejamento Governamental

#### Checklist-de-Prontidao-para-Producao – Planejamento Governamental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PLA-021

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

Este artefato descreve **o checklist de prontidão** do domínio Planejamento Governamental (`DOM-PLA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Itens

| Item | Situação | Evidência |
| --- | --- | --- |
| Esquema de persistência | PROPOSTO | 4 tabelas previstas |
| API publicada | PROPOSTA | Contrato previsto em `/api/v1/pla` |
| Regras propostas | NÃO APLICÁVEL | 4 regras propostas |
| Suíte de testes | NÃO APLICÁVEL | Testes serão definidos na implementação |
| Autenticação das escritas | OK | JWT do DOM-IDN obrigatório (ADR-0007) |
| Compatibilidade legada | EM TRANSIÇÃO | Header X-Usuario-Id aceito e depreciado |
| Revisão periódica | OK | Política de 12 meses definida no ADR-0007 |
| Compartilhamento de pessoa | OK | Contrato formal no ADR-0007 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 021-Planejamento-Governamental-Checklist-de-Prontidao-para-Producao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
