"""Exercita as operações TEL/IMO recém-integradas no frontend.

Roda contra a aplicação FastAPI com um repositório em memória, confirmando que
cada função adicionada em `api.ts` corresponde a uma rota que responde.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient  # noqa: E402

from src.main import app  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
API_TS = RAIZ / "frontend" / "admin" / "src" / "lib" / "api.ts"

# Funções adicionadas nesta integração e a rota que cada uma deve exercitar.
NOVAS = {
    # DOM-TEL
    "obterBairroTel": ("GET", "/api/v1/tel/bairros/inexistente"),
    "obterBairroPorCodigoTel": ("GET", "/api/v1/tel/bairros/codigo/inexistente"),
    "listarLogradourosDoBairroTel": ("GET", "/api/v1/tel/bairros/inexistente/logradouros"),
    "obterLogradouroTel": ("GET", "/api/v1/tel/logradouros/inexistente"),
    "obterLogradouroPorCodigoTel": ("GET", "/api/v1/tel/logradouros/codigo/inexistente"),
    "obterPlantaValoresTel": ("GET", "/api/v1/tel/plantas-valores/inexistente"),
    "obterPlantaVigenteTel": (
        "GET",
        "/api/v1/tel/plantas-valores/vigente?ano=2026&bairro_id=inexistente&ocupacao=residencial",
    ),
    "obterGeorreferenciaTel": ("GET", "/api/v1/tel/georreferencias/inexistente"),
    "listarGeorreferenciasPorReferenciaTel": (
        "GET",
        "/api/v1/tel/georreferencias/referencia?bairro_id=inexistente",
    ),
    # DOM-IMO
    "obterImovelImo": ("GET", "/api/v1/imo/imoveis/inexistente"),
    "obterImovelPorInscricaoImo": ("GET", "/api/v1/imo/imoveis/inscricao/inexistente"),
    "listarImoveisDoLogradouroImo": ("GET", "/api/v1/imo/imoveis/logradouro/inexistente"),
    "listarImoveisDoBairroImo": ("GET", "/api/v1/imo/imoveis/bairro/inexistente"),
    "listarProprietariosDoImovelImo": ("GET", "/api/v1/imo/imoveis/inexistente/proprietarios"),
    "obterAvaliacaoImo": ("GET", "/api/v1/imo/avaliacoes/inexistente"),
    "listarAvaliacoesDoImovelImo": ("GET", "/api/v1/imo/avaliacoes/imovel/inexistente"),
    "concluirAvaliacaoImo": ("POST", "/api/v1/imo/avaliacoes/inexistente/concluir"),
    "listarCaracteristicasDoImovelImo": ("GET", "/api/v1/imo/caracteristicas/imovel/inexistente"),
    "listarGeometriasDoImovelImo": ("GET", "/api/v1/imo/geometrias/imovel/inexistente"),
}

codigo = API_TS.read_text(encoding="utf-8")
esquema = app.openapi()


def _normalizar(valor: str) -> str:
    """Substitui por `{param}` tanto placeholders do OpenAPI quanto o segmento
    identificador concreto usado no caminho de teste (`inexistente`, UUID)."""
    caminho = re.sub(r"\{[^}]+\}", "{param}", valor.split("?")[0])
    return re.sub(r"/(inexistente|[0-9a-fA-F-]{36})(?=/|$)", "/{param}", caminho)


rotas_normalizadas = {_normalizar(c) for c in esquema["paths"]}


def existe_rota(caminho: str) -> bool:
    """Confere se o caminho casa com alguma rota declarada no OpenAPI."""
    return _normalizar(caminho) in rotas_normalizadas


print("=== 1. Funções declaradas no cliente ===")
ausentes = [nome for nome in NOVAS if f"export async function {nome}(" not in codigo]
print(f"  esperadas: {len(NOVAS)} | ausentes: {len(ausentes)}")
for nome in ausentes:
    print("    AUSENTE:", nome)

print("=== 2. Rotas resolvidas pela API ===")
inexistentes = [f"{nome} -> {caminho}" for nome, (_, caminho) in NOVAS.items() if not existe_rota(caminho)]
print(f"  rotas inexistentes: {len(inexistentes)}")
for item in inexistentes:
    print("    INEXISTENTE:", item)

print("=== 3. Resposta real do servidor ===")
cliente = TestClient(app, raise_server_exceptions=False)
falhas: list[str] = []
for nome, (metodo, caminho) in NOVAS.items():
    if not existe_rota(caminho):
        continue
    resposta = cliente.request(metodo, caminho)
    # 404 é o resultado esperado para um identificador inexistente e 422 indica
    # parâmetro obrigatório ausente; uma listagem vazia responde 200 com `[]`.
    esperado = resposta.status_code in (404, 422) or (
        resposta.status_code == 200 and resposta.text.strip() in ("[]", "null")
    )
    if not esperado:
        falhas.append(f"{nome}: {resposta.status_code} {resposta.text[:120]}")
    print(f"  {metodo:5} {resposta.status_code}  {nome}")
print(f"  respostas inesperadas: {len(falhas)}")
for item in falhas:
    print("    FALHA:", item)

# A transição de conclusão (409 quando a avaliação não está em rascunho) é
# exercitada pela suíte de testes do backend.
total_ok = not ausentes and not inexistentes and not falhas
print()
print("RESULTADO:", "OK" if total_ok else "FALHOU")
sys.exit(0 if total_ok else 1)
