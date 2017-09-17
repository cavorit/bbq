import mysql.connector 

dbconfig = { 'host' : '127.0.0.1',
             'user' : 'hfiedler',
             'password' : 'rentahero',
             'database' : 'nameDB'}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()


# Cavorit Convention: SQL-Abfragen in _SQL speichern.

cursor.execute("""DROP TABLE IF EXISTS lager""")
cursor.execute("""DROP TABLE IF EXISTS lieferanten""")
cursor.execute("""DROP TABLE IF EXISTS kunden""")


_SQL = """CREATE TABLE lager(
          fachnummer INTEGER, 
          seriennummer INTEGER,
          komponenten TEXT,
          lieferanten TEXT,
          reserviert INTEGER)
       """   
 
cursor.execute(_SQL)

_SQL = """CREATE TABLE lieferanten(
          kurzname TEXT,
          name TEXT,
          telefonnummer TEXT)
       """   

cursor.execute(_SQL)

_SQL = """CREATE TABLE kunden(
          kundennummer INTEGER,
          name TEXT,
          anschrift TEXT)
       """

cursor.execute(_SQL)

_SQL = """INSERT INTO lager VALUES(
          1, 2607198, 'Grafikkarte Typ A', 'FC' , 0
          )"""
          
cursor.execute(_SQL)
conn.commit()

print("------------------ #1")

werte = (1, 26071987, 'Grafikkarte Typ 1', 'SCHADCODE666', 0)

# So ist ein Sicherheitsrisiko, weil python die Zuordnung vornimmt, was
# malcode-injection ermöglicht
# _SQL = """INSERT INTO lager VALUES ({0}, {1}, '{2}', '{3}', {4})""".format(*werte)
#
# print(_SQL)

# Sicher ist, wenn man das DB-Management-System die Zuordnung vornehmen lässt


_SQL = """INSERT INTO lager VALUES (?,?,?,?,?)"""
print("----------------- #2")
print(_SQL)
print(werte)
print("-----------------")
cursor.execute(_SQL, werte)
conn.commit()


print("Ich bin jetzt da")

#werte = ((1, "2607871987", "Grafikkarte Typ 1", "FC", 0),
#(2, "19870109", "Prozessor Typ 13", "LPE", 57),
#(10, "06198823", "Netzteil Typ 3", "FC", 0),
#(25, "11198703", "LED-Lüfter", "FC", 57),
#(26, "19880105", "Festplatte 128 GB", "LPE", 12))

#_SQL = """INSERT INTO lager VALUES (?,?,?,?,?)"""

#cursor.executemany(_SQL, werte)

