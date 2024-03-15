# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog # pour pouvoir sélectionner le fichier à ouvrir
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

# Musique de l'Éditeur
import package.game_music as music

# Langue de l'Éditeur
import package.game_lang as langue

sound_manager = music.SoundManager()

#Chemin vers le fichier
base_path = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Sisyphe.io')

#parametres du jeu
with open(os.path.join(target_dir, 'settings.json'), 'r') as fichier:
    parametres = json.load(fichier)

#asserts pour le fichier json
required_keys = ["controles", "mondes", "tutoriels", "fps", "volume", "language"]
for key in required_keys:
    assert key in parametres, f"Valeur manquante : {key}"

#langue du jeu
lang = langue.Traduction()

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
    global functions_dic
    assert parametres["language"] in functions_dic.keys()
    for elt in functions_dic.keys():
        if elt==parametres["language"]:
            functions_dic[elt]()
            return
apply_language()

# Nom du fichier en cours d'édition
filepath=""
file_opened=lang.editor_new_file

# Titre de la fenêtre avec fichier en cours d'édition
    
Mafenetre = tk.Tk()
Mafenetre.title(f"{lang.editor_title} - {file_opened}")
Mafenetre.iconbitmap(os.path.join(base_path, 'img', 'icons', 'editor_tskbr.ico'))
Mafenetre.resizable(False, False)

# Sons du jeu
sound_manager.load_sound('steps1', os.path.join(base_path, 'sfx', 'footsteps1.wav'))
sound_manager.load_sound('steps2', os.path.join(base_path, 'sfx', 'footsteps2.wav'))
sound_manager.load_sound('small_win', os.path.join(base_path, 'sfx', 'level_completed.wav'))
sound_manager.load_sound('hole_filled', os.path.join(base_path, 'sfx', 'hole_filled.wav'))
sound_manager.load_sound('portal', os.path.join(base_path, 'sfx', 'portal_entered.wav'))
sound_manager.load_sound('powerup', os.path.join(base_path, 'sfx', 'powerup_taken.wav'))
sound_manager.load_sound('break', os.path.join(base_path, 'sfx', 'wall_broken.wav'))
sound_manager.load_sound('door', os.path.join(base_path, 'sfx', 'door_opened.wav'))
sound_manager.load_sound('button', os.path.join(base_path, 'sfx', 'button_pressed.wav'))
sound_manager.load_sound('reset', os.path.join(base_path, 'sfx', 'reset_level.wav'))

#Image de Sisyphe
sisyphe_image = Image.open(os.path.join(base_path, 'img', 'char', 'sisyphe_bas_1.png'))  # Chemin vers l'image
sisyphe_image = sisyphe_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
sisyphe_texture = ImageTk.PhotoImage(sisyphe_image)

# Image du chemin
ground_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'ground.png'))  # Chemin vers l'image
ground_image = ground_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
ground_texture = ImageTk.PhotoImage(ground_image)

# Image des murs
wall_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'wall.png'))  # Chemin vers l'image
wall_image = wall_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
wall_texture = ImageTk.PhotoImage(wall_image)

# Image des rochers
crate_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'crate.png'))  # Chemin vers l'image
crate_image = crate_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
crate_texture = ImageTk.PhotoImage(crate_image)

# Image des rochers
button_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'button.png'))  # Chemin vers l'image
button_image = button_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
button_texture = ImageTk.PhotoImage(button_image)

# Image des portails
bportal_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'blue_portal.png'))  # Chemin vers l'image
bportal_image = bportal_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
bportal_texture = ImageTk.PhotoImage(bportal_image)

rportal_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'red_portal.png'))  # Chemin vers l'image
rportal_image = rportal_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
rportal_texture = ImageTk.PhotoImage(rportal_image)

#Images de la plaque de pression et de la porte
door_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'door_closed.png'))  # Chemin vers l'image
door_image = door_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
door_texture = ImageTk.PhotoImage(door_image)

trapdoor_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'trapdoor.png'))  # Chemin vers l'image
trapdoor_image = trapdoor_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
trapdoor_texture = ImageTk.PhotoImage(trapdoor_image)

#Images du marteau et du mur fragile
fwall_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'wall_cracked.png'))  # Chemin vers l'image
fwall_image = fwall_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
fwall_texture = ImageTk.PhotoImage(fwall_image)

