# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import os


db_path=os.path.join(os.environ['LOCALAPPDATA'], 'Sisyphe.io', 'scores.db')

# Fonction pour initialiser la base de données, la créer si ce n'est pas déjà le cas et y insérer les tables
def init_database():
    global db_path
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS world_1 (
        id INTEGER PRIMARY KEY,
        score INTEGER,
        date TEXT
    );
    """)
    
    c.execute("""CREATE TABLE IF NOT EXISTS world_2 (
        id INTEGER PRIMARY KEY,
        score INTEGER,
        date TEXT
    );
    """)
    
    c.execute("""CREATE TABLE IF NOT EXISTS world_3 (
        id INTEGER PRIMARY KEY,
        score INTEGER,
        date TEXT
    );
    """)
              
    c.execute("""CREATE TABLE IF NOT EXISTS world_4 (
        id INTEGER PRIMARY KEY,
        score INTEGER,
        date TEXT
    );
    """)
    
    c.execute("""CREATE TABLE IF NOT EXISTS world_5 (
        id INTEGER PRIMARY KEY,
        score INTEGER,
        date TEXT
    );
    """)

# Fonction pour sauvegarder une valeur dans notre base de données (utilisée à la fin de chaque monde, avec l'heure à laquelle le monde a été terminé)
def save_value_to_database(score, world_number):
    global db_path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    column_name = f"world_{world_number}"
    query = f"INSERT INTO {column_name} (score, date) VALUES (?, ?)" # Requête sql
    date = datetime.now().strftime('%d-%m-%Y %H:%M')  # Date et heure
    try:
        cursor.execute(query, (score, date))
        conn.commit()
    except sqlite3.Error as e:
        print("Erreur dans la sauvegarde de score :", e)
    cursor.close()
    conn.close()

# Fonction qui renvoie le meilleur score et sa date correspondante pour le monde passé en paramètres
def get_highest_score_and_date(world_number):
    global db_path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    column_name = f"world_{world_number}"
    query = f"SELECT score, date FROM {column_name} ORDER BY score DESC LIMIT 1"
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            highest_score, date = result
            return highest_score, date
        else:
            return None, None
    except sqlite3.Error as e:
        print("Erreur dans le renvoi de score :", e)
        return None, None
    finally:
        cursor.close()
        conn.close()

# Fonction qui supprime le contenu des bases (pour réinitialiser sa sauvegarde)
def wipe_table_contents():
    try:
        global db_path
        
        # Connexion à la base de données
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Liste des noms des tables
        table_names = ['world_1', 'world_2', 'world_3', 'world_4', 'world_5']
        
        # Pour chaque table, supprime le contenu
        for table_name in table_names:
            cursor.execute(f"DELETE FROM {table_name};")
        
        # Confirme les changements
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print("Erreur dans la suppression du contenu des tables :", e)
