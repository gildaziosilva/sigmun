# 009 – Requisitos-Nao-Funcionais – Cadastro Único Municipal

#### Requisitos-Nao-Funcionais – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-009

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

Este artefato detalha **os requisitos não funcionais** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Categoria | Requisito |
| --- | --- | --- |
| RNF-CUM-001 | Desempenho | p95 até 300 ms na consulta por identificador. |
| RNF-CUM-002 | Integridade referencial | Chave primária UUID v4 gerada pela aplicação. |
| RNF-CUM-003 | Exclusão lógica | Exclusão física vedada; há deleted_at e deleted_by. |
| RNF-CUM-004 | Auditoria | created_at, created_by, updated_at e updated_by. |
| RNF-CUM-005 | Privacidade | Documento e contato são dado pessoal (LGPD). |
| RNF-CUM-006 | Autenticação | Acesso autenticado; X-Usuario-Id provisório até o IDN. |
| RNF-CUM-007 | Transacionalidade | Pessoa e extensão na mesma unidade de trabalho. |
| RNF-CUM-008 | Idempotência | Documento único entre pessoas não excluídas. |
| RNF-CUM-009 | Rastreabilidade | Toda alteração referencia a regra aplicada. |
| RNF-CUM-010 | Compatibilidade | Sem chave estrangeira entre schemas. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 009-Cadastro-Unico-Municipal-Requisitos-Nao-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
