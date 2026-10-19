"""Regressao da Fase 0 (TODO2 T-0.1..T-0.4 + T-4.6).

Com ALLOW_LEGACY_HEADERS=False (default de producao):
- T-0.1/T-4.6: header X-Usuario-Papel SEM JWT nao confere papel (401/403);
- T-0.2: hybrid com header legado e sem JWT => 401; flag default False;
- T-0.3: CORS sem `*`+credenciais; APP_DEBUG False; startup recusa
  SECRET_KEY placeholder;
- T-0.4: rate limit responde 429 e corpo gigante responde 413.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from src.main import app
from src.shared.config.settings import Settings, settings
from src.shared.middleware.rate_limit_middleware import (
    RateLimitMiddleware,
    reset_rate_limit_state,
)
from src.shared.security.jwt import (
    create_access_token,
    get_current_user_hybrid,
    get_current_user_jwt,
    require_roles_hybrid,
)


@pytest.fixture()
def flag_legada_off():
    """Garante ALLOW_LEGACY_HEADERS=False durante o teste (default seguro)."""
    anterior = settings.ALLOW_LEGACY_HEADERS
    settings.ALLOW_LEGACY_HEADERS = False
    try:
        yield
    finally:
        settings.ALLOW_LEGACY_HEADERS = anterior


def _mini_app() -> FastAPI:
    mini = FastAPI()
    exigir = require_roles_hybrid("ouvidor")

    @mini.get("/protegida")
    def protegida(user=Depends(exigir)):
        return {"ok": True}

    @mini.get("/identidade")
    def identidade(user=Depends(get_current_user_hybrid)):
        return {"usuario": str(user.usuario_id)}

    return mini


class TestFlagDefault:
    def test_flag_legada_desligada_por_padrao(self):
        assert Settings.model_fields["ALLOW_LEGACY_HEADERS"].default is False


class TestSpoofingDePapel:
    """T-0.1 + T-4.6: header forjado nao abre rota protegida por papel."""

    def test_header_papel_sem_jwt_nao_autoriza(self, flag_legada_off):
        uid = uuid4()
        resposta = TestClient(_mini_app()).get(
            "/protegida",
            headers={"X-Usuario-Id": str(uid), "X-Usuario-Papel": "ouvidor"},
        )
        assert resposta.status_code in (401, 403)

    def test_header_papel_sozinho_nao_autoriza(self, flag_legada_off):
        resposta = TestClient(_mini_app()).get("/protegida", headers={"X-Usuario-Papel": "ouvidor"})
        assert resposta.status_code in (401, 403)

    def test_require_roles_nao_usa_fallback_hibrido(self):
        import inspect

        fonte = inspect.getsource(require_roles_hybrid)
        assert "get_current_user_hybrid" not in fonte

    def test_jwt_valido_com_papel_acessa(self, flag_legada_off):
        token = create_access_token(usuario_id=uuid4(), login="ouvidor.teste", roles=["ouvidor"])
        resposta = TestClient(_mini_app()).get(
            "/protegida", headers={"Authorization": f"Bearer {token}"}
        )
        assert resposta.status_code == 200

    def test_jwt_valido_sem_papel_recebe_403(self, flag_legada_off):
        token = create_access_token(usuario_id=uuid4(), login="sem.papel", roles=["compras"])
        resposta = TestClient(_mini_app()).get(
            "/protegida", headers={"Authorization": f"Bearer {token}"}
        )
        assert resposta.status_code == 403

    def test_spoof_tambem_falha_na_rota_real_ouvidoria(self, flag_legada_off):
        with TestClient(app, raise_server_exceptions=False) as cliente:
            resposta = cliente.get(
                "/api/v1/ouv/estatisticas",
                headers={
                    "X-Usuario-Id": str(uuid4()),
                    "X-Usuario-Papel": "ouvidor",
                },
            )
        assert resposta.status_code in (401, 403)


class TestFallbackHibridoFechado:
    """T-0.2: sem JWT e sem flag, identidade legada => 401."""

    def test_hybrid_sem_jwt_retorna_401(self, flag_legada_off):
        resposta = TestClient(_mini_app()).get(
            "/identidade", headers={"X-Usuario-Id": str(uuid4())}
        )
        assert resposta.status_code == 401

    def test_jwt_direto_nunca_aceita_header(self):
        uid = uuid4()
        mini = FastAPI()

        @mini.get("/jwt")
        def jwt(user=Depends(get_current_user_jwt)):
            return {"usuario": str(user.usuario_id)}

        resposta = TestClient(mini).get("/jwt", headers={"X-Usuario-Id": str(uid)})
        assert resposta.status_code == 401


class TestStartupSeguro:
    """T-0.3: SECRET_KEY obrigatoria; CORS fechado; APP_DEBUG False."""

    def test_startup_recusa_placeholder(self):
        import pydantic

        with pytest.raises((RuntimeError, pydantic.ValidationError), match="SECRET_KEY"):
            Settings(SECRET_KEY="change-this-in-production").validar_para_startup()

    def test_startup_recusa_chave_curta_em_producao(self):
        import pydantic

        with pytest.raises((RuntimeError, pydantic.ValidationError), match="SECRET_KEY"):
            Settings(SECRET_KEY="curta", APP_ENV="production").validar_para_startup()

    def test_startup_recusa_wildcard_em_producao(self):
        import pydantic

        with pytest.raises((RuntimeError, pydantic.ValidationError), match="ALLOWED_HOSTS"):
            Settings(
                SECRET_KEY="x" * 40, APP_ENV="production", ALLOWED_HOSTS=["*"]
            ).validar_para_startup()

    def test_cors_sem_credencial_com_wildcard(self):
        middlewares = list(app.user_middleware)
        cors = next(m for m in middlewares if "CORSMiddleware" in str(m.cls))
        opcoes = cors.kwargs
        if "*" in opcoes.get("allow_origins", []):
            assert opcoes.get("allow_credentials") is not True
        assert "*" not in opcoes.get("allow_methods", [])

    def test_app_debug_default_false(self):
        # O default do campo e False; o .env local pode ligar p/ dev.
        assert Settings.model_fields["APP_DEBUG"].default is False


class TestRateLimitEPayload:
    """T-0.4: 429 sob rajada e 413 para corpo gigante."""

    def test_rajada_no_login_retorna_429(self, monkeypatch):
        monkeypatch.setattr(settings, "RATE_LIMIT_ENABLED", True)
        monkeypatch.setattr(settings, "RATE_LIMIT_AUTH_PER_MINUTE", 2)
        monkeypatch.setattr(settings, "APP_ENV", "production")
        monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
        reset_rate_limit_state()
        mini = FastAPI()
        mini.add_middleware(RateLimitMiddleware)

        @mini.post("/api/v1/idn/auth/login/jwt")
        def login():
            return {"ok": True}

        cliente = TestClient(mini, raise_server_exceptions=False)
        assert cliente.post("/api/v1/idn/auth/login/jwt").status_code == 200
        assert cliente.post("/api/v1/idn/auth/login/jwt").status_code == 200
        assert cliente.post("/api/v1/idn/auth/login/jwt").status_code == 429

    def test_corpo_gigante_retorna_413(self, monkeypatch):
        monkeypatch.setattr(settings, "RATE_LIMIT_ENABLED", True)
        monkeypatch.setattr(settings, "MAX_REQUEST_BODY_BYTES", 10)
        monkeypatch.setattr(settings, "APP_ENV", "production")
        monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
        reset_rate_limit_state()
        mini = FastAPI()
        mini.add_middleware(RateLimitMiddleware)

        @mini.post("/eco")
        def eco(payload: dict):
            return payload

        resposta = TestClient(mini, raise_server_exceptions=False).post(
            "/eco", json={"dado": "x" * 100}
        )
        assert resposta.status_code == 413
