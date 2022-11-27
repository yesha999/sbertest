import pyodbc

from fib import fib_row
from sql_and_python.settings import db_address

connection_to_db = pyodbc.connect(db_address)

cursor = connection_to_db.cursor()
cursor.execute("""
IF OBJECT_ID(N'task1', N'U') IS NULL
CREATE TABLE task1 (
    number varchar(30)
);""")
connection_to_db.commit()

fib_list = list(map(float, fib_row(100)))  # Мы должны сделать числа строками или дробными,
# так как слишком большие числа в данном ряду не умещаются даже в bigint

cursor.execute("""
DELETE FROM task1
""")

for i in fib_list:
    query_string = """
    INSERT INTO task1
    VALUES (%s)
    """ % i
    cursor.execute(query_string)
connection_to_db.commit()
