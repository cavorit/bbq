import sqlite3

connection = sqlite3.connect('Johnny.db')
cursor = connection.cursor()

_SQL = """
create table log(
vorname varchar(16),
nachname varchar(16),
id int auto_increment primary key
);
"""

cursor.execute(_SQL)

cursor.execute("""show tables;""")


