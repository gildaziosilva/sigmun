# 006 – Historias-de-Usuario – Gestão de Diárias, Viagens e Deslocamentos

#### Historias-de-Usuario – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-006

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **as histórias de usuário** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Histórias

| Identificador | História | Capacidade | Prioridade |
| --- | --- | --- | --- |
| HU-DIA-001 | Como servidor, quero registrar a viagem para que a diária seja vinculada. | CAP-DIA-001 | Alta |
| HU-DIA-002 | Como gestor, quero autorizar a diária para liberar o pagamento. | CAP-DIA-002 | Alta |
| HU-DIA-003 | ('HU-IDN-003', 'Como domínio, quero validar o escopo do token.', 'CAP-IDN-003', 'Alta') | CAP-DIA-003 | Alta |
| HU-DIA-004 | Como contabilidade, quero glosar a prestação com motivo para corrigir o valor. | CAP-DIA-003 | Média |
| HU-DIA-005 | Como auditor, quero consultar o histórico para rastrear a decisão. | CAP-DIA-004 | Média |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 006-Gestao-de-Diarias-Viagens-e-Deslocamentos-Historias-de-Usuario.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
