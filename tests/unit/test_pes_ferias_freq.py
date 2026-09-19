"""Testes de ferias e frequencia (DOM-PES)."""

from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioFerias,
    RepositorioFrequencia,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_ferias import (
    AprovarFeriasUseCase,
    ConcluirFeriasUseCase,
    IniciarGozoFeriasUseCase,
    PlanejarFeriasInput,
    PlanejarFeriasUseCase,
)
from src.modules.sigmun_rh.application.use_cases_frequencia import (
    JustificarFaltaInput,
    JustificarFaltaUseCase,
    RegistrarFrequenciaInput,
    RegistrarFrequenciaUseCase,
)
from src.modules.sigmun_rh.domain.entities.ferias import Ferias, StatusFerias
from src.modules.sigmun_rh.domain.entities.frequencia import (
    Frequencia,
    TipoFrequencia,
)
from src.modules.sigmun_rh.domain.entities.servidor import Servidor


def _servidor() -> Servidor:
    return Servidor(id="s1", matricula="001", cpf="12345678901",
                    nome="Ana", cargo_id="c1",
                    data_admissao=date(2024, 1, 1))


class TestFerias:
    """Ciclo de ferias."""

    def test_ciclo(self) -> None:
        """Planeja, aprova, goza e conclui."""
        servidores = MagicMock(spec=RepositorioServidor)
        servidores.get_by_id = MagicMock(return_value=_servidor())
        repo = MagicMock(spec=RepositorioFerias)
        ferias = Ferias(id="fe1", servidor_id="s1", dias=30)
        repo.save = MagicMock(return_value=ferias)
        repo.get_by_id = MagicMock(return_value=ferias)
        PlanejarFeriasUseCase(repo, servidores).execute(
            PlanejarFeriasInput(servidor_id="s1", dias=30)
        )
        AprovarFeriasUseCase(repo).execute("fe1")
        assert ferias.status == StatusFerias.APROVADA
        IniciarGozoFeriasUseCase(repo).execute("fe1")
        ConcluirFeriasUseCase(repo).execute("fe1")
        assert ferias.status == StatusFerias.CONCLUIDA


class TestFrequencia:
    """Frequencia diaria."""

    def test_falta_desconto(self) -> None:
        """Falta gera desconto em folha."""
        servidores = MagicMock(spec=RepositorioServidor)
        servidores.get_by_id = MagicMock(return_value=_servidor())
        repo = MagicMock(spec=RepositorioFrequencia)
        repo.get_por_servidor_data = MagicMock(return_value=None)
        freq = Frequencia(id="fr1", servidor_id="s1",
                          data=date(2024, 3, 1),
                          tipo=TipoFrequencia.FALTA)
        freq.marcar_desconto()
        repo.save = MagicMock(return_value=freq)
        result = RegistrarFrequenciaUseCase(repo, servidores).execute(
            RegistrarFrequenciaInput(servidor_id="s1",
                                     data=date(2024, 3, 1),
                                     tipo="falta")
        )
        assert result.desconto_folha is True

    def test_justificar(self) -> None:
        """Justificativa remove desconto."""
        repo = MagicMock(spec=RepositorioFrequencia)
        freq = Frequencia(id="fr1", servidor_id="s1",
                          data=date(2024, 3, 1),
                          tipo=TipoFrequencia.FALTA,
                          desconto_folha=True)
        repo.get_by_id = MagicMock(return_value=freq)
        repo.save = MagicMock(return_value=freq)
        result = JustificarFaltaUseCase(repo).execute(
            JustificarFaltaInput(frequencia_id="fr1",
                                 justificativa="atestado")
        )
        assert result.tipo == TipoFrequencia.FALTA_JUSTIFICADA
