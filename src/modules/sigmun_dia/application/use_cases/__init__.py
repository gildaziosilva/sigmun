"""Use Cases de DOM-DIA - Gestão de Diárias, Viagens e Deslocamentos."""

from dataclasses import dataclass
from datetime import date, datetime

from ...domain.entities import CategoriaDiaria, Diaria, PrestacaoContas, StatusDiaria, Viagem
from ...domain.exceptions import (
    DiariaNaoEncontradaError,
    DiariaPendenteAutorizacaoError,
    PrestacaoContasNaoEncontradaError,
    RegraNegocioError,
    ViagemCategoriaInvalidaError,
    ViagemNaoEncontradaError,
    ViagemSemDiariasError,
)


# =============================================================================
# Input/Output DTOs
# =============================================================================


@dataclass
class CriarViagemInputDTO:
    """DTO de entrada para criação de viagem."""

    servidor_id: str = ""
    dota_id: str = ""
    motivo: str = ""
    cargo_ocupado: str = ""
    unidade_origem_id: str = ""
    unidade_destino_id: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str = ""
    is_antecipacao: bool = False
    created_by: str = ""


@dataclass
class CriarViagemOutputDTO:
    """DTO de saída para criação de viagem."""

    id: str
    servidor_id: str
    dota_id: str
    motivo: str
    is_antecipacao: bool
    data_inicio: date | None = None
    data_fim: date | None = None


@dataclass
class AtualizarViagemInputDTO:
    """DTO de entrada para atualização de viagem."""

    id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    motivo: str = ""
    cargo_ocupado: str = ""
    unidade_origem_id: str = ""
    unidade_destino_id: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str = ""
    is_antecipacao: bool = False


@dataclass
class AtualizarViagemOutputDTO:
    """DTO de saída para atualização de viagem."""

    id: str
    servidor_id: str
    dota_id: str
    motivo: str
    data_inicio: date | None = None
    data_fim: date | None = None


@dataclass
class CriarDiariaInputDTO:
    """DTO de entrada para criação de diária."""

    viagem_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    categoria: str = ""
    descricao: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float = 0.0
    valor_total: float = 0.0
    created_by: str = ""


@dataclass
class CriarDiariaOutputDTO:
    """DTO de saída para criação de diária."""

    id: str
    viagem_id: str
    servidor_id: str
    dota_id: str
    categoria: str
    descricao: str
    status: str
    valor_diaria: float
    valor_total: float
    created_at: datetime


@dataclass
class AtualizarDiariaInputDTO:
    """DTO de entrada para atualização de diária."""

    id: str = ""
    categoria: str = ""
    descricao: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float = 0.0
    valor_total: float = 0.0


@dataclass
class AtualizarDiariaOutputDTO:
    """DTO de saída para atualização de diária."""

    id: str
    categoria: str
    descricao: str
    status: str
    valor_diaria: float
    valor_total: float


@dataclass
class CriarPrestacaoContasInputDTO:
    """DTO de entrada para criação de prestação de contas."""

    diaria_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    documento_id: str = ""
    valor_previsto: float = 0.0
    valor_apresentado: float = 0.0
    data_vencimento: datetime | None = None
    autor_id: str = ""


@dataclass
class CriarPrestacaoContasOutputDTO:
    """DTO de saída para criação de prestação de contas."""

    id: str
    diaria_id: str
    servidor_id: str
    dota_id: str
    documento_id: str
    valor_previsto: float
    valor_apresentado: float
    valor_liquido: float
    status: str
    created_at: datetime


@dataclass
class AprovacaoPrestacaoInputDTO:
    """DTO de entrada para aprovação de prestação de contas."""

    diaria_id: str = ""
    autor_id: str = ""


@dataclass
class AprovacaoPrestacaoOutputDTO:
    """DTO de saída para aprovação de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_liquido: float
    data_aprovacao: datetime


@dataclass
class GlosagemPrestacaoInputDTO:
    """DTO de entrada para glosagem de prestação de contas."""

    diaria_id: str = ""
    motivo: str = ""
    valor_glosado: float = 0.0
    autor_id: str = ""


@dataclass
class GlosagemPrestacaoOutputDTO:
    """DTO de saída para glosagem de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_glosado: float
    valor_liquido: float
    motivo_glosa: str
    data_glosa: datetime


