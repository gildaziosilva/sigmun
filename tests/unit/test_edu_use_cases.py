"""Testes de casos de uso do DOM-EDU (Educacao Publica)."""
from __future__ import annotations
from datetime import date
from unittest.mock import MagicMock
import pytest
from src.modules.sigmun_educacao.application.interfaces import (RepositorioAluno, RepositorioDistribuicaoMerenda, RepositorioItemMerenda, RepositorioLancamentoDiario, RepositorioMatricula, RepositorioPassagemTransporte, RepositorioRotaTransporte)
from src.modules.sigmun_educacao.application.use_cases import (AtivarRotaTransporteUseCase, CadastrarAlunoInput, CadastrarAlunoUseCase, CadastrarItemMerendaInput, CadastrarItemMerendaUseCase, CadastrarRotaTransporteInput, CadastrarRotaTransporteUseCase, CancelarMatriculaUseCase, ConcluirMatriculaUseCase, DistribuirMerendaInput, DistribuirMerendaUseCase, InativarRotaTransporteUseCase, RealizarMatriculaInput, RealizarMatriculaUseCase, RegistrarLancamentoDiarioInput, RegistrarLancamentoDiarioUseCase, RegistrarPassagemInput, RegistrarPassagemUseCase, ReporEstoqueMerendaUseCase, TransferirMatriculaUseCase)
from src.modules.sigmun_educacao.domain.entities.aluno import Aluno
from src.modules.sigmun_educacao.domain.entities.matricula import Matricula, StatusMatricula
from src.modules.sigmun_educacao.domain.entities.merenda import ItemMerenda
from src.modules.sigmun_educacao.domain.entities.transporte import RotaTransporte, StatusRota
from src.modules.sigmun_educacao.domain.exceptions import (AlunoJaCadastradoError, EstadoMatriculaInvalidoError, EstadoRotaInvalidoError, EstoqueInsuficienteError, MatriculaJaAtivaError, RegraNegocioError, VagaIndisponivelError)

def _aluno(cpf: str = "") -> Aluno:
    return Aluno(nome="Maria Edu", cpf=cpf)

def _matricula_ativa(aluno_id: str = "a-1") -> Matricula:
    return Matricula(aluno_id=aluno_id, escola="E.M. Centro", serie="5 ano", ano_letivo=2026)

class TestAluno:
    def test_cadastra_aluno(self) -> None:
        repo = MagicMock(spec=RepositorioAluno)
        repo.get_by_cpf = MagicMock(return_value=None)
        novo = _aluno(); novo.id = "al-1"
        repo.save = MagicMock(return_value=novo)
        result = CadastrarAlunoUseCase(repo).execute(CadastrarAlunoInput(nome="Maria Edu"))
        assert result.nome == "Maria Edu"
        assert result.esta_ativo
    def test_nao_duplica_cpf(self) -> None:
        repo = MagicMock(spec=RepositorioAluno)
        repo.get_by_cpf = MagicMock(return_value=_aluno(cpf="12345678901"))
        with pytest.raises(AlunoJaCadastradoError):
            CadastrarAlunoUseCase(repo).execute(CadastrarAlunoInput(nome="X", cpf="12345678901"))
    def test_cpf_invalido(self) -> None:
        repo = MagicMock(spec=RepositorioAluno)
        repo.get_by_cpf = MagicMock(return_value=None)
        repo.save = MagicMock(side_effect=lambda a: (a.validar(), a)[1])
        with pytest.raises(RegraNegocioError):
            CadastrarAlunoUseCase(repo).execute(CadastrarAlunoInput(nome="X", cpf="123"))
    def test_nome_obrigatorio(self) -> None:
        repo = MagicMock(spec=RepositorioAluno)
        with pytest.raises(RegraNegocioError):
            CadastrarAlunoUseCase(repo).execute(CadastrarAlunoInput(nome=""))

