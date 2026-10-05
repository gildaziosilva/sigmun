# 005 – Casos-de-Uso – Segurança da Informação

#### Casos-de-Uso – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-005

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **os casos de uso** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-SEG-001 | CriarChave | `CriarChaveUseCase` | Cria uma nova chave criptográfica. |
| CU-SEG-002 | BuscarChave | `BuscarChaveUseCase` | Busca chaves criptográficas. |
| CU-SEG-003 | AtualizarChave | `AtualizarChaveUseCase` | Atualiza uma chave criptográfica. |
| CU-SEG-004 | RevogarChave | `RevogarChaveUseCase` | Revoga uma chave criptográfica. |
| CU-SEG-005 | ExpirarChave | `ExpirarChaveUseCase` | Marca uma chave criptográfica como expirada. |
| CU-SEG-006 | DeletarChave | `DeletarChaveUseCase` | Remove uma chave criptográfica (soft-delete). |
| CU-SEG-007 | CriarControleSeguranca | `CriarControleSegurancaUseCase` | Cria um novo controle de segurança. |
| CU-SEG-008 | BuscarControleSeguranca | `BuscarControleSegurancaUseCase` | Busca controles de segurança. |
| CU-SEG-009 | AtualizarControleSeguranca | `AtualizarControleSegurancaUseCase` | Atualiza um controle de segurança. |
| CU-SEG-010 | ImplementarControleSeguranca | `ImplementarControleSegurancaUseCase` | Marca um controle como implementado. |
| CU-SEG-011 | ParcialmenteImplementado | `ParcialmenteImplementadoUseCase` | Marca um controle como parcialmente implementado. |
| CU-SEG-012 | DeletarControleSeguranca | `DeletarControleSegurancaUseCase` | Remove um controle de seguranção (soft-delete). |
| CU-SEG-013 | CriarCredencial | `CriarCredencialUseCase` | Cria uma nova credencial de acesso. |
| CU-SEG-014 | BuscarCredencial | `BuscarCredencialUseCase` | Busca credenciais. |
| CU-SEG-015 | SuspenderCredencial | `SuspenderCredencialUseCase` | Suspende uma credencial. |
| CU-SEG-016 | RevogarCredencial | `RevogarCredencialUseCase` | Revoga uma credencial. |
| CU-SEG-017 | RegistrarFalhaCredencial | `RegistrarFalhaCredencialUseCase` | Registra uma tentativa de uso falha. |
| CU-SEG-018 | RegistrarUsoCredencial | `RegistrarUsoCredencialUseCase` | Registra uso bem-sucedido de uma credencial. |
| CU-SEG-019 | DeletarCredencial | `DeletarCredencialUseCase` | Remove uma credencial (soft-delete). |
| CU-SEG-020 | RegistrarIncidenteSeguranca | `RegistrarIncidenteSegurancaUseCase` | Registra um novo incidente de segurança. |
| CU-SEG-021 | BuscarIncidenteSeguranca | `BuscarIncidenteSegurancaUseCase` | Busca incidentes de segurança. |
| CU-SEG-022 | EscalarIncidenteSeguranca | `EscalarIncidenteSegurancaUseCase` | Escala um incidente para um responsável. |
| CU-SEG-023 | MitigarIncidenteSeguranca | `MitigarIncidenteSegurancaUseCase` | Inicia mitigação de um incidente. |
| CU-SEG-024 | ResolverIncidenteSeguranca | `ResolverIncidenteSegurancaUseCase` | Resolve um incidente. |
| CU-SEG-025 | EncerrarIncidenteSeguranca | `EncerrarIncidenteSegurancaUseCase` | Encerra um incidente resolvido. |
| CU-SEG-026 | DeletarIncidenteSeguranca | `DeletarIncidenteSegurancaUseCase` | Remove um incidente (soft-delete). |
| CU-SEG-027 | CriarPoliticaSeguranca | `CriarPoliticaSegurancaUseCase` | Cria uma nova política de segurança. |
| CU-SEG-028 | BuscarPoliticaSeguranca | `BuscarPoliticaSegurancaUseCase` | Busca políticas de segurança. |
| CU-SEG-029 | AtualizarPoliticaSeguranca | `AtualizarPoliticaSegurancaUseCase` | Atualiza uma política de segurança. |
| CU-SEG-030 | AprovarPoliticaSeguranca | `AprovarPoliticaSegurancaUseCase` | Aprova uma política de segurança. |
| CU-SEG-031 | DeletarPoliticaSeguranca | `DeletarPoliticaSegurancaUseCase` | Remove uma política de segurança (soft-delete). |

---

# 3. Cobertura

Casos de uso no código: **31**. Operações publicadas: **32**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Seguranca-da-Informacao-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
