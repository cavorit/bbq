# Als Osterdatum wurde im Jahre 325 auf dem Konzil von Nicäa der erste Sonntag
# nach dem ersten Vollmond im Frühling (Datum des Frühlingsvollmondes)

# Für die Berechnung des Osterdatums wird stets der 21. März als
# Frühlingsbeginn verwendet.

# Der Mond benötigt 27,33 Tage, um die Erde zu umkreisen, was auch als
# "siderischer Monat" bezeichnet wird. Da die Erde aber die Sonne umkreist, so
# wie sie selbst von dem Mond umrundet wird, muss der Mond rund zwei weitere
# Tage zurücklegen, um wieder die gleiche Position zur Erde und der Sonne
# einzunehmen. Das ist dann der "synodische Monat". Um den Zeitpunkt des immer
# wiederkehrenden Vollmondes zu bestimmen, dient als Grundlage der synodische
# Monat. Was bedeutet: Der Mond braucht
# 29 Tage, 12 Stunden und 44 Minuten,
# um wieder exakt die gleiche Position zur Sonne und der Erde zu haben.


import time, timedate, timeoperators 

#Fruehlingsanfang_1 = time.strptime("21 03 1970", "%d %m %Y")# Erster Fruehlingsanfang in der Epoche
#Vollmond_1 = time.strptime("22 01 1970", "%d %m %Y") # Erster Vollmond in der Epoche
#Sonntag_1 = time.strptime(
#synodisch = ((((29 * 24) + 12) * 60) + 44) * 60 # 2551440 Sekunden

#Fruehlinge = [Fruehlingsanfang_1]
#Vollmonde = [Vollmond_1]
#Sonntage = time.strptime(())

#for y in range(100):
    
import os
os.system("ncal 2017 -e") # gibt das Datum für Ostern zurück


