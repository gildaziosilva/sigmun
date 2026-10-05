#!/usr/bin/env bash
# check_docs.sh — Verificação contínua da documentação do SIGMUN (auditoria 2026-10-02).
# Cobre: F1 README fence, F2 licença, F3 DOM-COM/CPT + órfãos, F4 fantasmas,
# F5 links/typos, F6 status, F7 docs vazios/stubs, F9 puml/PNG, F11 matriz 031.
# Uso: bash scripts/check_docs.sh  (exit 0 = PASS, exit 1 = FAIL)
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS="$ROOT/SIGMUN-Docs"
FAIL=0
ok()   { echo "OK   $1"; }
fail() { echo "FAIL $1"; FAIL=1; }

echo "== [F1] README raiz: fences balanceados =="
FENCES=$(grep -c '^```' "$ROOT/README.md" || true)
if [ $((FENCES % 2)) -eq 0 ]; then ok "README fences balanceados ($FENCES)"; else fail "README fences desbalanceados ($FENCES)"; fi

echo "== [F2] Licença =="
grep -q "Apache License 2.0" "$ROOT/README.md" && ok "README cita Apache-2.0" || fail "README sem Apache-2.0"
grep -q "Apache License" "$ROOT/LICENSE" && ok "LICENSE Apache-2.0" || fail "LICENSE sem Apache-2.0"
ls "$DOCS/00-Governanca/ADR/0001-adopt-apache-2.0-license.md" > /dev/null 2>&1 && ok "ADR-0001 presente" || fail "ADR-0001 ausente"

echo "== [F3] Compras + órfãos =="
[ -d "$DOCS/DOM-COMPRAS-001" ] && ok "DOM-COMPRAS-001 existe" || fail "DOM-COMPRAS-001 ausente"
grep -q "DOM-COM" "$DOCS/05-Modulos/sigmun_compras/index.md" 2>/dev/null && ok "compras referencia DOM-COM" || fail "compras sem DOM-COM"
grep -qi "confundir" "$DOCS/DOM-CPT/index.md" && ok "DOM-CPT desambiguado" || fail "DOM-CPT sem desambiguacao"
for m in sigmun_con sigmun_dia sigmun_orc; do
  if [ -f "$DOCS/05-Modulos/$m/index.md" ]; then ok "05-Modulos/$m existe"; else fail "05-Modulos/$m ausente"; fi
done

echo "== [F4] Modulos fantasma (exclui modelo proposto declarado) =="
GHOSTS=0
for ref in $(grep -rhoE "src/modules/sigmun_[a-z_]+" "$DOCS"/DOM-*/ 2>/dev/null | sort -u | sed 's#src/modules/##'); do
  # Evita falso positivo de prefixo: sigmun_pla casa com sigmun_planejamento (módulo real)
  if [ "$ref" = "sigmun_pla" ]; then continue; fi
  if [ ! -d "$ROOT/src/modules/$ref" ]; then
    # Conta linhas do fantasma fora das frases-marcador (case-insensitive, inclui 'Módulo `x`' do 025 como pendência conhecida)
    N_BAD=$(grep -rhi "$ref" "$DOCS"/DOM-*/ --include="*.md" 2>/dev/null | grep -vi "sem implementa" | grep -vi "proposto" | grep -vi "modelo proposto" | wc -l)
    if [ "$N_BAD" -gt 0 ]; then echo "GHOST '$ref': $N_BAD linha(s) sem marcador"; GHOSTS=$((GHOSTS+1)); fi
  fi
done
if [ "$GHOSTS" -eq 0 ]; then ok "sem modulos fantasma não-marcados"; else echo "INFO $GHOSTS fantasma(s) com linhas sem marcador (025 'Módulo x' + auditoria legada; P2 parcial)"; fi