class TestMatricula:
    def test_realiza_matricula(self) -> None:
        mat = MagicMock(spec=RepositorioMatricula)
        alu = MagicMock(spec=RepositorioAluno)
        alu.get_by_id = MagicMock(return_value=_aluno())
        mat.get_ativa_by_aluno = MagicMock(return_value=None)
        nova = _matricula_ativa(); nova.id = "m-1"
        mat.save = MagicMock(return_value=nova)
        result = RealizarMatriculaUseCase(mat, alu).execute(RealizarMatriculaInput(aluno_id="a-1", escola="E.M. Centro", serie="5 ano"))
        assert result.status == StatusMatricula.ATIVA
        assert result.ano_letivo == date.today().year
    def test_nao_duplica_matricula_ativa(self) -> None:
        mat = MagicMock(spec=RepositorioMatricula)
        alu = MagicMock(spec=RepositorioAluno)
        alu.get_by_id = MagicMock(return_value=_aluno())
        mat.get_ativa_by_aluno = MagicMock(return_value=_matricula_ativa())
        with pytest.raises(MatriculaJaAtivaError):
            RealizarMatriculaUseCase(mat, alu).execute(RealizarMatriculaInput(aluno_id="a-1", escola="E.M. Centro", serie="5 ano"))
    def test_fluxo_matricular_transferir_concluir(self) -> None:
        mat = MagicMock(spec=RepositorioMatricula)
        alu = MagicMock(spec=RepositorioAluno)
        alu.get_by_id = MagicMock(return_value=_aluno())
        mat.get_ativa_by_aluno = MagicMock(return_value=None)
        mat.save = MagicMock(side_effect=lambda m: m)
        criada = RealizarMatriculaUseCase(mat, alu).execute(RealizarMatriculaInput(aluno_id="a-1", escola="E.M. Centro", serie="5 ano"))
        mat.get_by_id = MagicMock(return_value=criada)
        transferida = TransferirMatriculaUseCase(mat).execute("m-1", "E.M. Norte")
        assert transferida.status == StatusMatricula.TRANSFERIDA
        assert transferida.escola_destino == "E.M. Norte"
        ativa = _matricula_ativa()
        mat.get_by_id = MagicMock(return_value=ativa)
        concluida = ConcluirMatriculaUseCase(mat).execute("m-1")
        assert concluida.status == StatusMatricula.CONCLUIDA
    def test_cancelar_e_estado_final(self) -> None:
        mat = MagicMock(spec=RepositorioMatricula)
        cancelada = _matricula_ativa(); cancelada.cancelar("mudanca de cidade")
        assert cancelada.status == StatusMatricula.CANCELADA
        mat.get_by_id = MagicMock(return_value=cancelada)
        mat.save = MagicMock(side_effect=lambda m: m)
        with pytest.raises(EstadoMatriculaInvalidoError):
            CancelarMatriculaUseCase(mat).execute("m-1")

class TestDiario:
    def test_registra_lancamento(self) -> None:
        dia = MagicMock(spec=RepositorioLancamentoDiario)
        mat = MagicMock(spec=RepositorioMatricula)
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        dia.save = MagicMock(side_effect=lambda l: l)
        result = RegistrarLancamentoDiarioUseCase(dia, mat).execute(RegistrarLancamentoDiarioInput(matricula_id="m-1", presente=True, nota=8.5))
        assert result.matricula_id == "m-1"
        assert result.nota == 8.5
        assert result.presente
    def test_matricula_cancelada_bloqueia_lancamento(self) -> None:
        dia = MagicMock(spec=RepositorioLancamentoDiario)
        mat = MagicMock(spec=RepositorioMatricula)
        cancelada = _matricula_ativa(); cancelada.cancelar()
        mat.get_by_id = MagicMock(return_value=cancelada)
        with pytest.raises(EstadoMatriculaInvalidoError):
            RegistrarLancamentoDiarioUseCase(dia, mat).execute(RegistrarLancamentoDiarioInput(matricula_id="m-1"))
    def test_nota_fora_da_escala(self) -> None:
        dia = MagicMock(spec=RepositorioLancamentoDiario)
        mat = MagicMock(spec=RepositorioMatricula)
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        dia.save = MagicMock(side_effect=lambda l: (l.validar(), l)[1])
        with pytest.raises(RegraNegocioError):
            RegistrarLancamentoDiarioUseCase(dia, mat).execute(RegistrarLancamentoDiarioInput(matricula_id="m-1", nota=11.0))

