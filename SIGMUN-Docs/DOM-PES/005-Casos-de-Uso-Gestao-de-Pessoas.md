# 005 – Casos-de-Uso – Gestão de Pessoas

#### Casos-de-Uso – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-005

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

Este artefato detalha **os casos de uso** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-PES-001 | CriarCargo | `CriarCargoUseCase` | Cria um cargo (RN-PES-001/002). |
| CU-PES-002 | AdmitirServidor | `AdmitirServidorUseCase` | Admite um servidor (RN-PES-010/011/012/013). |
| CU-PES-003 | AfastarServidor | `AfastarServidorUseCase` | Registra afastamento de servidor ativo. |
| CU-PES-004 | ReativarServidor | `ReativarServidorUseCase` | Reativa servidor afastado. |
| CU-PES-005 | DesligarServidor | `DesligarServidorUseCase` | Desliga servidor (exoneração/demissão). |
| CU-PES-006 | PlanejarFerias | `PlanejarFeriasUseCase` | Planeja ferias (RN-PES-040/041). |
| CU-PES-007 | AprovarFerias | `AprovarFeriasUseCase` | Aprova ferias planejadas. |
| CU-PES-008 | IniciarGozoFerias | `IniciarGozoFeriasUseCase` | Inicia gozo de ferias aprovadas. |
| CU-PES-009 | ConcluirFerias | `ConcluirFeriasUseCase` | Conclui gozo de ferias. |
| CU-PES-010 | AbrirFolha | `AbrirFolhaUseCase` | Abre folha da competência (RN-PES-030). |
| CU-PES-011 | ConsolidarFolha | `ConsolidarFolhaUseCase` | Consolida totais da folha aberta (RN-PES-031). |
| CU-PES-012 | FecharFolha | `FecharFolhaUseCase` | Fecha folha (ABERTA → FECHADA). |
| CU-PES-013 | ReabrirFolha | `ReabrirFolhaUseCase` | Reabre folha fechada. |
| CU-PES-014 | HomologarFolha | `HomologarFolhaUseCase` | Homologa folha fechada. |
| CU-PES-015 | PagarFolha | `PagarFolhaUseCase` | Registra pagamento da folha homologada. |
| CU-PES-016 | RegistrarFrequencia | `RegistrarFrequenciaUseCase` | Registra frequencia diaria (RN-PES-050/051/052). |
| CU-PES-017 | JustificarFalta | `JustificarFaltaUseCase` | Justifica falta registrada. |
| CU-PES-018 | LotarServidor | `LotarServidorUseCase` | Lota servidor em unidade (RN-PES-020/021). |
| CU-PES-019 | RemoverServidor | `RemoverServidorUseCase` | Encerra lotação vigente do servidor. |

---

# 3. Cobertura

Casos de uso no código: **19**. Operações publicadas: **19**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Gestao-de-Pessoas-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