hammer_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'hammer_on.png'))  # Chemin vers l'image
hammer_image = hammer_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
hammer_texture = ImageTk.PhotoImage(hammer_image)

#Image de la corde
rope_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'rope_on.png'))  # Chemin vers l'image
rope_image = rope_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
rope_texture = ImageTk.PhotoImage(rope_image)

#Image de la caisse
box_image = Image.open(os.path.join(base_path, 'img', 'blocs', 'box.png'))  # Chemin vers l'image
box_image = box_image.resize((50, 50), Image.LANCZOS)  # Redimensionne l'image
box_texture = ImageTk.PhotoImage(box_image)

# Plateau de l'éditeur
plateau = [[[0] * 4 for _ in range(16)] for _ in range(12)]

Largeur = 800
Hauteur = 600
Canevas = tk.Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='grey')
Canevas.grid(row=0, column=0)

frame_elements = tk.Frame(Mafenetre)
frame_elements.grid(row=0, column=1)

unsaved_changes = False

element_type = tk.IntVar()

textures=False

# Variables pour les différents objets sélectionnables
wall_selected = tk.IntVar()
boulder_selected = tk.IntVar()
hole_selected = tk.IntVar()
player_selected = tk.IntVar()
blue_portal_selected = tk.IntVar()
red_portal_selected = tk.IntVar()
door_selected = tk.IntVar()
trapdoor_selected = tk.IntVar()
fwall_selected=tk.IntVar()
hammer_selected=tk.IntVar()
rope_selected=tk.IntVar()
box_selected=tk.IntVar()
delete_selected = tk.IntVar()

# Fonctions pour sélectionner les objets
def uncheck_all():
    wall_selected.set(0)
    boulder_selected.set(0)
    hole_selected.set(0)
    player_selected.set(0)
    blue_portal_selected.set(0)
    red_portal_selected.set(0)
    door_selected.set(0)
    trapdoor_selected.set(0)
    fwall_selected.set(0)
    hammer_selected.set(0)
    rope_selected.set(0)
    box_selected.set(0)
    delete_selected.set(0)

def select_wall(event=None):
    uncheck_all()
    wall_selected.set(1)
    element_type.set(1)

def select_boulder(event=None):
    uncheck_all()
    boulder_selected.set(1)
    element_type.set(2)

def select_hole(event=None):
    uncheck_all()
    hole_selected.set(1)
    element_type.set(3)

def select_player(event=None):
    uncheck_all()
    player_selected.set(1)
    element_type.set(4)
    
def select_portal_blue(event=None):
    uncheck_all()
    blue_portal_selected.set(1)
    element_type.set(5)

def select_portal_red(event=None):
    uncheck_all()
    red_portal_selected.set(1)
    element_type.set(6)
    
def select_door(event=None):
    uncheck_all()
    door_selected.set(1)
    element_type.set(7)

def select_trapdoor(event=None):
    uncheck_all()
    trapdoor_selected.set(1)
    element_type.set(8)

def select_fwall(event=None):
    uncheck_all()
    fwall_selected.set(1)
    element_type.set(9)

def select_hammer(event=None):
    uncheck_all()
    hammer_selected.set(1)
    element_type.set(10)

def select_rope(event=None):
    uncheck_all()
    rope_selected.set(1)
    element_type.set(11)

def select_box(event=None):
    uncheck_all()
    box_selected.set(1)
    element_type.set(12)

def select_delete(event=None):
    uncheck_all()
    delete_selected.set(1)
    element_type.set(0)

# Affectation de touches à ces fonctions
Mafenetre.bind('w', select_wall)
Mafenetre.bind('W', select_wall)

Mafenetre.bind('x', select_boulder)
Mafenetre.bind('X', select_boulder)

Mafenetre.bind('c', select_hole)
Mafenetre.bind('C', select_hole)

Mafenetre.bind('b', select_player)
Mafenetre.bind('B', select_player)

Mafenetre.bind('q', select_portal_blue)
Mafenetre.bind('Q', select_portal_blue)

Mafenetre.bind('s', select_portal_red)
Mafenetre.bind('S', select_portal_red)

Mafenetre.bind('d', select_door)
Mafenetre.bind('D', select_door)

