# Afficher les éléments d'un tableau 2D
import numpy as np

tableau_2d = np.array([[1, 2, 3], [4, 5, 6]])

taille_tableau = np.shape(tableau_2d)  # donne la taille d'un tableau 2D
nb_lignes = taille_tableau[0]
nb_colonnes = taille_tableau[1]

print(f"Taille du tableau: {taille_tableau}")

for i in range(0, nb_lignes):
    for j in range(0, nb_colonnes):
        print(tableau_2d[i][j])
