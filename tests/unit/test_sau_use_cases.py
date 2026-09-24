"""Testes de casos de uso do DOM-SAU (Saude Municipal)."""
from __future__ import annotations
from datetime import date
from unittest.mock import MagicMock
import pytest
from src.modules.sigmun_saude.application.interfaces import (RepositorioAgendamento, RepositorioAtendimento, RepositorioDispensacao, RepositorioMedicamento, RepositorioPaciente, RepositorioRegulacao)
from src.modules.sigmun_saude.application.use_cases import (AgendarConsultaInput, AgendarConsultaUseCase, AutorizarRegulacaoUseCase, CadastrarMedicamentoInput, CadastrarMedicamentoUseCase, CadastrarPacienteInput, CadastrarPacienteUseCase, CancelarAgendamentoUseCase, ConfirmarAgendamentoUseCase, DispensarMedicamentoInput, DispensarMedicamentoUseCase, NegarRegulacaoUseCase, RealizarAgendamentoUseCase, RegistrarAtendimentoInput, RegistrarAtendimentoUseCase, ReporEstoqueUseCase, SolicitarRegulacaoInput, SolicitarRegulacaoUseCase)
from src.modules.sigmun_saude.domain.entities.atendimento import Agendamento, StatusAgendamento
from src.modules.sigmun_saude.domain.entities.farmacia_regulacao import Medicamento, Regulacao, StatusRegulacao
from src.modules.sigmun_saude.domain.entities.paciente import Paciente
from src.modules.sigmun_saude.domain.exceptions import (EstoqueInsuficienteError, PacienteJaExistenteError, RegraNegocioError)

def _paciente(cns: str = "123456789012345") -> Paciente:
    return Paciente(nome="Joana SUS", cns=cns)

class TestPaciente:
    def test_cadastra_paciente(self) -> None:
        repo = MagicMock(spec=RepositorioPaciente)
        repo.get_by_cns = MagicMock(return_value=None)
        novo = _paciente(); novo.id = "p-1"
        repo.save = MagicMock(return_value=novo)
        result = CadastrarPacienteUseCase(repo).execute(CadastrarPacienteInput(nome="Joana SUS", cns="123456789012345"))
        assert result.cns == "123456789012345"
        assert result.esta_ativo
    def test_nao_duplica_cns(self) -> None:
        repo = MagicMock(spec=RepositorioPaciente)
        repo.get_by_cns = MagicMock(return_value=_paciente())
        with pytest.raises(PacienteJaExistenteError):
            CadastrarPacienteUseCase(repo).execute(CadastrarPacienteInput(nome="X", cns="123456789012345"))
    def test_cns_invalido(self) -> None:
        repo = MagicMock(spec=RepositorioPaciente)
        repo.get_by_cns = MagicMock(return_value=None)
        repo.save = MagicMock(side_effect=lambda p: (p.validar(), p)[1])
        with pytest.raises(RegraNegocioError):
            CadastrarPacienteUseCase(repo).execute(CadastrarPacienteInput(nome="X", cns="123"))

class TestProntuario:
    def test_registra_atendimento(self) -> None:
        at = MagicMock(spec=RepositorioAtendimento)
        pac = MagicMock(spec=RepositorioPaciente)
        pac.get_by_id = MagicMock(return_value=_paciente())
        at.save = MagicMock(side_effect=lambda a: a)
        result = RegistrarAtendimentoUseCase(at, pac).execute(RegistrarAtendimentoInput(paciente_id="p-1", profissional="Dra. Ana", estabelecimento="UBS Centro"))
        assert result.paciente_id == "p-1"

