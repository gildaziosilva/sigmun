# 014 – Modelo-de-Integracao – Administração Tributária

#### Modelo-de-Integracao – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-014

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
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

Este artefato detalha **o modelo de integração** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Princípios

* Sem chave estrangeira entre schemas de domínios.
* Comunicação por contrato (API ou evento).
* Contrato publicado em `/api/v1/tri`.

---

# 3. Integrações

| Domínio | Nome | Sentido | Finalidade |
| --- | --- | --- | --- |
| DOM-CUM | Cadastro Único Municipal | Fornece | Identificação do contribuinte. |
| DOM-TEL | Gestão Territorial | Fornece | Base territorial do imóvel. |
| DOM-GEO | Geoinformação Municipal | Fornece | Planta de valores vigente. |
| DOM-CON | Contabilidade Pública | Fornece | Baixa contábil do lançamento. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 014-Administracao-Tributaria-Modelo-de-Integracao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
