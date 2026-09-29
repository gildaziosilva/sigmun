"""Verifica se identificadores malformados causam HTTP 500 nas rotas TEL/IMO.

Identificadores opacos alimentam `UUID(...)` no repositório; um valor fora do
formato deve ser recusado pela validação da aplicação, e não estourar uma
exceção não tratada.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient  # noqa: E402

from src.main import app  # noqa: E402

ROTA_ID = "nao-e-um-uuid"

# (método, caminho) para todas as operações que recebem um identificador opaco.
ROTAS = [
    ("GET", f"/api/v1/tel/bairros/{ROTA_ID}"),
    ("PATCH", f"/api/v1/tel/bairros/{ROTA_ID}"),
    ("DELETE", f"/api/v1/tel/bairros/{ROTA_ID}"),
    ("GET", f"/api/v1/tel/logradouros/{ROTA_ID}"),
    ("PATCH", f"/api/v1/tel/logradouros/{ROTA_ID}"),
    ("DELETE", f"/api/v1/tel/logradouros/{ROTA_ID}"),
    ("GET", f"/api/v1/tel/plantas-valores/{ROTA_ID}"),
    ("POST", f"/api/v1/tel/plantas-valores/{ROTA_ID}/ativar"),
    ("POST", f"/api/v1/tel/plantas-valores/{ROTA_ID}/revogar"),
    ("GET", f"/api/v1/tel/georreferencias/{ROTA_ID}"),
    ("DELETE", f"/api/v1/tel/georreferencias/{ROTA_ID}"),
    ("GET", f"/api/v1/imo/imoveis/{ROTA_ID}"),
    ("PATCH", f"/api/v1/imo/imoveis/{ROTA_ID}"),
    ("DELETE", f"/api/v1/imo/imoveis/{ROTA_ID}"),
    ("POST", f"/api/v1/imo/imoveis/{ROTA_ID}/situacao"),
    ("GET", f"/api/v1/imo/imoveis/{ROTA_ID}/proprietarios"),
    ("GET", f"/api/v1/imo/avaliacoes/{ROTA_ID}"),
    ("POST", f"/api/v1/imo/avaliacoes/{ROTA_ID}/concluir"),
    ("POST", f"/api/v1/imo/avaliacoes/{ROTA_ID}/cancelar"),
    ("DELETE", f"/api/v1/imo/proprietarios/{ROTA_ID}"),
]

cliente = TestClient(app, raise_server_exceptions=False)
print(f"Identificador de teste: {ROTA_ID!r}\n")
quebradas = []
for metodo, caminho in ROTAS:
    resposta = cliente.request(metodo, caminho, json={} if metodo in ("POST", "PATCH") else None)
    marca = "  <-- HTTP 500" if resposta.status_code >= 500 else ""
    print(f"  {metodo:6} {resposta.status_code}  {caminho}{marca}")
    if resposta.status_code >= 500:
        quebradas.append(f"{metodo} {caminho} -> {resposta.status_code}")

print(f"\nrotas com erro 5xx: {len(quebradas)}")
for item in quebradas:
    print("  ", item)