class TestAgendamento:
    def test_fluxo_agendar_confirmar_realizar(self) -> None:
        ag = MagicMock(spec=RepositorioAgendamento)
        pac = MagicMock(spec=RepositorioPaciente)
        pac.get_by_id = MagicMock(return_value=_paciente())
        ag.save = MagicMock(side_effect=lambda a: a)
        criado = AgendarConsultaUseCase(ag, pac).execute(AgendarConsultaInput(paciente_id="p-1", especialidade="cardiologia"))
        assert criado.status == StatusAgendamento.AGENDADO
        ag.get_by_id = MagicMock(return_value=criado)
        confirmado = ConfirmarAgendamentoUseCase(ag).execute("a-1")
        assert confirmado.status == StatusAgendamento.CONFIRMADO
        realizado = RealizarAgendamentoUseCase(ag).execute("a-1")
        assert realizado.status == StatusAgendamento.REALIZADO
    def test_cancelar(self) -> None:
        ag = MagicMock(spec=RepositorioAgendamento)
        agendamento = Agendamento(paciente_id="p-1", especialidade="pediatria", data=date.today())
        ag.get_by_id = MagicMock(return_value=agendamento)
        ag.save = MagicMock(side_effect=lambda a: a)
        result = CancelarAgendamentoUseCase(ag).execute("a-1", "paciente desistiu")
        assert result.status == StatusAgendamento.CANCELADO

class TestRegulacao:
    def test_solicita_autoriza(self) -> None:
        reg = MagicMock(spec=RepositorioRegulacao)
        pac = MagicMock(spec=RepositorioPaciente)
        pac.get_by_id = MagicMock(return_value=_paciente())
        reg.save = MagicMock(side_effect=lambda r: r)
        criada = SolicitarRegulacaoUseCase(reg, pac).execute(SolicitarRegulacaoInput(paciente_id="p-1", procedimento="ecocardiograma"))
        assert criada.status == StatusRegulacao.SOLICITADA
        reg.get_by_id = MagicMock(return_value=criada)
        autorizada = AutorizarRegulacaoUseCase(reg).execute("r-1")
        assert autorizada.status == StatusRegulacao.AUTORIZADA
    def test_negar(self) -> None:
        reg = MagicMock(spec=RepositorioRegulacao)
        regulacao = Regulacao(paciente_id="p-1", procedimento="ressonancia")
        reg.get_by_id = MagicMock(return_value=regulacao)
        reg.save = MagicMock(side_effect=lambda r: r)
        result = NegarRegulacaoUseCase(reg).execute("r-1", "sem indicacao")
        assert result.status == StatusRegulacao.NEGADA

class TestFarmacia:
    def test_cadastra_repoe_dispensa(self) -> None:
        meds = MagicMock(spec=RepositorioMedicamento)
        disp = MagicMock(spec=RepositorioDispensacao)
        pac = MagicMock(spec=RepositorioPaciente)
        pac.get_by_id = MagicMock(return_value=_paciente())
        med = Medicamento(nome="Losartana 50mg", estoque=100.0, estoque_minimo=10.0)
        meds.save = MagicMock(side_effect=lambda m: m)
        criado = CadastrarMedicamentoUseCase(meds).execute(CadastrarMedicamentoInput(nome="Losartana 50mg", estoque=100.0))
        assert criado.estoque == 100.0
        meds.get_by_id = MagicMock(return_value=med)
        reposto = ReporEstoqueUseCase(meds).execute("m-1", 50.0)
        assert reposto.estoque == 150.0
        disp.save = MagicMock(side_effect=lambda d: d)
        result = DispensarMedicamentoUseCase(disp, meds, pac).execute(DispensarMedicamentoInput(paciente_id="p-1", medicamento_id="m-1", quantidade=20.0))
        assert result.quantidade == 20.0
        assert med.estoque == 130.0
    def test_estoque_insuficiente(self) -> None:
        meds = MagicMock(spec=RepositorioMedicamento)
        disp = MagicMock(spec=RepositorioDispensacao)
        pac = MagicMock(spec=RepositorioPaciente)
        pac.get_by_id = MagicMock(return_value=_paciente())
        meds.get_by_id = MagicMock(return_value=Medicamento(nome="Insulina", estoque=2.0))
        with pytest.raises(EstoqueInsuficienteError):
            DispensarMedicamentoUseCase(disp, meds, pac).execute(DispensarMedicamentoInput(paciente_id="p-1", medicamento_id="m-1", quantidade=10.0))
