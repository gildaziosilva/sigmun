# 012 – Matriz de Rastreabilidade – Gestão de Compras e Contratações

**SIGMUN – Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

---

## 1. Identificação do Documento

| Campo | Informação |
|---|---|
| Documento | Matriz de Rastreabilidade – Gestão de Compras e Contratações |
| Código | DOM-COMPRAS-001-012 |
| Domínio | Gestão de Compras e Contratações |
| Sistema | SIGMUN |
| Versão | 1.0 |
| Status | Em desenvolvimento |
| Classificação da Informação | Pública |
| Responsável | Equipe SIGMUN |
| Documento Mestre do Domínio | `000-Dominio-Gestao-de-Compras-e-Contratacoes.md` |

---

# 2. Objetivo

Estabelecer a rastreabilidade entre os diferentes artefatos que compõem o domínio **Gestão de Compras e Contratações**, permitindo identificar a origem, evolução, implementação, validação e cobertura dos requisitos do domínio.

A matriz deve assegurar que cada necessidade de negócio possa ser rastreada desde sua origem até os respectivos requisitos, casos de uso, regras de negócio, especificações, implementação, testes e critérios de aceitação.

---

# 3. Finalidades

A matriz tem como finalidades:

- garantir rastreabilidade ponta a ponta;
- evitar requisitos sem implementação;
- evitar funcionalidades sem requisito correspondente;
- relacionar processos de negócio com requisitos;
- relacionar requisitos com casos de uso;
- relacionar requisitos com histórias de usuário;
- relacionar requisitos com regras de negócio;
- relacionar requisitos com especificações;
- relacionar requisitos com testes;
- relacionar testes com critérios de aceitação;
- apoiar homologação;
- apoiar auditoria;
- apoiar gestão de mudanças;
- facilitar análise de impacto;
- preservar a coerência arquitetural do domínio.

---

# 4. Princípio de Rastreabilidade

A rastreabilidade do domínio deverá seguir, sempre que aplicável, a seguinte cadeia:

