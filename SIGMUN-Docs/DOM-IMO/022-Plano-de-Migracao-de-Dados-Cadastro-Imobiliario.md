# 022 – Plano de Migração de Dados – Cadastro Imobiliário

#### Plano de Migração de Dados – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-022

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato define a migração dos dados existentes para o modelo do domínio de
Cadastro Imobiliário.

---

# 2. Fontes de Dados

| Fonte | Natureza | Abrangência |
| --- | --- | --- |
| Cadastro municipal anterior | Planilhas e sistema legado | Todo o acervo municipal |
| Base cartográfica | Arquivos georreferenciados | Uma revisão por exercício |
| Matrículas registrais | Dados de titularidade e área | Lotes com registro |

---

# 3. Estratégia

1. **Extração:** leitura das fontes, sem alteração na origem.
2. **Transformação:** normalização de códigos, tipos e formatos de data.
3. **Deduplicação:** confronto pela chave natural de cada agregado.
4. **Carga:** gravação em lote, respeitando a ordem das dependências.
5. **Validação:** confronto de contagens e valores entre origem e destino.

---

# 4. Ordem de Carga

| Etapa | Dependência |
| --- | --- |
| 1. Divisões territoriais | — |
| 2. Logradouros | Divisões territoriais |
| 3. Planta de valores | Divisões territoriais |
| 4. Lotes | Logradouros e divisões |
| 5. Titularidade e geometria | Lotes |
| 6. Avaliações | Lotes e planta de valores |

---

# 5. Regras de Deduplicação

| Agregado | Chave natural | Regra |
| --- | --- | --- |
| Divisão territorial | Código cadastral | RN-TEL-001 |
| Logradouro | Código cadastral | RN-TEL-002 |
| Planta de valores | Ano + divisão + ocupação | RN-TEL-003 |
| Lote | Inscrição imobiliária | RN-IMO-001 |

---

# 6. Validação

* Contagem de registros por agregado.
* Soma das áreas do terreno e da construção.
* Correspondência entre o valor venal apurado e o valor da planta aplicada.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 022-Plano-de-Migracao-de-Dados-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
