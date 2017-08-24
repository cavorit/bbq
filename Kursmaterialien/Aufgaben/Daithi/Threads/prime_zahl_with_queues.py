import threading
import queue

class prime_number_queued(threading.Thread):
    #setting up a dictionay to return values to
    result = {}
    #getting a lock to get jobs processd in queue
    resultLock = threading.Lock()
    #setting up the queue
    my_line = queue.Queue()

    def run(self):
        while True:
            # get the entry from the queue
            number = prime_number_queued.my_line.get()
            # find out if it's a prime or not and store it in results value
            result = self.is_prime(number)
            # get the lock
            prime_number_queued.resultLock.acquire()
            # put the entry and the answer into dictionary
            prime_number_queued.result[number] = result
            # release lock
            prime_number_queued.resultLock.release()
            # communicate that this task is done, if it's the last the program will end
            prime_number_queued.my_line.task_done()



    def is_prime(self,number):
        i = 2
        while i*i < number + 1:
            if number % i == 0:
                return " %d can be divided by %d" % (number,i)
            i +=1
        return "prime"

# set up a queue with five workers
my_threads = [prime_number_queued() for i in range(5)]
#fire them up
for thread in my_threads:
    thread.setDaemon(True)
    thread.start()
#get some entries
entry = input("> ")
while entry != "exit":
    # get the status
    if entry == "status":
        print("--------- Actual Status ---------")
        #get the lock to fullfill this request
        prime_number_queued.resultLock.acquire()
        for z, e in prime_number_queued.result.items():
            print("%d : %s" % (z,e))
            # give control back to workers
        prime_number_queued.resultLock.release()
        print("---------------------------------")

    elif int(entry) not in prime_number_queued.result:

        # get lock
        prime_number_queued.resultLock.acquire()
        # mark as processing
        prime_number_queued.result[int(entry)] = " processing "
        # release the lock
        prime_number_queued.resultLock.release()
        # put the entry into the queue for processing
        prime_number_queued.my_line.put(int(entry))

    entry = input("> ")
# finish up
prime_number_queued.my_line.join()