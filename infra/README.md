# SIGMUN Infrastructure

Infraestrutura como código (IaC) do SIGMUN, baseada na [Arquitetura de Implantação](SIGMUN-Docs/01-Arquitetura-Corporativa/008-Arquitetura-de-Implantacao-e-Infraestrutura.md).

## Estrutura

```
infra/
├── docker/           # Dockerfiles e configurações
│   ├── backend/      # Dockerfile do backend Python
│   ├── frontend/     # Dockerfile do frontend (multi-stage)
│   └── database/     # Scripts de inicialização do banco
├── terraform/        # Infraestrutura AWS (IaC)
│   ├── modules/      # Módulos reutilizáveis
│   ├── environments/ # Configurações por ambiente
│   ├── main.tf       # Recursos principais
│   └── variables.tf  # Variáveis de entrada
└── kubernetes/       # Manifestos Kubernetes
    ├── base/         # Manifestos base
    └── overlays/     # Sobrescritas por ambiente
        ├── dev/
        ├── homolog/
        └── prod/
```

## Ambientes

| Ambiente | Descrição |
|----------|-----------|
| **dev** | Desenvolvimento (dados fictícios) |
| **homolog** | Homologação (dados anonimizados) |
| **prod** | Produção (alta disponibilidade) |

## Tecnologias

- **Containers:** Docker, Docker Compose
- **Orquestração:** Docker Compose (inicial), Kubernetes/EKS (futuro)
- **Cloud:** AWS (PostgreSQL, Redis, S3)
- **IaC:** Terraform

## Uso

```bash
# Desenvolvimento local
docker-compose up -d

# Produção (Kubernetes)
kubectl apply -k infra/kubernetes/overlays/prod
```
