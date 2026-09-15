"""Value Objects do domínio de Integração e Interoperabilidade (DOM-INT).

Incluem a política de retries (backoff exponencial) e validadores
compartilhados de códigos e URLs dos contratos de integração.
"""

from __future__ import annotations

import re

__all__ = ["PoliticaRetry", "validar_codigo", "validar_url_http", "validar_topicos"]

_URL_HTTP_RE = re.compile(r"^https?://[^\s]+$")
_CODIGO_RE = re.compile(r"^[A-Z0-9][A-Z0-9_\-]{1,49}$")


class PoliticaRetry:
    """Política de retries com backoff exponencial para entregas de webhooks.

    Atraso em segundos para a tentativa ``n`` (1-based)::

        atraso(n) = backoff_base_seg * backoff_multiplier ** (n - 1)
    """

    def __init__(
        self,
        max_tentativas: int = 5,
        backoff_base_seg: int = 60,
        backoff_multiplier: float = 2.0,
    ) -> None:
        if max_tentativas < 1:
            raise ValueError("max_tentativas deve ser pelo menos 1")
        if backoff_base_seg < 0:
            raise ValueError("backoff_base_seg não pode ser negativo")
        if backoff_multiplier < 1.0:
            raise ValueError("backoff_multiplier deve ser >= 1.0")
        self.max_tentativas = max_tentativas
        self.backoff_base_seg = backoff_base_seg
        self.backoff_multiplier = backoff_multiplier

    def atraso_para(self, tentativa: int) -> int:
        """Atraso (segundos) para a tentativa informada (1-based)."""
        if tentativa < 1:
            return 0
        return int(self.backoff_base_seg * (self.backoff_multiplier ** (tentativa - 1)))


def validar_codigo(codigo: str) -> tuple[bool, str]:
    """Valida o formato corporativo de códigos de catálogo (ex.: GOVBR, API-01)."""
    if not codigo:
        return False, "O código não pode estar vazio"
    if not _CODIGO_RE.match(codigo):
        return False, "O código só aceita maiúsculas, números, hífens e deve ter 2-50 caracteres"
    return True, ""


def validar_url_http(url: str) -> tuple[bool, str]:
    """Valida se a URL destino usa HTTP/HTTPS (protocolo seguro obrigatório)."""
    if not url:
        return False, "A URL não pode estar vazia"
    if not _URL_HTTP_RE.match(url.strip()):
        return False, "A URL deve ser absoluta e usar esquema http:// ou https://"
    return True, ""


def validar_topicos(topicos: list[str]) -> tuple[bool, str]:
    """Valida a lista de tópicos de inscrição de um webhook."""
    if not topicos:
        return False, "Deve indicar pelo menos um tópico (ou '*' para todos)"
    if "*" in topicos and len(topicos) > 1:
        return False, "O curinga '*' não pode ser combinado com outros tópicos"
    for topico in topicos:
        if not topico or len(topico) > 200:
            return False, "Tópico inválido: deve ter entre 1 e 200 caracteres"
    return True, ""
