# 012 – Matriz-de-Rastreabilidade – Segurança da Informação

#### Matriz-de-Rastreabilidade – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-012

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-SEG-001 | CriarChave | HU-SEG-001 | RF-SEG-001 | RF-CUM-001 |
| CU-SEG-002 | BuscarChave | HU-SEG-002 | RF-SEG-002 | RF-CUM-001 |
| CU-SEG-003 | AtualizarChave | HU-SEG-003 | RF-SEG-003 | RF-CUM-001 |
| CU-SEG-004 | RevogarChave | HU-SEG-004 | RF-SEG-004 | RF-CUM-001 |
| CU-SEG-005 | ExpirarChave | HU-SEG-001 | RF-SEG-005 | RF-CUM-001 |
| CU-SEG-006 | DeletarChave | HU-SEG-002 | RF-SEG-006 | RF-CUM-001 |
| CU-SEG-007 | CriarControleSeguranca | HU-SEG-003 | RF-SEG-007 | RF-CUM-001 |
| CU-SEG-008 | BuscarControleSeguranca | HU-SEG-004 | RF-SEG-008 | RF-CUM-001 |
| CU-SEG-009 | AtualizarControleSeguranca | HU-SEG-001 | RF-SEG-009 | RF-CUM-001 |
| CU-SEG-010 | ImplementarControleSeguranca | HU-SEG-002 | RF-SEG-010 | RF-CUM-001 |
| CU-SEG-011 | ParcialmenteImplementado | HU-SEG-003 | RF-SEG-011 | RF-CUM-001 |
| CU-SEG-012 | DeletarControleSeguranca | HU-SEG-004 | RF-SEG-012 | RF-CUM-001 |
| CU-SEG-013 | CriarCredencial | HU-SEG-001 | RF-SEG-013 | RF-CUM-001 |
| CU-SEG-014 | BuscarCredencial | HU-SEG-002 | RF-SEG-014 | RF-CUM-001 |
| CU-SEG-015 | SuspenderCredencial | HU-SEG-003 | RF-SEG-015 | RF-CUM-001 |
| CU-SEG-016 | RevogarCredencial | HU-SEG-004 | RF-SEG-016 | RF-CUM-001 |
| CU-SEG-017 | RegistrarFalhaCredencial | HU-SEG-001 | RF-SEG-017 | RF-CUM-001 |
| CU-SEG-018 | RegistrarUsoCredencial | HU-SEG-002 | RF-SEG-018 | RF-CUM-001 |
| CU-SEG-019 | DeletarCredencial | HU-SEG-003 | RF-SEG-019 | RF-CUM-001 |
| CU-SEG-020 | RegistrarIncidenteSeguranca | HU-SEG-004 | RF-SEG-020 | RF-CUM-001 |
| CU-SEG-021 | BuscarIncidenteSeguranca | HU-SEG-001 | RF-SEG-021 | RF-CUM-001 |
| CU-SEG-022 | EscalarIncidenteSeguranca | HU-SEG-002 | RF-SEG-022 | RF-CUM-001 |
| CU-SEG-023 | MitigarIncidenteSeguranca | HU-SEG-003 | RF-SEG-023 | RF-CUM-001 |
| CU-SEG-024 | ResolverIncidenteSeguranca | HU-SEG-004 | RF-SEG-024 | RF-CUM-001 |
| CU-SEG-025 | EncerrarIncidenteSeguranca | HU-SEG-001 | RF-SEG-025 | RF-CUM-001 |
| CU-SEG-026 | DeletarIncidenteSeguranca | HU-SEG-002 | RF-SEG-026 | RF-CUM-001 |
| CU-SEG-027 | CriarPoliticaSeguranca | HU-SEG-003 | RF-SEG-027 | RF-CUM-001 |
| CU-SEG-028 | BuscarPoliticaSeguranca | HU-SEG-004 | RF-SEG-028 | RF-CUM-001 |
| CU-SEG-029 | AtualizarPoliticaSeguranca | HU-SEG-001 | RF-SEG-029 | RF-CUM-001 |
| CU-SEG-030 | AprovarPoliticaSeguranca | HU-SEG-002 | RF-SEG-030 | RF-CUM-001 |
| CU-SEG-031 | DeletarPoliticaSeguranca | HU-SEG-003 | RF-SEG-031 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Seguranca-da-Informacao-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
