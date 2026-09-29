# 014 – Modelo de Integração – Gestão Territorial

#### Modelo de Integração – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-014

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
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

Este artefato define os contratos de integração do domínio de Gestão Territorial com
os demais domínios e com sistemas externos.

---

# 2. Princípios de Integração

* **Sem dependência de banco entre domínios:** nenhum schema referencia outro
  diretamente por chave estrangeira.
* **Comunicação por contrato:** as trocas ocorrem por API ou evento, conforme o
  ROADMAP §2.7 e §2.8.
* **Isolamento por port:** a aplicação expõe interfaces (`Protocol`) que isolam a
  dependência e permitem implementação HTTP ou local.

---

# 3. Integração Interna

| Origem | Destino | Mecanismo | Contrato |
| --- | --- | --- | --- |
| DOM-TEL | DOM-IMO | API REST | `GET /api/v1/tel/plantas-valores/vigente` |

**Sentido:** Publica os valores vigentes consumidos pelo cadastro imobiliário.

---

# 4. Detalhamento do Contrato

| Elemento | Definição |
| --- | --- |
| Operação | `GET /api/v1/tel/plantas-valores/vigente` |
| Parâmetros | `ano`, `bairro_id`, `ocupacao` |
| Resposta | `valor_terreno_m2`, `valor_construcao_m2`, `aliquota_percent` |
| Ausência de dados | HTTP 404 quando não há planta vigente para a combinação |
| Regra aplicável | RN-TEL-003 |
| Consumidores | DOM-IMO, DOM-TRI, DOM-GEO |

No código, a dependência é isolada pelo port
`ConsultaPlantaValores` (`application/interfaces.py`), cuja implementação
inicial é resolvida pelo consumidor da API.

---

# 5. Integração Externa

| Sistema externo | Sentido | Meio |
| --- | --- | --- |
| Cartório de registro de imóveis | Entrada de dados registrais | Concessão de dados |
| Base cartográfica municipal ou do IBGE | Georreferenciamento | Intercâmbio de arquivos georreferenciados |

---

# 6. Contratos Publicados

| Prefixo | Consumidores |
| --- | |
| `/api/v1/tel` | DOM-IMO, DOM-TRI, DOM-GEO |


---

# 7. Tratamento de Falha

* Recurso remoto indisponível: a operação dependente é recusada e a transação é
  revertida, preservando a consistência local.
* Divergência de referência: o identificador é preservado e a inconsistência é
  reportada, sem alteração de dados locais.
* Referência inexistente: resposta `404`, sem efeito colateral.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 014-Modelo-de-Integracao-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
