# 008 – Requisitos-Funcionais – Administração Tributária

#### Requisitos-Funcionais – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-008

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-TRI-001 | POST /api/v1/tri/certidoes | Alta | certidoes | CAP-TRI-001 |
| RF-TRI-002 | GET /api/v1/tri/certidoes/{certidao_id} | Média | certidoes | CAP-TRI-001 |
| RF-TRI-003 | GET /api/v1/tri/contribuintes | Média | contribuintes | CAP-TRI-001 |
| RF-TRI-004 | POST /api/v1/tri/contribuintes | Alta | contribuintes | CAP-TRI-001 |
| RF-TRI-005 | GET /api/v1/tri/contribuintes/{contribuinte_id} | Média | contribuintes | CAP-TRI-001 |
| RF-TRI-006 | GET /api/v1/tri/divida-ativa | Média | divida-ativa | CAP-TRI-001 |
| RF-TRI-007 | GET /api/v1/tri/divida-ativa/{inscricao_id} | Média | divida-ativa | CAP-TRI-001 |
| RF-TRI-008 | POST /api/v1/tri/divida-ativa/{inscricao_id}/baixar | Alta | divida-ativa | CAP-TRI-001 |
| RF-TRI-009 | GET /api/v1/tri/imoveis | Média | imoveis | CAP-TRI-001 |
| RF-TRI-010 | POST /api/v1/tri/imoveis | Alta | imoveis | CAP-TRI-001 |
| RF-TRI-011 | GET /api/v1/tri/imoveis/{imovel_id} | Média | imoveis | CAP-TRI-001 |
| RF-TRI-012 | GET /api/v1/tri/lancamentos | Média | lancamentos | CAP-TRI-001 |
| RF-TRI-013 | POST /api/v1/tri/lancamentos | Alta | lancamentos | CAP-TRI-001 |
| RF-TRI-014 | GET /api/v1/tri/lancamentos/{lancamento_id} | Média | lancamentos | CAP-TRI-001 |
| RF-TRI-015 | POST /api/v1/tri/lancamentos/{lancamento_id}/inscrever-divida-ativa | Alta | lancamentos | CAP-TRI-001 |
| RF-TRI-016 | POST /api/v1/tri/lancamentos/{lancamento_id}/pagar | Alta | lancamentos | CAP-TRI-001 |

---

# 3. Cobertura

Operações publicadas: **16**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Administracao-Tributaria-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
