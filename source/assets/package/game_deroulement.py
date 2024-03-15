# -*- coding: utf-8 -*-

class GameDeroulement:
    def __init__(self):
        self.score=0 # Système de score
        self.fini=True
        self.niveau=1 # Système de niveau
        self.numero_monde=0
        self.deplacements=0
        self.deplacements_tot=0 # Système de compte des déplacements
        self.temps_debut_niveau=0 # Système de temps écoulé
        self.difficulte=0 # Système de difficulté pour score
        self.marteau = 0 # Système pour l'objet marteau
        self.marteau_present = False
        self.corde = 0 #Système pour l'objet corde
        self.corde_present = False
        self.custom=0 # Système de génération de niveaux custom
        self.process_launched=False
        self.wait_next_key=False
        
        self.fps=0
        self.fps_print=0
        self.mode_fps=30
        
        self.haut,self.bas,self.gauche,self.droite=0,1,0,0
        