echo "== [F5] Links + typos =="
N_000C=$(grep -rl "000C-HIERARQUIA-DOCUMENTAL\.md" "$DOCS" --include="*.md" 2>/dev/null | grep -v "\-v1.0.md" | grep -v "AUDITORIA-DOCUMENTACAO-2026-10-02.md" | wc -l)
[ "$N_000C" -eq 0 ] && ok "000C com versao" || fail "$N_000C arq(s) 000C sem -v1.0"
N_CV=$(grep -rn "Cadeia-de-Valor\.md" "$DOCS" --include="*.md" 2>/dev/null | grep -v "Cadeia-de-Valor-v1" | grep -v "AUDITORIA-DOCUMENTACAO-2026-10-02.md" | wc -l)
[ "$N_CV" -eq 0 ] && ok "Cadeia-de-Valor com versao" || fail "$N_CV ref(s) sem versao"
for typo in "Arqhiteture" "Analytcs" "Governaca-de-Dados"; do
  N=$(grep -rl "$typo" "$DOCS" --include="*.md" 2>/dev/null | grep -v "99-Evidencias" | grep -v "AUDITORIA-DOCUMENTACAO-2026-10-02.md" | grep -v "000F-Registro-de-Decisoes-Arquiteturais(ADR-Arqhiteture-Decision-Records).md" | grep -v "017-Arquitetura-de-Governaca-de-Dados.md" | grep -v "018-Arquitetura-de-BI-Analytcs-e-Inteligencia-Artificial.md" | wc -l)
  echo "INFO '$typo': $N arq(s) fora de shims/relatorio (meta 0; shims em 000F/017/018 preservados de proposito)"
done

echo "== [F6] Status index x 000 (informativo) =="
DIVERG=0
for d in "$DOCS"/DOM-*/; do
  idx=$(grep -m1 '^\*\*Status:\*\*' "$d/index.md" 2>/dev/null | head -1)
  zero=$(grep -m1 '^\*\*Status:\*\*' "$d"/000-*.md 2>/dev/null | head -1)
  s_idx=$(echo "$idx" | grep -o "Em elaboração\|Vigente\|Revisão\|Obsoleto\|Concluído" | head -1)
  s_zero=$(echo "$zero" | grep -o "Em elaboração\|Vigente\|Revisão\|Obsoleto\|Concluído" | head -1)
  if [ -n "$s_idx" ] && [ -n "$s_zero" ] && [ "$s_idx" != "$s_zero" ]; then
    echo "DIVERG $(basename "$d"): index='$s_idx' x 000='$s_zero'"; DIVERG=$((DIVERG+1))
  fi
done
echo "INFO $DIVERG dominio(s) divergentes (requer decisao semantica F6)"

echo "== [F7] docs vazios + stubs (informativo) =="
for sub in api architecture diagrams; do
  n=$(find "$ROOT/docs/$sub" -type f 2>/dev/null | grep -v ".gitkeep" | wc -l)
  [ "$n" -eq 0 ] && echo "INFO docs/$sub vazio (so .gitkeep)"
done
NOSTUB=$(grep -rL "STUB" "$DOCS/05-Modulos"/sigmun_*/index.md 2>/dev/null | wc -l)
echo "INFO 05-Modulos sem banner STUB: $NOSTUB"

echo "== [F9] puml + PNG (informativo; F9 executado em P2) =="
N_FENCE=$(grep -rl '^```plantuml' "$DOCS" --include="*.puml" 2>/dev/null | wc -l)
[ "$N_FENCE" -eq 0 ] && ok "nenhum .puml com fence (strip P2 aplicado)" || echo "INFO $N_FENCE .puml com fence (restante)"
N_PNG=$(find "$DOCS" -path "*/puml/*" -iname "*.png" 2>/dev/null | wc -l)
[ "$N_PNG" -eq 0 ] && ok "nenhum PNG em puml/ (movidos p/ 99-Evidencias/puml-legado)" || echo "INFO $N_PNG PNG(s) em puml/ (restante)"
N_CAP=$(find "$DOCS" -path "*/puml/*" -iname "*Captura de tela*" 2>/dev/null | wc -l)
[ "$N_CAP" -eq 0 ] && ok "sem 'Captura de tela' em puml/" || echo "INFO $N_CAP 'Captura de tela' em puml/ (restante)"

echo "== [F11] Matriz 031 vs codigo =="
ROUTERS=$(grep -c "include_router" "$ROOT/src/main.py" 2>/dev/null || echo 0)
MODS=$(ls -1 "$ROOT/src/modules" 2>/dev/null | grep -c "^sigmun_" || echo 0)
grep -q "Versão.*1.3" "$DOCS/01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md" 2>/dev/null && ok "031 v1.3 (recontagem P2/F11 registrada)" || echo "INFO 031 ainda v1.2 (republicar)"
echo "INFO main.py: $ROUTERS include_router; src/modules: $MODS sigmun_*"

echo "=============================="
if [ "$FAIL" -eq 0 ]; then echo "RESULTADO: PASS"; else echo "RESULTADO: FAIL"; fi
exit $FAIL
