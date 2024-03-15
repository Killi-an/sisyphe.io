# Sisyphe.io

![Static Badge](https://img.shields.io/badge/Licence-CC--BY--NC--ND-blue)

Sisyphe.io est un **projet de NSI de Terminale**, créé et mené à bien durant l'année 2023-2024 par Killian MILANI, Siméon GILLET, Kylian ROUSSEAU, Abdelmalik MOUSSAOUI et Tristan BIBENS.

![Capture de l'écran titre du jeu](https://sisyphe.acciaw.me/img/capture.png)

## Résumé

Sisyphe.io nous plonge dans une mythologie grecque parallèle, où le supplice que les dieux infligent à Sisyphe est d'errer dans un dédale infini, à la recherche de rochers qu'il doit pousser jusque dans des trous situés de part et d'autre du terrain. Le Gameplay est basé sur le concept du *Sokoban*, mais Sisyphe.io propose de nombreuses mécaniques **inédites** que vous pourrez découvrir dans les **5 mondes disponibles** ! Le jeu dispose également d'un **éditeur de niveaux** complet et facile à utiliser !

## Démonstration

(LIEN VERS LA VIDEO)

## Prérequis, installation, déploiement

> [!NOTE]
> Le projet dispose d'un **site internet** dédié, que vous pouvez visiter à l'adresse https://sisyphe.acciaw.me/ depuis votre ordinateur ou smartphone. Le site internet est également disponible dans le code source du projet.

> [!TIP]
> Si vous ne souhaitez pas procéder à une installation complète du projet, vous pouvez simplement télécharger la version exécutable depuis l'onglet release du GitHub ou depuis le [site internet dédié](https://sisyphe.acciaw.me) au jeu.

> [!WARNING]
> Avant de vous lancer dans l'installation du projet, veuillez vous assurer que votre machine tourne sur une version stable de Windows 10 ou 11.

### Étapes de mise en route

1. Installez le logiciel Thonny sur votre machine
   - Cliquez [ici](https://thonny.org/) pour accéder au site de téléchargement officiel du logiciel
2. Une fois le logiciel installé, téléchargez le code source du projet depuis le [site internet officiel](https://sisyphe.acciaw.me) du jeu ou depuis le projet GitHub
   - Assurez-vous de décompresser le jeu dans un dossier facile d'accès sur votre machine
4. Double-cliquez sur le fichier "sisyphe.io_beta_v1.0.py" ou accédez au menu Clic-Droit -> Ouvrir avec -> Thonny
5. Une fois le fichier ouvert dans Thonny il vous faudra installer ses dépendances en vous rendant sur le menu suivant :

![Capture de la démarche pour installer les dépendances](https://sisyphe.acciaw.me/img/capture_dependances1.png)

6. Dans la fenêtre suivante, vous devrez rechercher puis installer les modules suivants : "pillow", "pil-supporter", "pygame"
7. Assurez-vous que la variable "fichier_exe" à la ligne 25 du fichier Python est initialisée à "False"
8. Il ne vous reste plus qu'à cliquer sur le bouton vert Excécuter le script courant ou sur la touche F5

## Dépendances

Voici la liste des dépendances Python suivies de leur(s) fonction(s) :
- **Tkinter (incluant ttk)** : Interface graphique du jeu,
- **Time** : Minuterie en jeu & compteur de FPS, 
- **Json** : Création et gestion des niveaux dans le jeu ainsi que dans l'éditeur, et gestion des paramètres du jeu,
- **Subprocess** : Ouverture de l'éditeur de niveaux depuis le programme principal,
- **Threading** : Module complémentaire de Subprocess pour garder la trace de la fenêtre de l'éditeur lancée,
- **sys** : Compilation du jeu en fichier.exe avec toutes ses dépendances,
- **os** : Gestion relative des chemins d'accès aux ressources du jeu, notamment pour accéder au répertoire appdata/local pour y stocker les paramètres de l'utilisateur,
- **shutil** : Création du dossier Sisyphe.io et de son fichier settings.json dans le répertoire appdata/local,
- **pygame** : Implémentation des sons ainsi que de la musique dans le jeu.

## Sources Utilisées

- Les musiques proviennent du jeu [Undertale Yellow](https://gamejolt.com/games/UndertaleYellow/136925)
- Le personnage a été créé en utilisant le site de personnalisation [Universal-LPC-Spritesheet-Character-Generator](https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator)
