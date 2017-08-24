from dateutil.easter import*
from datetime import datetime

"""
Noch nicht fertig, also keine Menu, aber die functionalitat ist da

"""

feast_days = {"Oster Sontag":0,
              "Oster Montag":1,
              "Christi Himmerfahrt": 29,
              "Pfingstsonntag" : 39,
              "Pfingstmontag" : 40,
              "Karfreitag":- 1}

# gibt alle feirien tage in einen jahr zuruck
def get_all_dates_in_a_year(a = this_year):
    for key,value in feast_days.items():
        print(get_dates(a,b=value,c=key))

# gibt den ferientag zuruck, default ist Ostern
def get_date(a = this_year, b = 0, c ="Ostern"):

    if a == this_year:
        return (easter(int(datetime.now().strftime("%Y")))+ timedelta(b)).strftime(
                "{0} felt am %d. %b".format(c))
    else:
        return easter(a).strftime(" in %Y {0} felt am %d. von %b".format(c))

# gibt ein bestimt ferien tag zuruck
def get_holidays_date(feast_day, b = this_year):
        if feast_day in feast_days.keys():
            print(get_date(a = b, c = feast_day, b=feast_days[feast_day]))
        else:
            print(" Bitte geben sie eine von diesen Feiertage ein"
                  + feast_days.keys())

