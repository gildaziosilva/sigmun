# 005 – Casos-de-Uso – Ouvidoria

#### Casos-de-Uso – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-005

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **os casos de uso** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-OU-001 | RegistrarManifestacao | `RegistrarManifestacaoUseCase` | Registra nova manifestação genérica (RN-OUV-001, RN-OUV-002). |
| CU-OU-002 | RegistrarDenuncia | `RegistrarDenunciaUseCase` | Registra nova denúncia (RN-OUV-002, RN-OUV-030). |
| CU-OU-003 | RegistrarPedidoLai | `RegistrarPedidoLaiUseCase` | Registra novo pedido de acesso à informação (RN-OUV-003, LAI Art. 11). |
| CU-OU-004 | ResponderManifestacao | `ResponderManifestacaoUseCase` | Registra resposta à manifestação/denúncia/pedido LAI. |
| CU-OU-005 | AlterarStatus | `AlterarStatusUseCase` | Altera status de manifestação/denúncia/pedido LAI (RN-OUV-010). |
| CU-OU-006 | ProrrogarPrazo | `ProrrogarPrazoUseCase` | Prorroga prazo de resposta (LAI Art. 11 §1º, RN-OUV-020). |
| CU-OU-007 | AvaliarManifestacao | `AvaliarManifestacaoUseCase` | Registra avaliação do cidadão (1-5). |
| CU-OU-008 | EncaminharDenuncia | `EncaminharDenunciaUseCase` | Encaminha denúncia a órgão externo (MP, PF, TCE). |
| CU-OU-009 | InterporRecursoLai | `InterporRecursoLaiUseCase` | Interpõe recurso de pedido LAI negado (LAI Art. 15). |
| CU-OU-010 | DecidirRecursoLai | `DecidirRecursoLaiUseCase` | Decide sobre recurso LAI interposto. |
| CU-OU-011 | ListarManifestacoes | `ListarManifestacoesUseCase` | Lista manifestações com paginação e filtros. |
| CU-OU-012 | ListarDenuncias | `ListarDenunciasUseCase` | Lista denúncias com paginação e filtros. |
| CU-OU-013 | ListarPedidosLai | `ListarPedidosLaiUseCase` | Lista pedidos LAI com paginação e filtros. |
| CU-OU-014 | ObterManifestacao | `ObterManifestacaoUseCase` | Obtém detalhes de uma manifestação/denúncia/pedido LAI por ID ou protocolo. |
| CU-OU-015 | ObterEstatisticas | `ObterEstatisticasUseCase` | Obtém estatísticas e indicadores da ouvidoria. |

---

# 3. Cobertura

Casos de uso no código: **15**. Operações publicadas: **16**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Ouvidoria-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
