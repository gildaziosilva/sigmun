# 014 – Modelo-de-Integracao – Mobilidade e Serviços de Campo

#### Modelo-de-Integracao – Mobilidade e Serviços de Campo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MOB-014

**Domínio:** Mobilidade e Serviços de Campo

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`
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

Este artefato descreve **o modelo de integração** do domínio Mobilidade e Serviços de Campo (`DOM-MOB`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Princípios

* Sem chave estrangeira entre schemas de domínios.
* Comunicação por contrato (API ou evento).
* Contrato previsto em `/api/v1/mob`.

---

# 3. Integrações

| Domínio | Nome | Sentido | Finalidade |
| --- | --- | --- | --- |
| DOM-GEO | Geoinformação Municipal | Fornece | integração registrada no mapa de domínios |
| DOM-TEL | Gestão Territorial | Consome | integração registrada no mapa de domínios |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 014-Mobilidade-e-Servicos-de-Campo-Modelo-de-Integracao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
