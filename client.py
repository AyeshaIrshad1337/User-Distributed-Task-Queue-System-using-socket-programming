import socket

def main():
    host = 'localhost'
    port = 12345
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    while True:
        task = input("Enter a task: ")
        if task.lower() == "worker":
            print("Invalid task name 'worker'. Please enter a different task.")
            continue
        client.sendall(task.encode())
        if task.lower() == "exit":
            break

if __name__ == "__main__":
    main()
