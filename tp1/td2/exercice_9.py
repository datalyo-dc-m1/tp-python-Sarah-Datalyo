# Trie un tableau d'entiers par ordre croissant

tableau = [1, 2, 53, 10, 9, 27, 10, 67]

print(f"Tableau à trier: {tableau}")

tableau_trie = []
tampon = tableau.copy()

for i in range(0, len(tableau)):

    minimum = tampon[0]

    for j in range(0, len(tampon)):
        if tampon[j] < minimum:
            minimum = tampon[j]

    tableau_trie.append(minimum)
    tampon.remove(minimum)

print(f"Tableau trié: {tableau_trie}")
