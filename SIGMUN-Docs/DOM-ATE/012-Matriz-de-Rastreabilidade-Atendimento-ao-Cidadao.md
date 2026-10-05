# 012 – Matriz-de-Rastreabilidade – Atendimento ao Cidadão

#### Matriz-de-Rastreabilidade – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-012

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-ATE-001 | RealizarTriagem | HU-ATE-001 | RF-ATE-001 | RF-CUM-001 |
| CU-ATE-002 | AbrirFila | HU-ATE-002 | RF-ATE-002 | RF-CUM-001 |
| CU-ATE-003 | FecharFila | HU-ATE-003 | RF-ATE-003 | RF-CUM-001 |
| CU-ATE-004 | EmitirSenha | HU-ATE-001 | RF-ATE-004 | RF-CUM-001 |
| CU-ATE-005 | ChamarSenha | HU-ATE-002 | RF-ATE-005 | RF-CUM-001 |
| CU-ATE-006 | RechamarSenha | HU-ATE-003 | RF-ATE-006 | RF-CUM-001 |
| CU-ATE-007 | MarcarSenhaAtendida | HU-ATE-001 | RF-ATE-007 | RF-CUM-001 |
| CU-ATE-008 | IniciarAtendimento | HU-ATE-002 | RF-ATE-008 | RF-CUM-001 |
| CU-ATE-009 | ConcluirAtendimento | HU-ATE-003 | RF-ATE-009 | RF-CUM-001 |
| CU-ATE-010 | CancelarAtendimento | HU-ATE-001 | RF-ATE-010 | RF-CUM-001 |
| CU-ATE-011 | RegistrarAvaliacao | HU-ATE-002 | RF-ATE-011 | RF-CUM-001 |
| CU-ATE-012 | CriarEncaminhamento | HU-ATE-003 | RF-ATE-012 | RF-CUM-001 |
| CU-ATE-013 | ConcluirEncaminhamento | HU-ATE-001 | RF-ATE-013 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Atendimento-ao-Cidadao-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
