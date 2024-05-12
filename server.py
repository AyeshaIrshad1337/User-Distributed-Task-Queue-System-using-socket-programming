# import socket
# import threading
# import queue
# import json
# import numpy as np

# # Task queue
# task_queue = queue.Queue()

# # List of connected workers
# workers = []

# # Partial results storage
# partial_results = {}

# # Mutex for shared resources
# lock = threading.Lock()

# # Function to handle worker connections
# def handle_worker_connection(worker_socket, worker_id):
#     print("enter in this function")
#     while True:
#         try:
#             # Get a task from the task queue
#             task = task_queue.get()
#             if task is None:
#                 break
            
#             # Add worker ID to the task
#             task["worker_id"] = worker_id
            
#             # Send the task to the worker
#             worker_socket.sendall(json.dumps(task).encode())

#             # Receive the result from the worker
#             result_data = worker_socket.recv(4096).decode()
#             result = json.loads(result_data)
            
#             # Process the result
#             with lock:
#                 if result["status"] == "success":
#                     partial_results[result["task_id"]].append(result["result"])
                
#                 # Check if both results are received
#                 if len(partial_results[result["task_id"]]) == 2:
#                     # Combine the partial results
#                     final_result = np.vstack(partial_results[result["task_id"]])

#                     # Output the final result (e.g., print, save to file)
#                     print(f"Final result of task {result['task_id']}: {final_result}")

#                     # Clean up partial results
#                     del partial_results[result["task_id"]]

#         except ConnectionResetError:
#             # Handle worker disconnect
#             print(f"Worker {worker_id} disconnected")
#             with lock:
#                 workers.remove((worker_socket, worker_id))
#             break

# # Function to start the server
# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('localhost', 12345))
#     server_socket.listen(5)
#     print("Server listening on port 12345")

#     worker_id = 0
#     while True:
#         # Accept a new worker connection
#         worker_socket, _ = server_socket.accept()
#         worker_id += 1
#         print(f"New worker {worker_id} connected")
        
#         # Add the worker to the list
#         with lock:
#             workers.append((worker_socket, worker_id))
        
#         # Start a new thread to handle the worker connection
#         threading.Thread(target=handle_worker_connection, args=(worker_socket, worker_id)).start()

# # Run the server
# if __name__ == "__main__":
#     start_server()


import socket
import threading
import queue
import json
import numpy as np

# Task queue
task_queue = queue.Queue()

# List of connected workers
workers = []

# Mutex for shared resources
lock = threading.Lock()

# Function to handle worker connections
def handle_worker_connection(worker_socket, worker_id):
    while True:
        try:
            # Get a task from the task queue
            task_data = worker_socket.recv(4096).decode()
            task = json.loads(task_data)
            if task is None:
                break

            # Process the task and get the result
            result = process_task(task)

            # Send the result back to the client
            worker_socket.sendall(json.dumps(result).encode())

        except ConnectionResetError:
            # Handle worker disconnect
            print(f"Worker {worker_id} disconnected")
            with lock:
                workers.remove((worker_socket, worker_id))
            break

# Function to process tasks
def process_task(task):
    if task.get("task_type") == "matrix_multiplication":
        # Convert matrices from task to numpy arrays
        matrix_a = np.array(task["matrix_a"])
        matrix_b = np.array(task["matrix_b"])

        # Get the rows to process
        rows_to_process = task["rows_to_process"]

        # Perform matrix multiplication on the specified rows
        partial_result = np.dot(matrix_a[rows_to_process], matrix_b)

        # Convert partial result to list
        result = {
            "task_id": task["task_id"],
            "result": partial_result.tolist()
        }

        # Save result to output file
        output_path = task["output_path"]
        with open(output_path, "a") as file:
            file.write(json.dumps(result) + "\n")

        return result

    # If task type is not recognized, return an error message
    return {"status": "error", "message": "Unknown task type"}

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
