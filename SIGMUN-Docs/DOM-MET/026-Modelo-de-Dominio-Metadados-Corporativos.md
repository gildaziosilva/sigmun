# 026 – Modelo-de-Dominio – Metadados Corporativos

#### Modelo-de-Dominio – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-026

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **o modelo de domínio** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| classificacoes | `ClassificacaoModel` | 13 |
| metadados | `MetadadoModel` | 17 |
| taxonomias | `TaxonomiaModel` | 11 |
| termos_taxonomias | `TermoTaxonomiaModel` | 14 |
| valores_metadados | `ValorMetadadoModel` | 11 |

---

# 3. Domínios de valor

### TipoDadoMetadado

| Membro | Valor |
| --- | --- |
| TEXTO | "texto" |
| NUMERO | "numero" |
| DATA | "data" |
| BOOLEANO | "booleano" |
| LISTA | "lista" |
| JSON | "json" |
### StatusMetadado

| Membro | Valor |
| --- | --- |
| ATIVO | "ativo" |
| INATIVO | "inativo" |
### TipoClassificacao

| Membro | Valor |
| --- | --- |
| CONFIDENCIALIDADE | "confidencialidade" |
| ASSUNTO | "assunto" |
| RETENCAO | "retencao" |
| ORIGEM | "origem" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-MET-001 | metadado não pode ser duplicado para a mesma entidade e atributo. |
| RN-MET-002 | classificação vigente determina o acesso e a obrigatoriedade. |
| RN-MET-003 | taxonomiaterms devem referenciar a taxonomia vigente. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Metadados-Corporativos-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
