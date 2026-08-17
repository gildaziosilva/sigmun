#### Checklist de Prontidão para Produção – Gestão de Compras e Contratações

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

---

# 1. Finalidade

Este documento estabelece o **Checklist de Prontidão para Produção do Domínio de Gestão de Compras e Contratações do SIGMUN**.

Seu objetivo é verificar, de forma estruturada, se o domínio está tecnicamente, funcionalmente, operacionalmente e institucionalmente preparado para entrada em produção.

Este documento constitui um **gate de produção**.

A entrada em produção somente deverá ocorrer quando os critérios críticos de prontidão estiverem atendidos e formalmente validados.

---

# 2. Objetivos

São objetivos deste checklist:

1. verificar a conclusão da implementação;
2. verificar a conclusão dos testes;
3. validar requisitos críticos;
4. validar segurança;
5. validar auditoria;
6. validar banco de dados;
7. validar integrações;
8. validar infraestrutura;
9. validar backup e recuperação;
10. validar usuários e permissões;
11. validar documentação;
12. validar treinamento;
13. validar suporte;
14. validar monitoramento;
15. validar plano de reversão;
16. registrar pendências;
17. apoiar a decisão de entrada em produção.

---

# 3. Regra de Decisão

A decisão de produção deverá considerar quatro estados principais:

