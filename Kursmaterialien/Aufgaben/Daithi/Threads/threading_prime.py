import threading

class PrimzahlThread(threading.Thread):
    def __init__(self, zahl):
        threading.Thread.__init__(self)
        self.Zahl = zahl

    def run(self):
        i = 2
        while i*i <= self.Zahl:
            if self.Zahl % i == 0:
                print("{0} ist nicht prim, "
                      "da {1} = {2} * {3}".format( self.Zahl,
                                    self.Zahl, i, self.Zahl/ i))
                return
            i += 1
        print("{0} ist prim".format(self.Zahl))

meine_threads = []

eingabe = input("> ")

while eingabe != "ende":
    thread = PrimzahlThread(int(eingabe))
    meine_threads.append(thread)
    thread.start()
    eingabe = input("> ")

for t in meine_threads:
    t.join()