import threading

def task(value):
    # Code to be executed in the thread
    print("Thread is executing with value:", value)
    
def start():
    print('Inside Multi Threading Using Python')

    # Create multiple threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda val: task(val), args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All threads have completed")
