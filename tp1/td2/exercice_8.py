# Calcule la moyenne de la classe
import numpy as np

grades = np.array([[10, 12.5, 6], [19, 18.5, 16], [14, 13.5, 17]])

grades_len = np.shape(grades)
total_students = grades_len[0]
total_grades = grades_len[1]

averages = []  # liste vide pour stoker les moyennes

for i in range(0, total_students):

    sum_grades = 0

    for j in range(0, total_grades):
        sum_grades += grades[i, j]

    averages.append(sum_grades / total_grades)

# Calcul de la moyenne

sum_student_avg = 0

for student_avg in averages:
    sum_student_avg += student_avg

classroom_avg = sum_student_avg / total_students

print(f"Moyenne de la classe: {classroom_avg}")
