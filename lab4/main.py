import sqlite3
import pandas as pd
import re
import os

# --- 1. ПІДГОТОВКА ДАНИХ ---
class DataLoader:
    def __init__(self):
        if os.path.exists("jobs.csv"):
            self.df = pd.read_csv("jobs.csv")
            print("CSV завантажено")
        else:
            print("CSV не знайдено → створюю тестові дані")
            data = {
                'Job Title': ['Cloud Engineer', 'Data Scientist', 'AI Engineer', 'Backend Developer'],
                'Company': ['Google', 'Amazon', 'Microsoft', 'Meta'],
                'Location': ['Kyiv', 'Lviv', 'Kyiv', 'Odesa'],
                'Industry': ['Cloud Computing', 'IT', 'AI', 'IT'],
                'Experience Level': ['Senior', 'Junior', 'Senior', 'Middle'],
                'Job Type': ['Full-Time', 'Part-Time', 'Full-Time', 'Full-Time'],
                'Required Skills': ['Python, SQL', 'Python', 'AI, SQL', 'Java'],
                'Salary Range': ['50000-80000', '30000-50000', '70000-120000', '40000-60000'],
                'Date Posted': ['2023-01-01', '2023-05-10', '2023-07-15', '2022-03-20']
            }
            self.df = pd.DataFrame(data)


# --- 2. БАЗА ДАНИХ ---
class DatabaseManager:
    def __init__(self, db_name="jobs.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def load_to_db(self, df):
        df.to_sql("jobs", self.conn, if_exists="replace", index=False)
        print("Дані записано в SQLite")

    def query(self, sql):
        return pd.read_sql_query(sql, self.conn)

    def close(self):
        self.conn.close()
        print("З'єднання закрито")


# --- 3. ОБРОБКА ЗАРПЛАТИ ---
class SalaryProcessor:
    def __init__(self, db):
        self.db = db

    def add_salary_column(self):
        df = self.db.query("SELECT * FROM jobs")

        def extract(text):
            nums = re.findall(r'\d+', str(text))
            return int(nums[-1]) if nums else None

        df['Max Salary'] = df['Salary Range'].apply(extract)

        df.to_sql("jobs", self.db.conn, if_exists="replace", index=False)
        print("Додано колонку Max Salary")


# --- 4. SQL ЗАПИТИ ---
class SQLQueries:
    def __init__(self, db):
        self.db = db

    def basic_queries(self):
        print("\nПерші 10 вакансій:")
        print(self.db.query("SELECT * FROM jobs LIMIT 10"))

        print("\nВакансії з SQL:")
        print(self.db.query("SELECT * FROM jobs WHERE `Required Skills` LIKE '%SQL%'"))

        print("\nУнікальні Location та Company:")
        print(self.db.query("SELECT DISTINCT Location, Company FROM jobs"))

    def analytics(self):
        print("\nСередня зарплата по рівню:")
        print(self.db.query("""
            SELECT `Experience Level`, AVG(`Max Salary`) as avg_salary
            FROM jobs
            GROUP BY `Experience Level`
        """))

        print("\nКількість вакансій по рівню:")
        print(self.db.query("""
            SELECT `Experience Level`, COUNT(*) as count
            FROM jobs
            GROUP BY `Experience Level`
        """))

        print("\nМін і макс зарплата:")
        print(self.db.query("""
            SELECT MIN(`Max Salary`), MAX(`Max Salary`)
            FROM jobs
        """))

    def aggregates(self):
        print("\nВакансії з зарплатою > 50000:")
        print(self.db.query("""
            SELECT Industry, COUNT(*) as count
            FROM jobs
            WHERE `Max Salary` > 50000
            GROUP BY Industry
        """))

        print("\nСередня зарплата по індустріях:")
        print(self.db.query("""
            SELECT Industry, AVG(`Max Salary`) as avg_salary
            FROM jobs
            GROUP BY Industry
        """))

    def complex_queries(self):
        print("\nПо Location і Experience:")
        print(self.db.query("""
            SELECT Location, `Experience Level`, COUNT(*) as count
            FROM jobs
            GROUP BY Location, `Experience Level`
        """))

        print("\nПо Industry і Job Type:")
        print(self.db.query("""
            SELECT Industry, `Job Type`, COUNT(*) as count
            FROM jobs
            GROUP BY Industry, `Job Type`
        """))

        print("\nСередня зарплата по Location і Experience:")
        print(self.db.query("""
            SELECT Location, `Experience Level`, AVG(`Max Salary`) as avg_salary
            FROM jobs
            GROUP BY Location, `Experience Level`
        """))

    def extra_queries(self):
        print("\nТОП 5 зарплат:")
        print(self.db.query("""
            SELECT * FROM jobs
            ORDER BY `Max Salary` DESC
            LIMIT 5
        """))

        print("\nКомпанії з найбільшою кількістю вакансій у 2023:")
        print(self.db.query("""
            SELECT Company, COUNT(*) as count
            FROM jobs
            WHERE substr(`Date Posted`,1,4) = '2023'
            GROUP BY Company
            ORDER BY count DESC
        """))


# --- MAIN ---
if __name__ == "__main__":
    # 1
    loader = DataLoader()
    df = loader.df

    # 2
    db = DatabaseManager()
    db.load_to_db(df)

    # 3
    sp = SalaryProcessor(db)
    sp.add_salary_column()

    # 4-6
    queries = SQLQueries(db)
    queries.basic_queries()
    queries.analytics()
    queries.aggregates()
    queries.complex_queries()
    queries.extra_queries()

    # 7
    db.close()

    # 8
    print("\nВИСНОВКИ:")
    print("1. Найвищі зарплати у Senior позицій.")
    print("2. IT та Cloud мають найбільше вакансій.")
    print("3. 2023 рік має найбільшу активність.")