```text
Necessidade de Negócio
        ↓
Capacidade de Negócio
        ↓
Processo
        ↓
Serviço
        ↓
Caso de Uso
        ↓
História de Usuário
        ↓
Regra de Negócio
        ↓
Requisito Funcional
        ↓
Requisito Não Funcional
        ↓
Especificação
        ↓
Modelo de Dados / Serviço / Integração
        ↓
Implementação
        ↓
Teste
        ↓
Critério de Aceitação
        ↓
Homologação

Nem todos os elementos precisam possuir relacionamento direto em todos os casos. Entretanto, nenhum requisito aprovado deverá permanecer sem uma cadeia de rastreabilidade adequada.

5. Artefatos do Domínio

A rastreabilidade deverá considerar os seguintes artefatos:

Código	Artefato
000	Domínio Gestão de Compras e Contratações
001	Mapa de Atores
002	Mapa de Capacidades
003	Mapa de Processos
004	Mapa de Serviços
005	Casos de Uso
006	Histórias de Usuário
007	Regras de Negócio
008	Requisitos Funcionais
009	Requisitos Não Funcionais
010	Especificações
011	Critérios de Aceitação
012	Matriz de Rastreabilidade
013	Modelo de Dados
014	Modelo de Integração
015	Arquitetura de Serviços
016	Modelo de Segurança
017	Modelo de Auditoria
018	Plano de Testes
019	Casos de Teste
020	Plano de Implantação
021	Checklist de Prontidão para Produção
022	Plano de Migração de Dados
023	Plano de Treinamento
024	Plano de Suporte e Operação
025	Estrutura Técnica
026	Modelo de Domínio
6. Identificação dos Requisitos

Os requisitos funcionais deverão utilizar identificadores únicos no seguinte padrão:

RF-COM-001
RF-COM-002
RF-COM-003
...

Os requisitos não funcionais deverão utilizar:

RNF-COM-001
RNF-COM-002
RNF-COM-003
...

As regras de negócio deverão utilizar:

RN-COM-001
RN-COM-002
RN-COM-003
...

Os casos de uso deverão utilizar:

UC-COM-001
UC-COM-002
UC-COM-003
...

As histórias de usuário deverão utilizar:

HU-COM-001
HU-COM-002
HU-COM-003
...

Os critérios de aceitação deverão utilizar:

CA-COM-001
CA-COM-002
CA-COM-003
...

Os casos de teste deverão utilizar:

CT-COM-001
CT-COM-002
CT-COM-003
...
7. Matriz Principal de Rastreabilidade
ID	Processo	Serviço	Caso de Uso	História	Regra de Negócio	Requisito Funcional	Requisito Não Funcional	Especificação	Critério de Aceitação	Caso de Teste	Status
RF-COM-001	—	—	—	—	—	RF-COM-001	—	—	—	—	A definir
RF-COM-002	—	—	—	—	—	RF-COM-002	—	—	—	—	A definir
RF-COM-003	—	—	—	—	—	RF-COM-003	—	—	—	—	A definir

Esta tabela deverá ser preenchida progressivamente durante a especificação do domínio.

8. Rastreabilidade de Processos
ID Processo	Processo	Capacidades Relacionadas	Serviços	Casos de Uso	Requisitos
PROC-COM-001	Planejamento da Contratação	—	—	—	—
PROC-COM-002	Solicitação de Compra	—	—	—	—
PROC-COM-003	Pesquisa de Preços	—	—	—	—
PROC-COM-004	Contratação	—	—	—	—
PROC-COM-005	Gestão da Contratação	—	—	—	—
PROC-COM-006	Recebimento	—	—	—	—
PROC-COM-007	Fiscalização	—	—	—	—
PROC-COM-008	Encerramento da Contratação	—	—	—	—

Os identificadores deverão ser ajustados aos processos oficialmente definidos no documento 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md.

9. Rastreabilidade de Capacidades
ID Capacidade	Capacidade	Processos	Serviços	Requisitos
CAP-COM-001	Planejar Contratações	—	—	—
CAP-COM-002	Gerenciar Solicitações	—	—	—
CAP-COM-003	Gerenciar Pesquisa de Preços	—	—	—
CAP-COM-004	Gerenciar Contratações	—	—	—
CAP-COM-005	Gerenciar Fornecedores	—	—	—
CAP-COM-006	Gerenciar Contratos	—	—	—
CAP-COM-007	Gerenciar Recebimentos	—	—	—
CAP-COM-008	Gerenciar Fiscalização	—	—	—
10. Rastreabilidade de Casos de Uso
Caso de Uso	Objetivo	Atores	Requisitos	Regras de Negócio	Critérios de Aceitação	Testes
UC-COM-001	—	—	—	—	—	—
UC-COM-002	—	—	—	—	—	—
UC-COM-003	—	—	—	—	—	—
UC-COM-004	—	—	—	—	—	—
UC-COM-005	—	—	—	—	—	—
11. Rastreabilidade de Histórias de Usuário
História	Ator	Necessidade	Requisito	Regra de Negócio	Critério de Aceitação	Caso de Teste
HU-COM-001	—	—	—	—	—	—
HU-COM-002	—	—	—	—	—	—
HU-COM-003	—	—	—	—	—	—
HU-COM-004	—	—	—	—	—	—
12. Rastreabilidade de Regras de Negócio
Regra	Descrição	Origem	Requisitos Afetados	Casos de Uso	Testes
RN-COM-001	—	—	—	—	—
RN-COM-002	—	—	—	—	—
RN-COM-003	—	—	—	—	—
RN-COM-004	—	—	—	—	—
13. Rastreabilidade dos Requisitos Não Funcionais
ID	Categoria	Requisito	Componentes Afetados	Especificação	Teste
RNF-COM-001	Segurança	—	—	—	—
RNF-COM-002	Desempenho	—	—	—	—
RNF-COM-003	Disponibilidade	—	—	—	—
RNF-COM-004	Auditoria	—	—	—	—
RNF-COM-005	Usabilidade	—	—	—	—
14. Rastreabilidade com o Modelo de Dados

Os requisitos que resultarem em persistência de informações deverão possuir correspondência no modelo de dados.

Requisito	Entidade	Atributo	Relacionamento	Regra de Integridade
RF-COM-001	—	—	—	—
RF-COM-002	—	—	—	—
RF-COM-003	—	—	—	—
15. Rastreabilidade com Integrações
Requisito	Sistema Externo	Integração	Operação	Dados	Segurança
RF-COM-001	—	—	—	—	—
RF-COM-002	—	—	—	—	—

As integrações deverão estar alinhadas ao:

014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md

16. Rastreabilidade com Serviços
Serviço	Caso de Uso	Requisitos	Entidades	API/Interface	Testes
SRV-COM-001	—	—	—	—	—
SRV-COM-002	—	—	—	—	—
SRV-COM-003	—	—	—	—	—
17. Rastreabilidade de Segurança
Requisito	Controle de Segurança	Perfil de Acesso	Autorização	Auditoria
RF-COM-001	—	—	—	—
RF-COM-002	—	—	—	—

A rastreabilidade deverá considerar o documento:

016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md

18. Rastreabilidade de Auditoria
Operação	Requisito	Evento de Auditoria	Usuário	Data/Hora	Evidência
—	—	—	—	—	—

A rastreabilidade de auditoria deverá estar alinhada ao:

017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md

19. Rastreabilidade de Testes
Requisito	Caso de Teste	Tipo	Resultado Esperado	Resultado Obtido	Status
RF-COM-001	CT-COM-001	Funcional	—	—	Pendente
RF-COM-002	CT-COM-002	Funcional	—	—	Pendente
RF-COM-003	CT-COM-003	Funcional	—	—	Pendente
20. Rastreabilidade dos Critérios de Aceitação
Requisito	Critério	Condição	Resultado Esperado	Evidência
RF-COM-001	CA-COM-001	—	—	—
RF-COM-002	CA-COM-002	—	—	—
RF-COM-003	CA-COM-003	—	—	—
21. Cobertura de Requisitos

A cobertura deverá ser acompanhada pelos seguintes indicadores:

21.1 Cobertura de Requisitos Funcionais
Cobertura RF =
RF com Caso de Uso / Total de RF × 100
21.2 Cobertura de Testes
Cobertura de Testes =
RF com Caso de Teste / Total de RF × 100
21.3 Cobertura de Critérios de Aceitação
Cobertura de Aceitação =
RF com Critério de Aceitação / Total de RF × 100
21.4 Cobertura de Implementação
Cobertura de Implementação =
RF implementados / Total de RF × 100
22. Status de Rastreabilidade

Cada elemento deverá possuir um dos seguintes estados:

Status	Significado
A definir	Elemento ainda não especificado
Em análise	Elemento em análise
Especificado	Elemento especificado
Implementado	Elemento implementado
Testado	Elemento testado
Homologado	Elemento homologado
Rejeitado	Elemento rejeitado
Obsoleto	Elemento substituído ou descontinuado
23. Gestão de Alterações

Toda alteração significativa em requisitos deverá avaliar seu impacto sobre:

processos;
serviços;
casos de uso;
histórias de usuário;
regras de negócio;
modelo de dados;
integrações;
segurança;
auditoria;
testes;
critérios de aceitação;
implantação;
treinamento;
operação.
24. Análise de Impacto

Quando um requisito for alterado, deverá ser realizada análise de impacto.

Fluxo recomendado:

Alteração
   ↓
Identificação do requisito
   ↓
Identificação das dependências
   ↓
Análise dos artefatos afetados
   ↓
Atualização dos artefatos
   ↓
Atualização da matriz
   ↓
Atualização dos testes
   ↓
Nova validação
25. Controle de Integridade da Matriz

A matriz deverá ser periodicamente verificada para identificar:

requisitos sem caso de uso;
requisitos sem história de usuário quando aplicável;
requisitos sem regra de negócio quando aplicável;
requisitos sem especificação;
requisitos sem implementação;
requisitos sem teste;
requisitos sem critério de aceitação;
casos de uso sem requisito;
testes sem requisito;
critérios de aceitação sem requisito;
entidades sem requisito correspondente;
serviços sem caso de uso ou requisito correspondente.
26. Critérios de Qualidade

A matriz será considerada adequada quando:

todos os requisitos possuírem identificadores únicos;
todos os requisitos estiverem associados à origem correspondente;
todos os requisitos funcionais possuírem cobertura de teste;
os critérios de aceitação estiverem associados aos requisitos;
os casos de teste estiverem associados aos requisitos;
alterações relevantes estiverem refletidas na matriz;
não existirem relacionamentos inconsistentes;
os artefatos do domínio permanecerem sincronizados.
27. Governança da Rastreabilidade

A manutenção da matriz é responsabilidade da governança do domínio e deverá ocorrer durante todo o ciclo de vida da solução.

A matriz deverá ser atualizada sempre que houver alteração em:

requisitos;
processos;
serviços;
regras de negócio;
arquitetura;
modelo de dados;
integrações;
segurança;
testes;
critérios de aceitação.
28. Relação com o Mapa Mestre Corporativo

Este documento integra o conjunto de artefatos do domínio:

DOM-COMPRAS-001

e deverá permanecer alinhado ao documento corporativo:

00-Governanca/000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md

29. Documentos Relacionados
Documentos Corporativos
00-Governanca/000A–Padrao-Corporativo-de-Documentacao-do-SIGMUN.md
00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md
00-Governanca/000F-Registro-de-Decisoes-Arquiteturais(ADR-Arqhiteture-Decision-Records).md
00-Governanca/000G–Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md
00-Governanca/000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
Documentos Corporativos de Negócio e Requisitos
02-Modelo-de-Negocio/Cadeia-de-Valor-v1.1.md
02-Modelo-de-Negocio/Mapa-de-Dominios.md
02-Modelo-de-Negocio/Mapa-de-Atores.md
02-Modelo-de-Negocio/Mapa-de-Capacidades.md
02-Modelo-de-Negocio/Mapa-de-Processos.md
02-Modelo-de-Negocio/Mapa-de-Servicos.md
02-Modelo-de-Negocio/Glossario-de-Negocio.md
03-Requisitos/Casos-de-Uso.md
03-Requisitos/Historias-de-Usuario-v1.0.md
03-Requisitos/Regras-de-Negocio-v1.0.md
03-Requisitos/Requisitos-Funcionais-v1.0.md
03-Requisitos/Requisitos-Nao-Funcionais-v1.0.md
03-Requisitos/Especificacoes-v1.0.md
03-Requisitos/Criterios-de-Aceitacao.md
03-Requisitos/Matriz-de-Rastreabilidade-v1.md
Documentos Específicos do Domínio
000-Dominio-Gestao-de-Compras-e-Contratacoes.md
001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md
014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md
015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md
021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md
022-Plano-de-Migracao-de-Dados-Gestao-de-Compras-e-Contratacoes.md
023-Plano-de-Treinamento-Gestao-de-Compras-e-Contratacoes.md
024-Plano-de-Suporte-e-Operacao-Gestao-de-Compras-e-Contratacoes.md
025-Estrutura-Tecnica-Gestao-de-Compras-e-Contratacoes.md
026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes.md
30. Histórico de Versões
Versão	Data	Descrição	Responsável
1.0	2026-08-16	Criação da matriz de rastreabilidade do domínio	Equipe SIGMUN
31. Aprovação
Papel	Responsável	Data	Status
Responsável pelo Domínio	—	—	Pendente
Arquitetura	—	—	Pendente
Governança	—	—	Pendente
Área de Negócio	—	—	Pendente