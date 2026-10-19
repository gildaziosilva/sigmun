# ADR-0009 — Encerramento da autenticação legada por headers (Fase 0)

- **Status:** Aceito
- **Data:** 2026-10-05
- **Contexto:** Até a Fase 0, `get_current_user_hybrid()` aceitava
  `X-Usuario-Id` / `X-Usuario-Papel` como identidade autenticada, e
  `require_roles_hybrid()` conferia papel a partir desses headers
  controlados pelo cliente (spoofing de papel — TODO2 T-0.1/S-01).
- **Decisão:**
  1. `require_roles_hybrid()` usa `get_current_user_jwt()` (JWT estrito);
     header legado **nunca** confere papel.
  2. O fallback de header em `get_current_user_hybrid()` /
     `get_current_user_hybrid_optional()` / `get_current_user_legacy()`
     só atua com `ALLOW_LEGACY_HEADERS=True`; o default é `False`
     (quando desligado, o fallback retorna 401/None).
  3. `SECRET_KEY` sem placeholder é obrigatória no startup
     (`settings.validar_para_startup()`); CORS usa origens explícitas
     (`*` + credenciais rejeitado); `APP_DEBUG=False` por padrão.
  4. Rate limiting (429) + limite de payload (413) via
     `RateLimitMiddleware`, com limite mais baixo em `/auth/*`.
- **Transição de testes:** `tests/conftest.py` liga a flag apenas no
  processo de teste para os testes legados pendentes de migração JWT
  (Fase 2); `tests/integration/test_fase0_seguranca.py` prova o
  comportamento seguro com a flag OFF.
- **Consequências:** clientes devem usar
  `Authorization: Bearer <access token>` (emitido por
  `POST /api/v1/idn/auth/login/jwt`). Enviar só `X-Usuario-Papel`
  resulta em 401/403.
- **Referências:** TODO2 Fase 0 (T-0.1…T-0.4, T-4.6); ADR-0007; ADR-0008.
