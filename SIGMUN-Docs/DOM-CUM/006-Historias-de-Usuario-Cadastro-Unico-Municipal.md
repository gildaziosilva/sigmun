# 006 – Historias-de-Usuario – Cadastro Único Municipal

#### Historias-de-Usuario – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-006

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **as histórias de usuário** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Histórias

| Identificador | História | Capacidade | Prioridade |
| --- | --- | --- | --- |
| HU-CUM-001 | Registrar pessoa com contatos como fonte oficial. | CAP-CUM-001 | Alta |
| HU-CUM-002 | Registrar a extensão física ou jurídica correta. | CAP-CUM-002 | Alta |
| HU-CUM-003 | Adicionar endereço com vigência rastreável. | CAP-CUM-003 | Média |
| HU-CUM-004 | Validar CPF e CNPJ para evitar duplicidade. | CAP-CUM-004 | Alta |
| HU-CUM-005 | Manter hierarquia de unidades administrativas. | CAP-CUM-006 | Média |
| HU-CUM-006 | Consultar pessoa por identificador. | CAP-CUM-007 | Alta |
| HU-CUM-007 | Registrar autoria e data de toda alteração. | CAP-CUM-001 | Alta |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 006-Cadastro-Unico-Municipal-Historias-de-Usuario.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
