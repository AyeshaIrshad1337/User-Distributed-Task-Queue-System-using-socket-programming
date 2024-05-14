import socket

def main():
    host = 'localhost'
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    try:
        while True:
            task = input("Enter a task (format: task_type|arg1|arg2|...): ")
            if task.lower() == "exit":
                break
            client.sendall(task.encode())
            result = client.recv(1024).decode()
            print("Received from server:", result)
    finally:
        client.close()

if __name__ == "__main__":
    main()
