# 000 – Domínio de Cadastro Único Municipal

#### Domínio de Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM

**Domínio:** Cadastro Único Municipal

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000F-Registro-de-Decisoes-Arquiteturais(ADR).md
* 000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* 030-Roadmap-de-Implementacao-dos-Dominios.md
* Mapa-de-Dominios.md
* Modelo-Conceitual.md
* Modelo-Logico.md
* Modelo-Fisico.md
* Dicionario-de-dados.md

---

# 1. Finalidade

O **Domínio de Cadastro Único Municipal** (`DOM-CUM`) representa o conjunto de capacidades, processos, serviços, informações, regras e interações relacionados à área de cadastro único municipal no âmbito da Administração Pública Municipal.

Este documento define a razão de ser do domínio, seus objetivos, escopo, seus relacionamentos com outros domínios do SIGMUN e a estratégia de evolução, servindo de ponto de partida para os demais artefatos do domínio.

---

# 2. Objetivos do Domínio

São objetivos do domínio:

* estruturar e organizar as informações relacionadas;
* promover padronização dos procedimentos;
* reduzir retrabalho;
* reduzir duplicidade de informações;
* aumentar a rastreabilidade dos processos;
* centralizar informações relevantes;
* apoiar a tomada de decisão;
* disponibilizar informações para gestão;
* permitir geração de indicadores;
* preservar documentos e evidências;
* integrar informações com outros domínios do SIGMUN.

---

# 3. Visão do Domínio

O domínio **Cadastro Único Municipal** deverá permitir que as informações e processos relacionados sejam tratados de forma integrada, confiável e rastreável, apoiando a gestão municipal.

Visão conceitual:

```text
Necessidade
    ↓
Captura e registro
    ↓
Organização
    ↓
Gestão e controle
    ↓
Transparência
    ↓
Informação gerencial
```

---

# 4. Escopo

O domínio compreende, em nível corporativo:

* levantamento e organização de informações do domínio;
* apoio aos processos municipais relacionados;
* definição de entidades e dados relevantes;
* articulação com serviços e requisitos;
* geração de indicadores e relatórios;
* integração com outros domínios do SIGMUN.

O detalhamento de cada processo e requisito será realizado nos respectivos artefatos.

---

# 5. Relacionamentos do Domínio

O domínio **Cadastro Único Municipal** mantém relacionamentos com outros domínios do SIGMUN, os quais serão detalhados nos artefatos de modelo de dados e integração:

* compartilhamento de informação mestra (pessoa, unidade administrativa, fornecedor);
* consumo ou provisão de serviços;
* integração com os domínios funcionais e tecnológicos;
* uso de identidade e acesso (DOM-IDN);
* registro de auditoria e indicadores.

---

# 6. Artefatos Relacionados

A partir deste documento serão produzidos progressivamente os artefatos do domínio:

1. `001-Mapa-de-Atores-Cadastro-Unico-Municipal.md` – atores do domínio
2. `002-Mapa-de-Capacidades-Cadastro-Unico-Municipal.md` – capacidades do domínio
3. `003-Mapa-de-Processos-Cadastro-Unico-Municipal.md` – processos do domínio
4. `004-Mapa-de-Servicos-Cadastro-Unico-Municipal.md` – serviços do domínio
5. `005-Casos-de-Uso-Cadastro-Unico-Municipal.md` – casos de uso
6. `006-Historias-de-Usuario-Cadastro-Unico-Municipal.md` – histórias de usuário
7. `007-Regras-de-Negocio-Cadastro-Unico-Municipal.md` – regras de negócio
8. `008-Requisitos-Funcionais-Cadastro-Unico-Municipal.md` – requisitos funcionais
9. `009-Requisitos-Nao-Funcionais-Cadastro-Unico-Municipal.md` – requisitos não funcionais
10. `010-Especificacoes-Cadastro-Unico-Municipal.md` – especificações
11. `011-Criterios-de-Aceitacao-Cadastro-Unico-Municipal.md` – critérios de aceitação
12. `012-Matriz-de-Rastreabilidade-Cadastro-Unico-Municipal.md` – matriz de rastreabilidade
13. `013-Modelo-de-Dados-Cadastro-Unico-Municipal.md` – modelo de dados do domínio
14. `014-Modelo-de-Integracao-Cadastro-Unico-Municipal.md` – modelo de integração
15. `015-Arquitetura-de-Servicos-Cadastro-Unico-Municipal.md` – arquitetura de serviços
16. `016-Modelo-de-Seguranca-Cadastro-Unico-Municipal.md` – modelo de segurança
17. `017-Modelo-de-Auditoria-Cadastro-Unico-Municipal.md` – modelo de auditoria
18. `018-Plano-de-Testes-Cadastro-Unico-Municipal.md` – plano de testes
19. `019-Casos-de-Teste-Cadastro-Unico-Municipal.md` – casos de teste
20. `020-Plano-de-Implantacao-Cadastro-Unico-Municipal.md` – plano de implantação
21. `021-Checklist-de-Prontidao-para-Producao-Cadastro-Unico-Municipal.md` – checklist de prontidão para produção
22. `022-Plano-de-Migracao-de-Dados-Cadastro-Unico-Municipal.md` – plano de migração de dados
23. `023-Plano-de-Treinamento-Cadastro-Unico-Municipal.md` – plano de treinamento
24. `024-Plano-de-Suporte-e-Operacao-Cadastro-Unico-Municipal.md` – plano de suporte e operação
25. `025-Estrutura-Tecnica-Cadastro-Unico-Municipal.md` – estrutura técnica
26. `026-Modelo-de-Dominio-Cadastro-Unico-Municipal.md` – modelo de domínio

---

# 7. Versionamento

| Versão | Data       | Descrição                                    |
| ------ | ---------- | -------------------------------------------- |
| 1.0    | 2026-08-20 | Criação do documento de definição do domínio |

---

**Documento:** 000-Dominio-Cadastro-Unico-Municipal.md

**Última atualização:** 2026-08-20

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
