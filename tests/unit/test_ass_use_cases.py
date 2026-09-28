"""Testes de casos de uso do DOM-ASS (Assistência Social)."""
from __future__ import annotations
from datetime import date
from unittest.mock import MagicMock
import pytest
from src.modules.sigmun_assistencia_social.application.interfaces import (RepositorioAtendimento, RepositorioBeneficio, RepositorioFamilia, RepositorioPessoa, RepositorioUnidade)
from src.modules.sigmun_assistencia_social.application.use_cases import (AtualizarFamiliaInput, AtualizarFamiliaUseCase, AtualizarPessoaInput, AtualizarPessoaUseCase, AtualizarUnidadeInput, AtualizarUnidadeUseCase, AprovarBeneficioUseCase, CadastrarFamiliaInput, CadastrarFamiliaUseCase, CadastrarPessoaInput, CadastrarPessoaUseCase, CadastrarUnidadeInput, CadastrarUnidadeUseCase, CancelarBeneficioUseCase, EntregarBeneficioUseCase, ExcluirFamiliaUseCase, ExcluirPessoaUseCase, ExcluirUnidadeUseCase, NegarBeneficioUseCase, RegistrarAtendimentoInput, RegistrarAtendimentoUseCase, SolicitarBeneficioInput, SolicitarBeneficioUseCase)
from src.modules.sigmun_assistencia_social.domain.entities import (AtendimentoSocial, BeneficioEventual, FamiliaCadUnico, PessoaCadUnico, StatusBeneficio, StatusFamilia, StatusUnidade, UnidadeAssistencia)
from src.modules.sigmun_assistencia_social.domain.exceptions import (BeneficioNaoEncontradoError, FamiliaJaExistenteError, FamiliaNaoEncontradaError, PessoaJaExistenteError, PessoaNaoEncontradaError, RegraNegocioError, UnidadeNaoEncontradaError)

def _familia(nis: str = "12345678901") -> FamiliaCadUnico:
    return FamiliaCadUnico(nis=nis, responsavel_nome="Maria Souza")

def _pessoa(cpf: str = "98765432100") -> PessoaCadUnico:
    return PessoaCadUnico(familia_id="fam-1", nome="Joao Souza", cpf=cpf)

def _unidade() -> UnidadeAssistencia:
    return UnidadeAssistencia(codigo="CRAS-01", nome="CRAS Centro")

def _beneficio() -> BeneficioEventual:
    return BeneficioEventual(familia_id="fam-1", descricao="Cesta basica", valor=150.0, quantidade=1)

