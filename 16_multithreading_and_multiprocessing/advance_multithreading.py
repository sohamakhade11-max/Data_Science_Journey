# ThreadPoolExecutor is used to perform tasks concurrently using multiple threads.
# It is best suited for I/O-bound tasks (file handling, API calls, database queries, etc.)
# where the program spends most of its time waiting.

from concurrent.futures import ThreadPoolExecutor
import time

# Function executed by each thread
def print_number(number):
    
    # Simulates a slow I/O operation by making the thread wait for 1 second
    time.sleep(1)
    
    # Return the processed result
    return f"Number:{number}"

# Input data to be processed
numbers = [1,2,3,4,5]

# Create a thread pool with maximum 3 worker threads
# At most 3 tasks can run simultaneously
with ThreadPoolExecutor(max_workers=3) as executor:
    
    # executor.map() applies print_number() to every element in numbers
    # Tasks are distributed among available threads automatically
    # Returns an iterator containing results in the SAME order as input
    results = executor.map(print_number, numbers)

# Iterate through results and print them
for result in results:
    print(result)

'''
Execution Flow:

numbers = [1,2,3,4,5]
max_workers = 3

Round 1:
Thread 1 -> print_number(1)
Thread 2 -> print_number(2)
Thread 3 -> print_number(3)

(All run concurrently and wait for 1 second)

Round 2:
Thread 1 -> print_number(4)
Thread 2 -> print_number(5)

Total execution time ≈ 2 seconds

Without multithreading:
5 tasks × 1 second = 5 seconds

With 3 threads:
First 3 tasks -> 1 second
Remaining 2 tasks -> 1 second

Total ≈ 2 seconds

Important Notes:
1. executor.map() preserves input order in output.
2. Threads share the same memory space.
3. ThreadPoolExecutor automatically creates and destroys threads.
4. Useful for I/O-bound tasks, not CPU-intensive tasks.
5. 'with' statement automatically shuts down the thread pool after completion.
'''