# 011 – Criterios-de-Aceitacao – Gestão de Pessoas

#### Criterios-de-Aceitacao – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-011

**Domínio:** Gestão de Pessoas

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Pessoas.md`
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

Este artefato detalha **os critérios de aceitação** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Critérios

| ID | Categoria | Critério | Verificação |
| --- | --- | --- | --- |
| CA-PES-001 | Identificação | Matrícula e CPF do servidor são únicos. | Teste automatizado |
| CA-PES-002 | Imutabilidade | Folha homologada ou paga é terminal. | Teste automatizado |
| CA-PES-003 | Rastreabilidade | Admissão, lotação, folha e férias registram autor e data. | Teste automatizado |
| CA-PES-004 | Sigilo | Remuneração e frequência são dados pessoais (LGPD). | Teste automatizado |
| CA-PES-005 | Compatibilidade | Sem chave estrangeira entre schemas. | Teste automatizado |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 011-Gestao-de-Pessoas-Criterios-de-Aceitacao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
