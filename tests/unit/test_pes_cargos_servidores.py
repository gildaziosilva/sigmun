"""Testes de cargos e servidores (DOM-PES)."""

from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioCargo,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_cargos_servidores import (
    AdmitirServidorInput,
    AdmitirServidorUseCase,
    AfastarServidorUseCase,
    CriarCargoInput,
    CriarCargoUseCase,
    DesligarServidorUseCase,
    DesligarServidorInput,
    ReativarServidorUseCase,
)
from src.modules.sigmun_rh.domain.entities.cargo import Cargo
from src.modules.sigmun_rh.domain.entities.servidor import (
    Servidor,
    StatusServidor,
    TipoVinculo,
)


def _cargo() -> Cargo:
    return Cargo(id="cargo-1", codigo="ANL", nome="Analista",
                 salario_base=3000.0)


def _servidor(status=StatusServidor.ATIVO) -> Servidor:
    return Servidor(
        id="serv-1", matricula="001", cpf="12345678901", nome="Maria",
        cargo_id="cargo-1", tipo_vinculo=TipoVinculo.EFETIVO,
        status=status, data_admissao=date(2024, 1, 10), salario=3000.0,
    )


class TestCargo:
    """Criacao de cargos."""

    def test_criar_cargo(self) -> None:
        """Cria cargo com codigo unico."""
        repo = MagicMock(spec=RepositorioCargo)
        repo.get_by_codigo = MagicMock(return_value=None)
        repo.save = MagicMock(return_value=_cargo())
        uc = CriarCargoUseCase(repo)
        dto = CriarCargoInput(codigo="ANL", nome="Analista",
                              salario_base=3000.0)
        result = uc.execute(dto)
        assert result.codigo == "ANL"
        repo.save.assert_called_once()

    def test_codigo_duplicado(self) -> None:
        """Codigo duplicado gera erro."""
        repo = MagicMock(spec=RepositorioCargo)
        repo.get_by_codigo = MagicMock(return_value=_cargo())
        uc = CriarCargoUseCase(repo)
        with pytest.raises(Exception):
            uc.execute(CriarCargoInput(codigo="ANL", nome="X",
                                       salario_base=100.0))


class TestServidor:
    """Admissao e transicoes de servidor."""

    def test_admitir(self) -> None:
        """Admite servidor com cargo valido."""
        repo = MagicMock(spec=RepositorioServidor)
        repo.get_by_matricula = MagicMock(return_value=None)
        repo.get_by_cpf = MagicMock(return_value=None)
        repo.save = MagicMock(return_value=_servidor())
        cargos = MagicMock(spec=RepositorioCargo)
        cargos.get_by_id = MagicMock(return_value=_cargo())
        uc = AdmitirServidorUseCase(repo, cargos)
        dto = AdmitirServidorInput(
            matricula="001", cpf="12345678901", nome="Maria",
            cargo_id="cargo-1", data_admissao=date(2024, 1, 10),
        )
        result = uc.execute(dto)
        assert result.matricula == "001"
        repo.save.assert_called_once()

    def test_afastar_e_reativar(self) -> None:
        """Afastamento e reativacao."""
        serv = _servidor()
        repo = MagicMock(spec=RepositorioServidor)
        repo.get_by_id = MagicMock(return_value=serv)
        repo.save = MagicMock(return_value=serv)
        AfastarServidorUseCase(repo).execute("serv-1")
        assert serv.status == StatusServidor.AFASTADO
        ReativarServidorUseCase(repo).execute("serv-1")
        assert serv.status == StatusServidor.ATIVO

    def test_desligar(self) -> None:
        """Desligamento de efetivo exonera."""
        serv = _servidor()
        repo = MagicMock(spec=RepositorioServidor)
        repo.get_by_id = MagicMock(return_value=serv)
        repo.save = MagicMock(return_value=serv)
        result = DesligarServidorUseCase(repo).execute(
            DesligarServidorInput(servidor_id="serv-1",
                                  data_desligamento=date(2024, 6, 1))
        )
        assert result.status == StatusServidor.EXONERADO
