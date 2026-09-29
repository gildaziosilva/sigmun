# 010 – Especificações – Cadastro Imobiliário

#### Especificações – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-010

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

Este artefato detalha as especificações de interface do domínio de
Cadastro Imobiliário: contrato REST, esquema de persistência e convenções de
identificação.

---

# 2. Contrato de Interface

* **Base:** `/api/v1/imo`
* **Formato:** JSON sobre HTTP
* **Autenticação:** **não aplicada** — as rotas deste domínio não exigem token;
  a lacuna está registrada no artefato 016 (verifique antes de expor em produção)
* **Erros de negócio:** `409 Conflict` com mensagem descritiva
* **Recurso inexistente:** `404 Not Found`
* **Validação de entrada:** `422 Unprocessable Entity`
* **Listagem:** `page` (a partir de 1) e `page_size` (1 a 100)

---

# 3. Operações

| Método | Caminho | Finalidade |
| --- | | --- | |
| GET | /api/v1/imo/avaliacoes | Listar ou consultar avaliacoes |
| POST | /api/v1/imo/avaliacoes | Registrar ação sobre avaliacoes |
| GET | /api/v1/imo/avaliacoes/imovel/{imovel_id} | Consultar avaliacoes por identificador |
| GET | /api/v1/imo/avaliacoes/{avaliacao_id} | Consultar avaliacoes por identificador |
| POST | /api/v1/imo/avaliacoes/{avaliacao_id}/concluir | Registrar ação sobre avaliacoes |
| POST | /api/v1/imo/avaliacoes/{avaliacao_id}/cancelar | Registrar ação sobre avaliacoes |
| GET | /api/v1/imo/caracteristicas | Listar ou consultar caracteristicas |
| POST | /api/v1/imo/caracteristicas | Registrar ação sobre caracteristicas |
| GET | /api/v1/imo/caracteristicas/imovel/{imovel_id} | Consultar caracteristicas por identificador |
| GET | /api/v1/imo/geometrias | Listar ou consultar geometrias |
| POST | /api/v1/imo/geometrias | Registrar ação sobre geometrias |
| GET | /api/v1/imo/geometrias/imovel/{imovel_id} | Consultar geometrias por identificador |
| GET | /api/v1/imo/imoveis | Listar ou consultar imoveis |
| POST | /api/v1/imo/imoveis | Registrar ação sobre imoveis |
| GET | /api/v1/imo/imoveis/inscricao/{inscricao} | Consultar imoveis por identificador |
| GET | /api/v1/imo/imoveis/logradouro/{logradouro_id} | Consultar imoveis por identificador |
| GET | /api/v1/imo/imoveis/bairro/{bairro_id} | Consultar imoveis por identificador |
| DELETE | /api/v1/imo/imoveis/{imovel_id} | Excluir imoveis (exclusão lógica) |
| GET | /api/v1/imo/imoveis/{imovel_id} | Consultar imoveis por identificador |
| PATCH | /api/v1/imo/imoveis/{imovel_id} | Atualizar imoveis |
| POST | /api/v1/imo/imoveis/{imovel_id}/situacao | Registrar ação sobre imoveis |
| GET | /api/v1/imo/imoveis/{imovel_id}/proprietarios | Consultar imoveis por identificador |
| GET | /api/v1/imo/proprietarios | Listar ou consultar proprietarios |
| POST | /api/v1/imo/proprietarios | Registrar ação sobre proprietarios |
| DELETE | /api/v1/imo/proprietarios/{vinculo_id} | Excluir proprietarios (exclusão lógica) |


---

# 4. Modelo de Persistência

| Schema | Tabela | Colunas | Chave natural / restrição |
| --- | | --- | | --- | |
| `imo` | `imoveis` | 16 | inscricao_imobiliaria |
| `imo` | `proprietarios_imoveis` | 11 | — |
| `imo` | `avaliacoes_imoveis` | 14 | — |
| `imo` | `caracteristicas_imoveis` | 9 | — |
| `imo` | `geometrias_imoveis` | 13 | — |


---

# 5. Convenções de Identificação

* **Identificador interno:** UUID v4, gerado pela aplicação.
* **Chave natural:** código cadastral, textual e estável.
* **Exclusão:** lógica, por meio do campo `is_deleted`, preservando o histórico
  fiscal e fundiário.

---

# 6. Regras Aplicadas na Interface

| Regra | Efeito observável na API |
| --- | |
| RN-IMO-001 | A inscrição imobiliária é única no município e obrigatória; a alteração posterior mantém o mesmo identificador. |
| RN-IMO-002 | O imóvel exige logradouro e divisão territorial vinculados; o bairro é resolvido a partir do logradouro. |
| RN-IMO-003 | As áreas do terreno e da construção não podem ser negativas e o ano de construção deve ser coerente. |
| RN-IMO-004 | As transições são `ATIVO -> INATIVO | EM_OBRA | DESOCUPADO | DEMOLIDO`, `INATIVO -> ATIVO`, `EM_OBRA -> ATIVO | DEMOLIDO` e `DESOCUPADO -> ATIVO | INATIVO`; `DEMOLIDO` é terminal. |
| RN-IMO-005 | `valor_terreno = área_terreno_m2 × Vt`, `valor_construção = área_construida_m2 × Vc`, `valor_venal = valor_terreno + valor_construcao` e `valor_lançamento = valor_venal × alíquota / 100`; um exercício já concluído não pode ser reavaliado. |
| RN-IMO-006 | Cada imóvel admite no máximo um proprietário titular principal, a mesma pessoa não é vinculada duas vezes ao mesmo imóvel e o documento é CPF (11 dígitos) ou CNPJ (14 dígitos). |
| RN-IMO-007 | A geometria exige datum suportado, coordenadas no intervalo admissível e vértices compatíveis com o tipo de geometria; cada lote admite uma geometria vigente. |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 010-Especificacoes-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
