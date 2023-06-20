import threading

# Global variable to synchronize odd and even threads
lock = threading.Lock()
current_number = 1
final_number = 10

def print_odd_numbers():
    global current_number

    while current_number < final_number:
        if current_number % 2 != 0:
            with lock:
                print("Odd Thread:", current_number)
                current_number += 1

def print_even_numbers():
    global current_number

    while current_number <= final_number:
        if current_number % 2 == 0:
            with lock:
                print("Even Thread:", current_number)
                current_number += 1

def start():
    print('Inside Printing Odd Even From Alternative Threads in Python')
    
    # Create odd and even threads
    odd_thread = threading.Thread(target=print_odd_numbers)
    even_thread = threading.Thread(target=print_even_numbers)

    # Start the threads
    odd_thread.start()
    even_thread.start()

    # Wait for both threads to complete
    odd_thread.join()
    even_thread.join()

    print("All threads have completed")
