# TP Hadoop HDFS — Hashimi (c-21454)

Travaux pratiques de **Big Data & Systèmes Distribués** : déploiement d'un mini-cluster Hadoop via Docker, ingestion d'un dataset volumineux sur HDFS, analyse des blocs, réplication, tolérance aux pannes et opérations avancées.

| | |
|---|---|
| **Étudiant** | Hashimi |
| **Identifiant** | c-21454 |
| **Module** | Big Data & Systèmes Distribués |
| **Année universitaire** | 2025–2026 |
| **Cluster** | `hashimi-c21454` |

---

## Objectifs du TP

Ce dépôt documente la réalisation complète d'un TP Hadoop couvrant :

1. **Analyse et lancement** d'un cluster HDFS (1 NameNode + 2 DataNodes)
2. **Ingestion** du dataset NYC Taxi Trip (`nyctrip.csv`) dans HDFS
3. **Analyse FSCK** : découpage en blocs, localisation, réplication
4. **Tolérance aux pannes** : simulation d'arrêt d'un DataNode
5. **Gestion avancée** : fusion (`getmerge`), permissions, `appendToFile`
6. **Maintenance** : arrêt sécurisé et persistance des volumes Docker

---

## Architecture du cluster

```
                    ┌─────────────────┐
                    │    NameNode     │
                    │  :9870 (Web UI) │
                    │  :9000 (HDFS)   │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
     ┌────────▼────────┐         ┌──────────▼────────┐
     │   datanode1     │         │    datanode2      │
     │   :9864         │         │    :9865          │
     └─────────────────┘         └───────────────────┘
```

- **Images Docker :** `bde2020/hadoop-namenode` / `bde2020/hadoop-datanode` (Hadoop 3.2.1)
- **Réseau Docker :** `hashimi-c21454-hadoop-net`
- **Interface Web :** [http://localhost:9870](http://localhost:9870)

---

## Structure du dépôt

```
hadoop-tp-cluster/
├── docker-compose.yml          # Configuration du cluster
├── hadoop.env                  # Variables Hadoop (réplication, block size)
├── tp_config.env               # Chemins HDFS personnels
├── data/                       # Dataset local (nyctrip.csv, non versionné)
├── scripts_bash/               # Scripts Linux/Mac + common.sh
├── scripts_windows/            # Scripts PowerShell + common.ps1
├── rapport1.txt                # Rapport partiel — ingestion
├── rapport2.txt                # Rapport partiel — FSCK / blocs
├── rapport3.txt                # Rapport partiel — opérations avancées
├── Rapport_C21454_Hashimi_TP_Finale_Big_Data.pdf   # Rapport final
├── tp_hadoop_2026_Hashimi.mp4  # Vidéo de démonstration
└── tp hadoop.png               # Capture d'écran du cluster
```

### Chemins HDFS utilisés

| Usage | Chemin HDFS |
|-------|-------------|
| Datasets | `/user/hashimi/c21454/datasets/` |
| Rapports partiels | `/user/hashimi/c21454/rapports/` |

---

## Livrables

| Fichier | Description |
|---------|-------------|
| [`Rapport_C21454_Hashimi_TP_Finale_Big_Data.pdf`](Rapport_C21454_Hashimi_TP_Finale_Big_Data.pdf) | Rapport académique complet (8 pages) |
| [`tp_hadoop_2026_Hashimi.mp4`](tp_hadoop_2026_Hashimi.mp4) | Vidéo de démonstration de l'exécution du TP |
| [`tp hadoop.png`](tp%20hadoop.png) | Capture d'écran de l'interface NameNode / cluster |

### Aperçu — Interface NameNode

![Capture d'écran du cluster Hadoop — Hashimi c-21454](tp%20hadoop.png)

---

## Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et **démarré**
- Fichier `data/nyctrip.csv` présent localement (dataset NYC Taxi Trip, ~562 Mo)
- PowerShell (Windows) ou Bash (Linux/Mac)

> **Note :** le dossier `data/` est ignoré par Git (fichier trop volumineux). Placez manuellement `nyctrip.csv` dans `data/` avant de lancer le TP.

---

## Exécution pas à pas

Ouvrir un terminal à la racine du projet :

```powershell
cd "chemin/vers/hadoop-tp-cluster"
```

### Exercice 1 — Lancement du cluster

```powershell
.\scripts_windows\ex1_lancement.ps1
```

```bash
./scripts_bash/ex1_lancement.sh
```

Vérifier que les 3 conteneurs sont **healthy**, puis ouvrir [http://localhost:9870](http://localhost:9870) : onglet **Datanodes** → 2 nœuds **Live**.

---

### Exercice 2 — Ingestion et réplication

```powershell
.\scripts_windows\ex2_manipulation.ps1
```

```bash
./scripts_bash/ex2_manipulation.sh
```

**Actions réalisées :**
- Création de `/user/hashimi/c21454/datasets/`
- Upload de `nyctrip.csv` vers HDFS
- Vérification du facteur de réplication (3 par défaut)
- Réduction à 2 avec `hdfs dfs -setrep -w 2`

---

### Exercice 3 — Analyse FSCK et tolérance aux pannes

```powershell
.\scripts_windows\ex3_analyse_blocs.ps1
```

```bash
./scripts_bash/ex3_analyse_blocs.sh
```

**Actions réalisées :**
- Diagnostic `hdfs fsck` (blocs, localisations)
- Statut **HEALTHY**
- Arrêt simulé de `datanode1` puis vérification de la disponibilité des données
- Redémarrage automatique de `datanode1`

---

### Exercice 4 — Gestion avancée

```powershell
.\scripts_windows\ex4_gestion_avancee.ps1
```

```bash
./scripts_bash/ex4_gestion_avancee.sh
```

**Actions réalisées :**
- Fusion des rapports partiels via `getmerge`
- Gestion des permissions (`chown`, `chmod 600`)
- Ajout incrémental avec `appendToFile`

---

### Exercice 5 — Arrêt et maintenance

```powershell
.\scripts_windows\ex5_nettoyage.ps1
```

```bash
./scripts_bash/ex5_nettoyage.sh
```

Arrête les conteneurs **sans supprimer les volumes** (données HDFS conservées).

> **Attention :** `docker-compose down -v` supprime définitivement toutes les données HDFS.

---

## Redémarrage propre (avant enregistrement vidéo)

```powershell
docker-compose down
docker-compose up -d
Start-Sleep -Seconds 30
docker-compose ps
```

Puis exécuter les exercices 1 → 5 dans l'ordre.

---

## Résultats attendus

| Exercice | Résultat clé |
|----------|--------------|
| Ex. 1 | 3 conteneurs `healthy`, 2 DataNodes Live sur le port 9870 |
| Ex. 2 | Fichier visible dans HDFS, réplication = 2 |
| Ex. 3 | FSCK `HEALTHY`, blocs répartis sur les DataNodes |
| Ex. 4 | Fusion des 3 rapports, permissions `600`, append réussi |
| Ex. 5 | Cluster arrêté, volumes préservés |

---

## Auteur

**Hashimi** — Identifiant **c-21454**  
Travail personnel réalisé dans le cadre du module Big Data (2025–2026).

Ce dépôt contient l'ensemble du code, de la configuration, du rapport PDF, de la vidéo de démonstration et des captures d'écran produits pour ce TP.
