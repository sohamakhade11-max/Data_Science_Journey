# ProcessPoolExecutor is used for multiprocessing.
# Instead of creating multiple threads, it creates multiple processes.
# Each process has its own memory space and Python interpreter.

# Best suited for CPU-bound tasks such as:
# - Mathematical computations
# - Data processing
# - Machine Learning calculations
# - Image processing

from concurrent.futures import ProcessPoolExecutor
import time

# Function executed by each process
def square_number(number):
    
    # Simulates a time-consuming task
    time.sleep(1)
    
    # Returns square of the number
    return f"Square:{number*number}"

# Input data
numbers = [1,2,3,4,5]

# Required on Windows when using multiprocessing
# Prevents child processes from recursively executing the entire script
if __name__ == "__main__":
    
    # Create a process pool with 3 worker processes
    with ProcessPoolExecutor(max_workers=3) as executor:
        
        # Apply square_number() to every element in numbers
        # Tasks are distributed among available processes
        # Returns results in the same order as input
        results = executor.map(square_number, numbers)

    # Print results
    for result in results:
        print(result)

'''
Execution Flow:

numbers = [1,2,3,4,5]
max_workers = 3

Round 1:
Process 1 -> square_number(1)
Process 2 -> square_number(2)
Process 3 -> square_number(3)

(All run simultaneously)

Round 2:
Process 1 -> square_number(4)
Process 2 -> square_number(5)

Output:
Square:1
Square:4
Square:9
Square:16
Square:25

Approximate Execution Time:
2 seconds

Without multiprocessing:
5 tasks × 1 second = 5 seconds

With 3 processes:
First 3 tasks -> 1 second
Remaining 2 tasks -> 1 second
Total ≈ 2 seconds
'''