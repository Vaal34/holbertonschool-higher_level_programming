#!/usr/bin/python3
"""  lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
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
    cur.execute("SELECT name FROM states WHERE name LIKE '%N'")

    # récupère les résultats de la requête sous forme de liste de tuples

    rows = cur.fetchall()

    for row in rows:
        print(row)
    # ferme le curseur et la connexion à la base de données

    cur.close()
    db.close()