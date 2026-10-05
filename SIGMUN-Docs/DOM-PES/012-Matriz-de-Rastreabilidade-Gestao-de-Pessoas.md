# 012 – Matriz-de-Rastreabilidade – Gestão de Pessoas

#### Matriz-de-Rastreabilidade – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-012

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

Este artefato detalha **a matriz de rastreabilidade** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-PES-001 | CriarCargo | HU-PES-001 | RF-PES-001 | RF-CUM-001 |
| CU-PES-002 | AdmitirServidor | HU-PES-002 | RF-PES-002 | RF-CUM-001 |
| CU-PES-003 | AfastarServidor | HU-PES-003 | RF-PES-003 | RF-CUM-001 |
| CU-PES-004 | ReativarServidor | HU-PES-004 | RF-PES-004 | RF-CUM-001 |
| CU-PES-005 | DesligarServidor | HU-PES-005 | RF-PES-005 | RF-CUM-001 |
| CU-PES-006 | PlanejarFerias | HU-PES-001 | RF-PES-006 | RF-CUM-001 |
| CU-PES-007 | AprovarFerias | HU-PES-002 | RF-PES-007 | RF-CUM-001 |
| CU-PES-008 | IniciarGozoFerias | HU-PES-003 | RF-PES-008 | RF-CUM-001 |
| CU-PES-009 | ConcluirFerias | HU-PES-004 | RF-PES-009 | RF-CUM-001 |
| CU-PES-010 | AbrirFolha | HU-PES-005 | RF-PES-010 | RF-CUM-001 |
| CU-PES-011 | ConsolidarFolha | HU-PES-001 | RF-PES-011 | RF-CUM-001 |
| CU-PES-012 | FecharFolha | HU-PES-002 | RF-PES-012 | RF-CUM-001 |
| CU-PES-013 | ReabrirFolha | HU-PES-003 | RF-PES-013 | RF-CUM-001 |
| CU-PES-014 | HomologarFolha | HU-PES-004 | RF-PES-014 | RF-CUM-001 |
| CU-PES-015 | PagarFolha | HU-PES-005 | RF-PES-015 | RF-CUM-001 |
| CU-PES-016 | RegistrarFrequencia | HU-PES-001 | RF-PES-016 | RF-CUM-001 |
| CU-PES-017 | JustificarFalta | HU-PES-002 | RF-PES-017 | RF-CUM-001 |
| CU-PES-018 | LotarServidor | HU-PES-003 | RF-PES-018 | RF-CUM-001 |
| CU-PES-019 | RemoverServidor | HU-PES-004 | RF-PES-019 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Gestao-de-Pessoas-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
