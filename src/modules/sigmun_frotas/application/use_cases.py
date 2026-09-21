"""Use cases do DOM-FRO — Gestão de Frota."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.operacional import (
    Abastecimento,
    Manutencao,
    Rota,
    TipoManutencao,
)
from ..domain.entities.veiculo import (
    Combustivel,
    TipoVeiculo,
    Veiculo,
)


@dataclass
class CadastrarVeiculoInput:
    """DTO de cadastro de veículo."""

    placa: str
    marca: str
    modelo: str
    chassi: str = ""
    renavam: str = ""
    ano_fabricacao: int = 0
    ano_modelo: int = 0
    tipo: str = "leve"
    combustivel: str = "flex"
    capacidade: float = 0.0
    odometro_atual: float = 0.0
    unidade_id: str = ""
    autor_id: str = ""


class CadastrarVeiculoUseCase:
    """Cadastra um veículo (RN-FRO-001)."""

    def __init__(self, repo: ports.RepositorioVeiculo) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarVeiculoInput) -> Veiculo:
        """Executa o cadastro."""
        from ..domain.exceptions import RegraNegocioError, VeiculoJaExistenteError

        if not dto.placa or not dto.marca or not dto.modelo:
            raise RegraNegocioError(
                "Placa, marca e modelo são obrigatórios no cadastro"
            )
        if self._repo.get_by_placa(dto.placa) is not None:
            raise VeiculoJaExistenteError(
                "Placa já cadastrada na frota (RN-FRO-001)"
            )
        veiculo = Veiculo(
            placa=dto.placa,
            chassi=dto.chassi,
            renavam=dto.renavam,
            marca=dto.marca,
            modelo=dto.modelo,
            ano_fabricacao=dto.ano_fabricacao,
            ano_modelo=dto.ano_modelo,
            tipo=TipoVeiculo(dto.tipo),
            combustivel=Combustivel(dto.combustivel),
            capacidade=dto.capacidade,
            odometro_atual=dto.odometro_atual,
            unidade_id=dto.unidade_id,
            created_by=dto.autor_id,
        )
        veiculo.validar()
        return self._repo.save(veiculo)

@dataclass
class RegistrarAbastecimentoInput:
    """DTO de abastecimento."""

    veiculo_id: str
    quantidade_litros: float
    valor_unitario: float = 0.0
    data: date | None = None
    odometro: float = 0.0
    posto: str = ""
    tipo_combustivel: str = "flex"
    autor_id: str = ""


class RegistrarAbastecimentoUseCase:
    """Registra um abastecimento e atualiza o odômetro do veículo."""

    def __init__(
        self,
        repo: ports.RepositorioAbastecimento,
        veiculos: ports.RepositorioVeiculo,
    ) -> None:
        self._repo = repo
        self._veiculos = veiculos

    def execute(self, dto: RegistrarAbastecimentoInput) -> Abastecimento:
        """Executa o registro."""
        from ..domain.exceptions import VeiculoNaoEncontradoError

        veiculo = self._veiculos.get_by_id(dto.veiculo_id)
        if veiculo is None:
            raise VeiculoNaoEncontradoError(
                "Veículo não encontrado para abastecimento"
            )
        abastecimento = Abastecimento(
            veiculo_id=dto.veiculo_id,
            data=dto.data or date.today(),
            quantidade_litros=dto.quantidade_litros,
            valor_unitario=dto.valor_unitario,
            odometro=dto.odometro,
            posto=dto.posto,
            tipo_combustivel=Combustivel(dto.tipo_combustivel),
            created_by=dto.autor_id,
        )
        abastecimento.recalcular_total()
        abastecimento.validar()
        if dto.odometro > 0:
            veiculo.atualizar_odometro(dto.odometro)
            self._veiculos.save(veiculo)
        return self._repo.save(abastecimento)


class AbrirManutencaoUseCase:
    """Abre manutenção e marca o veículo como em manutenção (RN-FRO-002)."""

    def __init__(
        self,
        repo: ports.RepositorioManutencao,
        veiculos: ports.RepositorioVeiculo,
    ) -> None:
        self._repo = repo
        self._veiculos = veiculos

    def execute(
        self,
        veiculo_id: str,
        descricao: str = "",
        tipo: str = "preventiva",
        oficina: str = "",
        valor: float = 0.0,
        data_entrada: date | None = None,
        autor_id: str = "",
    ) -> Manutencao:
        """Executa a abertura."""
        from ..domain.exceptions import RegraNegocioError, VeiculoNaoEncontradoError

        veiculo = self._veiculos.get_by_id(veiculo_id)
        if veiculo is None:
            raise VeiculoNaoEncontradoError("Veículo não encontrado")
        if not descricao:
            raise RegraNegocioError("Descrição da manutenção é obrigatória")
        veiculo.entrar_em_manutencao()
        self._veiculos.save(veiculo)
        manutencao = Manutencao(
            veiculo_id=veiculo_id,
            data_entrada=data_entrada or date.today(),
            tipo=TipoManutencao(tipo),
            descricao=descricao,
            oficina=oficina,
            valor=valor,
            created_by=autor_id,
        )
        manutencao.validar()
        return self._repo.save(manutencao)


class ConcluirManutencaoUseCase:
    """Conclui manutenção e reativa o veículo (RN-FRO-002)."""

    def __init__(
        self,
        repo: ports.RepositorioManutencao,
        veiculos: ports.RepositorioVeiculo,
    ) -> None:
        self._repo = repo
        self._veiculos = veiculos

    def execute(self, manutencao_id: str) -> Manutencao:
        """Executa a conclusão."""
        from ..domain.exceptions import (
            ManutencaoNaoEncontradaError,
            VeiculoNaoEncontradoError,
        )

        manutencao = self._repo.get_by_id(manutencao_id)
        if manutencao is None:
            raise ManutencaoNaoEncontradaError("Manutenção não encontrada")
        veiculo = self._veiculos.get_by_id(manutencao.veiculo_id)
        if veiculo is None:
            raise VeiculoNaoEncontradoError(
                "Veículo vinculado à manutenção não encontrado"
            )
        manutencao.concluir()
        veiculo.concluir_manutencao()
        self._veiculos.save(veiculo)
        return self._repo.save(manutencao)


@dataclass
class RegistrarRotaInput:
    """DTO de rota/deslocamento."""

    veiculo_id: str
    origem: str
    destino: str
    data: date | None = None
    km_inicio: float = 0.0
    km_fim: float = 0.0
    descricao: str = ""
    autor_id: str = ""


class RegistrarRotaUseCase:
    """Registra uma rota e calcula a distância percorrida."""

    def __init__(
        self,
        repo: ports.RepositorioRota,
        veiculos: ports.RepositorioVeiculo,
    ) -> None:
        self._repo = repo
        self._veiculos = veiculos

    def execute(self, dto: RegistrarRotaInput) -> Rota:
        """Executa o registro."""
        from ..domain.exceptions import VeiculoNaoEncontradoError

        if self._veiculos.get_by_id(dto.veiculo_id) is None:
            raise VeiculoNaoEncontradoError("Veículo não encontrado para a rota")
        rota = Rota(
            veiculo_id=dto.veiculo_id,
            data=dto.data or date.today(),
            origem=dto.origem,
            destino=dto.destino,
            km_inicio=dto.km_inicio,
            km_fim=dto.km_fim,
            descricao=dto.descricao,
            created_by=dto.autor_id,
        )
        rota.validar()
        rota.calcular_distancia()
        return self._repo.save(rota)


class ConcluirRotaUseCase:
    """Conclui uma rota e atualiza o odômetro do veículo."""

    def __init__(
        self,
        repo: ports.RepositorioRota,
        veiculos: ports.RepositorioVeiculo,
    ) -> None:
        self._repo = repo
        self._veiculos = veiculos

    def execute(self, rota_id: str) -> Rota:
        """Executa a conclusão."""
        from ..domain.exceptions import (
            RotaNaoEncontradaError,
            VeiculoNaoEncontradoError,
        )

        rota = self._repo.get_by_id(rota_id)
        if rota is None:
            raise RotaNaoEncontradaError("Rota não encontrada")
        veiculo = self._veiculos.get_by_id(rota.veiculo_id)
        if veiculo is None:
            raise VeiculoNaoEncontradoError(
                "Veículo vinculado à rota não encontrado"
            )
        rota.concluir()
        if rota.km_fim > 0:
            veiculo.atualizar_odometro(rota.km_fim)
            self._veiculos.save(veiculo)
        return self._repo.save(rota)


class BaixarVeiculoUseCase:
    """Baixa definitiva de um veículo."""

    def __init__(self, repo: ports.RepositorioVeiculo) -> None:
        self._repo = repo

    def execute(self, veiculo_id: str) -> Veiculo:
        """Executa a baixa."""
        from ..domain.exceptions import VeiculoNaoEncontradoError

        veiculo = self._repo.get_by_id(veiculo_id)
        if veiculo is None:
            raise VeiculoNaoEncontradoError("Veículo não encontrado para baixa")
        veiculo.baixar()
        return self._repo.save(veiculo)


__all__ = [
    "CadastrarVeiculoInput",
    "CadastrarVeiculoUseCase",
    "RegistrarAbastecimentoInput",
    "RegistrarAbastecimentoUseCase",
    "AbrirManutencaoUseCase",
    "ConcluirManutencaoUseCase",
    "RegistrarRotaInput",
    "RegistrarRotaUseCase",
    "ConcluirRotaUseCase",
    "BaixarVeiculoUseCase",
]
