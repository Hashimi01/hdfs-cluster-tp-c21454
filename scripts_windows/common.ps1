# Hashimi (c-21454) - configuration partagee PowerShell

$script:Container = "namenode"
$script:LocalCsv = "/tp/data/nyctrip.csv"
$script:HdfsRoot = "/user/hashimi/c21454"
$script:HdfsData = "$script:HdfsRoot/datasets"
$script:HdfsReports = "$script:HdfsRoot/rapports"

function Show-Banner {
    param([string]$Title)
    Write-Host "============================================================"
    Write-Host "  TP Hadoop HDFS - Hashimi (c-21454)"
    Write-Host "  $Title"
    Write-Host "============================================================"
}

function Assert-ContainerRunning {
    $running = docker ps --format "{{.Names}}" | Select-String -Pattern "^$($script:Container)$"
    if (-not $running) {
        Write-Error "Conteneur $($script:Container) non demarre. Lancez ex1_lancement.ps1."
        exit 1
    }
}

function Invoke-Hdfs {
    param([string[]]$Cmd)
    docker exec $script:Container hdfs dfs @Cmd
}