class TestFamilia:
    def test_cadastra_familia(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_nis = MagicMock(return_value=None)
        nova = _familia(); nova.id = "fam-1"
        repo.save = MagicMock(return_value=nova)
        result = CadastrarFamiliaUseCase(repo).execute(CadastrarFamiliaInput(nis="12345678901", responsavel_nome="Maria Souza", responsavel_cpf="", endereco="", telefone=""))
        assert result.nis == "12345678901"
        assert result.esta_ativa

    def test_nao_duplica_nis(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_nis = MagicMock(return_value=_familia())
        with pytest.raises(FamiliaJaExistenteError):
            CadastrarFamiliaUseCase(repo).execute(CadastrarFamiliaInput(nis="12345678901", responsavel_nome="Maria Souza", responsavel_cpf="", endereco="", telefone=""))

    def test_nis_invalido(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_nis = MagicMock(return_value=None)
        with pytest.raises(RegraNegocioError):
            CadastrarFamiliaUseCase(repo).execute(CadastrarFamiliaInput(nis="123", responsavel_nome="Maria Souza", responsavel_cpf="", endereco="", telefone=""))

    def test_nome_responsavel_obrigatorio(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_nis = MagicMock(return_value=None)
        with pytest.raises(RegraNegocioError):
            CadastrarFamiliaUseCase(repo).execute(CadastrarFamiliaInput(nis="12345678901", responsavel_nome="", responsavel_cpf="", endereco="", telefone=""))

class TestPessoa:
    def test_cadastra_pessoa(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        repo.get_by_cpf = MagicMock(return_value=None)
        familias.get_by_id = MagicMock(return_value=_familia())
        nova = _pessoa(); nova.id = "pes-1"
        repo.save = MagicMock(return_value=nova)
        result = CadastrarPessoaUseCase(repo, familias).execute(CadastrarPessoaInput(familia_id="fam-1", nome="Joao Souza", cpf="98765432100"))
        assert result.nome == "Joao Souza"
        assert result.familia_id == "fam-1"

    def test_nao_duplica_cpf(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        repo.get_by_cpf = MagicMock(return_value=_pessoa())
        familias.get_by_id = MagicMock(return_value=_familia())
        with pytest.raises(PessoaJaExistenteError):
            CadastrarPessoaUseCase(repo, familias).execute(CadastrarPessoaInput(familia_id="fam-1", nome="Joao", cpf="98765432100"))

    def test_cpf_invalido(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        repo.get_by_cpf = MagicMock(return_value=None)
        familias.get_by_id = MagicMock(return_value=_familia())
        with pytest.raises(RegraNegocioError):
            CadastrarPessoaUseCase(repo, familias).execute(CadastrarPessoaInput(familia_id="fam-1", nome="Joao", cpf="123"))

    def test_familia_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        repo.get_by_cpf = MagicMock(return_value=None)
        familias.get_by_id = MagicMock(return_value=None)
        with pytest.raises(FamiliaNaoEncontradaError):
            CadastrarPessoaUseCase(repo, familias).execute(CadastrarPessoaInput(familia_id="fam-9", nome="Joao", cpf="98765432100"))

class TestUnidade:
    def test_cadastra_unidade(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        nova = _unidade(); nova.id = "uni-1"
        repo.save = MagicMock(return_value=nova)
        result = CadastrarUnidadeUseCase(repo).execute(CadastrarUnidadeInput(codigo="CRAS-01", nome="CRAS Centro"))
        assert result.codigo == "CRAS-01"
        assert result.esta_ativa

    def test_codigo_obrigatorio(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        with pytest.raises(RegraNegocioError):
            CadastrarUnidadeUseCase(repo).execute(CadastrarUnidadeInput(codigo="", nome="CRAS Centro"))

    def test_nome_obrigatorio(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        with pytest.raises(RegraNegocioError):
            CadastrarUnidadeUseCase(repo).execute(CadastrarUnidadeInput(codigo="CRAS-01", nome=""))


class TestBeneficio:
    def test_solicita_beneficio(self) -> None:
        beneficios = MagicMock(spec=RepositorioBeneficio)
        familias = MagicMock(spec=RepositorioFamilia)
        unidades = MagicMock(spec=RepositorioUnidade)
        familias.get_by_id = MagicMock(return_value=_familia())
        unidades.get_by_id = MagicMock(return_value=_unidade())
        novo = _beneficio(); novo.id = "ben-1"
        beneficios.save = MagicMock(return_value=novo)
        result = SolicitarBeneficioUseCase(beneficios, familias, unidades).execute(SolicitarBeneficioInput(familia_id="fam-1", descricao="Cesta basica", valor=150.0, quantidade=1, unidade_id="uni-1"))
        assert result.status == StatusBeneficio.SOLICITADO
        assert result.data_solicitacao is not None

    def test_familia_inexistente(self) -> None:
        beneficios = MagicMock(spec=RepositorioBeneficio)
        familias = MagicMock(spec=RepositorioFamilia)
        unidades = MagicMock(spec=RepositorioUnidade)
        familias.get_by_id = MagicMock(return_value=None)
        with pytest.raises(FamiliaNaoEncontradaError):
            SolicitarBeneficioUseCase(beneficios, familias, unidades).execute(SolicitarBeneficioInput(familia_id="fam-9", valor=150.0, quantidade=1))

    def test_unidade_inexistente(self) -> None:
        beneficios = MagicMock(spec=RepositorioBeneficio)
        familias = MagicMock(spec=RepositorioFamilia)
        unidades = MagicMock(spec=RepositorioUnidade)
        familias.get_by_id = MagicMock(return_value=_familia())
        unidades.get_by_id = MagicMock(return_value=None)
        with pytest.raises(UnidadeNaoEncontradaError):
            SolicitarBeneficioUseCase(beneficios, familias, unidades).execute(SolicitarBeneficioInput(familia_id="fam-1", valor=150.0, quantidade=1, unidade_id="uni-9"))

    def test_quantidade_invalida(self) -> None:
        beneficios = MagicMock(spec=RepositorioBeneficio)
        familias = MagicMock(spec=RepositorioFamilia)
        unidades = MagicMock(spec=RepositorioUnidade)
        familias.get_by_id = MagicMock(return_value=_familia())
        with pytest.raises(RegraNegocioError):
            SolicitarBeneficioUseCase(beneficios, familias, unidades).execute(SolicitarBeneficioInput(familia_id="fam-1", valor=150.0, quantidade=0))

    def test_fluxo_aprovar_entregar(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        ben = _beneficio(); ben.id = "ben-1"
        repo.get_by_id = MagicMock(return_value=ben)
        repo.save = MagicMock(side_effect=lambda b: b)
        aprovado = AprovarBeneficioUseCase(repo).execute("ben-1")
        assert aprovado.status == StatusBeneficio.APROVADO
        assert aprovado.data_aprovacao is not None
        entregue = EntregarBeneficioUseCase(repo).execute("ben-1")
        assert entregue.status == StatusBeneficio.ENTREGUE
        assert entregue.data_entrega is not None

    def test_negar_registra_justificativa(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        ben = _beneficio(); ben.id = "ben-1"
        repo.get_by_id = MagicMock(return_value=ben)
        repo.save = MagicMock(side_effect=lambda b: b)
        negado = NegarBeneficioUseCase(repo).execute("ben-1", "renda acima do limite")
        assert negado.status == StatusBeneficio.NEGADO
        assert negado.observacao == "renda acima do limite"

    def test_cancelar(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        ben = _beneficio(); ben.id = "ben-1"
        repo.get_by_id = MagicMock(return_value=ben)
        repo.save = MagicMock(side_effect=lambda b: b)
        assert CancelarBeneficioUseCase(repo).execute("ben-1").status == StatusBeneficio.CANCELADO

    def test_nao_aprova_beneficio_ja_aprovado(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        ben = _beneficio(); ben.id = "ben-1"; ben.aprovar("")
        repo.get_by_id = MagicMock(return_value=ben)
        with pytest.raises(RegraNegocioError):
            AprovarBeneficioUseCase(repo).execute("ben-1")

    def test_nao_entrega_beneficio_nao_aprovado(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        ben = _beneficio(); ben.id = "ben-1"
        repo.get_by_id = MagicMock(return_value=ben)
        with pytest.raises(RegraNegocioError):
            EntregarBeneficioUseCase(repo).execute("ben-1")

    def test_beneficio_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioBeneficio)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(BeneficioNaoEncontradoError):
            AprovarBeneficioUseCase(repo).execute("ben-9")


class TestAtendimento:
    def test_registra_atendimento(self) -> None:
        atendimentos = MagicMock(spec=RepositorioAtendimento)
        pessoas = MagicMock(spec=RepositorioPessoa)
        unidades = MagicMock(spec=RepositorioUnidade)
        pessoas.get_by_id = MagicMock(return_value=_pessoa())
        unidades.get_by_id = MagicMock(return_value=_unidade())
        novo = AtendimentoSocial(pessoa_id="pes-1", unidade_id="uni-1", profissional="Assistente Social"); novo.id = "ate-1"
        atendimentos.save = MagicMock(return_value=novo)
        result = RegistrarAtendimentoUseCase(atendimentos, pessoas, unidades).execute(RegistrarAtendimentoInput(pessoa_id="pes-1", unidade_id="uni-1", profissional="Assistente Social", data=date(2026, 1, 1)))
        assert result.profissional == "Assistente Social"
        assert result.pessoa_id == "pes-1"

    def test_pessoa_inexistente(self) -> None:
        atendimentos = MagicMock(spec=RepositorioAtendimento)
        pessoas = MagicMock(spec=RepositorioPessoa)
        unidades = MagicMock(spec=RepositorioUnidade)
        pessoas.get_by_id = MagicMock(return_value=None)
        unidades.get_by_id = MagicMock(return_value=_unidade())
        with pytest.raises(PessoaNaoEncontradaError):
            RegistrarAtendimentoUseCase(atendimentos, pessoas, unidades).execute(RegistrarAtendimentoInput(pessoa_id="pes-9", unidade_id="uni-1", profissional="Assistente Social"))

    def test_unidade_inexistente(self) -> None:
        atendimentos = MagicMock(spec=RepositorioAtendimento)
        pessoas = MagicMock(spec=RepositorioPessoa)
        unidades = MagicMock(spec=RepositorioUnidade)
        pessoas.get_by_id = MagicMock(return_value=_pessoa())
        unidades.get_by_id = MagicMock(return_value=None)
        with pytest.raises(UnidadeNaoEncontradaError):
            RegistrarAtendimentoUseCase(atendimentos, pessoas, unidades).execute(RegistrarAtendimentoInput(pessoa_id="pes-1", unidade_id="uni-9", profissional="Assistente Social"))

    def test_profissional_obrigatorio(self) -> None:
        atendimentos = MagicMock(spec=RepositorioAtendimento)
        pessoas = MagicMock(spec=RepositorioPessoa)
        unidades = MagicMock(spec=RepositorioUnidade)
        pessoas.get_by_id = MagicMock(return_value=_pessoa())
        unidades.get_by_id = MagicMock(return_value=_unidade())
        with pytest.raises(RegraNegocioError):
            RegistrarAtendimentoUseCase(atendimentos, pessoas, unidades).execute(RegistrarAtendimentoInput(pessoa_id="pes-1", unidade_id="uni-1", profissional=""))



class TestAtualizarFamilia:
    def test_atualiza_campos(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.save = MagicMock(side_effect=lambda f: f)
        result = AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", responsavel_nome="Maria Atualizada", renda_per_capita=250.0))
        assert result.responsavel_nome == "Maria Atualizada"
        assert result.renda_per_capita == 250.0
        assert result.updated_at is not None

    def test_nao_altera_campos_ausentes(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.save = MagicMock(side_effect=lambda f: f)
        result = AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", telefone="(73) 99999-0000"))
        assert result.nis == fam.nis
        assert result.responsavel_nome == "Maria Souza"
        assert result.telefone == "(73) 99999-0000"

    def test_familia_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(FamiliaNaoEncontradaError):
            AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-9", responsavel_nome="X"))

    def test_nao_duplica_nis_na_atualizacao(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        outra = _familia(nis="12345678909"); outra.id = "fam-2"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.get_by_nis = MagicMock(return_value=outra)
        with pytest.raises(FamiliaJaExistenteError):
            AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", nis="12345678909"))

    def test_permite_manter_proprio_nis(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.get_by_nis = MagicMock(return_value=fam)
        repo.save = MagicMock(side_effect=lambda f: f)
        result = AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", nis="12345678901"))
        assert result.nis == "12345678901"

    def test_renda_negativa_rejeitada(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        with pytest.raises(RegraNegocioError):
            AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", renda_per_capita=-1.0))

    def test_status_invalido_rejeitado(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        with pytest.raises(RegraNegocioError):
            AtualizarFamiliaUseCase(repo).execute(AtualizarFamiliaInput(familia_id="fam-1", status="excluida"))

    def test_inativar_e_reativar(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.save = MagicMock(side_effect=lambda f: f)
        use_case = AtualizarFamiliaUseCase(repo)
        assert use_case.execute(AtualizarFamiliaInput(familia_id="fam-1", status="inativa")).status == StatusFamilia.INATIVA
        assert use_case.execute(AtualizarFamiliaInput(familia_id="fam-1", status="ativa")).esta_ativa


class TestExcluirFamilia:
    def test_exclui_logicamente(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        fam = _familia(); fam.id = "fam-1"
        repo.get_by_id = MagicMock(return_value=fam)
        repo.save = MagicMock(side_effect=lambda f: f)
        result = ExcluirFamiliaUseCase(repo).execute("fam-1")
        assert result.is_deleted is True
        assert not result.esta_ativa

    def test_familia_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioFamilia)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(FamiliaNaoEncontradaError):
            ExcluirFamiliaUseCase(repo).execute("fam-9")


class TestAtualizarPessoa:
    def test_atualiza_campos(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        pes = _pessoa(); pes.id = "pes-1"
        repo.get_by_id = MagicMock(return_value=pes)
        repo.save = MagicMock(side_effect=lambda p: p)
        result = AtualizarPessoaUseCase(repo, familias).execute(AtualizarPessoaInput(pessoa_id="pes-1", nome="Joao Atualizado", renda=300.0))
        assert result.nome == "Joao Atualizado"
        assert result.renda == 300.0

    def test_pessoa_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(PessoaNaoEncontradaError):
            AtualizarPessoaUseCase(repo, familias).execute(AtualizarPessoaInput(pessoa_id="pes-9", nome="X"))

    def test_nao_duplica_cpf_na_atualizacao(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        pes = _pessoa(); pes.id = "pes-1"
        outra = _pessoa(cpf="23456789008"); outra.id = "pes-2"
        repo.get_by_id = MagicMock(return_value=pes)
        repo.get_by_cpf = MagicMock(return_value=outra)
        with pytest.raises(PessoaJaExistenteError):
            AtualizarPessoaUseCase(repo, familias).execute(AtualizarPessoaInput(pessoa_id="pes-1", cpf="23456789008"))

    def test_revincular_familia_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        pes = _pessoa(); pes.id = "pes-1"
        repo.get_by_id = MagicMock(return_value=pes)
        familias.get_by_id = MagicMock(return_value=None)
        with pytest.raises(FamiliaNaoEncontradaError):
            AtualizarPessoaUseCase(repo, familias).execute(AtualizarPessoaInput(pessoa_id="pes-1", familia_id="fam-9"))

    def test_sexo_invalido_rejeitado(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        familias = MagicMock(spec=RepositorioFamilia)
        pes = _pessoa(); pes.id = "pes-1"
        repo.get_by_id = MagicMock(return_value=pes)
        with pytest.raises(RegraNegocioError):
            AtualizarPessoaUseCase(repo, familias).execute(AtualizarPessoaInput(pessoa_id="pes-1", sexo="x"))


class TestExcluirPessoa:
    def test_exclui_logicamente(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        pes = _pessoa(); pes.id = "pes-1"
        repo.get_by_id = MagicMock(return_value=pes)
        repo.save = MagicMock(side_effect=lambda p: p)
        assert ExcluirPessoaUseCase(repo).execute("pes-1").is_deleted is True

    def test_pessoa_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioPessoa)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(PessoaNaoEncontradaError):
            ExcluirPessoaUseCase(repo).execute("pes-9")


class TestAtualizarUnidade:
    def test_atualiza_campos(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        uni = _unidade(); uni.id = "uni-1"
        repo.get_by_id = MagicMock(return_value=uni)
        repo.save = MagicMock(side_effect=lambda u: u)
        result = AtualizarUnidadeUseCase(repo).execute(AtualizarUnidadeInput(unidade_id="uni-1", nome="CRAS Atualizado"))
        assert result.nome == "CRAS Atualizado"

    def test_tipo_invalido_rejeitado(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        uni = _unidade(); uni.id = "uni-1"
        repo.get_by_id = MagicMock(return_value=uni)
        with pytest.raises(RegraNegocioError):
            AtualizarUnidadeUseCase(repo).execute(AtualizarUnidadeInput(unidade_id="uni-1", tipo="x"))

    def test_status_invalido_rejeitado(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        uni = _unidade(); uni.id = "uni-1"
        repo.get_by_id = MagicMock(return_value=uni)
        with pytest.raises(RegraNegocioError):
            AtualizarUnidadeUseCase(repo).execute(AtualizarUnidadeInput(unidade_id="uni-1", status="xxx"))

    def test_inativar_e_reativar(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        uni = _unidade(); uni.id = "uni-1"
        repo.get_by_id = MagicMock(return_value=uni)
        repo.save = MagicMock(side_effect=lambda u: u)
        use_case = AtualizarUnidadeUseCase(repo)
        assert use_case.execute(AtualizarUnidadeInput(unidade_id="uni-1", status="inativa")).status == StatusUnidade.INATIVA
        assert use_case.execute(AtualizarUnidadeInput(unidade_id="uni-1", status="ativa")).esta_ativa

    def test_unidade_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(UnidadeNaoEncontradaError):
            AtualizarUnidadeUseCase(repo).execute(AtualizarUnidadeInput(unidade_id="uni-9", nome="X"))


class TestExcluirUnidade:
    def test_exclui_logicamente(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        uni = _unidade(); uni.id = "uni-1"
        repo.get_by_id = MagicMock(return_value=uni)
        repo.save = MagicMock(side_effect=lambda u: u)
        assert ExcluirUnidadeUseCase(repo).execute("uni-1").is_deleted is True

    def test_unidade_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioUnidade)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(UnidadeNaoEncontradaError):
            ExcluirUnidadeUseCase(repo).execute("uni-9")
