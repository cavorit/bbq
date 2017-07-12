class cake(object):
    
    _eaten = False

    def __init__(self, peaces, caketype):
        self.peaces = peaces
        self.caketype = caketype
        print("Ich habe einen " + caketype + " gebacken mit "+str(self.peaces)+" Stücken")
    
    def eat(self):
        if (self._eaten):
            print("Der " + self.caketype + " ist bereits aufgegessen.")
        else:
            self.peaces -= 1
            self._eaten = (self.peaces == 0)
            print("Es sind jetzt nur noch " + str(self.peaces) + " Stücke vom " + str(self.caketype) + " übrig")
    
    def count(self):
        print("Es sind noch " + str(self.peaces) + " Stücken da.")
        return(self.peaces)
