#### Plano de Migração de Dados – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
- 000C-HIERARQUIA-DOCUMENTAL.md
- 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
- 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
- 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
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
- 018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
- 019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
- 020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md
- 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md

---

# 1. Finalidade

Este documento estabelece o **Plano de Migração de Dados do Domínio de Gestão de Compras e Contratações do SIGMUN**.

Seu objetivo é definir as diretrizes para levantamento, análise, preparação, saneamento, transformação, validação, carga, reconciliação e disponibilização dos dados provenientes de sistemas, arquivos ou bases de dados existentes.

A migração deverá preservar a integridade, consistência, rastreabilidade e confiabilidade das informações.

---

# 2. Objetivos

São objetivos deste plano:

1. identificar as fontes de dados;
2. identificar os responsáveis pelas fontes;
3. definir o escopo da migração;
4. avaliar a qualidade dos dados;
5. identificar dados duplicados;
6. identificar dados inconsistentes;
7. definir regras de transformação;
8. mapear origem e destino;
9. realizar cargas de teste;
10. validar os dados migrados;
11. realizar reconciliação;
12. executar a carga definitiva;
13. preservar informações históricas quando aplicável;
14. garantir rastreabilidade da migração;
15. estabelecer procedimentos de rollback.

---

# 3. Princípios

A migração deverá observar:

## 3.1 Integridade

Os dados migrados deverão manter sua consistência.

## 3.2 Rastreabilidade

Deverá ser possível identificar a origem dos dados quando aplicável.

## 3.3 Preservação Histórica

Informações históricas relevantes deverão ser preservadas conforme escopo aprovado.

## 3.4 Qualidade

Dados inconsistentes deverão ser identificados e tratados.

## 3.5 Segurança

Os dados deverão ser protegidos durante todo o processo.

## 3.6 Reversibilidade

Operações críticas deverão possuir estratégia de recuperação.

## 3.7 Validação

Nenhuma carga definitiva deverá ocorrer sem validação prévia.

---

# 4. Escopo

A migração poderá contemplar, conforme levantamento e aprovação:

- demandas;
- planejamentos;
- processos;
- fornecedores;
- itens;
- objetos de contratação;
- propostas;
- resultados;
- contratos;
- documentos;
- aditivos;
- execução contratual;
- fiscalização;
- medições;
- ocorrências;
- encerramentos;
- informações históricas;
- dados auxiliares;
- tabelas de referência.

---

# 5. Fora do Escopo

Não deverão ser migrados automaticamente:

- dados sem origem identificável;
- dados corrompidos sem possibilidade de recuperação;
- dados sem finalidade definida;
- dados duplicados sem regra de consolidação;
- dados incompatíveis com o modelo de destino;
- informações cuja migração não tenha sido aprovada.

---

# 6. Estratégia Geral

A migração seguirá o fluxo:

```text
Levantamento
    ↓
Inventário
    ↓
Perfilamento
    ↓
Análise de Qualidade
    ↓
Mapeamento
    ↓
Saneamento
    ↓
Transformação
    ↓
Carga de Teste
    ↓
Validação
    ↓
Homologação
    ↓
Carga Definitiva
    ↓
Reconciliação
    ↓
Validação Pós-Migração

7. Inventário das Fontes

Todas as fontes deverão ser registradas.

ID	Fonte	Tipo	Responsável	Periodicidade	Situação
FON-001		Banco de Dados			
FON-002		Planilha			
FON-003		Arquivo			
FON-004		API			
8. Tipos de Fonte

As fontes poderão incluir:

bancos de dados relacionais;
bancos de dados não relacionais;
planilhas;
arquivos CSV;
arquivos XML;
arquivos JSON;
APIs;
sistemas legados;
documentos estruturados;
arquivos institucionais.
9. Responsabilidade sobre as Fontes

Cada fonte deverá possuir responsável identificado.

O responsável deverá:

autorizar acesso;
validar os dados;
esclarecer dúvidas;
validar regras de transformação;
aprovar resultados da migração.
10. Inventário de Dados

Para cada entidade deverá ser identificado:

nome;
descrição;
fonte;
tabela ou estrutura;
campo;
tipo;
tamanho;
obrigatoriedade;
domínio;
relacionamento;
volume;
qualidade;
destino.
11. Entidades Prioritárias

As entidades prioritárias deverão ser avaliadas inicialmente:

Entidade	Prioridade
Fornecedor	Alta
Processo	Alta
Contratação	Alta
Contrato	Alta
Item	Alta
Documento	Alta
Fiscalização	Média
Execução	Média
Proposta	Média
Demanda	Média

A priorização definitiva deverá ser validada durante o levantamento.

12. Perfilamento dos Dados

Antes da migração deverão ser realizados procedimentos de perfilamento.

Deverão ser avaliados:

quantidade de registros;
valores nulos;
valores inválidos;
duplicidades;
padrões;
distribuição;
inconsistências;
relacionamentos;
registros órfãos;
formatos;
valores fora do domínio.
13. Qualidade dos Dados

A qualidade deverá ser avaliada segundo:

Dimensão	Avaliação
Completude	Campos obrigatórios preenchidos
Consistência	Dados coerentes
Unicidade	Ausência de duplicidades
Validade	Dados dentro dos domínios
Integridade	Relacionamentos preservados
Atualidade	Dados adequados ao período
Rastreabilidade	Origem identificável
14. Classificação dos Dados

Os dados deverão ser classificados conforme sua utilização.

Ativo
Histórico
Duplicado
Inválido
Incompleto
Inconsistente
Obsoleto
Não Migrável
15. Tratamento de Duplicidades

As duplicidades deverão ser identificadas antes da carga.

Deverão ser definidas regras para:

identificação;
agrupamento;
escolha do registro principal;
preservação de informações;
consolidação;
registro da decisão.

Nenhum registro deverá ser eliminado sem regra formal ou autorização aplicável.

16. Tratamento de Dados Incompletos

Dados incompletos deverão ser classificados.

Possibilidades:

correção na origem;
complementação;
transformação;
utilização de valor padrão;
migração parcial;
não migração.

A decisão deverá ser registrada.

17. Tratamento de Dados Inválidos

Dados inválidos deverão ser:

identificados;
classificados;
isolados;
corrigidos quando possível;
validados;
documentados.
18. Mapeamento Origem → Destino

Cada campo relevante deverá possuir correspondência.

Origem	Campo Origem	Destino	Campo Destino	Transformação
				
				
				
19. Regras de Transformação

As transformações poderão incluir:

conversão de tipos;
padronização;
normalização;
concatenação;
separação;
conversão de códigos;
conversão de unidades;
tratamento de datas;
tratamento de valores monetários;
tratamento de identificadores.

Todas as transformações relevantes deverão ser documentadas.

20. Datas

As datas deverão ser padronizadas.

Deverão ser tratados:

formatos diferentes;
timezone;
datas inválidas;
datas incompletas;
datas históricas;
campos de data/hora.

A representação definitiva deverá seguir o padrão adotado pelo SIGMUN.

21. Valores Monetários

Valores monetários deverão ser tratados com atenção especial.

Deverão ser verificados:

moeda;
casas decimais;
separadores;
valores negativos;
arredondamentos;
precisão;
unidade monetária.

Nenhum arredondamento deverá ocorrer sem regra definida.

22. Identificadores

Deverão ser definidos procedimentos para:

identificadores internos;
identificadores externos;
códigos legados;
chaves naturais;
chaves substitutas;
identificadores de fornecedores;
identificadores de processos;
identificadores de contratos.

Quando necessário, deverá existir tabela de correspondência entre identificadores antigos e novos.

23. Tabela de Correspondência
ID Origem	ID SIGMUN	Entidade	Origem	Observação
				
				
24. Documentos e Anexos

Quando documentos fizerem parte do escopo:

identificar arquivos;
validar formatos;
identificar relacionamentos;
preservar metadados;
preservar origem;
validar integridade;
validar acesso.

Os documentos deverão permanecer associados às entidades correspondentes.

25. Histórico

Quando houver dados históricos:

definir período;
definir entidades;
preservar datas;
preservar responsáveis;
preservar relacionamentos;
identificar origem;
preservar documentos quando aplicável.
26. Dados de Auditoria

Dados de auditoria provenientes do sistema anterior deverão ser avaliados separadamente.

Deverá ser definido:

o que será migrado;
o que será preservado como histórico;
como será identificado o sistema de origem;
como será mantida a integridade.

A trilha de auditoria existente não deverá ser confundida com novos eventos de auditoria gerados pelo SIGMUN.

27. Dados Sensíveis

Dados pessoais e informações que possuam restrição de acesso deverão receber tratamento adequado.

Durante a migração deverão ser observados:

controle de acesso;
criptografia quando aplicável;
proteção dos arquivos temporários;
proteção das credenciais;
logs;
descarte seguro;
retenção temporária.
28. Ambiente de Migração

A migração deverá utilizar ambientes controlados.

Origem
  ↓
Área de Staging
  ↓
Transformação
  ↓
Validação
  ↓
SIGMUN – Homologação
  ↓
Validação
  ↓
SIGMUN – Produção
29. Área de Staging

A área de staging deverá permitir:

armazenamento temporário;
validação;
transformação;
reconciliação;
identificação de erros;
reprocessamento.

O staging não deverá ser considerado ambiente definitivo de armazenamento operacional.

30. Carga de Teste

Antes da carga definitiva deverá ser realizada carga de teste.

A carga de teste deverá verificar:

volume;
integridade;
relacionamentos;
regras;
transformação;
desempenho;
documentos;
identificadores.
31. Validação da Carga de Teste

A validação deverá considerar:

Quantidade de registros
        ↓
Quantidade de registros válidos
        ↓
Quantidade de registros rejeitados
        ↓
Relacionamentos
        ↓
Valores
        ↓
Documentos
        ↓
Integridade
32. Reconciliação

A reconciliação deverá comparar origem e destino.

Exemplo:

Indicador	Origem	Destino	Diferença
Processos			
Fornecedores			
Contratos			
Itens			
Documentos			

Diferenças deverão ser explicadas e registradas.

33. Registros Rejeitados

Registros que não puderem ser migrados deverão ser registrados.

ID	Entidade	Motivo	Ação	Responsável	Status
REJ-001					
REJ-002					
34. Taxa de Migração

Deverá ser calculada:

Taxa de Migração =
Registros Migrados / Registros Elegíveis × 100

Também deverão ser acompanhados:

taxa de rejeição;
taxa de duplicidade;
taxa de correção;
taxa de inconsistência.
35. Critérios de Aceitação da Migração

A migração poderá ser considerada aprovada quando:

 origem identificada;
 escopo aprovado;
 mapeamento aprovado;
 regras de transformação aprovadas;
 carga de teste executada;
 dados validados;
 reconciliação realizada;
 rejeições analisadas;
 documentos validados quando aplicável;
 integridade referencial validada;
 responsáveis aprovarem os resultados.
36. Carga Definitiva

A carga definitiva deverá ocorrer somente após:

aprovação da migração de teste;
backup;
validação do ambiente;
aprovação dos responsáveis;
definição da janela;
comunicação aos envolvidos;
disponibilidade da equipe técnica;
disponibilidade do plano de rollback.
37. Janela de Migração

A janela deverá considerar:

volume;
duração estimada;
impacto operacional;
disponibilidade das equipes;
integrações;
indisponibilidade necessária;
tempo de contingência.
38. Checklist Pré-Migração
 Escopo aprovado.
 Fontes identificadas.
 Responsáveis definidos.
 Backup da origem realizado.
 Backup validado.
 Modelo de destino validado.
 Mapeamento aprovado.
 Transformações aprovadas.
 Dados saneados.
 Carga de teste aprovada.
 Ambiente de produção disponível.
 Plano de rollback disponível.
 Equipe disponível.
 Comunicação realizada.
39. Execução da Migração

Durante a execução deverão ser registrados:

início;
término;
versão dos scripts;
ambiente;
responsável;
quantidade processada;
quantidade migrada;
quantidade rejeitada;
erros;
ocorrências;
resultado.
40. Monitoramento

Durante a migração deverão ser monitorados:

CPU;
memória;
armazenamento;
banco;
conexões;
filas;
logs;
erros;
tempo de execução.
41. Falhas de Migração

Em caso de falha:

interromper quando necessário;
preservar logs;
identificar causa;
avaliar impacto;
corrigir;
reprocessar;
validar;
registrar ocorrência.
42. Rollback da Migração

O rollback poderá ocorrer quando:

dados forem corrompidos;
inconsistências graves forem identificadas;
carga incompleta comprometer a operação;
scripts apresentarem comportamento incorreto;
risco operacional for identificado.

O rollback deverá ser realizado conforme procedimento aprovado.

43. Pós-Migração

Após a carga definitiva deverão ser executadas:

validação de quantidade;
validação de integridade;
validação de relacionamentos;
validação de valores;
validação de documentos;
validação de consultas;
validação de relatórios;
validação de integrações;
validação de auditoria.
44. Reconciliação Pós-Migração

Deverá ser realizada reconciliação final.

Entidade	Origem	SIGMUN	Diferença	Justificativa
Demandas				
Processos				
Fornecedores				
Itens				
Propostas				
Contratos				
Documentos				
45. Validação Funcional

Os usuários-chave deverão validar:

consultas;
processos;
fornecedores;
contratos;
documentos;
históricos;
relatórios;
informações relevantes para operação.
46. Aprovação da Migração
Responsável Técnico

Nome: __________________________________

Data: //________

Assinatura: _____________________________

Responsável pelos Dados

Nome: __________________________________

Data: //________

Assinatura: _____________________________

Responsável Funcional

Nome: __________________________________

Data: //________

Assinatura: _____________________________

47. Resultado da Migração
[ ] APROVADA
[ ] APROVADA COM RESSALVAS
[ ] REPROVADA
[ ] INTERROMPIDA
[ ] ROLLBACK EXECUTADO

Observações:

48. Segurança e Descarte

Após a migração deverão ser avaliados:

arquivos temporários;
arquivos de staging;
cópias de dados;
credenciais;
arquivos exportados;
backups;
logs.

Materiais temporários contendo dados protegidos deverão ser descartados de forma segura conforme as políticas institucionais.

49. Auditoria da Migração

A migração deverá possuir registro contendo:

responsável;
data;
hora;
origem;
destino;
versão dos scripts;
quantidade de registros;
resultado;
erros;
rejeições;
aprovação.
50. Automação

Sempre que possível, a migração deverá ser automatizada por scripts versionados.

Os scripts deverão:

possuir controle de versão;
ser reproduzíveis;
possuir logs;
possuir tratamento de erros;
possuir validações;
evitar operações destrutivas sem confirmação;
permitir reprocessamento controlado.
51. Idempotência

Os processos de carga deverão ser projetados, quando tecnicamente possível, para permitir reexecução sem gerar duplicidade ou inconsistência.

A estratégia deverá considerar:

identificadores;
chaves naturais;
chaves técnicas;
controle de lotes;
registros já processados;
checkpoints.
52. Lotes de Migração

Quando o volume justificar, os dados poderão ser migrados em lotes.

Lote	Entidade	Volume	Status
LOTE-001			
LOTE-002			
LOTE-003			

Cada lote deverá possuir identificação própria.

53. Estratégia de Carga Incremental

Quando necessário, poderá ser utilizada carga incremental.

Exemplo:

Carga Inicial
      ↓
Validação
      ↓
Operação Paralela
      ↓
Captura de Alterações
      ↓
Carga Incremental
      ↓
Reconciliação
      ↓
Corte

A estratégia definitiva dependerá das características da fonte.

54. Operação Paralela

Quando necessário, o sistema legado e o SIGMUN poderão operar paralelamente durante período controlado.

Nesse caso deverão ser definidos:

duração;
processos abrangidos;
responsabilidades;
fonte oficial;
reconciliação;
critérios de encerramento.
55. Encerramento do Sistema Legado

A desativação do sistema anterior não deverá ocorrer imediatamente após a migração.

Deverá ser definida uma estratégia de:

preservação;
consulta histórica;
retenção;
arquivamento;
acesso controlado;
encerramento.

A decisão deverá considerar requisitos legais, administrativos e operacionais aplicáveis.

56. Indicadores de Migração

Deverão ser acompanhados:

Indicador	Objetivo
Registros elegíveis	Medir escopo
Registros migrados	Medir execução
Registros rejeitados	Medir problemas
Taxa de migração	Medir cobertura
Taxa de rejeição	Medir qualidade
Duplicidades	Medir saneamento
Inconsistências	Medir qualidade
Tempo de migração	Medir eficiência
Erros	Medir estabilidade
Reconciliação	Medir integridade
57. Riscos da Migração
Risco	Impacto	Probabilidade	Mitigação
Dados inconsistentes	Alto		Saneamento
Dados duplicados	Alto		Deduplicação
Perda de dados	Crítico		Backup e validação
Falha de transformação	Alto		Testes
Falha de carga	Alto		Carga piloto
Relacionamentos quebrados	Alto		Validação
Documentos perdidos	Alto		Validação de anexos
Identificadores inconsistentes	Alto		Tabela de correspondência
Tempo excessivo	Médio		Lotes
Falha de rollback	Crítico		Teste de recuperação
58. Responsabilidades
Equipe SIGMUN
definir estratégia;
desenvolver scripts;
executar migração;
monitorar;
registrar evidências;
corrigir problemas.
Responsáveis pelos Dados
validar origem;
validar conteúdo;
aprovar transformações;
validar resultado.
Usuários-Chave
validar dados;
validar processos;
identificar inconsistências;
homologar resultados.
Infraestrutura
disponibilizar ambientes;
garantir armazenamento;
executar backups;
garantir conectividade;
apoiar recuperação.
59. Evidências

Deverão ser preservadas, quando aplicável:

inventários;
arquivos de origem;
scripts;
logs;
relatórios;
resultados de validação;
relatórios de reconciliação;
registros de erro;
registros de aprovação.
60. Rastreabilidade

A migração deverá estar relacionada aos artefatos:

Modelo de Dados
      ↓
Requisitos
      ↓
Regras de Negócio
      ↓
Modelo de Integração
      ↓
Casos de Teste
      ↓
Plano de Implantação
      ↓
Plano de Migração
      ↓
Execução
      ↓
Validação

A rastreabilidade deverá ser registrada também em:

012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md

e:

000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md

61. Checklist Final de Migração
 Inventário concluído.
 Fontes validadas.
 Escopo aprovado.
 Dados perfilados.
 Qualidade avaliada.
 Duplicidades tratadas.
 Dados inválidos tratados.
 Mapeamento aprovado.
 Transformações aprovadas.
 Carga de teste executada.
 Carga de teste aprovada.
 Reconciliação realizada.
 Backup realizado.
 Rollback validado.
 Carga definitiva executada.
 Dados pós-carga validados.
 Relatórios validados.
 Integrações validadas.
 Usuários-chave aprovaram.
 Evidências armazenadas.
 Migração formalmente encerrada.
62. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Plano de Migração de Dados do Domínio de Gestão de Compras e Contratações

Documento: 022-Plano-de-Migracao-de-Dados-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente
