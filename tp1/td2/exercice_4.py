# Calcule la moyenne d'un élève

grades = [4.0, 10.5, 19, 20, 13.8]

grades_count = len(grades)
grades_sum = 0

for grade in grades:
    grades_sum += grade
average = grades_sum / grades_count

print(f"La moyenne est: {average}")