Mafenetre.bind('f', select_trapdoor)
Mafenetre.bind('F', select_trapdoor)

Mafenetre.bind('g', select_fwall)
Mafenetre.bind('G', select_fwall)

Mafenetre.bind('h', select_hammer)
Mafenetre.bind('H', select_hammer)

Mafenetre.bind('j', select_rope)
Mafenetre.bind('J', select_rope)

Mafenetre.bind('v', select_box)
Mafenetre.bind('V', select_box)

Mafenetre.bind('<BackSpace>', select_delete)

# Affectation de touches aux commandes de manipulation des niveaux
Mafenetre.bind_all('<Control-n>', lambda event: new_level())
Mafenetre.bind_all('<Control-o>', lambda event: open_level())
Mafenetre.bind_all('<Control-s>', lambda event: save())
Mafenetre.bind_all('<Control-Shift-s>', lambda event: save_as())
Mafenetre.bind_all('<Control-t>', lambda event: toggle_textures())
Mafenetre.bind_all('<Control-u>', lambda event: toggle_music())
Mafenetre.bind_all('<Control-i>', lambda event: toggle_sounds())

Mafenetre.bind_all('<Control-N>', lambda event: new_level())
Mafenetre.bind_all('<Control-O>', lambda event: open_level())
Mafenetre.bind_all('<Control-S>', lambda event: save())
Mafenetre.bind_all('<Control-Shift-S>', lambda event: save_as())
Mafenetre.bind_all('<Control-T>', lambda event: toggle_textures())
Mafenetre.bind_all('<Control-U>', lambda event: toggle_music())
Mafenetre.bind_all('<Control-I>', lambda event: toggle_sounds())

# Fonction pour afficher ou non les vraies textures du jeu
def toggle_textures():
    global textures
    textures=not textures
    affiche_plateau_canvas()
    
def toggle_music():
    if music.get_volume()!=0:
        music.set_volume(0)
    else:
        music.set_volume(parametres["volume"]["musique"])

def toggle_sounds():
    if sound_manager.get_volume("button")!=0:
        sound_manager.set_volume(0)
    else:
        sound_manager.set_volume(parametres["volume"]["sons"])
        

# Force un mur sur le contour de l'éditeur
def initialize_walls():
    for i in range(12):
        plateau[i][0][0] = 1
        #plateau[i][1][0] = 1
        #plateau[i][14][0] = 1
        plateau[i][15][0] = 1
        
    for j in range(16):
        plateau[0][j][0] = 1
        #plateau[1][j][0] = 1
        #plateau[10][j][0] = 1
        plateau[11][j][0] = 1

# Permet de placer l'objet sélectionné sur le canvas
def place_element(event):
    global element_type, unsaved_changes
    row, col = get_selected_cell(event)
    if element_type.get() == 0:
        delete(row, col)
    if element_type.get() == 1 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_wall(row, col)
    elif element_type.get() == 2 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_boulder(row, col)
    elif element_type.get() == 3 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_switch(row, col)
    elif element_type.get() == 4 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_player(row, col)
    elif element_type.get() == 5 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_portal_blue(row,col)
    elif element_type.get() == 6 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_portal_red(row,col)
    elif element_type.get() == 7 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_door(row,col)
    elif element_type.get() == 8 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_trapdoor(row,col)
    elif element_type.get() == 9 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_fwall(row,col)
    elif element_type.get() == 10 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_hammer(row,col)
    elif element_type.get() == 11 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_rope(row,col)
    elif element_type.get() == 12 and plateau[row][col][0]==0 and plateau[row][col][1]==0 and plateau[row][col][2]==0 and plateau[row][col][3]==0:
        place_box(row,col)
    unsaved_changes = True
    affiche_plateau_canvas()

# Permet de stocker les coordonnées de la case sur laquelle on a cliqué
def get_selected_cell(event):
    x = Canevas.canvasx(event.x)
    y = Canevas.canvasy(event.y)
    row = int(y / 50)
    col = int(x / 50)
    return row, col

# Fonctions appelées par "place_element(event)" afin d'effectuer la bonne action
def delete(row, col):
    if plateau[row][col][0] != 0 or plateau[row][col][1] != 0 or plateau[row][col][2] != 0 or plateau[row][col][3] != 0:
        sound_manager.play_sound('reset')
        plateau[row][col][0] = 0
        plateau[row][col][1] = 0
        plateau[row][col][2] = 0
        plateau[row][col][3] = 0

