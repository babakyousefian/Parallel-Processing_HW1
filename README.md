# Parallel-Processing_HW1

---

# 📘 README: Parallel Processing Homework 1

## 🧠 Instructor: Dr. Armin Rashno
## 🧑‍💻 Student: [Babak Yousefian]

This document provides a detailed explanation of all parts of the thread-based parallelism assignment in Python. Each section corresponds to a part of the assignment and describes line-by-line what the code does.

---

## ✅ Part 1: Defining a Thread

```python
import threading

def my_func(index):
    print(f"my_func called by thread N\u00b0{index}")

threads = []
for i in range(10):
    t = threading.Thread(target=my_func, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Explanation:
- `threading` module allows thread management.
- `my_func()` is the target function each thread will execute.
- A list `threads` stores 10 threads.
- Each thread starts and calls `my_func(i)`.
- `join()` ensures all threads finish before the program exits.

---

## ✅ Part 2: Determining the Current Thread

```python
def function_A():
    print("function_A--> starting")
    print("function_A--> exiting")
```

### Explanation:
- Three functions simulate work using print.
- Threads are created for each function and started.
- Demonstrates simple concurrent execution.

---

## ✅ Part 3: Defining a Thread Subclass

```python
class MyThread(threading.Thread):
    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id

    def run(self):
        print(f"---> Thread#{self.thread_id} running, belonging to process ID {os.getpid()}")
        time.sleep(1 + self.thread_id % 3)
        print(f"---> Thread#{self.thread_id} over")
```

### Explanation:
- Subclassing `Thread` allows custom thread behavior.
- `run()` defines what each thread does.
- `os.getpid()` shows the process ID.
- Threads sleep for a random amount (1-3s) to simulate varied workload.
- Timed with `start_time` and `end_time` to show duration.

---

## ✅ Part 4: Thread Synchronization with Lock

```python
lock = threading.Lock()

def thread_task(i):
    with lock:
        print(f"---> Thread#{i} running, belonging to process ID {os.getpid()}")
        time.sleep(1)
        print(f"---> Thread#{i} over")
```

### Explanation:
- Demonstrates how `Lock` ensures only one thread runs critical section.
- Threads print messages in order due to locking.
- Forces serialized execution of critical section.

---

## ✅ Part 5: Thread Synchronization with RLock

```python
rlock = threading.RLock()
items_to_add = 16
items_to_remove = 1
```

### Explanation:
- `RLock` is a reentrant lock that allows a thread to re-acquire it.
- Two functions: one for adding items, another for removing.
- Threads modify shared variables safely with `rlock`.
- Print statements show the state after each operation.

---

## ✅ Part 6: Thread Synchronization with Semaphores

```python
sem = threading.Semaphore(0)
buffer = []
```

### Explanation:
- Simulates producer-consumer pattern.
- `Semaphore` blocks consumers until a producer signals.
- `buffer` holds shared data.
- `lock` ensures only one thread accesses `buffer` at a time.
- Logging includes thread name and timestamp.

---

## ✅ Part 7: Thread Synchronization with Barrier

```python
barrier = threading.Barrier(3)
```

### Explanation:
- `Barrier` blocks threads until a fixed number reach it.
- Three threads reach the barrier before continuing.
- Simulates synchronization point in multithreaded computation.
- Output shows each participant's arrival time.

---

## 🏁 End

This assignment helps understand key threading concepts in Python:
- Basic thread creation
- Synchronization techniques using `Lock`, `RLock`, `Semaphore`, and `Barrier`
- Subclassing threads for advanced control

💡 Tip: Always use thread synchronization when accessing shared resources!

---
