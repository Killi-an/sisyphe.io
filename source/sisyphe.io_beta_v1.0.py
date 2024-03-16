# -*- coding: utf-8 -*-

# Import modules globaux
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import time
import json
import subprocess
import threading
#Imports pour la future compilation du jeu en .exe
import sys  # À GARDER POUR .EXE
import os
import shutil

# Import modules locaux
import assets.package.game_images as images
import assets.package.game_deroulement as deroulement
import assets.package.game_tooltip as tooltip
import assets.package.game_music as music
import assets.package.game_lang as langue

# METTRE À TRUE POUR COMPILER LE JEU EN .EXE
fichier_exe=False

# VERSION DU JEU
version = "beta v1.0"

# Pour lorsque le jeu est compilé en .exe, cela crée un répertoire dans local/appdata

def extract_settings():
    # Détermine si le jeu est exécuté depuis un fichier Python, ou un fichier .exe
    settings = os.path.join(assets_dir, 'assets', 'settings.json')

    # POUR WINDOWS - Met le répertoire de destination pour créer le dossier assets dans appdata/local
    target_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Sisyphe.io')
    
    # POUR MAC/LINUX - Met le répertoire de destination pour créer le dossier assets dans le répertoire courant
    #target_dir = 'Sisyphe.io'
    
    # Regarde si le dossier existe déjà
    if not os.path.exists(target_dir):
        #Si non, créer le dossier
        os.makedirs(target_dir, exist_ok=True)
    # Regarde si le fichier existe déjà
    if not os.path.exists(os.path.join(target_dir, 'settings.json')):
    # Si non, copie les paramètres du jeu dans le dossier local/appdata
        shutil.copy(settings, target_dir)

    return target_dir



if fichier_exe==True:
    assets_dir = sys._MEIPASS
else:
    assets_dir= ''
settings_dir=extract_settings()
images.base_path=assets_dir


# Création fenêtre principale
Mafenetre = tk.Tk()
Mafenetre.geometry("800x600")
Mafenetre.title(version)
Mafenetre.iconbitmap(os.path.join(assets_dir, 'assets', 'img', 'icons', 'game_tskbr.ico'))
Mafenetre.resizable(False, False)
path=os.path.join(assets_dir, 'assets', 'img', 'cur', 'normal.cur')
path = path.replace('\\', '/')
Mafenetre['cursor'] = f'@{path}'

# Pour la barre latérale des tutoriels
style = ttk.Style()
style.theme_use('clam')
color_1="#bea48e"
color_2='#7c645c'
style.configure('Vertical.TScrollbar', relief='flat',background=color_1, lightcolor=color_1, darkcolor=color_1,bordercolor=color_2, troughcolor=color_2, arrowcolor=color_2)

#Appel des classes dans modules locaux
if __name__ == "__main__":
    game_images = images.GameImages()
    jeu=deroulement.GameDeroulement()
    sound_manager = music.SoundManager()
    lang = langue.Traduction()
    
#variables globales
background_label = None

#Initialisation de tous les sons du jeu
sound_manager.load_sound('steps1', os.path.join(assets_dir, 'assets', 'sfx', 'footsteps1.wav'))
sound_manager.load_sound('steps2', os.path.join(assets_dir, 'assets', 'sfx', 'footsteps2.wav'))
sound_manager.load_sound('small_win', os.path.join(assets_dir, 'assets', 'sfx', 'level_completed.wav'))
sound_manager.load_sound('big_win', os.path.join(assets_dir, 'assets', 'sfx', 'world_completed.wav'))
sound_manager.load_sound('hole_filled', os.path.join(assets_dir, 'assets', 'sfx', 'hole_filled.wav'))
sound_manager.load_sound('portal', os.path.join(assets_dir, 'assets', 'sfx', 'portal_entered.wav'))
sound_manager.load_sound('powerup', os.path.join(assets_dir, 'assets', 'sfx', 'powerup_taken.wav'))
sound_manager.load_sound('break', os.path.join(assets_dir, 'assets', 'sfx', 'wall_broken.wav'))
sound_manager.load_sound('door', os.path.join(assets_dir, 'assets', 'sfx', 'door_opened.wav'))
sound_manager.load_sound('door2', os.path.join(assets_dir, 'assets', 'sfx', 'door_closed.wav'))
sound_manager.load_sound('button', os.path.join(assets_dir, 'assets', 'sfx', 'button_pressed.wav'))
sound_manager.load_sound('reset', os.path.join(assets_dir, 'assets', 'sfx', 'reset_level.wav'))
sound_manager.load_sound('menu', os.path.join(assets_dir, 'assets', 'sfx', 'return_menu.wav'))
sound_manager.load_sound('popup', os.path.join(assets_dir, 'assets', 'sfx', 'popup_menu.wav'))

#parametres du jeu
with open(os.path.join(settings_dir, 'settings.json'), 'r') as fichier:
    parametres = json.load(fichier)

#asserts pour le fichier json
required_keys = ["controles", "mondes", "tutoriels", "fps", "volume", "language"]
for key in required_keys:
    assert key in parametres, f"Valeur manquante : {key}"

# Met la langue du jeu par défaut
languages=["fr", "en", "es", "it", "pt", "de", "ru", "zh_TW", "zh_CN", "jp", "ko", "ar"]

