# 022 – Plano-de-Migracao-de-Dados – Atendimento ao Cidadão

#### Plano-de-Migracao-de-Dados – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-022

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **o plano de migração de dados** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas

| Tabela | Colunas | Classe ORM |
| --- | --- | --- |
| atendimentos | 13 | `AtendimentoModel` |
| avaliacoes_atendimento | 11 | `AvaliacaoAtendimentoModel` |
| canais_atendimento | 11 | `CanalAtendimentoModel` |
| chamadas | 15 | `ChamadaModel` |
| encaminhamentos | 12 | `EncaminhamentoModel` |
| eventos_outbox | 11 | `EventoOutboxModel` |
| filas_atendimento | 11 | `FilaAtendimentoModel` |
| guiches | 11 | `GuicheModel` |
| senhas | 14 | `SenhaModel` |
| servicos_atendimento | 11 | `ServicoAtendimentoModel` |
| triagens | 12 | `TriagemModel` |
| unidades_atendimento | 11 | `UnidadeAtendimentoModel` |

---

# 3. Estratégia

Carga inicial por migração Alembic; sem conversão de legado.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 022-Atendimento-ao-Cidadao-Plano-de-Migracao-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
