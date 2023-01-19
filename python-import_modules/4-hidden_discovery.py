#!/usr/bin/python3
if __name__ == "__main__":
    import statistics
    import hidden_4 as a
    # On crée une variable "j" le module importé "a"
    j = dir(a)
    for i in range(len(j)):
        # On vérifie si le premier caractère de chaque élément est _.
        if j[i][0] == '_':
            # Si oui, l'élément est ignoré,
            continue
        # Sinon il est affiché à l'écran.
        print("{}".format(j[i]))
