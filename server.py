import socket
import threading
from queue import Queue
from task import execute_task  # Import the execute_task function

task_queue = Queue()
active_workers = {}
worker_lock = threading.Lock()
worker_id_counter = 0

def parse_task(task_string):
    parts = task_string.split('|')
    task_type = parts[0]
    if task_type in ['factorial','add', 'subtract', 'multiply', 'divide']:
        args = map(int, parts[1:])  # Convert args to integers for arithmetic tasks
    else:
        args = parts[1:]  # Keep args as strings for tasks like web scraping
    return task_type, list(args)
def client_handler(conn, addr):
    while True:
        try:
            task = conn.recv(1024).decode()
            if not task or task.lower() == 'quit':
                conn.close()
                break
            print(f"Received task from {addr}: {task}")
            task_queue.put((task, conn))
            manage_workers()
        except Exception as e:
            print(f"Error with client {addr}: {str(e)}")
            break

def worker_handler(worker_id):
    global worker_id_counter
    with worker_lock:
        active_workers[worker_id] = True
        print(f"Worker {worker_id} started. Total workers: {len(active_workers)}")

    try:
        while True:
            task, client_conn = task_queue.get(block=True)
            task_type, args = parse_task(task)
            result = execute_task(task_type, *args)
            result_message = f"{task} Result: {result}"
            print(f"Worker {worker_id} completed task: {task} with result: {result_message}")
            try:
                client_conn.sendall(result_message.encode())
            except Exception as e:
                print(f"Failed to send result to client by Worker {worker_id}: {str(e)}")
    finally:
        with worker_lock:
            del active_workers[worker_id]
            print(f"Worker {worker_id} stopped. Remaining workers: {len(active_workers)}")

def manage_workers():
    global worker_id_counter
    with worker_lock:
        if len(active_workers) <= task_queue.qsize():
            worker_id_counter += 1
            threading.Thread(target=worker_handler, args=(worker_id_counter,), daemon=True).start()

def main():
    host = 'localhost'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server is listening...")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=client_handler, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
