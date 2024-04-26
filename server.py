import socket
import threading
import queue
import json
import numpy as np

# Task queue
task_queue = queue.Queue()

# List of connected workers
workers = []

# Partial results storage
partial_results = {}

# Mutex for shared resources
lock = threading.Lock()

# Function to handle worker connections
def handle_worker_connection(worker_socket, worker_id):
    while True:
        try:
            # Get a task from the task queue
            task = task_queue.get()
            if task is None:
                break
            
            # Add worker ID to the task
            task["worker_id"] = worker_id
            
            # Send the task to the worker
            worker_socket.sendall(json.dumps(task).encode())

            # Receive the result from the worker
            result_data = worker_socket.recv(4096).decode()
            result = json.loads(result_data)
            
            # Process the result
            with lock:
                if result["status"] == "success":
                    partial_results[result["task_id"]].append(result["result"])
                
                # Check if both results are received
                if len(partial_results[result["task_id"]]) == 2:
                    # Combine the partial results
                    final_result = np.vstack(partial_results[result["task_id"]])

                    # Output the final result (e.g., print, save to file)
                    print(f"Final result of task {result['task_id']}: {final_result}")

                    # Clean up partial results
                    del partial_results[result["task_id"]]

        except ConnectionResetError:
            # Handle worker disconnect
            print(f"Worker {worker_id} disconnected")
            with lock:
                workers.remove((worker_socket, worker_id))
            break

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    worker_id = 0
    while True:
        # Accept a new worker connection
        worker_socket, _ = server_socket.accept()
        worker_id += 1
        print(f"New worker {worker_id} connected")
        
        # Add the worker to the list
        with lock:
            workers.append((worker_socket, worker_id))
        
        # Start a new thread to handle the worker connection
        threading.Thread(target=handle_worker_connection, args=(worker_socket, worker_id)).start()

# Run the server
if __name__ == "__main__":
    start_server()
