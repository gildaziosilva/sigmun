# 002 – Mapa-de-Capacidades – Metadados Corporativos

#### Mapa-de-Capacidades – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-002

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

Este artefato detalha **o mapa de capacidades** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-MET-001 | Metadados | Registra, consulta e ativa metadados de dado. | PRO-MET-001 |
| CAP-MET-002 | Classificação | Classifica a informação e define obrigatoriedade. | PRO-MET-002 |
| CAP-MET-003 | Taxonomias | Organiza termos e hierarquias de domínios. | PRO-MET-003 |
| CAP-MET-004 | Consulta semântica | Busca metadados por entidade e atributo. | PRO-MET-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-MET-001 | Registrar metadado | Cria metadado com tipo, obrigatoriedade e escopo. | RN-MET-001 |
| PRO-MET-002 | Classificar informação | Aplica classificação e define valor padrão. | RN-MET-002 |
| PRO-MET-003 | Curar taxonomia | Cria taxonomia, termos e hierarquia. | RN-MET-003 |
| PRO-MET-004 | Consultar catálogo | Lista e busca metadados por entidade. | — |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Metadados-Corporativos-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
