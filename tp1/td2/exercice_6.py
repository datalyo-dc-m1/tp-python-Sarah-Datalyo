# Détecte si un mot est un palindrome

un_mot = "kayak"

nb_lettres = len(un_mot)
est_palindrome = True

for i in range(0, nb_lettres):  # Rq: pour optimiser la boucle, on peut parcourir uniquement la moitié du mot
    if not un_mot[i] == un_mot[nb_lettres - 1 - i]:
        est_palindrome = False
        break

print(f"{un_mot} est-il un palindrome? Réponse: {est_palindrome}")


# Avec une boucle TantQue

un_autre_mot = "kay3ak"

i = 0
est_palindrome = True

while i < nb_lettres and est_palindrome:
    est_palindrome = un_autre_mot[i] == un_autre_mot[nb_lettres - 1 - i]
    i += 1

print(f"{un_autre_mot} est-il un palindrome? Réponse: {est_palindrome}")
