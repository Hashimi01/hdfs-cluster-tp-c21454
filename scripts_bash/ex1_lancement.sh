#!/bin/bash
# Exercice 1 — Analyse et lancement du cluster
# Auteur : Hashimi (c-21454)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "${SCRIPT_DIR}/common.sh"

banner "Exercice 1 : Demarrage et verification du cluster"

echo "Lancement de Docker Compose..."
docker-compose -f "${SCRIPT_DIR}/../docker-compose.yml" up -d

echo ""
echo "Attente de 8 secondes pour la stabilisation des healthchecks..."
sleep 8

echo ""
echo "Etat des services :"
docker-compose -f "${SCRIPT_DIR}/../docker-compose.yml" ps

echo ""
echo "Interface Web NameNode : http://localhost:9870"
echo "Cluster : hashimi-c21454 | DataNodes attendus : 2 (Live)"
