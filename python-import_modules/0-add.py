#!/usr/bin/python3
# Ce bloc de code ne sera exécuté que lorsque le script est exécuté directement.
if __name__ == "__main__":
    # Importation du module add_0 avec le nom add
    from add_0 import add
    # déclaration des variables a, b avec leurs valeurs respectives
    a = 1
    b = 2
    # affiche le résultat de l'addition des deux variables avec l'utilisation de la fonction add du module add_0
    print("{} + {} = {}".format(a, b, add(a, b)))
