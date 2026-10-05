# 012 – Matriz-de-Rastreabilidade – Identidade e Acesso

#### Matriz-de-Rastreabilidade – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-012

**Domínio:** Identidade e Acesso

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Identidade-e-Acesso.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-IDN-001 | CriarUsuario | HU-IDN-001 | RF-IDN-001 | RF-CUM-001 |
| CU-IDN-002 | RegistrarUsuario | HU-IDN-002 | RF-IDN-002 | RF-CUM-001 |
| CU-IDN-003 | AtivarUsuario | HU-IDN-003 | RF-IDN-003 | RF-CUM-001 |
| CU-IDN-004 | DesativarUsuario | HU-IDN-004 | RF-IDN-004 | RF-CUM-001 |
| CU-IDN-005 | BloquearUsuario | HU-IDN-001 | RF-IDN-005 | RF-CUM-001 |
| CU-IDN-006 | BuscarUsuario | HU-IDN-002 | RF-IDN-006 | RF-CUM-001 |
| CU-IDN-007 | ConsultarUsuario | HU-IDN-003 | RF-IDN-007 | RF-CUM-001 |
| CU-IDN-008 | ListarUsuarios | HU-IDN-004 | RF-IDN-008 | RF-CUM-001 |
| CU-IDN-009 | AutenticarUsuario | HU-IDN-001 | RF-IDN-009 | RF-CUM-001 |
| CU-IDN-010 | Logout | HU-IDN-002 | RF-IDN-010 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Identidade-e-Acesso-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
