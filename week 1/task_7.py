students = [
    {"name": "Андрій", "surname": "Коваленко", "grades": [4, 5, 4, 5, 3]},
    {"name": "Олена",  "surname": "Бондар",    "grades": [5, 5, 5, 5, 5]},
    {"name": "Іван",   "surname": "Ткаченко",  "grades": [3, 4, 3, 3, 4]},
    {"name": "Марія",  "surname": "Шевченко",  "grades": [5, 4, 5, 5, 4]}
]

subjects = ["Матем", "Фізика", "Історія", "Прог.", "Англ."]
num_subjects = 5
group_subject_sums = [0] * num_subjects

print(f"{'Прізвище':<12} {'Імя':<10} | {'Середній бал':<10}")
print("-" * 40)

for s in students:
    student_avg = sum(s["grades"]) / num_subjects
    print(f"{s['surname']:<12} {s['name']:<10} | {student_avg:.2f}")

    for i in range(num_subjects):
        group_subject_sums[i] += s["grades"][i]

print("-" * 40)
print("Середній бал групи по предметах:")
for i in range(num_subjects):
    avg_subject = group_subject_sums[i] / len(students)
    print(f"{subjects[i]}: {avg_subject:.2f}")