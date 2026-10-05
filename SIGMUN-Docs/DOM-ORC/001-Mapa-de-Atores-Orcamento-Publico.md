# 001 – Mapa-de-Atores – Orçamento Público

#### Mapa-de-Atores – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-001

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **o mapa de atores** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-ORC-001 | Elaborador do orçamento | Interno | Servidor público | Elabora PPA, LDO e LOA. |
| AT-ORC-002 | Ordenador de despesa | Interno | Autoridade competente | Aprova o orçamento e a suplementação. |
| AT-ORC-003 | Contabilidade | Externo | Setor contábil | Executa dotação, reserva e empenho. |
| AT-ORC-004 | Cidadão | Externo | Cidadão | Consulta a execução orçamentária. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-ORC-001 |  |
| AT-ORC-002 |  |
| AT-ORC-003 |  |
| AT-ORC-004 |  |

---

# 4. Lacunas a validar

* API registrada em src/main.py (resolvido): 12 operações expostas em /api/v1/orc.
* Definir a integração com o sistema de SIMEOR de orçamento.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Orcamento-Publico-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
