from threading import _start_new_thread as start_new_thread 
 

def heron(a):
        """Calculates the square root of a"""
        eps = 0.0000001
        old = 1
        new = 1
        while True:
            old,new = new, (new + a/new) / 2.0
            print (old, new)
            if abs(new - old) < eps:
                break
        return new

start_new_thread(heron,(3299,))
start_new_thread(heron,(99329,))
start_new_thread(heron,(173322,))

c = input("Type something to quit.")