```text
PRONTO
NÃO PRONTO
PRONTO COM RESSALVAS
BLOQUEADO

3.1 PRONTO

Todos os critérios críticos foram atendidos.

3.2 NÃO PRONTO

Existem pendências que impedem a entrada em produção.

3.3 PRONTO COM RESSALVAS

Existem pendências não críticas formalmente aceitas pelos responsáveis.

3.4 BLOQUEADO

Existe risco crítico que impede a implantação.

4. Legenda do Checklist
Símbolo	Significado
[ ]	Não verificado
[x]	Aprovado
[!]	Pendência
[B]	Bloqueio
[N/A]	Não aplicável
5. Governança da Prontidão
Item	Status	Evidência	Responsável
Escopo aprovado	[ ]		
Versão definida	[ ]		
Responsáveis definidos	[ ]		
Janela de implantação definida	[ ]		
Aprovação da implantação registrada	[ ]		
Plano de comunicação aprovado	[ ]		
6. Documentação
6.1 Documentação Arquitetural
 Domínio documentado.
 Mapa de atores atualizado.
 Mapa de capacidades atualizado.
 Mapa de processos atualizado.
 Mapa de serviços atualizado.
 Casos de uso documentados.
 Histórias de usuário documentadas.
 Regras de negócio documentadas.
 Requisitos funcionais documentados.
 Requisitos não funcionais documentados.
 Especificações documentadas.
 Modelo de dados atualizado.
 Modelo de integração atualizado.
 Arquitetura de serviços atualizada.
 Modelo de segurança atualizado.
 Modelo de auditoria atualizado.

Status da seção: [ ]

7. Requisitos
 Requisitos funcionais implementados.
 Requisitos não funcionais avaliados.
 Regras de negócio implementadas.
 Critérios de aceitação atendidos.
 Requisitos críticos validados.
 Requisitos não implementados formalmente registrados.
 Exceções aprovadas.

Status da seção: [ ]

8. Rastreabilidade
 Casos de uso possuem rastreabilidade.
 Histórias de usuário possuem rastreabilidade.
 Regras de negócio possuem rastreabilidade.
 Requisitos possuem rastreabilidade.
 Critérios de aceitação possuem rastreabilidade.
 Casos de teste possuem rastreabilidade.
 Defeitos possuem rastreabilidade.
 Evidências de teste estão vinculadas.
 Matriz de rastreabilidade está atualizada.
 Mapa mestre de artefatos está atualizado.

Status da seção: [ ]

9. Implementação
 Código-fonte disponível.
 Código versionado.
 Branch de produção definida.
 Versão de release definida.
 Dependências identificadas.
 Dependências atualizadas.
 Código revisado.
 Pull Requests aprovados.
 Débitos técnicos críticos tratados.
 Configurações externas identificadas.
 Segredos não estão armazenados no código.
 Variáveis de ambiente configuradas.
 Scripts de implantação disponíveis.
 Scripts de rollback disponíveis.

Status da seção: [ ]

10. Banco de Dados
 Modelo físico validado.
 Migrações versionadas.
 Scripts de criação disponíveis.
 Scripts de atualização disponíveis.
 Índices revisados.
 Constraints revisadas.
 Integridade referencial validada.
 Regras de unicidade validadas.
 Dados obrigatórios preparados.
 Dados iniciais validados.
 Dados históricos validados quando aplicável.
 Estratégia de backup definida.
 Estratégia de restauração testada.

Status da seção: [ ]

11. Qualidade dos Dados
 Dados obrigatórios disponíveis.
 Dados duplicados tratados.
 Dados inconsistentes tratados.
 Dados inválidos identificados.
 Relacionamentos validados.
 Identificadores preservados.
 Origem dos dados identificada quando aplicável.
 Migração de teste executada.
 Migração definitiva validada.

Status da seção: [ ]

12. APIs
 APIs implementadas.
 Endpoints documentados.
 Autenticação validada.
 Autorização validada.
 Validação de entrada implementada.
 Tratamento de erros validado.
 Idempotência validada quando aplicável.
 Paginação validada.
 Versionamento definido.
 Logs implementados.
 APIs críticas testadas.

Status da seção: [ ]

13. Serviços
 Serviços implementados.
 Contratos de serviço definidos.
 Dependências identificadas.
 Tratamento de exceções validado.
 Timeouts configurados.
 Retry configurado quando aplicável.
 Circuit breaker configurado quando aplicável.
 Idempotência validada.
 Monitoramento disponível.

Status da seção: [ ]

14. Integrações
 Integrações identificadas.
 Sistemas externos identificados.
 Credenciais configuradas.
 Comunicação validada.
 Contratos de integração validados.
 Tratamento de indisponibilidade testado.
 Timeout testado.
 Retry testado.
 Idempotência testada.
 Falhas registradas.
 Monitoramento implementado.
15. Integrações Prioritárias
15.1 Orçamento
 Integração disponível.
 Teste realizado.
 Resultado validado.
15.2 Financeiro
 Integração disponível.
 Teste realizado.
 Resultado validado.
15.3 Outros Sistemas
 Sistema identificado.
 Integração validada.
 Responsável definido.

Status da seção: [ ]

16. Segurança
 Autenticação implementada.
 Autorização implementada.
 Perfis definidos.
 Permissões revisadas.
 Princípio do menor privilégio aplicado.
 Segregação de funções validada.
 Credenciais protegidas.
 Segredos protegidos.
 Comunicação protegida.
 Sessões protegidas.
 Logs de segurança ativos.
 Vulnerabilidades críticas tratadas.
 Testes de segurança aprovados.

Status da seção: [ ]

17. Auditoria
 Auditoria implementada.
 Operações críticas auditadas.
 Usuário registrado.
 Data/hora registrada.
 Operação registrada.
 Entidade registrada.
 Identificador registrado.
 Resultado registrado.
 Correlation ID registrado quando aplicável.
 Registros protegidos contra alteração indevida.
 Consulta de auditoria validada.

Status da seção: [ ]

18. Logs
 Logs de aplicação disponíveis.
 Logs de erro disponíveis.
 Logs de segurança disponíveis.
 Logs de integração disponíveis.
 Correlation ID implementado quando aplicável.
 Política de retenção definida.
 Dados sensíveis não são registrados indevidamente.
 Logs podem ser consultados pela equipe autorizada.

Status da seção: [ ]

19. Testes

Referência:

018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md

019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md

 Testes funcionais executados.
 Testes negativos executados.
 Testes de integração executados.
 Testes de segurança executados.
 Testes de auditoria executados.
 Testes de dados executados.
 Testes de performance executados quando aplicável.
 Testes de recuperação executados.
 Testes de regressão executados.
 Testes de sincronização executados quando aplicável.
 Evidências armazenadas.
 Resultados registrados.
20. Defeitos
Categoria	Quantidade	Aceitável?
Críticos		Não
Altos		Avaliar
Médios		Avaliar
Baixos		Avaliar

Critérios:

 Nenhum defeito crítico aberto.
 Nenhum defeito de segurança crítico aberto.
 Nenhum defeito de integridade de dados aberto.
 Nenhum defeito impeditivo aberto.
 Pendências restantes possuem aceite formal.

Status da seção: [ ]

21. Performance
 Tempo de resposta avaliado.
 Consultas críticas avaliadas.
 Operações de gravação avaliadas.
 APIs críticas avaliadas.
 Carga concorrente avaliada quando aplicável.
 Consumo de memória avaliado.
 Consumo de CPU avaliado.
 Banco avaliado.
 Gargalos conhecidos documentados.

Status da seção: [ ]

22. Infraestrutura
 Servidor disponível.
 Sistema operacional configurado.
 Banco disponível.
 Rede configurada.
 DNS configurado quando aplicável.
 Certificados configurados.
 Firewall configurado.
 Armazenamento disponível.
 Capacidade avaliada.
 Monitoramento configurado.
 Alertas configurados.

Status da seção: [ ]

23. Ambientes
Desenvolvimento
 Disponível.
 Configurado.
 Validado.
Homologação
 Disponível.
 Configurado.
 Validado.
 Homologação concluída.
Produção
 Disponível.
 Configurado.
 Validado.
 Pronto para implantação.

Status da seção: [ ]

24. Backup
 Backup configurado.
 Backup executado.
 Backup validado.
 Retenção definida.
 Local de armazenamento definido.
 Segurança do backup validada.
 Restauração testada.

Status da seção: [ ]

25. Recuperação de Desastres
 Procedimento de recuperação documentado.
 Responsáveis definidos.
 Ambiente de recuperação identificado.
 Backup disponível.
 Restauração testada.
 Tempo de recuperação avaliado.
 Dependências identificadas.

Status da seção: [ ]

26. Usuários
 Usuários administrativos cadastrados.
 Usuários operacionais cadastrados.
 Usuários-chave cadastrados.
 Perfis definidos.
 Permissões atribuídas.
 Permissões revisadas.
 Usuários inativos removidos/bloqueados quando aplicável.

Status da seção: [ ]

27. Treinamento
 Plano de treinamento executado.
 Usuários-chave treinados.
 Usuários operacionais treinados.
 Gestores treinados.
 Administradores treinados.
 Material disponibilizado.
 Registro de treinamento realizado.

Status da seção: [ ]

28. Documentação Operacional
 Manual do usuário disponível.
 Guia rápido disponível.
 Manual administrativo disponível.
 Procedimentos operacionais disponíveis.
 Procedimentos de suporte disponíveis.
 Procedimentos de recuperação disponíveis.
 Documentação técnica disponível.

Status da seção: [ ]

29. Suporte
 Canal de suporte definido.
 Responsáveis definidos.
 Horários definidos.
 Processo de abertura de chamados definido.
 Processo de escalonamento definido.
 Classificação de incidentes definida.
 Equipe de suporte treinada.

Status da seção: [ ]

30. Monitoramento
 Monitoramento da aplicação ativo.
 Monitoramento dos serviços ativo.
 Monitoramento do banco ativo.
 Monitoramento das integrações ativo.
 Monitoramento de infraestrutura ativo.
 Alertas configurados.
 Dashboard disponível.
 Responsáveis pelos alertas definidos.

Status da seção: [ ]

31. Notificações
 Notificações configuradas.
 Templates validados.
 Destinatários configurados.
 Testes executados.
 Falhas de envio tratadas.
 Duplicidade testada.

Status da seção: [ ]

32. Relatórios
 Relatórios críticos disponíveis.
 Filtros validados.
 Totais validados.
 Exportações testadas.
 Permissões validadas.
 Dados conferidos.

Status da seção: [ ]

33. Transparência
 Informações públicas identificadas.
 Dados publicáveis identificados.
 Dados restritos protegidos.
 Regras de publicação aplicadas.
 Publicação validada quando aplicável.

Deverá ser observado o princípio institucional:

Transparência por padrão, Segurança por princípio e Classificação da Informação por política.

34. Dados e LGPD
 Dados pessoais identificados.
 Finalidades identificadas.
 Acessos revisados.
 Dados sensíveis protegidos quando aplicável.
 Retenção definida quando aplicável.
 Logs não expõem dados indevidamente.
 Exportações respeitam controles de acesso.
35. Implantação

Referência:

020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md

 Plano de implantação aprovado.
 Cronograma definido.
 Equipe definida.
 Janela definida.
 Checklist de implantação preparado.
 Procedimentos executados em homologação.
 Procedimentos de produção revisados.
36. Plano de Rollback
 Plano de rollback documentado.
 Responsáveis definidos.
 Condições de acionamento definidas.
 Backup anterior disponível.
 Procedimento testado.
 Comunicação de rollback definida.
37. Comunicação
 Gestores comunicados.
 Usuários comunicados.
 Equipe técnica comunicada.
 Equipe de suporte comunicada.
 Janela de implantação comunicada.
 Possíveis indisponibilidades comunicadas.
 Canal de comunicação definido.
38. Piloto
 Escopo do piloto definido.
 Unidade piloto definida.
 Usuários piloto definidos.
 Processos piloto definidos.
 Critérios de sucesso definidos.
 Piloto executado.
 Resultados avaliados.
 Pendências do piloto tratadas.

Resultado do piloto:

[ ] Aprovado
[ ] Aprovado com ressalvas
[ ] Reprovado
39. Critérios de Go-Live

A entrada em produção somente poderá ser recomendada quando:

 requisitos críticos atendidos;
 testes críticos aprovados;
 defeitos críticos inexistentes;
 segurança validada;
 auditoria validada;
 dados validados;
 integrações críticas validadas;
 backup validado;
 rollback disponível;
 suporte disponível;
 monitoramento disponível;
 usuários preparados;
 homologação concluída;
 piloto aprovado quando aplicável.
40. Critérios de Bloqueio

A implantação deverá ser bloqueada quando existir:

 defeito crítico;
 vulnerabilidade crítica;
 perda potencial de dados;
 inconsistência grave de dados;
 falha de integração crítica;
 ausência de backup;
 ausência de rollback;
 ausência de suporte;
 ausência de autenticação;
 ausência de autorização;
 ausência de auditoria para operações críticas;
 ausência de homologação;
 risco operacional não aceito.
41. Pendências
ID	Pendência	Severidade	Responsável	Prazo	Bloqueia Produção?	Status
P-001						
P-002						
P-003						
42. Riscos Aceitos
ID	Risco	Impacto	Mitigação	Responsável	Aceite
R-001					
R-002					

Nenhum risco crítico deverá ser considerado aceito sem aprovação formal da autoridade competente.

43. Resumo de Prontidão
Área	Status
Governança	[ ]
Documentação	[ ]
Requisitos	[ ]
Rastreabilidade	[ ]
Implementação	[ ]
Banco de Dados	[ ]
Dados	[ ]
APIs	[ ]
Serviços	[ ]
Integrações	[ ]
Segurança	[ ]
Auditoria	[ ]
Testes	[ ]
Performance	[ ]
Infraestrutura	[ ]
Backup	[ ]
Recuperação	[ ]
Usuários	[ ]
Treinamento	[ ]
Suporte	[ ]
Monitoramento	[ ]
Implantação	[ ]
Rollback	[ ]
Comunicação	[ ]
Piloto	[ ]
44. Resultado Final

Status geral:

[ ] PRONTO
[ ] PRONTO COM RESSALVAS
[ ] NÃO PRONTO
[ ] BLOQUEADO

Data da avaliação: //________

Versão avaliada: ______________________

Ambiente: _____________________________

45. Aprovação para Produção
Responsável Técnico

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

Responsável Funcional

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

Responsável pela Implantação

Nome: __________________________________

Cargo/Função: __________________________

Assinatura: _____________________________

Data: //________

46. Decisão de Go-Live

Após análise do presente checklist:

[ ] AUTORIZADA A ENTRADA EM PRODUÇÃO


[ ] AUTORIZADA COM RESSALVAS


[ ] NÃO AUTORIZADA


[ ] BLOQUEADA

Justificativa:

47. Registro Pós-Go-Live

Após a entrada em produção deverão ser registrados:

data/hora da implantação;
versão implantada;
responsáveis;
duração;
incidentes;
indisponibilidades;
problemas identificados;
ações corretivas;
resultado inicial.

Data/Hora do Go-Live: __________________________

Versão: _______________________________________

Responsável: __________________________________

Resultado:

[ ] Sucesso
[ ] Sucesso com incidentes
[ ] Rollback
[ ] Implantação interrompida
48. Avaliação Pós-Implantação

Após o período inicial de operação deverá ser realizada avaliação contendo:

estabilidade;
desempenho;
utilização;
incidentes;
satisfação dos usuários;
qualidade dos dados;
integrações;
segurança;
auditoria;
pendências.

O resultado deverá alimentar o processo de melhoria contínua do domínio.

49. Controle de Versões
Versão	Data	Descrição
1.0	2026-08-13	Criação do Checklist de Prontidão para Produção do Domínio de Gestão de Compras e Contratações

Documento: 021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md

Última atualização: 2026-08-13

Responsável: Equipe SIGMUN

Status da revisão: Vigente

