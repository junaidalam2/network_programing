import socket
import threading
from queue import Queue, Empty

target = '127.0.0.1'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target, port))
        sock.close()
        return True
    except OSError:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while True:
        try:
            port = queue.get_nowait()
        except Empty:
            break

        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)

        queue.task_done()


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("open ports: ", open_ports)

