"""Testes de casos de uso do DOM-IMO (Cadastro Imobiliário) — imóveis."""

from __future__ import annotations

import pytest

from src.modules.sigmun_cadastro_imobiliario.application.use_cases import (
    AlterarSituacaoImovelUseCase,
    AtualizarImovelInput,
    AtualizarImovelUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
    ExcluirImovelUseCase,
    RemoverProprietarioUseCase,
    VincularProprietarioInput,
    VincularProprietarioUseCase,
)
from src.modules.sigmun_cadastro_imobiliario.domain.entities import SituacaoImovel
from src.modules.sigmun_cadastro_imobiliario.domain.exceptions import (
    ImovelJaExistenteError,
    ImovelNaoEncontradoError,
    ProprietarioJaExistenteError,
    ProprietarioNaoEncontradoError,
    ProprietarioPrincipalDuplicadoError,
    RegraNegocioError,
)
from tests.unit.imo_fixtures import _imovel as imovel
from tests.unit.imo_fixtures import _proprietario as proprietario
from tests.unit.imo_fixtures import repo_imovel, repo_proprietario


class TestImovel:
    def test_cadastra_imovel(self) -> None:
        result = CadastrarImovelUseCase(repo_imovel()).execute(
            CadastrarImovelInput(
                inscricao_imobiliaria="INS-0001",
                logradouro_id="lg-1",
                bairro_id="bairro-1",
                numero="120",
                area_terreno_m2=200.0,
                area_construida_m2=120.0,
            )
        )
        assert result.inscricao_imobiliaria == "INS-0001"
        assert result.situacao == SituacaoImovel.ATIVO
        assert result.esta_ativo

    def test_nao_duplica_inscricao(self) -> None:
        """RN-IMO-001: a inscrição imobiliária é única no município."""
        with pytest.raises(ImovelJaExistenteError):
            CadastrarImovelUseCase(repo_imovel(imovel())).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0001",
                    logradouro_id="lg-1",
                    bairro_id="bairro-1",
                )
            )

    def test_exige_inscricao(self) -> None:
        """RN-IMO-001: inscrição imobiliária é obrigatória."""
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="", logradouro_id="lg-1", bairro_id="bairro-1"
                )
            )

    def test_exige_logradouro_e_bairro(self) -> None:
        """RN-IMO-002: o imóvel exige logradouro e bairro vinculados."""
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="",
                    bairro_id="bairro-1",
                )
            )
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="lg-1",
                    bairro_id="",
                )
            )

    def test_areas_negativas_rejeitadas(self) -> None:
        """RN-IMO-003: áreas não podem ser negativas."""
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="lg-1",
                    bairro_id="bairro-1",
                    area_terreno_m2=-10.0,
                )
            )
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="lg-1",
                    bairro_id="bairro-1",
                    area_construida_m2=-10.0,
                )
            )

    def test_tipo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="lg-1",
                    bairro_id="bairro-1",
                    tipo="castelo",
                )
            )

    def test_ano_construcao_invalido(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarImovelUseCase(repo_imovel()).execute(
                CadastrarImovelInput(
                    inscricao_imobiliaria="INS-0002",
                    logradouro_id="lg-1",
                    bairro_id="bairro-1",
                    ano_construcao=1500,
                )
            )

    def test_atualiza_campos(self) -> None:
        alvo = imovel()
        alvo.id = "imovel-1"
        result = AtualizarImovelUseCase(repo_imovel(alvo)).execute(
            AtualizarImovelInput(imovel_id="imovel-1", area_terreno_m2=250.0)
        )
        assert result.area_terreno_m2 == 250.0

    def test_atualiza_tipo_invalido(self) -> None:
        alvo = imovel()
        alvo.id = "imovel-1"
        with pytest.raises(RegraNegocioError):
            AtualizarImovelUseCase(repo_imovel(alvo)).execute(
                AtualizarImovelInput(imovel_id="imovel-1", tipo="castelo")
            )

    def test_atualiza_imovel_inexistente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            AtualizarImovelUseCase(repo_imovel()).execute(
                AtualizarImovelInput(imovel_id="imovel-9", numero="1")
            )


    def test_altera_situacao_permitida(self) -> None:
        """RN-IMO-004: transições da máquina de estados do imóvel."""
        alvo = imovel()
        alvo.id = "imovel-1"
        use_case = AlterarSituacaoImovelUseCase(repo_imovel(alvo))
        assert use_case.execute("imovel-1", "em_obra").situacao == SituacaoImovel.EM_OBRA
        assert use_case.execute("imovel-1", "ativo").situacao == SituacaoImovel.ATIVO
        assert use_case.execute("imovel-1", "inativo").situacao == SituacaoImovel.INATIVO
        # Inativo é suspensão cadastral: a reativação é obrigatória antes de
        # registrar outra ocorrência sobre o imóvel.
        assert use_case.execute("imovel-1", "ativo").situacao == SituacaoImovel.ATIVO
        assert use_case.execute("imovel-1", "desocupado").situacao == SituacaoImovel.DESOCUPADO

    def test_inativo_nao_vai_direto_para_desocupado(self) -> None:
        """RN-IMO-004: a partir de inativo exige reativação."""
        alvo = imovel()
        alvo.id = "imovel-1"
        alvo.situacao = SituacaoImovel.INATIVO
        with pytest.raises(RegraNegocioError):
            AlterarSituacaoImovelUseCase(repo_imovel(alvo)).execute("imovel-1", "desocupado")

    def test_demolicao_e_irreversivel(self) -> None:
        """RN-IMO-004: imóvel demolido é estado terminal."""
        alvo = imovel()
        alvo.id = "imovel-1"
        alvo.situacao = SituacaoImovel.DEMOLIDO
        with pytest.raises(RegraNegocioError):
            AlterarSituacaoImovelUseCase(repo_imovel(alvo)).execute("imovel-1", "ativo")

    def test_situacao_invalida_rejeitada(self) -> None:
        alvo = imovel()
        alvo.id = "imovel-1"
        with pytest.raises(RegraNegocioError):
            AlterarSituacaoImovelUseCase(repo_imovel(alvo)).execute("imovel-1", "ruína")

    def test_altera_situacao_imovel_inexistente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            AlterarSituacaoImovelUseCase(repo_imovel()).execute("imovel-9", "ativo")

    def test_exclui_logicamente(self) -> None:
        alvo = imovel()
        alvo.id = "imovel-1"
        repo = repo_imovel(alvo)
        assert ExcluirImovelUseCase(repo).execute("imovel-1").is_deleted is True

    def test_exclui_imovel_inexistente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            ExcluirImovelUseCase(repo_imovel()).execute("imovel-9")


class TestProprietario:
    def test_vincula_titular_principal(self) -> None:
        result = VincularProprietarioUseCase(
            repo_proprietario(), repo_imovel(imovel())
        ).execute(
            VincularProprietarioInput(
                imovel_id="imovel-1", nome="Maria Souza", cpf="12345678909", principal=True
            )
        )
        assert result.nome == "Maria Souza"
        assert result.e_titular_principal

    def test_exige_imovel_existente(self) -> None:
        with pytest.raises(ImovelNaoEncontradoError):
            VincularProprietarioUseCase(repo_proprietario(), repo_imovel()).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-9", nome="Maria", cpf="12345678909"
                )
            )

    def test_nao_duplica_pessoa_no_imovel(self) -> None:
        """RN-IMO-006: a mesma pessoa não é vinculada duas vezes ao imóvel."""
        repo = repo_proprietario()
        repo.get_by_imovel_e_cpf.return_value = proprietario()
        with pytest.raises(ProprietarioJaExistenteError):
            VincularProprietarioUseCase(repo, repo_imovel(imovel())).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-1", nome="Maria Souza", cpf="12345678909"
                )
            )

    def test_recusa_segundo_titular_principal(self) -> None:
        """RN-IMO-006: no máximo um proprietário titular principal por imóvel."""
        repo = repo_proprietario()
        repo.get_principal.return_value = proprietario()
        with pytest.raises(ProprietarioPrincipalDuplicadoError):
            VincularProprietarioUseCase(repo, repo_imovel(imovel())).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-1",
                    nome="Joao Souza",
                    cpf="98765432100",
                    principal=True,
                )
            )

    def test_nao_torna_principal_vinculo_nao_titular(self) -> None:
        alvo = repo_imovel(imovel())
        result = VincularProprietarioUseCase(repo_proprietario(), alvo).execute(
            VincularProprietarioInput(
                imovel_id="imovel-1",
                nome="Joao Souza",
                cpf="98765432100",
                vinculo="parceiro",
                principal=True,
            )
        )
        assert result.principal is False

    def test_cpf_invalido_rejeitado(self) -> None:
        """RN-IMO-006: o CPF do proprietário deve ter 11 dígitos."""
        with pytest.raises(RegraNegocioError):
            VincularProprietarioUseCase(
                repo_proprietario(), repo_imovel(imovel())
            ).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-1", nome="Maria", cpf="123"
                )
            )

    def test_nome_obrigatorio(self) -> None:
        with pytest.raises(RegraNegocioError):
            VincularProprietarioUseCase(
                repo_proprietario(), repo_imovel(imovel())
            ).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-1", nome="", cpf="12345678909"
                )
            )

    def test_vinculo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            VincularProprietarioUseCase(
                repo_proprietario(), repo_imovel(imovel())
            ).execute(
                VincularProprietarioInput(
                    imovel_id="imovel-1",
                    nome="Maria",
                    cpf="12345678909",
                    vinculo="x",
                )
            )

    def test_remove_vinculo_logicamente(self) -> None:
        alvo = proprietario()
        alvo.id = "vinculo-1"
        repo = repo_proprietario(alvo)
        assert RemoverProprietarioUseCase(repo).execute("vinculo-1").is_deleted is True

    def test_remove_vinculo_inexistente(self) -> None:
        with pytest.raises(ProprietarioNaoEncontradoError):
            RemoverProprietarioUseCase(repo_proprietario()).execute("vinculo-9")

