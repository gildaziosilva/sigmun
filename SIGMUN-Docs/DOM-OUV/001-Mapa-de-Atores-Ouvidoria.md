# 001 – Mapa-de-Atores – Ouvidoria

#### Mapa-de-Atores – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-001

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

Este artefato detalha **o mapa de atores** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Atores do domínio

| Identificador | Ator | Classificação | Papel | Responsabilidade |
| --- | --- | --- | --- | --- |
| AT-OU-001 | Cidadão | Externo | Cidadão | Registra manifestação, denúncia ou pedido de informação. |
| AT-OU-002 | Ouvidor | Interno | Servidor público | Triagem, encaminhamento e resposta. |
| AT-OU-003 | Órgão competente | Externo | Unidade municipal | Recebe o encaminhamento e presta a informação. |
| AT-OU-004 | Controle interno | Externo | Controle | Acompanha prazo, conclusão e satisfação do cidadão. |

---

# 3. Matriz ator × capacidade

| Ator | Capacidades |
| --- | --- |
| AT-OU-001 |  |
| AT-OU-002 |  |
| AT-OU-003 |  |
| AT-OU-004 |  |

---

# 4. Lacunas a validar

* Definir o prazo legal por tipo de manifestação e por LAI.
* Definir a integração com o FalaBR / e-OUV.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 001-Ouvidoria-Mapa-de-Atores.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
