# Demande un nombre n à l'utilisateur puis calcule la somme des n premiers nombres impairs

iteration = int(input("Saisir un entier strictement positif: "))

if iteration < 0:
    print(f"{iteration} n'est pas strictement positif !")
else:
    somme = 0
    for i in range(1, iteration * 2, 2):
        somme += i
    print(f"La somme des {iteration} premiers entiers impairs est: {somme}")


#  Une autre solution possible

iteration = int(input("Saisir un entier strictement positif: "))

if iteration < 0:
    print(f"{iteration} n'est pas strictement positif !")
else:
    somme = 0
    i = 0
    while i < iteration:
        somme += i * 2 + 1
        i += 1
    print(f"La somme des {iteration} premiers entiers impairs est: {somme}")