def place_wall(row, col):
    sound_manager.play_sound('button')
    plateau[row][col][0] = 1

def place_boulder(row, col):
    sound_manager.play_sound('steps1')
    plateau[row][col][2] = 1

def place_switch(row, col):
    sound_manager.play_sound('hole_filled')
    plateau[row][col][3] = 1

def place_portal_blue(row, col):
    already=False
    for i in range(12):
        for j in range(16):
            if plateau[i][j][1]==2:
                already=True
    if already==False:
        sound_manager.play_sound('portal')
        plateau[row][col][1] = 2

def place_portal_red(row, col):
    already=False
    for i in range(12):
        for j in range(16):
            if plateau[i][j][2]==2:
                already=True
    if already==False:
        sound_manager.play_sound('portal')
        plateau[row][col][2] = 2

def place_door(row, col):
    already=False
    for i in range(12):
        for j in range(16):
            if plateau[i][j][1]==3:
                already=True
    if already==False:
        sound_manager.play_sound('door')
        plateau[row][col][1] = 3
        
def place_trapdoor(row, col):
    already=False
    for i in range(12):
        for j in range(16):
            if plateau[i][j][2]==3:
                already=True
    if already==False:
        sound_manager.play_sound('door')
        plateau[row][col][2] = 3

def place_fwall(row, col):
    sound_manager.play_sound('break')
    plateau[row][col][1] = 4

def place_hammer(row, col):
    sound_manager.play_sound('powerup')
    plateau[row][col][2] = 4

def place_rope(row, col):
    sound_manager.play_sound('powerup')
    plateau[row][col][1] = 5

def place_box(row, col):
    sound_manager.play_sound('steps2')
    plateau[row][col][2] = 5

def place_player(row, col):
    already=False
    for i in range(12):
        for j in range(16):
            if plateau[i][j][1]==1:
                already=True
    if already==False:
        sound_manager.play_sound('small_win')
        plateau[row][col][1] = 1

