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

c.execute("""INSERT INTO lieferanten VALUES(%s, %s, %s)""", ('Hans', 'Hans-Joachim', '011234813'))
c.execute("""INSERT INTO lieferanten VALUES (%s, %s, %s)""", ('Stef', 'Stefania', '011813'))
c.execute("""INSERT INTO lieferanten VALUES (%s, %s, %s)""", ('Tim', 'Timotheus', '0114813'))
c.execute("""INSERT INTO lieferanten VALUES (%s, %s, %s)""", ('Gulul', 'Joachim', '0234813'))
conn.commit()

print("huli")


_SQL = """CREATE TABLE kunden(
          kundennummer INTEGER,
          name TEXT,
          anschrift TEXT)
       """

c.execute(_SQL)
print("huli")
_SQL = """INSERT INTO kunden VALUES (%s, %s, %s)"""
werte = ((2, 'Kita', 'Elsenstr'),(5, 'Schule', 'Berlin'))
c.executemany(_SQL, werte)


_SQL = """INSERT INTO lager VALUES(
          1, 2607198, 'Grafikkarte Typ A', 'FC' , 0
          )"""

c.execute(_SQL)
conn.commit()



werte = (1, 26071987, 'Grafikkarte Typ 1', 'SCHADCODE666', 0)
_SQL = """INSERT INTO lager VALUES (%s,%s,%s,%s,%s)""" 
c.execute(_SQL, werte) # this way no SQL-injection possible.
# security issue: cursor.execute("""INSERT INTO lager VALUES ({0}{1}{2}{3}{4})""".format(...


print("Ich bin jetzt da")

werte = ((1, 260787, "Grafikkarte Typ 1", "FC", 0),
(2, 19809, "Prozessor Typ 13", "LPE", 57),
(10, 6123, "Netzteil Typ 3", "FC", 0),
(25, 118703, "LED-Lüfter", "Hans", 57),
(26, 19105, "Festplatte 128 GB", "LPE", 12))

_SQL = """INSERT INTO lager VALUES (%s, %s, %s, %s, %s)"""

c.executemany(_SQL, werte)
conn.commit()

_SQL = """SELECT lager.fachnummer, lager.komponenten, lieferanten.name 
          FROM lager, lieferanten
          WHERE lieferanten.telefonnummer = '011234813' AND lager.lieferanten = lieferanten.kurzname
       """

c.execute(_SQL)
print(c.fetchall())

c.execute("""SELECT * FROM kunden""")
#row = c.fetchone()
#while row:
#    print(row)
#    row=c.fetchone()

for row in c:
    print(row)



