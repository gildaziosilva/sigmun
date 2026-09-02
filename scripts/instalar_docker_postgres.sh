#!/usr/bin/env bash
# =============================================================================
# SIGMUN - Bootstrap do ambiente de homologação: Docker Engine + PostgreSQL.
#
# Instala o Docker Engine (repositório oficial) e o cliente PostgreSQL no
# Ubuntu 22.04, habilita o serviço e adiciona o usuário ao grupo docker.
# O PostgreSQL em si é provisionado pelo docker-compose.yml do projeto
# (postgres:15 na porta 5433 - ver SIGMUN-Docs/DOM-COMPRAS-001).
#
# Uso (exige privilégios):
#   sudo bash scripts/instalar_docker_postgres.sh
#
# O script é idempotente: pode ser executado novamente sem efeitos colaterais.
# =============================================================================
set -euo pipefail

if [[ $EUID -ne 0 ]]; then
  echo "ERRO: execute com sudo:  sudo bash scripts/instalar_docker_postgres.sh" >&2
  exit 1
fi

USUARIO_ALVO="${SUDO_USER:-gildazio}"

echo "==> [1/5] Atualizando índice de pacotes e instalando dependências base..."
apt-get update -y
apt-get install -y ca-certificates curl gnupg postgresql-client

echo "==> [2/5] Configurando o repositório oficial do Docker..."
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  > /etc/apt/sources.list.d/docker.list
apt-get update -y

echo "==> [3/5] Instalando Docker Engine, containerd e plugin Compose v2..."
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "==> [4/5] Habilitando e iniciando o serviço docker..."
systemctl enable --now docker

echo "==> [5/5] Adicionando o usuário '${USUARIO_ALVO}' ao grupo docker..."
usermod -aG docker "$USUARIO_ALVO"

echo
docker --version
docker compose version
pg_isready --version
echo
echo "OK: Docker instalado e ativo."
echo "IMPORTANTE: a mudança de grupo do usuário '${USUARIO_ALVO}' vale para novos logins."
echo "Para usar 'docker' sem sudo nesta sessão:  newgrp docker"
echo "Próximo passo (sem sudo): docker compose up -d postgres redis"