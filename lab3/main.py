import pandas as pd
import re
import os

# --- 1. ЗАВАНТАЖЕННЯ АБО СТВОРЕННЯ ДАНИХ ---
if os.path.exists("jobs.csv"):
    df = pd.read_csv("jobs.csv")
    print("Файл jobs.csv завантажено")
else:
    print("Файл не знайдено → створюю тестові дані")

    data = {
        'Job Title': ['Cloud Engineer', 'Data Scientist', 'AI Engineer', 'Backend Developer', 'DevOps Engineer'],
        'Industry': ['Cloud Computing', 'IT', 'AI', 'IT', 'Cloud Computing'],
        'Experience Level': ['Senior', 'Junior', 'Senior', 'Middle', 'Senior'],
        'Employment Type': ['Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Full-Time'],
        'Location': ['Kyiv', 'Lviv', 'Kyiv', 'Odesa', 'Kyiv'],
        'Salary Range': ['50000-80000', '30000-50000', '70000-120000', '40000-60000', '60000-90000'],
        'Date Posted': ['2023-01-01', '2022-05-10', '2023-07-15', '2021-03-20', '2023-09-01']
    }

    df = pd.DataFrame(data)

# --- 1. ПЕРВИННИЙ АНАЛІЗ ---
print("\nПерші 5 рядків:")
print(df.head())

print("\nОстанні 5 рядків:")
print(df.tail())

print("\nРозмір:", df.shape)

print("\nПам'ять:")
print(df.memory_usage(deep=True))


# --- 2. АНАЛІЗ ---
print("\nТипи даних:")
print(df.dtypes)

print("\nПропуски:")
print(df.isnull().sum())


# --- 3. ФІЛЬТРАЦІЯ ---
print("\nCloud:")
print(df[df['Industry'].str.contains('Cloud', na=False)])

print("\nSenior:")
print(df[df['Experience Level'].str.contains('Senior', na=False)])

print("\nFull-Time Kyiv:")
print(df[
    (df['Employment Type'].str.contains('Full', na=False)) &
    (df['Location'].str.contains('Kyiv', na=False))
])


# --- 4. ЗАРПЛАТА ---
def extract_max_salary(text):
    nums = re.findall(r'\d+', str(text))
    return int(nums[-1]) if nums else None

df['Max Salary'] = df['Salary Range'].apply(extract_max_salary)

df_sorted = df.sort_values(by='Max Salary', ascending=False)

print("\nТОП 5 зарплат:")
print(df_sorted.head())

print("\nНайбільш оплачувані:")
print(df_sorted[['Job Title', 'Max Salary']])


# --- 5. ГРУПУВАННЯ ---
grouped = df.groupby('Industry').agg(
    count=('Job Title', 'count'),
    avg_salary=('Max Salary', 'mean')
)

print("\nГрупування:")
print(grouped)

print("\nТоп галузь:")
print(grouped.sort_values(by='avg_salary', ascending=False).head(1))


# --- 6. КАТЕГОРІЇ ---
def category(s):
    if s <= 40000:
        return 'Low'
    elif s <= 70000:
        return 'Medium'
    else:
        return 'High'

df['Salary Category'] = df['Max Salary'].apply(category)

print("\nКатегорії:")
print(df[['Max Salary', 'Salary Category']])


# --- 7. ЧАС ---
df['Date Posted'] = pd.to_datetime(df['Date Posted'], errors='coerce')
df['Year'] = df['Date Posted'].dt.year

years = df.groupby('Year').agg(count=('Job Title', 'count'))

print("\nПо роках:")
print(years)

print("\nНайактивніший рік:")
print(years.sort_values(by='count', ascending=False).head(1))


# --- 8. ВИСНОВОК ---
print("\nВИСНОВОК:")
print("Код працює навіть без CSV. Дані проаналізовані.")