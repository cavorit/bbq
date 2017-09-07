import _thread
from wallsches import wallsches as wallsches

anzahl_threads = 0

def naehere_pi_an(n):
    global anzahl_threads
    anzahl_threads += 1
    wallsches(n)
    anzahl_threads -=1

_thread.start_new_thread(naehere_pi_an, (10**7,))
_thread.start_new_thread(naehere_pi_an, (12341234,))
_thread.start_new_thread(naehere_pi_an, (9999999,))
_thread.start_new_thread(naehere_pi_an, (), {'n' : 1337}

while anzahl_threads > 0:
    pass 

# dies naive Umsetzung hat das Problem, dass evtl. das Programm terminiert,
# noch bevor ein Thread losgeht.     

