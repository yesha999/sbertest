import pyodbc

connection_to_db = pyodbc.connect(
    r"Driver={SQL Server};Server=YESHA\SQLEXPRESS;Database=sbertest;Trusted_Connection=yes;")

cursor = connection_to_db.cursor()
cursor.execute("""
SELECT TOP (90)[number]
  FROM [sbertest].[dbo].[task1]
""")

rows = cursor.fetchall()
counter = 0
for row in rows:
    counter += 1
    print(f"{counter}) {row[0]}")
connection_to_db.close()

# Если у нас список всяких разных чисел и нужно получить те,
# которые входят в ряд Фиббоначчи (по условию не совсем понятно)
# fib_tuple = tuple(map(str, fib_row(100)))
#
# cursor.execute(f"""
# SELECT TOP (90)[number]
#   FROM [sbertest].[dbo].[task1]
#   WHERE number in {fib_tuple}
# """)
