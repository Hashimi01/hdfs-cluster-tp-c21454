#!/usr/bin/env python3
"""Generate academic PDF report for Hadoop TP - Hashimi c-21454."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path(__file__).parent / "Rapport_C21454_Hashimi_TP_Finale_Big_Data.pdf"
FONT_REG = "C:/Windows/Fonts/times.ttf"
FONT_BOLD = "C:/Windows/Fonts/timesbd.ttf"
FONT_ITALIC = "C:/Windows/Fonts/timesi.ttf"
FONT_NAME = "TNR"


class AcademicReport(FPDF):
    def __init__(self):
        super().__init__(format="A4", unit="mm")
        self.set_auto_page_break(auto=True, margin=25)
        self.add_font(FONT_NAME, "", FONT_REG)
        self.add_font(FONT_NAME, "B", FONT_BOLD)
        self.add_font(FONT_NAME, "I", FONT_ITALIC)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font(FONT_NAME, "I", 9)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, "Rapport TP Hadoop HDFS — Hashimi (c-21454)", align="C", new_x="LMARGIN", new_y="NEXT")
        self.line(10, 18, 200, 18)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font(FONT_NAME, "I", 9)
        self.set_text_color(90, 90, 90)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, number: str, title: str):
        self.ln(4)
        self.set_font(FONT_NAME, "B", 14)
        self.set_text_color(20, 40, 80)
        self.multi_cell(0, 8, f"{number}  {title}")
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def subsection_title(self, title: str):
        self.ln(2)
        self.set_font(FONT_NAME, "B", 12)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 7, title)
        self.ln(1)
        self.set_text_color(0, 0, 0)

    def body(self, text: str):
        self.set_font(FONT_NAME, "", 11)
        self.multi_cell(0, 6.5, text)
        self.ln(1)

    def bullet(self, text: str):
        self.set_font(FONT_NAME, "", 11)
        x = self.get_x()
        self.cell(6, 6.5, chr(8226))
        self.multi_cell(0, 6.5, text)
        self.set_x(x)

    def code_block(self, text: str):
        self.set_fill_color(245, 245, 245)
        self.set_font("Courier", "", 9)
        self.multi_cell(0, 5.5, text, fill=True)
        self.ln(2)
        self.set_font(FONT_NAME, "", 11)

    def table_row(self, cols, widths, header=False):
        if header:
            self.set_font(FONT_NAME, "B", 10)
            self.set_fill_color(230, 235, 245)
        else:
            self.set_font(FONT_NAME, "", 10)
            self.set_fill_color(255, 255, 255)
        h = 7
        for i, (col, w) in enumerate(zip(cols, widths)):
            self.cell(w, h, col, border=1, fill=True, align="L")
        self.ln(h)


def build_report():
    pdf = AcademicReport()
    pdf.set_margins(20, 20, 20)

    # --- Page de garde ---
    pdf.add_page()
    pdf.ln(35)
    pdf.set_font(FONT_NAME, "B", 22)
    pdf.set_text_color(20, 40, 80)
    pdf.multi_cell(0, 12, "Rapport de Travaux Pratiques", align="C")
    pdf.ln(4)
    pdf.set_font(FONT_NAME, "B", 16)
    pdf.multi_cell(0, 10, "Déploiement et Manipulation de Données\nsur Hadoop HDFS", align="C")
    pdf.ln(20)
    pdf.set_font(FONT_NAME, "", 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "Module : Big Data & Systèmes Distribués", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)
    pdf.set_font(FONT_NAME, "", 12)
    pdf.cell(0, 8, "Étudiant : Hashimi", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Identifiant : c-21454", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(25)
    pdf.set_font(FONT_NAME, "I", 12)
    pdf.cell(0, 8, "Année universitaire 2025–2026", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Juin 2026", align="C")

    # --- Introduction ---
    pdf.add_page()
    pdf.section_title("1.", "Introduction")
    pdf.body(
        "Le présent rapport documente la réalisation d'un travail pratique portant sur "
        "l'architecture Hadoop et le système de fichiers distribué HDFS (Hadoop Distributed "
        "File System). L'objectif pédagogique consiste à déployer un mini-cluster Hadoop "
        "containerisé, à ingérer un jeu de données volumineux, puis à analyser les mécanismes "
        "fondamentaux du Big Data : découpage en blocs, réplication, tolérance aux pannes "
        "et administration du cycle de vie du cluster."
    )
    pdf.body(
        "Le corpus expérimental repose sur le dataset NYC Taxi Trip (fichier CSV d'environ "
        "562 Mo), déployé au sein d'une infrastructure Docker Compose composée d'un NameNode "
        "et de deux DataNodes. L'ensemble des manipulations a été automatisé par des scripts "
        "Bash et PowerShell fournis dans le dépôt hadoop-tp-cluster."
    )

    pdf.subsection_title("1.1 Objectifs du travail pratique")
    for obj in [
        "Analyser et lancer un cluster Hadoop via Docker Compose.",
        "Ingérer et consulter des données massives dans HDFS.",
        "Étudier le découpage en blocs et la réplication des données.",
        "Manipuler les flux de données et les opérations avancées (fusion, permissions, append).",
        "Maîtriser l'arrêt, la persistance et la maintenance sécurisée du cluster.",
    ]:
        pdf.bullet(obj)

    pdf.subsection_title("1.2 Environnement expérimental")
    pdf.body(
        "L'environnement repose sur Docker Compose (version 3.8), les images bde2020/hadoop-namenode "
        "et bde2020/hadoop-datanode (Hadoop 3.2.1, Java 8), ainsi que les fichiers hadoop.env "
        "et tp_config.env. Le cluster est nommé hashimi-c21454 et utilise l'espace HDFS "
        "/user/hashimi/c21454/. L'interface Web du NameNode est accessible sur http://localhost:9870."
    )

    # --- Exercice 1 ---
    pdf.add_page()
    pdf.section_title("2.", "Exercice 1 — Analyse et lancement du cluster")
    pdf.subsection_title("2.1 Analyse du fichier docker-compose.yml")
    pdf.body(
        "Le fichier docker-compose.yml décrit une architecture HDFS minimale mais représentative "
        "d'un déploiement distribué : un service namenode (nœud maître) et deux services "
        "datanode1 et datanode2 (nœuds esclaves). Chaque service charge les variables "
        "d'environnement depuis hadoop.env et monte le répertoire local data vers /tp/data."
    )
    pdf.body(
        "Concernant l'exposition des ports, le NameNode publie les ports 9870 (interface Web) "
        "et 9000 (protocole HDFS). Les DataNodes exposent respectivement 9864:9864 pour "
        "datanode1 et 9865:9864 pour datanode2. Ce second mapping est une pratique standard "
        "lorsque plusieurs conteneurs utilisent le même port interne (9864/tcp) : il évite "
        "tout conflit sur la machine hôte tout en conservant la communication interne via "
        "le réseau Docker."
    )

    pdf.subsection_title("2.2 Démarrage et diagnostic")
    pdf.body("Le cluster est démarré par la commande suivante :")
    pdf.code_block("docker-compose up -d")
    pdf.body("L'état des conteneurs est ensuite contrôlé par :")
    pdf.code_block("docker-compose ps")
    pdf.body(
        "Le statut healthy atteste du succès des healthchecks internes. Pour le NameNode, "
        "cela garantit que le service est opérationnel et prêt à gérer les métadonnées HDFS. "
        "Les deux DataNodes apparaissent également en état sain, confirmant leur intégration "
        "au cluster."
    )

    pdf.subsection_title("2.3 Validation via l'interface Web")
    pdf.body(
        "L'interface Web du NameNode (http://localhost:9870) permet de visualiser l'état "
        "global du cluster. Dans l'onglet Datanodes, les deux nœuds datanode1 et datanode2 "
        "sont listés avec le statut Live. Cette observation confirme que le déploiement "
        "Docker est fonctionnel et que la communication NameNode–DataNodes est établie."
    )

    # --- Exercice 2 ---
    pdf.add_page()
    pdf.section_title("3.", "Exercice 2 — Ingestion et consultation des données")
    pdf.subsection_title("3.1 Création de l'espace de stockage HDFS")
    pdf.code_block("hdfs dfs -mkdir -p /user/hashimi/c21454/datasets")
    pdf.body(
        "La commande mkdir -p crée la hiérarchie de répertoires nécessaire. L'option -p "
        "permet de créer les répertoires parents manquants, conformément au comportement "
        "habituel des systèmes de fichiers."
    )

    pdf.subsection_title("3.2 Chargement du dataset")
    pdf.code_block("hdfs dfs -put /tp/data/nyctrip.csv /user/hashimi/c21454/datasets/")
    pdf.body(
        "Cette opération transfère le fichier depuis le système de fichiers local (monté "
        "dans le conteneur) vers HDFS. Le NameNode enregistre les métadonnées tandis que "
        "HDFS découpe automatiquement le fichier en blocs de 128 Mo et les distribue sur "
        "les DataNodes disponibles."
    )

    pdf.subsection_title("3.3 Vérification et facteur de réplication")
    pdf.code_block("hdfs dfs -ls /user/hashimi/c21454/datasets/\nhdfs dfs -stat \"%r\" /user/hashimi/c21454/datasets/nyctrip.csv")
    pdf.body(
        "La commande ls confirme la présence du fichier nyctrip.csv (562 386 202 octets, "
        "soit environ 562 Mo). La colonne de réplication affiche la valeur 3, correspondant "
        "au facteur par défaut de HDFS. Chaque bloc est ainsi dupliqué sur trois nœuds, "
        "garantissant la tolérance aux pannes."
    )

    pdf.subsection_title("3.4 Modification du facteur de réplication")
    pdf.code_block("hdfs dfs -setrep -w 2 /user/hashimi/c21454/datasets/nyctrip.csv")
    pdf.body(
        "L'option -setrep 2 réduit le nombre de copies à deux. L'option -w (wait) est "
        "essentielle : elle force Hadoop à attendre la fin effective de la réplication avant "
        "de retourner le contrôle. Sans cette option, la commande pourrait se terminer "
        "prématurément, laissant des blocs partiellement répliqués."
    )

    pdf.subsection_title("3.5 Synthèse")
    pdf.body(
        "Cet exercice illustre le cycle complet d'ingestion d'un dataset volumineux dans "
        "HDFS et met en évidence le rôle central de la réplication dans la fiabilité du "
        "stockage distribué."
    )

    # --- Exercice 3 ---
    pdf.add_page()
    pdf.section_title("4.", "Exercice 3 — Analyse des blocs")
    pdf.subsection_title("4.1 Diagnostic FSCK")
    pdf.code_block("hdfs fsck /user/hashimi/c21454/datasets/nyctrip.csv -files -blocks -locations")
    pdf.body(
        "La commande fsck (File System Check) analyse l'intégrité du fichier dans HDFS. "
        "Le résultat HEALTHY confirme que tous les blocs sont présents, correctement "
        "répliqués et localisés sur les DataNodes du cluster."
    )

    pdf.subsection_title("4.2 Découpage en blocs")
    pdf.body(
        "Avec une taille de bloc par défaut de 128 Mo et un fichier de 562 Mo, le calcul "
        "théorique donne : 562 ÷ 128 ≈ 4,4, soit 5 blocs au total. HDFS ne stocke jamais "
        "un fichier volumineux dans un bloc unique : cette fragmentation permet le traitement "
        "parallèle, la répartition de charge et la scalabilité horizontale, piliers "
        "fondamentaux du paradigme Big Data."
    )

    pdf.subsection_title("4.3 Localisation et réplication")
    pdf.body(
        "Chaque bloc est réparti sur plusieurs DataNodes conformément au facteur de "
        "réplication configuré. Cette redondance géographique (au sein du cluster) assure "
        "la disponibilité des données même en cas de défaillance matérielle ou logicielle "
        "d'un nœud."
    )

    pdf.subsection_title("4.4 Test de tolérance aux pannes")
    pdf.code_block("docker stop datanode1\nhdfs dfs -cat /user/hashimi/c21454/datasets/nyctrip.csv | head")
    pdf.body(
        "L'arrêt simulé de datanode1 n'empêche pas la lecture du fichier. Grâce à la "
        "réplication, chaque bloc dispose de copies sur d'autres DataNodes. HDFS route "
        "automatiquement les requêtes de lecture vers les nœuds disponibles, démontrant "
        "la robustesse du système face aux pannes fréquentes en environnement distribué."
    )

    # --- Exercice 4 ---
    pdf.add_page()
    pdf.section_title("5.", "Exercice 4 — Gestion avancée des flux HDFS")
    pdf.subsection_title("5.1 Fusion de fichiers (getmerge)")
    pdf.body(
        "Trois fichiers textuels (rapport1.txt, rapport2.txt, rapport3.txt) ont été "
        "chargés dans /user/hashimi/c21454/rapports/, puis fusionnés localement via la commande "
        "getmerge, qui concatène l'ensemble des fichiers d'un répertoire HDFS en un "
        "fichier unique."
    )
    pdf.code_block("hdfs dfs -getmerge /user/hashimi/c21454/rapports/ /tmp/fusion_hashimi.txt")

    pdf.subsection_title("5.2 Gestion des permissions")
    pdf.body(
        "Un fichier personnes.txt a été créé sur HDFS, puis ses droits ont été restreints "
        "à l'aide de chown et chmod 600. Cette manipulation rappelle que HDFS implémente "
        "un modèle de permissions comparable à POSIX (propriétaire, groupe, autres), "
        "indispensable en contexte multi-utilisateurs."
    )
    pdf.code_block(
        "hdfs dfs -chown root:supergroup /user/hashimi/c21454/datasets/personnes.txt\n"
        "hdfs dfs -chmod 600 /user/hashimi/c21454/datasets/personnes.txt"
    )

    pdf.subsection_title("5.3 Ajout incrémental via appendToFile")
    pdf.code_block(
        'echo "[2026-06-14] INFO: Log Hashimi - taxi enregistre" > log_hashimi.txt\n'
        "hdfs dfs -appendToFile log_hashimi.txt /user/hashimi/c21454/datasets/personnes.txt"
    )
    pdf.body(
        "La commande appendToFile permet d'ajouter du contenu à un fichier HDFS existant "
        "sans le réimporter intégralement. Cette fonctionnalité est particulièrement "
        "utile pour les flux de logs et les données séquentielles. L'expérimentation "
        "a également mis en lumière l'importance de la précision des chemins : une "
        "erreur de nommage peut créer un fichier distinct plutôt que d'enrichir le "
        "fichier cible. Par ailleurs, les opérations d'écriture nécessitent des DataNodes "
        "opérationnels ; une indisponibilité temporaire peut provoquer des erreurs de "
        "pipeline (lease recovery)."
    )

    # --- Exercice 5 ---
    pdf.add_page()
    pdf.section_title("6.", "Exercice 5 — Clôture et maintenance du cluster")
    pdf.subsection_title("6.1 Arrêt contrôlé")
    pdf.code_block("docker-compose stop\n# ou\ndocker-compose down")
    pdf.body(
        "L'arrêt via docker-compose stop interrompt les conteneurs tout en préservant "
        "les volumes Docker. Les données HDFS demeurent intactes et seront disponibles "
        "au prochain redémarrage."
    )

    pdf.subsection_title("6.2 Persistance des données")
    pdf.body(
        "Les blocs HDFS sont stockés dans des volumes Docker persistants. Tant que "
        "l'option -v n'est pas utilisée, un redémarrage du cluster ne provoque aucune "
        "perte de données. En revanche, la commande docker-compose down -v supprime "
        "les volumes associés, entraînant une effacement irréversible du contenu HDFS."
    )

    pdf.subsection_title("6.3 Commandes à risque en production")
    pdf.code_block("docker-compose down -v\ndocker system prune -a --volumes")
    pdf.body(
        "Ces commandes sont particulièrement dangereuses en environnement de production "
        "Big Data. Elles suppriment conteneurs, images et volumes, détruisant ainsi "
        "l'ensemble des données distribuées. Toute opération de maintenance doit être "
        "précédée d'une sauvegarde et d'une validation explicite des volumes concernés."
    )

    # --- Tableau récapitulatif ---
    pdf.add_page()
    pdf.section_title("7.", "Tableau récapitulatif des concepts Hadoop")
    widths = [45, 135]
    pdf.table_row(["Concept", "Définition et observation durant le TP"], widths, header=True)
    rows = [
        ("NameNode", "Nœud maître gérant les métadonnées HDFS (arborescence, blocs, permissions). Interface Web sur le port 9870."),
        ("DataNode", "Nœuds esclaves stockant physiquement les blocs. Assurent lecture, écriture et réplication."),
        ("Block Size", "Taille maximale d'un bloc (128 Mo par défaut). Le fichier nyctrip.csv (562 Mo) est découpé en 5 blocs."),
        ("Replication Factor", "Nombre de copies par bloc (3 par défaut, modifié à 2). Garantit la tolérance aux pannes."),
        ("FSCK", "Outil de diagnostic vérifiant l'intégrité, la localisation et l'état de santé des fichiers HDFS."),
        ("appendToFile", "Commande d'ajout incrémental au contenu d'un fichier HDFS sans réimport complet."),
        ("getmerge", "Fusion de fichiers d'un répertoire HDFS en un fichier local unique."),
    ]
    for row in rows:
        pdf.table_row(row, widths)

    # --- Conclusion générale ---
    pdf.ln(6)
    pdf.section_title("8.", "Conclusion générale")
    pdf.body(
        "Ce travail pratique a permis de mettre en œuvre et d'analyser les composants "
        "essentiels de l'écosystème Hadoop. Le déploiement containerisé via Docker Compose "
        "facilite la reproductibilité de l'environnement expérimental, tandis que "
        "l'ingestion du dataset NYC Taxi Trip offre un cas d'usage réaliste de traitement "
        "de données massives."
    )
    pdf.body(
        "Les exercices réalisés démontrent que HDFS repose sur trois principes "
        "architecturaux fondamentaux : la fragmentation des fichiers en blocs, la "
        "réplication pour la fiabilité, et la distribution sur plusieurs nœuds pour "
        "la scalabilité. La simulation de panne et l'analyse FSCK confirment la "
        "robustesse du système. Enfin, les opérations avancées (fusion, permissions, "
        "append) et la gestion du cycle de vie du cluster soulignent l'importance d'une "
        "administration rigoureuse en contexte Big Data."
    )

    # --- Références ---
    pdf.subsection_title("Références bibliographiques")
    refs = [
        "Apache Hadoop Documentation — HDFS Architecture. https://hadoop.apache.org/docs/stable/",
        "White, T. (2015). Hadoop: The Definitive Guide (4th ed.). O'Reilly Media.",
        "Docker Inc. — Docker Compose Documentation. https://docs.docker.com/compose/",
        "Big Data Europe — bde2020/hadoop-docker images. https://github.com/big-data-europe/docker-hadoop",
    ]
    for ref in refs:
        pdf.bullet(ref)

    pdf.output(str(OUTPUT))
    print("Rapport genere avec succes.")


if __name__ == "__main__":
    build_report()
