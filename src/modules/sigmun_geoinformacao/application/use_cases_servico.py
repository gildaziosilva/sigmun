"""Casos de uso do DOM-GEO — serviços geoespaciais (RN-GEO-007)."""

from __future__ import annotations

from dataclasses import dataclass

from ..domain.entities import ServicoGeo
from . import interfaces as ports
from .conversores import datum, tipo_servico


@dataclass
class CadastrarServicoInput:
    """DTO de cadastro de serviço geoespacial (RN-GEO-007)."""

    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: str = "wms"
    url: str = ""
    camada: str = ""
    datum: str = "sirgas2000"
    srid: int = 4326
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    publico: bool = False
    autor_id: str = ""


class CadastrarServicoUseCase:
    """Cadastra um serviço geoespacial no geoportal (RN-GEO-007)."""

    def __init__(self, repo: ports.RepositorioServicoGeo) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarServicoInput) -> ServicoGeo:
        """Executa o cadastro."""
        from ..domain.exceptions import ServicoGeoJaExistenteError

        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise ServicoGeoJaExistenteError("Código de serviço já cadastrado (RN-GEO-007)")

        servico = ServicoGeo(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            tipo=tipo_servico(dto.tipo),
            url=dto.url,
            camada=dto.camada,
            datum=datum(dto.datum),
            srid=dto.srid,
            zoom_minimo=dto.zoom_minimo,
            zoom_maximo=dto.zoom_maximo,
            publico=dto.publico,
            created_by=dto.autor_id,
        )
        servico.validar()
        return self._repo.save(servico)


@dataclass
class AtualizarServicoInput:
    """DTO de atualização de serviço geoespacial (todos os campos opcionais)."""

    servico_id: str = ""
    codigo: str | None = None
    nome: str | None = None
    descricao: str | None = None
    tipo: str | None = None
    url: str | None = None
    camada: str | None = None
    datum: str | None = None
    srid: int | None = None
    zoom_minimo: int | None = None
    zoom_maximo: int | None = None
    publico: bool | None = None
    autor_id: str = ""


class AtualizarServicoUseCase:
    """Atualiza o cadastro de um serviço geoespacial."""

    def __init__(self, repo: ports.RepositorioServicoGeo) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarServicoInput) -> ServicoGeo:
        """Executa a atualização."""
        from datetime import datetime

        from ..domain.exceptions import RegraNegocioError, ServicoGeoNaoEncontradoError

        servico = self._repo.get_by_id(dto.servico_id)
        if servico is None:
            raise ServicoGeoNaoEncontradoError(
                "Serviço geoespacial não encontrado para atualização"
            )

        if dto.codigo is not None and dto.codigo != servico.codigo:
            outro = self._repo.get_by_codigo(dto.codigo)
            if outro is not None and outro.id != servico.id:
                raise RegraNegocioError("Código de serviço já cadastrado (RN-GEO-007)")
            servico.codigo = dto.codigo
        if dto.nome is not None:
            servico.nome = dto.nome
        if dto.descricao is not None:
            servico.descricao = dto.descricao
        if dto.tipo is not None:
            servico.tipo = tipo_servico(dto.tipo)
        if dto.url is not None:
            servico.url = dto.url
        if dto.camada is not None:
            servico.camada = dto.camada
        if dto.datum is not None:
            servico.datum = datum(dto.datum)
        if dto.srid is not None:
            servico.srid = dto.srid
        if dto.zoom_minimo is not None:
            servico.zoom_minimo = dto.zoom_minimo
        if dto.zoom_maximo is not None:
            servico.zoom_maximo = dto.zoom_maximo
        if dto.publico is not None:
            servico.publico = dto.publico

        servico.updated_at = datetime.utcnow()
        servico.validar()
        return self._repo.save(servico)


class InativarServicoUseCase:
    """Inativa um serviço geoespacial (RN-GEO-007)."""

    def __init__(self, repo: ports.RepositorioServicoGeo) -> None:
        self._repo = repo

    def execute(self, servico_id: str, autor_id: str = "") -> ServicoGeo:
        """Executa a inativação."""
        from ..domain.exceptions import ServicoGeoNaoEncontradoError

        servico = self._repo.get_by_id(servico_id)
        if servico is None:
            raise ServicoGeoNaoEncontradoError("Serviço geoespacial não encontrado para inativação")
        servico.inativar(autor_id)
        return self._repo.save(servico)


class ExcluirServicoUseCase:
    """Exclui (soft-delete) um serviço geoespacial."""

    def __init__(self, repo: ports.RepositorioServicoGeo) -> None:
        self._repo = repo

    def execute(self, servico_id: str) -> ServicoGeo:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import ServicoGeoNaoEncontradoError

        servico = self._repo.get_by_id(servico_id)
        if servico is None:
            raise ServicoGeoNaoEncontradoError("Serviço geoespacial não encontrado para exclusão")
        servico.excluir()
        return self._repo.save(servico)


__all__ = [
    "CadastrarServicoInput",
    "CadastrarServicoUseCase",
    "AtualizarServicoInput",
    "AtualizarServicoUseCase",
    "InativarServicoUseCase",
    "ExcluirServicoUseCase",
]
