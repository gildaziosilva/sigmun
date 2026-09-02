#### Modelo de Domínio – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000C-HIERARQUIA-DOCUMENTAL.md
- 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
- 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
- 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
- 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
- 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
- 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
- 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
- 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
- 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
- 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
- 012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
- 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md
- 014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md
- 015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
- 016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
- 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
- 025-Estrutura-Tecnica-Gestao-de-Compras-e-Contratacoes.md

---

# 1. Finalidade

Este documento define o **Modelo de Domínio Técnico do domínio Gestão de Compras e Contratações do SIGMUN**.

Seu objetivo é estabelecer os principais conceitos técnicos que representam o negócio, seus limites, responsabilidades, relacionamentos, estados, invariantes e comportamentos.

O modelo deverá servir como ponte entre:

```text
Modelo de Negócio
        ↓
Regras de Negócio
        ↓
Requisitos
        ↓
Modelo de Dados
        ↓
Modelo de Domínio
        ↓
Implementação

Este documento não substitui o Modelo de Dados nem a Especificação Técnica.

2. Objetivos

São objetivos deste documento:

definir os conceitos centrais do domínio;
estabelecer as entidades;
estabelecer os objetos de valor;
estabelecer os agregados;
identificar as raízes dos agregados;
definir responsabilidades;
definir estados;
definir transições;
preservar as regras de negócio;
estabelecer limites de consistência;
identificar eventos de domínio;
orientar a implementação;
manter rastreabilidade;
reduzir acoplamento entre componentes.
3. Princípios do Modelo de Domínio

O modelo deverá observar:

Alta coesão;
Baixo acoplamento;
Encapsulamento;
Integridade das regras de negócio;
Responsabilidade única;
Rastreabilidade;
Testabilidade;
Independência de infraestrutura;
Evolução incremental.
4. Limite do Domínio

O domínio representa os processos relacionados à Gestão de Compras e Contratações do Município.

Seu escopo deverá contemplar, conforme os artefatos funcionais existentes:

planejamento da contratação;
demandas;
processos de contratação;
itens;
fornecedores;
contratações;
contratos;
documentos;
acompanhamento;
fiscalização;
encerramento;
registros de auditoria relacionados ao domínio.

A delimitação definitiva deverá respeitar os documentos funcionais e o Modelo de Dados.

5. Linguagem Ubíqua

A implementação deverá utilizar uma linguagem comum entre:

usuários;
analistas;
gestores;
arquitetos;
desenvolvedores;
equipe de testes;
equipe de suporte.

Termos técnicos deverão ser derivados do vocabulário de negócio do SIGMUN.

6. Conceitos Principais

Os principais conceitos identificados para o domínio são:

Demanda
Processo de Contratação
Item
Fornecedor
Contratação
Contrato
Documento
Fiscalização
Ocorrência

A lista permanece evolutiva e deverá ser validada durante a implementação.

7. Entidades

Entidades são objetos que possuem identidade própria e ciclo de vida.

Neste domínio, são candidatos a entidades:

Entidade	Identidade	Ciclo de Vida
Demanda	ID	Sim
Processo de Contratação	ID	Sim
Item	ID	Sim
Fornecedor	ID/CNPJ	Sim
Contratação	ID	Sim
Contrato	ID	Sim
Documento	ID	Sim
Fiscalização	ID	Sim
Ocorrência	ID	Sim

A definição definitiva de cada entidade deverá ser validada contra o Modelo de Dados.

8. Entidade Demanda

Representa uma necessidade de aquisição ou contratação identificada pela Administração Municipal.

Responsabilidades possíveis:

registrar a necessidade;
identificar unidade solicitante;
registrar justificativa;
registrar itens;
controlar estado da demanda;
permitir aprovação;
manter histórico relevante.

A entidade não deverá permitir transições de estado que violem as regras de negócio.

9. Entidade Processo de Contratação

Representa o processo administrativo utilizado para conduzir determinada contratação.

Responsabilidades:

identificar o processo;
relacionar a demanda;
controlar situação;
registrar etapas;
manter documentos relacionados;
registrar tramitações;
controlar encerramento.
10. Entidade Item

Representa um item objeto de aquisição ou contratação.

Pode representar:

material;
serviço;
solução;
outro objeto previsto pelo domínio.

Responsabilidades:

identificação;
descrição;
quantidade;
unidade;
valores;
relacionamento com demanda;
relacionamento com contratação.
11. Entidade Fornecedor

Representa a pessoa física ou jurídica que poderá participar ou manter relação contratual com o Município.

A identificação deverá respeitar os mecanismos corporativos de cadastro e identificação.

Responsabilidades:

identificação;
dados cadastrais;
situação;
relacionamento com contratações;
histórico relacionado ao domínio.
12. Entidade Contratação

Representa o resultado administrativo do processo de contratação.

Responsabilidades:

registrar contratação;
relacionar fornecedor;
relacionar itens;
registrar valores;
controlar situação;
gerar ou originar contrato quando aplicável.
13. Entidade Contrato

Representa o instrumento formal que estabelece direitos e obrigações entre o Município e o contratado.

Responsabilidades:

identificação;
vigência;
objeto;
valores;
fornecedor;
situação;
alterações;
fiscalização;
encerramento.
14. Entidade Documento

Representa documentos associados aos processos e operações do domínio.

Pode estar relacionado a:

demanda;
processo;
contratação;
contrato;
fiscalização.

A gestão física e o armazenamento deverão seguir a arquitetura corporativa de documentos.

15. Entidade Fiscalização

Representa um registro relacionado ao acompanhamento da execução contratual.

Responsabilidades possíveis:

registrar fiscalização;
registrar data;
registrar responsável;
registrar situação;
registrar evidências;
registrar ocorrências;
registrar providências.
16. Entidade Ocorrência

Representa um fato relevante identificado durante o acompanhamento de uma contratação ou contrato.

Responsabilidades:

registrar ocorrência;
classificar ocorrência;
registrar impacto;
registrar providências;
controlar resolução.
17. Objetos de Valor

Objetos de valor representam conceitos sem identidade própria.

Candidatos:

CNPJ
CPF
ValorMonetario
Periodo
Endereco
NumeroProcesso
NumeroContrato
Status
TipoDocumento

A implementação definitiva deverá ocorrer somente após validação dos requisitos e modelo de dados.

18. Valor Monetário

O conceito de valor monetário deverá encapsular:

valor;
moeda;
precisão necessária.

Não deverá ser tratado simplesmente como número sem contexto quando isso comprometer a integridade do domínio.

19. Período

O objeto de valor Período poderá representar:

Data Inicial
Data Final

Deverá garantir:

Data Inicial <= Data Final

quando aplicável.

20. Identificação de Processo

O número do processo administrativo deverá possuir regras de validação e identificação conforme o padrão definido pelo SIGMUN.

21. Identificação de Contrato

O identificador do contrato deverá permitir:

identificação;
rastreabilidade;
associação ao processo;
associação ao fornecedor;
consulta histórica.
22. Agregados

Os agregados deverão estabelecer limites de consistência.

Candidatos iniciais:

Agregado Demanda
Agregado Processo de Contratação
Agregado Contratação
Agregado Contrato
Agregado Fiscalização

A definição final deverá ser validada durante a implementação.

23. Agregado Demanda

Raiz: Demanda

Possíveis componentes:

Demanda
 ├── Item
 └── Informações da solicitação

Responsabilidades:

controlar a demanda;
garantir consistência de seus itens;
controlar seu ciclo de vida;
impedir alterações incompatíveis com seu estado.
24. Agregado Processo de Contratação

Raiz: Processo de Contratação

Possíveis componentes:

Processo de Contratação
 ├── Itens
 ├── Documentos
 └── Informações de tramitação

Responsabilidades:

controlar o processo;
garantir consistência;
controlar etapas;
manter relacionamento com a demanda.
25. Agregado Contratação

Raiz: Contratação

Possíveis componentes:

Contratação
 ├── Itens
 ├── Fornecedor
 └── Informações da contratação

Responsabilidades:

controlar a contratação;
garantir consistência;
relacionar fornecedor;
controlar valores;
controlar estado.
26. Agregado Contrato

Raiz: Contrato

Possíveis componentes:

Contrato
 ├── Itens
 ├── Documentos
 ├── Fiscalizações
 └── Ocorrências

A composição definitiva deverá respeitar o limite transacional estabelecido durante a implementação.

27. Agregado Fiscalização

Raiz: Fiscalização

Possíveis componentes:

Fiscalização
 ├── Evidências
 └── Ocorrências

O modelo definitivo deverá evitar que a fiscalização ultrapasse os limites de responsabilidade estabelecidos pelo domínio.

28. Relacionamentos Conceituais

O relacionamento inicial poderá ser representado por:

Demanda
   │
   ▼
Processo de Contratação
   │
   ▼
Contratação
   │
   ├──────────► Fornecedor
   │
   ▼
Contrato
   │
   ▼
Fiscalização
   │
   ▼
Ocorrência

Documentos poderão estar associados aos diferentes elementos do processo.

29. Fluxo Conceitual
Necessidade
    ↓
Demanda
    ↓
Análise
    ↓
Processo de Contratação
    ↓
Contratação
    ↓
Fornecedor
    ↓
Contrato
    ↓
Execução
    ↓
Fiscalização
    ↓
Encerramento

Este fluxo é conceitual e deverá ser refinado conforme os processos oficiais.

30. Estados

Entidades com ciclo de vida deverão possuir estados explícitos.

Exemplo conceitual:

RASCUNHO
   ↓
SUBMETIDA
   ↓
EM_ANALISE
   ↓
APROVADA
   ↓
EM_EXECUCAO
   ↓
CONCLUIDA

Os estados reais deverão ser derivados das regras de negócio.

31. Transições

As transições deverão ser controladas pelo domínio.

Exemplo:

RASCUNHO → SUBMETIDA
SUBMETIDA → EM_ANALISE
EM_ANALISE → APROVADA
EM_ANALISE → REJEITADA
APROVADA → EM_EXECUCAO
EM_EXECUCAO → CONCLUIDA

Não deverá ser permitido alterar diretamente o estado ignorando as regras.

32. Invariantes

Invariantes representam condições que deverão permanecer verdadeiras.

Exemplos:

entidade deve possuir identificador;
quantidade deve ser válida;
valores monetários devem respeitar regras de negócio;
contrato deve possuir dados mínimos;
período de vigência deve ser consistente;
transições de estado devem ser válidas.
33. Regras de Estado

Cada entidade com ciclo de vida deverá possuir regras explícitas.

Exemplo:

Contrato encerrado
    ↓
não pode ser simplesmente reaberto

qualquer exceção deverá ser expressamente definida por regra de negócio.

34. Serviços de Domínio

Serviços de domínio deverão existir somente quando uma operação não pertencer naturalmente a uma única entidade ou agregado.

Exemplos candidatos:

ServicoDeValidacaoDeContratacao
ServicoDeValidacaoDeVigencia
ServicoDeAnaliseDeConsistencia

Esses serviços deverão ser confirmados durante a implementação.

35. Repositórios

Repositórios representam abstrações de persistência.

Candidatos:

RepositorioDeDemandas
RepositorioDeProcessos
RepositorioDeContratacoes
RepositorioDeContratos
RepositorioDeFornecedores

As interfaces deverão permanecer independentes da tecnologia de banco de dados.

36. Eventos de Domínio

Eventos deverão representar fatos já ocorridos.

Candidatos:

DemandaCriada
DemandaSubmetida
DemandaAprovada
ProcessoCriado
ProcessoAprovado
ContratacaoRealizada
ContratoCriado
ContratoAlterado
FiscalizacaoRegistrada
OcorrenciaRegistrada
ContratoEncerrado

A lista definitiva deverá ser estabelecida conforme os casos de uso.

37. Eventos Não São Comandos

O domínio deverá distinguir:

Comando
    ↓
Solicitação de uma ação


Evento
    ↓
Fato que já ocorreu

Exemplo:

AprovarContratoCommand
        ↓
ContratoAprovadoEvent
38. Regras de Negócio

As regras de negócio deverão permanecer alinhadas ao documento:

007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md

Não deverão ser duplicadas em múltiplas camadas sem necessidade.

39. Encapsulamento

As entidades deverão proteger seu próprio estado.

Preferencialmente:

Entidade
   ↓
Método de comportamento
   ↓
Validação
   ↓
Alteração de estado

em vez de:

Código externo
   ↓
Alteração direta de atributos
40. Exemplo Conceitual

Em vez de:

contrato.status = "ENCERRADO";

o modelo deverá favorecer comportamento equivalente a:

contrato.encerrar();

quando o encerramento for uma operação de domínio.

A implementação concreta dependerá da tecnologia escolhida.

41. Separação entre Domínio e Infraestrutura

O domínio não deverá depender diretamente de:

ORM;
banco;
HTTP;
framework web;
sistema operacional;
serviços externos.

Essas dependências deverão permanecer nas camadas apropriadas.

42. Persistência

O modelo de domínio deverá ser persistido conforme:

013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md

O modelo de domínio não deverá ser alterado simplesmente para atender limitações de persistência sem avaliação arquitetural.

43. Mapeamento Domínio → Dados

O relacionamento entre domínio e persistência deverá ser explicitamente definido.

Exemplo:

Entidade de Domínio
        ↓
Mapeamento
        ↓
Modelo de Persistência
        ↓
Banco de Dados
44. Integrações

O domínio deverá utilizar abstrações para comunicação com outros domínios e sistemas.

A definição deverá respeitar:

014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md

45. Serviços Externos

Serviços externos deverão ser encapsulados por portas/adaptadores.

Exemplo:

Domínio
   ↓
Interface
   ↓
Adaptador
   ↓
Serviço Externo
46. Segurança

O modelo deverá respeitar:

016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md

A autorização deverá ocorrer no contexto adequado sem transformar regras de segurança em regras de negócio indevidamente acopladas.

47. Auditoria

Eventos relevantes deverão permitir rastreabilidade.

A implementação deverá respeitar:

017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md

48. Rastreabilidade

Cada elemento relevante deverá possuir relação com os artefatos superiores.

Exemplo:

RN
 ↓
RF
 ↓
UC
 ↓
Modelo de Domínio
 ↓
Componente
 ↓
Teste
 ↓
Critério de Aceitação
49. Matriz Inicial de Rastreabilidade
Elemento	Artefato de Origem	Elemento Técnico
Demanda	Casos de Uso	Agregado Demanda
Processo	Casos de Uso	Agregado Processo
Contratação	Requisitos	Agregado Contratação
Contrato	Requisitos	Agregado Contrato
Fornecedor	Modelo de Dados	Entidade Fornecedor
Fiscalização	Regras de Negócio	Agregado Fiscalização

A matriz deverá ser ampliada durante a implementação.

50. Critérios para Criação de Entidade

Uma entidade somente deverá ser criada quando houver necessidade de:

identidade própria;
ciclo de vida;
comportamento;
regras próprias;
rastreabilidade individual.
51. Critérios para Objeto de Valor

Um conceito deverá ser considerado objeto de valor quando:

não possuir identidade independente;
for definido por seus atributos;
puder ser imutável;
possuir validações próprias.
52. Critérios para Agregado

Um agregado deverá ser criado quando houver necessidade de:

consistência transacional;
invariantes;
fronteira clara;
raiz de acesso;
controle de ciclo de vida.
53. Critérios para Serviço de Domínio

Um serviço de domínio deverá ser utilizado quando:

a operação for de negócio;
não pertencer naturalmente a uma entidade;
envolver múltiplos conceitos;
precisar permanecer no domínio.
54. Critérios para Evento

Um evento deverá ser criado quando um fato relevante do negócio precisar ser:

comunicado;
auditado;
processado;
rastreado;
utilizado por outro componente.
55. Limites de Consistência

O domínio deverá evitar transações desnecessariamente grandes.

Cada agregado deverá proteger apenas a consistência que realmente lhe pertence.

56. Concorrência

Alterações concorrentes deverão respeitar as invariantes do agregado.

O mecanismo técnico poderá utilizar:

versionamento;
controle otimista;
bloqueios;
outras estratégias adequadas.

A decisão técnica será registrada posteriormente quando necessária.

57. Idempotência

Operações que possam ser executadas mais de uma vez deverão possuir tratamento de idempotência quando necessário.

58. Integridade

O domínio deverá impedir estados inválidos.

Exemplo:

Contrato
   ↓
Encerrado
   ↓
Operação incompatível
   ↓
ERRO DE REGRA DE NEGÓCIO
59. Erros de Domínio

Erros relacionados a regras de negócio deverão ser expressos de forma identificável.

Exemplos conceituais:

DemandaInvalida
TransicaoDeEstadoInvalida
ContratoInvalido
VigenciaInvalida
OperacaoNaoPermitida
60. Dependências

O modelo deverá minimizar dependências externas.

┌──────────────────┐
│     Domínio      │
└────────┬─────────┘
         │
         ▼
    Abstrações
         │
         ▼
┌──────────────────┐
│  Infraestrutura  │
└──────────────────┘
61. Componentes Técnicos Derivados

A partir deste modelo poderão surgir componentes como:

Demanda
DemandaService
DemandaRepository


ProcessoContratacao
ProcessoContratacaoService
ProcessoContratacaoRepository


Contratacao
ContratacaoService
ContratacaoRepository


Contrato
ContratoService
ContratoRepository


Fornecedor
FornecedorRepository


Fiscalizacao
FiscalizacaoService
FiscalizacaoRepository

Os nomes definitivos deverão seguir o padrão de desenvolvimento escolhido.

62. Não Antecipação de Implementação

Este documento não deverá definir prematuramente:

linguagem;
framework;
ORM;
banco específico;
provedor de nuvem;
servidor;
biblioteca.

Essas decisões deverão ser registradas nos respectivos artefatos técnicos ou ADRs.

63. Evolução Incremental

O modelo será evolutivo.

Durante a implementação poderão surgir:

novos conceitos;
novas regras;
novos agregados;
novos eventos;
novos serviços.

Alterações deverão ser registradas e rastreadas.

64. Controle de Mudanças

Alterações que afetem:

limites do domínio;
agregados;
regras;
integrações;
persistência;
segurança;

deverão ser avaliadas quanto ao impacto nos demais artefatos.

65. Próxima Etapa Técnica

Após a aprovação deste modelo, a implementação deverá avançar incrementalmente.

A primeira etapa prática deverá ser:

Modelo de Domínio
      ↓
Definir Agregado inicial
      ↓
Definir Entidades
      ↓
Definir Objetos de Valor
      ↓
Definir Regras
      ↓
Implementar
      ↓
Testar

Não será necessário modelar todo o domínio novamente antes de iniciar o código.

66. Estratégia Incremental de Implementação

A implementação deverá começar pelo primeiro fluxo de negócio prioritário, e não pelo desenvolvimento simultâneo de todo o domínio.

A ordem deverá considerar:

valor para o negócio;
dependências;
risco;
complexidade;
capacidade de validação;
necessidade operacional.
67. Primeiro Incremento

O primeiro incremento deverá ser definido a partir dos casos de uso e processos já documentados.

Antes da implementação, deverão ser identificados:

caso de uso;
história de usuário;
regra de negócio;
requisito funcional;
entidade;
agregado;
serviço;
persistência;
critério de aceitação;
caso de teste.
68. Resultado Esperado

Ao final da implementação incremental, deverá existir:

Código
+
Testes
+
Persistência
+
API/Interface
+
Segurança
+
Auditoria
+
Rastreabilidade

para cada incremento funcional concluído.

69. Checklist do Modelo de Domínio
 Limite do domínio definido.
 Linguagem ubíqua identificada.
 Entidades identificadas.
 Objetos de valor identificados.
 Agregados identificados.
 Raízes dos agregados identificadas.
 Relacionamentos identificados.
 Estados identificados.
 Transições identificadas.
 Invariantes identificadas.
 Serviços de domínio identificados.
 Eventos identificados.
 Repositórios identificados.
 Integrações consideradas.
 Segurança considerada.
 Auditoria considerada.
 Rastreabilidade estabelecida.
70. Situação do Artefato
Modelo:        026
Versão:        1.0
Situação:      Em evolução
Finalidade:    Orientar implementação técnica
Próxima etapa: Primeiro incremento implementável
71. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-15	Criação do Modelo de Domínio Técnico

Documento: 026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-15

Responsável: Equipe SIGMUN

Status da revisão: Vigente