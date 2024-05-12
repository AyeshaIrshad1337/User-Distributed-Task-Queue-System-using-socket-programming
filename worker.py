import socket
import json
import numpy as np

# Function to start the worker
def start_worker():
    worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker_socket.connect(('localhost', 12345))
    print("Connected to server")

    while True:
        # Receive a task from the server
        task_data = worker_socket.recv(4096).decode()
        task = json.loads(task_data)
        print(f"Received task: {task}")
        # Process the task and get the result
        result = process_task(task)
        print(f"Result for task {task['task_id']}: {result}")
        # Send the result back to the server
        worker_socket.sendall(json.dumps(result).encode())

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
        print(f"Partial result for task {task['task_id']}: {partial_result}")
        # Convert partial result to list and return
        return {
            "status": "success",
            "task_id": task["task_id"],
            "result": partial_result.tolist()
        }

    # If task type is not recognized, return an error message
    return {"status": "error", "message": "Unknown task type"}

# Run the worker
if __name__ == "__main__":
    start_worker()