# Affichage global du canvas
def affiche_plateau_canvas():
    global textures, unsaved_changes, file_opened
    Canevas.delete('all')
    for i in range(12):
        Canevas.create_line(0,50*i,800,50*i,width=0.5)
    for j in range(16):
        Canevas.create_line(50*j,0,50*j,600,width=0.5)
    initialize_walls()
    for row in range(12):
        for col in range(16):
            # Sol
            if plateau[row][col][0] == 0 and textures==True:
                Canevas.create_image(50*col + 25, 50*row + 25, image=ground_texture, anchor='center')
            # Mur
            if plateau[row][col][0] == 1:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=wall_texture, anchor='center')
                else:
                    Canevas.create_rectangle(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='blue')
            # Joueur
            elif plateau[row][col][1] == 1:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=sisyphe_texture, anchor='center')
                else:
                    Canevas.create_oval(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='yellow')
            # Rocher
            elif plateau[row][col][2] == 1:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=crate_texture, anchor='center')
                else:
                    Canevas.create_oval(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='#804000')
            # Trou
            elif plateau[row][col][3] == 1:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=button_texture, anchor='center')
                else:
                    #Canevas.create_oval(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='red')
                    y = 50*row +25
                    x = 50*col +25
                    couleur ='black'         #CHANGEZ MOI pour modifier la couleur du trou dans l'editeur de lvl
                    epaisseur = 3                 #CHANGEZ MOI pour l'eapissseur des fleches
                    #rond central
                    Canevas.create_oval(x-13, y-13, x+13, y+13, fill=couleur)

                    #fleche haut droite
                    Canevas.create_line(x+24, y-24, x+12, y-12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x+12, y-12, x+19, y-12,  fill=couleur, width=epaisseur)
                    Canevas.create_line(x+12, y-12, x+12, y-19,  fill=couleur, width=epaisseur)
                    #Flèche haut gauche
                    Canevas.create_line(x-24, y-24, x-12, y-12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x-12, y-12, x-19, y-12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x-12, y-12, x-12, y-19, fill=couleur, width=epaisseur)

                    #Fleche bas droite
                    Canevas.create_line(x+24, y+24, x+12, y+12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x+12, y+12, x+19, y+12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x+12, y+12, x+12, y+19, fill=couleur, width=epaisseur)

                    #Fleche bas gauche
                    Canevas.create_line(x-24, y+24, x-12, y+12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x-12, y+12, x-19, y+12, fill=couleur, width=epaisseur)
                    Canevas.create_line(x-12, y+12, x-12, y+19, fill=couleur, width=epaisseur)    
            # Portail Bleu
            elif plateau[row][col][1] == 2:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=bportal_texture, anchor='center')
                else:
                    Canevas.create_oval(50 * col+5, 50 * row, 50 * col + 45, 50 * row + 50, fill='cyan')
            # Portail Rouge
            elif plateau[row][col][2] ==2:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=rportal_texture, anchor='center')
                else:
                    Canevas.create_oval(50 * col+5, 50 * row, 50 * col + 45, 50 * row + 50, fill='#ff3333')
            # Porte
            elif plateau[row][col][1] ==3:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=door_texture, anchor='center')
                else:
                    Canevas.create_rectangle(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='lime')
            # Plaque de pression
            elif plateau[row][col][2] ==3:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=trapdoor_texture, anchor='center')
                else:
                    Canevas.create_oval(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='lime')
            # Mur Fragile
            elif plateau[row][col][1] ==4:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=fwall_texture, anchor='center')
                else:
                    Canevas.create_rectangle(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='magenta')
            # Marteau
            elif plateau[row][col][2] ==4:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=hammer_texture, anchor='center')
                else:
                    y = 50 * row + 43
                    x = 50 * col + 25
                    
                    handle_length = 30
                    handle_thickness = 2 
                    head_width = 20
                    head_height = 10
                    couleur = '#804000'
                    
                    # Base du marteau
                    Canevas.create_line(x, y, x, y - handle_length, fill=couleur, width=handle_thickness)
                    
                    # Tête du marteau
                    head_start_x = x - head_width // 2
                    head_start_y = y - handle_length - head_height // 2
                    head_end_x = head_start_x + head_width
                    head_end_y = head_start_y + head_height
                    Canevas.create_rectangle(head_start_x, head_start_y, head_end_x, head_end_y, fill=couleur)
                    Canevas.create_rectangle(head_start_x, head_start_y, head_end_x, head_end_y, fill=couleur)
            # Corde
            elif plateau[row][col][1] ==5:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=rope_texture, anchor='center')
                else:
                    y = 50*row +25
                    x = 50*col +25
                    Canevas.create_line(x-20, y-20, x+20, y+20, fill='#804000', width=5)
            # Caisse
            elif plateau[row][col][2] ==5:
                if textures==True:
                    Canevas.create_image(50*col + 25, 50*row + 25, image=box_texture, anchor='center')
                else:
                    y = 50*row +25
                    x = 50*col +25
                    Canevas.create_rectangle(50 * col, 50 * row, 50 * col + 50, 50 * row + 50, fill='#804000')
                    Canevas.create_line(x-25, y-25, x+25, y+25, fill='black', width=3)
                    Canevas.create_line(x+25, y-25, x-25, y+25, fill='black', width=3)
    if unsaved_changes==True:
        fenetre_title=f"{lang.editor_title} - {file_opened}"
        Mafenetre.title(fenetre_title+"*")
                    

# Bouton Nouveau
def new_level():
    global plateau, unsaved_changes, file_opened, filepath
    # Vérifie si les modifications ont été enregistrées
    if unsaved_changes:
        if messagebox.askyesno(lang.unsaved_title, lang.unsaved, icon="warning"):
            unsaved_changes=False
            new_level()
            return
        else:
            return
    plateau = [[[0] * 4 for _ in range(16)] for _ in range(12)]
    unsaved_changes = False
    
    # Titre du niveau
    file_opened=lang.editor_new_file
    filepath=""
    Mafenetre.title(f"{lang.editor_title} - {file_opened}")
    affiche_plateau_canvas()

