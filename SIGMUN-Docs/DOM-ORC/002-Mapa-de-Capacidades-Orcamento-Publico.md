# 002 – Mapa-de-Capacidades – Orçamento Público

#### Mapa-de-Capacidades – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-002

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

Este artefato detalha **o mapa de capacidades** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-ORC-001 | Planejamento orçamentário | Elabora PPA, LDO e LOA. | PRO-ORC-001 |
| CAP-ORC-002 | Dotação e reserva | Autoriza, suplementa, anula e reserva saldo. | PRO-ORC-002 |
| CAP-ORC-003 | Execução | Acompanha a execução do orçamento autorizado. | PRO-ORC-003 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-ORC-001 | Elaborar instrumento | Cria PPA, LDO ou LOA e encaminha para publicação. | RN-ORC-001, RN-ORC-010, RN-ORC-020 |
| PRO-ORC-002 | Autorizar e suplementar | Aprova a LOA e suplementa a dotação. | RN-ORC-011, RN-ORC-021 |
| PRO-ORC-003 | Reservar saldo | Reserva e cancela saldo de dotação. | RN-ORC-030, RN-ORC-031 |
| PRO-ORC-004 | Encerrar exercício | Encerra dotação e reserva do exercício. | RN-ORC-040 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Orcamento-Publico-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
