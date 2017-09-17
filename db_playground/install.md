# 1. Den MariaDB- Server installieren

sudo apt-get install mysql-server


# 2. Einen MySQL-Datenbanktreiber für Python installieren

Lade den Treiber runter:

- https://dev.mysql.com/downloads/connector/python  

- choose 'platform independent'

> tar -xf mysql-connector-python-2.1.7

Gehe in das entpackte Verzeichnis

> sudo -H python3 setup.py install


# 3. Die Datenbank und die nötigen Tabellen erstellen

Starte die MySQL-Konsole:

> mysql -u root -p

Ab hier in der MySQL-Konsole:

> create database nameDB; 

Erzeuge einen MySQL-Benutzer für die App

> grant all on nameDB.* to 'hfiedler' identified by 'rentahero';

> quit 