@dataclass
class RestituicaPrestacaoInputDTO:
    """DTO de entrada para restituição de prestação de contas."""

    diaria_id: str = ""
    autor_id: str = ""


@dataclass
class RestituicaPrestacaoOutputDTO:
    """DTO de saída para restituição de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_glosado: float
    valor_liquido: float
    data_restituicao: datetime


@dataclass
class SolicitacaoDiariaInput:
    """DTO de solicitação de diária."""
    
    servidor_id: str = ""
    dota_id: str = ""
    viagem_id: str = ""
    categoria: str = ""
    descricao: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    valor_diaria: float = 0.0
    autor_id: str = ""


# =============================================================================
@dataclass
class SolicitarViagemInput:
    """DTO de entrada para solicitar/tramitar/visitar uma viagem.

    Campos opcionais permitem reuso em diferentes etapas:
    - Solicitação: servidor, dotação, motivo, destino e datas.
    - Tramitação: unidades de origem/destino.
    - Visitação: data de visita, visitante e observações.
    """

    viagem_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    motivo: str = ""
    cargo_ocupado: str = ""
    unidade_origem_id: str = ""
    unidade_destino_id: str = ""
    data_inicio: date | None = None
    data_fim: date | None = None
    destino: str = ""
    is_antecipacao: bool = False
    data_visita: date | None = None
    visitante_id: str = ""
    observacoes: str = ""
    autor_id: str = ""


# =============================================================================
# Use Cases de Viagem
# =============================================================================


class CriarViagemUseCase:
    """Caso de uso para criar uma nova viagem."""

    def __init__(self, repositorio_viagem):
        self._repo = repositorio_viagem

    def execute(self, dto: SolicitarViagemInput) -> Viagem:
        """Cria uma nova viagem e retorna a entidade persistida."""
        viagem = Viagem(
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            motivo=dto.motivo,
            cargo_ocupado=dto.cargo_ocupado,
            unidade_origem_id=dto.unidade_origem_id,
            unidade_destino_id=dto.unidade_destino_id,
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            destino=dto.destino,
            is_antecipacao=dto.is_antecipacao,
            created_by=dto.autor_id,
        )
        return self._repo.save(viagem)


class AtualizarViagemUseCase:
    """Caso de uso para atualizar uma viagem existente."""

    def __init__(self, repositorio_viagem):
        self._repo = repositorio_viagem

    def execute(self, dto: AtualizarViagemInputDTO) -> AtualizarViagemOutputDTO:
        """Atualiza uma viagem existente."""
        viagem = self._repo.get_by_id(dto.id)
        if not viagem:
            raise ViagemNaoEncontradaError(f"Viagem {dto.id} não encontrada")
        
        viagem.servidor_id = dto.servidor_id
        viagem.dota_id = dto.dota_id
        viagem.motivo = dto.motivo
        viagem.cargo_ocupado = dto.cargo_ocupado
        viagem.unidade_origem_id = dto.unidade_origem_id
        viagem.unidade_destino_id = dto.unidade_destino_id
        viagem.data_inicio = dto.data_inicio
        viagem.data_fim = dto.data_fim
        viagem.destino = dto.destino
        viagem.is_antecipacao = dto.is_antecipacao
        
        viagem_atualizada = self._repo.save(viagem)
        return AtualizarViagemOutputDTO(
            id=viagem_atualizada.id,
            servidor_id=viagem_atualizada.servidor_id,
            dota_id=viagem_atualizada.dota_id,
            motivo=viagem_atualizada.motivo,
            data_inicio=viagem_atualizada.data_inicio,
            data_fim=viagem_atualizada.data_fim,
        )


# =============================================================================
# Use Cases de Diária
# =============================================================================


class CriarDiariaUseCase:
    """Caso de uso para criar uma diária."""

    def __init__(self, repositorio_diaria, repositorio_viagem):
        self._repo_diaria = repositorio_diaria
        self._repo_viagem = repositorio_viagem

    def execute(self, dto: SolicitacaoDiariaInput) -> Diaria:
        """Cria uma nova diária a partir de uma solicitação."""
        categoria = CategoriaDiaria(dto.categoria) if dto.categoria else CategoriaDiaria.EVENTO
        diaria = Diaria(
            viagem_id=dto.viagem_id,
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            categoria=categoria,
            descricao=dto.descricao,
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            valor_diaria=dto.valor_diaria,
            created_by=dto.autor_id,
        )
        return self._repo_diaria.save(diaria)


class AtualizarDiariaUseCase:
    """Caso de uso para atualizar uma diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, dto: AtualizarDiariaInputDTO) -> AtualizarDiariaOutputDTO:
        """Atualiza uma diária."""
        diaria = self._repo.get_by_id(dto.id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.id} não encontrada")
        
        if dto.categoria:
            diaria.categoria = CategoriaDiaria(dto.categoria)
        if dto.descricao:
            diaria.descricao = dto.descricao
        if dto.data_inicio:
            diaria.data_inicio = dto.data_inicio
        if dto.data_fim:
            diaria.data_fim = dto.data_fim
        if dto.valor_diaria:
            diaria.valor_diaria = dto.valor_diaria
        
        diaria_atualizada = self._repo.save(diaria)
        return AtualizarDiariaOutputDTO(
            id=diaria_atualizada.id,
            categoria=diaria_atualizada.categoria.value,
            descricao=diaria_atualizada.descricao,
            status=diaria_atualizada.status.value,
            valor_diaria=diaria_atualizada.valor_diaria,
            valor_total=diaria_atualizada.valor_total,
        )


