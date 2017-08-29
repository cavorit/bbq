import os, re, datetime, time


Jahr = input("Welches Jahr: ")
Ostern = os.popen("ncal -e {0}".format(Jahr)).read()
print("Ostern ist dieses Jahr am: {0}".format(Ostern))
match = re.search(r"(?P<Tag>\d+).(?P<Monat>\w+) ", Ostern)
print("Der Tag ist also {0} und der Monat {1}".format(match.group('Tag'), match.group('Monat')))
datetime.date.fromtimestamp(time.mktime(time.strptime(match.group('Tag')+'-04-'+Jahr)))      