languages_dic = {
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

functions_dic = {
    "fr": lang.french,
    "en": lang.english,
    "es": lang.spanish,
    "it": lang.italian,
    "pt": lang.portuguese,
    "de": lang.german,
    "ru": lang.russian,
    "zh_TW": lang.chinese_traditional,
    "zh_CN": lang.chinese_simplified,
    "jp": lang.japanese,
    "ko": lang.korean,
    "ar": lang.arabic
}

def apply_language():
    global languages, functions_dic
    assert parametres["language"] in languages
    for elt in languages:
        if elt==parametres["language"]:
            functions_dic[elt]()
            return
apply_language()

#volume initial des musiques
music.set_volume(parametres["volume"]["musique"])
sound_manager.set_volume(parametres["volume"]["sons"])

# Boutons pour menu
start_button = None
menu_button = None
edit_button = None
command_button = None
credits_button = None
leave_button = None

# Bouton pour mondes
monde_buttons=None
return_button=None

#popup pour crédits
popup=None

# Crée le plateau de jeu
plateau = []
for i in range(12):
    plateau.append([])
    for j in range(16):
        plateau[i].append([0, 0, 0, 0])  # Case vide par défaut

#ajoute les murs par défaut autour de la zone de jeu
def murs_de_base():
    clear_canvas()
    for i in range(12):
        plateau[i][0][0]=1
        plateau[i][1][0]=1
        plateau[i][14][0]=1
        plateau[i][15][0]=1
        
    for j in range(16):
        plateau[0][j][0]=1
        plateau[1][j][0]=1
        plateau[10][j][0]=1
        plateau[11][j][0]=1
        
# Efface le canvas
def clear_canvas():
    Canevas.delete("all")

def clear_buttons_1():
    global start_button, menu_button, edit_button, command_button, credits_button, leave_button, return_button
    if start_button is not None:
        start_button.destroy()
        start_button = None
    if menu_button is not None:
        menu_button.destroy()
        menu_button = None
    if edit_button is not None:
        edit_button.destroy()
        edit_button = None
    if command_button is not None:
        command_button.destroy()
        command_button = None
    if credits_button is not None:
        credits_button.destroy()
        credits_button = None
    if leave_button is not None:
        leave_button.destroy()
        leave_button = None
    if return_button is not None:
        return_button.destroy()
        return_button=None

def clear_buttons_2():
    global monde_buttons, return_button
    for elt in monde_buttons:
        if elt is not None:
            elt.destroy()
    monde_buttons=None
    if return_button is not None:
        return_button.destroy()
        return_button=None
        
def clear_bg():
    global background_label
    if background_label is not None:
        background_label.destroy()
        background_label = None

# Fonctions pour ouvrir l'éditeur et les paramètres
def monitor_subprocess(process):
    process.wait()  # Attend la fin du sous-processus
    jeu.process_launched=False
    Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', 'menu_main.ogg')))

def open_external_app():
    sound_manager.play_sound('button')
    if jeu.process_launched==False:
        if fichier_exe==True:
            proc = subprocess.Popen([os.path.join(assets_dir, 'assets', 'sisyphe.io_editor_v2.0.exe')])
        else:
            proc = subprocess.Popen(["python", os.path.join(assets_dir, 'assets', 'sisyphe.io_editor_v2.0.py')])
        jeu.process_launched=True
        monitor_thread = threading.Thread(target=monitor_subprocess, args=(proc,))
        monitor_thread.start()
        music.stop_music()

def show_popup():
    sound_manager.play_sound('button')
    if jeu.process_launched==True:
        return
    if messagebox.showinfo(lang.no_access_title, lang.no_access, icon="warning") == 'ok':
        sound_manager.play_sound('button')

# La variable croix permet de vérifier si la fonction est appelée lors d'un ALT+F4 ou d'une fermeture forcée, ou avec le bouton quitter en jeu
def quitter(croix=False):
    global proc
    if jeu.process_launched==True:
        if croix==False:
            sound_manager.play_sound('button')
            return
    elif croix==False:
        sound_manager.play_sound('button')
    # Arrête la musique à la fermeture du jeu
    music.stop_music()
    Mafenetre.destroy()

def button_world():
    sound_manager.play_sound('button')
    create_world_selection_menu()

def button_settings():
    sound_manager.play_sound('button')
    create_settings_menu()

# Fonction pour créer le menu principal
def create_main_menu():
    global start_button, menu_button, edit_button, command_button, credits_button, leave_button, background_label, monde_buttons, parametres
    
    # Pour bouton reset/menu
    clear_canvas_and_buttons()
    clear_buttons_1()
    clear_bg()
    
    # Titre de la fenêtre
    Mafenetre.title(lang.game_name)
    
    # Image en fond d'écran
    if background_label is None:
        background_image=game_images.world_menu_texture
        background_label = tk.Label(Mafenetre, image=background_image)
        background_label.place(x=0, y=0, width=800, height=600)
    
    if monde_buttons is not None:
        clear_buttons_2()
    #couleurs pour le bouton
    #color1='#7c645c'
    color2='#bb7e4b'
    color3='#714e31'
    color4='WHITE'
    
    # refresh les paramètres du jeu
    with open(os.path.join(settings_dir, 'settings.json'), 'r') as fichier:
        parametres = json.load(fichier)
      
    #Bouton Démarrer
    start_button=tk.Button(
        Mafenetre,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.play_button,
        font=('Small Fonts', 20, 'bold'),
        command=button_world
    )
    
    if parametres["mondes"]["monde_1_termine"]==True:
        #Bouton Niveaux Custom
        menu_button=tk.Button(
            Mafenetre,
            background=color2,
            foreground=color4,
            activebackground=color3,
            activeforeground=color4,
            highlightthickness=2,
            highlightbackground=color2,
            highlightcolor='WHITE',
            width=10,
            height=1,
            border=5,
            text=lang.open_button,
            font=('Small Fonts', 20, 'bold'),
            command=start_game_custom
        )
    
        #Bouton Editeur de niveaux
        edit_button=tk.Button(
            Mafenetre,
            background=color2,
            foreground=color4,
            activebackground=color3,
            activeforeground=color4,
            highlightthickness=2,
            highlightbackground=color2,
            highlightcolor='WHITE',
            width=10,
            height=1,
            border=5,
            text=lang.editor_button,
            font=('Small Fonts', 20, 'bold'),
            command=open_external_app
        )
    else:
        #Bouton Niveaux Custom grisé
        menu_button=tk.Button(
            Mafenetre,
            background='#656565',
            foreground='#a9a9a9',
            activebackground='#656565',
            activeforeground='#a9a9a9',
            highlightthickness=2,
            highlightbackground='#656565',
            highlightcolor='WHITE',
            width=10,
            height=1,
            border=5,
            text=lang.open_button,
            font=('Small Fonts', 20, 'bold'),
            command=show_popup
        )
        
        #Bouton Editeur de niveaux grisé
        edit_button=tk.Button(
            Mafenetre,
            background='#656565',
            foreground='#a9a9a9',
            activebackground='#656565',
            activeforeground='#a9a9a9',
            highlightthickness=2,
            highlightbackground='#656565',
            highlightcolor='WHITE',
            width=10,
            height=1,
            border=5,
            text=lang.editor_button,
            font=('Small Fonts', 20, 'bold'),
            command=show_popup
        )
        
    
    #Bouton Commandes du jeu
    command_button=tk.Button(
        Mafenetre,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.settings,
        font=('Small Fonts', 20, 'bold'),
        command=button_settings
    )

    credits_button=tk.Button(
        Mafenetre,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.credits_button,
        font=('Small Fonts', 20, 'bold'),
        command=credits_menu
    )

    leave_button=tk.Button(
        Mafenetre,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.leave_button,
        font=('Small Fonts', 20, 'bold'),
        command=quitter
    )
    
    #calcul du milieu de l'écran où placer le bouton
    button_width = start_button.winfo_reqwidth()
    button_height = start_button.winfo_reqheight()
    window_width = 800
    window_height = 600
    
    x = window_width / 2 - button_width - 10
    y = window_height / 2 - button_height - 10
    
    start_button.place(x=x, y=y)

    x = window_width / 2 - button_width - 10
    y = window_height/2 + 10
    
    command_button.place(x=x, y=y)

    x = window_width / 2 + 10
    y = window_height / 2 - button_height - 10

    menu_button.place(x=x, y=y)
    
    x = window_width / 2 + 10
    y = window_height / 2 +10
    
    edit_button.place(x=x, y=y)

    x = window_width / 2 - button_width - 10
    y = window_height/2 + button_height + 30
    
    credits_button.place(x=x, y=y)

    x = window_width / 2 + 10
    y = window_height/2 + button_height + 30
    
    leave_button.place(x=x, y=y)
    
    # Montre le curseur à nouveau après le jeu (pour le menu paramètres)
    Canevas.configure(cursor=f'@{path}')
    Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', 'menu_main.ogg')))

# Fonction pour les boîtes de dialogue
def show_dialog_bottom_screen(world_number):
    sound_manager.play_sound('popup')
    # Pour le bouton fermer
    def close_tutorial():
        sound_manager.play_sound('button')
        Canevas.focus_force()
        dialog_frame.destroy()
        border_frame.destroy()
    # Tous les textes de Tutoriels
    tuto_monde={
        1: lang.w1_tutorial_1+f"[ {parametres['controles']['reset'].upper()} ]"+lang.w1_tutorial_2+f"[ {parametres['controles']['menu'].upper()} ].",
        2: lang.w2_tutorial,
        3: lang.w3_tutorial_1+f"[ {parametres['controles']['interact'].upper()} ]"+lang.w3_tutorial_2,
        4: lang.w4_tutorial,
        5: lang.w5_tutorial+f"[ {parametres['controles']['interact'].upper()} ].",
    }
    
    dialog_text = tuto_monde[world_number]
    bg_color = '#998070'
    fg_color = 'WHITE'
    font_style = ('Small Fonts', 15)

    # Bordure de la boîte
    border_frame = tk.Frame(Mafenetre, background='#433632')
    
    # Boîte de dialogue
    dialog_frame = tk.Frame(Mafenetre, bg=bg_color)
    dialog_frame.pack_propagate(False) # Taille fixe pour la boîte

    # Texte à afficher
    text_widget = tk.Text(dialog_frame, wrap='word', font=font_style, borderwidth=0, bg=bg_color, fg=fg_color, height=4)
    text_widget.insert('1.0', dialog_text)
    path=os.path.join(assets_dir, 'assets', 'img', 'cur', 'normal.cur')
    path = path.replace('\\', '/')
    text_widget.configure(state='disabled', padx=10, pady=10, cursor=f'@{path}', takefocus=0)
    text_widget.tag_configure("centre_texte", justify='center')
    text_widget.tag_add("centre_texte", "1.0", "end")
    text_widget.focus_set()

    text_widget.bind("<Button-1>", lambda event: "break")
    text_widget.bind("<Button-2>", lambda event: "break")
    text_widget.bind("<Button-3>", lambda event: "break")
    text_widget.bind('<B1-Motion>', lambda event: "break")
    text_widget.bind("<FocusIn>", lambda event: "break")
    
    scrollbar = ttk.Scrollbar(dialog_frame, orient="vertical", style='Vertical.TScrollbar', command=text_widget.yview)
    text_widget['yscrollcommand'] = scrollbar.set
    
    scrollbar.pack(side='right', fill='y')

    # Bouton fermer
    close_button = tk.Button(dialog_frame, text=lang.popup_close_button, font=font_style, bg='#bea48e', border=2,fg=fg_color,activebackground='#7c645c', activeforeground='white', command=close_tutorial)

    # Met le bouton et le texte dans la boîte de dialogue
    text_widget.pack(side='top', fill='x', expand=True)
    close_button.pack(side='bottom', pady=10)

    # Calcule la taille du texte
    text_widget.update_idletasks()
    text_height = text_widget.winfo_reqheight()

    # Calcule la hauteur de la boîte
    button_height = close_button.winfo_reqheight()
    dialog_frame_height = text_height + button_height + 20

    # Centrer la boîte de dialogue sur l'écran
    window_width = Mafenetre.winfo_width()
    dialog_frame_width = window_width * 0.8  # 80% de la taille de la fenêtre

    # Met la boîte de dialogue au centre de la fenêtre
    border_frame.place(in_=Mafenetre, anchor='center', relx=0.5, rely=0.5, width=dialog_frame_width+10, height=dialog_frame_height+10)
    dialog_frame.place(in_=Mafenetre, anchor='center', relx=0.5, rely=0.5, width=dialog_frame_width, height=dialog_frame_height)

    # Empêche le tutoriel de se montrer plusieurs fois
    parametres["tutoriels"][f"tutoriel_{world_number}_termine"] = True
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)

Mafenetre.protocol("WM_DELETE_WINDOW", lambda croix=True: quitter(croix))
popup=None

# Pour faire le son d'appui de bouton avant de revenir au menu
def button_sound():
    sound_manager.play_sound('button')
    create_main_menu()

