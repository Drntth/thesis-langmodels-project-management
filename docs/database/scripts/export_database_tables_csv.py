import os
import sqlite3
import csv
import environ

env = environ.Env()
environ.Env.read_env()

conn = sqlite3.connect(env("DATABASE_PATH"))
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

output_dir = env("TABLES_DIR")
os.makedirs(output_dir, exist_ok=True)

for table in tables:
    table_name = table[0]
    file_path = os.path.join(output_dir, f"{table_name}.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        writer.writerow(column_names) 
        writer.writerows(rows)

    print(f"Database table exported to: {file_path}")

conn.close()
