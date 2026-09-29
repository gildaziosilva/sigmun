"""Use cases do DOM-TEL — Gestão Territorial (parte 2: logradouros)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..domain.entities import (
    Logradouro,
    SituacaoLogradouro,
    TipoLogradouro,
)
from . import interfaces as ports


def _tipo_logradouro(valor: str) -> TipoLogradouro:
    """Converte o tipo textual do logradouro, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoLogradouro(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de logradouro inválido: {valor}") from exc


@dataclass
class CadastrarLogradouroInput:
    """DTO de cadastro de logradouro público."""

    codigo: str
    nome: str
    bairro_id: str
    tipo: str = "rua"
    cep: str = ""
    numero_inicial: int = 0
    numero_final: int = 0
    autor_id: str = ""


class CadastrarLogradouroUseCase:
    """Cadastra um logradouro público vinculado a bairro (RN-TEL-002)."""

    def __init__(
        self, repo: ports.RepositorioLogradouro, bairros: ports.RepositorioBairro
    ) -> None:
        self._repo = repo
        self._bairros = bairros

    def execute(self, dto: CadastrarLogradouroInput) -> Logradouro:
        """Executa o cadastro."""
        from ..domain.exceptions import (
            BairroNaoEncontradoError,
            LogradouroJaExistenteError,
            RegraNegocioError,
        )

        if not dto.codigo or not dto.nome:
            raise RegraNegocioError(
                "Código e nome do logradouro são obrigatórios (RN-TEL-002)"
            )
        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise LogradouroJaExistenteError(
                "Logradouro já cadastrado com este código (RN-TEL-002)"
            )
        bairro = self._bairros.get_by_id(dto.bairro_id)
        if bairro is None:
            raise BairroNaoEncontradoError("Bairro não encontrado para o logradouro (RN-TEL-002)")

        logradouro = Logradouro(
            codigo=dto.codigo,
            nome=dto.nome,
            bairro_id=bairro.id,
            tipo=_tipo_logradouro(dto.tipo),
            cep=dto.cep,
            numero_inicial=dto.numero_inicial,
            numero_final=dto.numero_final,
            created_by=dto.autor_id,
        )
        logradouro.validar()
        return self._repo.save(logradouro)


@dataclass
class AtualizarLogradouroInput:
    """DTO de atualização cadastral do logradouro (campos opcionais)."""

    logradouro_id: str
    codigo: str | None = None
    nome: str | None = None
    tipo: str | None = None
    bairro_id: str | None = None
    cep: str | None = None
    numero_inicial: int | None = None
    numero_final: int | None = None
    situacao: str | None = None
    autor_id: str = ""


class AtualizarLogradouroUseCase:
    """Atualiza o cadastro de um logradouro público (RN-TEL-002)."""

    def __init__(
        self, repo: ports.RepositorioLogradouro, bairros: ports.RepositorioBairro
    ) -> None:
        self._repo = repo
        self._bairros = bairros

    def execute(self, dto: AtualizarLogradouroInput) -> Logradouro:
        """Executa a atualização."""
        from ..domain.exceptions import (
            BairroNaoEncontradoError,
            LogradouroJaExistenteError,
            LogradouroNaoEncontradoError,
            RegraNegocioError,
        )

        logradouro = self._repo.get_by_id(dto.logradouro_id)
        if logradouro is None:
            raise LogradouroNaoEncontradoError("Logradouro não encontrado para atualização")

        if dto.codigo is not None and dto.codigo != logradouro.codigo:
            outro = self._repo.get_by_codigo(dto.codigo)
            if outro is not None and outro.id != logradouro.id:
                raise LogradouroJaExistenteError(
                    "Logradouro já cadastrado com este código (RN-TEL-002)"
                )
            logradouro.codigo = dto.codigo
        if dto.nome is not None:
            logradouro.nome = dto.nome
        if dto.tipo is not None:
            logradouro.tipo = _tipo_logradouro(dto.tipo)
        if dto.bairro_id is not None and dto.bairro_id != logradouro.bairro_id:
            if self._bairros.get_by_id(dto.bairro_id) is None:
                raise BairroNaoEncontradoError("Bairro não encontrado para o logradouro")
            logradouro.bairro_id = dto.bairro_id
        if dto.cep is not None:
            logradouro.cep = dto.cep
        if dto.numero_inicial is not None:
            logradouro.numero_inicial = dto.numero_inicial
        if dto.numero_final is not None:
            logradouro.numero_final = dto.numero_final
        if dto.situacao is not None:
            if dto.situacao == SituacaoLogradouro.ATIVO.value:
                logradouro.ativar()
            elif dto.situacao == SituacaoLogradouro.INATIVO.value:
                logradouro.inativar()
            elif dto.situacao == SituacaoLogradouro.EM_OBRA.value:
                logradouro.situacao = SituacaoLogradouro.EM_OBRA
                logradouro.updated_at = datetime.utcnow()
            else:
                raise RegraNegocioError(f"Situação inválida para logradouro: {dto.situacao}")

        logradouro.validar()
        logradouro.updated_at = datetime.utcnow()
        return self._repo.save(logradouro)


class ExcluirLogradouroUseCase:
    """Exclui (soft-delete) um logradouro público."""

    def __init__(self, repo: ports.RepositorioLogradouro) -> None:
        self._repo = repo

    def execute(self, logradouro_id: str) -> Logradouro:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import LogradouroNaoEncontradoError

        logradouro = self._repo.get_by_id(logradouro_id)
        if logradouro is None:
            raise LogradouroNaoEncontradoError("Logradouro não encontrado para exclusão")
        logradouro.excluir()
        return self._repo.save(logradouro)
