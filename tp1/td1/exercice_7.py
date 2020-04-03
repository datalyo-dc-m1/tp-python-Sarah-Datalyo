# Estime la valeur de Pi par la méthode de Monte-Carlo

from random import random  # import de la librairie random qui permet de tirer des nombres aléatoires

nb_tirages = 1000000
nb_points_dans_cercle = 0

for i in range(0, nb_tirages):

    x = random()
    y = random()
    distance = x * x + y * y

    if distance <= 1:
        nb_points_dans_cercle += 1


pi_estime = nb_points_dans_cercle / nb_tirages * 4

print(f"Pour {nb_tirages} tirages, l'estimation de pi est: {pi_estime}")