# Bouton Ouvrir
def open_level():
    global unsaved_changes, file_opened, filepath
    # Vérifie si les modifications ont été enregistrées
    if unsaved_changes:
        if messagebox.askyesno(lang.unsaved_title, lang.unsaved, icon="warning"):
            unsaved_changes=False
            open_level()
            return
        else:
            return
    filepath = filedialog.askopenfilename(title=lang.open_file, filetypes=[("JSON files", "*.json")])
    if not filepath:  # L'utilisateur n'a rien choisi
        return
    try:
        with open(filepath, 'r') as infile:
            global plateau
            loaded_data = json.load(infile)
            plateau = loaded_data
            unsaved_changes = False
            
            # Titre du niveau
            file_opened=filepath.split("/")[-1]
            Mafenetre.title(f"{lang.editor_title} - {file_opened}")

            affiche_plateau_canvas()
    except Exception:
        messagebox.showerror(lang.error, lang.corrupted)
        new_level()

# Bouton Enregistrer...
def save():
    global unsaved_changes, filepath, file_opened
    if not_valid():
        return
    if not filepath:  # Regarde si l'utilisateur a choisi un nom de fichier
        filepath = filedialog.asksaveasfilename(initialfile=file_opened, defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'w') as outfile:
                json.dump(plateau, outfile)
            unsaved_changes = False
            
            # Titre du niveau
            file_opened=filepath.split("/")[-1]
            Mafenetre.title(f"{lang.editor_title} - {file_opened}")
        except Exception as e:
            messagebox.showerror(lang.error, lang.error_opening+str(e))

