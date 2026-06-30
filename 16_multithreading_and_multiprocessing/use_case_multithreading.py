# import threading
# import time 
# import requests

# from bs4 import BeautifulSoup

# urls=[
#     'https://www.langchain.com/blog',
#     'https://docs.langchain.com/'
# ]

# def fetch_content(urls):
#     response=requests.get(urls)
#     soup=BeautifulSoup(response.content,'html.parser')
#     print(f'fetched {len(soup.text)} character from url{urls}')

# threads=[]
# for url in urls:
#     thread=threading.Thread(target=fetch_content,args=(url,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print('All webpages fetched!!')


# ==========================================
# MULTITHREADING WEB SCRAPING - REVISION
# ==========================================

import threading
import requests
from bs4 import BeautifulSoup

# List of URLs to fetch
urls = [
    "https://www.langchain.com/blog",
    "https://docs.langchain.com/"
]

# Function executed by each thread
def fetch_content(url):

    # Send GET request to webpage
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Print number of characters fetched
    print(f"Fetched {len(soup.text)} characters from {url}")


# Store all thread objects
threads = []

# Create and start threads
for url in urls:

    # target = function object (NO quotes)
    # args must be a tuple
    thread = threading.Thread(
        target=fetch_content,
        args=(url,)
    )

    threads.append(thread)

    # Start thread execution
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All webpages fetched!!")


"""
Execution Flow:

Main Thread
│
├── Thread 1 → fetch_content(blog_url)
│
├── Thread 2 → fetch_content(docs_url)
│
└── Main Thread waits using join()

After both threads finish:
→ "All webpages fetched!!"

Important Points:

1. target = function name WITHOUT quotes
   Correct: target=fetch_content
   Wrong:   target='fetch_content'

2. args must be a tuple
   args=(url,)

3. start()
   → Starts thread execution

4. join()
   → Waits until thread completes

5. Best Use Cases:
   - Web Scraping
   - API Calls
   - File Reading/Writing
   - Database Queries

6. Multithreading is best for I/O-bound tasks
   because threads spend most of their time waiting.
"""