# Menu de sélection du monde
def create_world_selection_menu():
    global monde_buttons, background_label, popup, parametres
    if jeu.process_launched==True:
        return
    clear_canvas()
    clear_buttons_1()
    if monde_buttons is not None:
        clear_buttons_2()
    clear_bg()

    if background_label is None:
        background_image=game_images.world_menu_texture
        background_label = tk.Label(Mafenetre, image=background_image)
        background_label.place(x=0, y=0, width=800, height=600)
    
    # Fonctions pour commencer le jeu du monde 1 au monde 5
    def start_monde(monde):
        sound_manager.play_sound('button')
        clear_bg()
        clear_buttons_2()
        jeu.custom = 0
        clear_canvas()
        jeu.fini = False
        
        jeu.haut,jeu.bas,jeu.gauche,jeu.droite=0,0,0,0
        jeu.difficulte=monde
        demarrer_niveau()
        jeu.niveau = 1
        jeu.numero_monde = monde
        jeu.deplacements = 0

        genere_niveau(jeu.niveau,jeu.numero_monde, diff=jeu.difficulte)
        periodic_canvas_update(True)
        
        if parametres["tutoriels"][f"tutoriel_{jeu.numero_monde}_termine"] == False:
            show_dialog_bottom_screen(jeu.numero_monde)
        Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', f'world_{monde}.ogg')))
    button_pos = {
        1: [-250, 250],
        2: [-125, 375],
        3: [0, 250],
        4: [125, 375],
        5: [250, 250],
    }
    
    #refresh les parametres du jeu
    with open(os.path.join(settings_dir, 'settings.json'), 'r') as fichier:
        parametres = json.load(fichier)
    
    if parametres["fps"]["mode"]==2:
        jeu.mode_fps=33
    else:
        jeu.mode_fps=100
    
    # Crée un bouton pour chaque monde
    monde_buttons = []
    for i in range(1, 6):
        if i==1:
            commande=lambda i=i: start_monde(i)
            color2='#bea48e'
            color3='#7c645c'
            color4='WHITE'
            states='normal'
        elif parametres["mondes"][f"monde_{i-1}_termine"] == True:
            commande=lambda i=i: start_monde(i)
            color2='#bea48e'
            color3='#7c645c'
            color4='WHITE'
            states='normal'
        else:
            commande=None
            color2='#656565'
            color3=color2
            color4='#a9a9a9'
            states="disabled"
        
        monde_button = tk.Button(
            Mafenetre,
            background=color2,
            foreground=color4,
            activebackground=color3,
            activeforeground=color4,
            disabledforeground=color4,
            highlightthickness=2,
            highlightbackground=color2,
            highlightcolor='WHITE',
            width=10,
            height=1,
            border=5,
            text=lang.world+str(i),
            font=('Small Fonts', 20, 'bold'),
            command=commande,
            state=states
        )
        monde_button.place(x=400 - monde_button.winfo_reqwidth() / 2+button_pos[i][0], y=button_pos[i][1])
        monde_buttons.append(monde_button)
    
    return_button = tk.Button(
        Mafenetre,
        background='#bb7e4b',
        foreground='WHITE',
        activebackground='#714e31',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bb7e4b',
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.back_button,
        font=('Small Fonts', 15, 'bold'),
        command=button_sound
    )
    return_button.place(x=625, y=525)
    monde_buttons.append(return_button)
    
    reset_save_button = tk.Button(Mafenetre, text=lang.reset_button, command=reset_save,
                       background='#bb4b4b', foreground='WHITE', activebackground='#713131',
                       activeforeground='WHITE', highlightthickness=2, border=5, highlightbackground='#bb4b4b',
                       highlightcolor='WHITE', font=('Small Fonts', 15, 'bold'), width=15, anchor="center")
    reset_save_button.place(x=25, y=525)
    monde_buttons.append(reset_save_button)
    Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', 'menu_world.ogg')))

# Fonction pour remettre les paramètres à zéro
def reset_save():
    sound_manager.play_sound('button')
    if messagebox.askyesno(lang.confirm, lang.reset_save_confirm, icon="warning"):
        sound_manager.play_sound('button')
        for i in range(1,6):
            parametres["mondes"][f"monde_{i}_termine"] = False
            parametres["tutoriels"][f"tutoriel_{i}_termine"] = False
        parametres["tutoriels"]["tutoriel_editeur_termine"] = False
        with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
            json.dump(parametres, fichier, indent=4)
        create_world_selection_menu()
    else:
        sound_manager.play_sound('button')


# Menu paramètres

# Variables globales
popup = None  # Référence globale pour la fenêtre popup
button_widgets = []  # Liste globale pour les buttons afin de pouvoir les supprimer

def show_listening_popup(action):
    global popup
    sound_manager.play_sound('button')
    popup = tk.Toplevel(Mafenetre)
    popup.title("En attente...")
    popup.configure(bg='#9b6b53')  # Couleur du fond
    popup.geometry("450x100")
    popup.resizable(False, False)
    # Met à jour le label de la popup
    tk.Label(popup, text="Veuillez appuyer sur une touche...", bg='#9b6b53', fg='white', 
             font=("Small Fonts", "20")).pack(pady=20)
    # Commence à écouter les touches du clavier
    popup.bind('<Key>', lambda event: save_key_press(event, action))
    # La popup prend le focus
    popup.grab_set()
    popup.focus_set()
    # Pour fermer la popup
    popup.protocol("WM_DELETE_WINDOW", lambda: on_popup_close(action))
    # mettre la popup au centre
    window_width, window_height = 200, 100
    position_right = int(popup.winfo_screenwidth()/2 - window_width/2)
    position_down = int(popup.winfo_screenheight()/2 - window_height/2)
    popup.geometry("+{}+{}".format(position_right, position_down))
    
def on_popup_close(filename):
    global popup
    if popup:
        # Arrête d'écouter les touches du clavier
        popup.unbind('<Key>')
        popup.destroy()
        popup = None
        create_settings_menu()

# Quand une touche est appuyée
def save_key_press(event, action):
    valid_keys=["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","Up","Left","Down","Right", "space"]
    touche=event.keysym
    if touche=="Up" or touche=="Left" or touche=="Right" or touche=="Down":
        pass
    else:
        touche=touche.lower()
    if not touche in valid_keys:
        return
    # Vérifie si la touche que l'utilisateur veut utiliser est déjà assingée à une autre touche
    for key, value in parametres["controles"].items():
        if touche == value and key != action:
            return  # La touche est déjà utilisée, ne rien faire
    # Change la touche correspondante au bouton appuyé
    parametres["controles"][action] = touche

    # Sauvegarde les changements dans le fichier JSON
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    
    if popup:
        on_popup_close(action)  # Ferme la popup

# Gère les clics sur les boutons
def handle_button_click(action):
    def on_click():
        # Affiche la popup et continue le déroulement des actions
        show_listening_popup(action)
    return on_click

# Fonction pour créer les boutons
def create_direction_button(text, x, y, filename):
    global button_widgets
    button_width = 10
    button = tk.Button(Mafenetre, text=text, command=handle_button_click(filename),
                       background='#bea48e', foreground='WHITE', activebackground='#7c645c',
                       activeforeground='WHITE', highlightthickness=2, highlightbackground='#bea48e',
                       highlightcolor='WHITE', font=('Small Fonts', 15, 'bold'),border=3, width=button_width, anchor="center")
    button.place(x=x, y=y)
    button_widgets.append(button)

def clear_canvas_and_buttons():
    global button_widgets
    Canevas.delete("all")  # Supprime les éléments du canvas
    for button in button_widgets:
        button.destroy()  # Supprime tous les boutons
    button_widgets.clear()  # Vide la liste

