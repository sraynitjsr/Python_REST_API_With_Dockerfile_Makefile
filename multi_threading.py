import threading

def task():
    # Code to be executed in the thread
    print("Thread critical section")
    
def start():
    print('Inside Multi Threading Using Python')

    # Create multiple threads
    threads = []
    for _ in range(5):
        t = threading.Thread(target=task)
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads have completed")
