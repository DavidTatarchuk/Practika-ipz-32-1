import pandas as pd

data = {
    'Прізвище': ['Коваленко', 'Бондар', 'Ткаченко', 'Шевченко'],
    'Імя': ['Андрій', 'Олена', 'Іван', 'Марія'],
    'Матем': [4, 5, 3, 5],
    'Фізика': [5, 5, 4, 4],
    'Історія': [4, 5, 3, 5],
    'Прог': [5, 5, 3, 5],
    'Англ': [3, 5, 4, 4]
}

df_initial = pd.DataFrame(data)
df_initial.to_csv('students.csv', index=False)

df = pd.read_csv('students.csv')

subjects = ['Матем', 'Фізика', 'Історія', 'Прог', 'Англ']

df['Середній бал'] = df[subjects].mean(axis=1)

print(df[['Прізвище', 'Імя', 'Середній бал']])
print("-" * 40)
print("Середній бал групи по предметах:")
print(df[subjects].mean())