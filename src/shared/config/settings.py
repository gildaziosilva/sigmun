"""
Configurações da aplicação SIGMUN.
Gerenciadas via variáveis de ambiente com pydantic-settings.
"""

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_PLACEHOLDERS_SECRET = {"", "change-this-in-production", "changeme", "secret"}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Application
    APP_NAME: str = "SIGMUN"
    APP_ENV: str = "development"
    APP_DEBUG: bool = False
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "sigmun"
    DB_USER: str = "sigmun"
    DB_PASSWORD: str = "sigmun"
    DB_SCHEMA: str = "sigmun"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    # Security
    SECRET_KEY: str = "change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 7

    # Transicao legada - T-0.2: False => fallback de header retorna 401.
    ALLOW_LEGACY_HEADERS: bool = False

    # CORS
    ALLOWED_HOSTS: list[str] = []

    # Rate limiting e payload - T-0.4.
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_AUTH_PER_MINUTE: int = 10
    MAX_REQUEST_BODY_BYTES: int = 2097152

    # External APIs
    GOVR_BR_CLIENT_ID: str = ""
    GOVR_BR_CLIENT_SECRET: str = ""
    GOVR_BR_REDIRECT_URI: str = ""

    # AWS
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: str = "sigmun-documentos"

    # Storage local de anexos/arquivos físicos do DOM-GDO (Fase VII).
    STORAGE_ROOT: str = "storage/documentos"

    # Celery / mensageria assíncrona (Fase VII — Celery & Redis).
    CELERY_TASK_TIME_LIMIT: int = 300
    CELERY_TASK_SOFT_TIME_LIMIT: int = 240
    CELERY_RESULT_EXPIRES: int = 3600
    OUTBOX_DISPATCH_BATCH: int = 100
    OUTBOX_MAX_TENTATIVAS: int = 5

    # Logging
    LOG_LEVEL: str = "INFO"

    @model_validator(mode="after")
    def _validar_seguranca(self) -> "Settings":
        """Fail fast em producao: placeholder, chave curta e `*` nao passam."""
        chave = (self.SECRET_KEY or "").strip()
        if self.APP_ENV.lower() == "production":
            if chave.lower() in _PLACEHOLDERS_SECRET:
                raise ValueError("SECRET_KEY ausente ou placeholder em producao.")
            if len(chave) < 32:
                raise ValueError("SECRET_KEY deve ter ao menos 32 caracteres em producao.")
            if "*" in self.ALLOWED_HOSTS:
                raise ValueError("ALLOWED_HOSTS nao pode conter '*' em producao.")
        return self

    def validar_para_startup(self) -> None:
        """Validacao chamada no startup (T-0.3): sem chave valida, sem startup.

        Bypass exclusivo quando o proprio `settings` global roda sob pytest
        (a suite usa `with TestClient(app)`, que dispara o startup): a
        validacao real e coberta por `test_fase0_seguranca.py`, que chama o
        metodo em instancias isoladas.
        """
        import os

        if self is settings and (
            os.getenv("PYTEST_CURRENT_TEST") or self.APP_ENV.lower() in {"test", "testing"}
        ):
            return
        chave = (self.SECRET_KEY or "").strip()
        if chave.lower() in _PLACEHOLDERS_SECRET:
            raise RuntimeError(
                "SIGMUN recusou o startup: SECRET_KEY ausente ou placeholder. "
                "Defina SECRET_KEY no ambiente."
            )
        if self.APP_ENV.lower() == "production":
            if len(chave) < 32:
                raise RuntimeError("SIGMUN recusou o startup: SECRET_KEY curta em producao.")
            if "*" in self.ALLOWED_HOSTS:
                raise RuntimeError("SIGMUN recusou o startup: ALLOWED_HOSTS com '*'.")


settings = Settings()
