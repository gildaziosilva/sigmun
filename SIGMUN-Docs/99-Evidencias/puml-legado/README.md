# PNGs legados movidos de `puml/` (P2/F9, 2026-10-02)

19 arquivos `.png` estavam dentro de diretórios `puml/` (fonte PlantUML), incluindo
10 arquivos com nome `Captura de tela de ... .png`. Foram movidos para cá com prefixo
de origem (`DOMINIO--arquivo.png`) para não quebrar referências externas por hash.

- `puml/` deve conter **apenas fontes `.puml`** (sem fence — ver `scripts/check_docs.sh` F9).
- Renderizações futuras vão para `docs/diagrams/render/` ou `DOM-*/evidencias/`.
- Renomear `*Captura de tela*` para `<dominio>-<topico>-AAAAMMDD.png` antes de referenciar.
