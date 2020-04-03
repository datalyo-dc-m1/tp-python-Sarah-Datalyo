# Renvoie le plus petit élément d'un tableau

liste = [4, 10, 9, 1, 12]
print(liste)

taille_liste = len(liste)
minimum = liste[0]

for i in range(1, taille_liste):
    current_val = liste[i]
    if current_val < minimum:
        minimum = current_val

print(f"Le minimum du tableau est: {minimum}")
