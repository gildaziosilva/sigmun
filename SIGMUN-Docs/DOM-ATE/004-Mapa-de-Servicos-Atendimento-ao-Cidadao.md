# 004 – Mapa-de-Servicos – Atendimento ao Cidadão

#### Mapa-de-Servicos – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-004

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

Este artefato detalha **o mapa de serviços** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/ate`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/ate/atendimentos` | atendimentos | Listar Atendimentos Em Andamento |
| POST | `/api/v1/ate/atendimentos/iniciar` | atendimentos | Iniciar Atendimento |
| GET | `/api/v1/ate/atendimentos/{atendimento_id}` | atendimentos | Buscar Atendimento |
| POST | `/api/v1/ate/atendimentos/{atendimento_id}/cancelar` | atendimentos | Cancelar Atendimento |
| POST | `/api/v1/ate/atendimentos/{atendimento_id}/concluir` | atendimentos | Concluir Atendimento |
| GET | `/api/v1/ate/atendimentos/{atendimento_id}/encaminhamentos` | atendimentos | Listar Encaminhamentos Por Atendimento |
| POST | `/api/v1/ate/avaliacoes` | avaliacoes | Registrar Avaliacao |
| GET | `/api/v1/ate/avaliacoes/{avaliacao_id}` | avaliacoes | Buscar Avaliacao |
| POST | `/api/v1/ate/encaminhamentos` | encaminhamentos | Criar Encaminhamento |
| GET | `/api/v1/ate/encaminhamentos/{encaminhamento_id}` | encaminhamentos | Buscar Encaminhamento |
| POST | `/api/v1/ate/encaminhamentos/{encaminhamento_id}/concluir` | encaminhamentos | Concluir Encaminhamento |
| POST | `/api/v1/ate/filas` | filas | Abrir Fila |
| POST | `/api/v1/ate/filas/{fila_id}/fechar` | filas | Fechar Fila |
| GET | `/api/v1/ate/health` | health | Health Check |
| POST | `/api/v1/ate/senhas` | senhas | Emitir Senha |
| POST | `/api/v1/ate/senhas/{senha_id}/atender` | senhas | Marcar Senha Atendida |
| POST | `/api/v1/ate/senhas/{senha_id}/chamar` | senhas | Chamar Senha |
| POST | `/api/v1/ate/senhas/{senha_id}/rechamar` | senhas | Rechamar Senha |
| POST | `/api/v1/ate/triagens` | triagens | Realizar Triagem |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| atendimentos | 6 |
| avaliacoes | 2 |
| encaminhamentos | 3 |
| filas | 2 |
| health | 1 |
| senhas | 4 |
| triagens | 1 |

---

# 4. Lacunas a validar

* Definir o contrato de integração com a agenda municipal.
* Validar o modelo proposto com a área de atendimento antes do início da implementação.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Atendimento-ao-Cidadao-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
