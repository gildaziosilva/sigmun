# 012 – Matriz-de-Rastreabilidade – Ouvidoria

#### Matriz-de-Rastreabilidade – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-012

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-OU-001 | RegistrarManifestacao | HU-OU-001 | RF-OU-001 | RF-CUM-001 |
| CU-OU-002 | RegistrarDenuncia | HU-OU-002 | RF-OU-002 | RF-CUM-001 |
| CU-OU-003 | RegistrarPedidoLai | HU-OU-003 | RF-OU-003 | RF-CUM-001 |
| CU-OU-004 | ResponderManifestacao | HU-OU-004 | RF-OU-004 | RF-CUM-001 |
| CU-OU-005 | AlterarStatus | HU-OU-001 | RF-OU-005 | RF-CUM-001 |
| CU-OU-006 | ProrrogarPrazo | HU-OU-002 | RF-OU-006 | RF-CUM-001 |
| CU-OU-007 | AvaliarManifestacao | HU-OU-003 | RF-OU-007 | RF-CUM-001 |
| CU-OU-008 | EncaminharDenuncia | HU-OU-004 | RF-OU-008 | RF-CUM-001 |
| CU-OU-009 | InterporRecursoLai | HU-OU-001 | RF-OU-009 | RF-CUM-001 |
| CU-OU-010 | DecidirRecursoLai | HU-OU-002 | RF-OU-010 | RF-CUM-001 |
| CU-OU-011 | ListarManifestacoes | HU-OU-003 | RF-OU-011 | RF-CUM-001 |
| CU-OU-012 | ListarDenuncias | HU-OU-004 | RF-OU-012 | RF-CUM-001 |
| CU-OU-013 | ListarPedidosLai | HU-OU-001 | RF-OU-013 | RF-CUM-001 |
| CU-OU-014 | ObterManifestacao | HU-OU-002 | RF-OU-014 | RF-CUM-001 |
| CU-OU-015 | ObterEstatisticas | HU-OU-003 | RF-OU-015 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Ouvidoria-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
