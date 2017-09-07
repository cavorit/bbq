from primfaktorzerlegung import primfaktorzerlegung as prim
from queue import Queue
import threading

def pprint(index):
    print('------ Aktueller Status ------')
    for i in index:
        print(str(i) + " = " + str(index[i]))
    print('------------------------------')    

def do_work(n):
    Berechnungsindex[n] = 'berechnung läuft'
    Berechnungsindex[n] = prim(n)

# set global queue
q = Queue()
num_worker_threads = 2
Berechnungsindex = {}

# Worker to get item/message from the queue and process it
def worker():
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        do_work(item)
        q.task_done()

# Start worker threads
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)


print('(q)uit, (s)tatus')
eingabe = input('Zahl >')

while eingabe != 'q':
    if eingabe == 's':
        pprint(Berechnungsindex)
    else:
        q.put(int(eingabe))
        Berechnungsindex[int(eingabe)] = 'warte auf Zuweisung von Rechenpower'
    eingabe = input('Zahl >')   

# stop all worker
for i in range(num_worker_threads):
    q.put(None)