# =============================================================================
# Use Cases de Transição de Diária
# =============================================================================


class AutorizarDiariaUseCase:
    """Caso de uso para autorizar uma diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, autor_id: str = "") -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.autorizar(diaria.valor_diaria)
        return self._repo.save(diaria)


class CriarPrestacaoContasUseCase:
    """Caso de uso para criar uma prestação de contas (abertura)."""

    def __init__(self, repositorio_prestacao, repositorio_diaria):
        self._repo_prestacao = repositorio_prestacao
        self._repo_diaria = repositorio_diaria

    def execute(self, dto: CriarPrestacaoContasInputDTO) -> PrestacaoContas:
        """Cria uma nova prestação de contas para uma diária paga."""
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.diaria_id} não encontrada")
        if diaria.status not in (StatusDiaria.PAGA,):
            raise RegraNegocioError("Prestação de contas só pode ser aberta para diárias pagas")

        prestacao = PrestacaoContas(
            diaria_id=dto.diaria_id,
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            documento_id=dto.documento_id,
            valor_previsto=dto.valor_previsto,
            valor_apresentado=dto.valor_apresentado,
            data_vencimento=dto.data_vencimento,
            created_by=dto.autor_id,
        )
        return self._repo_prestacao.save(prestacao)


class AprovarPrestacaoUseCase:
    """Caso de uso para aprovar uma prestação de contas.

    RN-DIA-015: Aprovação requer:
    - Diária em estado PAGA
    - Prestação de contas aberta
    """

    def __init__(self, repositorio_diaria, repositorio_prestacao):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: AprovacaoPrestacaoInputDTO) -> PrestacaoContas:
        """Aprova uma prestação de contas e retorna a entidade persistida."""
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.diaria_id} não encontrada")

        prestacao = self._repo_prestacao.get_by_diaria(dto.diaria_id)
        if not prestacao:
            raise PrestacaoContasNaoEncontradaError(
                f"Prestação de contas para diária {dto.diaria_id} não encontrada"
            )

        if getattr(diaria, "status", "") != StatusDiaria.PAGA:
            raise RegraNegocioError(
                f"Diária deve estar em estado PAGA para aprovar prestação"
            )
        if prestacao.status != "aberta":
            raise RegraNegocioError("Apenas prestações abertas podem ser aprovadas")

        prestacao.aprovar(dto.autor_id)
        return self._repo_prestacao.save(prestacao)


class GlosarPrestacaoUseCase:
    """Caso de uso para glosar uma prestação de contas.

    RN-DIA-016: Glosa requer:
    - Diária em estado PAGA
    - Prestação de contas aberta
    - Motivo da glosa (obrigatório)
    - Valor glosado (0 = glosa total)
    """

    def __init__(self, repositorio_diaria, repositorio_prestacao):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: GlosagemPrestacaoInputDTO) -> PrestacaoContas:
        """Glosa uma prestação de contas e retorna a entidade persistida."""
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.diaria_id} não encontrada")

        prestacao = self._repo_prestacao.get_by_diaria(dto.diaria_id)
        if not prestacao:
            raise PrestacaoContasNaoEncontradaError(
                f"Prestação de contas para diária {dto.diaria_id} não encontrada"
            )

        if getattr(diaria, "status", "") != StatusDiaria.PAGA:
            raise RegraNegocioError("Diária deve estar em estado PAGA para glosar prestação")
        if prestacao.status != "aberta":
            raise RegraNegocioError("Apenas prestações abertas podem ser glosadas")
        if not dto.motivo:
            raise RegraNegocioError("Motivo da glosa é obrigatório (RN-DIA-016)")
        if dto.valor_glosado < 0:
            raise RegraNegocioError("Valor glosado não pode ser negativo")
        if dto.valor_glosado > prestacao.valor_apresentado:
            raise RegraNegocioError(
                f"Valor glosado ({dto.valor_glosado}) não pode exceder valor apresentado ({prestacao.valor_apresentado})"
            )

        prestacao.glosar(dto.motivo, dto.valor_glosado, dto.autor_id)
        return self._repo_prestacao.save(prestacao)


class RestituirPrestacaoUseCase:
    """Caso de uso para restituir valor glosado.

    RN-DIA-017: Restituição requer:
    - Diária em estado PAGA
    - Prestação de contas em estado GLOSADA
    """

    def __init__(self, repositorio_diaria, repositorio_prestacao):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: RestituicaPrestacaoInputDTO) -> PrestacaoContas:
        """Restitui o valor glosado e retorna a entidade persistida."""
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.diaria_id} não encontrada")

        prestacao = self._repo_prestacao.get_by_diaria(dto.diaria_id)
        if not prestacao:
            raise PrestacaoContasNaoEncontradaError(
                f"Prestação de contas para diária {dto.diaria_id} não encontrada"
            )

        if getattr(diaria, "status", "") != StatusDiaria.PAGA:
            raise RegraNegocioError("Diária deve estar em estado PAGA para restituir")
        if prestacao.status != "glosa":
            raise RegraNegocioError(
                "Apenas prestações em estado 'glosa' podem ser restituídas"
            )
        if prestacao.valor_glosado <= 0:
            raise RegraNegocioError("Não há valor glosado para restituir")

        prestacao.restituir(dto.autor_id)
        return self._repo_prestacao.save(prestacao)


class CalcularDiariaUseCase:
    """Caso de uso para calcular o valor da diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str) -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.calcular(diaria.valor_total or diaria.valor_diaria)
        return self._repo.save(diaria)


