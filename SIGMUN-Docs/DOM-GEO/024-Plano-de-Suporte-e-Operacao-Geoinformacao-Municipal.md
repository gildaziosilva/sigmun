# 024 – Plano de Suporte e Operação – Geoinformação Municipal

#### Plano de Suporte e Operação – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-024

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
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

Este artefato define a operação e o suporte do domínio de Geoinformação Municipal após
a implantação.

---

# 2. Operação Rotineira

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Monitoramento de erros de integração | Diária | Suporte técnico |
| Conferência da planta de valores vigente | A cada exercício | Comissão de valores |
| Verificação de desempenho das consultas | Contínua | Suporte técnico |
| Backup do banco | Conforme política municipal | Infraestrutura |

---

# 3. Níveis de Atendimento

| Nível | Escopo | Prazo-alvo |
| --- | --- | --- |
| 1 | Dúvida de uso, sem impacto na operação | 1 dia útil |
| 2 | Erro em operação, com contorno | 1 dia útil |
| 3 | Indisponibilidade do serviço | Imediato |

---

# 4. Diagnóstico de Incidentes

| Sintoma | Causa provável | Ação |
| --- | --- | --- |
| HTTP 409 em cadastro | Violação de regra de negócio | Ler a mensagem; ela identifica a regra violada |
| HTTP 404 em referência | Registro inexistente ou excluído | Consultar pelo código cadastral |
| Valor venal divergente | Planta de valores não aplicada ao exercício | Verificar a planta vigente no DOM-TEL |

---

# 5. Rotinas de Manutenção

* Verificação da integridade do seed e sua limpeza em ambientes não produtivos.
* Acompanhamento da cadeia de migrações, mantendo cabeça única.
* Revisão periódica das regras de acesso.

---

# 6. Escalonamento

Incidentes de severidade alta escalam à equipe de arquitetura, com registro no
Mapa Mestre de Artefatos e na documentação de decisões (ADR).

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 024-Plano-de-Suporte-e-Operacao-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
