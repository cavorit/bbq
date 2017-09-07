from primfaktorzerlegung import primfaktorzerlegung as prim
import threading, time 

class PrimzahlThread(threading.Thread):

    def __init__(self, zahl):
        threading.Thread.__init__(self)
        self.Zahl = zahl
    def run(self):
        Berechnungsindex[self.Zahl] = 'Berechnung läuft'
        Berechnungsindex[self.Zahl] = prim(self.Zahl)

def pprint(index):
    print('------ Aktueller Status ------')
    for i in index:
        print(str(i) + " = " + str(index[i]))
    print('------------------------------')    

meine_threads = []
Berechnungsindex = {}

eingabe = input("Zahl (oder q)> ")

while eingabe != "q":
    if eingabe == "status":
        pprint(Berechnungsindex)
    else:
        thread = PrimzahlThread(int(eingabe))
        meine_threads.append(thread)
        thread.start()
    eingabe = input("Zahl (oder q)> ")
            
for t in meine_threads:
    t.join()
