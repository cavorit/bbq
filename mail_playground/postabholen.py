#/! /usr/bin/env python3

import json, poplib, os 

if os.access('config.json', os.R_OK): 
    print("Lade config.json")
    configfilename = 'config.json'
else:
    print("config.json nicht vorhanden oder kein Lesezugriff. Lade config.default.json") 
    configfilename = 'config.default.json'

with open(configfilename, encoding='utf-8') as appsettings:
    appsettings = json.load(appsettings)

if __debug__:
    print(appsettings)

server = poplib.POP3_SSL(appsettings['POP_Server'], port='995') # port 995 google
print(server.getwelcome())
# print(server.user(appsettings['POP_Username'])) gmail takes Mailadress instead of POP_Username
print(server.user(appsettings['Mailadresse']))
#pwd = input("password: ")
print(server.pass_(appsettings['POP_Passwort'])) # gmail need either oauth-registration and authentification, or the mail account settings must enable lower security apps enable 
print(server.quit())        



