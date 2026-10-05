# 002 – Mapa-de-Capacidades – Identidade e Acesso

#### Mapa-de-Capacidades – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-002

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

Este artefato detalha **o mapa de capacidades** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-IDN-001 | Autenticação | Emite e renova token JWT de acesso. | PRO-IDN-001 |
| CAP-IDN-002 | Gestão de usuários | Registra, ativa, bloqueia e desativa usuários. | PRO-IDN-002 |
| CAP-IDN-003 | Papéis e permissões | Mantém papéis, permissões e seus vínculos. | PRO-IDN-003 |
| CAP-IDN-004 | Sessões e auditoria | Controla sessão e registra tentativas de login. | PRO-IDN-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-IDN-001 | Autenticar | Valida credenciais e emite o par de tokens. | RN-IDN-001 |
| PRO-IDN-002 | Gerenciar usuário | Registra, ativa, bloqueia e desativa. | RN-IDN-002 |
| PRO-IDN-003 | Conceder acesso | Vincula papéis e permissões por escopo. | RN-IDN-003 |
| PRO-IDN-004 | Auditar acesso | Registra tentativa de login e sessão. | RN-IDN-004 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Identidade-e-Acesso-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
