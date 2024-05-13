import socket
import threading
from queue import Queue

task_queue = Queue()

def client_handler(conn, addr):
    while True:
        task = conn.recv(1024).decode()
        if not task or task.lower() == 'quit':
            break
        print(f"Received task from {addr}: {task}")
        task_queue.put(task)
    conn.close()

def worker_handler(conn, addr):
    while True:
        if not task_queue.empty():
            task = task_queue.get()
            conn.send(task.encode())
            print(f"Sent task to worker {addr}: {task}")
            response = conn.recv(1024).decode()
            print(f"Received from worker {addr}: {response}")
        else:
            # Send a "No task" message and then wait for a moment
            conn.send("No task".encode())
            threading.Event().wait(5)  # Wait for 5 seconds before checking again

def main():
    host = 'localhost'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Server is listening...")
    
    while True:
        conn, addr = server.accept()
        initial_msg = conn.recv(1024).decode()
        if initial_msg == "worker":
            threading.Thread(target=worker_handler, args=(conn, addr)).start()
        else:
            threading.Thread(target=client_handler, args=(conn, addr)).start()
            task_queue.put(initial_msg)  # Handle the case where the first message is a task

if __name__ == "__main__":
    main()