class ConcederDiariaUseCase:
    """Caso de uso para confirmar concessão da diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, data_inicio: date | None = None, data_fim: date | None = None, autor_id: str = "") -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        if data_inicio:
            diaria.data_inicio = data_inicio
        if data_fim:
            diaria.data_fim = data_fim
        diaria.conceder()
        return self._repo.save(diaria)


class IniciarPrestacaoUseCase:
    """Caso de uso para iniciar a prestação de contas."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, autor_id: str = "") -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.iniciar_prestacao()
        return self._repo.save(diaria)


class PagarDiariaUseCase:
    """Caso de uso para registrar pagamento da diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, autor_id: str = "") -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.pagar()
        return self._repo.save(diaria)


class CancelarDiariaUseCase:
    """Caso de uso para cancelar uma diária."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, motivo: str, autor_id: str = "") -> Diaria:
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.cancelar(motivo)
        return self._repo.save(diaria)


# =============================================================================
# Use Cases de Transição de Viagem
# =============================================================================


class TramitarViagemUseCase:
    """Caso de uso para tramitar uma viagem entre unidades."""

    def __init__(self, repositorio_viagem):
        self._repo = repositorio_viagem

    def execute(self, dto: SolicitarViagemInput) -> Viagem:
        viagem = self._repo.get_by_id(dto.viagem_id)
        if not viagem:
            raise ViagemNaoEncontradaError(f"Viagem {dto.viagem_id} não encontrada")
        viagem.tramitar_para(dto.unidade_destino_id, dto.autor_id)
        return self._repo.save(viagem)


