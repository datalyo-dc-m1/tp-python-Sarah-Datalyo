# Recherche une valeur dans un tableau d'entier

search_val = int(input("Saisir un entier à rechercher:"))

tableau = [4, 10, 9, 1, 12]

taille_tableau = len(tableau)
is_found = False

for element in tableau:
    if search_val == element:
        is_found = True
        break  # l'instruction break permet de sortir de la boucle
if is_found:
    print("Vrai")
else:
    print("Faux")
