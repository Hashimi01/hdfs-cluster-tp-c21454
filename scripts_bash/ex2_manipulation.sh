#!/bin/bash
# Exercice 2 — Ingestion et consultation des donnees HDFS
# Auteur : Hashimi (c-21454)

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "${SCRIPT_DIR}/common.sh"

banner "Exercice 2 : Ingestion du dataset NYC Taxi Trip"
require_container

echo "[1/5] Creation de l'espace HDFS personnel : ${HDFS_DATA}"
run_hdfs -mkdir -p "${HDFS_DATA}"

echo ""
echo "[2/5] Verification de la presence du fichier local : ${LOCAL_CSV}"
docker exec "${CONTAINER}" test -f "${LOCAL_CSV}"

echo ""
echo "[3/5] Transfert vers HDFS :"
run_hdfs -put "${LOCAL_CSV}" "${HDFS_DATA}/"

echo ""
echo "[4/5] Facteur de replication par defaut :"
run_hdfs -stat "%r" "${HDFS_DATA}/nyctrip.csv"

echo ""
echo "[5/5] Reduction du facteur de replication a 2 (option -w) :"
run_hdfs -setrep -w 2 "${HDFS_DATA}/nyctrip.csv"

echo ""
echo "Inventaire HDFS :"
run_hdfs -ls "${HDFS_DATA}/"
