#multithreading
##it is use when task spends more time waiting for i/o operations

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Numbers:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"Letters:{letter}")

#creating threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time() 
# print_numbers()
# print_letter()
t1.start()
t2.start()

##wait for threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)