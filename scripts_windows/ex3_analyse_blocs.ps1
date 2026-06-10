# Exercice 3 — Analyse des blocs et tolerance aux pannes
# Auteur : Hashimi (c-21454)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
. (Join-Path $Root "scripts_windows\common.ps1")

Show-Banner "Exercice 3 : Diagnostic FSCK et simulation de panne"
Assert-ContainerRunning

$HdfsFile = "$HdfsData/nyctrip.csv"

Write-Host "Analyse FSCK (blocs + localisations) :"
docker exec $Container hdfs fsck $HdfsFile -files -blocks -locations

Write-Host ""
Write-Host "Simulation de panne : arret de datanode1..."
docker stop datanode1

Write-Host ""
Write-Host "Lecture du fichier malgre la panne (5 premieres lignes) :"
docker exec $Container bash -c "hdfs dfs -cat '$HdfsFile' | head -n 5"

Write-Host ""
Write-Host "Redemarrage de datanode1 pour restaurer le cluster..."
docker start datanode1
Write-Host "Cluster restaure."
