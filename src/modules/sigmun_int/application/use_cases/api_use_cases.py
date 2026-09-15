"""Casos de uso do catálogo de APIs externas (DOM-INT).

Responsáveis pelo registro, consulta, atualização, mudança de estado e exclusão
lógica das APIs externas do catálogo corporativo de interoperabilidade.
"""

from datetime import datetime

from ...application.interfaces import RepositorioApiExterna
from ...domain.entities import ApiExterna, AutenticacaoApi, EstadoApi, TipoApi
from ...domain.exceptions import ApiExternaJaExisteError, ApiExternaNaoEncontradaError
from ...domain.value_objects import validar_codigo, validar_url_http

__all__ = [
    "CriarApiExternaUseCase",
    "BuscarApiExternaUseCase",
    "AtualizarApiExternaUseCase",
    "MudarEstadoApiUseCase",
    "DeletarApiExternaUseCase",
]


class CriarApiExternaUseCase:
    """Registra uma nova API externa no catálogo."""

    def __init__(self, repo: RepositorioApiExterna) -> None:
        self._repo = repo

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        provedor: str = "",
        url_base: str = "",
        tipo: str = "rest",
        autenticacao: str = "oauth2",
        estado: str = "rascunho",
        versao: str = "1.0",
        limite_por_minuto: int = 300,
        timeout_seg: int = 30,
    ) -> ApiExterna:
        """Cria a API externa validando código, URL e unicidade."""
        valido, msg = validar_codigo(codigo)
        if not valido:
            raise ValueError(msg)
        if url_base:
            valido, msg = validar_url_http(url_base)
            if not valido:
                raise ValueError(msg)
        if self._repo.exists_by_codigo(codigo):
            raise ApiExternaJaExisteError(f"Já existe uma API externa com código '{codigo}'")

        api = ApiExterna(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            provedor=provedor,
            url_base=url_base,
            tipo=TipoApi(tipo),
            autenticacao=AutenticacaoApi(autenticacao),
            estado=EstadoApi(estado),
            versao=versao,
            limite_por_minuto=limite_por_minuto,
            timeout_seg=timeout_seg,
        )
        return self._repo.save(api)


class BuscarApiExternaUseCase:
    """Consulta do catálogo de APIs externas."""

    def __init__(self, repo: RepositorioApiExterna) -> None:
        self._repo = repo

    def get_by_id(self, api_id: str) -> ApiExterna:
        api = self._repo.get_by_id(api_id)
        if api is None:
            raise ApiExternaNaoEncontradaError(f"API externa '{api_id}' não encontrada")
        return api

    def get_by_codigo(self, codigo: str) -> ApiExterna | None:
        return self._repo.get_by_codigo(codigo)

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        tipo: str | None = None,
    ) -> tuple[list[ApiExterna], int]:
        return self._repo.list_all(page, page_size, estado, tipo)


class AtualizarApiExternaUseCase:
    """Atualiza os dados de uma API externa (atualização parcial)."""

    def __init__(self, repo: RepositorioApiExterna) -> None:
        self._repo = repo

    def execute(
        self,
        api_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        provedor: str | None = None,
        url_base: str | None = None,
        tipo: str | None = None,
        autenticacao: str | None = None,
        versao: str | None = None,
        limite_por_minuto: int | None = None,
        timeout_seg: int | None = None,
    ) -> ApiExterna:
        api = self._repo.get_by_id(api_id)
        if api is None:
            raise ApiExternaNaoEncontradaError(f"API externa '{api_id}' não encontrada")

        if nome is not None:
            api.nome = nome
        if descricao is not None:
            api.descricao = descricao
        if provedor is not None:
            api.provedor = provedor
        if url_base is not None:
            valido, msg = validar_url_http(url_base)
            if not valido:
                raise ValueError(msg)
            api.url_base = url_base
        if tipo is not None:
            api.tipo = TipoApi(tipo)
        if autenticacao is not None:
            api.autenticacao = AutenticacaoApi(autenticacao)
        if versao is not None:
            api.versao = versao
        if limite_por_minuto is not None:
            api.limite_por_minuto = limite_por_minuto
        if timeout_seg is not None:
            api.timeout_seg = timeout_seg

        api.atualizado_em = datetime.utcnow()
        return self._repo.save(api)


class MudarEstadoApiUseCase:
    """Transiciona uma API entre os estados do ciclo de vida."""

    def __init__(self, repo: RepositorioApiExterna) -> None:
        self._repo = repo

    def execute(self, api_id: str, estado: str) -> ApiExterna:
        api = self._repo.get_by_id(api_id)
        if api is None:
            raise ApiExternaNaoEncontradaError(f"API externa '{api_id}' não encontrada")
        api.estado = EstadoApi(estado)
        api.atualizado_em = datetime.utcnow()
        return self._repo.save(api)


class DeletarApiExternaUseCase:
    """Exclui (exclusão lógica) uma API externa do catálogo."""

    def __init__(self, repo: RepositorioApiExterna) -> None:
        self._repo = repo

    def execute(self, api_id: str) -> bool:
        api = self._repo.get_by_id(api_id)
        if api is None:
            raise ApiExternaNaoEncontradaError(f"API externa '{api_id}' não encontrada")
        return self._repo.delete(api_id)
