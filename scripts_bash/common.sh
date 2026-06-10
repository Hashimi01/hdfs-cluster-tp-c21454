#!/bin/bash
# Hashimi (c-21454) — fonctions utilitaires partagées

CONTAINER="namenode"
LOCAL_CSV="/tp/data/nyctrip.csv"
HDFS_ROOT="/user/hashimi/c21454"
HDFS_DATA="${HDFS_ROOT}/datasets"
HDFS_REPORTS="${HDFS_ROOT}/rapports"

banner() {
    echo "============================================================"
    echo "  TP Hadoop HDFS — Hashimi (c-21454)"
    echo "  $1"
    echo "============================================================"
}

require_container() {
    if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
        echo "Erreur : le conteneur '${CONTAINER}' n'est pas demarre."
        echo "Lancez d'abord : ./scripts_bash/ex1_lancement.sh"
        exit 1
    fi
}

run_hdfs() {
    docker exec "${CONTAINER}" hdfs dfs "$@"
}
