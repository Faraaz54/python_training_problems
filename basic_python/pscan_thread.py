import socket
import threading
from Queue import Queue

print_lock = threading.Lock()

target = 'Pythonprogramming.net'

server_ip = socket.gethostbyname(target)

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target,port))
        with print_lock:
            print ('port', port ,'is open', threading.currentThread())

    except:
        pass

def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 100):
    q.put(worker)

q.join()
