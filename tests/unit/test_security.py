"""Testes do módulo compartilhado de autorização (shared/security).

Valida a extração do contexto a partir dos headers provisórios e as
guardas de autenticação (401) e papel (403).
"""

from typing import Annotated
from uuid import uuid4

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from src.shared.security import (
    UsuarioContexto,
    exigir_autenticacao,
    exigir_papeis,
    extrair_usuario_id_header,
    obter_usuario_contexto,
)

_exigir_gestor = exigir_papeis("gestor")


def test_extrair_usuario_id_header() -> None:
    uid = uuid4()
    assert extrair_usuario_id_header(x_usuario_id=uid) == uid
    assert extrair_usuario_id_header(x_usuario_id=None) is None


def test_obter_usuario_contexto_com_headers() -> None:
    uid = uuid4()
    from src.shared.security import obter_usuario_contexto as _dep

    # Chamada direta (sem o ciclo FastAPI de Depends).
    contexto = _dep(usuario_id=uid, x_usuario_papel="gestor,compras")
    assert contexto is not None
    assert contexto.usuario_id == uid
    assert contexto.papeis == ("gestor", "compras")


def test_obter_usuario_contexto_sem_autenticacao() -> None:
    assert obter_usuario_contexto(usuario_id=None, x_usuario_papel=None) is None


def test_usuario_contexto_checagem_de_papeis() -> None:
    contexto = UsuarioContexto(usuario_id=uuid4(), papeis=("compras",))
    assert contexto.possui_papel("compras")
    assert not contexto.possui_papel("gestor")
    assert contexto.possui_algum_papel("gestor", "compras")
    assert not contexto.possui_algum_papel("gestor")


def test_route_protegida_sem_header_retorna_401() -> None:
    app = FastAPI()

    @app.get("/rota")
    def rota(contexto: Annotated[UsuarioContexto, Depends(exigir_autenticacao)]):
        return {"usuario": str(contexto.usuario_id)}

    response = TestClient(app).get("/rota")
    assert response.status_code == 401


def test_route_protegida_com_header_retorna_200() -> None:
    app = FastAPI()

    @app.get("/rota")
    def rota(contexto: Annotated[UsuarioContexto, Depends(exigir_autenticacao)]):
        return {"usuario": str(contexto.usuario_id)}

    uid = uuid4()
    response = TestClient(app).get("/rota", headers={"X-Usuario-Id": str(uid)})
    assert response.status_code == 200
    assert response.json() == {"usuario": str(uid)}


def test_exigir_papeis_com_papel_correto_ok() -> None:
    app = FastAPI()

    @app.get("/gestor")
    def gestor(contexto: Annotated[UsuarioContexto, Depends(_exigir_gestor)]):
        return {"ok": True}

    uid = uuid4()
    response = TestClient(app).get(
        "/gestor",
        headers={"X-Usuario-Id": str(uid), "X-Usuario-Papel": "gestor"},
    )
    assert response.status_code == 200


def test_exigir_papeis_sem_papel_retorna_403() -> None:
    app = FastAPI()

    @app.get("/gestor")
    def gestor(contexto: Annotated[UsuarioContexto, Depends(_exigir_gestor)]):
        return {"ok": True}

    uid = uuid4()
    response = TestClient(app).get(
        "/gestor",
        headers={"X-Usuario-Id": str(uid), "X-Usuario-Papel": "compras"},
    )
    assert response.status_code == 403

    sem_papel = TestClient(app).get(
        "/gestor", headers={"X-Usuario-Id": str(uid)}
    )
    assert sem_papel.status_code == 403
