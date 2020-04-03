# Calcule les racines réelles d'un polynôme du second degré

from math import sqrt  # import de la librairie math

a = float(input("Saisir la valeur de a: "))
b = float(input("Saisir la valeur de b: "))
c = float(input("Saisir la valeur de c: "))

equation = f"{a}x^2+{b}x+{c}=0"
discrimant = (b * b) - (4 * a * c)

if discrimant > 0:
    discrimant_sqrt = sqrt(discrimant)
    solution1 = - (b + discrimant_sqrt) / (2 * a)
    solution2 = - (b - discrimant_sqrt) / (2 * a)
    print(f"{discrimant} > 0")
    print(f"{equation} a deux solutions réelles: x1={solution1} &  x2={solution2}")

elif discrimant == 0:
    solution = - b / (2 * a)
    print(f"{discrimant} = 0")
    print(f"{equation} a une unique solution réelle: x={solution}")

else:
    print(f"{discrimant} < 0")
    print(f"{equation} n'a pas de solution réeelle")
