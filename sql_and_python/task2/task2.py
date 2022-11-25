import pyodbc
from natasha import NamesExtractor, MorphVocab
from prettytable import PrettyTable

from sql_and_python.settings import db_address

morph_vocab = MorphVocab()
names_extractor = NamesExtractor(morph_vocab)

connection_to_db = pyodbc.connect(db_address)

cursor = connection_to_db.cursor()
cursor.execute("""
SELECT [name]
  FROM [sbertest].[dbo].[task2]
""")

th = ["Имя", "Фамилия", "Отчество"]
table = PrettyTable(th)

rows = cursor.fetchall()
for row in rows:
    match = names_extractor.find(row[0])
    print(match)
    if not match.fact.middle:
        name_list = row[0].strip().split()
        match.fact.middle = name_list[-1]  # Данная библиотека не очень хорошо работает,
        # если русское ФИО начинается с имени, небольшой костыль)
    table.add_row([match.fact.first, match.fact.last, match.fact.middle])
connection_to_db.close()

print(table)
