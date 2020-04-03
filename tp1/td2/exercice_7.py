# Calcule la moyenne des étudiants
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

print(f"Résultats des étudiants: {averages}")
