"""Casos de uso de contratos de integração (DOM-INT).

Gestão do ciclo de vida dos contratos que definem formato, versão e
esquema das mensagens trocadas com as APIs do catálogo.
"""

from datetime import datetime

from ...application.interfaces import RepositorioApiExterna, RepositorioContratoIntegracao
from ...domain.entities import ContratoIntegracao, EstadoContrato
from ...domain.exceptions import (
    ApiExternaNaoEncontradaError,
    ContratoIntegracaoJaExisteError,
    ContratoIntegracaoNaoEncontradoError,
)
from ...domain.value_objects import validar_codigo

__all__ = [
    "CriarContratoIntegracaoUseCase",
    "BuscarContratoIntegracaoUseCase",
    "AtualizarContratoIntegracaoUseCase",
    "AprovarContratoIntegracaoUseCase",
    "RetirarContratoIntegracaoUseCase",
    "DeletarContratoIntegracaoUseCase",
]


class CriarContratoIntegracaoUseCase:
    """Cria um contrato de integração para uma API do catálogo."""

    def __init__(
        self,
        repo: RepositorioContratoIntegracao,
        repo_apis: RepositorioApiExterna,
    ) -> None:
        self._repo = repo
        self._repo_apis = repo_apis

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        versao_formato: str = "1.0",
        esquema_ref: str = "",
        api_externa_id: str = "",
        estado: str = "rascunho",
    ) -> ContratoIntegracao:
        """Cria o contrato validando código, API referenciada e unicidade."""
        valido, msg = validar_codigo(codigo)
        if not valido:
            raise ValueError(msg)
        if self._repo.exists_by_codigo(codigo):
            raise ContratoIntegracaoJaExisteError(
                f"Já existe um contrato de integração com código '{codigo}'"
            )
        # RN-INT-002: o contrato deve referenciar uma API existente do catálogo
        if api_externa_id and self._repo_apis.get_by_id(api_externa_id) is None:
            raise ApiExternaNaoEncontradaError(
                f"API externa '{api_externa_id}' não encontrada no catálogo"
            )

        contrato = ContratoIntegracao(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            versao_formato=versao_formato,
            esquema_ref=esquema_ref,
            api_externa_id=api_externa_id,
            estado=EstadoContrato(estado),
        )
        return self._repo.save(contrato)


class BuscarContratoIntegracaoUseCase:
    """Consulta de contratos de integração."""

    def __init__(self, repo: RepositorioContratoIntegracao) -> None:
        self._repo = repo

    def get_by_id(self, contrato_id: str) -> ContratoIntegracao:
        contrato = self._repo.get_by_id(contrato_id)
        if contrato is None:
            raise ContratoIntegracaoNaoEncontradoError(
                f"Contrato de integração '{contrato_id}' não encontrado"
            )
        return contrato

    def get_by_codigo(self, codigo: str) -> ContratoIntegracao | None:
        return self._repo.get_by_codigo(codigo)

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        estado: str | None = None,
        api_externa_id: str | None = None,
    ) -> tuple[list[ContratoIntegracao], int]:
        return self._repo.list_all(page, page_size, estado, api_externa_id)


class AprovarContratoIntegracaoUseCase:
    """Aprova um contrato (rascunho -> vigente)."""

    def __init__(self, repo: RepositorioContratoIntegracao) -> None:
        self._repo = repo

    def execute(self, contrato_id: str) -> ContratoIntegracao:
        contrato = self._repo.get_by_id(contrato_id)
        if contrato is None:
            raise ContratoIntegracaoNaoEncontradoError(
                f"Contrato de integração '{contrato_id}' não encontrado"
            )
        contrato.estado = EstadoContrato.VIGENTE
        contrato.atualizado_em = datetime.utcnow()
        return self._repo.save(contrato)


class RetirarContratoIntegracaoUseCase:
    """Retira um contrato (vigente -> retirado)."""

    def __init__(self, repo: RepositorioContratoIntegracao) -> None:
        self._repo = repo

    def execute(self, contrato_id: str) -> ContratoIntegracao:
        contrato = self._repo.get_by_id(contrato_id)
        if contrato is None:
            raise ContratoIntegracaoNaoEncontradoError(
                f"Contrato de integração '{contrato_id}' não encontrado"
            )
        contrato.estado = EstadoContrato.RETIRADO
        contrato.atualizado_em = datetime.utcnow()
        return self._repo.save(contrato)


class DeletarContratoIntegracaoUseCase:
    """Exclui (exclusão lógica) um contrato de integração."""

    def __init__(self, repo: RepositorioContratoIntegracao) -> None:
        self._repo = repo

    def execute(self, contrato_id: str) -> bool:
        contrato = self._repo.get_by_id(contrato_id)
        if contrato is None:
            raise ContratoIntegracaoNaoEncontradoError(
                f"Contrato de integração '{contrato_id}' não encontrado"
            )
        return self._repo.delete(contrato_id)


class AtualizarContratoIntegracaoUseCase:
    """Atualiza os dados de um contrato de integração."""

    def __init__(self, repo: RepositorioContratoIntegracao) -> None:
        self._repo = repo

    def execute(
        self,
        contrato_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        versao_formato: str | None = None,
        esquema_ref: str | None = None,
    ) -> ContratoIntegracao:
        contrato = self._repo.get_by_id(contrato_id)
        if contrato is None:
            raise ContratoIntegracaoNaoEncontradoError(
                f"Contrato de integração '{contrato_id}' não encontrado"
            )

        if nome is not None:
            contrato.nome = nome
        if descricao is not None:
            contrato.descricao = descricao
        if versao_formato is not None:
            contrato.versao_formato = versao_formato
        if esquema_ref is not None:
            contrato.esquema_ref = esquema_ref

        contrato.atualizado_em = datetime.utcnow()
        return self._repo.save(contrato)
