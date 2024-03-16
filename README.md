# Sisyphe.io

[![Capture de l'écran titre du jeu](source/assets/img/menus/sisyphe.png)](https://sisyphe.acciaw.me)

[![Static Badge](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue)](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1)

Sisyphe.io est un **projet de NSI de Terminale**, créé et mené à bien durant l'année 2023-2024 par Killian MILANI, Siméon GILLET, Kylian ROUSSEAU, Abdelmalik MOUSSAOUI et Tristan BIBENS sous le nom Team ST-2A2K.

Un accès complet à **l'historique des modifications version par version** du projet jusqu'à la release est disponible [ici](source/changelog.txt).

## Résumé

Le jeu nous plonge dans une mythologie grecque parallèle, où le supplice que les dieux infligent à Sisyphe est d'errer dans un dédale infini, à la recherche de rochers qu'il doit pousser jusque dans des trous situés de part et d'autre du terrain. Le Gameplay est basé sur le concept du *Sokoban*, mais Sisyphe.io propose de nombreuses mécaniques **inédites** que vous pourrez découvrir dans les **5 mondes disponibles** ! Le jeu dispose également d'un **éditeur de niveaux** complet et facile à utiliser !

## Démonstration

(LIEN VERS LA VIDEO)

## Pré-requis, installation, déploiement

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
4. Ouvrez le répertoire "source" du projet puis double-cliquez sur le fichier "sisyphe.io_beta_v1.0.py" ou accédez au menu Clic-Droit -> Ouvrir avec -> Thonny
5. Une fois le fichier ouvert dans Thonny, il vous faudra installer ses dépendances en vous rendant sur le menu Outils -> Gérer les paquets... :

![Capture Dépendances](https://github.com/Killi-an/sisyphe.io/assets/157998078/a2d2b883-6e1c-4725-9b54-38a055a7d640)


6. Dans la fenêtre suivante, vous devrez rechercher puis installer les modules suivants : "pillow", "pil-supporter", "pygame"
7. Assurez-vous que la variable "fichier_exe" à la ligne 25 du fichier Python est initialisée à "False"
8. Il ne vous reste plus qu'à cliquer sur le bouton vert Excécuter le script courant ou sur la touche F5
9. Si le projet ne se lance pas avec comme erreur une clé manquante, ouvrez et exécutez avec Thonny le fichier Python "del_save.py" se trouvant dans le répertoire "assets" du projet.

## Description de l'architecture

Le code source du projet contient : 
- Ce **fichier "Read-Me"**,
- Un **fichier "requirements.txt"** listant les pré-requis de lancement et de fonctionnement du projet,
- Un **répertoire "docs"** contenant la documentation technique du projet,
- Un **répertoire "sources"** composé :
   - D'un **fichier "compilateur.txt"** contenant des commandes pour compiler le jeu en .exe (à ignorer),
   - D'un **fichier "sisyphe.io_beta_v1.0.py"**, fichier principal du jeu,
   - D'un **répertoire "assets"** composé :
     - D'un **fichier "sisyphe.io_editor_v2.0.py"** utilisé par le programme principal pour l'éditeur,
     - D'un **fichier "settings.json"** qui est copié au premier lancement du jeu dans le répertoire appdata/local/Sisyphe.io,
     - D'un **répertoire "img"** contenant les images du jeu,
     - D'un **répertoire "mus"** contenant la musique du jeu,
     - D'un **répertoire "niveaux"** contenant les niveaux principaux du jeu,
     - D'un **répertoire "package"** composé :
        - D'un **module "game_deroulement.py"** servant à gérer le déroulement du programme principal,
        - D'un **module "game_images.py"** servant à charger et utiliser les images du jeu,
        - D'un **module "game_lang.py"** servant à stocker les différentes langues du jeu (12),
        - D'un **module "game_music.py"** servant à charger et utiliser la musique et les sons du jeu,
        - D'un **module "game_tooltip.py"** servant à définir et charger les tutoriels pour chaque monde du jeu,
     - D'un **répertoire "sfx"** contenant les sons du jeu,
   - D'un **répertoire "idees_niveaux"** contenant des tests de niveaux personnalisés à essayer,
   - D'un **répertoire "site_web"** contenant le code source complet du site internet dédié au jeu.

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

Le site internet du jeu utilise des bibliothèques de code indépendantes non modifiées fournies par des tiers :

![JQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)

## Sources Utilisées

- Toutes les musiques proviennent du jeu [Undertale Yellow](https://gamejolt.com/games/UndertaleYellow/136925) : 
   - Menu : [OST: 051 - Feisty!](https://youtu.be/hvl1GqD-Vis)
   - Sélection de mondes : [OST: 056 - The Stable](https://youtu.be/owAVwJ5-EaE)
   - Paramètres : [OST: 053 - Happy Hour](https://youtu.be/T0IRbP1Z2pI?si=fZkLpd8WWcjTBq68)
   - Éditeur : [OST: 081 - Build-A-Bot](https://youtu.be/ut-_p-P9lsI)
   - Monde 1 : [OST: 012 - Seclusion](https://youtu.be/CinLLgjqUqI)
   - Monde 2 : [OST: 037 - Mining Co](https://youtu.be/wJVubgGxUwI)
   - Monde 3 : [OST: 055 - The Wild East](https://youtu.be/5Q6Ss9uoQhE)
   - Monde 4 : [OST: 035 - Vigorous Terrain](https://youtu.be/PuHE_GRzT5Q)
   - Monde 5 : [OST: 070 - Showdown!](https://youtu.be/b4Z_GFpXScI)
   - Crédits (inutilisée) : [OST: 067 - Deal 'Em Out](https://www.youtube.com/watch?v=IetJ8URgg5c)
- Tous les sons du jeu proviennent du site internet https://freesound.org/ sous la **licence Creative Commons Zero**,
- Le personnage a été créé en utilisant le site de personnalisation [Universal-LPC-Spritesheet-Character-Generator](https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator),
- Les illustrations du jeu (logos/Image de présentation) ont été réalisées par **Arthur BARBEROUSSE**, élève du lycée Edmond Perrier en classe de Terminale.

## Licenses

**License Sokoban :**

Sokoban® & © 1982 Thinking Rabbit Co., Ltd.  
Sokoban logo, Sokoban theme song, and Sokoban mechanics are trademarks of Thinking Rabbit Co., Ltd.  
Licensed to Unbalance Co., Ltd.  
Game Design by Hiroyuki Imabayashi.  
All Rights Reserved.

----

**License Undertale Yellow :**

Undertale Yellow is a free fan project based on Undertale by Toby Fox and Temmie Chang.   
Undertale Yellow soundtrack composed by MasterSwordRemix, Noteblock, MyNewSoundtrack, and Figburn.

---

**License Sisyphe.io :**

For more information about the licensing of this project, please refer to the badge at the very top of this documentation. Click on said badge to be redirected to the official Creative Commons description of the license.
