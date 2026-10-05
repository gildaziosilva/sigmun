# 004 – Mapa-de-Servicos – Gestão de Pessoas

#### Mapa-de-Servicos – Gestão de Pessoas

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PES-004

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

Este artefato detalha **o mapa de serviços** do domínio Gestão de Pessoas (`DOM-PES`), com base na implementação material identificada em `src/modules/sigmun_rh` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/pes`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| POST | `/api/v1/pes/cargos` | cargos | Criar Cargo |
| POST | `/api/v1/pes/ferias` | ferias | Planejar Ferias |
| POST | `/api/v1/pes/ferias/{ferias_id}/aprovar` | ferias | Aprovar Ferias |
| POST | `/api/v1/pes/ferias/{ferias_id}/concluir` | ferias | Concluir Ferias |
| POST | `/api/v1/pes/ferias/{ferias_id}/iniciar-gozo` | ferias | Iniciar Gozo |
| POST | `/api/v1/pes/folhas` | folhas | Abrir Folha |
| POST | `/api/v1/pes/folhas/{folha_id}/consolidar` | folhas | Consolidar Folha |
| POST | `/api/v1/pes/folhas/{folha_id}/fechar` | folhas | Fechar Folha |
| POST | `/api/v1/pes/folhas/{folha_id}/homologar` | folhas | Homologar Folha |
| POST | `/api/v1/pes/folhas/{folha_id}/pagar` | folhas | Pagar Folha |
| POST | `/api/v1/pes/folhas/{folha_id}/reabrir` | folhas | Reabrir Folha |
| POST | `/api/v1/pes/frequencias` | frequencias | Registrar Frequencia |
| POST | `/api/v1/pes/frequencias/{frequencia_id}/justificar` | frequencias | Justificar Falta |
| POST | `/api/v1/pes/lotacoes` | lotacoes | Lotar Servidor |
| POST | `/api/v1/pes/lotacoes/{lotacao_id}/encerrar` | lotacoes | Encerrar Lotacao |
| POST | `/api/v1/pes/servidores` | servidores | Admitir Servidor |
| POST | `/api/v1/pes/servidores/{servidor_id}/afastar` | servidores | Afastar Servidor |
| POST | `/api/v1/pes/servidores/{servidor_id}/desligar` | servidores | Desligar Servidor |
| POST | `/api/v1/pes/servidores/{servidor_id}/reativar` | servidores | Reativar Servidor |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| cargos | 1 |
| ferias | 4 |
| folhas | 6 |
| frequencias | 2 |
| lotacoes | 2 |
| servidores | 4 |

---

# 4. Lacunas a validar

* Definir a integração do SIGRH ou sistema estadual de folha.
* Definir o calendário de férias por mês de gozo.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Gestao-de-Pessoas-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
