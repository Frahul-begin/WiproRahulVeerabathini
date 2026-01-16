import threading

def task():
    print("Thread is running")
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task, args=("Thread",))
t2.start()
t1.start()
t1.join()
t2.join()

print("main thread ends")
