"""Casos de uso do DOM-OBR — etapas e vistorias fiscalizadoras.

RN-OBR-007: ciclo de vida das etapas da obra.
RN-OBR-008: vistorias registram o parecer sobre o avanço físico verificado.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..domain.entities import EtapaObra, VistoriaObra
from . import interfaces as ports
from .conversores import parecer_vistoria, tipo_etapa, tipo_vistoria


@dataclass
class CadastrarEtapaInput:
    """DTO de cadastro de etapa de obra (RN-OBR-007)."""

    obra_id: str = ""
    numero: str = ""
    descricao: str = ""
    tipo: str = "estrutura"
    percentual_previsto: float = 0.0
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    responsavel: str = ""
    autor_id: str = ""


class CadastrarEtapaUseCase:
    """Cadastra uma etapa de execução em uma obra existente (RN-OBR-007)."""

    def __init__(self, repo: ports.RepositorioEtapa, obras: ports.RepositorioObra) -> None:
        self._repo = repo
        self._obras = obras

    def execute(self, dto: CadastrarEtapaInput) -> EtapaObra:
        """Executa o cadastro da etapa."""
        from ..domain.exceptions import ObraNaoEncontradaError

        if self._obras.get_by_id(dto.obra_id) is None:
            raise ObraNaoEncontradaError("Obra não encontrada para a etapa")

        etapa = EtapaObra(
            obra_id=dto.obra_id,
            numero=dto.numero,
            descricao=dto.descricao,
            tipo=tipo_etapa(dto.tipo),
            percentual_previsto=dto.percentual_previsto,
            data_inicio_prevista=dto.data_inicio_prevista,
            data_fim_prevista=dto.data_fim_prevista,
            responsavel=dto.responsavel,
            created_by=dto.autor_id,
        )
        etapa.validar()
        return self._repo.save(etapa)


class AtualizarEtapaUseCase:
    """Atualiza o avanço físico de uma etapa (RN-OBR-007)."""

    def __init__(self, repo: ports.RepositorioEtapa) -> None:
        self._repo = repo

    def execute(
        self,
        etapa_id: str,
        percentual_realizado: float | None = None,
        situacao: str | None = None,
        autor_id: str = "",
    ) -> EtapaObra:
        """Executa a atualização da etapa."""
        from ..domain.entities import SituacaoEtapa
        from ..domain.exceptions import EtapaNaoEncontradaError, RegraNegocioError

        etapa = self._repo.get_by_id(etapa_id)
        if etapa is None:
            raise EtapaNaoEncontradaError("Etapa não encontrada para atualização")

        if percentual_realizado is not None:
            etapa.percentual_realizado = percentual_realizado
        if situacao is not None:
            try:
                etapa.situacao = SituacaoEtapa(situacao)
            except ValueError as exc:
                raise RegraNegocioError(f"Situação inválida para etapa: {situacao}") from exc

        etapa.validar()
        return self._repo.save(etapa)


class ConcluirEtapaUseCase:
    """Conclui uma etapa, exigindo 100% do previsto (RN-OBR-007)."""

    def __init__(self, repo: ports.RepositorioEtapa) -> None:
        self._repo = repo

    def execute(self, etapa_id: str, data: date | None = None) -> EtapaObra:
        """Executa a conclusão da etapa."""
        from ..domain.exceptions import EtapaNaoEncontradaError

        etapa = self._repo.get_by_id(etapa_id)
        if etapa is None:
            raise EtapaNaoEncontradaError("Etapa não encontrada para conclusão")
        etapa.concluir(data)
        return self._repo.save(etapa)


@dataclass
class RegistrarVistoriaInput:
    """DTO de registro de vistoria fiscalizadora (RN-OBR-008)."""

    obra_id: str = ""
    data: date | None = None
    tipo: str = "periodica"
    parecer: str = "aprovado"
    percentual_fisico_verificado: float = 0.0
    fiscal: str = ""
    observacao: str = ""
    autor_id: str = ""


class RegistrarVistoriaUseCase:
    """Registra a vistoria de avanço físico na obra (RN-OBR-008)."""

    def __init__(self, repo: ports.RepositorioVistoria, obras: ports.RepositorioObra) -> None:
        self._repo = repo
        self._obras = obras

    def execute(self, dto: RegistrarVistoriaInput) -> VistoriaObra:
        """Executa o registro da vistoria."""
        from ..domain.exceptions import ObraNaoEncontradaError

        if self._obras.get_by_id(dto.obra_id) is None:
            raise ObraNaoEncontradaError("Obra não encontrada para a vistoria")

        vistoria = VistoriaObra(
            obra_id=dto.obra_id,
            data=dto.data or date.today(),
            tipo=tipo_vistoria(dto.tipo),
            parecer=parecer_vistoria(dto.parecer),
            percentual_fisico_verificado=dto.percentual_fisico_verificado,
            fiscal=dto.fiscal,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        vistoria.validar()
        return self._repo.save(vistoria)


__all__ = [
    "CadastrarEtapaInput",
    "CadastrarEtapaUseCase",
    "AtualizarEtapaUseCase",
    "ConcluirEtapaUseCase",
    "RegistrarVistoriaInput",
    "RegistrarVistoriaUseCase",
]
