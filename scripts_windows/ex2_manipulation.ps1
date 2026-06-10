# Exercice 2 — Ingestion et consultation des donnees HDFS
# Auteur : Hashimi (c-21454)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
. (Join-Path $Root "scripts_windows\common.ps1")

Show-Banner "Exercice 2 : Ingestion du dataset NYC Taxi Trip"
Assert-ContainerRunning

Write-Host "[1/5] Creation de lespace HDFS personnel : $HdfsData"
Invoke-Hdfs -Cmd @('-mkdir', '-p', $HdfsData)

Write-Host ""
Write-Host "[2/5] Verification du fichier local : $LocalCsv"
docker exec $Container test -f $LocalCsv

Write-Host ""
Write-Host "[3/5] Transfert vers HDFS :"
Invoke-Hdfs -Cmd @('-put', $LocalCsv, "$HdfsData/")

Write-Host ""
Write-Host "[4/5] Facteur de replication par defaut :"
Invoke-Hdfs -Cmd @('-stat', '%r', "$HdfsData/nyctrip.csv")

Write-Host ""
Write-Host "[5/5] Reduction du facteur de replication a 2 (option -w) :"
Invoke-Hdfs -Cmd @('-setrep', '-w', '2', "$HdfsData/nyctrip.csv")

Write-Host ""
Write-Host "Inventaire HDFS :"
Invoke-Hdfs -Cmd @('-ls', "$HdfsData/")
