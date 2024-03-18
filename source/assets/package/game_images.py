# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
import os

base_path=None

class GameImages:
    def __init__(self):
        self.sisyphe_images = self.load_character_images('sisyphe', ['bas', 'haut', 'gauche', 'droite'], 3)
        self.ground_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'ground.png'))
        self.wall_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'wall.png'))
        self.crate_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'crate.png'))
        self.button_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'button.png'))
        self.blue_portal_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'blue_portal.png'))
        self.red_portal_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'red_portal.png'))
        
        self.main_menu_texture = self.load_menu(os.path.join(base_path, 'assets', 'img', 'menus', 'bg.png'))
        self.world_menu_texture = self.load_menu(os.path.join(base_path, 'assets', 'img', 'menus', 'bg_world.png'))

        self.settings_menu_texture = self.load_menu(os.path.join(base_path, 'assets', 'img', 'menus', 'bg_settings.png'))
        self.logo_texture = self.load_logo(os.path.join(base_path, 'assets', 'img', 'menus', 'sisyphe.png'))
        
        self.Trapdoor_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'trapdoor.png'))
        self.Door_closed_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'door_closed.png'))
        self.Door_open_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'door_open.png'))
        self.crate_hole_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'crate_hole.png'))
        self.wall_cracked_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'wall_cracked.png'))
        self.box_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'box.png'))
        
        self.hammer_off_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'hammer_off.png'))
        self.hammer_on_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'hammer_on.png'))
        self.hammer_on_1_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'hammer_on_1.png'))
        self.hammer_on_2_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'hammer_on_2.png'))
        self.hammer_on_3_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'hammer_on_3.png'))
        
        self.rope_on_1_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'rope_on_1.png'))
        self.rope_on_2_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'rope_on_2.png'))
        self.rope_on_3_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'rope_on_3.png'))
        self.rope_off_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'rope_off.png'))
        self.rope_on_texture = self.load_texture(os.path.join(base_path, 'assets', 'img', 'blocs', 'rope_on.png'))

    def load_texture(self, path):
        image = Image.open(path)
        image = image.resize((50, 50), Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    
    def load_menu(self, path):
        image= Image.open(path)
        image = image.resize((800,600), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def load_logo(self, path):
        image= Image.open(path)
        image = image.resize((300,64), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def load_character_images(self, character_name, directions, count):
        textures = {}
        for direction in directions:
            textures[direction] = []
            for i in range(1, count + 1):
                path = os.path.join(base_path, 'assets', 'img', 'char', f'{character_name}_{direction}_{i}.png')
                textures[direction].append(self.load_texture(path))
        return textures
