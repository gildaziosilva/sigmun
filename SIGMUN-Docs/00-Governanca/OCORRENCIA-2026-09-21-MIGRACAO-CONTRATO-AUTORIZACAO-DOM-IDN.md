# OCORRÊNCIA — MIGRAÇÃO DO CONTRATO DE AUTORIZAÇÃO DO DOM-IDN

**Código:** OCORRÊNCIA-2026-09-21-DOM-IDN-AUTORIZAÇÃO
**Domínio:** DOM-IDN — Identidade e Acesso
**Data:** 2026-09-21
**Responsável:** Gildazio
**Status:** Concluída
**Classificação da Informação:** Pública
**Status da revisão:** Vigente

## 1. Objetivo

Registrar a alteração do contrato de persistência da autorização do DOM-IDN, especificamente da relação entre usuários e roles, substituindo a persistência física legada em idn.usuarios.roles_ids pela estrutura normalizada idn.usuario_roles.

A alteração preserva o contrato de domínio e API existente, evitando mudança desnecessária na representação utilizada pelas camadas superiores da aplicação.

## 2. Situação anterior

A tabela idn.usuarios possuía a coluna legada:

roles_ids

A coluna armazenava a identificação das roles associadas ao usuário diretamente no registro do usuário.

Paralelamente, o banco de dados já possuía a estrutura normalizada:

idn.usuario_roles

responsável pela relação N:N entre usuários e roles.

Essa duplicidade representava duas possíveis fontes físicas para a mesma informação e exigia uma definição explícita de autoridade para a persistência.

## 3. Situação adotada

Foi estabelecido o seguinte contrato:

API / Use Case
      ↓
Usuario
      ↓
UsuarioRepository
      ↓
idn.usuario_roles
      ↓
Role
      ↓
idn.role_permissoes
      ↓
Permissao

A partir desta alteração:

idn.usuario_roles é a fonte física oficial da associação usuário ↔ role.

A propriedade:

Usuario.roles_ids

permanece no domínio e no contrato da API como representação dos identificadores das roles associadas ao usuário.

Portanto, a remoção da coluna física idn.usuarios.roles_ids não representa a remoção do contrato roles_ids da aplicação.

## 4. Alterações realizadas
4.1 Modelo ORM

A propriedade física roles_ids foi removida de UsuarioModel.

Permanece o modelo:

UsuarioRoleModel

representando a tabela:

idn.usuario_roles
4.2 Repositório de usuários

SqlAlchemyUsuarioRepository foi adaptado para:

consultar as roles através de idn.usuario_roles;
converter a associação normalizada para Usuario.roles_ids ao reconstruir a entidade;
adicionar novas associações usuário ↔ role;
remover associações que deixaram de existir;
preservar a representação roles_ids na entidade de domínio;
deixar de gravar roles_ids diretamente em idn.usuarios.

A sincronização passou a ocorrer sobre a relação N.

4.3 Migração dos dados existentes

Foi utilizada a migração:

e03b4a941f40_data_migra_roles_ids_para_usuario_roles.py

para transferir as associações existentes da representação legada para idn.usuario_roles.

A auditoria realizada antes da remoção da coluna confirmou equivalência entre os dados legados e normalizados.

Resultado:

demo.compras.operador
role_legado       = 04d7c3b8-dc6e-4ae6-a550-fe63ebfa57fd
role_normalizado  = 04d7c3b8-dc6e-4ae6-a550-fe63ebfa57fd
resultado         = EQUIVALENTE

A verificação inversa também não encontrou divergências.

4.4 Remoção da estrutura legada

Foi criada a migração:

28cda5671e8b_idn_remove_coluna_legada_roles_ids.py

responsável pela remoção da coluna:

idn.usuarios.roles_ids

A migração foi aplicada com sucesso.

Estado final:

Alembic:
28cda5671e8b (head)

idn.usuarios.roles_ids:
não existe
## 5. Contrato preservado

A alteração não removeu roles_ids das camadas de domínio e apresentação.

Continuam válidos:

Usuario.roles_ids
UsuarioCreateRequest.roles_ids
UsuarioResponse.roles_ids
CriarUsuarioUseCase(... roles_ids ...)
AutorizacaoService

A decisão foi manter o contrato externo enquanto se normaliza a persistência interna.

Isso reduz impacto sobre consumidores da API e sobre as regras de autorização existentes.

6. Normalização de PermissaoEscopo

Durante a validação do contrato de autorização foi identificada uma divergência entre a representação do escopo no domínio e sua representação física no banco.

## 6. Normalização de `PermissaoEscopo`

Domínio:

global
dominio
unidade
proprio

Banco:

