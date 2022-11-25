import pyodbc

from sql_and_python.settings import db_address

connection_to_db = pyodbc.connect(db_address)

cursor = connection_to_db.cursor()

cursor.execute("""
SELECT people.id, people.name, COUNT(sales.id) as sale_count, SUM(sales.price) as sale_rank  FROM people
LEFT JOIN sales
ON people.id = sales.people_id
GROUP BY people.id, people.name;""")

print(f"Ранжировка каждого человека по количеству продаж:\n{cursor.fetchall()}")

cursor.execute("""
SELECT COUNT(sales.id) FROM sales""")

print(f"COUNT всех продаж: {cursor.fetchone()[0]}")