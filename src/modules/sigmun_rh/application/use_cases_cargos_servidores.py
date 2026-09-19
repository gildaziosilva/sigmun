"""Use cases de Cargos e Servidores (DOM-PES)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.cargo import Cargo
from ..domain.entities.servidor import Servidor, TipoVinculo


@dataclass
class CriarCargoInput:
    """DTO de criação de cargo."""

    codigo: str
    nome: str
    descricao: str = ""
    nivel: str = "basico"
    salario_base: float = 0.0
    carga_horaria_semanal: int = 40
    autor_id: str = ""


class CriarCargoUseCase:
    """Cria um cargo (RN-PES-001/002)."""

    def __init__(self, repo: ports.RepositorioCargo) -> None:
        self._repo = repo

    def execute(self, dto: CriarCargoInput) -> Cargo:
        """Executa a criação do cargo."""
        from ..domain.exceptions import RegraNegocioError

        if not dto.codigo or not dto.nome:
            raise RegraNegocioError("Código e nome do cargo são obrigatórios (RN-PES-001)")
        if dto.salario_base <= 0:
            raise RegraNegocioError("Salário-base deve ser maior que zero (RN-PES-002)")
        existente = self._repo.get_by_codigo(dto.codigo)
        if existente is not None:
            raise RegraNegocioError(f"Cargo '{dto.codigo}' já cadastrado (RN-PES-001)")
        cargo = Cargo(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            nivel=dto.nivel,
            salario_base=dto.salario_base,
            carga_horaria_semanal=dto.carga_horaria_semanal,
            created_by=dto.autor_id,
        )
        return self._repo.save(cargo)


@dataclass
class AdmitirServidorInput:
    """DTO de admissão de servidor."""

    matricula: str
    cpf: str
    nome: str
    cargo_id: str
    tipo_vinculo: str = "efetivo"
    salario: float = 0.0
    data_admissao: date | None = None
    email: str = ""
    telefone: str = ""
    autor_id: str = ""


class AdmitirServidorUseCase:
    """Admite um servidor (RN-PES-010/011/012/013)."""

    def __init__(
        self,
        repo: ports.RepositorioServidor,
        cargos: ports.RepositorioCargo,
    ) -> None:
        self._repo = repo
        self._cargos = cargos

    def execute(self, dto: AdmitirServidorInput) -> Servidor:
        """Executa a admissão do servidor."""
        from ..domain.exceptions import RegraNegocioError

        if not dto.matricula:
            raise RegraNegocioError("Matrícula é obrigatória (RN-PES-010)")
        if not dto.cpf or len(dto.cpf) != 11:
            raise RegraNegocioError("CPF inválido (RN-PES-011)")
        if not dto.nome:
            raise RegraNegocioError("Nome do servidor é obrigatório")
        if self._repo.get_by_matricula(dto.matricula) is not None:
            raise RegraNegocioError(f"Matrícula '{dto.matricula}' já utilizada (RN-PES-010)")
        if self._repo.get_by_cpf(dto.cpf) is not None:
            raise RegraNegocioError("CPF já cadastrado (RN-PES-011)")
        if self._cargos.get_by_id(dto.cargo_id) is None:
            raise RegraNegocioError("Cargo inválido para admissão (RN-PES-012)")
        servidor = Servidor(
            matricula=dto.matricula,
            cpf=dto.cpf,
            nome=dto.nome,
            cargo_id=dto.cargo_id,
            tipo_vinculo=TipoVinculo(dto.tipo_vinculo),
            salario=dto.salario,
            data_admissao=dto.data_admissao,
            email=dto.email,
            telefone=dto.telefone,
            created_by=dto.autor_id,
        )
        servidor.admitir()
        return self._repo.save(servidor)


class AfastarServidorUseCase:
    """Registra afastamento de servidor ativo."""

    def __init__(self, repo: ports.RepositorioServidor) -> None:
        self._repo = repo

    def execute(self, servidor_id: str) -> Servidor:
        """Executa o afastamento."""
        from ..domain.exceptions import ServidorNaoEncontradoError

        servidor = self._repo.get_by_id(servidor_id)
        if servidor is None:
            raise ServidorNaoEncontradoError("Servidor não encontrado")
        servidor.afastar()
        return self._repo.save(servidor)


class ReativarServidorUseCase:
    """Reativa servidor afastado."""

    def __init__(self, repo: ports.RepositorioServidor) -> None:
        self._repo = repo

    def execute(self, servidor_id: str) -> Servidor:
        """Executa a reativação."""
        from ..domain.exceptions import ServidorNaoEncontradoError

        servidor = self._repo.get_by_id(servidor_id)
        if servidor is None:
            raise ServidorNaoEncontradoError("Servidor não encontrado")
        servidor.reativar()
        return self._repo.save(servidor)


@dataclass
class DesligarServidorInput:
    """DTO de desligamento."""

    servidor_id: str
    data_desligamento: date | None = None


class DesligarServidorUseCase:
    """Desliga servidor (exoneração/demissão)."""

    def __init__(self, repo: ports.RepositorioServidor) -> None:
        self._repo = repo

    def execute(self, dto: DesligarServidorInput) -> Servidor:
        """Executa o desligamento."""
        from ..domain.exceptions import ServidorNaoEncontradoError

        servidor = self._repo.get_by_id(dto.servidor_id)
        if servidor is None:
            raise ServidorNaoEncontradoError("Servidor não encontrado")
        servidor.desligar(dto.data_desligamento)
        return self._repo.save(servidor)


__all__ = [
    "CriarCargoInput",
    "CriarCargoUseCase",
    "AdmitirServidorInput",
    "AdmitirServidorUseCase",
    "AfastarServidorUseCase",
    "ReativarServidorUseCase",
    "DesligarServidorInput",
    "DesligarServidorUseCase",
]
