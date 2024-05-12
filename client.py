# import socket
# import json
# import uuid

# # Function to submit tasks
# def submit_task(matrix_a, matrix_b, output_path):
#     # Create a unique task ID
#     task_id = str(uuid.uuid4())
#     print("entered in function")

#     # Divide the matrix multiplication task into two parts
#     task1 = {
#         "task_type": "matrix_multiplication",
#         "matrix_a": matrix_a,
#         "matrix_b": matrix_b,
#         "rows_to_process": [0, 1],  # First half of matrix_a rows
#         "task_id": task_id,
#         "output_path": output_path,
#     }

#     task2 = {
#         "task_type": "matrix_multiplication",
#         "matrix_a": matrix_a,
#         "matrix_b": matrix_b,
#         "rows_to_process": [2, 3],  # Second half of matrix_a rows
#         "task_id": task_id,
#         "output_path": output_path,
#     }

#     # Connect to the server
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(('localhost', 12345))
#     print("Connected to server")
#     # Submit tasks to the server
#     client_socket.sendall(json.dumps(task1).encode())
#     print("task1 sent")
#     client_socket.sendall(json.dumps(task2).encode())
#     print("task2 sent")
#     # Close the socket
#     client_socket.close()

# # Example usage
# if __name__ == "__main__":
#     # Define matrices
#     matrix_a = [[1, 2], [3, 4], [5, 6], [7, 8]]
#     matrix_b = [[5, 6, 7], [8, 9, 10]]
    
#     # Output path (not used in this example)
#     output_path = "D:/User-Distributed-Task-Queue-System-using-socket-programming/result.json"

#     # Submit tasks
#     submit_task(matrix_a, matrix_b, output_path)


import socket
import json
import uuid

# Function to submit tasks
def submit_task(matrix_a, matrix_b, output_path):
    # Create a unique task ID
    task_id = str(uuid.uuid4())

    # Divide the matrix multiplication task into two parts
    task1 = {
        "task_type": "matrix_multiplication",
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "rows_to_process": [0, 1],  # First half of matrix_a rows
        "task_id": task_id,
        "output_path": output_path,
    }

    task2 = {
        "task_type": "matrix_multiplication",
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "rows_to_process": [2, 3],  # Second half of matrix_a rows
        "task_id": task_id,
        "output_path": output_path,
    }

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Submit tasks to the server
    client_socket.sendall(json.dumps(task1).encode())
    client_socket.sendall(json.dumps(task2).encode())
    print("task sent")
    # Close the socket
    client_socket.close()

# Example usage
if __name__ == "__main__":
    # Define matrices
    matrix_a = [[1, 2], [3, 4], [5, 6], [7, 8]]
    matrix_b = [[5, 6, 7], [8, 9, 10]]
    
    # Output path (use backslashes for Windows)
    output_path = "D:/User-Distributed-Task-Queue-System-using-socket-programming/result.json"

    # Submit tasks
    submit_task(matrix_a, matrix_b, output_path)
