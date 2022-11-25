import pyodbc

connection_to_db = pyodbc.connect(
    r"Driver={SQL Server};Server=YESHA\SQLEXPRESS;Database=sbertest;Trusted_Connection=yes;")

cursor = connection_to_db.cursor()
cursor.execute("""
IF OBJECT_ID(N'people', N'U') IS NULL
CREATE TABLE people (
    id int IDENTITY (1,1) NOT NULL PRIMARY KEY,
    name varchar(255)
);""")
connection_to_db.commit()
cursor.execute("""
IF OBJECT_ID(N'sales', N'U') IS NULL
CREATE TABLE sales (
    id int IDENTITY (1,1) NOT NULL PRIMARY KEY,
    people_id int,
    FOREIGN KEY (people_id) REFERENCES people (id) ON DELETE CASCADE ON UPDATE CASCADE,
    sale varchar(255),
    price decimal(19,2)
);""")
connection_to_db.commit()

query_string = """
INSERT INTO people (name)
VALUES ('Петр'), ('Герман'), ('Светлана'), ('Виктория'),
('Самуил'), ('Иван')
"""
cursor.execute(query_string)
connection_to_db.commit()

query_string = """
INSERT INTO sales (people_id, sale, price)
VALUES (2, 'Стул', 2000), (1, 'Кресло', 5000), (5, 'Телевизор', 50000), (3, 'Ноутбук', 45000),
 (4, 'Кресло', 5500), (1, 'Автомобиль', 500000), (2, 'Диван', 15000)
"""
cursor.execute(query_string)
connection_to_db.commit()


