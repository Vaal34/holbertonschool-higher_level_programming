#!/usr/bin/python3
"""Script Python pour afficher les états de la table
"states" d'une base de données MySQL triés par ID.
"""
from sys import argv    # importe le module argv du module sys
import MySQLdb    # importe la bibliothèque MySQLdb

# établit une connexion à la base de données MySQL en utilisant
# les arguments passés au script
# (nom d'utilisateur, mot de passe, nom de la base de données)
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

# crée un objet curseur pour interagir avec la base de données
cur = db.cursor()

# exécute une requête SQL pour sélectionner
# toutes les lignes de la table "states" et les trier par ID
cur.execute("SELECT * FROM states ORDER BY states.id")

# récupère les résultats de la requête sous forme de liste de tuples

rows = cur.fetchall()

for row in rows:
    print(row)
# ferme le curseur et la connexion à la base de données

cur.close()
db.close()
