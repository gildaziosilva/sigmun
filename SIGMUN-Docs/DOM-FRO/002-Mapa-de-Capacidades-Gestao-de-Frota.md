# 002 – Mapa-de-Capacidades – Gestão de Frota

#### Mapa-de-Capacidades – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-002

**Domínio:** Gestão de Frota

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Frota.md`
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

Este artefato detalha **o mapa de capacidades** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-FRO-001 | Cadastro de veículos | Registra veículo, tipo, combustível e situação. | PRO-FRO-001 |
| CAP-FRO-002 | Abastecimento | Registra abastecimento e quilometragem. | PRO-FRO-002 |
| CAP-FRO-003 | Manutenção | Abre e conclui manutenção do veículo. | PRO-FRO-003 |
| CAP-FRO-004 | Rotas | Registra e conclui rota de deslocamento. | PRO-FRO-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-FRO-001 | Cadastrar veículo | Registra veículo e seu responsável. | RN-FRO-001 |
| PRO-FRO-002 | Abastecer | Registra abastecimento com litros e quilometragem. | RN-FRO-002 |
| PRO-FRO-003 | Manter veículo | Abre e conclui manutenção. | — |
| PRO-FRO-004 | Usar em rota | Registra e conclui rota. | — |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Gestao-de-Frota-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
