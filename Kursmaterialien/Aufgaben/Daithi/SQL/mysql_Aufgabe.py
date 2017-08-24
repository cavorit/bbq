import MySQLdb

connection = MySQLdb.connect(host = "localhost",
                       user= "root",
                       db = "lagerverwaltung")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE lager(
                fachnummer INTEGER,
                serinenummer INTEGER,
                komponente TEXT,
                lieferant TEXT,
                reserviert INTEGER
                 )""")

cursor.execute(""" CREATE TABLE lieferanten(
                    kurzname TEXT,
                    name TEXT,
                    telefonnummer TEXT)""")

cursor.execute("""CREATE TABLE kunden(
                    kundennummer INTEGER,
                    name TEXT,
                    anschrift TEXT)""")

cursor.execute("""INSERT INTO lager VALUES(
                    1,26071987,'Grafikkarte Typ 1','FC',0
                    )""")
connection.commit()

werte = (1,26071987,'Grafikkarte Typ 1','FC',0)

sql = "INSERT INTO lager VALUES ({0},{1},'{2}','{3}',{4})".format(*werte)

cursor.execute(sql)

# tried this for the laugh, didnt' work

#werte = ("DR","Danger Electronics","666');Hier kann Schadcode stehen")

#cursor.execute( "INSERT INTO lager VALUES (%s,%s,%s,%s,%s)",*werte)

cursor.execute("INSERT INTO lieferanten VALUES ('kurz','name','telefon')",werte)

data = ((1,"2607871987","Grafikkarte Typ 1","FC",0),
        (2,"19870109","Prizessor Typ 13","LPE",57),
        (10,"06198823","Netzteil Typ 3","FC",0),
        (25,"11198703","LED-Lufter","FC",57),
        (26,"19880105","Festplatte 128 GB","LPE",12))

cursor.executemany("INSERT INTO lager VALUES(%s,%s,%s,%s,%s)",data)

lieferanten = (("FC","FiboComputing Inc.","011235813"),
               ("LPE","LettgenPetersErnesti","026741337"),
               ("GC","Golden Computers","016180339")
               )

for row in lieferanten:

    cursor.execute("INSERT INTO lieferanten VALUES (%s,%s,%s)",row)

kunden = ((12,"Heinz Elhurg","Turnhallenstr.1, 3763 Sporthausen"),
          (57,"Markus Altbert","Kämperweg 24, 2463 Duisschloss"),
          (64,"Steve Apple","Podeyemac street 2,7467 Iwarhausen"))

cursor.executemany("INSERT INTO kunden VALUES(%s,%s,%s)",kunden)


connection.commit()

sql = """
SELECT lager.fachnummer,lager.komponente,lieferanten.name
FROM lager,lieferanten
WHERE lieferanten.telefonnummer = '011235813' AND
                    lager.lieferant=lieferanten.kurzname"""

cursor.execute(sql)