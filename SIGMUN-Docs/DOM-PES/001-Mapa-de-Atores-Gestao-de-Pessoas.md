# 001 – Mapa-de-Atores – Gestão de Pessoas

#### Mapa-de-Atores – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-001

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

Este artefato detalha **o mapa de atores** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-PES-001 | Servidor público | Interno | Servidor | Cadastra férias, frequência e lotação. |
| AT-PES-002 | Gestor de pessoas | Interno | Gestor | Admite, afasta, desliga e lota o servidor. |
| AT-PES-003 | Contabilidade | Externo | Setor contábil | Consolida, fecha e paga a folha. |
| AT-PES-004 | Gestor da unidade | Externo | Órgão | Confirma o desempenho e a lotação. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-PES-001 |  |
| AT-PES-002 |  |
| AT-PES-003 |  |
| AT-PES-004 |  |

---

# 4. Lacunas a validar

* Definir a integração do SIGRH ou sistema estadual de folha.
* Definir o calendário de férias por mês de gozo.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Gestao-de-Pessoas-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
