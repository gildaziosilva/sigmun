# 002 – Mapa-de-Capacidades – Dados Corporativos

#### Mapa-de-Capacidades – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-002

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **o mapa de capacidades** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-DAD-001 | Catálogo de ativos | Registra e cataloga os ativos de dado do município. | PRO-DAD-001 |
| CAP-DAD-002 | Qualidade do dado | Avalia dimensões e nível de qualidade. | PRO-DAD-002 |
| CAP-DAD-003 | Linhagem | Registra a origem e as transformações do dado. | PRO-DAD-003 |
| CAP-DAD-004 | Políticas de dados | Versiona a política de gestão e uso de dados. | PRO-DAD-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-DAD-001 | Publicar ativo de dado | Cadastra o ativo, cataloga e ativa. | RN-DAD-001 |
| PRO-DAD-002 | Avaliar qualidade | Atualiza dimensões e nível de qualidade. | RN-DAD-002 |
| PRO-DAD-003 | Rastrear linhagem | Registra origem e transformação do dado. | RN-DAD-003 |
| PRO-DAD-004 | Versionar política | Cria e publica a política de dados. | RN-DAD-004 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Dados-Corporativos-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
