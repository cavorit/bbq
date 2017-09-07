import _thread
from wallsches import wallsches as wallsches

anzahl_threads = 0
threads_gestartet = False

lock = _thread.allocate_lock()

def naehere_pi_an(n):
    global anzahl_threads, thread_gestartet

    lock.acquire()
    anzahl_threads += 1
    thread_gestartet = True
    lock.release()

    wallsches(n) 

    lock.acquire()
    anzahl_threads() -=1
    lock.release()

_thread.start_new_thread(naehere_pi_an, (1234567,))
_thread.start_new_thread(naehere_pi_an, (991234567,))
_thread.start_new_thread(naehere_pi_an, (81234567,))
_thread.start_new_thread(naehere_pi_an, (2221234567,))
_thread.start_new_thread(naehere_pi_an, (331234567,))

while not thread_gestartet:
    pass
while anzahl_threads > 0:
    pass
