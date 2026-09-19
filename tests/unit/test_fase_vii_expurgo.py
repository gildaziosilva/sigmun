"""Testes do expurgo fisico Fase VII (tmp_path, sem banco real)."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

from src.shared.tasks.expurgo import (
    coletar_candidatos_expurgo,
    expurgar_arquivos,
    resolver_caminho_seguro,
)


class _FakeQuery:
    def __init__(self, itens):
        self._itens = itens

    def filter(self, *a, **k):
        return self

    def order_by(self, *a, **k):
        return self

    def limit(self, n):
        return _FakeQuery(self._itens[:n])

    def all(self):
        return list(self._itens)


class _FakeSession:
    def __init__(self, itens):
        # Simula o filtro de banco (status encerrado + data_eliminacao + ativo);
        # a carência (dias) é aplicada pelo código sob teste.
        self._itens = [
            i
            for i in itens
            if getattr(i, "status", None) == "encerrado"
            and getattr(i, "data_eliminacao", None) is not None
            and getattr(i, "deleted_at", None) is None
        ]

    def query(self, *a, **k):
        return _FakeQuery(self._itens)


def _doc(doc_id="d1", dias=40, status="encerrado", ref="a.pdf"):
    base = datetime.now(timezone.utc) - timedelta(days=dias)
    return SimpleNamespace(
        id=doc_id, data_eliminacao=base, status=status, conteudo_ref=ref, deleted_at=None
    )


class TestCaminhoSeguro:
    def test_relativo_dentro_da_raiz(self, tmp_path):
        assert resolver_caminho_seguro(tmp_path, "d1/a.pdf") == (tmp_path / "d1/a.pdf").resolve()

    def test_traversal_bloqueado(self, tmp_path):
        assert resolver_caminho_seguro(tmp_path, "../../etc/passwd") is None
        assert resolver_caminho_seguro(tmp_path, "/etc/passwd") is None
        assert resolver_caminho_seguro(tmp_path, "") is None
        assert resolver_caminho_seguro(tmp_path, ".") is None


class TestExpurgo:
    def test_coleta_respeita_carencia(self):
        sessao = _FakeSession([_doc("ok", 40), _doc("recente", 5), _doc("aberto", 40, "ativo")])
        els = coletar_candidatos_expurgo(sessao, dias_retencao=30)  # type: ignore[arg-type]
        assert [d.id for d in els] == ["ok"]

    def test_remove_arquivo_real(self, tmp_path):
        alvo = tmp_path / "a.pdf"
        alvo.write_bytes(b"x")
        sessao = _FakeSession([_doc("d1", 40, "encerrado", "a.pdf")])
        res = expurgar_arquivos(sessao, storage_root=tmp_path, dias_retencao=30)  # type: ignore[arg-type]
        assert res.removidos == 1 and res.candidatos == 1
        assert not alvo.exists()

    def test_dry_run_nao_apaga(self, tmp_path):
        alvo = tmp_path / "a.pdf"
        alvo.write_bytes(b"x")
        sessao = _FakeSession([_doc("d1", 40, "encerrado", "a.pdf")])
        res = expurgar_arquivos(sessao, storage_root=tmp_path, dry_run=True)  # type: ignore[arg-type]
        assert res.removidos == 0 and alvo.exists()

    def test_fora_da_raiz_ignorado(self, tmp_path):
        sessao = _FakeSession([_doc("d1", 40, "encerrado", "/etc/passwd")])
        res = expurgar_arquivos(sessao, storage_root=tmp_path)  # type: ignore[arg-type]
        assert res.ignorados_fora_da_raiz == 1 and res.removidos == 0
        assert Path("/etc/passwd").exists()

    def test_ausente(self, tmp_path):
        sessao = _FakeSession([_doc("d1", 40, "encerrado", "falta.pdf")])
        res = expurgar_arquivos(sessao, storage_root=tmp_path)  # type: ignore[arg-type]
        assert res.ausentes == 1

    def test_symlink_nunca_seguido(self, tmp_path):
        fora = tmp_path.parent / "segredo.txt"
        fora.write_text("segredo")
        link = tmp_path / "link.pdf"
        try:
            os.symlink(fora, link)
        except OSError:
            return
        sessao = _FakeSession([_doc("d1", 40, "encerrado", "link.pdf")])
        res = expurgar_arquivos(sessao, storage_root=tmp_path)  # type: ignore[arg-type]
        assert res.removidos == 0 and fora.exists()
