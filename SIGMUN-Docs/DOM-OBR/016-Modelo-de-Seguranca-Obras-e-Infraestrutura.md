# 016 – Modelo de Segurança – Obras e Infraestrutura

#### Modelo de Segurança – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-016

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
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

Este artefato define os controles de segurança aplicáveis ao domínio de
Obras e Infraestrutura.

---

# 2. Autenticação e Autorização

> **Estado verificado em 2026-09-29:** a varredura de
> `src/modules/sigmun_obras` não encontrou dependência de autenticação ou
> autorização nas rotas deste domínio. A tabela abaixo descreve o **controle
> previsto** e o **estado real** de cada mecanismo; os itens marcados como
> pendentes são lacunas conhecidas, não garantias.

| Aspecto | Controle previsto | Situação verificada |
| --- | --- | --- |
| Autenticação | Token JWT emitido pelo DOM-IDN (`POST /api/v1/idn/auth/login`) | **Não aplicada** — as rotas não declaram dependência de autenticação |
| Autorização | Perfis `admin` e `servidor` | **Não aplicada** — não há verificação de papel nas rotas |
| Autorização de Destino (BOLA) | Conferência de propriedade do objeto | **Pendente** — o objeto é resolvido por identificador sem conferência de propriedade |
| Credenciais de usuário | Transmitem o valor em `created_by` | **Parcial** — o campo existe e é persistido, mas não deriva de sessão autenticada |
| Sessão | Expiração conforme `JWT_EXPIRATION_HOURS` | Não aplicável a este domínio |

---

# 3. Dados Sensíveis

* **Georreferência e geometria de lotes:** dado cadastral fundiário, sujeito à
  Lei nº 9.279/1996 (sigilo de informações cadastrais).
* **Titularidade:** dados pessoais de titulares protegidos pela LGPD
  (Lei nº 13.709/2018).
* **Valores da planta de valores:** informação econômica de uso tributário,
  não sigilosa, mas de acesso restrito aos agentes fiscais.

---

# 4. Controles Aplicados

| Controle | Implementação |
| --- | --- |
| Autenticação obrigatória | Token JWT nas operações do prefixo |
| Rastreabilidade de autoria | Campos `created_by` e `updated_at` |
| Exclusão lógica | Campo `is_deleted` preserva o histórico |
| Validação de entrada | Schemas Pydantic com faixas e padrões |
| Mensagens auditáveis | Mensagens de erro referenciam a regra violada |

---

# 5. Regras de Acesso por Papel

| Papel | Permissões esperadas |
| --- | --- |
| Administrador | Todas as operações, incluindo exclusões |
| Servidor | Consulta e atualização; exclusão conforme delegação |

---

# 6. Regras de Negócio com Reflexo na Segurança

| Regra | Garantia |
| --- | |
| RN-OBR-001 | Restrição UNIQUE em `obr.obras.numero` e validação em `Obra.validar()`. |
| RN-OBR-002 | Transições em `Obra.iniciar_execucao()`, `.suspender()`, `.concluir()` e `.cancelar()`. |
| RN-OBR-003 | Validações em `Obra.iniciar_execucao()`. |
| RN-OBR-004 | Checks `ck_obr_obra_valores`, `ck_obr_obra_avanco` e `ck_obr_obra_pago`, e validação em `Obra.validar()`. |
| RN-OBR-005 | Transições em `MedicaoObra.conferir()`, `.aprovar()`, `.glosar()` e `.cancelar()`; índice único parcial `uq_obr_medicao_numero`; check `ck_obr_medicao_percentual`. |
| RN-OBR-006 | Check `ck_obr_despesa_valor` e validações em `RegistrarDespesaUseCase` e `DespesaObra.validar()`. |
| RN-OBR-007 | Transições em `EtapaObra.iniciar()` e `.concluir()`, e check `ck_obr_etapa_percentual`. |
| RN-OBR-008 | Check `ck_obr_vistoria_percentual` e validação em `VistoriaObra.validar()`. |


---

# 7. Pendências

* A autorização fina por operação é avaliada no cliente; a imposição
  server-side permanece evolução planejada no ROADMAP.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 016-Modelo-de-Seguranca-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
