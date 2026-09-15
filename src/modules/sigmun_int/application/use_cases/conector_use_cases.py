"""Casos de uso de conectores oficiais de interoperabilidade (DOM-INT).

Gerenciam os conectores com as plataformas externas exigidas pela
normativa: GOV.BR, e-Social, SIAFIC e PNCP. Os `CONECTORES_OFICIAIS`
constituem a referência canônica que o seed usa para pré-carregar o schema.
"""

from datetime import datetime

from ...application.interfaces import RepositorioConector
from ...domain.entities import Conector, EstadoConector
from ...domain.exceptions import (
    ConectorJaExisteError,
    ConectorNaoEncontradoError,
    OperacaoNaoPermitidaError,
)
from ...domain.value_objects import validar_codigo, validar_url_http

__all__ = [
    "CONECTORES_OFICIAIS",
    "CODIGOS_CONECTORES_OFICIAIS",
    "CriarConectorUseCase",
    "BuscarConectorUseCase",
    "AtualizarConectorUseCase",
    "MudarEstadoConectorUseCase",
    "DeletarConectorUseCase",
]

CONECTORES_OFICIAIS: list[dict] = [
    {
        "codigo": "GOVBR",
        "nome": "Plataforma Digital GOV.BR",
        "descricao": (
            "Interoperabilidade com a Plataforma Digital Nacional (SSO e serviços digitais)."
        ),
        "provedor": "Presidência da República",
        "url_base": "https://api.brasil.gov.br",
        "autenticacao_tipo": "oauth2",
        "config": {"ambiente": "producao", "credencial_ref": "GOVBR_CLIENT_SECRET"},
    },
    {
        "codigo": "ESOCIAL",
        "nome": "e-Social",
        "descricao": (
            "Envio de eventos de folha de pagamento, previdência social e relações trabalhistas."
        ),
        "provedor": "e-Social Brasil",
        "url_base": "https://sgc.e-social.gov.br",
        "autenticacao_tipo": "mtls",
        "config": {
            "ambiente": "producao",
            "certificado_ref": "ESOCIAL_CERTIFICADO",
            "empresa_id": "",
        },
    },
    {
        "codigo": "SIAFIC",
        "nome": "SIAFIC (Sistema Integrado de Administração Financeira e Controle)",
        "descricao": "Envio de informações financeiras, fiscais e contábeis (Decreto 407/2020).",
        "provedor": "Ministério da Fazenda",
        "url_base": "https://siafic.economia.gov.br",
        "autenticacao_tipo": "oauth2",
        "config": {
            "ambiente": "producao",
            "credencial_ref": "SIAFIC_CLIENT_SECRET",
            "periodo_ativo": "",
        },
    },
    {
        "codigo": "PNCP",
        "nome": "PNCP (Plataforma Nacional de Contratações Públicas)",
        "descricao": "Publicação de licitações, contratos e fornecedores.",
        "provedor": "Plataforma Nacional de Contratações Públicas",
        "url_base": "https://api.contratacoespublicas.gov.br",
        "autenticacao_tipo": "api_key",
        "config": {"ambiente": "producao", "credencial_ref": "PNCP_API_KEY", "organizacao_id": ""},
    },
]

CODIGOS_CONECTORES_OFICIAIS: list[str] = [c["codigo"] for c in CONECTORES_OFICIAIS]


