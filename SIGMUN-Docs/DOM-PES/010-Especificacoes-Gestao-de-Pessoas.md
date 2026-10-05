# 010 – Especificacoes – Gestão de Pessoas

#### Especificacoes – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-010

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

Este artefato detalha **as especificações** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| POST | `/api/v1/pes/cargos` | cargos | JSON (payload do domínio) |
| POST | `/api/v1/pes/ferias` | ferias | JSON (payload do domínio) |
| POST | `/api/v1/pes/ferias/{ferias_id}/aprovar` | ferias | JSON (payload do domínio) |
| POST | `/api/v1/pes/ferias/{ferias_id}/concluir` | ferias | JSON (payload do domínio) |
| POST | `/api/v1/pes/ferias/{ferias_id}/iniciar-gozo` | ferias | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas/{folha_id}/consolidar` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas/{folha_id}/fechar` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas/{folha_id}/homologar` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas/{folha_id}/pagar` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/folhas/{folha_id}/reabrir` | folhas | JSON (payload do domínio) |
| POST | `/api/v1/pes/frequencias` | frequencias | JSON (payload do domínio) |
| POST | `/api/v1/pes/frequencias/{frequencia_id}/justificar` | frequencias | JSON (payload do domínio) |
| POST | `/api/v1/pes/lotacoes` | lotacoes | JSON (payload do domínio) |
| POST | `/api/v1/pes/lotacoes/{lotacao_id}/encerrar` | lotacoes | JSON (payload do domínio) |
| POST | `/api/v1/pes/servidores` | servidores | JSON (payload do domínio) |
| POST | `/api/v1/pes/servidores/{servidor_id}/afastar` | servidores | JSON (payload do domínio) |
| POST | `/api/v1/pes/servidores/{servidor_id}/desligar` | servidores | JSON (payload do domínio) |
| POST | `/api/v1/pes/servidores/{servidor_id}/reativar` | servidores | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-PES-001 | código do cargo é único no município |
| RN-PES-002 | salário-base deve ser maior que zero |
| RN-PES-010 | matrícula funcional é única no município |
| RN-PES-011 | CPF é único e validado (11 dígitos) |
| RN-PES-012 | servidor precisa de cargo válido para admissão |
| RN-PES-013 | admissão exige data de admissão; demissão exige data |
| RN-PES-020 | servidor só pode ter uma lotação vigente por período |
| RN-PES-021 | lotação exige unidade de destino e data de início |
| RN-PES-022 | remoção encerra a lotação vigente (data_fim = data da remoção) |
| RN-PES-030 | competência (ano/mês) é única no município |
| RN-PES-031 | folha ABERTA pode receber lançamentos; FECHADA não |
| RN-PES-032 | fechamento exige ao menos um lançamento |
| RN-PES-033 | folha HOMOLOGADA ou PAGA é terminal (imutável) |
| RN-PES-040 | período de gozo deve estar dentro do período aquisitivo + 12 meses |
| RN-PES-041 | mínimo de 10 dias por parcela; máximo de 3 parcelas |
| RN-PES-042 | máquina de estados PLANEJADA → APROVADA → EM_GOZO → CONCLUIDA |
| RN-PES-050 | um registro por servidor/dia (unicidade servidor + data) |
| RN-PES-051 | atraso superior a 60 minutos conta como meio período |
| RN-PES-052 | falta injustificada gera desconto em folha (integração DOM-PES→folha) |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Gestao-de-Pessoas-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
