# Calculatrice

left = int(input("Saisir un nombre: "))
right = int(input("Saisir un second nombre: "))
operator = input(f"Choisir une opération à effectuer entre {left} et {right} ( + , - , * , / ): ")

if operator not in ['+', '-', '*', '/']:
    print(f"{operator} n'est pas une opération valide!")
else:
    if operator == '+':
        print(f"{left} + {right} = {left + right}")
    elif operator == '-':
        print(f"{left} - {right} = {left - right}")
    elif operator == '*':
        print(f"{left} * {right} = {left * right}")
    elif operator == '/':
        if right == 0:  # On vérifie que l'opération est valide
            print(f"{left} n'est pas divisible par {right}!")
        else:
            print(f"{left} / {right} = {left / right}")
