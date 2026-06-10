#!/bin/bash
# Exercice 3 — Analyse des blocs et tolerance aux pannes
# Auteur : Hashimi (c-21454)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "${SCRIPT_DIR}/common.sh"

banner "Exercice 3 : Diagnostic FSCK et simulation de panne"
require_container

HDFS_FILE="${HDFS_DATA}/nyctrip.csv"

echo "Analyse FSCK (blocs + localisations) :"
docker exec "${CONTAINER}" hdfs fsck "${HDFS_FILE}" -files -blocks -locations

echo ""
echo "Simulation de panne : arret de datanode1..."
docker stop datanode1

echo ""
echo "Lecture du fichier malgre la panne (5 premieres lignes) :"
docker exec "${CONTAINER}" bash -c "hdfs dfs -cat '${HDFS_FILE}' | head -n 5"

echo ""
echo "Redemarrage de datanode1 pour restaurer le cluster..."
docker start datanode1
echo "Cluster restaure."
