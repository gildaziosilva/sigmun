# 001 – Mapa-de-Atores – Cadastro Único Municipal

#### Mapa-de-Atores – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-001

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

Este artefato detalha **o mapa de atores** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-CUM-001 | Operador de Cadastro | Interno | Servidor público | Cadastra e mantém pessoas, endereços, documentos e contatos. |
| AT-CUM-002 | Gestor de Unidade | Interno | Gestor municipal | Mantém o cadastro das unidades administrativas sob sua responsabilidade. |
| AT-CUM-003 | Titular do Cadastro | Externo | Cidadão ou pessoa jurídica | Fornece e corrige seus próprios dados em atendimento. |
| AT-CUM-004 | Administrador do SIGMUN | Interno | Administrador de plataforma | Administra parâmetros de auditoria e operação do cadastro. |
| AT-CUM-005 | DOM-IDN | Serviço | Identidade e Acesso | Autentica o operador e resolve a identidade digital da pessoa. |
| AT-CUM-006 | Domínios consumidores | Externo | Domínios do SIGMUN | Consomem o cadastro como fonte oficial de pessoa e unidade. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-CUM-001 | CAP-CUM-001, CAP-CUM-002, CAP-CUM-003, CAP-CUM-004, CAP-CUM-005, CAP-CUM-006, CAP-CUM-007 |
| AT-CUM-002 |  |
| AT-CUM-003 |  |
| AT-CUM-004 |  |
| AT-CUM-005 |  |
| AT-CUM-006 |  |

---

# 4. Lacunas a validar

* Autenticação: resolvido no ADR-0007 (JWT do DOM-IDN obrigatório nas escritas).
* Revisão periódica: definida no ADR-0007 (12 meses, tarefa mensal, indicador).
* Compartilhamento: contrato formal definido no ADR-0007 (fonte oficial, id opaco).

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Cadastro-Unico-Municipal-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
