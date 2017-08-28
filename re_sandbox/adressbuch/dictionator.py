import re

# card = open('addr.txt')
# card.close()

# Name: Max Mustermann 
# Adr: Musterstr. 123
# 12345 Musterhausen
# Tel: +49 1234 5678"

card = r"Name: Max Mustermann Adr: Musterstr. 123 12345 Musterhausen Tel: +49 12345 6789"
#m = re.search(r"(?P<Name>(?<=Name: ).+(?=Adr:))", card)
m = re.finditer(r"(?P<Name>(?<=Name:).+(?=Adr:))|(?P<Adresse>(?<=Adr:).+(?=Tel:))|(?P<Telephon>(?<=Tel:).+)", card)

k = 0
for i in m:
    k += 1
    print(i.group('Name'))
    print(i.group('Adresse'))
    print(i.group('Telephon'))        

#print(m.group('Name'))