def create_settings_menu():
    global monde_buttons, background_label, popup, parametres, button_widgets, languages_dic
    if jeu.process_launched==True:
        return
    clear_canvas()
    clear_buttons_1()
    if monde_buttons is not None:
        clear_buttons_2()
    clear_bg()
    clear_canvas_and_buttons()
    
    # rafraîchissement des paramètres
    with open(os.path.join(settings_dir, 'settings.json'), 'r') as fichier:
        parametres = json.load(fichier)
    
    Canevas.create_image(400, 300, image=game_images.settings_menu_texture, anchor="center")
    Canevas.create_image(400, 60, anchor="center", image=game_images.logo_texture)
    # Titre, sous-titre et textes à gauche des boutons
    Canevas.create_text(192, 182, fill='black', font=("Small Fonts", "20"), text=lang.up, anchor='e')
    Canevas.create_text(190, 180, fill='white', font=("Small Fonts", "20"), text=lang.up, anchor='e')

    Canevas.create_text(532, 282, fill='black', font=("Small Fonts", "20"), text=lang.music, anchor='e')
    Canevas.create_text(530, 280, fill='white', font=("Small Fonts", "20"), text=lang.music, anchor='e')
    
    Canevas.create_text(642, 282, fill='black', font=("Small Fonts", "20"), text=f"{parametres['volume']['musique']*5} %", anchor='center')
    Canevas.create_text(640, 280, fill='white', font=("Small Fonts", "20"), text=f"{parametres['volume']['musique']*5} %", anchor='center')

    Canevas.create_text(532, 182, fill='black', font=("Small Fonts", "20"), text=lang.fps, anchor='e')
    Canevas.create_text(530, 180, fill='white', font=("Small Fonts", "20"), text=lang.fps, anchor='e')
    
    Canevas.create_text(192, 232, fill='black', font=("Small Fonts", "20"), text=lang.left, anchor='e')
    Canevas.create_text(190, 230, fill='white', font=("Small Fonts", "20"), text=lang.left, anchor='e')
    
    Canevas.create_text(192, 282, fill='black', font=("Small Fonts", "20"), text=lang.down, anchor='e')
    Canevas.create_text(190, 280, fill='white', font=("Small Fonts", "20"), text=lang.down, anchor='e')

    Canevas.create_text(532, 332, fill='black', font=("Small Fonts", "20"), text=lang.sounds, anchor='e')
    Canevas.create_text(530, 330, fill='white', font=("Small Fonts", "20"), text=lang.sounds, anchor='e')
    
    Canevas.create_text(642, 332, fill='black', font=("Small Fonts", "20"), text=f"{parametres['volume']['sons']*5} %", anchor='center')
    Canevas.create_text(640, 330, fill='white', font=("Small Fonts", "20"), text=f"{parametres['volume']['sons']*5} %", anchor='center')
    
    Canevas.create_text(192, 332, fill='black', font=("Small Fonts", "20"), text=lang.right, anchor='e')
    Canevas.create_text(190, 330, fill='white', font=("Small Fonts", "20"), text=lang.right, anchor='e')

    Canevas.create_text(532, 232, fill='black', font=("Small Fonts", "20"), text=lang.language, anchor='e')
    Canevas.create_text(530, 230, fill='white', font=("Small Fonts", "20"), text=lang.language, anchor='e')
    
    Canevas.create_text(192, 382, fill='black', font=("Small Fonts", "20"), text=lang.interact, anchor='e')
    Canevas.create_text(190, 380, fill='white', font=("Small Fonts", "20"), text=lang.interact, anchor='e')
    
    Canevas.create_text(192, 432, fill='black', font=("Small Fonts", "20"), text=lang.restart, anchor='e')
    Canevas.create_text(190, 430, fill='white', font=("Small Fonts", "20"), text=lang.restart, anchor='e')
    
    Canevas.create_text(192, 482, fill='black', font=("Small Fonts", "20"), text=lang.menu, anchor='e')
    Canevas.create_text(190, 480, fill='white', font=("Small Fonts", "20"), text=lang.menu, anchor='e')
    
    Canevas.create_text(402, 122, fill='black', font=("Small Fonts", "25"), text=lang.settings, anchor='center')
    Canevas.create_text(400, 120, fill='white', font=("Small Fonts", "25"), text=lang.settings, anchor='center')
    
    # Boutons pour afficher et changer les contrôles
    create_direction_button(f'{parametres["controles"]["up"].upper()}', 230, 160, 'up')
    create_direction_button(f'{parametres["controles"]["left"].upper()}', 230, 210, 'left')
    create_direction_button(f'{parametres["controles"]["down"].upper()}', 230, 260, 'down')
    create_direction_button(f'{parametres["controles"]["right"].upper()}', 230, 310, 'right')
    create_direction_button(f'{parametres["controles"]["interact"].upper()}', 230, 360, 'interact')
    create_direction_button(f'{parametres["controles"]["reset"].upper()}', 230, 410, 'reset')
    create_direction_button(f'{parametres["controles"]["menu"].upper()}', 230, 460, 'menu')
    button = tk.Button(Mafenetre, text=lang.reset_button, command=reset_settings,
                       background='#bb4b4b', foreground='WHITE', activebackground='#713131',
                       activeforeground='WHITE', highlightthickness=2, border=5, highlightbackground='#bb4b4b',
                       highlightcolor='WHITE', font=('Small Fonts', 15, 'bold'), width=15, anchor="center")
    button_width_pixels = 214
    window_width = 800
    x_position = (window_width - button_width_pixels) / 2
    button.place(x=x_position, y=525)
    button_widgets.append(button)
    
    return_button = tk.Button(
        Mafenetre,
        background='#bb7e4b',
        foreground='WHITE',
        activebackground='#714e31',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bb7e4b',
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.back_button,
        font=('Small Fonts', 15, 'bold'),
        command=button_sound
    )
    return_button.place(x=625, y=525)
    button_widgets.append(return_button)
    
    if parametres["fps"]["mode"]==1:
        fps=10
    else:
        fps=30
    if parametres["fps"]["show"]:
        fps_state=lang.fps_show
    else:
        fps_state=lang.fps_hide

    fps_button = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=3,
        height=1,
        border=3,
        text=fps,
        font=('Small Fonts', 15, 'bold'),
        command=change_fps
    )
    fps_button.place(x=570, y=160)
    button_widgets.append(fps_button)

    fps_show = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        border=3,
        width=6,
        height=1,
        text=fps_state[0].upper()+fps_state[1:].lower(),
        font=('Small Fonts', 15, 'bold'),
        command=change_show_fps
    )
    fps_show.place(x=622, y=160)
    button_widgets.append(fps_show)

    music_button_minus = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=1,
        border=3,
        text="-",
        font=('Small Fonts', 15, 'bold'),
        command=lambda: change_volume_musique("down")
    )
    music_button_minus.place(x=570, y=260)
    button_widgets.append(music_button_minus)

    music_button_plus = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=1,
        border=3,
        text="+",
        font=('Small Fonts', 15, 'bold'),
        command=lambda: change_volume_musique("up")
    )
    music_button_plus.place(x=687, y=260)
    button_widgets.append(music_button_plus)

    sound_button_minus = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=1,
        border=3,
        text="-",
        font=('Small Fonts', 15, 'bold'),
        command=lambda: change_volume_sons("down")
    )
    sound_button_minus.place(x=570, y=310)
    button_widgets.append(sound_button_minus)

    sound_button_plus = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=1,
        border=3,
        text="+",
        font=('Small Fonts', 15, 'bold'),
        command=lambda: change_volume_sons("up")
    )
    sound_button_plus.place(x=687, y=310)
    button_widgets.append(sound_button_plus)
    
    language_button = tk.Button(
        Mafenetre,
        background='#bea48e',
        foreground='WHITE',
        activebackground='#7c645c',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bea48e',
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=3,
        text=languages_dic[parametres["language"]],
        font=('Small Fonts', 15, 'bold'),
        command=change_language
    )
    language_button.place(x=570, y=210)
    button_widgets.append(language_button)


    Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', 'menu_settings.ogg')))
    
# Fonction pour la gestion des fps
def change_fps():
    sound_manager.play_sound('button')
    if parametres["fps"]["mode"]==2:
        parametres["fps"]["mode"]=1
    else:
        parametres["fps"]["mode"]=2
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    create_settings_menu()

# Fonction pour la gestion des langues
def change_language():
    global languages, languages_dic
    sound_manager.play_sound('button')
    assert parametres["language"] in languages
    index_language=languages.index(parametres["language"])
    if index_language<len(languages)-1:
        index_language+=1
    else:
        index_language=0
    parametres["language"]=languages[index_language]
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    apply_language()
    create_settings_menu()

def change_volume_musique(direction):
    sound_manager.play_sound('button')
    if parametres["volume"]['musique']<20 and direction=="up":
        parametres["volume"]['musique']+=1
    elif parametres["volume"]['musique']>0 and direction=="down":
        parametres["volume"]['musique']-=1
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    music.set_volume(parametres["volume"]['musique'])
    create_settings_menu()

def change_volume_sons(direction):
    sound_manager.play_sound('button')
    if parametres["volume"]['sons']<20 and direction=="up":
        parametres["volume"]['sons']+=1
    elif parametres["volume"]['sons']>0 and direction=="down":
        parametres["volume"]['sons']-=1
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    sound_manager.set_volume(parametres["volume"]["sons"])
    create_settings_menu()

def change_show_fps():
    sound_manager.play_sound('button')
    parametres["fps"]["show"]=not parametres["fps"]["show"]
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
    create_settings_menu()

# Fonction pour remettre les paramètres à zéro
def reset_settings():
    sound_manager.play_sound('button')
    if messagebox.askyesno(lang.confirm, lang.reset_lang_confirm, icon="warning"):
        sound_manager.play_sound('button')
        parametres["controles"]["up"] = "Up"
        parametres["controles"]["left"] = "Left"
        parametres["controles"]["down"] = "Down"
        parametres["controles"]["right"] = "Right"
        parametres["controles"]["interact"] = "e"
        parametres["controles"]["reset"] = "r"
        parametres["controles"]["menu"] = "m"
        parametres["fps"]["mode"] = 2
        parametres["fps"]["show"] = True
        parametres["volume"]['musique'] = 10
        parametres["volume"]['sons'] = 10
        parametres["language"] = "fr"
        with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
            json.dump(parametres, fichier, indent=4)
        music.set_volume(parametres["volume"]['musique'])
        sound_manager.set_volume(parametres["volume"]["sons"])
        apply_language()
        create_settings_menu()
    else:
        sound_manager.play_sound('button')

