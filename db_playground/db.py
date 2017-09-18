import mysql.connector 

dbconfig = { 'host' : '127.0.0.1',
             'user' : 'hfiedler',
             'password' : 'rentahero',
             'database' : 'nameDB'}

conn = mysql.connector.connect(**dbconfig)
c = conn.cursor()


# Cavorit Convention: SQL-Abfragen in _SQL speichern.

c.execute("""DROP TABLE IF EXISTS lager""")
c.execute("""DROP TABLE IF EXISTS lieferanten""")
c.execute("""DROP TABLE IF EXISTS kunden""")


_SQL = """CREATE TABLE lager(
          fachnummer INTEGER, 
          seriennummer INTEGER,
          komponenten TEXT,
          lieferanten TEXT,
          reserviert INTEGER)
       """   
 
c.execute(_SQL)

_SQL = """CREATE TABLE lieferanten(
          kurzname TEXT,
          name TEXT,
          telefonnummer TEXT)
       """   

c.execute(_SQL)

_SQL = """CREATE TABLE kunden(
          kundennummer INTEGER,
          name TEXT,
          anschrift TEXT)
       """

c.execute(_SQL)

_SQL = """INSERT INTO lager VALUES(
          1, 2607198, 'Grafikkarte Typ A', 'FC' , 0
          )"""
print("eins")        
c.execute(_SQL)
conn.commit()
print("zwei")

werte = (1, 26071987, 'Grafikkarte Typ 1', 'SCHADCODE666', 0)
_SQL = """INSERT INTO lager VALUES (%s,%s,%s,%s,%s)""" 
c.execute(_SQL, werte) # this way no SQL-injection possible.
# security issue: cursor.execute("""INSERT INTO lager VALUES ({0}{1}{2}{3}{4})""".format(...


print("Ich bin jetzt da")

werte = ((1, 260787, "Grafikkarte Typ 1", "FC", 0),
(2, 19809, "Prozessor Typ 13", "LPE", 57),
(10, 6123, "Netzteil Typ 3", "FC", 0),
(25, 118703, "LED-Lüfter", "FC", 57),
(26, 19105, "Festplatte 128 GB", "LPE", 12))

_SQL = """INSERT INTO lager VALUES (%s, %s, %s, %s, %s)"""

c.executemany(_SQL, werte)
conn.commit()
