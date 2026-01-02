import threading
import queue
import time

# Shared priority queue
shared_pq = queue.PriorityQueue()

def producer(thread_id):
    """Thread that adds tasks to the queue"""
    for i in range(3):
        priority = i  # Lower number = higher priority
        task = f"Task from thread {thread_id}, item {i}"
        shared_pq.put((priority, task))
        print(f"Producer {thread_id} added: {task}")
        time.sleep(0.1)

def consumer(thread_id):
    """Thread that processes tasks from the queue"""
    while True:
        try:
            priority, task = shared_pq.get(timeout=2)
            print(f"Consumer {thread_id} processing: {task} (priority: {priority})")
            shared_pq.task_done()
        except queue.Empty:
            break

# Create multiple producer and consumer threads
producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

# Start all threads
for p in producers:
    p.start()
for c in consumers:
    c.start()

# Wait for completion
for p in producers:
    p.join()
for c in consumers:
    c.join()


# Producer 0 added: Task from thread 0, item 0
#
#Consumer 0 processing: 0 priority: 0