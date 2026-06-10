# Exercice 1 — Analyse et lancement du cluster
# Auteur : Hashimi (c-21454)

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
. (Join-Path $Root "scripts_windows\common.ps1")

Show-Banner "Exercice 1 : Demarrage et verification du cluster"

Write-Host "Lancement de Docker Compose..."
docker-compose -f (Join-Path $Root "docker-compose.yml") up -d

Write-Host ""
Write-Host "Attente de 8 secondes pour la stabilisation des healthchecks..."
Start-Sleep -Seconds 8

Write-Host ""
Write-Host "Etat des services :"
docker-compose -f (Join-Path $Root "docker-compose.yml") ps

Write-Host ""
Write-Host "Interface Web NameNode : http://localhost:9870"
Write-Host "Cluster : hashimi-c21454 | DataNodes attendus : 2 (Live)"
