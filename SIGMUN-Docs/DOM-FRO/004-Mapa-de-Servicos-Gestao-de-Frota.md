# 004 – Mapa-de-Servicos – Gestão de Frota

#### Mapa-de-Servicos – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-004

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

Este artefato detalha **o mapa de serviços** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/fro`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/fro/abastecimentos` | abastecimentos | Listar Abastecimentos |
| GET | `/api/v1/fro/manutencoes` | manutencoes | Listar Manutencoes |
| POST | `/api/v1/fro/manutencoes/{manutencao_id}/concluir` | manutencoes | Concluir Manutencao |
| GET | `/api/v1/fro/rotas` | rotas | Listar Rotas |
| POST | `/api/v1/fro/rotas/{rota_id}/concluir` | rotas | Concluir Rota |
| GET | `/api/v1/fro/veiculos` | veiculos | Listar Veiculos |
| POST | `/api/v1/fro/veiculos` | veiculos | Cadastrar Veiculo |
| GET | `/api/v1/fro/veiculos/{veiculo_id}` | veiculos | Obter Veiculo |
| GET | `/api/v1/fro/veiculos/{veiculo_id}/abastecimentos` | veiculos | Listar Abastecimentos Veiculo |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/abastecimentos` | veiculos | Registrar Abastecimento |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/baixar` | veiculos | Baixar Veiculo |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/manutencoes` | veiculos | Abrir Manutencao |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/rotas` | veiculos | Registrar Rota |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| abastecimentos | 1 |
| manutencoes | 2 |
| rotas | 2 |
| veiculos | 8 |

---

# 4. Lacunas a validar

* Definir a integração com o sistema de controle de combustível.
* Definir o plano de manutenção preventiva por quilometragem.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Gestao-de-Frota-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