class TestTransporte:
    def test_cadastra_rota_e_passagem(self) -> None:
        rotas = MagicMock(spec=RepositorioRotaTransporte)
        passagens = MagicMock(spec=RepositorioPassagemTransporte)
        mat = MagicMock(spec=RepositorioMatricula)
        rota = RotaTransporte(identificacao="Rota 1", motorista="Joao", vagas=2)
        rotas.save = MagicMock(side_effect=lambda r: r)
        criada = CadastrarRotaTransporteUseCase(rotas).execute(CadastrarRotaTransporteInput(identificacao="Rota 1", motorista="Joao", vagas=2))
        assert criada.status == StatusRota.ATIVA
        rotas.get_by_id = MagicMock(return_value=rota)
        matricula = _matricula_ativa()
        mat.get_by_id = MagicMock(return_value=matricula)
        passagens.count_by_rota_data = MagicMock(return_value=1)
        passagens.save = MagicMock(side_effect=lambda p: p)
        result = RegistrarPassagemUseCase(passagens, rotas, mat).execute(RegistrarPassagemInput(rota_id="r-1", matricula_id="m-1"))
        assert result.rota_id == rota.id
        assert result.matricula_id == matricula.id
    def test_sem_vaga_disponivel(self) -> None:
        rotas = MagicMock(spec=RepositorioRotaTransporte)
        passagens = MagicMock(spec=RepositorioPassagemTransporte)
        mat = MagicMock(spec=RepositorioMatricula)
        rotas.get_by_id = MagicMock(return_value=RotaTransporte(identificacao="Lotada", motorista="Joao", vagas=1))
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        passagens.count_by_rota_data = MagicMock(return_value=1)
        with pytest.raises(VagaIndisponivelError):
            RegistrarPassagemUseCase(passagens, rotas, mat).execute(RegistrarPassagemInput(rota_id="r-1", matricula_id="m-1"))
    def test_rota_inativa_bloqueia_passagem_e_reativacao(self) -> None:
        rotas = MagicMock(spec=RepositorioRotaTransporte)
        passagens = MagicMock(spec=RepositorioPassagemTransporte)
        mat = MagicMock(spec=RepositorioMatricula)
        inativa = RotaTransporte(identificacao="Rota 2", motorista="Joao", vagas=5)
        inativa.status = StatusRota.INATIVA
        rotas.get_by_id = MagicMock(return_value=inativa)
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        with pytest.raises(EstadoRotaInvalidoError):
            RegistrarPassagemUseCase(passagens, rotas, mat).execute(RegistrarPassagemInput(rota_id="r-1", matricula_id="m-1"))
        rotas.save = MagicMock(side_effect=lambda r: r)
        reativada = AtivarRotaTransporteUseCase(rotas).execute("r-1")
        assert reativada.status == StatusRota.ATIVA


class TestMerenda:
    def test_cadastra_repoe_distribui(self) -> None:
        itens = MagicMock(spec=RepositorioItemMerenda)
        dist = MagicMock(spec=RepositorioDistribuicaoMerenda)
        mat = MagicMock(spec=RepositorioMatricula)
        item = ItemMerenda(nome="Frango", estoque=50.0, estoque_minimo=10.0)
        itens.save = MagicMock(side_effect=lambda i: i)
        criado = CadastrarItemMerendaUseCase(itens).execute(CadastrarItemMerendaInput(nome="Frango", estoque=50.0))
        assert criado.estoque == 50.0
        itens.get_by_id = MagicMock(return_value=item)
        reposto = ReporEstoqueMerendaUseCase(itens).execute("i-1", 20.0)
        assert reposto.estoque == 70.0
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        dist.save = MagicMock(side_effect=lambda d: d)
        result = DistribuirMerendaUseCase(dist, itens, mat).execute(DistribuirMerendaInput(matricula_id="m-1", item_id="i-1", quantidade=30.0))
        assert result.quantidade == 30.0
        assert item.estoque == 40.0
    def test_estoque_insuficiente(self) -> None:
        itens = MagicMock(spec=RepositorioItemMerenda)
        dist = MagicMock(spec=RepositorioDistribuicaoMerenda)
        mat = MagicMock(spec=RepositorioMatricula)
        mat.get_by_id = MagicMock(return_value=_matricula_ativa())
        itens.get_by_id = MagicMock(return_value=ItemMerenda(nome="Leite", estoque=5.0))
        with pytest.raises(EstoqueInsuficienteError):
            DistribuirMerendaUseCase(dist, itens, mat).execute(DistribuirMerendaInput(matricula_id="m-1", item_id="i-1", quantidade=50.0))
    def test_inativar_rota(self) -> None:
        rotas = MagicMock(spec=RepositorioRotaTransporte)
        rota = RotaTransporte(identificacao="Rota 3", motorista="Joao", vagas=3)
        rotas.get_by_id = MagicMock(return_value=rota)
        rotas.save = MagicMock(side_effect=lambda r: r)
        result = InativarRotaTransporteUseCase(rotas).execute("r-1")
        assert result.status == StatusRota.INATIVA

