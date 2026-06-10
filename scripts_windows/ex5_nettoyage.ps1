# Exercice 5 - Cloture et maintenance du cluster
# Auteur : Hashimi (c-21454)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
. (Join-Path $Root "scripts_windows\common.ps1")

Show-Banner "Exercice 5 : Arret securise du cluster"

$ComposeFile = Join-Path $Root "docker-compose.yml"

Write-Host "Arret des conteneurs (donnees preservees dans les volumes)..."
docker-compose -f $ComposeFile stop

Write-Host ""
Write-Host "ATTENTION - commandes destructives a ne jamais lancer en production :"
Write-Host "  docker-compose -f $ComposeFile down -v"
Write-Host "  docker system prune -a --volumes"
Write-Host ""
Write-Host "Ces commandes suppriment les volumes HDFS et effacent toutes les donnees."
