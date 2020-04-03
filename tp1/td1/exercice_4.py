# Demande à l'utilisateur un nombre n compris entre 0 et 100 puis affiche les n premiers entiers

iteration = int(input("Saisir un entier entre 0 et 100: "))

if iteration < 0 or iteration > 100:
    print(f"{iteration} n'est pas compris entre 0 et 100!")
else:
    for i in range(iteration):
        print(i)
