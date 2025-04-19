
import threading
import time
import os
import random
import logging

print("\n--- Part 1: Defining a Thread ---")
def my_func(index):
    print(f"my_func called by thread N\u00b0{index}")

threads = []
for i in range(10):
    t = threading.Thread(target=my_func, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("\n--- Part 2: Determining the Current Thread ---")
def function_A():
    print("function_A--> starting")
    print("function_A--> exiting")

def function_B():
    print("function_B--> starting")
    print("function_B--> exiting")

def function_C():
    print("function_C--> starting")
    print("function_C--> exiting")

threads = []
for func in [function_A, function_B, function_C]:
    t = threading.Thread(target=func)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("\n--- Part 3: Defining a Thread Subclass ---")
class MyThread(threading.Thread):
    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(1 + self.thread_id % 3)
        print(f"---> Thread#{self.thread_id} over")

threads = []
start_time = time.time()
for i in range(1, 10):
    t = MyThread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("End")
print(f"--- {time.time() - start_time} seconds ---")

print("\n--- Part 4: Thread Synchronization with Lock ---")
lock = threading.Lock()
def thread_task(i):
    with lock:
        print(f"---> Thread#{i} running, belonging to process ID {os.getpid()}")
        time.sleep(1)
        print(f"---> Thread#{i} over")

threads = []
start_time = time.time()
for i in range(1, 10):
    t = threading.Thread(target=thread_task, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("End")
print(f"--- {time.time() - start_time} seconds ---")

print("\n--- Part 5: Thread Synchronization with RLock ---")
rlock = threading.RLock()
items_to_add = 16
items_to_remove = 1

def add_items():
    global items_to_add
    while items_to_add > 0:
        with rlock:
            items_to_add -= 1
            print(f"ADDED one item -->{items_to_add} item to ADD")

def remove_items():
    global items_to_remove
    while items_to_remove > 0:
        with rlock:
            items_to_remove -= 1
            print(f"REMOVED one item -->{items_to_remove} item to REMOVE")

print(f"N\u00b0 16 items to ADD\n")
print(f"N\u00b0 1 items to REMOVE\n")
add_thread = threading.Thread(target=add_items)
remove_thread = threading.Thread(target=remove_items)
add_thread.start()
remove_thread.start()
add_thread.join()
remove_thread.join()

print("\n--- Part 6: Thread Synchronization with Semaphores ---")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)s %(levelname)s %(message)s")
buffer = []
sem = threading.Semaphore(0)
lock = threading.Lock()

def consumer():
    with lock:
        if not buffer:
            logging.info("Consumer is waiting")
    sem.acquire()
    with lock:
        item = buffer.pop(0)
        logging.info(f"Consumer notify: item number {item}")

def producer():
    time.sleep(3)
    item = random.randint(100, 1000)
    with lock:
        buffer.append(item)
        logging.info(f"Producer notify: item number {item}")
    sem.release()

threads = []
for i in range(10):
    if i % 2 == 0:
        t = threading.Thread(target=consumer)
    else:
        t = threading.Thread(target=producer)
    threads.append(t)
    t.start()
    time.sleep(1)
for t in threads:
    t.join()

print("\n--- Part 7: Thread Synchronization with Barrier ---")
barrier = threading.Barrier(3)
def race_participant(name):
    print(f"{name} reached the barrier at: {time.ctime()}")
    barrier.wait()

print("START RACE!!!!\n")
threads = []
for name in ["Dewey", "Huey", "Louie"]:
    t = threading.Thread(target=race_participant, args=(name,))
    threads.append(t)
    t.start()
    time.sleep(1)
for t in threads:
    t.join()
print("\nRace over!")