#Menu des crédits
def credits_menu():
    global background_label, monde_buttons
    sound_manager.play_sound('button')
    if jeu.process_launched==True:
        return
    clear_canvas()
    clear_buttons_1()
    clear_bg()

    if background_label is None:
        background_image=game_images.main_menu_texture
        background_label = tk.Label(Mafenetre, image=background_image)
        background_label.place(x=0, y=0, width=800, height=600)
    
    monde_buttons = []
    return_button = tk.Button(
        Mafenetre,
        background='#bb7e4b',
        foreground='WHITE',
        activebackground='#714e31',
        activeforeground='WHITE',
        highlightthickness=2,
        highlightbackground='#bb7e4b',
        highlightcolor='WHITE',
        width=10,
        height=1,
        border=5,
        text=lang.back_button,
        font=('Small Fonts', 15, 'bold'),
        command=button_sound
    )
    return_button.place(x=625, y=525)
    monde_buttons.append(return_button)
    
    btn = tk.Button(Mafenetre, text="Killian", disabledforeground='WHITE',state="disabled", font=('Small Fonts', 15, 'bold'), height=1, borderwidth=0, background="black")
    btn.place(x=540, y=265)
    monde_buttons.append(btn)
    tooltip.ToolTip(btn, "Developer, Lead Editor Developer, Game Designer, Web Developer, Level Designer")
    
    btn = tk.Button(Mafenetre, text="Siméon", disabledforeground='WHITE',state="disabled", font=('Small Fonts', 15, 'bold'), height=1, borderwidth=0, background="black")
    btn.place(x=350, y=250)
    monde_buttons.append(btn)
    tooltip.ToolTip(btn, "Developer, Editor Developer, Lead Game Designer, Level Designer, Quality Assurance Tester")

    btn = tk.Button(Mafenetre, text="Kylian", disabledforeground='WHITE',state="disabled", font=('Small Fonts', 15, 'bold'), height=1, borderwidth=0, background="black")
    btn.place(x=175, y=300)
    monde_buttons.append(btn)
    tooltip.ToolTip(btn, "Lead Developer, Game Designer, Translator, Pixel Artist, Level Designer")

    btn = tk.Button(Mafenetre, text="Tristan", disabledforeground='WHITE',state="disabled", font=('Small Fonts', 15, 'bold'), height=1, borderwidth=0, background="black")
    btn.place(x=85, y=450)
    monde_buttons.append(btn)
    tooltip.ToolTip(btn, "Developer, Editor Developer, Lead Level Designer, Quality Assurance Tester")
    
    btn = tk.Button(Mafenetre, text="Malik", disabledforeground='WHITE',state="disabled", font=('Small Fonts', 15, 'bold'), height=1, borderwidth=0, background="black")
    btn.place(x=690, y=450)
    monde_buttons.append(btn)
    tooltip.ToolTip(btn, "Developer, Game Designer, Lead Web Developer, Level Designer")
        

def demarrer_niveau():
    jeu.temps_debut_niveau = time.time()
    jeu.niveau=1
    jeu.deplacements = 0
    jeu.deplacements_tot=0
    jeu.score=0

# 3 FONCTIONS DE DEROULEMENT POST NIVEAU
def attente_post_niveau():
    jeu.fini=True
    Canevas.after(500, affichage_ecran_transition)

def affichage_ecran_transition():
    clear_canvas()
    Canevas.configure(bg="black")
    score_1=round(jeu.score)
    if jeu.niveau==5:
        level=lang.end
    else:
        level=jeu.niveau+1
    Canevas.create_text(Largeur / 2, Hauteur / 2-30, text=lang.score+str(score_1), fill="white", font=("Small Fonts", "30", "bold"))
    Canevas.create_text(Largeur / 2, Hauteur / 2+30, text=lang.next_level+f"{jeu.numero_monde} - {level}", fill="white", font=("Small Fonts", "30", "bold"))
    Canevas.after(2000, mise_en_place_nouveau_niveau)

def mise_en_place_nouveau_niveau():
    clear_canvas()
    Canevas.configure(bg='#9b6b53')
    jeu.fini=False
    jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,0,0
    jeu.niveau=jeu.niveau+1
    jeu.marteau=0
    jeu.corde=0
    genere_niveau(jeu.niveau, jeu.numero_monde)
    periodic_canvas_update(True)

# Fonction pour commencer le jeu avec un niveau custom
def start_game_custom():
    global filepath
    sound_manager.play_sound('button')
    if jeu.process_launched==True:
        return
    
    #Remet le jeu à zéro
    jeu.fini=False
    filepath = filedialog.askopenfilename(title=lang.open_file, filetypes=[("JSON files", "*.json")])
    if not filepath:  # Regarde si l'utilisateur n'a pas choisi de fichier
        jeu.fini=True
        create_main_menu()
        return
    #Détruit le bouton et cache le fond d'écran
    clear_bg()
    clear_buttons_1()
    Mafenetre.title(f'{lang.game_name} - {filepath.split("/")[-1]}')
    try:
        genere_niveau(mode="Custom")
        periodic_canvas_update(True)
        Mafenetre.after(200, lambda: music.play_music(os.path.join(assets_dir, 'assets','mus', 'world_custom.ogg')))
    except Exception:
        
        jeu.fini=True
        create_main_menu()
        messagebox.showerror(lang.error, lang.corrupted)
        return

# Revient au menu principal après 3 secondes
def loop_back_to_menu(gamemode="Normal"):
    affiche_plateau_canvas()
    clear_buttons_1()
    if gamemode=="Custom":
        ms_time=500
    else:
        ms_time=3000
    Mafenetre.after(ms_time, create_main_menu)# Revient au menu principal après une attente

# Fonction pour tester si un niveau est terminé
def test_victoire():
    for i in range(12):
        for j in range(16):
            if plateau[i][j][3] == 1 and plateau[i][j][2] == 0:
                return False

    return True

# Fonction pour générer les niveaux
def genere_niveau(numero_niveau=1, numero_monde=1,mode="Normal",diff=1):
    global filepath
    jeu.difficulte=diff
    jeu.niveau =numero_niveau
    jeu.deplacements = 0
    jeu.haut,jeu.bas,jeu.gauche,jeu.droite=0,0,0,0
    for i in range(12):
        for j in range(16):
            plateau[i][j][0]=0
            plateau[i][j][1]=0
            plateau[i][j][2]=0
            plateau[i][j][3]=0
    if mode=="Normal":
        jeu.custom=0
        # Presence Discord
        if numero_niveau==6: # Remplacer cette valeur par 1 pour finir le monde instantanément
            affiche_ecran_fin(numero_monde)
            return
        try:
            with open(os.path.join(assets_dir, 'assets', 'niveaux', f'monde{numero_monde}', f'monde{numero_monde}_niveau{numero_niveau}.json'), 'r') as fichier:
                grille_chargee = json.load(fichier)
            Mafenetre.title(f'{lang.game_name} - {lang.level}{numero_monde}-{numero_niveau}')
        except Exception:
            jeu.fini=True
            create_main_menu()
            messagebox.showerror(lang.error, lang.error_opening)
            return
    else:
        jeu.custom=1
        jeu.temps_debut_niveau=time.time()
        with open(filepath, 'r') as fichier:
            grille_chargee = json.load(fichier)
    marteau=0
    corde=0
    for i in range(12):
        for j in range(16):
            if grille_chargee[i][j]==[1,0,0,0]:
                plateau[i][j][0]=1
            elif grille_chargee[i][j]==[0,0,1,0]:
                plateau[i][j][2]=1
            elif grille_chargee[i][j]==[0,0,0,1]:
                plateau[i][j][3]=1
            elif grille_chargee[i][j]==[0,1,0,0]:
                plateau[i][j][1]=1
            elif grille_chargee[i][j]==[0,2,0,0]:
                plateau[i][j][2]=3
            elif grille_chargee[i][j]==[0,0,2,0]:
                plateau[i][j][2]=4
            elif grille_chargee[i][j]==[0,3,0,0]:
                plateau[i][j][3]=9
            elif grille_chargee[i][j]==[0,0,3,0]:
                plateau[i][j][3]=8
            elif grille_chargee[i][j]==[0,4,0,0]:
                plateau[i][j][0]=2
            elif grille_chargee[i][j]==[0,0,4,0]:
                plateau[i][j][3]=5
                marteau+=1
            elif grille_chargee[i][j]==[0,5,0,0]:
                plateau[i][j][3]=6
                corde+=1
            elif grille_chargee[i][j]==[0,0,5,0]:
                plateau[i][j][2]=2
            
            # Check s'il faut afficher l'image de la corde/du marteau en bas à gauche
            if corde>0:
                jeu.corde_present=True
            else:
                jeu.corde_present=False
            if marteau>0:
                jeu.marteau_present=True
            else:
                jeu.marteau_present=False
    # Cache le curseur pendant le jeu
    Canevas.configure(cursor='none')
                
                
                

