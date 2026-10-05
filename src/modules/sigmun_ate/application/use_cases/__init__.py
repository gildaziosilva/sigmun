"""Casos de uso de Atendimento ao Cidadão (DOM-ATE) - Parte 1: Triagem e Fila."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from uuid import uuid4

from src.modules.sigmun_ate.application.interfaces import (
    PublicadorEventos,
    RepositorioAtendimento,
    RepositorioAvaliacao,
    RepositorioChamada,
    RepositorioEncaminhamento,
    RepositorioFila,
    RepositorioGuiche,
    RepositorioSenha,
    RepositorioServicoAtendimento,
    RepositorioTriagem,
    RepositorioUnidadeAtendimento,
)
from src.modules.sigmun_ate.domain.entities import (
    Atendimento,
    AvaliacaoAtendimento,
    Chamada,
    Encaminhamento,
    FilaAtendimento,
    Guiche,
    Senha,
    ServicoAtendimento,
    StatusAtendimento,
    StatusSenha,
    Triagem,
    UnidadeAtendimento,
)
from src.modules.sigmun_ate.domain.events import (
    AtendimentoCancelado,
    AtendimentoConcluido,
    AtendimentoIniciado,
    AvaliacaoRegistrada,
    EncaminhamentoCriado,
    EncaminhamentoConcluido,
    FilaAberta,
    FilaFechada,
    SenhaAtendida,
    SenhaCancelada,
    SenhaChamada,
    SenhaEmitida,
    SenhaNaoCompareceu,
    SenhaRechamada,
    TriagemRealizada,
)
from src.modules.sigmun_ate.domain.exceptions import (
    AtendimentoInvalidoError,
    AtendimentoJaConcluidoError,
    AtendimentoNaoIniciadoError,
    AvaliacaoInvalidaError,
    AvaliacaoJaRegistradaError,
    CanalInvalidoError,
    EncaminhamentoInvalidoError,
    EncaminhamentoJaConcluidoError,
    FilaFechadaError,
    FilaInvalidaError,
    GuicheInvalidoError,
    GuicheInativoError,
    MaximoRechamadasError,
    OperadorInvalidoError,
    SenhaAtendidaError,
    SenhaCanceladaError,
    SenhaInvalidaError,
    SenhaJaChamadaError,
    SenhaNaoChamadaError,
    UnidadeInvalidaError,
)
from src.modules.sigmun_ate.domain.services import (
    ServicoAtendimento as DomainServicoAtendimento,
    ServicoAvaliacao as DomainServicoAvaliacao,
    ServicoEncaminhamento as DomainServicoEncaminhamento,
    ServicoFila as DomainServicoFila,
    ServicoSenha as DomainServicoSenha,
    ServicoTriagem as DomainServicoTriagem,
)


# =============================================================================
# Triagem
# =============================================================================

@dataclass
class RealizarTriagemInputDTO:
    servico_id: str
    observacao: str = ""
    prioridade: int = 2


@dataclass
class RealizarTriagemOutputDTO:
    triagem_id: str
    servico_id: str
    prioridade: int


class RealizarTriagemUseCase:
    """Caso de uso: Realizar triagem de atendimento."""

    def __init__(
        self,
        repo_triagem: RepositorioTriagem,
        repo_servico: RepositorioServicoAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_triagem = repo_triagem
        self._repo_servico = repo_servico
        self._eventos = eventos
        self._domain = DomainServicoTriagem()

    def execute(self, input_dto: RealizarTriagemInputDTO) -> RealizarTriagemOutputDTO:
        servico = self._repo_servico.buscar_por_id(input_dto.servico_id)
        if not servico:
            raise ValueError("Serviço não encontrado")

        triagem = self._domain.classificar(
            servico_id=input_dto.servico_id,
            observacao=input_dto.observacao,
            prioridade=input_dto.prioridade,
        )

        self._repo_triagem.salvar(triagem)

        self._eventos.publicar(
            TriagemRealizada(
                aggregate_id=triagem.id,
                servico_id=input_dto.servico_id,
                prioridade=input_dto.prioridade,
                observacao=input_dto.observacao,
            )
        )

        return RealizarTriagemOutputDTO(
            triagem_id=triagem.id,
            servico_id=input_dto.servico_id,
            prioridade=input_dto.prioridade,
        )


# =============================================================================
# Fila
# =============================================================================

@dataclass
class AbrirFilaInputDTO:
    unidade_id: str
    servico_id: str


@dataclass
class AbrirFilaOutputDTO:
    fila_id: str
    unidade_id: str
    servico_id: str


class AbrirFilaUseCase:
    """Caso de uso: Abrir fila de atendimento."""

    def __init__(
        self,
        repo_fila: RepositorioFila,
        repo_unidade: RepositorioUnidadeAtendimento,
        repo_servico: RepositorioServicoAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_fila = repo_fila
        self._repo_unidade = repo_unidade
        self._repo_servico = repo_servico
        self._eventos = eventos
        self._domain = DomainServicoFila()

    def execute(self, input_dto: AbrirFilaInputDTO):
        unidade = self._repo_unidade.buscar_por_id(input_dto.unidade_id)
        if not unidade or not unidade.esta_ativo:
            raise ValueError("Unidade inválida")

        servico = self._repo_servico.buscar_por_id(input_dto.servico_id)
        if not servico or not servico.esta_ativo:
            raise ValueError("Serviço inválido ou inativo")

        fila_existente = self._repo_fila.buscar_aberta(
            input_dto.unidade_id, input_dto.servico_id
        )
        if fila_existente:
            raise ValueError("Já existe fila aberta")

        fila = DomainServicoFila().abrir_fila(
            unidade_id=input_dto.unidade_id,
            servico_id=input_dto.servico_id,
            data=datetime.utcnow(),
        )

        self._repo_fila.salvar(fila)

        self._eventos.publicar(
            FilaAberta(
                aggregate_id=fila.id,
                unidade_id=input_dto.unidade_id,
                servico_id=input_dto.servico_id,
                data=fila.data.isoformat(),
            )
        )

        return type("AbrirFilaOutputDTO", (), {
            "fila_id": fila.id,
            "unidade_id": input_dto.unidade_id,
            "servico_id": input_dto.servico_id,
        })()


@dataclass
class FecharFilaInputDTO:
    fila_id: str


@dataclass
class FecharFilaOutputDTO:
    fila_id: str


class FecharFilaUseCase:
    """Caso de uso: Fechar fila de atendimento."""

    def __init__(
        self,
        repo_fila: RepositorioFila,
        eventos: PublicadorEventos,
    ):
        self._repo_fila = repo_fila
        self._eventos = eventos
        self._domain = DomainServicoFila()

    def execute(self, input_dto):
        fila = self._repo_fila.buscar_por_id(input_dto.fila_id)
        if not fila:
            raise ValueError("Fila inválida")

        self._domain.fechar_fila(fila)
        self._repo_fila.salvar(fila)

        self._eventos.publicar(FilaFechada(aggregate_id=fila.id))

        return type("FecharFilaOutputDTO", (), {"fila_id": fila.id})()


# =============================================================================
# Senha
# =============================================================================

@dataclass
class EmitirSenhaInputDTO:
    fila_id: str
    servico_id: str
    triagem_id: str


@dataclass
class EmitirSenhaOutputDTO:
    senha_id: str
    numero: str
    fila_id: str


class EmitirSenhaUseCase:
    """Caso de uso: Emitir senha de atendimento."""

    def __init__(
        self,
        repo_senha: RepositorioSenha,
        repo_fila: RepositorioFila,
        repo_servico: RepositorioServicoAtendimento,
        repo_triagem: RepositorioTriagem,
        eventos: PublicadorEventos,
    ):
        self._repo_senha = repo_senha
        self._repo_fila = repo_fila
        self._repo_servico = repo_servico
        self._repo_triagem = repo_triagem
        self._eventos = eventos
        self._domain = DomainServicoSenha()

    def execute(self, input_dto: EmitirSenhaInputDTO) -> EmitirSenhaOutputDTO:
        fila = self._repo_fila.buscar_por_id(input_dto.fila_id)
        if not fila or not fila.esta_aberta:
            raise ValueError("Fila fechada")

        servico = self._repo_servico.buscar_por_id(input_dto.servico_id)
        if not servico:
            raise ValueError("Serviço não encontrado")

        triagem = self._repo_triagem.buscar_por_id(input_dto.triagem_id)
        if not triagem:
            raise ValueError("Triagem não encontrada")

        senhas_emitidas = self._repo_senha.listar_emitidas_hoje(input_dto.fila_id)
        numero = DomainServicoSenha().proxima_senha(fila, senhas_emitidas)

        senha = DomainServicoSenha().emitir_senha(
            fila_id=input_dto.fila_id,
            servico_id=input_dto.servico_id,
            triagem_id=input_dto.triagem_id,
            numero=numero,
            prioridade=triagem.prioridade,
        )

        self._repo_senha.salvar(senha)

        from src.modules.sigmun_ate.domain.events import SenhaEmitida
        self._eventos.publicar(
            SenhaEmitida(
                aggregate_id=senha.id,
                fila_id=input_dto.fila_id,
                servico_id=input_dto.servico_id,
                triagem_id=input_dto.triagem_id,
                numero=senha.numero,
                prioridade=triagem.prioridade,
            )
        )

        return EmitirSenhaOutputDTO(
            senha_id=senha.id,
            numero=senha.numero,
            fila_id=input_dto.fila_id,
        )


# =============================================================================
# Chamar / Rechamar / Atender Senha
# =============================================================================

@dataclass
class ChamarSenhaInputDTO:
    senha_id: str
    guiche_id: str
    unidade_id: str
    operador: str


@dataclass
class ChamarSenhaOutputDTO:
    chamada_id: str
    senha_id: str
    guiche_id: str
    ordem: int


class ChamarSenhaUseCase:
    """Caso de uso: Chamar senha para atendimento."""

    def __init__(
        self,
        repo_senha: RepositorioSenha,
        repo_chamada: RepositorioChamada,
        repo_guiche: RepositorioGuiche,
        repo_unidade: RepositorioUnidadeAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_senha = repo_senha
        self._repo_chamada = repo_chamada
        self._repo_guiche = repo_guiche
        self._repo_unidade = repo_unidade
        self._eventos = eventos
        self._domain = DomainServicoSenha()

    def execute(self, input_dto: ChamarSenhaInputDTO) -> ChamarSenhaOutputDTO:
        senha = self._repo_senha.buscar_por_id(input_dto.senha_id)
        if not senha:
            raise ValueError("Senha inválida")

        if senha.status != StatusSenha.EMITIDA:
            raise ValueError("Senha não pode ser chamada")

        guiche = self._repo_guiche.buscar_por_id(input_dto.guiche_id)
        if not guiche or not guiche.esta_ativo:
            raise ValueError("Guichê inválido ou inativo")

        unidade = self._repo_unidade.buscar_por_id(input_dto.unidade_id)
        if not unidade:
            raise ValueError("Unidade inválida")

        chamadas_hoje = self._repo_chamada.listar_por_guiche(input_dto.guiche_id)
        ordem = len(chamadas_hoje) + 1

        chamada = self._domain.chamar_senha(
            senha=senha,
            guiche_id=input_dto.guiche_id,
            unidade_id=input_dto.unidade_id,
            operador=input_dto.operador,
            ordem=ordem,
        )

        self._repo_senha.salvar(senha)
        self._repo_chamada.salvar(chamada)

        from src.modules.sigmun_ate.domain.events import SenhaChamada
        self._eventos.publicar(
            SenhaChamada(
                aggregate_id=senha.id,
                guiche_id=input_dto.guiche_id,
                unidade_id=input_dto.unidade_id,
                operador=input_dto.operador,
                ordem=ordem,
                tentativa=1,
            )
        )

        return ChamarSenhaOutputDTO(
            chamada_id=chamada.id,
            senha_id=senha.id,
            guiche_id=input_dto.guiche_id,
            ordem=ordem,
        )


@dataclass
class RechamarSenhaInputDTO:
    senha_id: str


@dataclass
class RechamarSenhaOutputDTO:
    chamada_id: str
    tentativa: int


class RechamarSenhaUseCase:
    """Caso de uso: Rechamar senha."""

    def __init__(
        self,
        repo_senha: RepositorioSenha,
        repo_chamada: RepositorioChamada,
        eventos: PublicadorEventos,
    ):
        self._repo_senha = repo_senha
        self._repo_chamada = repo_chamada
        self._eventos = eventos
        self._domain = DomainServicoSenha()

    def execute(self, input_dto: RechamarSenhaInputDTO) -> RechamarSenhaOutputDTO:
        senha = self._repo_senha.buscar_por_id(input_dto.senha_id)
        if not senha:
            raise ValueError("Senha inválida")

        chamadas = self._repo_chamada.buscar_por_senha(senha.id)
        if not chamadas:
            raise ValueError("Senha não foi chamada")

        ultima_chamada = chamadas[-1]
        if ultima_chamada.tentativa >= 3:
            raise ValueError("Máximo de rechamadas atingido")

        chamada = self._domain.rechamar_senha(senha, ultima_chamada)

        self._repo_senha.salvar(senha)
        self._repo_chamada.salvar(chamada)

        from src.modules.sigmun_ate.domain.events import SenhaRechamada
        self._eventos.publicar(
            SenhaRechamada(
                aggregate_id=senha.id,
                guiche_id=ultima_chamada.guiche_id,
                unidade_id=ultima_chamada.unidade_id,
                operador=ultima_chamada.operador,
                ordem=ultima_chamada.ordem,
                tentativa=chamada.tentativa,
            )
        )

        return RechamarSenhaOutputDTO(
            chamada_id=chamada.id,
            tentativa=chamada.tentativa,
        )


@dataclass
class MarcarSenhaAtendidaInputDTO:
    senha_id: str


@dataclass
class MarcarSenhaAtendidaOutputDTO:
    senha_id: str


class MarcarSenhaAtendidaUseCase:
    """Caso de uso: Marcar senha como atendida."""

    def __init__(
        self,
        repo_senha: RepositorioSenha,
        eventos: PublicadorEventos,
    ):
        self._repo_senha = repo_senha
        self._eventos = eventos
        self._domain = DomainServicoSenha()

    def execute(self, input_dto: MarcarSenhaAtendidaInputDTO):
        senha = self._repo_senha.buscar_por_id(input_dto.senha_id)
        if not senha:
            raise ValueError("Senha inválida")

        if senha.status == StatusSenha.ATENDIDA:
            raise ValueError("Senha já atendida")

        self._domain.marcar_atendida(senha)
        self._repo_senha.salvar(senha)

        from src.modules.sigmun_ate.domain.events import SenhaAtendida
        self._eventos.publicar(SenhaAtendida(aggregate_id=senha.id))

        return type("MarcarSenhaAtendidaOutputDTO", (), {"senha_id": senha.id})()


# =============================================================================
# Atendimento
# =============================================================================

@dataclass
class IniciarAtendimentoInputDTO:
    chamada_id: str
    canal_id: str


@dataclass
class IniciarAtendimentoOutputDTO:
    atendimento_id: str


class IniciarAtendimentoUseCase:
    """Caso de uso: Iniciar atendimento."""

    def __init__(
        self,
        repo_atendimento: RepositorioAtendimento,
        repo_chamada: RepositorioChamada,
        eventos: PublicadorEventos,
    ):
        self._repo_atendimento = repo_atendimento
        self._repo_chamada = repo_chamada
        self._eventos = eventos
        self._domain = DomainServicoAtendimento()

    def execute(self, input_dto: IniciarAtendimentoInputDTO) -> IniciarAtendimentoOutputDTO:
        chamada = self._repo_chamada.buscar_por_id(input_dto.chamada_id)
        if not chamada:
            raise ValueError("Chamada não encontrada")

        existente = self._repo_atendimento.buscar_por_chamada(input_dto.chamada_id)
        if existente:
            raise ValueError("Já existe atendimento para esta chamada")

        atendimento = self._domain.iniciar_atendimento(
            chamada_id=input_dto.chamada_id,
            canal_id=input_dto.canal_id,
        )

        self._repo_atendimento.salvar(atendimento)

        self._eventos.publicar(
            AtendimentoIniciado(
                aggregate_id=atendimento.id,
                chamada_id=input_dto.chamada_id,
                canal_id=input_dto.canal_id,
            )
        )

        return IniciarAtendimentoOutputDTO(atendimento_id=atendimento.id)


@dataclass
class ConcluirAtendimentoInputDTO:
    atendimento_id: str
    descricao: str


@dataclass
class ConcluirAtendimentoOutputDTO:
    atendimento_id: str
    duracao_segundos: int


class ConcluirAtendimentoUseCase:
    """Caso de uso: Concluir atendimento."""

    def __init__(
        self,
        repo_atendimento: RepositorioAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_atendimento = repo_atendimento
        self._eventos = eventos
        self._domain = DomainServicoAtendimento()

    def execute(self, input_dto: ConcluirAtendimentoInputDTO) -> ConcluirAtendimentoOutputDTO:
        atendimento = self._repo_atendimento.buscar_por_id(input_dto.atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado")

        if atendimento.status == StatusAtendimento.CONCLUIDO:
            raise ValueError("Atendimento já concluído")

        if atendimento.status != StatusAtendimento.EM_ANDAMENTO:
            raise ValueError("Atendimento não está em andamento")

        duracao = atendimento.duracao_segundos or 0
        self._domain.concluir_atendimento(atendimento, input_dto.descricao)
        self._repo_atendimento.salvar(atendimento)

        self._eventos.publicar(
            AtendimentoConcluido(
                aggregate_id=atendimento.id,
                descricao=input_dto.descricao,
                duracao_segundos=duracao,
            )
        )

        return ConcluirAtendimentoOutputDTO(
            atendimento_id=atendimento.id,
            duracao_segundos=duracao,
        )


@dataclass
class CancelarAtendimentoInputDTO:
    atendimento_id: str
    motivo: str


@dataclass
class CancelarAtendimentoOutputDTO:
    atendimento_id: str


class CancelarAtendimentoUseCase:
    """Caso de uso: Cancelar atendimento."""

    def __init__(
        self,
        repo_atendimento: RepositorioAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_atendimento = repo_atendimento
        self._eventos = eventos
        self._domain = DomainServicoAtendimento()

    def execute(self, input_dto: CancelarAtendimentoInputDTO) -> CancelarAtendimentoOutputDTO:
        atendimento = self._repo_atendimento.buscar_por_id(input_dto.atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado")

        if atendimento.status == StatusAtendimento.CONCLUIDO:
            raise ValueError("Atendimento já concluído")

        self._domain.cancelar_atendimento(atendimento, input_dto.motivo)
        self._repo_atendimento.salvar(atendimento)

        self._eventos.publicar(
            AtendimentoCancelado(
                aggregate_id=atendimento.id,
                motivo=input_dto.motivo,
            )
        )

        return CancelarAtendimentoOutputDTO(atendimento_id=atendimento.id)


# =============================================================================
# Avaliação
# =============================================================================

@dataclass
class RegistrarAvaliacaoInputDTO:
    atendimento_id: str
    nota: int
    comentario: str = ""


@dataclass
class RegistrarAvaliacaoOutputDTO:
    avaliacao_id: str


class RegistrarAvaliacaoUseCase:
    """Caso de uso: Registrar avaliação de atendimento."""

    def __init__(
        self,
        repo_avaliacao: RepositorioAvaliacao,
        repo_atendimento: RepositorioAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_avaliacao = repo_avaliacao
        self._repo_atendimento = repo_atendimento
        self._eventos = eventos
        self._domain = DomainServicoAvaliacao()

    def execute(self, input_dto: RegistrarAvaliacaoInputDTO) -> RegistrarAvaliacaoOutputDTO:
        atendimento = self._repo_atendimento.buscar_por_id(input_dto.atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado")

        if not 1 <= input_dto.nota <= 5:
            raise ValueError("Nota deve estar entre 1 e 5")

        existente = self._repo_avaliacao.buscar_por_atendimento(input_dto.atendimento_id)
        if existente:
            raise ValueError("Avaliação já registrada")

        avaliacao = self._domain.registrar_avaliacao(
            atendimento_id=input_dto.atendimento_id,
            nota=input_dto.nota,
            comentario=input_dto.comentario,
        )

        self._repo_avaliacao.salvar(avaliacao)

        from src.modules.sigmun_ate.domain.events import AvaliacaoRegistrada
        self._eventos.publicar(
            AvaliacaoRegistrada(
                aggregate_id=avaliacao.id,
                nota=input_dto.nota,
                comentario=input_dto.comentario,
            )
        )

        return RegistrarAvaliacaoOutputDTO(avaliacao_id=avaliacao.id)


# =============================================================================
# Encaminhamento
# =============================================================================

@dataclass
class CriarEncaminhamentoInputDTO:
    atendimento_id: str
    destino: str
    motivo: str


@dataclass
class CriarEncaminhamentoOutputDTO:
    encaminhamento_id: str


class CriarEncaminhamentoUseCase:
    """Caso de uso: Criar encaminhamento."""

    def __init__(
        self,
        repo_encaminhamento: RepositorioEncaminhamento,
        repo_atendimento: RepositorioAtendimento,
        eventos: PublicadorEventos,
    ):
        self._repo_encaminhamento = repo_encaminhamento
        self._repo_atendimento = repo_atendimento
        self._eventos = eventos
        self._domain = DomainServicoEncaminhamento()

    def execute(self, input_dto: CriarEncaminhamentoInputDTO):
        atendimento = self._repo_atendimento.buscar_por_id(input_dto.atendimento_id)
        if not atendimento:
            raise ValueError("Atendimento não encontrado")

        encaminhamento = self._domain.criar_encaminhamento(
            atendimento_id=input_dto.atendimento_id,
            destino=input_dto.destino,
            motivo=input_dto.motivo,
        )

        self._repo_encaminhamento.salvar(encaminhamento)

        from src.modules.sigmun_ate.domain.events import EncaminhamentoCriado
        self._eventos.publicar(
            EncaminhamentoCriado(
                aggregate_id=encaminhamento.id,
                destino=input_dto.destino,
                motivo=input_dto.motivo,
            )
        )

        return type("CriarEncaminhamentoOutputDTO", (), {"encaminhamento_id": encaminhamento.id})()


@dataclass
class ConcluirEncaminhamentoInputDTO:
    encaminhamento_id: str


@dataclass
class ConcluirEncaminhamentoOutputDTO:
    encaminhamento_id: str


class ConcluirEncaminhamentoUseCase:
    """Caso de uso: Concluir encaminhamento."""

    def __init__(
        self,
        repo_encaminhamento: RepositorioEncaminhamento,
        eventos: PublicadorEventos,
    ):
        self._repo_encaminhamento = repo_encaminhamento
        self._eventos = eventos
        self._domain = DomainServicoEncaminhamento()

    def execute(self, input_dto):
        encaminhamento = self._repo_encaminhamento.buscar_por_id(input_dto.encaminhamento_id)
        if not encaminhamento:
            raise ValueError("Encaminhamento não encontrado")

        if encaminhamento.status == "concluido":
            raise ValueError("Encaminhamento já concluído")

        from src.modules.sigmun_ate.domain.services import ServicoEncaminhamento
        DomainServicoEncaminhamento().concluir_encaminhamento(encaminhamento)
        self._repo_encaminhamento.salvar(encaminhamento)

        from src.modules.sigmun_ate.domain.events import EncaminhamentoConcluido
        self._eventos.publicar(EncaminhamentoConcluido(aggregate_id=encaminhamento.id))

        return type("ConcluirEncaminhamentoOutputDTO", (), {"encaminhamento_id": encaminhamento.id})()


__all__ = [
    "RealizarTriagemUseCase",
    "AbrirFilaUseCase",
    "FecharFilaUseCase",
    "EmitirSenhaUseCase",
    "ChamarSenhaUseCase",
    "RechamarSenhaUseCase",
    "MarcarSenhaAtendidaUseCase",
    "IniciarAtendimentoUseCase",
    "ConcluirAtendimentoUseCase",
    "CancelarAtendimentoUseCase",
    "RegistrarAvaliacaoUseCase",
    "CriarEncaminhamentoUseCase",
    "ConcluirEncaminhamentoUseCase",
]
