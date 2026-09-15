# Evidência de Homologação — DOM-GDO (Gestão Documental)

**Domínio:** DOM-GDO — Gestão Documental
**Data:** 2026-09-06 16:31:36
**Duração:** 3.22s
**Resultado:** SUCESSO

## Verificações

| # | Verificação | Status | Detalhe |
|---|-------------|--------|---------|
| H-00 | Migrações Alembic aplicadas no head | PASS | output=INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL. |
| H-01 | GET /health responde 200 | PASS | database=up |
| H-02 | OpenAPI expõe endpoints de GDO | PASS | 17 rotas /api/v1/gdo |
| H-03 | Seed de tipos documentais carregado | PASS | 12 tipos |
| H-04 | Plano de classificação documental carregado | PASS | 9 classificações |
| H-05 | POST /documentos cria documento (201) | PASS | status=ativo |
| H-06 | RN-GDO-001: código duplicado retorna 409 | PASS | detail=Código 'HOMOLOG-56394DE1' já utilizado pelo documento 3e5c5c1b-a8c4-4f46-aa08-9ddb464b7582 |
| H-07 | RN-GDO-002: hash inválido retorna 400 | PASS | detail=Hash de integridade inválido. Deve ser SHA-256 (64 hex chars) |
| H-08 | Payload inválido retorna 422 | PASS | status=422 |
| H-09 | POST /documentos/{id}/versoes cria versão (201) | PASS | numero_versao=1 |
| H-09b | Segunda versão registrada (201) | PASS | numero_versao=2 |
| H-10 | Histórico de versões listado (>=2) | PASS | 2 versões |
| H-11 | POST /documentos/{id}/tramitar (201) | PASS | tipo=envio |
| H-12 | Tramitações do documento listadas | PASS | 1 tramitações |
| H-13 | Consulta de tabela de temporalidade (TEMP-001) | PASS | prazo=12 meses |
| H-14 | POST /documentos/{id}/assinar (201) | PASS | hash_assinatura=set |
| H-15 | POST /documentos/{id}/arquivar (201) | PASS | arquivamento_id=0dbbe992-5d13-46b4-b43b-0695a8b68151 |
| H-16 | Destinação guarda permanente aplicada (200) | PASS | status=arquivado |
| H-18 | RN-GDO-011: eliminação sem homologadora retorna 403 | PASS | detail=Eliminação requer autoridade homologadora (RN-GDO-011) |
| H-17 | Estado final do documento consistente | PASS | status=arquivado, conteudo_ref=storage://homologacao/HOMOLOG-56394DE1/v1.pdf |
| H-19 | Eliminação com homologadora aplicada (200) | PASS | status=encerrado, data_eliminacao=True |
| H-20 | Documento inexistente retorna 404 | PASS | detail=Documento não encontrado |
| H-21 | GET /documentos lista documentos criados | PASS | total=2 |

---

**Documento:** 2026-09-06-homologacao-gdo.md
**Última atualização:** 2026-09-06
**Responsável:** Equipe SIGMUN
**Status:** Concluído
