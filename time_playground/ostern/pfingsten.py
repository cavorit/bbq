import os, re, datetime, time

Jahr = input("Welches Jahr: ")
Ostern = os.popen("ncal -e {0}".format(Jahr)).read()
print("Ostern ist dieses Jahr am: {0}".format(Ostern))
match = re.search(r"(?P<Tag>\d+).(?P<Monat>\w+) ", Ostern)
# print("Der Tag ist also {0} und der Monat {1}".format(match.group('Tag'), match.group('Monat')))
Ostern_date = datetime.date.fromtimestamp(time.mktime(time.strptime(match.group('Tag')+'-04-'+Jahr, "%d-%m-%Y")))      
Pfingsten_date = (Ostern_date+datetime.timedelta(days=50))
#print("Pfingsten ist somit am:" + re.search(r"(?<=....-..-)..", Pfingsten_date).group(0) +  " April " +Jahr)

