import socket
import time
from task import execute_task

def main():
    host = 'localhost'
    port = 12345
    worker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker.connect((host, port))
    worker.sendall("worker".encode())

    last_heartbeat = time.time()
    while True:
        if time.time() - last_heartbeat > 30:
            worker.sendall("heartbeat".encode())
            last_heartbeat = time.time()

        try:
            worker.settimeout(1)  # Set timeout for socket
            task = worker.recv(1024).decode()
        except socket.timeout:
            continue  # Handle timeout by continuing the loop

        if task == "No task":
            print("No new tasks available, waiting...")
            continue

        task_details = task.split('|')
        task_type = task_details[0]
        task_args = map(eval, task_details[1:])  # Convert arguments from strings to appropriate types

        print(f"Received task: {task}")
        # Use execute_task to dynamically run tasks
        result = execute_task(task_type, *task_args)
        print(f"Processed result: {result}")
        
        worker.sendall(f"Completed task: {task}. Result: {result}".encode())

if __name__ == "__main__":
    main()
