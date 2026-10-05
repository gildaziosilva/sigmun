"""Serviços de domínio de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import uuid4

from src.modules.sigmun_ate.domain.entities import (
    Atendimento,
    AvaliacaoAtendimento,
    Chamada,
    Encaminhamento,
    FilaAtendimento,
    Guiche,
    Senha,
    StatusAtendimento,
    StatusSenha,
    Triagem,
    UnidadeAtendimento,
)
from src.modules.sigmun_ate.domain.value_objects import (
    NotaAvaliacao,
    Prioridade,
    TempoEspera,
)


@dataclass
class ServicoTriagem:
    """Serviço de domínio para triagem de atendimentos."""

    def classificar(
        self,
        servico_id: str,
        observacao: str = "",
        prioridade: int = 2,
    ) -> Triagem:
        """Cria uma nova triagem."""
        return Triagem(
            servico_id=servico_id,
            data_hora=datetime.utcnow(),
            classificacao=servico_id,
            prioridade=prioridade,
            observacao=observacao,
        )

    def recalcular_prioridade(self, triagem: Triagem, nova_prioridade: int) -> None:
        """Recalcula prioridade da triagem."""
        if 1 <= nova_prioridade <= 4:
            triagem.prioridade = nova_prioridade
            triagem.updated_at = datetime.utcnow()


@dataclass
class ServicoFila:
    """Serviço de domínio para gestão de filas."""

    def abrir_fila(
        self,
        unidade_id: str,
        servico_id: str,
        data: datetime,
    ) -> FilaAtendimento:
        """Abre uma nova fila de atendimento."""
        return FilaAtendimento(
            unidade_id=unidade_id,
            servico_id=servico_id,
            data=data,
            status="aberta",
        )

    def fechar_fila(self, fila: FilaAtendimento) -> None:
        """Fecha uma fila de atendimento."""
        fila.status = "fechada"
        fila.updated_at = datetime.utcnow()

    def proxima_senha(self, fila: FilaAtendimento, senhas_emitidas: list) -> int:
        """Calcula o próximo número da senha na fila."""
        senhas_fila = [s for s in senhas_emitidas if s.fila_id == fila.id]
        if not senhas_fila:
            return 1
        return max(int(s.numero) for s in senhas_fila if s.numero.isdigit()) + 1


@dataclass
class ServicoSenha:
    """Serviço de domínio para emissão e gestão de senhas."""

    def emitir_senha(
        self,
        fila_id: str,
        servico_id: str,
        triagem_id: str,
        numero: int,
        prioridade: int = 2,
    ) -> Senha:
        """Emite uma nova senha."""
        return Senha(
            fila_id=fila_id,
            servico_id=servico_id,
            triagem_id=triagem_id,
            numero=str(numero).zfill(4),
            data_hora_emissao=datetime.utcnow(),
            prioridade=prioridade,
            status=StatusSenha.EMITIDA,
        )

    def chamar_senha(
        self,
        senha: Senha,
        guiche_id: str,
        unidade_id: str,
        operador: str,
        ordem: int,
    ) -> Chamada:
        """Chama uma senha para atendimento."""
        senha.status = StatusSenha.CHAMADA
        senha.updated_at = datetime.utcnow()

        return Chamada(
            senha_id=senha.id,
            guiche_id=guiche_id,
            unidade_id=unidade_id,
            operador=operador,
            data_hora=datetime.utcnow(),
            ordem=ordem,
            tentativa=1,
        )

    def rechamar_senha(self, senha: Senha, chamada_anterior: Chamada) -> Chamada:
        """Rechama uma senha (incrementa tentativa)."""
        senha.status = StatusSenha.RECHAMADA
        senha.updated_at = datetime.utcnow()

        return Chamada(
            senha_id=senha.id,
            guiche_id=chamada_anterior.guiche_id,
            unidade_id=chamada_anterior.unidade_id,
            operador=chamada_anterior.operador,
            data_hora=datetime.utcnow(),
            ordem=chamada_anterior.ordem,
            tentativa=chamada_anterior.tentativa + 1,
        )

    def marcar_atendida(self, senha: Senha) -> None:
        """Marca senha como atendida."""
        senha.status = StatusSenha.ATENDIDA
        senha.updated_at = datetime.utcnow()

    def marcar_nao_compareceu(self, senha: Senha) -> None:
        """Marca senha como não compareceu."""
        senha.status = StatusSenha.NAO_COMPARECEU
        senha.updated_at = datetime.utcnow()

    def cancelar_senha(self, senha: Senha) -> None:
        """Cancela uma senha."""
        senha.status = StatusSenha.CANCELADA
        senha.updated_at = datetime.utcnow()


@dataclass
class ServicoAtendimento:
    """Serviço de domínio para atendimentos."""

    def iniciar_atendimento(self, chamada_id: str, canal_id: str) -> Atendimento:
        """Inicia um atendimento a partir de uma chamada."""
        return Atendimento(
            chamada_id=chamada_id,
            canal_id=canal_id,
            inicio=datetime.utcnow(),
            status=StatusAtendimento.EM_ANDAMENTO,
        )

    def concluir_atendimento(self, atendimento: Atendimento, descricao: str) -> None:
        """Conclui um atendimento."""
        atendimento.fim = datetime.utcnow()
        atendimento.status = StatusAtendimento.CONCLUIDO
        atendimento.descricao = descricao
        atendimento.updated_at = datetime.utcnow()

    def cancelar_atendimento(self, atendimento: Atendimento, motivo: str) -> None:
        """Cancela um atendimento."""
        atendimento.fim = datetime.utcnow()
        atendimento.status = StatusAtendimento.CANCELADO
        atendimento.descricao = f"Cancelado: {motivo}"
        atendimento.updated_at = datetime.utcnow()


@dataclass
class ServicoAvaliacao:
    """Serviço de domínio para avaliações de atendimento."""

    def registrar_avaliacao(
        self,
        atendimento_id: str,
        nota: int,
        comentario: str = "",
    ) -> AvaliacaoAtendimento:
        """Registra uma avaliação."""
        return AvaliacaoAtendimento(
            atendimento_id=atendimento_id,
            nota=nota,
            comentario=comentario,
            data_hora=datetime.utcnow(),
        )


@dataclass
class ServicoEncaminhamento:
    """Serviço de domínio para encaminhamentos."""

    def criar_encaminhamento(
        self,
        atendimento_id: str,
        destino: str,
        motivo: str,
    ) -> Encaminhamento:
        """Cria um encaminhamento."""
        return Encaminhamento(
            atendimento_id=atendimento_id,
            destino=destino,
            motivo=motivo,
            status="pendente",
        )

    def concluir_encaminhamento(self, encaminhamento: Encaminhamento) -> None:
        """Marca encaminhamento como concluído."""
        encaminhamento.status = "concluido"
        encaminhamento.updated_at = datetime.utcnow()


@dataclass
class ServicoTempoEspera:
    """Serviço de domínio para cálculo de tempo de espera."""

    def calcular_tempo_medio(
        self,
        fila: FilaAtendimento,
        chamadas_recentes: list,
    ) -> TempoEspera:
        """Calcula tempo médio de espera baseado em chamadas recentes."""
        # Placeholder - implementar cálculo real
        return TempoEspera(minutos=15)

    def estimar_tempo_fila(
        self,
        posicao_na_fila: int,
        tempo_medio_atendimento: int = 15,
    ) -> TempoEspera:
        """Estima tempo de espera baseado na posição na fila."""
        return TempoEspera(minutos=posicao_na_fila * tempo_medio_atendimento)


__all__ = [
    "ServicoTriagem",
    "ServicoFila",
    "ServicoSenha",
    "ServicoAtendimento",
    "ServicoAvaliacao",
    "ServicoEncaminhamento",
    "ServicoTempoEspera",
]