GLOBAL
DOMINIO
UNIDADE
PROPRIO

Os repositórios foram ajustados para realizar explicitamente a conversão:

Banco → domínio:
lower()

Domínio → banco:
upper()

Dessa forma, o contrato do domínio permanece coerente com o Enum PermissaoEscopo, enquanto a restrição física existente no banco continua sendo respeitada.

## 7. Seed DEMO de autorização

Também foi incorporado um seed técnico para validação do RBAC do DOM-IDN.

Arquivos:

scripts/seed_idn.py
src/modules/sigmun_idn/infrastructure/database/seeds.py

O seed contém exclusivamente dados demonstrativos de autorização relacionados a Compras.

Foram definidos:

12 permissões DEMO
3 roles DEMO
23 associações role-permissão

Roles:

ROLE_DEMO_COMPRAS_CONSULTA
ROLE_DEMO_COMPRAS_OPERADOR
ROLE_DEMO_COMPRAS_GESTOR

O seed:

é idempotente;
não cria usuários;
não cria sessões;
não cria registros de auditoria de login;
não executa automaticamente no startup da API;
permite execução com --dry-run;
utiliza codigo como chave natural;
adiciona somente associações inexistentes.

Os dados são explicitamente classificados como demonstrativos e não constituem catálogo institucional oficial do SIGMUN.

## 8. Validações realizadas
8.1 Testes específicos do DOM-IDN

Resultado:

20 passed
5 warnings
8.2 Suíte completa

Resultado:

807 passed
5 warnings

Os warnings correspondem a avisos de depreciação relacionados ao httpx/TestClient e ao mecanismo on_event do FastAPI, não sendo introduzidos por esta alteração.

8.3 Validação estrutural

Confirmado:

idn.usuarios.roles_ids
→ inexistente

idn.usuario_roles
→ existente e utilizada como fonte física da associação
8.4 Validação das roles DEMO

Confirmado:

ROLE_DEMO_COMPRAS_CONSULTA → 3 permissões
ROLE_DEMO_COMPRAS_OPERADOR → 8 permissões
ROLE_DEMO_COMPRAS_GESTOR   → 12 permissões

Total:

23 associações

Nenhuma associação duplicada foi encontrada.

## 9. Rastreabilidade dos commits

A implementação foi dividida em três commits independentes:

9.1 Normalização da persistência de roles
07f783b refactor(DOM-IDN): normaliza persistência de roles em usuario_roles

Responsável por:

alteração do modelo ORM;
normalização do repositório de usuários;
migração dos dados;
remoção da coluna física legada;
testes de integração e autorização.
9.2 Normalização do escopo de permissão
f249610 fix(DOM-IDN): normaliza persistência do escopo de permissao

Responsável por:

conversão banco → domínio;
conversão domínio → banco;
compatibilização com PermissaoEscopo.
9.3 Seed DEMO de autorização
0dad5a1 feat(DOM-IDN): adiciona seed DEMO de autorizacao

Responsável por:

catálogo técnico DEMO de permissões;
roles DEMO;
associações role-permissão;
script de execução do seed.
## 10. Estado final

O contrato de autorização do DOM-IDN encontra-se tecnicamente normalizado.

A arquitetura vigente passa a ser:

                    DOM-IDN
                       │
              ┌────────┴────────┐
              │                 │
          Usuário             Role
              │                 │
              └───────┬─────────┘
                      │
               usuario_roles
                      │
                   Role
                      │
               role_permissoes
                      │
                 Permissao

A regra de autoridade física é:

idn.usuario_roles
        ↓
fonte oficial da associação usuário ↔ role

Enquanto:

Usuario.roles_ids
        ↓
representação do contrato de domínio/API
## 11. Resultado da ocorrência

Ocorrência concluída.

A persistência legada foi removida sem alteração indevida do contrato de domínio/API.

Foram confirmados:

migração dos dados existentes;
ausência de divergências entre legado e normalizado;
remoção física de idn.usuarios.roles_ids;
persistência normalizada em idn.usuario_roles;
compatibilidade do PermissaoEscopo;
funcionamento do RBAC DEMO;
idempotência do seed;
aprovação da suíte completa de testes.
## 12. Próxima ação de governança

Após o registro desta ocorrência, realizar a verificação final do repositório e publicar os commits pendentes no repositório remoto origin/main.

Antes do push, devem ser confirmados:

git status --short
git diff --check origin/main..main
git log --oneline origin/main..main

Nenhuma alteração adicional de código está prevista como parte desta ocorrência.

**Responsável:** Gildazio
**Status:** Concluída
**Classificação da Informação:** Pública
**Status da revisão:** Vigente