def affiche_ecran_fin(numero_monde):
    global parametres
    jeu.fini=True
    jeu.niveau = "FIN"
    murs_de_base()
    jeu.deplacements = jeu.deplacements_tot # remets les déplacements à 0 pour chaque niveau
        
    parametres["mondes"][f"monde_{numero_monde}_termine"] = True
    with open(os.path.join(settings_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
        
    # on efface le tableau
    for i in range(2,10):
        for j in range(2,14):
            plateau[i][j][0]=0
            plateau[i][j][1]=0
            plateau[i][j][2]=0
            plateau[i][j][3]=0
    music.stop_music()
    sound_manager.play_sound('big_win')
    loop_back_to_menu()

#Pour Rafraîchir l'image
def periodic_canvas_update(FirstTime=False):
    #Pour l'afficheur de fps en bas à droite
    def count_fps():
        if not jeu.fini:
            jeu.fps_print=jeu.fps
            jeu.fps=0
            Mafenetre.after(1000, count_fps)
    if FirstTime:
        count_fps()
    if not jeu.fini:
        Canevas.delete('all')
        affiche_plateau_canvas()
        jeu.fps+=1
        # Limiteur de FPS si la fenêtre n'a pas le focus
        if Mafenetre.focus_displayof() is not None:
            Mafenetre.after(jeu.mode_fps, periodic_canvas_update)
        else:
            Mafenetre.after(100, periodic_canvas_update)

# Affiche le plateau de jeu sur le canvas
def affiche_plateau_canvas():
    for i in range(12):
        for j in range(16):
            if (plateau[i][j][0] == 0):
                #affichage case vide
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.ground_texture, anchor='center')
            if (plateau[i][j][0]==1):
                #affichage mur
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.wall_texture, anchor='center')
            
            
            if plateau[i][j][2] == 3:
                #affichage portal bleu
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.blue_portal_texture, anchor='center')
            elif plateau[i][j][2] == 4:
                #affichage portal rouge
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.red_portal_texture, anchor='center')
                
            #affiche plaque de pression 
            if plateau[i][j][3] == 8:
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.Trapdoor_texture, anchor='center')
            #affiche porte fermée
            elif plateau[i][j][3] == 9:
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.Door_closed_texture, anchor='center')
            #affiche porte ouverte    
            elif plateau[i][j][3] == 10:
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.Door_open_texture, anchor='center')
                
            #affichache marteau
            if plateau[i][j][3] == 5 :
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.hammer_on_texture, anchor='center')
            
            #affichage mur fissuré
            if plateau[i][j][0] == 2:
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.wall_cracked_texture, anchor='center')
                
            #affichage corde
            if plateau[i][j][3] == 6 :
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.rope_on_texture, anchor='center')
            
            #affichage boite
            if plateau[i][j][2]== 2 :
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.box_texture, anchor='center')
                
            #affichage rocher dans un trou
            if plateau[i][j][2]==1 and plateau[i][j][3]==1:
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.crate_hole_texture, anchor='center')
                
            elif (plateau[i][j][1]==1):
                #affichage joueur
                if jeu.haut>=1:
                    if jeu.haut==1:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['haut'][1], anchor='center')
                    elif jeu.haut==2:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['haut'][0], anchor='center')
                    elif jeu.haut==3:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['haut'][2], anchor='center')
                    elif jeu.haut==4:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['haut'][0], anchor='center')
                    else:
                        jeu.haut=1
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['haut'][1], anchor='center')
                        
                elif jeu.bas>=1:
                    if jeu.bas==1:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][1], anchor='center')
                    elif jeu.bas==2:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][0], anchor='center')
                    elif jeu.bas==3:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][2], anchor='center')
                    elif jeu.bas==4:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][0], anchor='center')
                    else:
                        jeu.bas=1
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][1], anchor='center')
                elif jeu.gauche>=1:
                    if jeu.gauche==1:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['gauche'][1], anchor='center')
                    elif jeu.gauche==2:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['gauche'][0], anchor='center')
                    elif jeu.gauche==3:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['gauche'][2], anchor='center')
                    elif jeu.gauche==4:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['gauche'][0], anchor='center')
                    else:
                        jeu.gauche=1
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['gauche'][1], anchor='center')
                elif jeu.droite>=1:
                    if jeu.droite==1:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['droite'][1], anchor='center')
                    elif jeu.droite==2:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['droite'][0], anchor='center')
                    elif jeu.droite==3:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['droite'][2], anchor='center')
                    elif jeu.droite==4:
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['droite'][0], anchor='center')
                    else:
                        jeu.droite=1
                        Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['droite'][1], anchor='center')
                else:
                    Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.sisyphe_images['bas'][0], anchor='center')
            elif (plateau[i][j][2]==1):
                #affichage rocher
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.crate_texture, anchor='center')
            elif (plateau[i][j][3]==1):
                #affichage trou
                Canevas.create_image(50*j + 25, 50*i + 25, image=game_images.button_texture, anchor='center')
                
    # Afficher le niveau
    if jeu.custom>0:
        pass
    else:
        Canevas.create_text(402, 24, fill='black', font=("Small Fonts", "20"), text=lang.level+f"{jeu.numero_monde} - {jeu.niveau}", anchor='center') # Affiche le niveau
        Canevas.create_text(400, 22, fill='white', font=("Small Fonts", "20"), text=lang.level+f"{jeu.numero_monde} - {jeu.niveau}", anchor='center')
        
    # affichage icone marteau
    if jeu.marteau_present==True:
        MAX_USES_PER_HAMMER = 3
                
        # Calcule le nombre d'utilisations restantes pour le marteau
        full_hammers, remaining_uses = divmod(jeu.marteau, MAX_USES_PER_HAMMER)
                
        # Détermine la texture à afficher en fonction de l'état de durabilité du marteau
        if jeu.marteau==0:
            hammer_texture = game_images.hammer_off_texture
        elif remaining_uses == 1:
            hammer_texture = game_images.hammer_on_3_texture  # Texture pour 1 utilisation restante
        elif remaining_uses == 2:
            hammer_texture = game_images.hammer_on_2_texture  # Texture pour 2 utilisations restantes
        else:  # Cela veut dire que le marteau est neuf
            hammer_texture = game_images.hammer_on_1_texture  # Texture pour 3 utilisations restantes
                
        # Montre la texture du marteau
        Canevas.create_image(75, 575, image=hammer_texture, anchor='center')
                
        # Met à jour le texte avec le nombre d'utilisations du marteau
        total_hammers_display = full_hammers + 1 if remaining_uses > 0 else full_hammers  # + le marteau actuel s'il lui reste de la durabilité
                
        # Affiche le texte
        Canevas.create_text(92, 590, fill='black', font=("Small Fonts", "15"), text=total_hammers_display, anchor='center')
        Canevas.create_text(90, 588, fill='white', font=("Small Fonts", "15"), text=total_hammers_display, anchor='center')

    # affichage icone corde
    if jeu.corde_present==True:
        MAX_USES_PER_ROPE = 3
                
        # Calcule le nombre d'utilisations restantes pour la corde
        full_ropes, remaining_uses_2 = divmod(jeu.corde, MAX_USES_PER_ROPE)
                
        # Détermine la texture à afficher en fonction de l'état de durabilité de la corde
        if jeu.corde==0:
            rope_texture = game_images.rope_off_texture
        elif remaining_uses_2 == 1:
            rope_texture = game_images.rope_on_3_texture  # Texture pour 1 utilisation restante
        elif remaining_uses_2 == 2:
            rope_texture = game_images.rope_on_2_texture  # Texture pour 2 utilisations restantes
        else:  # Cela veut dire que le marteau est neuf
            rope_texture = game_images.rope_on_1_texture  # Texture pour 3 utilisations restantes
                
        # Montre la texture de la corde
        Canevas.create_image(25, 575, image=rope_texture, anchor='center')
                
        # Met à jour le texte avec le nombre d'utilisations de la corde
        total_ropes_display = full_ropes + 1 if remaining_uses_2 > 0 else full_ropes  # + la corde actuelle s'il lui reste de la durabilité
                
        # Affiche le texte
        Canevas.create_text(42, 590, fill='black', font=("Small Fonts", "15"), text=total_ropes_display, anchor='center')
        Canevas.create_text(40, 588, fill='white', font=("Small Fonts", "15"), text=total_ropes_display, anchor='center')

    # Afficher le compteur de déplacements
    Canevas.create_text(792, 24, fill='black', font=("Small Fonts", "20"), text=lang.moves+str(jeu.deplacements), anchor='e')
    Canevas.create_text(790, 22, fill='white', font=("Small Fonts", "20"), text=lang.moves+str(jeu.deplacements), anchor='e') # Affiche le nombre de déplacements
    if jeu.niveau=='FIN':
        Canevas.create_text(402,277,fill="black" ,font=("Small Fonts", "30", "bold"),text=lang.congrats_1, anchor='center')
        Canevas.create_text(400,275,fill="white" ,font=("Small Fonts", "30", "bold"),text=lang.congrats_1, anchor='center')
        Canevas.create_text(402,327, fill="black", font=("Small Fonts", "30", "bold"), text=lang.congrats_2+str(jeu.numero_monde)+lang.congrats_3, anchor='center')
        Canevas.create_text(400,325, fill="white", font=("Small Fonts", "30", "bold"), text=lang.congrats_2+str(jeu.numero_monde)+lang.congrats_3, anchor='center')
    # Afficher le temps écoulé
    temps_ecoule = round(time.time() - jeu.temps_debut_niveau)
    minutes = temps_ecoule // 60
    secondes = temps_ecoule % 60 #Pour convertir en Minutes les secondes
    Canevas.create_text(12, 24, fill='black', font=("Small Fonts", "20"), text=lang.time+f'{minutes}min {secondes}s', anchor='w')
    Canevas.create_text(10, 22, fill='white', font=("Small Fonts", "20"), text=lang.time+f'{minutes}min {secondes}s', anchor='w') # Affiche le temps écoulé à chaque déplacement
    if parametres["fps"]["show"]:
        Canevas.create_text(794, 584, fill='black', font=("Small Fonts", "15"), text=lang.fps+str(jeu.fps_print), anchor='e')
        Canevas.create_text(792, 582, fill='white', font=("Small Fonts", "15"), text=lang.fps+str(jeu.fps_print), anchor='e') # Affiche le niveau


def find_portal(plateau, portal_type): # fonction pour trouver le portail associé à un premier sur la grille
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j][2] == portal_type:
                return (i, j)
    return None  # Renvoie None si aucun portail n'est trouvé

def find_door(plateau): # fonction pour trouver la porte associée à une plaque de pression sur la grille
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j][3] == 9 or plateau[i][j][3] == 10 :
                return [i, j]
    return None  # Renvoie None si aucune porte n'est trouvé

