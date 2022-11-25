import pyodbc

from sql.settings import db_address

connection_to_db = pyodbc.connect(db_address)

cursor = connection_to_db.cursor()
cursor.execute("""
IF OBJECT_ID(N'task2', N'U') IS NULL
CREATE TABLE task2 (
    name varchar(255)
);""")
connection_to_db.commit()

cursor.execute("""
DELETE FROM task2
""")

query_string = """
INSERT INTO task2
VALUES ('Васильев Петр Геннадьевич'), ('Греф Герман Оскарович'), ('Светлана Семина Германовна'), ('Громова Виктория Владимировна'),
('Кеттлер     Самуил Джонович'), ('Иван Дорошенко  Никитович')
"""
cursor.execute(query_string)
connection_to_db.commit()
