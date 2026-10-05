# 006 – Historias-de-Usuario – Identidade e Acesso

#### Historias-de-Usuario – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-006

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

Este artefato detalha **as histórias de usuário** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Histórias

| Identificador | História | Capacidade | Prioridade |
| --- | --- | --- | --- |
| HU-IDN-001 | Como usuário, quero obter token para acessar os serviços do SIGMUN. | CAP-IDN-001 | Alta |
| HU-IDN-002 | Como administrador, quero bloquear um usuário para suspender o acesso. | CAP-IDN-002 | Alta |
| HU-IDN-003 | Como domínio, quero validar o token e o escopo para autorizar a operação. | CAP-IDN-003 | Alta |
| HU-IDN-004 | Como auditor, quero ver as tentativas de login para detectar abuso. | CAP-IDN-004 | Média |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 006-Identidade-e-Acesso-Historias-de-Usuario.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
