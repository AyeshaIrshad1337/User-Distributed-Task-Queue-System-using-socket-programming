import socket

def main():
    host = 'localhost'
    port = 12345
    worker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker.connect((host, port))
    worker.sendall("worker".encode())  # Identify as worker
    
    while True:
        task = worker.recv(1024).decode()
        if task == "No task":
            print("No new tasks available, waiting...")
            continue
        print(f"Received task: {task}")
        print(f"Processing task: {task}")
        worker.sendall(f"Completed task: {task}".encode())

if __name__ == "__main__":
    main()
