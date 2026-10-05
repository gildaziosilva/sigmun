# 026 – Modelo-de-Dominio – Gestão de Frota

#### Modelo-de-Dominio – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-026

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

Este artefato detalha **o modelo de domínio** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| abastecimentos | `AbastecimentoModel` | 11 |
| manutencoes | `ManutencaoModel` | 11 |
| rotas | `RotaModel` | 12 |
| veiculos | `VeiculoModel` | 18 |

---

# 3. Domínios de valor

### TipoManutencao

| Membro | Valor |
| --- | --- |
| PREVENTIVA | "preventiva" |
| CORRETIVA | "corretiva" |
### StatusManutencao

| Membro | Valor |
| --- | --- |
| ABERTA | "aberta" |
| EM_ANDAMENTO | "em_andamento" |
| CONCLUIDA | "concluida" |
### StatusRota

| Membro | Valor |
| --- | --- |
| PLANEJADA | "planejada" |
| EM_ANDAMENTO | "em_andamento" |
| CONCLUIDA | "concluida" |
| CANCELADA | "cancelada" |
### TipoVeiculo

| Membro | Valor |
| --- | --- |
| LEVE | "leve" |
| PESADO | "pesado" |
| MOTOCICLETA | "motocicleta" |
| ONIBUS | "onibus" |
| TRATOR | "trator" |
### Combustivel

| Membro | Valor |
| --- | --- |
| GASOLINA | "gasolina" |
| ALCOOL | "alcool" |
| FLEX | "flex" |
| DIESEL | "diesel" |
| ELEETRICO | "eletrico" |
| GAS | "gas" |
### StatusVeiculo

| Membro | Valor |
| --- | --- |
| ATIVO | "ativo" |
| MANUTENCAO | "manutencao" |
| INATIVO | "inativo" |
| BAIXADO | "baixado" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-FRO-001 | a placa do veículo é única no cadastro |
| RN-FRO-002 | veículos em manutenção têm status ``manutencao``; concluída a |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Gestao-de-Frota-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
