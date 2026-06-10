#!/bin/bash
# Exercice 4 — Gestion avancee des flux HDFS
# Auteur : Hashimi (c-21454)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
# shellcheck source=common.sh
source "${SCRIPT_DIR}/common.sh"

banner "Exercice 4 : Fusion, permissions et appendToFile"
require_container

echo "[1/3] Fusion de rapports partiels via getmerge"
run_hdfs -mkdir -p "${HDFS_REPORTS}"

for i in 1 2 3; do
    docker cp "${PROJECT_ROOT}/rapport${i}.txt" "${CONTAINER}:/tmp/rapport${i}.txt"
    run_hdfs -put -f "/tmp/rapport${i}.txt" "${HDFS_REPORTS}/"
done

run_hdfs -getmerge "${HDFS_REPORTS}/" /tmp/fusion_hashimi.txt
echo "Contenu fusionne :"
docker exec "${CONTAINER}" cat /tmp/fusion_hashimi.txt

echo ""
echo "[2/3] Gestion des permissions sur personnes.txt"
docker exec "${CONTAINER}" sh -c "echo 'Hashimi - c-21454' > /tmp/personnes.txt"
run_hdfs -put -f /tmp/personnes.txt "${HDFS_DATA}/personnes.txt"
run_hdfs -chown root:supergroup "${HDFS_DATA}/personnes.txt"
run_hdfs -chmod 600 "${HDFS_DATA}/personnes.txt"
run_hdfs -ls "${HDFS_DATA}/personnes.txt"

echo ""
echo "[3/3] Ajout incremental avec appendToFile"
docker exec "${CONTAINER}" sh -c "echo '[2026-06-14] INFO: Log Hashimi - taxi enregistre' > /tmp/log_hashimi.txt"
run_hdfs -appendToFile /tmp/log_hashimi.txt "${HDFS_DATA}/personnes.txt"
echo "Contenu final :"
run_hdfs -cat "${HDFS_DATA}/personnes.txt"
