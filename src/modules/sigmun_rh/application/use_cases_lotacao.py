"""Use cases de Lotação (DOM-PES)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.lotacao import Lotacao


@dataclass
class LotarServidorInput:
    """DTO de lotação de servidor."""

    servidor_id: str
    unidade_id: str
    cargo_id: str = ""
    data_inicio: date | None = None
    motivo: str = ""
    autor_id: str = ""


class LotarServidorUseCase:
    """Lota servidor em unidade (RN-PES-020/021)."""

    def __init__(
        self,
        lotacoes: ports.RepositorioLotacao,
        servidores: ports.RepositorioServidor,
    ) -> None:
        self._lotacoes = lotacoes
        self._servidores = servidores

    def execute(self, dto: LotarServidorInput) -> Lotacao:
        """Executa a lotação."""
        from ..domain.exceptions import RegraNegocioError

        servidor = self._servidores.get_by_id(dto.servidor_id)
        if servidor is None:
            raise RegraNegocioError("Servidor não encontrado")
        if not servidor.esta_ativo:
            raise RegraNegocioError("Apenas servidores ativos podem ser lotados")
        if not dto.unidade_id:
            raise RegraNegocioError("Lotação exige unidade de destino (RN-PES-021)")
        if not dto.data_inicio:
            raise RegraNegocioError("Lotação exige data de início (RN-PES-021)")
        vigentes = self._lotacoes.list_vigentes_por_servidor(dto.servidor_id)
        for vig in vigentes:
            if vig.data_inicio and dto.data_inicio and vig.data_inicio <= dto.data_inicio:
                if vig.data_fim is None or vig.data_fim >= dto.data_inicio:
                    raise RegraNegocioError(
                        "Servidor já possui lotação vigente no período (RN-PES-020)"
                    )
        lotacao = Lotacao(
            servidor_id=dto.servidor_id,
            unidade_id=dto.unidade_id,
            cargo_id=dto.cargo_id or servidor.cargo_id,
            data_inicio=dto.data_inicio,
            motivo=dto.motivo,
            created_by=dto.autor_id,
        )
        return self._lotacoes.save(lotacao)


@dataclass
class RemoverServidorInput:
    """DTO de remoção (encerramento de lotação)."""

    lotacao_id: str
    data_fim: date | None = None
    motivo: str = ""


class RemoverServidorUseCase:
    """Encerra lotação vigente do servidor."""

    def __init__(self, lotacoes: ports.RepositorioLotacao) -> None:
        self._lotacoes = lotacoes

    def execute(self, dto: RemoverServidorInput) -> Lotacao:
        """Executa a remoção."""
        from ..domain.exceptions import LotacaoNaoEncontradaError

        lotacao = self._lotacoes.get_by_id(dto.lotacao_id)
        if lotacao is None:
            raise LotacaoNaoEncontradaError("Lotação não encontrada")
        lotacao.encerrar(dto.data_fim, dto.motivo)
        return self._lotacoes.save(lotacao)


__all__ = [
    "LotarServidorInput",
    "LotarServidorUseCase",
    "RemoverServidorInput",
    "RemoverServidorUseCase",
]
