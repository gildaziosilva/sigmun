# 004 – Mapa-de-Servicos – Segurança da Informação

#### Mapa-de-Servicos – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-004

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

Este artefato detalha **o mapa de serviços** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/seg`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/seg/chaves` | chaves | Lista chaves criptográficas |
| POST | `/api/v1/seg/chaves` | chaves | Registra uma chave criptográfica |
| DELETE | `/api/v1/seg/chaves/{chave_id}` | chaves | Remove (exclusão lógica) uma chave criptográfica |
| GET | `/api/v1/seg/chaves/{chave_id}` | chaves | Busca uma chave criptográfica por ID |
| POST | `/api/v1/seg/chaves/{chave_id}/expirar` | chaves | Marca uma chave criptográfica como expirada |
| POST | `/api/v1/seg/chaves/{chave_id}/revogar` | chaves | Revoga uma chave criptográfica |
| GET | `/api/v1/seg/controles` | controles | Lista controles de segurança |
| POST | `/api/v1/seg/controles` | controles | Registra um controle de segurança |
| DELETE | `/api/v1/seg/controles/{controle_id}` | controles | Remove (exclusão lógica) um controle de segurança |
| GET | `/api/v1/seg/controles/{controle_id}` | controles | Busca um controle de segurança por ID |
| PUT | `/api/v1/seg/controles/{controle_id}` | controles | Atualiza um controle de segurança |
| POST | `/api/v1/seg/controles/{controle_id}/implementar` | controles | Marca um controle como implementado |
| POST | `/api/v1/seg/controles/{controle_id}/parcial` | controles | Marca um controle como parcialmente implementado |
| GET | `/api/v1/seg/credenciais` | credenciais | Lista credenciais |
| POST | `/api/v1/seg/credenciais` | credenciais | Registra uma credencial de acesso |
| GET | `/api/v1/seg/credenciais/{credencial_id}` | credenciais | Busca uma credencial por ID |
| POST | `/api/v1/seg/credenciais/{credencial_id}/revogar` | credenciais | Revoga uma credencial |
| POST | `/api/v1/seg/credenciais/{credencial_id}/suspender` | credenciais | Suspende uma credencial |
| GET | `/api/v1/seg/incidentes` | incidentes | Lista incidentes de segurança |
| POST | `/api/v1/seg/incidentes` | incidentes | Registra um incidente de segurança |
| DELETE | `/api/v1/seg/incidentes/{incidente_id}` | incidentes | Remove (exclusão lógica) um incidente |
| GET | `/api/v1/seg/incidentes/{incidente_id}` | incidentes | Busca um incidente de segurança por ID |
| POST | `/api/v1/seg/incidentes/{incidente_id}/encerrar` | incidentes | Encerra um incidente resolvido |
| POST | `/api/v1/seg/incidentes/{incidente_id}/escalar` | incidentes | Escala um incidente para um responsável |
| POST | `/api/v1/seg/incidentes/{incidente_id}/mitigar` | incidentes | Inicia mitigação de um incidente |
| POST | `/api/v1/seg/incidentes/{incidente_id}/resolver` | incidentes | Resolve um incidente |
| GET | `/api/v1/seg/politicas` | politicas | Lista políticas de segurança |
| POST | `/api/v1/seg/politicas` | politicas | Registra uma política de segurança |
| DELETE | `/api/v1/seg/politicas/{politica_id}` | politicas | Remove (exclusão lógica) uma política de segurança |
| GET | `/api/v1/seg/politicas/{politica_id}` | politicas | Busca uma política de segurança por ID |
| PUT | `/api/v1/seg/politicas/{politica_id}` | politicas | Atualiza uma política de segurança |
| POST | `/api/v1/seg/politicas/{politica_id}/aprovar` | politicas | Aprova uma política de segurança |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| chaves | 6 |
| controles | 7 |
| credenciais | 5 |
| incidentes | 8 |
| politicas | 6 |

---

# 4. Lacunas a validar

* Definir a rotação periódica das chaves criptográficas.
* Definir o prazo de retenção dos incidentes encerrados.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Seguranca-da-Informacao-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
