# Exercice 4 — Gestion avancee des flux HDFS
# Auteur : Hashimi (c-21454)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
. (Join-Path $Root "scripts_windows\common.ps1")

Show-Banner "Exercice 4 : Fusion, permissions et appendToFile"
Assert-ContainerRunning

Write-Host "[1/3] Fusion de rapports partiels via getmerge"
Invoke-Hdfs -Cmd @('-mkdir', '-p', $HdfsReports)

foreach ($i in 1, 2, 3) {
    docker cp (Join-Path $Root "rapport$i.txt") "${Container}:/tmp/rapport$i.txt"
    Invoke-Hdfs -Cmd @('-put', '-f', "/tmp/rapport$i.txt", "$HdfsReports/")
}

Invoke-Hdfs -Cmd @('-getmerge', "$HdfsReports/", '/tmp/fusion_hashimi.txt')
Write-Host "Contenu fusionne :"
docker exec $Container cat /tmp/fusion_hashimi.txt

Write-Host ""
Write-Host "[2/3] Gestion des permissions sur personnes.txt"
docker exec $Container sh -c "echo 'Hashimi - c-21454' > /tmp/personnes.txt"
Invoke-Hdfs -Cmd @('-put', '-f', '/tmp/personnes.txt', "$HdfsData/personnes.txt")
Invoke-Hdfs -Cmd @('-chown', 'root:supergroup', "$HdfsData/personnes.txt")
Invoke-Hdfs -Cmd @('-chmod', '600', "$HdfsData/personnes.txt")
Invoke-Hdfs -Cmd @('-ls', "$HdfsData/personnes.txt")

Write-Host ""
Write-Host "[3/3] Ajout incremental avec appendToFile"
docker exec $Container sh -c "echo '[2026-06-14] INFO: Log Hashimi - taxi enregistre' > /tmp/log_hashimi.txt"
Invoke-Hdfs -Cmd @('-appendToFile', '/tmp/log_hashimi.txt', "$HdfsData/personnes.txt")
Write-Host "Contenu final :"
Invoke-Hdfs -Cmd @('-cat', "$HdfsData/personnes.txt")
