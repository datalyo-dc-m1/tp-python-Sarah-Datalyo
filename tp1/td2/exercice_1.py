# Permute deux éléments d'un tableau

liste = [1, 2, 3, 4, 5]

print("Liste avant la permutation:")
print(liste)

tampon = liste[0]  # on stocke la valeur du 1er élément dans une variable "tampon"
liste[0] = liste[3]  # on affecte la valeur 4 au premier élément du tableau
liste[3] = tampon  # on affecte la valeur 1 au 4ème élément du tableau

print("Liste après permutation de 1 et 4:")
print(liste)
