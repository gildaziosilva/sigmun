# 001 – Mapa-de-Atores – Assistência Social

#### Mapa-de-Atores – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-001

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **o mapa de atores** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-ASS-001 | Técnico de CRAS/CREAS | Interno | Servidor público | Executa o atendimento e registra a evolução da família. |
| AT-ASS-002 | Gestor de unidade | Interno | Gestor do CRAS/CREAS | Autoriza benefícios e responde pela unidade. |
| AT-ASS-003 | Família em situação de vulnerabilidade | Externo | Cidadão | Recebe o atendimento e apresenta a documentação. |
| AT-ASS-004 | Conselho Municipal de Assistência | Externo | Colegiado | Acompanha e delibera sobre a execução. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-ASS-001 |  |
| AT-ASS-002 |  |
| AT-ASS-003 |  |
| AT-ASS-004 |  |

---

# 4. Lacunas a validar

* Definir o glossário de tipos de benefício eventual por município.
* Formalizar o fluxo de aferimento de renda com o DOM-IND.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Assistencia-Social-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
