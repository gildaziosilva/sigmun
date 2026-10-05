# 008 – Requisitos-Funcionais – Gestão de Pessoas

#### Requisitos-Funcionais – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-008

**Domínio:** Gestão de Pessoas

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Pessoas.md`
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

Este artefato detalha **os requisitos funcionais** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Requisitos

| ID | Requisito | Prioridade | Recurso | Capacidade |
| --- | --- | --- | --- | --- |
| RF-PES-001 | POST /api/v1/pes/cargos | Alta | cargos | CAP-PES-001 |
| RF-PES-002 | POST /api/v1/pes/ferias | Alta | ferias | CAP-PES-001 |
| RF-PES-003 | POST /api/v1/pes/ferias/{ferias_id}/aprovar | Alta | ferias | CAP-PES-001 |
| RF-PES-004 | POST /api/v1/pes/ferias/{ferias_id}/concluir | Alta | ferias | CAP-PES-001 |
| RF-PES-005 | POST /api/v1/pes/ferias/{ferias_id}/iniciar-gozo | Alta | ferias | CAP-PES-001 |
| RF-PES-006 | POST /api/v1/pes/folhas | Alta | folhas | CAP-PES-001 |
| RF-PES-007 | POST /api/v1/pes/folhas/{folha_id}/consolidar | Alta | folhas | CAP-PES-001 |
| RF-PES-008 | POST /api/v1/pes/folhas/{folha_id}/fechar | Alta | folhas | CAP-PES-001 |
| RF-PES-009 | POST /api/v1/pes/folhas/{folha_id}/homologar | Alta | folhas | CAP-PES-001 |
| RF-PES-010 | POST /api/v1/pes/folhas/{folha_id}/pagar | Alta | folhas | CAP-PES-001 |
| RF-PES-011 | POST /api/v1/pes/folhas/{folha_id}/reabrir | Alta | folhas | CAP-PES-001 |
| RF-PES-012 | POST /api/v1/pes/frequencias | Alta | frequencias | CAP-PES-001 |
| RF-PES-013 | POST /api/v1/pes/frequencias/{frequencia_id}/justificar | Alta | frequencias | CAP-PES-001 |
| RF-PES-014 | POST /api/v1/pes/lotacoes | Alta | lotacoes | CAP-PES-001 |
| RF-PES-015 | POST /api/v1/pes/lotacoes/{lotacao_id}/encerrar | Alta | lotacoes | CAP-PES-001 |
| RF-PES-016 | POST /api/v1/pes/servidores | Alta | servidores | CAP-PES-001 |
| RF-PES-017 | POST /api/v1/pes/servidores/{servidor_id}/afastar | Alta | servidores | CAP-PES-001 |
| RF-PES-018 | POST /api/v1/pes/servidores/{servidor_id}/desligar | Alta | servidores | CAP-PES-001 |
| RF-PES-019 | POST /api/v1/pes/servidores/{servidor_id}/reativar | Alta | servidores | CAP-PES-001 |

---

# 3. Cobertura

Operações publicadas: **19**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 008-Gestao-de-Pessoas-Requisitos-Funcionais.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
