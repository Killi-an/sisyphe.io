# -*- coding: utf-8 -*-
import pygame

pygame.mixer.init()

# Variable globale pour garder en mémoire le chemin de la dernière musique jouée
current_music_path = None

def play_music(path):
    global current_music_path
    # Regarde si la musique que l'on essaie de jouer est différente de celle qui se joue
    if path != current_music_path:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)  # Boucle infinie
        current_music_path = path  # Met à jour la musique actuelle

def stop_music():
    global current_music_path
    if current_music_path is not None:
        pygame.mixer.music.stop()
        current_music_path = None  # Remet à zéro la musique actuelle

# Pour changer le volume de la musique
def set_volume(volume):
    volume=volume*5 # La variable volume allant de 1 à 20, il faut multiplier par 5 pour trouver sa valeur en pourcentage
    volume=volume/100 # La valeur du volume dans pygame est comprise entre 0.0 et 1.0
    pygame.mixer.music.set_volume(volume)
    
def get_volume():
    return pygame.mixer.music.get_volume()

class SoundManager:
    def __init__(self):
        # Dictionnaire avec tous les sons du jeu
        self.sounds = {}

    def load_sound(self, name, path):
        # Ajoute le son dans le dictionnaire
        self.sounds[name] = pygame.mixer.Sound(path)

    def play_sound(self, name):
        # Joue un son
        if name in self.sounds:
            self.sounds[name].play()

    def set_volume(self, volume):
        # Met le volume de tous les sons comme voulu dans les paramètres
        volume=volume*5 # La variable volume allant de 1 à 20, il faut multiplier par 5 pour trouver sa valeur en pourcentage
        volume=volume/100 # La valeur du volume dans pygame est comprise entre 0.0 et 1.0
        for sound in self.sounds.values():
            sound.set_volume(volume)
    def get_volume(self, name):
        assert name in self.sounds.keys(), "Le son rentré n'est pas valide"
        return self.sounds[name].get_volume()