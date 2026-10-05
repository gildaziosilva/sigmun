# 004 – Mapa-de-Servicos – Gestão de Diárias, Viagens e Deslocamentos

#### Mapa-de-Servicos – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-004

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **o mapa de serviços** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/dia`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| POST | `/api/v1/dia/diarias` | diarias | Solicita uma nova diária |
| GET | `/api/v1/dia/diarias/servidor/{servidor_id}` | diarias | Lista diárias de um servidor |
| GET | `/api/v1/dia/diarias/status/{status}` | diarias | Lista diárias por status |
| GET | `/api/v1/dia/diarias/{diaria_id}` | diarias | Busca uma diária por ID |
| POST | `/api/v1/dia/diarias/{diaria_id}/autorizar` | diarias | Autoriza uma diária (RN-DIA-004) |
| POST | `/api/v1/dia/diarias/{diaria_id}/calcular` | diarias | Calcula o valor da diária (RN-DIA-005) |
| POST | `/api/v1/dia/diarias/{diaria_id}/conceder` | diarias | Confirma concessão da diária (RN-DIA-006) |
| POST | `/api/v1/dia/diarias/{diaria_id}/iniciar-prestacao` | diarias | Inicia a prestação de contas (RN-DIA-007) |
| POST | `/api/v1/dia/diarias/{diaria_id}/pagar` | diarias | Registra pagamento da diária (RN-DIA-008) |
| POST | `/api/v1/dia/prestacoes` | prestacoes | Abre uma prestação de contas |
| GET | `/api/v1/dia/prestacoes/abertas` | prestacoes | Lista prestações abertas |
| GET | `/api/v1/dia/prestacoes/{prestacao_id}` | prestacoes | Busca uma prestação por ID |
| POST | `/api/v1/dia/prestacoes/{prestacao_id}/aprovar` | prestacoes | Aprova uma prestação de contas (RN-DIA-011) |
| POST | `/api/v1/dia/prestacoes/{prestacao_id}/glosar` | prestacoes | Glosa uma prestação de contas (RN-DIA-012) |
| POST | `/api/v1/dia/prestacoes/{prestacao_id}/restituir` | prestacoes | Restitui valor glosado de uma prestação (RN-DIA-013) |
| POST | `/api/v1/dia/viagens` | viagens | Solicita uma nova viagem oficial |
| GET | `/api/v1/dia/viagens/servidor/{servidor_id}` | viagens | Lista viagens de um servidor |
| GET | `/api/v1/dia/viagens/{viagem_id}` | viagens | Busca uma viagem por ID |
| POST | `/api/v1/dia/viagens/{viagem_id}/tramitar` | viagens | Tramita uma viagem entre unidades |
| POST | `/api/v1/dia/viagens/{viagem_id}/visitar` | viagens | Visita uma viagem (registra chegada) |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| diarias | 9 |
| prestacoes | 6 |
| viagens | 5 |

---

# 4. Lacunas a validar

* Definir tabela de valores de diária por categoria e nível.
* Formalizar o envio de folha para a contabilidade (DOM-CON).

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Gestao-de-Diarias-Viagens-e-Deslocamentos-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
