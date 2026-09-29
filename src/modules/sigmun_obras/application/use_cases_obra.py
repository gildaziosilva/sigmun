"""Casos de uso do DOM-OBR — cadastro e ciclo de vida das obras.

RN-OBR-001: número da obra único.
RN-OBR-002/003/004: ciclo de vida, contratação e coerência físico-financeira.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from ..domain.entities import Obra, SituacaoObra
from . import interfaces as ports
from .conversores import fonte_recurso, tipo_contratacao, tipo_obra


@dataclass
class CadastrarObraInput:
    """DTO de cadastro de obra pública (RN-OBR-001)."""

    numero: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: str = "outro"
    tipo_contratacao: str = "licitacao"
    fonte_recurso: str = "orcamento_proprio"
    valor_orcado: float = 0.0
    valor_contratado: float = 0.0
    empresa_contratada: str = ""
    numero_contrato: str = ""
    responsavel_tecnico: str = ""
    endereco: str = ""
    bairro: str = ""
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    autor_id: str = ""


class CadastrarObraUseCase:
    """Cadastra uma obra pública em situação PLANEJADA (RN-OBR-001)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarObraInput) -> Obra:
        """Executa o cadastro."""
        from ..domain.exceptions import ObraJaExistenteError

        if self._repo.get_by_numero(dto.numero) is not None:
            raise ObraJaExistenteError("Número de obra já cadastrado (RN-OBR-001)")

        obra = Obra(
            numero=dto.numero,
            nome=dto.nome,
            descricao=dto.descricao,
            tipo=tipo_obra(dto.tipo),
            tipo_contratacao=tipo_contratacao(dto.tipo_contratacao),
            fonte_recurso=fonte_recurso(dto.fonte_recurso),
            valor_orcado=dto.valor_orcado,
            valor_contratado=dto.valor_contratado,
            empresa_contratada=dto.empresa_contratada,
            numero_contrato=dto.numero_contrato,
            responsavel_tecnico=dto.responsavel_tecnico,
            endereco=dto.endereco,
            bairro=dto.bairro,
            data_inicio_prevista=dto.data_inicio_prevista,
            data_fim_prevista=dto.data_fim_prevista,
            created_by=dto.autor_id,
        )
        obra.validar()
        return self._repo.save(obra)


@dataclass
class AtualizarObraInput:
    """DTO de atualização de obra pública (todos os campos opcionais)."""

    obra_id: str = ""
    nome: str | None = None
    descricao: str | None = None
    tipo: str | None = None
    tipo_contratacao: str | None = None
    fonte_recurso: str | None = None
    valor_orcado: float | None = None
    valor_contratado: float | None = None
    empresa_contratada: str | None = None
    numero_contrato: str | None = None
    responsavel_tecnico: str | None = None
    endereco: str | None = None
    bairro: str | None = None
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    observacao: str | None = None
    autor_id: str = ""


class AtualizarObraUseCase:
    """Atualiza os dados cadastrais de uma obra não concluída (RN-OBR-002)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarObraInput) -> Obra:
        """Executa a atualização."""
        from ..domain.exceptions import ObraNaoEncontradaError, RegraNegocioError

        obra = self._repo.get_by_id(dto.obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para atualização")
        if obra.situacao == SituacaoObra.CONCLUIDA:
            raise RegraNegocioError("Obra concluída não aceita alterações (RN-OBR-002)")

        for campo, valor in (
            ("nome", dto.nome),
            ("descricao", dto.descricao),
            ("valor_orcado", dto.valor_orcado),
            ("valor_contratado", dto.valor_contratado),
            ("empresa_contratada", dto.empresa_contratada),
            ("numero_contrato", dto.numero_contrato),
            ("responsavel_tecnico", dto.responsavel_tecnico),
            ("endereco", dto.endereco),
            ("bairro", dto.bairro),
            ("data_inicio_prevista", dto.data_inicio_prevista),
            ("data_fim_prevista", dto.data_fim_prevista),
            ("observacao", dto.observacao),
        ):
            if valor is not None:
                setattr(obra, campo, valor)
        if dto.tipo is not None:
            obra.tipo = tipo_obra(dto.tipo)
        if dto.tipo_contratacao is not None:
            obra.tipo_contratacao = tipo_contratacao(dto.tipo_contratacao)
        if dto.fonte_recurso is not None:
            obra.fonte_recurso = fonte_recurso(dto.fonte_recurso)

        obra.updated_at = datetime.utcnow()
        obra.validar()
        return self._repo.save(obra)


class IniciarExecucaoObraUseCase:
    """Inicia a execução física da obra (RN-OBR-002, RN-OBR-003)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, obra_id: str, data: date | None = None, autor_id: str = "") -> Obra:
        """Executa a transição para EM_EXECUCAO."""
        from ..domain.exceptions import ObraNaoEncontradaError

        obra = self._repo.get_by_id(obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para iniciar execução")
        obra.iniciar_execucao(data)
        return self._repo.save(obra)


class ConcluirObraUseCase:
    """Conclui a obra, exigindo 100% do avanço físico (RN-OBR-005)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, obra_id: str, data: date | None = None, autor_id: str = "") -> Obra:
        """Executa a transição para CONCLUIDA."""
        from ..domain.exceptions import ObraNaoEncontradaError

        obra = self._repo.get_by_id(obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para conclusão")
        obra.concluir(data)
        return self._repo.save(obra)


class SuspenderObraUseCase:
    """Suspende a execução da obra (RN-OBR-002)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, obra_id: str, motivo: str = "", autor_id: str = "") -> Obra:
        """Executa a transição para SUSPENSA."""
        from ..domain.exceptions import ObraNaoEncontradaError

        obra = self._repo.get_by_id(obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para suspensão")
        obra.suspender(motivo)
        return self._repo.save(obra)


class CancelarObraUseCase:
    """Cancela a obra (RN-OBR-002)."""

    def __init__(self, repo: ports.RepositorioObra) -> None:
        self._repo = repo

    def execute(self, obra_id: str, motivo: str = "", autor_id: str = "") -> Obra:
        """Executa a transição para CANCELADA."""
        from ..domain.exceptions import ObraNaoEncontradaError

        obra = self._repo.get_by_id(obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para cancelamento")
        obra.cancelar(motivo)
        return self._repo.save(obra)


class ExcluirObraUseCase:
    """Exclui (soft-delete) uma obra sem dependências financeiras (RN-OBR-006)."""

    def __init__(
        self,
        repo: ports.RepositorioObra,
        medicoes: ports.RepositorioMedicao,
        despesas: ports.RepositorioDespesa,
    ) -> None:
        self._repo = repo
        self._medicoes = medicoes
        self._despesas = despesas

    def execute(self, obra_id: str) -> Obra:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import ObraComDependenciasError, ObraNaoEncontradaError

        obra = self._repo.get_by_id(obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para exclusão")
        if self._medicoes.list_by_obra(obra_id) or self._despesas.list_by_obra(obra_id):
            raise ObraComDependenciasError(
                "Obra possui medições ou despesas vinculadas e não pode ser excluída "
                "(RN-OBR-005, RN-OBR-006)"
            )

        obra.excluir()
        return self._repo.save(obra)


__all__ = [
    "CadastrarObraInput",
    "CadastrarObraUseCase",
    "AtualizarObraInput",
    "AtualizarObraUseCase",
    "IniciarExecucaoObraUseCase",
    "ConcluirObraUseCase",
    "SuspenderObraUseCase",
    "CancelarObraUseCase",
    "ExcluirObraUseCase",
]
