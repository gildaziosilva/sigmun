# 007 – Regras-de-Negocio – Infraestrutura Tecnológica

#### Regras-de-Negocio – Infraestrutura Tecnológica

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INF-007

**Domínio:** Infraestrutura Tecnológica

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Infraestrutura-Tecnologica.md`
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

Este artefato descreve **as regras de negócio** do domínio Infraestrutura Tecnológica (`DOM-INF`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Regras propostas

| Identificador | Descrição | Fonte |
| --- | --- | --- |
| RN-INF-001 | o recurso pertence a um ambiente e registra tipo e situação. | modelo proposto |
| RN-INF-002 | métrica coletada além do limite gera status de atenção ou crítico. | modelo proposto |
| RN-INF-003 | o incidente tem severidade, responsável, data de abertura e data de encerramento. | modelo proposto |
| RN-INF-004 | ativos de dados são referenciados no DOM-DAD por identificador. | modelo proposto |

---

# 3. Cobertura

Regras referenciadas no código: **4**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 007-Infraestrutura-Tecnologica-Regras-de-Negocio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
