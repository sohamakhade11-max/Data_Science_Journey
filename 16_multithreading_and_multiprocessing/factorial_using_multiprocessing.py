# # ==========================================
# MULTIPROCESSING USING POOL - REVISION
# ==========================================

import multiprocessing
import math
import sys
import time

# Increase maximum digits allowed when converting
# huge integers to strings (Python 3.11+)
sys.set_int_max_str_digits(100000)

# Function executed by each process
def compute_factorial(number):

    print(f"Computing factorial of {number}")

    # CPU-intensive task
    result = math.factorial(number)

    print(f"Factorial of {number} is {result}")

    return result


if __name__ == "__main__":

    # List of inputs
    numbers = [5000, 6000, 7000, 8000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:

        # pool.map() distributes tasks among processes
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time Taken: {end_time - start_time} seconds")