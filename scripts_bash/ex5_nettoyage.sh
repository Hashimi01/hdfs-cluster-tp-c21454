#!/bin/bash
# Exercice 5 — Cloture et maintenance du cluster
# Auteur : Hashimi (c-21454)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "${SCRIPT_DIR}/common.sh"

banner "Exercice 5 : Arret securise du cluster"

COMPOSE_FILE="${SCRIPT_DIR}/../docker-compose.yml"

echo "Arret des conteneurs (donnees preservees dans les volumes)..."
docker-compose -f "${COMPOSE_FILE}" stop

echo ""
echo "ATTENTION — commandes destructives a ne jamais lancer en production :"
echo "  docker-compose -f ${COMPOSE_FILE} down -v"
echo "  docker system prune -a --volumes"
echo ""
echo "Ces commandes suppriment les volumes HDFS et effacent toutes les donnees."
