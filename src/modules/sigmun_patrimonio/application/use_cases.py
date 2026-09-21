"""Use cases do DOM-PAT — Gestão Patrimonial."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.bem import Bem, StatusBem, TipoBem
from ..domain.entities.depreciacao import Depreciacao
from ..domain.entities.transferencia import Transferencia


@dataclass
class CadastrarBemInput:
    """DTO de cadastro de bem."""

    codigo: str
    tipo: str
    descricao: str
    valor_aquisicao: float
    categoria: str = ""
    data_aquisicao: date | None = None
    valor_residual: float = 0.0
    vida_util_anos: int = 0
    localizacao: str = ""
    responsavel_id: str = ""
    autor_id: str = ""


class CadastrarBemUseCase:
    """Cadastra um bem patrimonial (RN-PAT-001)."""

    def __init__(self, repo: ports.RepositorioBem) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarBemInput) -> Bem:
        """Executa o cadastro."""
        from ..domain.exceptions import BemJaExistenteError, RegraNegocioError

        if not dto.codigo or not dto.descricao:
            raise RegraNegocioError("Código e descrição do bem são obrigatórios")
        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise BemJaExistenteError(
                "Tombo/código de bem já cadastrado (RN-PAT-001)"
            )
        bem = Bem(
            codigo=dto.codigo,
            tipo=TipoBem(dto.tipo),
            descricao=dto.descricao,
            categoria=dto.categoria,
            valor_aquisicao=dto.valor_aquisicao,
            data_aquisicao=dto.data_aquisicao,
            valor_residual=dto.valor_residual,
            vida_util_anos=dto.vida_util_anos,
            valor_contabil=dto.valor_aquisicao,
            localizacao=dto.localizacao,
            responsavel_id=dto.responsavel_id,
            created_by=dto.autor_id,
        )
        bem.validar()
        return self._repo.save(bem)


class DepreciarBemUseCase:
    """Aplica depreciação linear a um bem (RN-PAT-002)."""

    def __init__(
        self,
        bens: ports.RepositorioBem,
        depreciacoes: ports.RepositorioDepreciacao,
    ) -> None:
        self._bens = bens
        self._depreciacoes = depreciacoes

    def execute(self, bem_id: str, data: date | None = None) -> Depreciacao:
        """Executa a depreciação."""
        from ..domain.exceptions import BemNaoEncontradoError, RegraNegocioError

        bem = self._bens.get_by_id(bem_id)
        if bem is None:
            raise BemNaoEncontradoError("Bem não encontrado sobre o qual depreciar")
        valor = bem.depreciacao_anual()
        if valor <= 0:
            raise RegraNegocioError(
                "Bem não possui depreciação aplicável (vida útil nula ou "
                "valor residual igual ao de aquisição)"
            )
        if bem.status == StatusBem.BAIXADO:
            raise RegraNegocioError("Bem baixado não pode ser depreciado")
        acumulado = sum(d.valor_depreciado for d in self._depreciacoes.list_by_bem(bem_id))
        novo_acumulado = round(acumulado + valor, 2)
        liquido = round(max(bem.valor_contabil - valor, 0.0), 2)
        bem.depreciar(valor)
        self._bens.save(bem)
        depreciacao = Depreciacao(
            bem_id=bem_id,
            data=data or date.today(),
            valor_depreciado=valor,
            valor_acumulado=novo_acumulado,
            valor_liquido=liquido,
        )
        depreciacao.validar()
        return self._depreciacoes.save(depreciacao)


@dataclass
class TransferirBemInput:
    """DTO de transferência de bem."""

    bem_id: str
    para_localizacao: str
    de_localizacao: str = ""
    de_responsavel_id: str = ""
    para_responsavel_id: str = ""
    motivo: str = ""
    autor_id: str = ""


class TransferirBemUseCase:
    """Registra transferência de bem (RN-PAT-010)."""

    def __init__(
        self,
        bens: ports.RepositorioBem,
        transferencias: ports.RepositorioTransferencia,
    ) -> None:
        self._bens = bens
        self._transferencias = transferencias

    def execute(self, dto: TransferirBemInput) -> Transferencia:
        """Executa a transferência."""
        from ..domain.exceptions import BemNaoEncontradoError

        bem = self._bens.get_by_id(dto.bem_id)
        if bem is None:
            raise BemNaoEncontradoError("Bem não encontrado para transferência")
        bem.transferir(dto.para_localizacao)
        transferencia = Transferencia(
            bem_id=dto.bem_id,
            de_localizacao=(
                dto.de_localizacao or bem.localizacao
            ),
            para_localizacao=dto.para_localizacao,
            de_responsavel_id=dto.de_responsavel_id,
            para_responsavel_id=dto.para_responsavel_id,
            data_transferencia=date.today(),
            motivo=dto.motivo,
            created_by=dto.autor_id,
        )
        transferencia.validar()
        self._bens.save(bem)
        return self._transferencias.save(transferencia)


class ConcluirTransferenciaUseCase:
    """Consolida uma transferência pendente."""

    def __init__(
        self,
        transferencias: ports.RepositorioTransferencia,
        bens: ports.RepositorioBem,
    ) -> None:
        self._transferencias = transferencias
        self._bens = bens

    def execute(self, transferencia_id: str) -> Transferencia:
        """Executa a conclusão."""
        from ..domain.exceptions import (
            BemNaoEncontradoError,
            TransferenciaNaoEncontradaError,
        )

        transferencia = self._transferencias.get_by_id(transferencia_id)
        if transferencia is None:
            raise TransferenciaNaoEncontradaError(
                "Transferência não encontrada"
            )
        bem = self._bens.get_by_id(transferencia.bem_id)
        if bem is None:
            raise BemNaoEncontradoError("Bem vinculado à transferência não encontrado")
        transferencia.concluir()
        bem.confirmar_localizacao(transferencia.para_localizacao)
        self._bens.save(bem)
        return self._transferencias.save(transferencia)


class BaixarBemUseCase:
    """Baixa definitiva de um bem (RN-PAT-003)."""

    def __init__(self, repo: ports.RepositorioBem) -> None:
        self._repo = repo

    def execute(self, bem_id: str) -> Bem:
        """Executa a baixa."""
        from ..domain.exceptions import BemNaoEncontradoError

        bem = self._repo.get_by_id(bem_id)
        if bem is None:
            raise BemNaoEncontradoError("Bem não encontrado para baixa")
        bem.baixar()
        return self._repo.save(bem)


__all__ = [
    "CadastrarBemInput",
    "CadastrarBemUseCase",
    "DepreciarBemUseCase",
    "TransferirBemInput",
    "TransferirBemUseCase",
    "ConcluirTransferenciaUseCase",
    "BaixarBemUseCase",
]