students_data = {
    "Анна": [5, 4, 5, 5, 4],
    "Богдан": [3, 4, 3, 3, 4],
    "Вікторія": [5, 5, 5, 5, 5],
    "Дмитро": [4, 3, 4, 4, 5]
}

average_scores = {}
all_grades_list = []

for name, grades in students_data.items():
    avg = sum(grades) / len(grades)
    average_scores[name] = round(avg, 2)
    all_grades_list.extend(grades)

unique_grades = set(all_grades_list)

print(f"Словник середніх балів: {average_scores}")
print(f"Унікальні оцінки (set): {unique_grades}")