import re

pattern = re.compile(r"Name:\s(?P<first_name>\w+)\s(?P<second_name>\w+)"
                     r"\s*Addr:\s(?P<street_name>\w+)\s(?P<house_number>\d{1,4})"
                     r"\s*(?P<DE_postal_code>\d{5})\s(?P<city>\w+)"
                     r"\s*Tel:\s(?P<country_code>\+\d{1,2})\s(?P<area_code>\d{1,5})\s(?P<tel_number>\d{3,6})")


with open("max_Musterman.txt","r") as file:
    my_file = file.read()
    my_dict = pattern.search(my_file).groupdict()
    print(my_dict)