class VisitarViagemUseCase:
    """Caso de uso para registrar visita em viagem (registra chegada)."""

    def __init__(self, repositorio_viagem):
        self._repo = repositorio_viagem

    def execute(self, dto: SolicitarViagemInput) -> Viagem:
        viagem = self._repo.get_by_id(dto.viagem_id)
        if not viagem:
            raise ViagemNaoEncontradaError(f"Viagem {dto.viagem_id} não encontrada")
        from datetime import datetime

        viagem.visitar(
            data_visita=dto.data_visita or datetime.utcnow(),
            visitante_id=dto.visitante_id,
            autor_id=dto.autor_id,
        )
        return self._repo.save(viagem)


class SolicitarDiariaUseCase:
    """Caso de uso para solicitar uma diária (cria e registra a solicitação)."""

    def __init__(self, repositorio_diaria, repositorio_viagem=None):
        self._repo_diaria = repositorio_diaria
        self._repo_viagem = repositorio_viagem

    def execute(self, dto: SolicitacaoDiariaInput) -> Diaria:
        """Cria uma diária a partir de uma solicitação."""
        diaria = Diaria(
            viagem_id=dto.viagem_id,
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            categoria=CategoriaDiaria(dto.categoria) if dto.categoria else CategoriaDiaria.EVENTO,
            descricao=dto.descricao,
            data_inicio=dto.data_inicio,
            data_fim=dto.data_fim,
            valor_diaria=dto.valor_diaria,
        )
        diaria.solicitar()
        diaria_salva = self._repo_diaria.save(diaria)
        return diaria_salva


class ConfirmarConcessaoUseCase:
    """Caso de uso para confirmar a concessão da diária (RN-DIA-006)."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, data_inicio: date | None = None, data_fim: date | None = None, autor_id: str = "") -> Diaria:
        """Confirma a concessão da diária."""
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        if data_inicio:
            diaria.data_inicio = data_inicio
        if data_fim:
            diaria.data_fim = data_fim
        diaria.conceder()
        return self._repo.save(diaria)


class ReverterParaPagamentoUseCase:
    """Caso de uso para reverter a diária para pagamento (RN-DIA-008)."""

    def __init__(self, repositorio_diaria):
        self._repo = repositorio_diaria

    def execute(self, diaria_id: str, autor_id: str = "") -> Diaria:
        """Registra/reverte a diária para o estado PAGA."""
        diaria = self._repo.get_by_id(diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {diaria_id} não encontrada")
        diaria.pagar()
        return self._repo.save(diaria)


__all__ = [
    # DTOs de Viagem
    "CriarViagemInputDTO",
    "CriarViagemOutputDTO",
    "AtualizarViagemInputDTO",
    "AtualizarViagemOutputDTO",
    "SolicitarViagemInput",
    "CriarViagemUseCase",
    "AtualizarViagemUseCase",
    "TramitarViagemUseCase",
    "VisitarViagemUseCase",
    # DTOs de Diaria
    "CriarDiariaInputDTO",
    "CriarDiariaOutputDTO",
    "AtualizarDiariaInputDTO",
    "AtualizarDiariaOutputDTO",
    "SolicitacaoDiariaInput",
    "CriarDiariaUseCase",
    "AtualizarDiariaUseCase",
    "SolicitarDiariaUseCase",
    # DTOs de PrestacaoContas
    "CriarPrestacaoContasInputDTO",
    "CriarPrestacaoContasOutputDTO",
    "CriarPrestacaoContasUseCase",
    # DTOs de Aprovação de Prestação
    "AprovacaoPrestacaoInputDTO",
    "AprovacaoPrestacaoOutputDTO",
    "AprovarPrestacaoUseCase",
    # DTOs de Glosa de Prestação
    "GlosagemPrestacaoInputDTO",
    "GlosagemPrestacaoOutputDTO",
    "GlosarPrestacaoUseCase",
    # DTOs de Restituição de Prestação
    "RestituicaPrestacaoInputDTO",
    "RestituicaPrestacaoOutputDTO",
    "RestituirPrestacaoUseCase",
    # Use Cases de Transição de Diária
    "AutorizarDiariaUseCase",
    "CalcularDiariaUseCase",
    "ConcederDiariaUseCase",
    "IniciarPrestacaoUseCase",
    "PagarDiariaUseCase",
    "ConfirmarConcessaoUseCase",
    "ReverterParaPagamentoUseCase",
    "CancelarDiariaUseCase",
]
