"""Compara duas versões de openapi.json e detecta breaking changes — T-3.3.

Uso:
    python scripts/diff_openapi.py --base openapi/v1.0.0/openapi.json --head openapi/v1.1.0/openapi.json
    python scripts/diff_openapi.py --base openapi/latest/openapi.json --head openapi/v1.1.0/openapi.json

Códigos de saída:
    0 = sem breaking changes (apenas adições compatíveis)
    1 = breaking changes detectadas
    2 = erro de execução
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


class OpenAPIDiffer:
    """Compara dois schemas OpenAPI e identifica breaking changes."""

    def __init__(self, base: dict[str, Any], head: dict[str, Any]):
        self.base = base
        self.head = head
        self.breaking_changes: list[str] = []
        self.non_breaking_changes: list[str] = []

    def compare(self) -> tuple[list[str], list[str]]:
        self._compare_info()
        self._compare_servers()
        self._compare_paths()
        self._compare_components_schemas()
        self._compare_components_parameters()
        self._compare_components_responses()
        self._compare_security()
        return self.breaking_changes, self.non_breaking_changes

    def _add_breaking(self, msg: str):
        self.breaking_changes.append(msg)

    def _add_non_breaking(self, msg: str):
        self.non_breaking_changes.append(msg)

    def _compare_info(self):
        base_info = self.base.get("info", {})
        head_info = self.head.get("info", {})

        if base_info.get("title") != head_info.get("title"):
            self._add_breaking(f"Título alterado: '{base_info.get('title')}' -> '{head_info.get('title')}'")

        base_ver = base_info.get("version", "")
        head_ver = head_info.get("version", "")
        if base_ver != head_ver:
            self._add_non_breaking(f"Versão alterada: {base_ver} -> {head_ver}")

    def _compare_servers(self):
        base_servers = self.base.get("servers", [])
        head_servers = self.head.get("servers", [])

        if len(head_servers) < len(base_servers):
            self._add_breaking("Servidores removidos (pode quebrar clientes)")

    def _compare_paths(self):
        base_paths = self.base.get("paths", {})
        head_paths = self.head.get("paths", {})

        for path in base_paths:
            if path not in head_paths:
                self._add_breaking(f"Path removido: {path}")

        for path in head_paths:
            if path not in base_paths:
                self._add_non_breaking(f"Path adicionado: {path}")

        for path in base_paths:
            if path in head_paths:
                self._compare_path_operations(path, base_paths[path], head_paths[path])

    def _compare_path_operations(self, path: str, base_ops: dict, head_ops: dict):
        for method in base_ops:
            if method not in head_ops:
                self._add_breaking(f"Operação removida: {method.upper()} {path}")
            else:
                self._compare_operation(path, method, base_ops[method], head_ops[method])

        for method in head_ops:
            if method not in base_ops:
                self._add_non_breaking(f"Operação adicionada: {method.upper()} {path}")

    def _compare_operation(self, path: str, method: str, base_op: dict, head_op: dict):
        base_params = {self._param_key(p): p for p in base_op.get("parameters", [])}
        head_params = {self._param_key(p): p for p in head_op.get("parameters", [])}

        for key in base_params:
            if key not in head_params:
                self._add_breaking(f"Parâmetro removido: {method.upper()} {path} -> {key}")

        for key in head_params:
            if key not in base_params:
                self._add_non_breaking(f"Parâmetro adicionado: {method.upper()} {path} -> {key}")

        base_req = base_op.get("requestBody")
        head_req = head_op.get("requestBody")
        if base_req and not head_req:
            self._add_breaking(f"Request body removido: {method.upper()} {path}")
        elif head_req and not base_req:
            self._add_non_breaking(f"Request body adicionado: {method.upper()} {path}")
        elif base_req and head_req:
            self._compare_request_body(path, method, base_req, head_req)

        base_resps = base_op.get("responses", {})
        head_resps = head_op.get("responses", {})

        for status in base_resps:
            if status not in head_resps:
                self._add_breaking(f"Response removido: {method.upper()} {path} -> {status}")

        for status in head_resps:
            if status not in base_resps:
                self._add_non_breaking(f"Response adicionado: {method.upper()} {path} -> {status}")

        base_sec = base_op.get("security", [])
        head_sec = head_op.get("security", [])
        if len(head_sec) > len(base_sec):
            self._add_breaking(f"Requisitos de segurança aumentados: {method.upper()} {path}")

    def _compare_request_body(self, path: str, method: str, base_req: dict, head_req: dict):
        base_content = base_req.get("content", {})
        head_content = head_req.get("content", {})

        for mime in base_content:
            if mime not in head_content:
                self._add_breaking(f"Media type removido no request: {method.upper()} {path} -> {mime}")

        base_required = base_req.get("required", False)
        head_required = head_req.get("required", False)
        if not base_required and head_required:
            self._add_breaking(f"Request body tornado obrigatório: {method.upper()} {path}")

    def _compare_components_schemas(self):
        base_schemas = self.base.get("components", {}).get("schemas", {})
        head_schemas = self.head.get("components", {}).get("schemas", {})

        for name in base_schemas:
            if name not in head_schemas:
                self._add_breaking(f"Schema removido: {name}")
            else:
                self._compare_schema(name, base_schemas[name], head_schemas[name])

        for name in head_schemas:
            if name not in base_schemas:
                self._add_non_breaking(f"Schema adicionado: {name}")

    def _compare_schema(self, name: str, base: dict, head: dict):
        if base.get("type") != head.get("type"):
            self._add_breaking(f"Schema {name}: tipo alterado ({base.get('type')} -> {head.get('type')})")

        base_props = base.get("properties", {})
        head_props = head.get("properties", {})

        for prop in base_props:
            if prop not in head_props:
                self._add_breaking(f"Schema {name}: propriedade removida '{prop}'")

        for prop in head_props:
            if prop not in base_props:
                self._add_non_breaking(f"Schema {name}: propriedade adicionada '{prop}'")

        base_required = set(base.get("required", []))
        head_required = set(head.get("required", []))

        for req in head_required - base_required:
            self._add_breaking(f"Schema {name}: campo required adicionado '{req}'")

        for req in base_required - head_required:
            self._add_non_breaking(f"Schema {name}: campo required removido '{req}'")

        for prop, prop_schema in base_props.items():
            if prop in head_props:
                base_enum = prop_schema.get("enum")
                head_enum = head_props[prop].get("enum")
                if base_enum and head_enum:
                    removed = set(base_enum) - set(head_enum)
                    if removed:
                        self._add_breaking(f"Schema {name}.{prop}: valores enum removidos {removed}")

    def _compare_components_parameters(self):
        base_params = self.base.get("components", {}).get("parameters", {})
        head_params = self.head.get("components", {}).get("parameters", {})

        for name in base_params:
            if name not in head_params:
                self._add_breaking(f"Parâmetro global removido: {name}")

    def _compare_components_responses(self):
        base_resps = self.base.get("components", {}).get("responses", {})
        head_resps = self.head.get("components", {}).get("responses", {})

        for name in base_resps:
            if name not in head_resps:
                self._add_breaking(f"Response global removida: {name}")

    def _compare_security(self):
        base_sec = self.base.get("security", [])
        head_sec = self.head.get("security", [])

        if len(head_sec) > len(base_sec):
            self._add_breaking("Requisitos de segurança globais aumentados")

    @staticmethod
    def _param_key(param: dict) -> str:
        return f"{param.get('in', '')}:{param.get('name', '')}"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Compara dois openapi.json e detecta breaking changes")
    parser.add_argument("--base", required=True, help="Arquivo base (versão anterior)")
    parser.add_argument("--head", required=True, help="Arquivo head (nova versão)")
    parser.add_argument("--fail-on-non-breaking", action="store_true", help="Falha também em non-breaking changes")
    args = parser.parse_args()

    base_path = Path(args.base)
    head_path = Path(args.head)

    if not base_path.exists():
        print(f"ERRO: Arquivo base não encontrado: {base_path}", file=sys.stderr)
        return 2
    if not head_path.exists():
        print(f"ERRO: Arquivo head não encontrado: {head_path}", file=sys.stderr)
        return 2

    base = load_json(base_path)
    head = load_json(head_path)

    differ = OpenAPIDiffer(base, head)
    breaking, non_breaking = differ.compare()

    if breaking:
        print("🔴 BREAKING CHANGES detectadas:")
        for change in breaking:
            print(f"  - {change}")
    else:
        print("✅ Sem breaking changes")

    if non_breaking:
        print("\n🟢 Non-breaking changes (aditivos):")
        for change in non_breaking:
            print(f"  - {change}")

    if breaking:
        return 1
    if args.fail_on_non_breaking and non_breaking:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
