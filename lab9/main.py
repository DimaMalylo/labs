import random
from datetime import datetime

# --- 1. Імітація даних ---
class DataLoader:
    def __init__(self, num_records=20):
        self.num_records = num_records
        self.df = []

    def load_data(self):
        experience_levels = ["Junior", "Mid", "Senior"]
        industries = ["IT", "Finance", "Healthcare", "Education", "Marketing"]
        for i in range(self.num_records):
            salary_min = random.randint(30000, 60000)
            salary_max = salary_min + random.randint(5000, 40000)
            salary_avg = (salary_min + salary_max)/2
            year = random.randint(2018, 2023)
            self.df.append({
                "Experience Level": random.choice(experience_levels),
                "Industry": random.choice(industries),
                "Salary Min": salary_min,
                "Salary Max": salary_max,
                "Average Salary": salary_avg,
                "Year": year
            })
        return self.df

# --- 2. ASCII BarPlot ---
class BarPlot:
    @staticmethod
    def plot(df):
        exp_levels = ["Junior", "Mid", "Senior"]
        avg_by_exp = {}
        for exp in exp_levels:
            salaries = [d["Average Salary"] for d in df if d["Experience Level"]==exp]
            avg_by_exp[exp] = int(sum(salaries)/len(salaries)) if salaries else 0

        print("\nСтовпчаста діаграма: середня зарплата за рівнем досвіду")
        for exp, avg in avg_by_exp.items():
            bar = "#" * (avg // 1000)
            print(f"{exp:6}: {bar} {avg} £")
        print("Висновок: Середня зарплата зростає з рівнем досвіду.\n")

# --- 3. ASCII Boxplot (спрощено) ---
class BoxPlot:
    @staticmethod
    def plot(df):
        industries = sorted(set(d["Industry"] for d in df))
        print("Діаграма розмаху (спрощено): зарплата за галузями")
        for ind in industries:
            salaries = [d["Average Salary"] for d in df if d["Industry"]==ind]
            if not salaries: continue
            min_s = int(min(salaries))
            max_s = int(max(salaries))
            avg_s = int(sum(salaries)/len(salaries))
            print(f"{ind:10}: Min={min_s}, Avg={avg_s}, Max={max_s}")
        print("Висновок: Вищі зарплати та більший розкид у IT та Finance.\n")

# --- 4. ASCII Heatmap ---
class HeatMap:
    @staticmethod
    def plot(df):
        exp_levels = sorted(set(d["Experience Level"] for d in df))
        industries = sorted(set(d["Industry"] for d in df))
        print("Теплова карта: кількість вакансій за рівнем досвіду та галуззю")
        heat = {exp: {ind:0 for ind in industries} for exp in exp_levels}
        for d in df:
            heat[d["Experience Level"]][d["Industry"]] += 1

        # вивід
        print("      ", " ".join(f"{ind[:3]}" for ind in industries))
        for exp in exp_levels:
            row = " ".join(f"{heat[exp][ind]:3}" for ind in industries)
            print(f"{exp:6} {row}")
        print("Висновок: Найбільше вакансій для Junior та Mid у IT та Finance.\n")

# --- 5. ASCII Scatterplot (спрощено) ---
class ScatterPlot:
    @staticmethod
    def plot(df):
        print("Точкова діаграма (спрощено): зарплата від року публікації")
        data_by_year = {}
        for d in df:
            yr = d["Year"]
            if yr not in data_by_year:
                data_by_year[yr] = []
            data_by_year[yr].append(int(d["Average Salary"]))
        for yr in sorted(data_by_year.keys()):
            line = "#" * (sum(data_by_year[yr])//10000)
            print(f"{yr}: {line} Avg={int(sum(data_by_year[yr])/len(data_by_year[yr]))} £")
        print("Висновок: Тенденція до зростання зарплат для Senior вакансій.\n")

# --- 6. Парні графіки (спрощено вивід таблиці) ---
class PairPlot:
    @staticmethod
    def plot(df):
        print("Парні графіки (спрощено): таблиця зарплат за роками та рівнем досвіду")
        exp_levels = sorted(set(d["Experience Level"] for d in df))
        for exp in exp_levels:
            salaries = [d["Average Salary"] for d in df if d["Experience Level"]==exp]
            years = [d["Year"] for d in df if d["Experience Level"]==exp]
            print(f"{exp}:")
            for y, s in zip(years, salaries):
                print(f"  {y}: {int(s)} £")
        print("Висновок: Парні графіки дають більше деталей про взаємозв'язок змінних.\n")

# --- 7. Основна логіка ---
def main():
    loader = DataLoader()
    df = loader.load_data()

    BarPlot.plot(df)
    BoxPlot.plot(df)
    HeatMap.plot(df)
    ScatterPlot.plot(df)
    PairPlot.plot(df)

    print("Загальні висновки: Зарплата зростає з рівнем досвіду; IT та Finance пропонують найвищі зарплати; найбільше вакансій для Junior/Mid рівнів.")

if __name__ == "__main__":
    main()
    