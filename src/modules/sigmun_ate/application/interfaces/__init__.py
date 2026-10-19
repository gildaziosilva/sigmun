"""Interfaces de aplicação de Atendimento ao Cidadão (DOM-ATE)."""

from abc import ABC, abstractmethod

from src.modules.sigmun_ate.domain.entities import (
    Atendimento,
    AvaliacaoAtendimento,
    Chamada,
    Encaminhamento,
    FilaAtendimento,
    Guiche,
    Senha,
    ServicoAtendimento,
    Triagem,
    UnidadeAtendimento,
)
from src.modules.sigmun_ate.domain.value_objects import TempoEspera


class RepositorioTriagem(ABC):
    """Interface do repositório de triagens."""

    @abstractmethod
    def salvar(self, triagem) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Triagem | None: ...

    @abstractmethod
    def listar_por_servico(self, servico_id: str) -> list[Triagem]: ...


class RepositorioFila(ABC):
    """Interface do repositório de filas."""

    @abstractmethod
    def salvar(self, fila: FilaAtendimento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> FilaAtendimento | None: ...

    @abstractmethod
    def buscar_aberta(self, unidade_id: str, servico_id: str) -> FilaAtendimento | None: ...

    @abstractmethod
    def listar_por_unidade(self, unidade_id: str) -> list[FilaAtendimento]: ...


class RepositorioSenha(ABC):
    """Interface do repositório de senhas."""

    @abstractmethod
    def salvar(self, senha: Senha) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Senha | None: ...

    @abstractmethod
    def buscar_por_numero(self, numero: str) -> Senha | None: ...

    @abstractmethod
    def listar_por_fila(self, fila_id: str) -> list[Senha]: ...

    @abstractmethod
    def listar_emitidas_hoje(self, fila_id: str) -> list[Senha]: ...


class RepositorioChamada(ABC):
    """Interface do repositório de chamadas."""

    @abstractmethod
    def salvar(self, chamada: Chamada) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Chamada | None: ...

    @abstractmethod
    def buscar_por_senha(self, senha_id: str) -> list[Chamada]: ...

    @abstractmethod
    def listar_por_guiche(self, guiche_id: str) -> list[Chamada]: ...


class RepositorioAtendimento(ABC):
    """Interface do repositório de atendimentos."""

    @abstractmethod
    def salvar(self, atendimento: Atendimento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Atendimento | None: ...

    @abstractmethod
    def buscar_por_chamada(self, chamada_id: str) -> Atendimento | None: ...

    @abstractmethod
    def listar_em_andamento(self) -> list[Atendimento]: ...


class RepositorioAvaliacao(ABC):
    """Interface do repositório de avaliações."""

    @abstractmethod
    def salvar(self, avaliacao: AvaliacaoAtendimento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> AvaliacaoAtendimento | None: ...

    @abstractmethod
    def buscar_por_atendimento(self, atendimento_id: str) -> AvaliacaoAtendimento | None: ...


class RepositorioEncaminhamento(ABC):
    """Interface do repositório de encaminhamentos."""

    @abstractmethod
    def salvar(self, encaminhamento: Encaminhamento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Encaminhamento | None: ...

    @abstractmethod
    def buscar_por_atendimento(self, atendimento_id: str) -> list[Encaminhamento]: ...

    @abstractmethod
    def listar_pendentes(self) -> list[Encaminhamento]: ...


class RepositorioGuiche(ABC):
    """Interface do repositório de guichês."""

    @abstractmethod
    def salvar(self, guiche: Guiche) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> Guiche | None: ...

    @abstractmethod
    def listar_por_unidade(self, unidade_id: str) -> list[Guiche]: ...

    @abstractmethod
    def listar_ativos(self, unidade_id: str) -> list[Guiche]: ...


class RepositorioUnidadeAtendimento(ABC):
    """Interface do repositório de unidades de atendimento."""

    @abstractmethod
    def salvar(self, unidade: UnidadeAtendimento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> UnidadeAtendimento | None: ...

    @abstractmethod
    def buscar_por_codigo(self, codigo: str) -> UnidadeAtendimento | None: ...

    @abstractmethod
    def listar_ativas(self) -> list[UnidadeAtendimento]: ...


class RepositorioServicoAtendimento(ABC):
    """Interface do repositório de serviços de atendimento."""

    @abstractmethod
    def salvar(self, servico: ServicoAtendimento) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: str) -> ServicoAtendimento | None: ...

    @abstractmethod
    def buscar_por_codigo(self, codigo: str) -> ServicoAtendimento | None: ...

    @abstractmethod
    def listar_ativos(self) -> list[ServicoAtendimento]: ...


class PublicadorEventos(ABC):
    """Interface para publicação de eventos de domínio."""

    @abstractmethod
    def publicar(self, evento) -> None: ...


class ServicoTempoEsperaExterno(ABC):
    """Interface para serviço externo de tempo de espera."""

    @abstractmethod
    def obter_tempo_estimado(self, fila_id: str) -> int: ...

    @abstractmethod
    def notificar_espera(self, senha_id: str, tempo_estimado: int) -> None: ...


__all__ = [
    "RepositorioTriagem",
    "RepositorioFila",
    "RepositorioSenha",
    "RepositorioChamada",
    "RepositorioAtendimento",
    "RepositorioAvaliacao",
    "RepositorioEncaminhamento",
    "RepositorioGuiche",
    "RepositorioUnidadeAtendimento",
    "RepositorioServicoAtendimento",
    "PublicadorEventos",
    "ServicoTempoEsperaExterno",
]
