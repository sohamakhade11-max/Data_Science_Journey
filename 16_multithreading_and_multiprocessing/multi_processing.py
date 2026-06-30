#create process that runs in parallel 
## when to use:
###1)cpu bound task  which are heavy like maths or quant etc
###2)parrallel execution-multiples core of cpu

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube:{i*i*i}")

if __name__=="__main__":

    #create 2 processes
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_numbers)

    t=time.time()
    #start the  process
    p1.start()
    p2.start()

    #wait for the proces to complete
    p1.join()
    p2.join()

    finish_time=time.time()-t
    print(finish_time)

