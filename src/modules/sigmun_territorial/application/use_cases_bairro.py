"""Use cases do DOM-TEL — Gestão Territorial (parte 1: bairros e logradouros)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..domain.entities import (
    Bairro,
    SituacaoBairro,
    TipoBairro,
)
from . import interfaces as ports


@dataclass
class CadastrarBairroInput:
    """DTO de cadastro de divisão territorial."""

    codigo: str
    nome: str
    tipo: str = "bairro"
    populacao_estimada: int = 0
    area_km2: float = 0.0
    autor_id: str = ""


class CadastrarBairroUseCase:
    """Cadastra uma divisão territorial (RN-TEL-001)."""

    def __init__(self, repo: ports.RepositorioBairro) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarBairroInput) -> Bairro:
        """Executa o cadastro."""
        from ..domain.exceptions import BairroJaExistenteError, RegraNegocioError

        if not dto.codigo or not dto.nome:
            raise RegraNegocioError("Código e nome do bairro são obrigatórios (RN-TEL-001)")
        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise BairroJaExistenteError("Bairro já cadastrado com este código (RN-TEL-001)")
        bairro = Bairro(
            codigo=dto.codigo,
            nome=dto.nome,
            tipo=_tipo_bairro(dto.tipo),
            populacao_estimada=dto.populacao_estimada,
            area_km2=dto.area_km2,
            created_by=dto.autor_id,
        )
        bairro.validar()
        return self._repo.save(bairro)


def _tipo_bairro(valor: str) -> TipoBairro:
    """Converte o tipo textual do bairro, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoBairro(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de bairro inválido: {valor}") from exc


@dataclass
class AtualizarBairroInput:
    """DTO de atualização cadastral do bairro (campos opcionais)."""

    bairro_id: str
    codigo: str | None = None
    nome: str | None = None
    tipo: str | None = None
    populacao_estimada: int | None = None
    area_km2: float | None = None
    situacao: str | None = None
    autor_id: str = ""


class AtualizarBairroUseCase:
    """Atualiza a cadastro de uma divisão territorial (RN-TEL-001)."""

    def __init__(self, repo: ports.RepositorioBairro) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarBairroInput) -> Bairro:
        """Executa a atualização."""
        from ..domain.exceptions import (
            BairroJaExistenteError,
            BairroNaoEncontradoError,
            RegraNegocioError,
        )

        bairro = self._repo.get_by_id(dto.bairro_id)
        if bairro is None:
            raise BairroNaoEncontradoError("Bairro não encontrado para atualização")

        if dto.codigo is not None and dto.codigo != bairro.codigo:
            outro = self._repo.get_by_codigo(dto.codigo)
            if outro is not None and outro.id != bairro.id:
                raise BairroJaExistenteError(
                    "Bairro já cadastrado com este código (RN-TEL-001)"
                )
            bairro.codigo = dto.codigo
        if dto.nome is not None:
            bairro.nome = dto.nome
        if dto.tipo is not None:
            bairro.tipo = _tipo_bairro(dto.tipo)
        if dto.populacao_estimada is not None:
            if dto.populacao_estimada < 0:
                raise RegraNegocioError("População estimada não pode ser negativa")
            bairro.populacao_estimada = dto.populacao_estimada
        if dto.area_km2 is not None:
            if dto.area_km2 < 0:
                raise RegraNegocioError("Área do bairro não pode ser negativa")
            bairro.area_km2 = dto.area_km2
        if dto.situacao is not None:
            if dto.situacao == SituacaoBairro.ATIVO.value:
                bairro.ativar()
            elif dto.situacao == SituacaoBairro.INATIVO.value:
                bairro.inativar()
            else:
                raise RegraNegocioError(f"Situação inválida para bairro: {dto.situacao}")

        bairro.validar()
        bairro.updated_at = datetime.utcnow()
        return self._repo.save(bairro)


class ExcluirBairroUseCase:
    """Exclui (soft-delete) uma divisão territorial (RN-TEL-006)."""

    def __init__(
        self, repo: ports.RepositorioBairro, logradouros: ports.RepositorioLogradouro
    ) -> None:
        self._repo = repo
        self._logradouros = logradouros

    def execute(self, bairro_id: str) -> Bairro:
        """Executa a exclusão lógica, recusando bairro com logradouros."""
        from ..domain.exceptions import BairroComDependenciasError, BairroNaoEncontradoError

        bairro = self._repo.get_by_id(bairro_id)
        if bairro is None:
            raise BairroNaoEncontradoError("Bairro não encontrado para exclusão")
        vinculados = [lg for lg in self._logradouros.list_by_bairro(bairro_id) if lg.esta_ativo]
        if vinculados:
            raise BairroComDependenciasError(
                f"Bairro possui {len(vinculados)} logradouro(s) ativo(s) e não pode ser "
                "excluído (RN-TEL-006)"
            )
        bairro.excluir()
        return self._repo.save(bairro)
