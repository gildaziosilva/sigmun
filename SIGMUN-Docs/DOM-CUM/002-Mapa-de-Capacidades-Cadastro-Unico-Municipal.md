# 002 – Mapa-de-Capacidades – Cadastro Único Municipal

#### Mapa-de-Capacidades – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-002

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

Este artefato detalha **o mapa de capacidades** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-CUM-001 | Cadastro de pessoa | Registra, consulta, altera e exclui logicamente pessoas. | PRO-CUM-001 |
| CAP-CUM-002 | Extensão por tipo | Mantém a extensão 1:1 de pessoa física ou jurídica. | PRO-CUM-001 |
| CAP-CUM-003 | Endereços | Controla o histórico de vigência e o endereço principal. | PRO-CUM-002 |
| CAP-CUM-004 | Documentos | Vincula documentos com validação de CPF e CNPJ. | PRO-CUM-002 |
| CAP-CUM-005 | Contatos | Mantém contatos telefônicos, de e-mail e WhatsApp. | PRO-CUM-002 |
| CAP-CUM-006 | Unidades administrativas | Mantém a hierarquia de órgãos e setores do município. | PRO-CUM-003 |
| CAP-CUM-007 | Consulta e qualidade cadastral | Oferece busca por identificador e indicadores de qualidade. | PRO-CUM-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-CUM-001 | Registrar pessoa | Registra a pessoa e sua extensão. | RN-CUM-001 a 003 |
| PRO-CUM-002 | Complementar cadastro | Endereço, documento e contato. | RN-CUM-004 a 006 |
| PRO-CUM-003 | Manter unidade administrativa | Hierarquia de órgãos e setores. | RN-CUM-008, 009 |
| PRO-CUM-004 | Consultar cadastro | Consulta por identificador. | — |
| PRO-CUM-005 | Excluir logicamente | Exclusão em cascata com histórico. | RN-CUM-007 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Cadastro-Unico-Municipal-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