# Bouton Enregistrer sous...
def save_as():
    global unsaved_changes, filepath, file_opened
    if not_valid():
        return
    filepath2 = filedialog.asksaveasfilename(initialfile=file_opened, defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filepath2:  # Regarde si l'utilisateur a choisi un nom de fichier
        try:
            filepath=filepath2
            with open(filepath, 'w') as outfile:
                json.dump(plateau, outfile)
            unsaved_changes = False
            
            # Titre du niveau
            file_opened=filepath.split("/")[-1]
            Mafenetre.title(f"{lang.editor_title} - {file_opened}")
        except Exception as e:
            messagebox.showerror(lang.error, lang.error_opening+str(e))

# Détection de changements afin de ne pas pouvoir fermer par erreur sans avoir sauvegardé
def confirm_close():
    global unsaved_changes
    if unsaved_changes:
        if messagebox.askyesno(lang.unsaved_title, lang.unsaved, icon="warning"):
            music.stop_music()
            Mafenetre.destroy()
    else:
        music.stop_music()
        Mafenetre.destroy()

def not_valid():
    error=""
    
    #Met des variables pour chaque type d'objet à vérifier
    player=False
    portal_blue=False
    portal_red=False
    door=False
    trapdoor=False
    button=0
    crate=0
    
    # Boucle qui compte les différents objets obligatoires
    for i in range(12):
        for j in range(16):
            if plateau[i][j][1]==1:
                player=True
            elif plateau[i][j][1]==2:
                portal_blue=True
            elif plateau[i][j][2]==2:
                portal_red=True
            elif plateau[i][j][1]==3:
                door=True
            elif plateau[i][j][2]==3:
                trapdoor=True
            elif plateau[i][j][2]==1:
                crate+=1
            elif plateau[i][j][3]==1:
                button+=1
                
    # Met un message d'erreur si l'une des conditions n'est pas remplie
    if player==False:
        error=lang.error_player
    elif button==0 or crate==0 or button>crate:
        error=lang.error_boulder
    elif portal_blue==True and portal_red==False or portal_blue==False and portal_red==True:
        error=lang.error_portal
    elif door==True and trapdoor==False or door==False and trapdoor==True:
        error=lang.error_door
        
    if error!="":
        messagebox.showerror(lang.error, lang.error_not_valid+str(error))
        return True
    return False

# Création de la barre au dessus de l'éditeur
menu_bar = tk.Menu(Mafenetre)
Mafenetre.config(menu=menu_bar)
Mafenetre.protocol("WM_DELETE_WINDOW", confirm_close)

# Création des cases de cette barre
file_menu = tk.Menu(menu_bar, tearoff=0)
edition_menu = tk.Menu(menu_bar, tearoff=0)
textures_menu = tk.Menu(menu_bar, tearoff=0)
music_menu = tk.Menu(menu_bar, tearoff=0)

# Création des sous-menus d'Édition
basic_objects_menu = tk.Menu(edition_menu, tearoff=0)
special_objects_menu = tk.Menu(edition_menu, tearoff=0)

menu_bar.add_cascade(label=lang.file_menu, menu=file_menu)
menu_bar.add_cascade(label=lang.edition_menu, menu=edition_menu)
menu_bar.add_cascade(label=lang.textures_menu, menu=textures_menu)
menu_bar.add_cascade(label=lang.music_menu, menu=music_menu)

# Création des options de la case "Fichier"
file_menu.add_command(label=lang.new_button, command=new_level, accelerator="Ctrl+N")
file_menu.add_command(label=lang.open_button, command=lambda: open_level(), accelerator="Ctrl+O")
file_menu.add_command(label=lang.save_button, command=save, accelerator="Ctrl+S")
file_menu.add_command(label=lang.save_as_button, command=save_as, accelerator="Ctrl+Shift+S")
file_menu.add_command(label=lang.leave_button, command=confirm_close, accelerator="ALT+F4")

# Création des options de la case "Textures"
textures_menu.add_command(label=lang.toggle_textures_button, command=toggle_textures, accelerator="Ctrl+T")

# Création des options de la case "Musique & Sons"
music_menu.add_command(label=lang.toggle_music_button, command=toggle_music, accelerator="Ctrl+U")
music_menu.add_command(label=lang.toggle_sounds_button, command=toggle_sounds, accelerator="Ctrl+I")

# Création des options de la case "Edition"
#Menu Basique
basic_objects_menu.add_checkbutton(label=lang.select_wall, variable=wall_selected, command=select_wall, accelerator="W")
basic_objects_menu.add_checkbutton(label=lang.select_boulder, variable=boulder_selected, command=select_boulder, accelerator="X")
basic_objects_menu.add_checkbutton(label=lang.select_hole, variable=hole_selected, command=select_hole, accelerator="C")
basic_objects_menu.add_checkbutton(label=lang.select_box, variable=box_selected, command=select_box, accelerator="V")
basic_objects_menu.add_checkbutton(label=lang.select_player, variable=player_selected, command=select_player, accelerator="B")

#Menu Spécial
special_objects_menu.add_checkbutton(label=lang.select_portal1, variable=blue_portal_selected, command=select_portal_blue, accelerator="Q")
special_objects_menu.add_checkbutton(label=lang.select_portal2, variable=red_portal_selected, command=select_portal_red, accelerator="S")
special_objects_menu.add_checkbutton(label=lang.select_door, variable=door_selected, command=select_door, accelerator="D")
special_objects_menu.add_checkbutton(label=lang.select_pressure_plate, variable=trapdoor_selected, command=select_trapdoor, accelerator="F")
special_objects_menu.add_checkbutton(label=lang.select_cracked_wall, variable=fwall_selected, command=select_fwall, accelerator="G")
special_objects_menu.add_checkbutton(label=lang.select_hammer, variable=hammer_selected, command=select_hammer, accelerator="H")
special_objects_menu.add_checkbutton(label=lang.select_rope, variable=rope_selected, command=select_rope, accelerator="J")

#Ajout des sous-menus dans le menu Edition
edition_menu.add_cascade(label=lang.base_objects, menu=basic_objects_menu)
edition_menu.add_cascade(label=lang.special_objects, menu=special_objects_menu)

#Ajout du mode suppression
edition_menu.add_separator()
edition_menu.add_checkbutton(label=lang.delete_mode, variable=delete_selected, command=select_delete, accelerator=lang.return_key)

# Permet de détecter le clic de l'utilisateur
Canevas.bind('<Button-1>', place_element)

select_wall()
affiche_plateau_canvas()

with open(os.path.join(target_dir, 'settings.json'), 'r') as fichier:
    parametres = json.load(fichier)

music.set_volume(parametres["volume"]["musique"])
sound_manager.set_volume(parametres["volume"]["sons"])


Mafenetre.after(200, lambda: music.play_music(os.path.join(base_path, 'mus', 'editor.ogg')))

if not parametres["tutoriels"]["tutoriel_editeur_termine"]:
    messagebox.showinfo(lang.editor_tutorial_title, lang.editor_tutorial)
    parametres["tutoriels"]["tutoriel_editeur_termine"]=True
    with open(os.path.join(target_dir, 'settings.json'), 'w') as fichier:
        json.dump(parametres, fichier, indent=4)
#Boucle
Mafenetre.mainloop()