class CriarConectorUseCase:
    """Registra um conector oficial de interoperabilidade."""

    def __init__(self, repo: RepositorioConector) -> None:
        self._repo = repo

    def execute(
        self,
        codigo: str,
        nome: str = "",
        descricao: str = "",
        provedor: str = "",
        url_base: str = "",
        autenticacao_tipo: str = "oauth2",
        config: dict | None = None,
    ) -> Conector:
        """Cria o conector; se o código é oficial, completa dados padrão."""
        valido, msg = validar_codigo(codigo)
        if not valido:
            raise ValueError(msg)
        codigo_upper = codigo.upper()
        if self._repo.exists_by_codigo(codigo_upper):
            raise ConectorJaExisteError(f"Já existe um conector com código '{codigo_upper}'")
        if url_base:
            valido, msg = validar_url_http(url_base)
            if not valido:
                raise ValueError(msg)

        # Completar dados dos conectores oficiais
        oficial = next((c for c in CONECTORES_OFICIAIS if c["codigo"] == codigo_upper), None)
        if oficial:
            nome = nome or oficial["nome"]
            descricao = descricao or oficial["descricao"]
            provedor = provedor or oficial["provedor"]
            url_base = url_base or oficial["url_base"]
            autenticacao_tipo = oficial["autenticacao_tipo"]
            config = {**oficial.get("config", {}), **(config or {})}

        conector = Conector(
            codigo=codigo_upper,
            nome=nome,
            descricao=descricao,
            provedor=provedor,
            url_base=url_base,
            autenticacao_tipo=autenticacao_tipo,
            config=config or {},
        )
        return self._repo.save(conector)


class BuscarConectorUseCase:
    """Consulta de conectores oficiais."""

    def __init__(self, repo: RepositorioConector) -> None:
        self._repo = repo

    def get_by_id(self, conector_id: str) -> Conector:
        conector = self._repo.get_by_id(conector_id)
        if conector is None:
            raise ConectorNaoEncontradoError(f"Conector '{conector_id}' não encontrado")
        return conector

    def get_by_codigo(self, codigo: str) -> Conector | None:
        return self._repo.get_by_codigo(codigo)

    def list_all(
        self, page: int = 0, page_size: int = 50, estado: str | None = None
    ) -> tuple[list[Conector], int]:
        return self._repo.list_all(page, page_size, estado)


class AtualizarConectorUseCase:
    """Atualiza a configuração de um conector (merge do dict config)."""

    def __init__(self, repo: RepositorioConector) -> None:
        self._repo = repo

    def execute(
        self,
        conector_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        provedor: str | None = None,
        url_base: str | None = None,
        autenticacao_tipo: str | None = None,
        config: dict | None = None,
    ) -> Conector:
        conector = self._repo.get_by_id(conector_id)
        if conector is None:
            raise ConectorNaoEncontradoError(f"Conector '{conector_id}' não encontrado")

        if nome is not None:
            conector.nome = nome
        if descricao is not None:
            conector.descricao = descricao
        if provedor is not None:
            conector.provedor = provedor
        if url_base is not None:
            valido, msg = validar_url_http(url_base)
            if not valido:
                raise ValueError(msg)
            conector.url_base = url_base
        if autenticacao_tipo is not None:
            conector.autenticacao_tipo = autenticacao_tipo
        if config is not None:
            conector.config = {**conector.config, **config}

        conector.atualizado_em = datetime.utcnow()
        return self._repo.save(conector)


class MudarEstadoConectorUseCase:
    """Transiciona o estado de configuração do conector.

    RN-INT-004: para passar a `ativo` o conector deve ter configuração
    (não pode ativar um conector `sem_configuracao`).
    """

    def __init__(self, repo: RepositorioConector) -> None:
        self._repo = repo

    def execute(self, conector_id: str, estado: str) -> Conector:
        conector = self._repo.get_by_id(conector_id)
        if conector is None:
            raise ConectorNaoEncontradoError(f"Conector '{conector_id}' não encontrado")

        novo_estado = EstadoConector(estado)
        if novo_estado is EstadoConector.ATIVO and not conector.config:
            raise OperacaoNaoPermitidaError(
                "Não pode ativar um conector sem configuração (RN-INT-004)"
            )
        conector.estado = novo_estado
        conector.atualizado_em = datetime.utcnow()
        return self._repo.save(conector)


class DeletarConectorUseCase:
    """Exclui (exclusão lógica) um conector."""

    def __init__(self, repo: RepositorioConector) -> None:
        self._repo = repo

    def execute(self, conector_id: str) -> bool:
        conector = self._repo.get_by_id(conector_id)
        if conector is None:
            raise ConectorNaoEncontradoError(f"Conector '{conector_id}' não encontrado")
        return self._repo.delete(conector_id)
