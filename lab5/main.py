import asyncio
import sqlite3
import random

DB_FILE = "nodes_stdlib.db"

# --- 1. Створення таблиці ---
def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- Додавання вузлів ---
def add_nodes(num_nodes=10):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for i in range(num_nodes):
        cursor.execute("INSERT INTO nodes (ip, status) VALUES (?, ?)", (f"192.168.0.{i+1}", "unknown"))
    conn.commit()
    conn.close()

# --- Отримання вузлів ---
def get_nodes():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, ip, status FROM nodes")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Оновлення статусу вузла ---
def update_node_status(node_id, status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE nodes SET status = ? WHERE id = ?", (status, node_id))
    conn.commit()
    conn.close()

# --- Асинхронна імітація опитування ---
async def check_node(node):
    await asyncio.sleep(random.uniform(0.2, 0.5))  # імітація мережевого запиту
    status = random.choice(["online", "offline"])
    update_node_status(node[0], status)
    return (node[0], node[1], status)

# --- Моніторинг ---
async def monitor_nodes():
    nodes = get_nodes()
    print("\nСписок вузлів ДО оновлення статусу:")
    for n in nodes:
        print(f"{n[0]}: {n[1]} - {n[2]}")

    # Асинхронне оновлення статусів
    tasks = [check_node(n) for n in nodes]
    updated_nodes = await asyncio.gather(*tasks)

    print("\nСписок вузлів ПІСЛЯ оновлення статусу:")
    for n in updated_nodes:
        print(f"{n[0]}: {n[1]} - {n[2]}")

# --- MAIN ---
async def main():
    create_table()
    add_nodes(10)  # додаємо 10 вузлів
    await monitor_nodes()

if __name__ == "__main__":
    asyncio.run(main())