def find_trapdoor(plateau): # fonction pour trouver la plaque de pression sur la grille
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j][3] == 8 :
                return [i, j]
    return None  # Renvoie None si aucune plaque de pression n'est trouvé

def on_shift_press(event):
    jeu.wait_next_key = True

def on_shift_release(event):
    jeu.wait_next_key = False

door_opened=0
def Clavier(event):
    """Gestion de l'évènement Appui sur une touche du clavier"""
    global parametres, door_opened
    if jeu.fini==False: #quand le jeu est fini on ne peux plus se deplacer
        #on efface le canevas
        
        mvt_poss=True
        touche= event.keysym
        if touche=="Up" or touche=="Left" or touche=="Right" or touche=="Down":
            pass
        else:
            touche=touche.lower()
            
        for i in range(12):
            for j in range(16):
                if (plateau[i][j][1]==1) and mvt_poss==True :
                    #Pour touche shift/controle
                    if jeu.wait_next_key:
                        if touche in [parametres["controles"]["up"], "Up"]:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=2,0,0,0
                        elif touche in [parametres["controles"]["down"], "Down"]:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,2,0,0
                        elif touche in [parametres["controles"]["left"], "Left"]:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,2,0
                        elif touche in [parametres["controles"]["right"], "Right"]:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,0,2
                        return
                        

                    direction = None
                    if touche in [parametres["controles"]["up"], "Up"]:
                        direction = (-1, 0)
                    elif touche in [parametres["controles"]["down"], "Down"]:
                        direction = (1, 0)
                    elif touche in [parametres["controles"]["left"], "Left"]:
                        direction = (0, -1)
                    elif touche in [parametres["controles"]["right"], "Right"]:
                        direction = (0, 1)
                    
                    # Si une direction de mouvement est définie
                    if direction:
                        new_i, new_j = i + direction[0], j + direction[1]
                        
                    # Vérification et ramassage de la corde
                        if plateau[new_i][new_j][3] == 6:  # Si la case de destination contient une corde
                            jeu.corde += 3  # Incrémente le nombre de cordes
                            plateau[new_i][new_j][3] = 0  # Retire la corde de la case
                            sound_manager.play_sound('powerup')
                            
                             #Tirage de rocher/boite
                    #si joueur va vers en haut
                    if touche==parametres["controles"]["interact"] and (plateau[i-1][j][2] == 1 or  plateau[i-1][j][2]== 2) and jeu.corde > 0 and plateau[i+1][j][2]!= 2 and plateau[i+1][j][2]!= 1 and plateau[i+1][j][0]!=2 and plateau[i+1][j][3]!=9 and plateau[i+1][j][0]!=1 and (plateau[i+1][j][2]!=3 and plateau[i+1][j][2]!=4) and plateau[i+1][j][3]!=1 and plateau[i][j][2]!=3 and plateau[i][j][2]!=4 and jeu.haut>0 :
                        if plateau[i-1][j][2] == 1 :
                            plateau[i-1][j][2] = 0
                            plateau[i][j][2] = 1
                            plateau[i][j][1] = 0
                            plateau[i+1][j][1] = 1
                        else :
                            plateau[i-1][j][2] = 0
                            plateau[i][j][2] = 2
                            plateau[i][j][1] = 0
                            plateau[i+1][j][1] = 1
                        sound_manager.play_sound('steps1')
                        jeu.corde -=1
                        jeu.deplacements += 1
                        direction = (1, 0)
                    #si joueur va vers en bas
                    if touche==parametres["controles"]["interact"] and (plateau[i+1][j][2] == 1 or  plateau[i+1][j][2]== 2) and jeu.corde > 0 and plateau[i-1][j][2]!= 2 and plateau[i-1][j][2]!= 1 and plateau[i-1][j][0]!=2 and plateau[i-1][j][3]!=9 and plateau[i-1][j][0]!=1 and (plateau[i-1][j][2]!=3 and plateau[i-1][j][2]!=4) and plateau[i-1][j][3]!=1 and plateau[i][j][2]!=3 and plateau[i][j][2]!=4 and jeu.bas>0:
                        if plateau[i+1][j][2] == 1 :
                            plateau[i+1][j][2] = 0
                            plateau[i][j][2] = 1
                            plateau[i][j][1] = 0
                            plateau[i-1][j][1] = 1
                        else :
                            plateau[i+1][j][2] = 0
                            plateau[i][j][2] = 2
                            plateau[i][j][1] = 0
                            plateau[i-1][j][1] = 1
                        sound_manager.play_sound('steps1')
                        jeu.corde -=1
                        jeu.deplacements += 1
                        direction = (-1, 0)
                    #si joueur va vers la gauche
                    if touche==parametres["controles"]["interact"] and (plateau[i][j-1][2] == 1 or  plateau[i][j-1][2]== 2) and jeu.corde > 0 and plateau[i][j+1][2]!= 2 and plateau[i][j+1][2]!= 1 and plateau[i][j+1][0]!=2 and plateau[i][j+1][3]!=9 and plateau[i][j+1][0]!=1 and (plateau[i][j+1][2]!=3 and plateau[i][j+1][2]!=4) and plateau[i][j+1][3]!=1 and plateau[i][j][2]!=3 and plateau[i][j][2]!=4 and jeu.gauche>0:
                        if plateau[i][j-1][2] == 1 :
                            plateau[i][j-1][2] = 0
                            plateau[i][j][2] = 1
                            plateau[i][j][1] = 0
                            plateau[i][j+1][1] = 1
                        else :
                            plateau[i][j-1][2] = 0
                            plateau[i][j][2] = 2
                            plateau[i][j][1] = 0
                            plateau[i][j+1][1] = 1
                        sound_manager.play_sound('steps1')
                        jeu.corde -=1
                        jeu.deplacements += 1
                        direction = (0, 1)
                    #si joueur va vers la droite
                    if touche==parametres["controles"]["interact"] and (plateau[i][j+1][2] == 1 or  plateau[i][j+1][2]== 2) and jeu.corde > 0 and plateau[i][j-1][2]!= 2 and plateau[i][j-1][2]!= 1 and plateau[i][j-1][0]!=2 and plateau[i][j-1][3]!=9 and plateau[i][j-1][0]!=1 and (plateau[i][j-1][2]!=3 and plateau[i][j-1][2]!=4) and plateau[i][j-1][3]!=1 and plateau[i][j][2]!=3 and plateau[i][j][2]!=4 and jeu.droite>0:
                        if plateau[i][j+1][2] == 1 :
                            plateau[i][j+1][2] = 0
                            plateau[i][j][2] = 1
                            plateau[i][j][1] = 0
                            plateau[i][j-1][1] = 1
                        else :
                            plateau[i][j+1][2] = 0
                            plateau[i][j][2] = 2
                            plateau[i][j][1] = 0
                            plateau[i][j-1][1] = 1
                        sound_manager.play_sound('steps1')
                        jeu.corde -=1
                        jeu.deplacements += 1
                        direction = (0, -1)
                        
                        
                    # Si une direction de mouvement est définie
                    if direction:
                        new_i, new_j = i + direction[0], j + direction[1]
                        
                        # Vérification et ramassage du marteau
                        if plateau[new_i][new_j][3] == 5:  # Si la case de destination contient un marteau
                            jeu.marteau += 3  # Incrémente le nombre de marteaux
                            plateau[new_i][new_j][3] = 0  # Retire le marteau de la case
                            sound_manager.play_sound('powerup')
                        
                        #Destruction mur fissuré
                    #si joueur va vers en haut
                    if touche==parametres["controles"]["interact"] and plateau[i-1][j][0] == 2 and jeu.marteau > 0 and jeu.haut>0 :
                        plateau[i-1][j][0] = 0
                        jeu.marteau -=1
                        sound_manager.play_sound('break')
                    #si joueur va vers en bas
                    if touche==parametres["controles"]["interact"] and plateau[i+1][j][0] == 2 and jeu.marteau > 0 and jeu.bas>0:
                        plateau[i+1][j][0] = 0
                        jeu.marteau -=1
                        sound_manager.play_sound('break')
                    #si joueur va vers la gauche
                    if touche==parametres["controles"]["interact"] and plateau[i][j-1][0] == 2 and jeu.marteau > 0 and jeu.gauche>0:
                        plateau[i][j-1][0] = 0
                        jeu.marteau -=1
                        sound_manager.play_sound('break')
                    #si joueur va vers la droite
                    if touche==parametres["controles"]["interact"] and plateau[i][j+1][0] == 2 and jeu.marteau > 0 and jeu.droite>0:
                        plateau[i][j+1][0] = 0
                        jeu.marteau -=1
                        sound_manager.play_sound('break')
                              
                    # Si le joueur est sur le point de rentrer dans un portail
                    if touche in [parametres["controles"]["up"], parametres["controles"]["left"], parametres["controles"]["right"], parametres["controles"]["down"]]:
                        # Détermine la direction basée sur la touche pressée
                        destination_i, destination_j = i, j
                        if touche == parametres["controles"]["up"]:
                            destination_i -= 1
                        elif touche == parametres["controles"]["down"]:
                            destination_i += 1
                        elif touche == parametres["controles"]["left"]:
                            destination_j -= 1
                        elif touche == parametres["controles"]["right"]:
                            destination_j += 1
                    
                        # Regarde si la destination du joueur est un portail
                        if plateau[destination_i][destination_j][2] in [3, 4]:  # Portail détecté
                            portal_type = plateau[destination_i][destination_j][2]
                            other_portal_type = 4 if portal_type == 3 else 3  # Détermine l'autre portail
                            other_portal_coords = find_portal(plateau, other_portal_type)  # Trouve l'autre portail
                    
                            if other_portal_coords:
                                # Téléporte le joueur
                                plateau[i][j][1] = 0
                                i, j = other_portal_coords
                                plateau[i][j][1] = 1
                                jeu.haut,jeu.bas,jeu.gauche,jeu.droite=0,0,0,0
                                sound_manager.play_sound('portal')
                                return

                    if touche==parametres["controles"]["up"]:
                        if  plateau[i-1][j][0]!=2 and plateau[i-1][j][3]!=9 and plateau[i-1][j][2]!= 2 and plateau[i-1][j][0]!=1 and (plateau[i-1][j][2]!=3 and plateau[i-1][j][2]!=4) and plateau[i-1][j][3]!=1 and not (plateau[i-1][j][2]==1 and (plateau[i-2][j][2]==1 or plateau[i-2][j][0]==1 or plateau[i-2][j][2]==3 or plateau[i-2][j][2]==4 or plateau[i-2][j][3]==9 or plateau[i-2][j][0]==2 or plateau[i-2][j][2]== 2)):
                            if plateau[i-1][j][2]==1:
                                plateau[i-2][j][2]=1
                                plateau[i-1][j][2]=0
                                if plateau[i-2][j][3]==1 and not (test_victoire()==True):
                                    sound_manager.play_sound('hole_filled')
                            plateau[i][j][1]=0
                            plateau[i-1][j][1]=1
                            jeu.deplacements += 1  # Incrémentation du compteur de déplacements
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=jeu.haut+1,0,0,0
                            if jeu.haut%2==0:
                                sound_manager.play_sound('steps2')
                            else:
                                sound_manager.play_sound('steps1')
                        else:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=2,0,0,0
                    elif touche==parametres["controles"]["left"]:
                        if plateau[i][j-1][0]!=2 and plateau[i][j-1][3]!=9 and plateau[i][j-1][2]!= 2 and plateau[i][j-1][0]!=1 and (plateau[i][j-1][2]!=3 and plateau[i][j-1][2]!=4) and plateau[i][j-1][3]!=1 and not (plateau[i][j-1][2]==1 and (plateau[i][j-2][2]==1 or plateau[i][j-2][0]==1  or plateau[i][j-2][2]==3 or plateau[i][j-2][2]==4 or plateau[i][j-2][3]==9 or plateau[i][j-2][0]==2 or plateau[i][j-2][2]== 2)):
                            if plateau[i][j-1][2]==1:
                                plateau[i][j-2][2]=1
                                plateau[i][j-1][2]=0
                                if plateau[i][j-2][3]==1 and not (test_victoire()==True):
                                    sound_manager.play_sound('hole_filled')
                            plateau[i][j][1]=0
                            plateau[i][j-1][1]=1
                            jeu.deplacements += 1  # Incrémentation du compteur de déplacements
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,jeu.gauche+1,0
                            if jeu.gauche%2==0:
                                sound_manager.play_sound('steps2')
                            else:
                                sound_manager.play_sound('steps1')
                        else:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,2,0
                    elif touche==parametres["controles"]["right"]:
                        if plateau[i][j+1][0]!=2 and plateau[i][j+1][3]!=9 and plateau[i][j+1][2]!= 2 and plateau[i][j+1][0]!=1 and (plateau[i][j+1][2]!=3 and plateau[i][j+1][2]!=4) and plateau[i][j+1][3]!=1 and not (plateau[i][j+1][2]==1 and (plateau[i][j+2][2]==1 or plateau[i][j+2][0]==1  or plateau[i][j+2][2]==3 or plateau[i][j+2][2]==4 or plateau[i][j+2][3]==9 or plateau[i][j+2][0]==2 or plateau[i][j+2][2]== 2)):
                            if plateau[i][j+1][2]==1:
                                plateau[i][j+2][2]=1
                                plateau[i][j+1][2]=0
                                if plateau[i][j+2][3]==1 and not (test_victoire()==True):
                                    sound_manager.play_sound('hole_filled')
                            plateau[i][j][1]=0
                            plateau[i][j+1][1]=1
                            jeu.deplacements += 1  # Incrémentation du compteur de déplacements
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,0,jeu.droite+1
                            if jeu.droite%2==0:
                                sound_manager.play_sound('steps1')
                            else:
                                sound_manager.play_sound('steps2')
                        else:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,0,2
                    elif touche==parametres["controles"]["down"]:
                        if plateau[i+1][j][0]!=2 and plateau[i+1][j][3]!=9 and plateau[i+1][j][2]!= 2 and plateau[i+1][j][0]!=1 and (plateau[i+1][j][2]!=3 and plateau[i+1][j][2]!=4) and plateau[i+1][j][3]!=1 and not (plateau[i+1][j][2]==1 and (plateau[i+2][j][2]==1 or plateau[i+2][j][0]==1  or plateau[i+2][j][2]==3 or plateau[i+2][j][2]==4 or plateau[i+2][j][3]==9 or plateau[i+2][j][0]==2 or plateau[i+2][j][2]== 2)):
                            if plateau[i+1][j][2]==1:
                                plateau[i+2][j][2]=1
                                plateau[i+1][j][2]=0
                                if plateau[i+2][j][3]==1 and not (test_victoire()==True):
                                    sound_manager.play_sound('hole_filled')
                            jeu.deplacements += 1  # Incrémentation du compteur de déplacements
                            plateau[i][j][1]=0
                            plateau[i+1][j][1]=1
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,jeu.bas+1,0,0
                            if jeu.bas%2==0:
                                sound_manager.play_sound('steps1')
                            else:
                                sound_manager.play_sound('steps2')
                        else:
                            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,2,0,0
                        #deplacements vers plaque de pression / porte
                    # si rocher sur la plaque
                    trapdoor_pos = find_trapdoor(plateau)
                    door_pos = find_door(plateau)
                    if trapdoor_pos != None and door_pos != None :
                        if plateau[trapdoor_pos[0]][trapdoor_pos[1]][3] == 8 and plateau[trapdoor_pos[0]][trapdoor_pos[1]][2] == 1 :
                            plateau[door_pos[0]][door_pos[1]][3] = 10
                            if door_opened==0:
                                sound_manager.play_sound('door')
                                door_opened+=1
                        # si rien sur la plaque
                        else :
                            trapdoor_pos = find_trapdoor(plateau)
                            door_pos = find_door(plateau)
                            plateau[door_pos[0]][door_pos[1]][3] = 9
                            if door_opened>0:
                                sound_manager.play_sound('door2')
                                door_opened=0
                    # si rocher sur la porte fermée
                    trapdoor_pos = find_trapdoor(plateau)
                    door_pos = find_door(plateau)
                    if trapdoor_pos != None and door_pos != None :
                        if plateau[door_pos[0]][door_pos[1]][3] == 9 and (plateau[door_pos[0]][door_pos[1]][2] == 1 or plateau[door_pos[0]][door_pos[1]][2] == 2):
                            plateau[door_pos[0]][door_pos[1]][2] = 0
                    mvt_poss=False #pour ne pas se déplacer plusieurs cases à la fois
        if touche==parametres["controles"]["reset"]:
            sound_manager.play_sound('reset')
            jeu.haut, jeu.bas, jeu.gauche, jeu.droite=0,0,0,0
            jeu.marteau = 0
            jeu.corde = 0
            door_opened=0
            if jeu.custom>0:
                genere_niveau(mode="Custom")
            else:
                genere_niveau(jeu.niveau, jeu.numero_monde)
        elif touche==parametres["controles"]["menu"]:
            sound_manager.play_sound('menu')
            jeu.marteau = 0
            jeu.corde = 0
            door_opened=0
            jeu.fini=True
            music.stop_music()
            create_main_menu()
        #le cas échéant on change de niveau:
        if (test_victoire()==True):
            if jeu.custom >0:
                jeu.fini=True
                music.stop_music()
                sound_manager.play_sound('small_win')
                loop_back_to_menu("Custom")
            else:
                jeu.deplacements_tot+=jeu.deplacements
                jeu.score+=((1500*jeu.difficulte/10)//((jeu.deplacements//10)+1))*10
                door_opened=0
                sound_manager.play_sound('small_win')
                affiche_plateau_canvas()
                attente_post_niveau()

# Création du Canvas
Largeur = 800
Hauteur = 600
Canevas = tk.Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='#9b6b53')
Canevas.configure(highlightthickness=0)
Canevas.grid(row=0, column=0)
Canevas.focus_set()
Canevas.bind('<Key>', Clavier)
Canevas.bind('<Shift_L>', on_shift_press)
Canevas.bind('<Shift_R>', on_shift_press)
Canevas.bind('<KeyRelease-Shift_L>', on_shift_release)
Canevas.bind('<KeyRelease-Shift_R>', on_shift_release)
Canevas.bind('<Control_L>', on_shift_press)
Canevas.bind('<Control_R>', on_shift_press)
Canevas.bind('<KeyRelease-Control_L>', on_shift_release)
Canevas.bind('<KeyRelease-Control_R>', on_shift_release)





Mafenetre.bind("<Tab>", lambda event: "break")
Mafenetre.bind("<Shift-Tab>", lambda event: "break")

# Commence le jeu avec le menu principal
create_main_menu()

# Boucle
Mafenetre.mainloop()