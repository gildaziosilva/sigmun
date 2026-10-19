"""Queries CQRS de Atendimento ao Cidadão (DOM-ATE)."""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID


@dataclass
class BuscarTriagemQuery:
    """Query: Buscar triagem por ID."""

    triagem_id: str


@dataclass
class ListarTriagensPorServicoQuery:
    """Query: Listar triagens por serviço."""

    servico_id: str


@dataclass
class BuscarFilaQuery:
    """Query: Buscar fila por ID."""

    fila_id: str


@dataclass
class BuscarFilaAbertaQuery:
    """Query: Buscar fila aberta por unidade e serviço."""

    unidade_id: str
    servico_id: str


@dataclass
class ListarFilasPorUnidadeQuery:
    """Query: Listar filas por unidade."""

    unidade_id: str


@dataclass
class BuscarSenhaQuery:
    """Query: Buscar senha por ID."""

    senha_id: str


@dataclass
class BuscarSenhaPorNumeroQuery:
    """Query: Buscar senha por número."""

    numero: str


@dataclass
class ListarSenhasPorFilaQuery:
    """Query: Listar senhas por fila."""

    fila_id: str


@dataclass
class ListarSenhasEmitidasHojeQuery:
    """Query: Listar senhas emitidas hoje."""

    fila_id: str


@dataclass
class BuscarChamadaQuery:
    """Query: Buscar chamada por ID."""

    chamada_id: str


@dataclass
class ListarChamadasPorSenhaQuery:
    """Query: Listar chamadas por senha."""

    senha_id: str


@dataclass
class ListarChamadasPorGuicheQuery:
    """Query: Listar chamadas por guichê."""

    guiche_id: str


@dataclass
class BuscarAtendimentoQuery:
    """Query: Buscar atendimento por ID."""

    atendimento_id: str


@dataclass
class BuscarAtendimentoPorChamadaQuery:
    """Query: Buscar atendimento por chamada."""

    chamada_id: str


@dataclass
class ListarAtendimentosEmAndamentoQuery:
    """Query: Listar atendimentos em andamento."""


@dataclass
class BuscarAvaliacaoQuery:
    """Query: Buscar avaliação por ID."""

    avaliacao_id: str


@dataclass
class BuscarAvaliacaoPorAtendimentoQuery:
    """Query: Buscar avaliação por atendimento."""

    atendimento_id: str


@dataclass
class BuscarEncaminhamentoQuery:
    """Query: Buscar encaminhamento por ID."""

    encaminhamento_id: str


@dataclass
class ListarEncaminhamentosPorAtendimentoQuery:
    """Query: Listar encaminhamentos por atendimento."""

    atendimento_id: str


@dataclass
class ListarEncaminhamentosPendentesQuery:
    """Query: Listar encaminhamentos pendentes."""


@dataclass
class BuscarGuicheQuery:
    """Query: Buscar guichê por ID."""

    guiche_id: str


@dataclass
class ListarGuichesPorUnidadeQuery:
    """Query: Listar guichês por unidade."""

    unidade_id: str


@dataclass
class ListarGuichesAtivosQuery:
    """Query: Listar guichês ativos."""

    unidade_id: str


@dataclass
class BuscarUnidadeAtendimentoQuery:
    """Query: Buscar unidade de atendimento por ID."""

    unidade_id: str


@dataclass
class BuscarUnidadePorCodigoQuery:
    """Query: Buscar unidade por código."""

    codigo: str


@dataclass
class ListarUnidadesAtivasQuery:
    """Query: Listar unidades ativas."""


@dataclass
class BuscarServicoAtendimentoQuery:
    """Query: Buscar serviço por ID."""

    servico_id: str


@dataclass
class BuscarServicoPorCodigoQuery:
    """Query: Buscar serviço por código."""

    codigo: str


@dataclass
class ListarServicosAtivosQuery:
    """Query: Listar serviços ativos."""


@dataclass
class BuscarTriagemQuery:
    """Query: Buscar triagem por ID."""

    triagem_id: str


@dataclass
class ListarTriagensPorServicoQuery:
    """Query: Listar triagens por serviço."""

    servico_id: str


@dataclass
class ObterTempoEsperaQuery:
    """Query: Obter tempo estimado de espera."""

    fila_id: str


@dataclass
class ListarAtendimentosEmAndamentoQuery:
    """Query: Listar atendimentos em andamento."""


@dataclass
class ObterEstatisticasFilaQuery:
    """Query: Obter estatísticas da fila."""

    fila_id: str


@dataclass
class ObterEstatisticasUnidadeQuery:
    """Query: Obter estatísticas da unidade."""

    unidade_id: str
    data_inicio: datetime | None = None
    data_fim: datetime | None = None


__all__ = [
    "BuscarTriagemQuery",
    "ListarTriagensPorServicoQuery",
    "BuscarFilaQuery",
    "BuscarFilaAbertaQuery",
    "ListarFilasPorUnidadeQuery",
    "BuscarSenhaQuery",
    "BuscarSenhaPorNumeroQuery",
    "ListarSenhasPorFilaQuery",
    "ListarSenhasEmitidasHojeQuery",
    "BuscarChamadaQuery",
    "ListarChamadasPorSenhaQuery",
    "ListarChamadasPorGuicheQuery",
    "BuscarAtendimentoQuery",
    "BuscarAtendimentoPorChamadaQuery",
    "ListarAtendimentosEmAndamentoQuery",
    "BuscarAvaliacaoQuery",
    "BuscarAvaliacaoPorAtendimentoQuery",
    "BuscarEncaminhamentoQuery",
    "ListarEncaminhamentosPorAtendimentoQuery",
    "ListarEncaminhamentosPendentesQuery",
    "BuscarGuicheQuery",
    "ListarGuichesPorUnidadeQuery",
    "ListarGuichesAtivosQuery",
    "BuscarUnidadeAtendimentoQuery",
    "BuscarUnidadePorCodigoQuery",
    "ListarUnidadesAtivasQuery",
    "BuscarServicoAtendimentoQuery",
    "BuscarServicoPorCodigoQuery",
    "ListarServicosAtivosQuery",
    "BuscarTriagemQuery",
    "ListarTriagensPorServicoQuery",
    "ObterTempoEsperaQuery",
    "ListarAtendimentosEmAndamentoQuery",
    "ObterEstatisticasFilaQuery",
    "ObterEstatisticasUnidadeQuery",
]
