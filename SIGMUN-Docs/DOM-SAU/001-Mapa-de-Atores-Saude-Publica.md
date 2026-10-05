# 001 – Mapa-de-Atores – Saúde Pública

#### Mapa-de-Atores – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-001

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **o mapa de atores** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-SAU-001 | Profissional de saúde | Interno | Servidor público | Registra atendimento e agenda consulta. |
| AT-SAU-002 | Recepcionista | Interno | Servidor público | Cadastra paciente e confirma agendamento. |
| AT-SAU-003 | Paciente | Externo | Cidadão | Busca atendimento, agendamento e medicamento. |
| AT-SAU-004 | Autorizador de regulação | Interno | Coordenação | Autoriza a regulação conforme fila e prioridade. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-SAU-001 |  |
| AT-SAU-002 |  |
| AT-SAU-003 |  |
| AT-SAU-004 |  |

---

# 4. Lacunas a validar

* Definir a integração com o prontuário estadual.
* Definir a regra de dispensação por tipo de medicamento.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Saude-Publica-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
