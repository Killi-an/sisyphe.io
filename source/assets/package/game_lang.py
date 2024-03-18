# -*- coding: utf-8 -*-

class Traduction:
    def __init__(self):
        self.selection={
            "fr": "Français",
            "en": "English",
            "es": "Español",
            "it": "Italiano",
            "pt": "Português",
            "de": "Deutsch",
            "ru": "Pусский",
            "zh_TW": "繁體中文",
            "zh_CN": "简体中文",
            "jp": "日本語",
            "ko": "한국어",
            "ar": "العربية"
        }
    
    def french(self):
        self.game_name="Sisyphe.io"
        
        # Boutons
        self.play_button="Jouer"
        self.open_button="Ouvrir"
        self.editor_button="Editeur"
        self.credits_button="Crédits"
        self.leave_button="Quitter"
        
        self.reset_button="Réinitialiser"
        self.back_button="Retour"
        self.popup_close_button="Fermer"
        
        # Tutoriels
        self.w1_tutorial_1="Bienvenue dans Sisyphe.io !\n\nDans ce jeu, vous devez pousser tous les rochers dans les trous correspondants pour progresser ! (Défilez pour voir +)\n\nVotre score dépend de votre nombre de déplacements, alors essayez d'optimiser vos parties !\n\nSi vous souhaitez recommencer un niveau, appuyez sur "
        self.w1_tutorial_2=",\nSi vous souhaitez revenir au menu principal, appuyez sur "
        
        self.w2_tutorial="Vous voici dans le Monde 2 !\n\nDans ce monde, vous pouvez rencontrer 2 nouveaux types de blocs : un portail bleu ainsi qu'un portail rouge. (Défilez pour voir +)\n\nPour avancer, il vous faudra les emprunter afin de vous téléporter de l'un à l'autre !"
        
        self.w3_tutorial_1="En avant vers le Monde 3 !\n\nDans ce monde, vous pouvez ramasser des cordes afin de tirer un rocher vers vous à l'aide de la touche "
        self.w3_tutorial_2=" ! (Défilez pour voir +)\n\nPour changer l'orientation de votre personnage sans vous déplacer afin de tirer un rocher, vous pouvez appuyer sur les touches [ CTRL/MAJ + TOUCHES DIRECTIONNELLES ].\n\nVous allez également rencontrer des caisses qui bloqueront votre progression, mais pas de panique :\n\nleur fonctionnement est similaire à celui des rochers, à l'exception qu'il est impossible de les bouger sans l'aide d'une corde et qu'il ne faut pas les amener dans des trous !"
        
        self.w4_tutorial="Monde 4, nous voilà !\n\nDans ce monde, vous devrez ouvrir les portes vertes afin d'avancer. (Défilez pour voir +)\n\nComment ? En poussant un rocher sur les plaques de pression vertes que vous rencontrerez !\n\nAttention : Lorsque les portes se referment, elles écrasent tout objet se situant sur la même case, vous obligeant à recommencer le niveau."
        
        self.w5_tutorial="Le monde 5 vous attend !\n\nDans ce monde, des marteaux peuvent apparaître sur le plateau. (Défilez pour voir +)\n\nLes ramasser vous permettra de casser jusqu'à 3 murs fragilisés en utilisant la touche "
        
        # Autre
        self.world="Monde "
        self.reset_save_confirm="Voulez-vous réellement réinitialiser votre progression ?"
        self.error="Erreur"
        self.error_opening="Erreur dans l'ouverture du fichier."
        self.corrupted="Erreur dans l'ouverture du fichier. Celui-ci est peut-être corrompu ou n'est pas un niveau compatible avec Sisyphe.io !"
        self.reset_lang_confirm="Voulez-vous réellement réinitialiser vos paramètres ?"
        self.open_file="Ouvrir un fichier"
        self.confirm="Confirmation"
        self.no_access_title="Accès refusé"
        self.no_access="Veuillez terminer le Monde 1 avant d'accéder à l'éditeur de niveaux et aux niveaux personnalisés !"
        self.rpc_download = "Télécharger"
        self.rpc_menu = "En train de jouer"
        
        # DB
        self.no_score= "Aucun score enregistré"
        self.best_score_1="Meilleur score : "
        self.best_score_2=" le "
        self.best_score_3=" à "
        self.best_score_4=""
        
        # Menu Paramètres
        self.up="Haut : "
        self.left="Gauche : "
        self.down="Bas : "
        self.right="Droite : "
        
        self.music="Musique : "
        self.fps="FPS : "
        self.sounds="Sons : "
        self.interact="Interagir : "
        self.restart="Rejouer : "
        self.menu="Menu : "
        self.language="Langue : "
        self.settings="Paramètres"
        
        self.fps_show="Montrer"
        self.fps_hide="Cacher"
        
        # Gameplay
        self.end="FIN"
        self.score="Score : "
        self.next_level="Niveau Suivant : "
        self.level="Niveau : "
        self.moves="Déplacements : "
        self.time="Temps : "
        
        self.congrats_1="Bravo,"
        self.congrats_2="Tu as terminé le monde "
        self.congrats_3=" !"
        
        # Editeur
        self.editor_title="Sisyphe.io - Editeur de Niveaux"
        self.editor_new_file="Sans titre"
        self.unsaved_title="Modifications non-enregistrées"
        self.unsaved="Vous avez peut-être des modifications non-enregistrées, voulez vous tout de même quitter ?"
        
        self.error_player="Aucun joueur placé sur le plateau de jeu."
        self.error_boulder="Aucun rocher ou aucun trou placé sur le plateau de jeu, ou il n'y a pas assez de rochers pour combler tous les trous."
        self.error_portal="Un portail est placé sur le plateau de jeu sans sa paire."
        self.error_door="Une porte est placée sur le plateau de jeu sans plaque de pression, ou vice-versa."
        self.error_not_valid="Le niveau que vous essayez d'enregistrer n'est pas valide : "
        
        self.file_menu="Fichier"
        self.edition_menu="Edition"
        self.textures_menu="Textures"
        self.music_menu="Musique & Sons"
        
        self.new_button="Nouveau"
        self.save_button="Enregistrer"
        self.save_as_button="Enregistrer sous..."
        self.toggle_textures_button="Activer/Désactiver les textures"
        self.toggle_music_button="Activer/Désactiver la musique"
        self.toggle_sounds_button="Activer/Désactiver les sons"
        
        self.base_objects="Objets de Base"
        self.special_objects="Objets Spéciaux"
        
        self.select_wall="Sélectionner l'objet Mur"
        self.select_boulder="Sélectionner l'objet Rocher"
        self.select_hole="Sélectionner l'objet Trou"
        self.select_box="Sélectionner l'objet Caisse"
        self.select_player="Sélectionner l'objet Sisyphe"
        self.select_portal1="Sélectionner l'objet Portail Bleu"
        self.select_portal2="Sélectionner l'objet Portail Rouge"
        self.select_door="Sélectionner l'objet Porte"
        self.select_pressure_plate="Sélectionner l'objet Plaque de pression"
        self.select_cracked_wall="Sélectionner l'objet Mur Fragile"
        self.select_hammer="Sélectionner l'objet Marteau"
        self.select_rope="Sélectionner l'objet Corde"
        self.delete_mode="Mode Suppression"
        
        self.return_key="Retour Arrière"
        
        self.editor_tutorial_title="Tutoriel - Éditeur de niveaux"
        self.editor_tutorial="Bienvenue dans l'éditeur de niveaux !\n\nIci, vous pouvez sélectionner l'objet de votre choix dans le menu Editeur.\n\nVous pouvez également créer, charger et sauvegarder votre niveau avec le menu Fichier.\n\nPour afficher/cacher les textures du jeu, utilisez le menu Textures.\n\nAprès en avoir terminé avec l'éditeur, vous pouvez utiliser le bouton Ouvrir dans le menu principal afin de sélectionner votre niveau !"

    def english(self):
        self.game_name="Sisyphe.io"
        
        # Buttons
        self.play_button="Play"
        self.open_button="Open"
        self.editor_button="Editor"
        self.credits_button="Credits"
        self.leave_button="Quit"
        
        self.reset_button="Reset"
        self.back_button="Go Back"
        self.popup_close_button="Dismiss"
        
        # Tutorials
        self.w1_tutorial_1="Welcome to Sisyphe.io !\n\nIn this game, you need to bring all the boulders into the corresponding holes to push forward! (Scroll for more)\n\nYour score heavily depends on your move count, so try to optimise your gameplay!\n\nIf you wish to restart a level, tap "
        self.w1_tutorial_2=",\nIf you wish to go back to the main menu, tap "
        
        self.w2_tutorial="You are now in world 2!\n\nIn this world, you can find 2 new bloc types: a blue portal and a red portal. (Scroll for more)\n\nTo push forward, you will need to go through one of them to be teleported to the other one!"

        self.w3_tutorial_1="Let's head into world 3!\n\nIn this world, you can pick up ropes to pull a boulder towards you by tapping "
        self.w3_tutorial_2=" ! (Scroll for more)\n\nTo change the direction in which your character is facing, you can use [ CTRL/SHIFT + DIRECTIONAL KEYS ].\n\nSome boxes might also get in your way, but no need to worry:\n\nthey function similarly to the boulders, except for the fact that you can only move them with a rope, and you don't need to bring them anywhere!"        
        self.w4_tutorial="World 4, here we are!\n\nIn this world, You will need to open a set of doors to push forward. (Scroll for more)\n\nHow? By pushing a boulder onto the corresponding green pressure plates!\n\nWarning: The doors will crush anything that's underneath when you close them, including the boulders which might force you to restart the current level."
        
        self.w5_tutorial="World 5 awaits you!\n\nIn this world, hammers can spawn on the game board. (Scroll for more)\n\nPicking them up will allow you to break up to 3 cracked walls by tapping "
        
        # Other
        self.world="World "
        self.reset_save_confirm="Do you really wish to reset your progress?"
        self.error="Error"
        self.error_opening="An error occured while trying to open your file."
        self.corrupted="An error occured while trying to open your file. You level might be corrupted or incompatible with Sisyphe.io!"
        self.reset_lang_confirm="Do you really wish to reset your settings?"
        self.open_file="Open File"
        self.confirm="Confirmation"
        self.no_access_title = "Access Denied"
        self.no_access = "Please complete World 1 before accessing the level editor and custom levels!"
        self.rpc_download = "Download"
        self.rpc_menu = "Playing"
        
        # DB
        self.no_score= "No scores recorded"
        self.best_score_1="Best score: "
        self.best_score_2=" on "
        self.best_score_3=" at "
        self.best_score_4=""

        
        # Settings Menu
        self.up="Up: "
        self.left="Left: "
        self.down="Down: "
        self.right="Right: "
        
        self.music="Music: "
        self.fps="FPS: "
        self.sounds="Sounds: "
        self.interact="Interact: "
        self.restart="Restart: "
        self.menu="Menu: "
        self.language="Language: "
        self.settings="Settings"
        
        self.fps_show="Show"
        self.fps_hide="Hide"

        # Gameplay
        self.end="END"
        self.score="Score: "
        self.next_level="Next Level: "
        self.level="Level: "
        self.moves="Move Count: "
        self.time="Timer: "
        
        self.congrats_1="Congratulations,"
        self.congrats_2="You have completed "
        self.congrats_3="!"
        
        # Editor
        self.editor_title="Sisyphe.io - Level Editor"
        self.editor_new_file = "Untitled"
        self.unsaved_title = "Unsaved Changes"
        self.unsaved = "You may have unsaved changes. Do you still wish to exit?"
        
        self.error_player = "No player placed on the game board."
        self.error_boulder = "No boulder or hole placed on the game board, or there are not enough boulders to fill all the holes."
        self.error_portal = "A portal is placed on the game board without its pair."
        self.error_door = "A door is placed on the game board without a pressure plate, or vice versa."
        self.error_not_valid = "The level you are trying to save is not valid: "
        
        self.file_menu = "File"
        self.edition_menu = "Edit"
        self.textures_menu = "Textures"
        self.music_menu = "Music & Sounds"
        
        self.new_button = "New"
        self.save_button = "Save"
        self.save_as_button = "Save As..."
        self.toggle_textures_button = "Toggle Textures"
        self.toggle_music_button = "Toggle Music"
        self.toggle_sounds_button = "Toggle Sounds"
        
        self.base_objects = "Basic Objects"
        self.special_objects = "Special Objects"
        
        self.select_wall = "Select Wall object"
        self.select_boulder = "Select Boulder object"
        self.select_hole = "Select Hole object"
        self.select_box = "Select Box object"
        self.select_player = "Select Sisyphe object"
        self.select_portal1 = "Select Blue Portal object"
        self.select_portal2 = "Select Red Portal object"
        self.select_door = "Select Door object"
        self.select_pressure_plate = "Select Pressure Plate object"
        self.select_cracked_wall = "Select Cracked Wall object"
        self.select_hammer = "Select Hammer object"
        self.select_rope = "Select Rope object"
        self.delete_mode = "Deletion Mode"
        
        self.return_key = "Backspace"
        
        self.editor_tutorial_title = "Tutorial - Level Editor"
        self.editor_tutorial = "Welcome to the level editor!\n\nHere, you can select the object of your choice from the Edit menu.\n\nYou can also create, load, and save your level using the File menu.\n\nTo show/hide the game textures, use the Textures menu.\n\nAfter finishing with the editor, you can use the Open button in the main menu to select your level!"
        
    def spanish(self):
        self.game_name="Sisyphe.io"
        
        # Botones
        self.play_button = "Jugar"
        self.open_button = "Abrir"
        self.editor_button = "Editor"
        self.credits_button = "Créditos"
        self.leave_button = "Salir"
        
        self.reset_button = "Reiniciar"
        self.back_button = "Volver"
        self.popup_close_button = "Cerrar"
        
        # Tutoriales
        self.w1_tutorial_1 = "¡Bienvenido a Sisyphe.io!\n\nEn este juego, debes llevar todas las rocas a los agujeros correspondientes para avanzar. (Desplázate para más información)\n\nTu puntuación depende en gran medida de la cantidad de movimientos, ¡así que intenta optimizar tu juego!\n\nSi deseas reiniciar un nivel, toca "
        self.w1_tutorial_2 = ", si deseas volver al menú principal, toca "
        
        self.w2_tutorial = "¡Ahora estás en el mundo 2!\n\nEn este mundo, encontrarás 2 nuevos tipos de bloques: un portal azul y un portal rojo. (Desplázate para más información)\n\n¡Para avanzar, deberás pasar por uno de ellos para ser teletransportado al otro!"
        
        self.w3_tutorial_1 = "¡Vamos al mundo 3!\n\nEn este mundo, puedes recoger cuerdas para tirar de una roca hacia ti tocando "
        self.w3_tutorial_2 = " ¡(Desplázate para más información)\n\nPara cambiar la dirección en la que tu personaje está mirando, puedes usar [CTRL/MAYÚS + TECLAS DIRECCIONALES].\n\nAlgunas cajas también pueden estar en tu camino, pero no te preocupes:\n\nfuncionan de manera similar a las rocas, excepto que solo puedes moverlas con una cuerda, y no necesitas llevarlas a ningún lado."
        
        self.w4_tutorial = "¡Mundo 4, aquí estamos!\n\nEn este mundo, deberás abrir un conjunto de puertas para avanzar. (Desplázate para más información)\n\n¿Cómo? ¡Empujando una roca sobre las placas de presión verdes correspondientes!\n\nAdvertencia: Las puertas aplastarán todo lo que esté debajo cuando las cierres, incluidas las rocas que podrían obligarte a reiniciar el nivel actual."
        
        self.w5_tutorial = "¡El mundo 5 te espera!\n\nEn este mundo, martillos pueden aparecer en el tablero de juego. (Desplázate para más información)\n\nRecogerlos te permitirá romper hasta 3 paredes agrietadas tocando "
        
        # Otro
        self.world = "Mundo "
        self.reset_save_confirm = "¿Realmente deseas reiniciar tu progreso?"
        self.error = "Error"
        self.error_opening = "Se produjo un error al intentar abrir tu archivo."
        self.corrupted = "Se produjo un error al intentar abrir tu archivo. ¡Tu nivel podría estar corrupto o ser incompatible con Sisyphe.io!"
        self.reset_lang_confirm = "¿Realmente deseas restablecer tus opciones?"
        self.open_file = "Abrir Archivo"
        self.confirm = "Confirmación"
        self.no_access_title = "Acceso denegado"
        self.no_access = "¡Por favor, completa el Mundo 1 antes de acceder al editor de niveles y niveles personalizados!"
        self.rpc_download = "Descargar"
        self.rpc_menu = "Jugando"
        
        # DB
        self.no_score= "Ningún puntaje registrado"
        self.best_score_1="Mejor puntaje: "
        self.best_score_2=" el "
        self.best_score_3=" a las "
        self.best_score_4=""
        
        # Menú de Configuración
        self.up = "Arriba: "
        self.left = "Izquierda: "
        self.down = "Abajo: "
        self.right = "Derecha: "
        
        self.music = "Música: "
        self.fps = "FPS: "
        self.sounds = "Sonidos: "
        self.interact = "Interactuar: "
        self.restart = "Reiniciar: "
        self.menu = "Menú: "
        self.language="Idioma: "
        self.settings = "Opciones"
        
        self.fps_show = "Mostrar"
        self.fps_hide = "Ocultar"
    
        # Jugabilidad
        self.end = "FIN"
        self.score = "Puntuación: "
        self.next_level = "Próximo Nivel: "
        self.level = "Nivel: "
        self.moves = "Conteo de Movimientos: "
        self.time = "Temporizador: "
        
        self.congrats_1 = "¡Felicidades,"
        self.congrats_2 = "Has completado "
        self.congrats_3 = "!"
        
        # Editor
        self.editor_title="Sisyphe.io - Editor de Niveles"
        self.editor_new_file = "Sin título"
        self.unsaved_title = "Cambios no guardados"
        self.unsaved = "Puede que tengas cambios no guardados. ¿Aún deseas salir?"
        
        self.error_player = "Ningún jugador colocado en el tablero de juego."
        self.error_boulder = "Ninguna roca o agujero colocados en el tablero de juego, o no hay suficientes rocas para llenar todos los agujeros."
        self.error_portal = "Se colocó un portal en el tablero de juego sin su pareja."
        self.error_door = "Se colocó una puerta en el tablero de juego sin una placa de presión, o viceversa."
        self.error_not_valid = "El nivel que estás intentando guardar no es válido: "
        
        self.file_menu = "Archivo"
        self.edition_menu = "Edición"
        self.textures_menu = "Texturas"
        self.music_menu = "Música y Sonidos"
        
        self.new_button = "Nuevo"
        self.save_button = "Guardar"
        self.save_as_button = "Guardar Como..."
        self.toggle_textures_button = "Activar/Desactivar Texturas"
        self.toggle_music_button = "Activar/Desactivar Música"
        self.toggle_sounds_button = "Activar/Desactivar Sonidos"
        
        self.base_objects = "Objetos Básicos"
        self.special_objects = "Objetos Especiales"
        
        self.select_wall = "Seleccionar objeto Pared"
        self.select_boulder = "Seleccionar objeto Roca"
        self.select_hole = "Seleccionar objeto Agujero"
        self.select_box = "Seleccionar objeto Caja"
        self.select_player = "Seleccionar objeto Sisyphe"
        self.select_portal1 = "Seleccionar objeto Portal Azul"
        self.select_portal2 = "Seleccionar objeto Portal Rojo"
        self.select_door = "Seleccionar objeto Puerta"
        self.select_pressure_plate = "Seleccionar objeto Placa de Presión"
        self.select_cracked_wall = "Seleccionar objeto Pared Agrietada"
        self.select_hammer = "Seleccionar objeto Martillo"
        self.select_rope = "Seleccionar objeto Cuerda"
        self.delete_mode = "Modo Eliminación"
        
        self.return_key = "Retroceso"
        
        self.editor_tutorial_title = "Tutorial - Editor de Niveles"
        self.editor_tutorial = "¡Bienvenido al editor de niveles!\n\nAquí puedes seleccionar el objeto que desees en el menú Editar.\n\nTambién puedes crear, cargar y guardar tu nivel con el menú Archivo.\n\nPara mostrar/ocultar las texturas del juego, usa el menú Texturas.\n\nDespués de terminar con el editor, puedes usar el botón Abrir en el menú principal para seleccionar tu nivel!"
    
    
    def italian(self):
        self.game_name = "Sisyphe.io"
        
        # Pulsanti
        self.play_button = "Gioca"
        self.open_button = "Apri"
        self.editor_button = "Editor"
        self.credits_button = "Crediti"
        self.leave_button = "Esci"
        
        self.reset_button = "Ripristina"
        self.back_button = "Indietro"
        self.popup_close_button = "Chiudi"
        
        # Tutorial
        self.w1_tutorial_1 = "Benvenuto in Sisyphe.io!\n\nIn questo gioco, devi portare tutti i massi nei buchi corrispondenti per avanzare! (Scorri per ulteriori dettagli)\n\nIl tuo punteggio dipende pesantemente dal numero di mosse, quindi cerca di ottimizzare il tuo gameplay!\n\nSe desideri riavviare un livello, tocca "
        self.w1_tutorial_2 = ",\nSe desideri tornare al menu principale, tocca "
        
        self.w2_tutorial = "Sei ora nel mondo 2!\n\nIn questo mondo, troverai 2 nuovi tipi di blocchi: un portale blu e un portale rosso. (Scorri per ulteriori dettagli)\n\nPer avanzare, dovrai attraversarne uno per essere teletrasportato all'altro!"
    
        self.w3_tutorial_1 = "Dirigiamoci nel mondo 3!\n\nIn questo mondo, puoi raccogliere corde per tirare un masso verso di te toccando "
        self.w3_tutorial_2 = " ! (Scorri per ulteriori dettagli)\n\nPer cambiare la direzione in cui il tuo personaggio è rivolto, puoi usare [ CTRL/SHIFT + TASTI DIREZIONALI ].\n\nAlcune casse potrebbero ostacolarti, ma non preoccuparti:\n\nfunzionano in modo simile ai massi, tranne per il fatto che puoi spostarli solo con una corda, e non è necessario portarli da nessuna parte!"
        
        self.w4_tutorial = "Mondo 4, eccoci qua!\n\nIn questo mondo, dovrai aprire un insieme di porte per avanzare. (Scorri per ulteriori dettagli)\n\nCome? Spostando un masso sulla corrispondente lastra verde di pressione!\n\nAttenzione: Le porte schiacciano qualsiasi cosa ci sia sotto quando si chiudono, compresi i massi, il che potrebbe costringerti a riavviare il livello corrente."
        
        self.w5_tutorial = "Il mondo 5 ti aspetta!\n\nIn questo mondo, possono apparire martelli sulla plancia di gioco. (Scorri per ulteriori dettagli)\n\nRaccoglierli ti permetterà di rompere fino a 3 muri crepate toccando "
        
        # Altro
        self.world = "Mondo "
        self.reset_save_confirm = "Vuoi davvero ripristinare il tuo progresso?"
        self.error = "Errore"
        self.error_opening = "Si è verificato un errore durante il tentativo di aprire il tuo file."
        self.corrupted = "Si è verificato un errore durante il tentativo di aprire il tuo file. Il tuo livello potrebbe essere corrotto o incompatibile con Sisyphe.io!"
        self.reset_lang_confirm = "Vuoi davvero ripristinare le tue impostazioni?"
        self.open_file = "Apri file"
        self.confirm = "Conferma"
        self.no_access_title = "Accesso negato"
        self.no_access = "Completa il Mondo 1 prima di accedere all'editor di livelli e ai livelli personalizzati!"
        self.rpc_download = "Scarica"
        self.rpc_menu = "Giocando"
        
        # DB
        self.no_score= "Nessun punteggio registrato"
        self.best_score_1="Miglior punteggio: "
        self.best_score_2=" il "
        self.best_score_3=" alle "
        self.best_score_4=""

        # Menu Impostazioni
        self.up = "Su: "
        self.left = "Sinistra: "
        self.down = "Giù: "
        self.right = "Destra: "
        
        self.music = "Musica: "
        self.fps = "FPS: "
        self.sounds = "Suoni: "
        self.interact = "Interagisci: "
        self.restart = "Riavvia: "
        self.menu = "Menu: "
        self.language = "Lingua: "
        self.settings = "Impostazioni"
        
        self.fps_show = "Mostra"
        self.fps_hide = "Nasc."
    
        # Gioco
        self.end = "FINE"
        self.score = "Punteggio: "
        self.next_level = "Prossimo Livello: "
        self.level = "Livello: "
        self.moves = "Conteggio Mosse: "
        self.time = "Timer: "
        
        self.congrats_1 = "Congratulazioni,"
        self.congrats_2 = "Hai completato "
        self.congrats_3 = "!"
    
        # Editor
        self.editor_title = "Sisyphe.io - Editor di livelli"
        self.editor_new_file = "Senza titolo"
        self.unsaved_title = "Modifiche non salvate"
        self.unsaved = "Potresti avere delle modifiche non salvate. Vuoi comunque uscire?"
        
        self.error_player = "Nessun giocatore posizionato sulla plancia di gioco."
        self.error_boulder = "Nessun masso o buco posizionato sulla plancia di gioco, o non ci sono abbastanza massi per riempire tutti i buchi."
        self.error_portal = "Un portale è posizionato sulla plancia di gioco senza la sua coppia."
        self.error_door = "Una porta è posizionata sulla plancia di gioco senza una lastra di pressione, o viceversa."
        self.error_not_valid = "Il livello che stai cercando di salvare non è valido: "
        
        self.file_menu = "File"
        self.edition_menu = "Modifica"
        self.textures_menu = "Texture"
        self.music_menu = "Musica e Suoni"
        
        self.new_button = "Nuovo"
        self.save_button = "Salva"
        self.save_as_button = "Salva con nome..."
        self.toggle_textures_button = "Attiva/Disattiva le texture"
        self.toggle_music_button = "Attiva/Disattiva la musica"
        self.toggle_sounds_button = "Attiva/Disattiva i suoni"
        
        self.base_objects = "Oggetti di Base"
        self.special_objects = "Oggetti Speciali"
        
        self.select_wall = "Seleziona oggetto Muro"
        self.select_boulder = "Seleziona oggetto Masso"
        self.select_hole = "Seleziona oggetto Buco"
        self.select_box = "Seleziona oggetto Scatola"
        self.select_player = "Seleziona oggetto Sisyphe"
        self.select_portal1 = "Seleziona oggetto Portale Blu"
        self.select_portal2 = "Seleziona oggetto Portale Rosso"
        self.select_door = "Seleziona oggetto Porta"
        self.select_pressure_plate = "Seleziona oggetto Lastra di Pressione"
        self.select_cracked_wall = "Seleziona oggetto Muro Crepato"
        self.select_hammer = "Seleziona oggetto Martello"
        self.select_rope = "Seleziona oggetto Corda"
        self.delete_mode = "Modalità Eliminazione"
        
        self.return_key = "Backspace"
        
        self.editor_tutorial_title = "Tutorial - Editor di Livelli"
        self.editor_tutorial = "Benvenuto nell'editor di livelli!\n\nQui, puoi selezionare l'oggetto che preferisci dal menu Modifica.\n\nPuoi anche creare, caricare e salvare il tuo livello usando il menu File.\n\nPer mostrare/nascondere le texture di gioco, usa il menu Texture.\n\nDopo aver finito con l'editor, puoi usare il pulsante Apri nel menu principale per selezionare il tuo livello!"

    def portuguese(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "Jogar"
        self.open_button = "Abrir"
        self.editor_button = "Editor"
        self.credits_button = "Créditos"
        self.leave_button = "Sair"
        
        self.reset_button = "Resetar"
        self.back_button = "Voltar"
        self.popup_close_button = "Fechar"
        
        # Tutorials
        self.w1_tutorial_1 = "Bem-vindo ao Sisyphe.io!\n\nNeste jogo, você precisa levar todas as pedras para os buracos correspondentes para avançar! (Role para mais)\n\nSua pontuação depende muito do número de movimentos, então tente otimizar seu gameplay!\n\nSe deseja reiniciar um nível, toque em "
        self.w1_tutorial_2 = ",\nSe deseja voltar ao menu principal, toque em "
        
        self.w2_tutorial = "Agora você está no mundo 2!\n\nNeste mundo, você encontrará 2 novos tipos de blocos: um portal azul e um portal vermelho. (Role para mais)\n\nPara avançar, você precisará passar por um deles para ser teleportado para o outro!"
    
        self.w3_tutorial_1 = "Vamos para o mundo 3!\n\nNeste mundo, você pode pegar cordas para puxar uma pedra em sua direção tocando "
        self.w3_tutorial_2 = " ! (Role para mais)\n\nPara mudar a direção em que seu personagem está enfrentando, você pode usar [ CTRL/SHIFT + TECLAS DIRECIONAIS ].\n\nAlgumas caixas também podem ficar no seu caminho, mas não se preocupe:\n\nelas funcionam de maneira semelhante às pedras, exceto pelo fato de que você só pode movê-las com uma corda e não precisa levá-las a lugar nenhum!"        
        self.w4_tutorial = "Mundo 4, aqui estamos!\n\nNeste mundo, você precisará abrir um conjunto de portas para avançar. (Role para mais)\n\nComo? Empurrando uma pedra sobre as placas de pressão verdes correspondentes!\n\nAviso: As portas esmagarão qualquer coisa que estiver embaixo quando você as fechar, incluindo as pedras, o que pode forçá-lo a reiniciar o nível atual."
        
        self.w5_tutorial = "O Mundo 5 o aguarda!\n\nNeste mundo, martelos podem aparecer no tabuleiro. (Role para mais)\n\nPegá-los permitirá que você quebre até 3 paredes rachadas tocando "
        
        # Other
        self.world = "Mundo "
        self.reset_save_confirm = "Você realmente deseja redefinir seu progresso?"
        self.error = "Erro"
        self.error_opening = "Ocorreu um erro ao tentar abrir seu arquivo."
        self.corrupted = "Ocorreu um erro ao tentar abrir seu arquivo. Seu nível pode estar corrompido ou incompatível com o Sisyphe.io!"
        self.reset_lang_confirm = "Você realmente deseja redefinir suas configurações?"
        self.open_file = "Abrir Arquivo"
        self.confirm = "Confirmação"
        self.no_access_title = "Acesso Negado"
        self.no_access = "Por favor, complete o Mundo 1 antes de acessar o editor de níveis e níveis personalizados!"
        self.rpc_download = "Baixar"
        self.rpc_menu = "Jogando"
        
        # DB
        self.no_score= "Nenhum score registrado"
        self.best_score_1="Melhor score: "
        self.best_score_2=" em "
        self.best_score_3=" às "
        self.best_score_4=""

        # Settings Menu
        self.up = "Cima: "
        self.left = "Esquerda: "
        self.down = "Baixo: "
        self.right = "Direita: "
        
        self.music = "Música: "
        self.fps = "FPS: "
        self.sounds = "Sons: "
        self.interact = "Interagir: "
        self.restart = "Reiniciar: "
        self.menu = "Menu: "
        self.language = "Idioma: "
        self.settings = "Opções"
        
        self.fps_show = "Mostrar"
        self.fps_hide = "Ocultar"
    
        # Gameplay
        self.end = "FIM"
        self.score = "Pontuação: "
        self.next_level = "Próximo Nível: "
        self.level = "Nível: "
        self.moves = "Contagem de Movimentos: "
        self.time = "Tempo: "
        
        self.congrats_1 = "Parabéns,"
        self.congrats_2 = "Você concluiu "
        self.congrats_3 = "!"
        
        # Editor
        self.editor_title = "Sisyphe.io - Editor de Níveis"
        self.editor_new_file = "Sem título"
        self.unsaved_title = "Alterações Não Salvas"
        self.unsaved = "Você pode ter alterações não salvas. Ainda deseja sair?"
        
        self.error_player = "Nenhum jogador colocado no tabuleiro."
        self.error_boulder = "Nenhuma pedra ou buraco colocado no tabuleiro, ou não há pedras suficientes para preencher todos os buracos."
        self.error_portal = "Um portal está colocado no tabuleiro sem o seu par."
        self.error_door = "Uma porta está colocada no tabuleiro sem uma placa de pressão, ou vice-versa."
        self.error_not_valid = "O nível que você está tentando salvar não é válido: "
        
        self.file_menu = "Arquivo"
        self.edition_menu = "Editar"
        self.textures_menu = "Texturas"
        self.music_menu = "Música e Sons"
        
        self.new_button = "Novo"
        self.save_button = "Salvar"
        self.save_as_button = "Salvar Como..."
        self.toggle_textures_button = "Alternar Texturas"
        self.toggle_music_button = "Alternar Música"
        self.toggle_sounds_button = "Alternar Sons"
        
        self.base_objects = "Objetos Básicos"
        self.special_objects = "Objetos Especiais"
        
        self.select_wall = "Selecionar objeto Parede"
        self.select_boulder = "Selecionar objeto Pedra"
        self.select_hole = "Selecionar objeto Buraco"
        self.select_box = "Selecionar objeto Caixa"
        self.select_player = "Selecionar objeto Sisyphe"
        self.select_portal1 = "Selecionar objeto Portal Azul"
        self.select_portal2 = "Selecionar objeto Portal Vermelho"
        self.select_door = "Selecionar objeto Porta"
        self.select_pressure_plate = "Selecionar objeto Placa de Pressão"
        self.select_cracked_wall = "Selecionar objeto Parede Rachada"
        self.select_hammer = "Selecionar objeto Martelo"
        self.select_rope = "Selecionar objeto Corda"
        self.delete_mode = "Modo Exclusão"
        
        self.return_key = "Backspace"
        
        self.editor_tutorial_title = "Tutorial - Editor de Níveis"
        self.editor_tutorial = "Bem-vindo ao editor de níveis!\n\nAqui, você pode selecionar o objeto de sua escolha no menu Editar.\n\nVocê também pode criar, carregar e salvar seu nível usando o menu Arquivo.\n\nPara mostrar/ocultar as texturas do jogo, use o menu Texturas.\n\nDepois de terminar com o editor, você pode usar o botão Abrir no menu principal para selecionar seu nível!"

    def german(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "Spielen"
        self.open_button = "Öffnen"
        self.editor_button = "Editor"
        self.credits_button = "Credits"
        self.leave_button = "Beenden"
        
        self.reset_button = "Zurücksetzen"
        self.back_button = "Zurück"
        self.popup_close_button = "Schließen"
        
        # Tutorials
        self.w1_tutorial_1 = "Willkommen bei Sisyphe.io!\n\nIn diesem Spiel müssen Sie alle Felsen in die entsprechenden Löcher bringen, um voranzukommen! (Scrollen Sie für mehr)\n\nIhre Punktzahl hängt stark von der Anzahl Ihrer Züge ab, also versuchen Sie, Ihr Gameplay zu optimieren!\n\nWenn Sie ein Level neu starten möchten, tippen Sie auf "
        self.w1_tutorial_2 = ",\nWenn Sie zum Hauptmenü zurückkehren möchten, tippen Sie auf "
        
        self.w2_tutorial = "Sie sind jetzt in Welt 2!\n\nIn dieser Welt finden Sie 2 neue Blocktypen: ein blaues Portal und ein rotes Portal. (Scrollen Sie für mehr)\n\nUm voranzukommen, müssen Sie durch eines von ihnen gehen, um zum anderen teleportiert zu werden!"
    
        self.w3_tutorial_1 = "Lassen Sie uns in Welt 3 gehen!\n\nIn dieser Welt können Sie Seile aufnehmen, um einen Felsen zu sich zu ziehen, indem Sie auf "
        self.w3_tutorial_2 = " tippen! (Scrollen Sie für mehr)\n\nUm die Richtung zu ändern, in die Ihr Charakter schaut, können Sie [ STRG/UMSCHALT + PFEILTASTEN ] verwenden.\n\nEinige Kisten könnten Ihnen auch im Weg stehen, aber keine Sorge:\n\nSie funktionieren ähnlich wie die Felsen, mit der Ausnahme, dass Sie sie nur mit einem Seil bewegen können und sie nirgendwohin bringen müssen!"
        self.w4_tutorial = "Welt 4, hier sind wir!\n\nIn dieser Welt müssen Sie eine Reihe von Türen öffnen, um voranzukommen. (Scrollen Sie für mehr)\n\nWie? Indem Sie einen Felsen auf die entsprechenden grünen Druckplatten schieben!\n\nWarnung: Die Türen werden alles zerquetschen, was darunter ist, wenn Sie sie schließen, einschließlich der Felsen, was Sie dazu zwingen könnte, das aktuelle Level neu zu starten."
        
        self.w5_tutorial = "Welt 5 erwartet Sie!\n\nIn dieser Welt können Hämmer auf dem Spielfeld erscheinen. (Scrollen Sie für mehr)\n\nWenn Sie sie aufheben, können Sie bis zu 3 rissige Wände durch Tippen auf "
        
        # Other
        self.world = "Welt "
        self.reset_save_confirm = "Möchten Sie wirklich Ihren Fortschritt zurücksetzen?"
        self.error = "Fehler"
        self.error_opening = "Ein Fehler ist aufgetreten beim Versuch, Ihre Datei zu öffnen."
        self.corrupted = "Ein Fehler ist aufgetreten beim Versuch, Ihre Datei zu öffnen. Ihr Level könnte beschädigt oder mit Sisyphe.io nicht kompatibel sein!"
        self.reset_lang_confirm = "Möchten Sie wirklich Ihre Einstellungen zurücksetzen?"
        self.open_file = "Datei öffnen"
        self.confirm = "Bestätigung"
        self.no_access_title = "Zugriff verweigert"
        self.no_access = "Bitte schließen Sie Welt 1 ab, bevor Sie den Level-Editor und benutzerdefinierte Level verwenden!"
        self.rpc_download = "Herunterladen"
        self.rpc_menu = "Hauptmenü"
        self.rpc_custom = "Benutzerdefiniertes Level"
        self.rpc_download = "Herunterladen"
        self.rpc_menu = "Spielen"
        
        # DB
        self.no_score= "Keine Punkte gespeichert"
        self.best_score_1="Beste Punktzahl: "
        self.best_score_2=" am "
        self.best_score_3=" um "
        self.best_score_4=" Uhr"

        # Settings Menu
        self.up = "Oben: "
        self.left = "Links: "
        self.down = "Unten: "
        self.right = "Rechts: "
        
        self.music = "Musik: "
        self.fps = "FPS: "
        self.sounds = "Geräusche: "
        self.interact = "Interagieren: "
        self.restart = "Neustart: "
        self.menu = "Menü: "
        self.language = "Sprache: "
        self.settings = "Einstellungen"
        
        self.fps_show = "Zeig"
        self.fps_hide = "Verberg"
    
        # Gameplay
        self.end = "ENDE"
        self.score = "Punktzahl: "
        self.next_level = "Nächstes Level: "
        self.level = "Level: "
        self.moves = "Zuganzahl: "
        self.time = "Timer: "
        
        self.congrats_1 = "Herzlichen Glückwunsch,"
        self.congrats_2 = "Sie haben "
        self.congrats_3 = " abgeschlossen!"
        
        # Editor
        self.editor_title = "Sisyphe.io - Level-Editor"
        self.editor_new_file = "Ohne Titel"
        self.unsaved_title = "Ungespeicherte Änderungen"
        self.unsaved = "Es könnten ungespeicherte Änderungen vorliegen. Möchten Sie wirklich beenden?"
        
        self.error_player = "Kein Spieler auf dem Spielfeld platziert."
        self.error_boulder = "Kein Felsen oder Loch auf dem Spielfeld platziert oder es gibt nicht genug Felsen, um alle Löcher zu füllen."
        self.error_portal = "Ein Portal ist auf dem Spielfeld platziert ohne sein Gegenstück."
        self.error_door = "Eine Tür ist auf dem Spielfeld platziert ohne eine Druckplatte oder umgekehrt."
        self.error_not_valid = "Das Level, das Sie zu speichern versuchen, ist nicht gültig: "
        
        self.file_menu = "Datei"
        self.edition_menu = "Bearbeiten"
        self.textures_menu = "Texturen"
        self.music_menu = "Musik & Geräusche"
        
        self.new_button = "Neu"
        self.save_button = "Speichern"
        self.save_as_button = "Speichern unter..."
        self.toggle_textures_button = "Texturen umschalten"
        self.toggle_music_button = "Musik umschalten"
        self.toggle_sounds_button = "Geräusche umschalten"
        
        self.base_objects = "Grundobjekte"
        self.special_objects = "Spezialobjekte"
        
        self.select_wall = "Wandobjekt auswählen"
        self.select_boulder = "Felsenobjekt auswählen"
        self.select_hole = "Lochobjekt auswählen"
        self.select_box = "Kistenobjekt auswählen"
        self.select_player = "Sisyphe-Objekt auswählen"
        self.select_portal1 = "Blaues Portal-Objekt auswählen"
        self.select_portal2 = "Rotes Portal-Objekt auswählen"
        self.select_door = "Tür-Objekt auswählen"
        self.select_pressure_plate = "Druckplattenobjekt auswählen"
        self.select_cracked_wall = "Rissige Wand-Objekt auswählen"
        self.select_hammer = "Hammer-Objekt auswählen"
        self.select_rope = "Seil-Objekt auswählen"
        self.delete_mode = "Löschmodus"
        
        self.return_key = "Backspace"
        
        self.editor_tutorial_title = "Tutorial - Level-Editor"
        self.editor_tutorial = "Willkommen im Level-Editor!\n\nHier können Sie das gewünschte Objekt im Bearbeiten-Menü auswählen.\n\nSie können auch Ihr Level erstellen, laden und speichern über das Datei-Menü.\n\nUm die Spieltexturen ein-/auszublenden, verwenden Sie das Textur-Menü.\n\nNach Abschluss des Editors können Sie die Schaltfläche Öffnen im Hauptmenü verwenden, um Ihr Level auszuwählen!"
        
    def russian(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "Играть"
        self.open_button = "Открыть"
        self.editor_button = "Редактор"
        self.credits_button = "Кредиты"
        self.leave_button = "Выйти"
        
        self.reset_button = "Сброс"
        self.back_button = "Назад"
        self.popup_close_button = "Закрыть"
        
        # Tutorials
        self.w1_tutorial_1 = "Добро пожаловать в Sisyphe.io!\n\nВ этой игре вам нужно переместить все валуны в соответствующие отверстия, чтобы продвигаться вперед! (Прокрутите для получения дополнительной информации)\n\nВаш счет сильно зависит от количества ваших ходов, поэтому попробуйте оптимизировать свою игру!\n\nЕсли вы хотите перезапустить уровень, коснитесь "
        self.w1_tutorial_2 = ",\nЕсли вы хотите вернуться в главное меню, коснитесь "
        
        self.w2_tutorial = "Теперь вы в мире 2!\n\nВ этом мире вы найдете 2 новых типа блоков: синий портал и красный портал. (Прокрутите для получения дополнительной информации)\n\nЧтобы продвинуться вперед, вам нужно пройти через один из них, чтобы быть телепортированным в другой!"
    
        self.w3_tutorial_1 = "Давайте отправимся в мир 3!\n\nВ этом мире вы можете подбирать веревки, чтобы тащить валун к себе, коснувшись "
        self.w3_tutorial_2 = " ! (Прокрутите для получения дополнительной информации)\n\nЧтобы изменить направление, в котором смотрит ваш персонаж, вы можете использовать [ CTRL/SHIFT + КЛАВИШИ НАПРАВЛЕНИЯ ].\n\nНекоторые коробки могут оказаться на вашем пути, но не волнуйтесь:\n\nони работают аналогично валунам, за исключением того, что вы можете перемещать их только с помощью веревки, и вам не нужно их никуда нести!"
        self.w4_tutorial = "Мир 4, вот мы и здесь!\n\nВ этом мире вам нужно открыть ряд дверей, чтобы продвинуться вперед. (Прокрутите для получения дополнительной информации)\n\nКак? Поместив валун на соответствующие зеленые давящие плиты!\n\nПредупреждение: Двери раздавят все, что окажется под ними, когда вы их закроете, включая валуны, что может заставить вас перезапустить текущий уровень."
        
        self.w5_tutorial = "Вас ждет мир 5!\n\nВ этом мире могут появляться молотки на игровом поле. (Прокрутите для получения дополнительной информации)\n\nПодберите их, чтобы разбить до 3 треснутых стен, коснувшись "
        
        # Other
        self.world = "Мир "
        self.reset_save_confirm = "Вы действительно хотите сбросить свой прогресс?"
        self.error = "Ошибка"
        self.error_opening = "Произошла ошибка при попытке открыть ваш файл."
        self.corrupted = "Произошла ошибка при попытке открыть ваш файл. Ваш уровень может быть поврежден или несовместим с Sisyphe.io!"
        self.reset_lang_confirm = "Вы действительно хотите сбросить настройки?"
        self.open_file = "Открыть файл"
        self.confirm = "Подтверждение"
        self.no_access_title = "Доступ запрещен"
        self.no_access = "Пожалуйста, завершите Мир 1, прежде чем получить доступ к редактору уровней и пользовательским уровням!"
        self.rpc_download = "Скачать"
        self.rpc_menu = "Главное меню"
        self.rpc_custom = "Пользовательский уровень"
        self.rpc_download = "Скачать"
        self.rpc_menu = "Играет"
        
        # DB
        self.no_score= "Нет записанных очков"
        self.best_score_1="Лучший результат: "
        self.best_score_2=" "
        self.best_score_3=" в "
        self.best_score_4=""

        # Settings Menu
        self.up = "Вверх: "
        self.left = "Влево: "
        self.down = "Вниз: "
        self.right = "Вправо: "
        
        self.music = "Музыка: "
        self.fps = "FPS: "
        self.sounds = "Звуки: "
        self.interact = "Взаимодействие: "
        self.restart = "Перезапуск: "
        self.menu = "Меню: "
        self.language = "Язык: "
        self.settings = "Настройки"
        
        self.fps_show = "шоу"
        self.fps_hide = "Скрыть"
    
        # Gameplay
        self.end = "КОНЕЦ"
        self.score = "Очки: "
        self.next_level = "Следующий уровень: "
        self.level = "Уровень: "
        self.moves = "Количество ходов: "
        self.time = "Таймер: "
        
        self.congrats_1 = "Поздравляем,"
        self.congrats_2 = "Вы завершили "
        self.congrats_3 = "!"
        
        # Editor
        self.editor_title = "Sisyphe.io - Редактор уровней"
        self.editor_new_file = "Без названия"
        self.unsaved_title = "Не сохраненные изменения"
        self.unsaved = "У вас могут быть несохраненные изменения. Вы все равно хотите выйти?"
        
        self.error_player = "Нет игрока на игровом поле."
        self.error_boulder = "На игровом поле нет валуна или отверстия, или их недостаточно, чтобы заполнить все отверстия."
        self.error_portal = "Портал размещен на игровом поле без своей пары."
        self.error_door = "Дверь установлена на игровом поле без давящей плиты, или наоборот."
        self.error_not_valid = "Уровень, который вы пытаетесь сохранить, недопустим: "
        
        self.file_menu = "Файл"
        self.edition_menu = "Правка"
        self.textures_menu = "Текстуры"
        self.music_menu = "Музыка и звуки"
        
        self.new_button = "Новый"
        self.save_button = "Сохранить"
        self.save_as_button = "Сохранить как..."
        self.toggle_textures_button = "Переключить текстуры"
        self.toggle_music_button = "Переключить музыку"
        self.toggle_sounds_button = "Переключить звуки"
        
        self.base_objects = "Основные объекты"
        self.special_objects = "Специальные объекты"
        
        self.select_wall = "Выбрать объект Стена"
        self.select_boulder = "Выбрать объект Валун"
        self.select_hole = "Выбрать объект Отверстие"
        self.select_box = "Выбрать объект Коробка"
        self.select_player = "Выбрать объект Sisyphe"
        self.select_portal1 = "Выбрать объект Синий портал"
        self.select_portal2 = "Выбрать объект Красный портал"
        self.select_door = "Выбрать объект Дверь"
        self.select_pressure_plate = "Выбрать объект Давящая плита"
        self.select_cracked_wall = "Выбрать объект Треснутая стена"
        self.select_hammer = "Выбрать объект Молоток"
        self.select_rope = "Выбрать объект Веревка"
        self.delete_mode = "Режим удаления"
        
        self.return_key = "Backspace"
        
        self.editor_tutorial_title = "Обучение - Редактор уровней"
        self.editor_tutorial = "Добро пожаловать в редактор уровней!\n\nЗдесь вы можете выбрать объект по вашему выбору из меню Правка.\n\nВы также можете создавать, загружать и сохранять свой уровень с помощью меню Файл.\n\nЧтобы показать/скрыть игровые текстуры, используйте меню Текстуры.\n\nПо завершении работы с редактором вы можете использовать кнопку Открыть в главном меню, чтобы выбрать свой уровень!"
    
    def chinese_traditional(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "開始遊戲"
        self.open_button = "開啟"
        self.editor_button = "編輯器"
        self.credits_button = "製作人員"
        self.leave_button = "退出"
        
        self.reset_button = "重置"
        self.back_button = "返回"
        self.popup_close_button = "關閉"
        
        # Tutorials
        self.w1_tutorial_1 = "歡迎來到Sisyphe.io！\n\n在這個遊戲中，你需要把所有的巨石移動到相應的洞口以推進！（向下滾動以獲取更多資訊）\n\n你的分數主要取決於你的移動次數，所以儘量優化你的遊戲方式！\n\n如果你想重新開始一個關卡，輕觸 "
        self.w1_tutorial_2 = "，如果你想返回主菜單，輕觸 "
        
        self.w2_tutorial = "你現在進入了第二個世界！\n\n在這個世界中，你可以找到兩種新的區塊類型：藍色傳送門和紅色傳送門。 （向下滾動以獲取更多資訊）\n\n為了推進，你需要通過其中一個傳送門，以被傳送到另一個！"
    
        self.w3_tutorial_1 = "讓我們進入第三個世界！\n\n在這個世界中，你可以通過輕觸 "
        self.w3_tutorial_2 = " 來拾取繩索，將一個巨石拉向你！（向下滾動以獲取更多資訊）\n\n要改變你的角色面朝的方向，你可以使用 [ CTRL/SHIFT + 方向鍵 ]。\n\n一些箱子可能也會擋住你的路，但不用擔心：\n\n它們的功能與巨石相似，只不過你只能用繩索移動它們，而且你不需要將它們帶到任何地方！"
        self.w4_tutorial = "第四個世界，我們來了！\n\n在這個世界中，你需要打開一組門以推進。 （向下滾動以獲取更多資訊）\n\n怎麼做？通過將一個巨石推到相應的綠色壓力板上！\n\n警告：關門時會壓扁所有在下面的東西，包括可能迫使你重新開始當前關卡的巨石。"
        
        self.w5_tutorial = "第五個世界在等著你！\n\n在這個世界中，錘子可以在遊戲板上生成。 （向下滾動以獲取更多資訊）\n\n撿起它們將允許您敲碎最多3堵裂的牆壁，只需輕觸 "
        
        # Other
        self.world = "世界 "
        self.reset_save_confirm = "你真的想重置你的進度嗎？"
        self.error = "錯誤"
        self.error_opening = "在嘗試打開您的文件時發生錯誤。"
        self.corrupted = "在嘗試打開您的文件時發生錯誤。您的級別可能已損壞或與Sisyphe.io不兼容！"
        self.reset_lang_confirm = "您真的要重置您的設置嗎？"
        self.open_file = "打開文件"
        self.confirm = "確認"
        self.no_access_title = "拒絕訪問"
        self.no_access = "在訪問級別編輯器和自定義級別之前，請完成第一世界！"
        self.rpc_download = "下載"
        self.rpc_menu = "遊戲中"
        
        # DB
        self.no_score= "沒有記錄的分數"
        self.best_score_1="最佳分數： "
        self.best_score_2=" 在 "
        self.best_score_3=" 下午 "
        self.best_score_4=""
        
        # Settings Menu
        self.up = "上："
        self.left = "左："
        self.down = "下："
        self.right = "右："
        
        self.music = "音樂："
        self.fps = "FPS："
        self.sounds = "音效："
        self.interact = "交互："
        self.restart = "重新啟動："
        self.menu = "菜單："
        self.language = "語言："
        self.settings = "設置"
        
        self.fps_show = "顯示"
        self.fps_hide = "隱藏"
    
        # Gameplay
        self.end = "結束"
        self.score = "分數："
        self.next_level = "下一級："
        self.level = "級別："
        self.moves = "移動次數："
        self.time = "計時器："
        
        self.congrats_1 = "恭喜，"
        self.congrats_2 = "你已完成 "
        self.congrats_3 = "！"
        
        # Editor
        self.editor_title = "Sisyphe.io - 級別編輯器"
        self.editor_new_file = "無標題"
        self.unsaved_title = "未保存的更改"
        self.unsaved = "您可能有未保存的更改。您是否仍然要退出？"
        
        self.error_player = "未放置玩家在遊戲板上。"
        self.error_boulder = "在遊戲板上未放置巨石或洞口，或者沒有足夠的巨石來填滿所有的洞口。"
        self.error_portal = "在遊戲板上放置了一個傳送門而沒有它的配對物。"
        self.error_door = "在遊戲板上放置了一扇門，沒有壓力板，反之亦然。"
        self.error_not_valid = "您嘗試保存的級別無效："
        
        self.file_menu = "文件"
        self.edition_menu = "編輯"
        self.textures_menu = "紋理"
        self.music_menu = "音樂和音效"
        
        self.new_button = "新建"
        self.save_button = "保存"
        self.save_as_button = "另存為..."
        self.toggle_textures_button = "切換紋理"
        self.toggle_music_button = "切換音樂"
        self.toggle_sounds_button = "切換音效"
        
        self.base_objects = "基本對象"
        self.special_objects = "特殊對象"
        
        self.select_wall = "選擇牆壁對象"
        self.select_boulder = "選擇巨石對象"
        self.select_hole = "選擇洞口對象"
        self.select_box = "選擇箱子對象"
        self.select_player = "選擇Sisyphe對象"
        self.select_portal1 = "選擇藍色傳送門對象"
        self.select_portal2 = "選擇紅色傳送門對象"
        self.select_door = "選擇門對象"
        self.select_pressure_plate = "選擇壓力板對象"
        self.select_cracked_wall = "選擇裂縫牆壁對象"
        self.select_hammer = "選擇錘子對象"
        self.select_rope = "選擇繩索對象"
        self.delete_mode = "刪除模式"
        
        self.return_key = "返回"
        
        self.editor_tutorial_title = "教程 - 級別編輯器"
        self.editor_tutorial = "歡迎來到級別編輯器！\n\n在這裡，您可以從編輯菜單中選擇所需的對象。\n\n您還可以使用文件菜單創建、加載和保存您的級別。\n\n要顯示/隱藏遊戲紋理，請使用紋理菜單。\n\n編輯器完成後，您可以在主菜單中使用打開按鈕選擇您的級別！"
    
    def chinese_simplified(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "开始游戏"
        self.open_button = "打开"
        self.editor_button = "编辑器"
        self.credits_button = "制作人员"
        self.leave_button = "退出"
        
        self.reset_button = "重置"
        self.back_button = "返回"
        self.popup_close_button = "关闭"
        
        # Tutorials
        self.w1_tutorial_1 = "欢迎来到Sisyphe.io！\n\n在这个游戏中，你需要把所有的巨石移动到相应的洞口以推进！（向下滚动以获取更多信息）\n\n你的分数主要取决于你的移动次数，所以尽量优化你的游戏方式！\n\n如果你想重新开始一个关卡，轻触 "
        self.w1_tutorial_2 = "，如果你想返回主菜单，轻触 "
        
        self.w2_tutorial = "你现在进入了第二个世界！\n\n在这个世界中，你可以找到两种新的区块类型：蓝色传送门和红色传送门。 （向下滚动以获取更多信息）\n\n为了推进，你需要通过其中一个传送门，以被传送到另一个！"
    
        self.w3_tutorial_1 = "让我们进入第三个世界！\n\n在这个世界中，你可以通过轻触 "
        self.w3_tutorial_2 = " 来拾取绳索，将一个巨石拉向你！（向下滚动以获取更多信息）\n\n要改变你的角色面朝的方向，你可以使用 [ CTRL/SHIFT + 方向键 ]。\n\n一些箱子可能也会挡住你的路，但不用担心：\n\n它们的功能与巨石相似，只不过你只能用绳索移动它们，而且你不需要将它们带到任何地方！"
        self.w4_tutorial = "第四个世界，我们来了！\n\n在这个世界中，你需要打开一组门以推进。 （向下滚动以获取更多信息）\n\n怎么做？通过将一个巨石推到相应的绿色压力板上！\n\n警告：关门时会压扁所有在下面的东西，包括可能迫使你重新开始当前关卡的巨石。"
        
        self.w5_tutorial = "第五个世界在等着你！\n\n在这个世界中，锤子可以在游戏板上生成。 （向下滚动以获取更多信息）\n\n捡起它们将允许您敲碎最多3堵裂的墙壁，只需轻触 "
        
        # Other
        self.world = "世界 "
        self.reset_save_confirm = "你真的想重置你的进度吗？"
        self.error = "错误"
        self.error_opening = "在尝试打开您的文件时发生错误。"
        self.corrupted = "在尝试打开您的文件时发生错误。您的级别可能已损坏或与Sisyphe.io不兼容！"
        self.reset_lang_confirm = "您真的要重置您的设置吗？"
        self.open_file = "打开文件"
        self.confirm = "确认"
        self.no_access_title = "拒绝访问"
        self.no_access = "在访问级别编辑器和自定义级别之前，请完成第一世界！"
        self.rpc_download = "下载"
        self.rpc_menu = "游戏中"
        
        # DB
        self.no_score= "没有记录的分数"
        self.best_score_1="最佳分数： "
        self.best_score_2=" 在 "
        self.best_score_3=" 下午 "
        self.best_score_4=""
        
        # Settings Menu
        self.up = "上："
        self.left = "左："
        self.down = "下："
        self.right = "右："
        
        self.music = "音乐："
        self.fps = "FPS："
        self.sounds = "音效："
        self.interact = "交互："
        self.restart = "重新启动："
        self.menu = "菜单："
        self.language = "语言："
        self.settings = "设置"
        
        self.fps_show = "显示"
        self.fps_hide = "隐藏"
    
        # Gameplay
        self.end = "结束"
        self.score = "分数："
        self.next_level = "下一级："
        self.level = "级别："
        self.moves = "移动次数："
        self.time = "计时器："
        
        self.congrats_1 = "恭喜，"
        self.congrats_2 = "你已完成 "
        self.congrats_3 = "！"
        
        # Editor
        self.editor_title = "Sisyphe.io - 级别编辑器"
        self.editor_new_file = "无标题"
        self.unsaved_title = "未保存的更改"
        self.unsaved = "您可能有未保存的更改。您是否仍然要退出？"
        
        self.error_player = "未放置玩家在游戏板上。"
        self.error_boulder = "在游戏板上未放置巨石或洞口，或者没有足够的巨石来填满所有的洞口。"
        self.error_portal = "一个传送门放置在游戏板上没有它的配对物。"
        self.error_door = "一个门放置在游戏板上没有压力板，反之亦然。"
        self.error_not_valid = "您尝试保存的级别无效："
        
        self.file_menu = "文件"
        self.edition_menu = "编辑"
        self.textures_menu = "纹理"
        self.music_menu = "音乐和音效"
        
        self.new_button = "新建"
        self.save_button = "保存"
        self.save_as_button = "另存为..."
        self.toggle_textures_button = "切换纹理"
        self.toggle_music_button = "切换音乐"
        self.toggle_sounds_button = "切换音效"
        
        self.base_objects = "基本对象"
        self.special_objects = "特殊对象"
        
        self.select_wall = "选择墙壁对象"
        self.select_boulder = "选择巨石对象"
        self.select_hole = "选择洞口对象"
        self.select_box = "选择箱子对象"
        self.select_player = "选择Sisyphe对象"
        self.select_portal1 = "选择蓝色传送门对象"
        self.select_portal2 = "选择红色传送门对象"
        self.select_door = "选择门对象"
        self.select_pressure_plate = "选择压力板对象"
        self.select_cracked_wall = "选择裂缝墙壁对象"
        self.select_hammer = "选择锤子对象"
        self.select_rope = "选择绳索对象"
        self.delete_mode = "删除模式"
        
        self.return_key = "返回"
        
        self.editor_tutorial_title = "教程 - 级别编辑器"
        self.editor_tutorial = "欢迎来到级别编辑器！\n\n在这里，您可以从编辑菜单中选择所需的对象。\n\n您还可以使用文件菜单创建、加载和保存您的级别。\n\n要显示/隐藏游戏纹理，请使用纹理菜单。\n\n编辑器完成后，您可以在主菜单中使用打开按钮选择您的级别！"

    def japanese(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "プレイ"
        self.open_button = "開く"
        self.editor_button = "エディタ"
        self.credits_button = "クレジット"
        self.leave_button = "終了"
        
        self.reset_button = "リセット"
        self.back_button = "戻る"
        self.popup_close_button = "閉じる"
        
        # Tutorials
        self.w1_tutorial_1 = "Sisyphe.ioへようこそ！\n\nこのゲームでは、すべての大きな岩を対応する穴に持っていって前進する必要があります！（詳細はスクロールしてください）\n\nスコアは移動回数に大きく依存しているので、ゲームプレイを最適化しましょう！\n\nレベルをリスタートしたい場合は、タップしてください "
        self.w1_tutorial_2 = "、メインメニューに戻りたい場合はタップしてください "
        
        self.w2_tutorial = "あなたは今、ワールド2にいます！\n\nこの世界では、2つの新しいブロックタイプがあります：青いポータルと赤いポータル。 （詳細はスクロールしてください）\n\n前進するには、そのうちの1つを通過してもう1つにテレポートする必要があります！"
    
        self.w3_tutorial_1 = "さあ、ワールド3に向かいましょう！\n\nこの世界では、タップして大きな岩を引き寄せるためにロープを拾うことができます "
        self.w3_tutorial_2 = "！（詳細はスクロールしてください）\n\nキャラクターが向いている方向を変更するには、[CTRL/SHIFT + 方向キー]を使用できます。\n\nいくつかの箱が邪魔になるかもしれませんが、心配はいりません：\n\nそれらは大きな岩と同様に機能しますが、ロープでのみ移動でき、どこにも持っていく必要はありません！"
        self.w4_tutorial = "ワールド4、ここにいます！\n\nこの世界では、前進するために一連の扉を開く必要があります。 （詳細はスクロールしてください）\n\nどうやって？対応する緑の圧力プレートに大きな岩を押し当てることで！\n\n警告：ドアは閉じるときに下にあるものすべてを押しつぶします。これには、現在のレベルを再起動する可能性のある大きな岩も含まれます。"
        
        self.w5_tutorial = "ワールド5があなたを待っています！\n\nこの世界では、ハンマーがゲームボード上に生成されることがあります。 （詳細はスクロールしてください）\n\nそれらを拾うと、タップして最大3つの裂けた壁を壊すことができます "
        
        # Other
        self.world = "ワールド "
        self.reset_save_confirm = "本当に進捗をリセットしますか？"
        self.error = "エラー"
        self.error_opening = "ファイルを開こうとしてエラーが発生しました。"
        self.corrupted = "ファイルを開こうとしてエラーが発生しました。おそらく、Sisyphe.ioと互換性がないか、または破損している可能性があります！"
        self.reset_lang_confirm = "本当に設定をリセットしますか？"
        self.open_file = "ファイルを開く"
        self.confirm = "確認"
        self.no_access_title = "アクセスが拒否されました"
        self.no_access = "レベルエディタとカスタムレベルにアクセスする前に、ワールド1を完了してください！"
        self.rpc_download = "ダウンロード"
        self.rpc_menu = "プレイ中"
        
        # DB
        self.no_score= "記録されたスコアはありません"
        self.best_score_1="ベストスコア： "
        self.best_score_2=" "
        self.best_score_3=" "
        self.best_score_4=" に"

        # Settings Menu
        self.up = "上："
        self.left = "左："
        self.down = "下："
        self.right = "右："
        
        self.music = "音楽："
        self.fps = "FPS："
        self.sounds = "サウンド："
        self.interact = "インタラクト："
        self.restart = "再起動："
        self.menu = "メニュー："
        self.language = "言語："
        self.settings = "設定"
        
        self.fps_show = "表示"
        self.fps_hide = "非表示"
    
        # Gameplay
        self.end = "終了"
        self.score = "スコア："
        self.next_level = "次のレベル："
        self.level = "レベル："
        self.moves = "移動回数："
        self.time = "タイマー："
        
        self.congrats_1 = "おめでとう、"
        self.congrats_2 = "あなたは完了しました "
        self.congrats_3 = "！"
        
        # Editor
        self.editor_title = "Sisyphe.io - レベルエディタ"
        self.editor_new_file = "無題"
        self.unsaved_title = "未保存の変更"
        self.unsaved = "未保存の変更があるかもしれません。まだ終了しますか？"
        
        self.error_player = "ゲームボードにプレイヤーが配置されていません。"
        self.error_boulder = "ゲームボードに大きな岩や穴が配置されていないか、すべての穴を埋めるのに十分な大きな岩がありません。"
        self.error_portal = "ポータルがそのペアなしにゲームボードに配置されています。"
        self.error_door = "ドアが圧力プレートなしにゲームボードに配置されているか、その逆です。"
        self.error_not_valid = "保存しようとしているレベルは無効です："
        
        self.file_menu = "ファイル"
        self.edition_menu = "編集"
        self.textures_menu = "テクスチャ"
        self.music_menu = "音楽＆サウンド"
        
        self.new_button = "新規作成"
        self.save_button = "保存"
        self.save_as_button = "名前を付けて保存..."
        self.toggle_textures_button = "テクスチャの切り替え"
        self.toggle_music_button = "音楽の切り替え"
        self.toggle_sounds_button = "サウンドの切り替え"
        
        self.base_objects = "基本オブジェクト"
        self.special_objects = "特殊オブジェクト"
        
        self.select_wall = "壁オブジェクトを選択"
        self.select_boulder = "大きな岩オブジェクトを選択"
        self.select_hole = "穴オブジェクトを選択"
        self.select_box = "箱オブジェクトを選択"
        self.select_player = "Sisypheオブジェクトを選択"
        self.select_portal1 = "青いポータルオブジェクトを選択"
        self.select_portal2 = "赤いポータルオブジェクトを選択"
        self.select_door = "ドアオブジェクトを選択"
        self.select_pressure_plate = "圧力プレートオブジェクトを選択"
        self.select_cracked_wall = "裂けた壁オブジェクトを選択"
        self.select_hammer = "ハンマーオブジェクトを選択"
        self.select_rope = "ロープオブジェクトを選択"
        self.delete_mode = "削除モード"
        
        self.return_key = "バックスペース"
        
        self.editor_tutorial_title = "チュートリアル - レベルエディタ"
        self.editor_tutorial = "レベルエディタへようこそ！\n\nここでは、編集メニューから必要なオブジェクトを選択できます。\n\nファイルメニューを使用してレベルを作成、読み込み、保存することもできます。\n\nゲームテクスチャの表示/非表示には、テクスチャメニューを使用します。\n\nエディタで作業が終了したら、メインメニューの[開く]ボタンを使用してレベルを選択できます！"

    def korean(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "플레이"
        self.open_button = "열기"
        self.editor_button = "편집기"
        self.credits_button = "크레딧"
        self.leave_button = "종료"
        
        self.reset_button = "초기화"
        self.back_button = "뒤로 가기"
        self.popup_close_button = "닫기"
        
        # Tutorials
        self.w1_tutorial_1 = "Sisyphe.io에 오신 것을 환영합니다!\n\n이 게임에서는 모든 큰 바위를 해당하는 구멍으로 가져가서 전진해야합니다! (자세한 내용은 스크롤하여 확인)\n\n스코어는 이동 횟수에 크게 의존하므로 게임 플레이를 최적화하려고 노력하세요!\n\n레벨을 다시 시작하려면 탭하십시오 "
        self.w1_tutorial_2 = ", 메인 메뉴로 돌아가려면 탭하십시오 "
        
        self.w2_tutorial = "이제 2번째 세계에 있습니다!\n\n이 세계에서는 두 가지 새로운 블록 유형을 찾을 수 있습니다: 파란 포탈과 빨간 포탈. (자세한 내용은 스크롤하여 확인)\n\n전진하려면 그 중 하나를 통과하여 다른 곳으로 이동해야합니다!"
    
        self.w3_tutorial_1 = "3번 세계로 이동합시다!\n\n이 세계에서는 탭하여 로프를 줍고 "
        self.w3_tutorial_2 = " ! (자세한 내용은 스크롤하여 확인)\n\n캐릭터가 향하는 방향을 변경하려면 [CTRL/SHIFT + 방향 키]를 사용할 수 있습니다.\n\n일부 상자가 길에 오를 수도 있지만 걱정하지 마세요:\n\n그들은 바위와 유사하게 작동하지만 로프로만 이동할 수 있으며 어디로든 가져 갈 필요가 없습니다!"
        self.w4_tutorial = "4번 세계, 여기 있습니다!\n\n이 세계에서는 전진하려면 일련의 문을 열어야합니다. (자세한 내용은 스크롤하여 확인)\n\n어떻게? 대응하는 녹색 압력 판 위로 큰 바위를 밀어 넣음으로써!\n\n경고 : 문은 닫을 때 아래에있는 모든 것을 짓누르게됩니다. 이는 현재 레벨을 다시 시작할 수있는 큰 바위를 포함 할 수 있습니다."
        
        self.w5_tutorial = "5번 세계가 당신을 기다리고 있습니다!\n\n이 세계에서는 게임 보드에 망치가 생성 될 수 있습니다. (자세한 내용은 스크롤하여 확인)\n\n이를 줍으면 탭하여 최대 3개의 깨진 벽을 부술 수 있습니다 "
        
        # Other
        self.world = "세계 "
        self.reset_save_confirm = "진행을 재설정 하시겠습니까?"
        self.error = "에러"
        self.error_opening = "파일을 열려고 할 때 오류가 발생했습니다."
        self.corrupted = "파일을 열려고 할 때 오류가 발생했습니다. 레벨이 손상되었거나 Sisyphe.io와 호환되지 않을 수 있습니다!"
        self.reset_lang_confirm = "정말로 설정을 재설정 하시겠습니까?"
        self.open_file = "파일 열기"
        self.confirm = "확인"
        self.no_access_title = "액세스 거부"
        self.no_access = "레벨 편집기와 사용자 정의 레벨에 액세스하려면 World 1을 완료하십시오!"
        self.rpc_download = "다운로드"
        self.rpc_menu = "플레이 중"
        
        # DB
        self.no_score= "저장된 점수가 없습니다"
        self.best_score_1="최고 점수: "
        self.best_score_2=" "
        self.best_score_3=" "
        self.best_score_4=" 에"

        # Settings Menu
        self.up = "위: "
        self.left = "왼쪽: "
        self.down = "아래: "
        self.right = "오른쪽: "
        
        self.music = "음악: "
        self.fps = "FPS: "
        self.sounds = "사운드: "
        self.interact = "상호 작용: "
        self.restart = "재시작: "
        self.menu = "메뉴: "
        self.language = "언어: "
        self.settings = "설정"
        
        self.fps_show = "표시"
        self.fps_hide = "숨기기"
    
        # Gameplay
        self.end = "종료"
        self.score = "스코어: "
        self.next_level = "다음 레벨: "
        self.level = "레벨: "
        self.moves = "이동 횟수: "
        self.time = "타이머: "
        
        self.congrats_1 = "축하합니다,"
        self.congrats_2 = "당신은 완료했습니다 "
        self.congrats_3 = "!"
        
        # Editor
        self.editor_title = "Sisyphe.io - 레벨 편집기"
        self.editor_new_file = "무제"
        self.unsaved_title = "저장되지 않은 변경 사항"
        self.unsaved = "저장되지 않은 변경 사항이 있을 수 있습니다. 그래도 종료 하시겠습니까?"
        
        self.error_player = "게임 보드에 플레이어가 배치되지 않았습니다."
        self.error_boulder = "게임 보드에 큰 바위 또는 구멍이 배치되지 않았거나 모든 구멍을 채울만큼 충분한 큰 바위가 없습니다."
        self.error_portal = "포탈이 그것의 짝없이 게임 보드에 배치되어 있습니다."
        self.error_door = "게임 보드에 문이 압력 판이나 그 반대없이 배치되었거나 그 반대입니다."
        self.error_not_valid = "저장하려는 레벨이 유효하지 않습니다: "
        
        self.file_menu = "파일"
        self.edition_menu = "편집"
        self.textures_menu = "텍스처"
        self.music_menu = "음악 및 사운드"
        
        self.new_button = "새로 만들기"
        self.save_button = "저장"
        self.save_as_button = "다른 이름으로 저장..."
        self.toggle_textures_button = "텍스처 전환"
        self.toggle_music_button = "음악 전환"
        self.toggle_sounds_button = "사운드 전환"
        
        self.base_objects = "기본 오브젝트"
        self.special_objects = "특별 오브젝트"
        
        self.select_wall = "벽 오브젝트 선택"
        self.select_boulder = "큰 바위 오브젝트 선택"
        self.select_hole = "구멍 오브젝트 선택"
        self.select_box = "상자 오브젝트 선택"
        self.select_player = "Sisyphe 오브젝트 선택"
        self.select_portal1 = "파란 포탈 오브젝트 선택"
        self.select_portal2 = "빨간 포탈 오브젝트 선택"
        self.select_door = "문 오브젝트 선택"
        self.select_pressure_plate = "압력 판 오브젝트 선택"
        self.select_cracked_wall = "깨진 벽 오브젝트 선택"
        self.select_hammer = "망치 오브젝트 선택"
        self.select_rope = "로프 오브젝트 선택"
        self.delete_mode = "삭제 모드"
        
        self.return_key = "백스페이스"
        
        self.editor_tutorial_title = "튜토리얼 - 레벨 편집기"
        self.editor_tutorial = "레벨 편집기에 오신 것을 환영합니다!\n\n여기에서는 편집 메뉴에서 원하는 오브젝트를 선택할 수 있습니다.\n\n파일 메뉴를 사용하여 레벨을 만들고 로드하고 저장할 수도 있습니다.\n\n게임 텍스처를 표시/숨기려면 텍스처 메뉴를 사용하십시오.\n\n편집기 작업을 마치면 메인 메뉴에서 [열기] 버튼을 사용하여 레벨을 선택할 수 있습니다!"

    def arabic(self):
        self.game_name = "Sisyphe.io"
        
        # Buttons
        self.play_button = "شغل"
        self.open_button = "افتح"
        self.editor_button = "المحرر"
        self.credits_button = "الاعتمادات"
        self.leave_button = "خروج"
        
        self.reset_button = "إعادة تعيين"
        self.back_button = "عد إلى الخلف"
        self.popup_close_button = "رفض"
        
        # Tutorials
        self.w1_tutorial_1 = "مرحبًا بك في Sisyphe.io!\n\nفي هذه اللعبة ، تحتاج إلى نقل جميع الصخور إلى الفجوات المقابلة للتقدم! (التمرير للمزيد)\n\nيعتمد درجة أدائك بشكل كبير على عدد الحركات الخاصة بك ، لذا حاول تحسين أسلوب اللعب الخاص بك!\n\nإذا كنت ترغب في إعادة تشغيل المستوى ، اضغط "
        self.w1_tutorial_2 = "، إذا كنت ترغب في العودة إلى القائمة الرئيسية ، اضغط "
        
        self.w2_tutorial = "أنت الآن في العالم 2!\n\nفي هذا العالم ، يمكنك العثور على نوعين جديدين من الكتل: بوابة زرقاء وبوابة حمراء. (التمرير للمزيد)\n\nللتقدم ، ستحتاج إلى المرور من خلال واحدة منها لتنتقل إلى الأخرى!"
        
        self.w3_tutorial_1 = "لنتوجه إلى العالم 3!\n\nفي هذا العالم ، يمكنك التقاط حبال لسحب صخرة نحوك بالضغط "
        self.w3_tutorial_2 = " ! (التمرير للمزيد)\n\nلتغيير اتجاه شخصيتك ، يمكنك استخدام [CTRL/SHIFT + مفاتيح الاتجاه].\n\nقد تكون بعض الصناديق أيضًا في طريقك ، ولكن لا داعي للقلق:\n\nإنها تعمل بشكل مماثل للصخور ، باستثناء حقيقة أنه يمكنك نقلها فقط بواسطة حبل ، ولا داعي لجلبها إلى أي مكان!"
        self.w4_tutorial = "العالم 4 ، ها نحن الآن!\n\nفي هذا العالم ، ستحتاج إلى فتح مجموعة من الأبواب للتقدم. (التمرير للمزيد)\n\nكيف؟ عن طريق دفع صخرة على الألواح الخضراء المقابلة!\n\nتحذير: الأبواب ستسحق أي شيء يكون أسفلها عند إغلاقها ، بما في ذلك الصخور التي قد تضطرك إلى إعادة تشغيل المستوى الحالي."
        
        self.w5_tutorial = "العالم 5 ينتظرك!\n\nفي هذا العالم ، يمكن أن تظهر مطارق على لوحة اللعب. (التمرير للمزيد)\n\nاقتلاعها سيسمح لك بكسر ما يصل إلى 3 جدران متصدعة بالضغط "
        
        # Other
        self.world = "عالم "
        self.reset_save_confirm = "هل ترغب حقًا في إعادة تعيين تقدمك؟"
        self.error = "خطأ"
        self.error_opening = "حدث خطأ أثناء محاولة فتح الملف الخاص بك."
        self.corrupted = "حدث خطأ أثناء محاولة فتح الملف الخاص بك. يمكن أن يكون مستواك قد تم تلفه أو عدم توافقه مع Sisyphe.io!"
        self.reset_lang_confirm = "هل ترغب حقًا في إعادة تعيين الإعدادات؟"
        self.open_file = "فتح الملف"
        self.confirm = "تأكيد"
        self.no_access_title = "تم الرفض في الوصول"
        self.no_access = "الرجاء إكمال العالم 1 قبل الوصول إلى محرر المستوى والمستويات المخصصة!"
        self.rpc_download = "تحميل"
        self.rpc_menu = "اللعب"
        
        # DB
        self.no_score= "لا يوجد درجات مسجلة"
        self.best_score_1= "أفضل درجة: "
        self.best_score_2=""
        self.best_score_3=" الساعة "
        self.best_score_4=" في"

        # Settings Menu
        self.up = "أعلى: "
        self.left = "يسار: "
        self.down = "أسفل: "
        self.right = "يمين: "
        
        self.music = "الموسيقى: "
        self.fps = "FPS: "
        self.sounds = "الأصوات: "
        self.interact = "تفاعل: "
        self.restart = "إعادة بدء: "
        self.menu = "القائمة: "
        self.language = "اللغة: "
        self.settings = "الإعدادات"
        
        self.fps_show = "عرض"
        self.fps_hide = "إخفاء"
        
        # Gameplay
        self.end = "نهاية"
        self.score = "النقاط: "
        self.next_level = "المستوى التالي: "
        self.level = "المستوى: "
        self.moves = "عدد الحركات: "
        self.time = "المؤقت: "
        
        self.congrats_1 = "تهانينا،"
        self.congrats_2 = "لقد أكملت "
        self.congrats_3 = "!"
        
        # Editor
        self.editor_title = "Sisyphe.io - محرر المستوى"
        self.editor_new_file = "بدون عنوان"
        self.unsaved_title = "تغييرات غير محفوظة"
        self.unsaved = "قد تكون لديك تغييرات غير محفوظة. هل ترغب لا تزال في الخروج؟"
        
        self.error_player = "لم يتم وضع لاعب على لوحة اللعب."
        self.error_boulder = "لم يتم وضع صخرة أو فجوة على لوحة اللعب ، أو ليس هناك ما يكفي من الصخور لملء جميع الفجوات."
        self.error_portal = "تم وضع بوابة على لوحة اللعب بدون الزوج الخاص بها."
        self.error_door = "تم وضع باب على لوحة اللعب بدون لوحة ضغط ، أو العكس."
        self.error_not_valid = "المستوى الذي تحاول حفظه غير صالح: "
        
        self.file_menu = "ملف"
        self.edition_menu = "تحرير"
        self.textures_menu = "النقوش"
        self.music_menu = "الموسيقى والأصوات"
        
        self.new_button = "جديد"
        self.save_button = "حفظ"
        self.save_as_button = "حفظ باسم..."
        self.toggle_textures_button = "تبديل النقوش"
        self.toggle_music_button = "تبديل الموسيقى"
        self.toggle_sounds_button = "تبديل الأصوات"
        
        self.base_objects = "الكائنات الأساسية"
        self.special_objects = "الكائنات الخاصة"
        
        self.select_wall = "اختيار كائن الجدار"
        self.select_boulder = "اختيار كائن الصخرة"
        self.select_hole = "اختيار كائن الفجوة"
        self.select_box = "اختيار كائن الصندوق"
        self.select_player = "اختيار كائن Sisyphe"
        self.select_portal1 = "اختيار كائن البوابة الزرقاء"
        self.select_portal2 = "اختيار كائن البوابة الحمراء"
        self.select_door = "اختيار كائن الباب"
        self.select_pressure_plate = "اختيار كائن لوحة الضغط"
        self.select_cracked_wall = "اختيار كائن الجدار المتصدع"
        self.select_hammer = "اختيار كائن المطرقة"
        self.select_rope = "اختيار كائن الحبل"
        self.delete_mode = "وضع الحذف"
        
        self.return_key = "مفتاح العودة"
        
        self.editor_tutorial_title = "دورة تعليمية - محرر المستوى"
        self.editor_tutorial = "مرحبًا بك في محرر المستوى!\n\nهنا يمكنك اختيار الكائن الذي تريده من قائمة التحرير.\n\nيمكنك أيضًا إنشاء وتحميل وحفظ مستواك باستخدام قائمة الملف.\n\nلإظهار/إخفاء النقوش في اللعبة ، استخدم قائمة النقوش.\n\nبعد الانتهاء من المحرر ، يمكنك استخدام زر افتح في القائمة الرئيسية لتحديد مستواك!"
