# Programme de copie et renommage de fichiers pour les étudiants

Ce programme permet de renommer des fichiers Excel (grille de correction) pour chaque étudiant en fonction de la liste d'étudiants téléchargée en format CSV dans Léa. Le nom du fichier est généré à partir du **DA**, **nom**, **prénom**, et un **suffixe personnalisé** que vous spécifiez.

## Prérequis

- **Python** (version 3.x) installé sur votre machine.
- **Pandas** : bibliothèque Python pour manipuler des données. Vous pouvez l'installer via `pip install pandas`.

## Étapes d'utilisation

### 1. Télécharger la liste des étudiants

Rendez-vous sur **Léa** et téléchargez la liste des étudiants sous le format CSV avec un séparateur de **points virgules** (`;`). Le fichier doit avoir l'en-tête suivant :  
**DA de l'étudiant, nom, prénom**

Le fichier CSV devrait ressembler à ceci :
DA;Nom;Prénom 1234567;Dupont;Jean 2345678;Martin;Sophie ...

### 2. Préparer vos fichiers

Assurez-vous d'avoir :
- **Le fichier CSV** contenant la liste des étudiants (avec les colonnes "DA", "Nom", et "Prénom").
- **Le fichier Excel** de la grille de correction à copier et renommer.
- **Un dossier de destination** où les fichiers renommés seront copiés.

### 3. Utiliser le programme

Exécutez le programme Python avec les étapes suivantes :

1. **Téléchargez et sauvegardez le script** Python sur votre machine.
2. **Lancez le script** en exécutant la commande suivante dans le terminal (ou invite de commande) :
python nom_du_script.py

3. Le programme vous demandera les chemins des fichiers nécessaires :
- Entrez le chemin complet du fichier **CSV** contenant la liste des étudiants. Exemple :  
  `C:/chemin/vers/etudiants.csv`

- Entrez le chemin du **fichier Excel** de la grille de correction à copier et renommer. Exemple :  
  `C:/chemin/vers/grille_correction.xlsx`

- Entrez le chemin du **dossier de destination** où les fichiers seront copiés et renommés. Exemple :  
  `C:/chemin/vers/dossier_destination`

- Enfin, **entrez un suffixe personnalisé** pour les fichiers renommés (par exemple : TP1, TP2, etc.). Exemple :  
  `TP2`

4. Si tout est correctement configuré, le programme génèrera les nouveaux noms de fichiers en suivant le format :  
`DA_Nom_Prénom_suffixe.xlsx`

5. Le programme copiera chaque fichier de la grille de correction dans le dossier de destination avec le nouveau nom de fichier.

### Exemple d'exécution

Entrez le chemin du fichier CSV avec entête contenant la liste d'étudiants en format (DA;Nom;Prénom;): C:/chemin/vers/etudiants.csv 
Entrez le chemin de la grille de correction en format excel .xlsx: C:/chemin/vers/grille_correction.xlsx 
Entrez le chemin du dossier de destination (destination folder): C:/chemin/vers/dossier_destination 
Entrez le suffixe pour les fichiers (par exemple : TP1, TP2, etc.): TP2 
Copied and renamed to: C:/chemin/vers/dossier_destination/1234567_Dupont_Jean_TP2.xlsx 
Copied and renamed to: C:/chemin/vers/dossier_destination/2345678_Martin_Sophie_TP2.xlsx ...

### 4. Points importants

- Le fichier CSV doit être **séparé par des points virgules** et doit avoir l'en-tête **DA;Nom;Prénom**.
- Assurez-vous que le fichier Excel source existe et est bien au format `.xlsx`.
- Le programme remplace les espaces dans les noms par des underscores (`_`) pour créer des noms de fichiers valides.
- Si un fichier avec le même nom existe déjà dans le dossier de destination, il sera remplacé sans avertissement.
