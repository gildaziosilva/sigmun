# 014 – Modelo-de-Integracao – Gestão de Diárias, Viagens e Deslocamentos

#### Modelo-de-Integracao – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-014

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

Este artefato detalha **o modelo de integração** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Princípios

* Sem chave estrangeira entre schemas de domínios.
* Comunicação por contrato (API ou evento).
* Contrato publicado em `/api/v1/dia`.

---

# 3. Integrações

| Domínio | Nome | Sentido | Finalidade |
| --- | --- | --- | --- |
| DOM-PES | Gestão de Pessoas | Consome | Pessoa e lotação do servidor. |
| DOM-GDO | Gestão Documental | Consome | Documento da prestação de contas. |
| DOM-CON | Contabilidade Pública | Fornece | Controle do pagamento. |
| DOM-INT | Interoperabilidade | Fornece | Contrato e outbox. |
| DOM-IDN | Identidade e Acesso | Consume | Autenticação do operador. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 014-Gestao-de-Diarias-Viagens-e-Deslocamentos-Modelo-de-Integracao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
