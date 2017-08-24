import csv

# simple manipulation of a csv text file

csv.list_dialects()

reader = csv.reader


reader = csv.reader(open("data.txt","r"))

for row in reader:
    print(row)


reader = csv.DictReader(open("data.txt","r"))
for row in reader:
    print(row)

# example from book, create a csv file, write to it and then read from it

car_file = open("auto.csv","w")

writer = csv.writer(car_file)


writer.writerow(["marke","modell","leistung_in_ps"])
daten = (
    ["Volvo","P245","130"],["Ford","Focus","90"],
    ["Mercedes","CLK","250"])
writer.writerows(daten)

car_file.close()

file_cars = open("auto.csv","r")
read_cars = csv.reader(file_cars)

for row in read_cars:
    print(row)

reader = csv.DictReader(file_cars)

for row in reader:
    print(row)