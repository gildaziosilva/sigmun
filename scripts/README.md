# SIGMUN Scripts

Scripts de automação e utilitários do SIGMUN.

## Estrutura

```
scripts/
├── setup/              # Scripts de configuração inicial
├── migrations/         # Scripts de migração de dados
├── deployment/         # Scripts de implantação
└── utilities/          # Utilitários diversos
```

## Scripts Disponíveis

| Script | Descrição |
|--------|-----------|
| `setup/create_structure.ps1` | Cria a estrutura de diretórios do projeto |
| `setup/create_placeholders.ps1` | Cria arquivos placeholder (__init__.py, .gitkeep) |

## Uso

```powershell
# Criar estrutura de diretórios
powershell -ExecutionPolicy Bypass -File scripts\setup\create_structure.ps1

# Criar arquivos placeholder
powershell -ExecutionPolicy Bypass -File scripts\setup\create_placeholders.ps1
```
