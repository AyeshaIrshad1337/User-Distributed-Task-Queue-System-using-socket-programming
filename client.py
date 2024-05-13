import socket
import json
import cv2
import base64

# Function to submit image processing task
def submit_image_processing_task(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert image to base64 string
    _, image_encoded = cv2.imencode('.png', image)
    image_base64 = base64.b64encode(image_encoded)

    # Prepare task data
    task_data = {
        "task_type": "image_processing",
        "image_base64": image_base64.decode()  # Decode bytes to convert to string
    }

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Submit task to the server
    client_socket.sendall(json.dumps(task_data).encode())

    # Receive processed image from the server
    processed_image_data = client_socket.recv(4096)
    processed_image_data = json.loads(processed_image_data.decode())

    # Decode processed image from base64
    processed_image_base64 = processed_image_data["processed_image_base64"]
    processed_image_np = base64.b64decode(processed_image_base64)
    processed_image = cv2.imdecode(np.frombuffer(processed_image_np, dtype=np.uint8), cv2.IMREAD_COLOR)

    # Display original and processed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Close the socket
    client_socket.close()

# Example usage
if __name__ == "__main__":
    # Specify the path to the image
    image_path = "image.jpg"

    # Submit image processing task
    submit_image_processing_task(image_path)




# import socket
# import json
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Function to submit image processing task
# def submit_image_processing_task(image_path):
#     # Read the image
#     image = cv2.imread(image_path)
    
#     # Convert image to base64 string
#     _, image_encoded = cv2.imencode('.png', image)
#     image_base64 = image_encoded.tobytes()

#     # Prepare task data
#     task_data = {
#         "task_type": "image_processing",
#         "image_base64": image_base64
#     }

#     # Connect to the server
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(('localhost', 12345))

#     # Submit task to the server
#     client_socket.sendall(json.dumps(task_data).encode())

#     # Receive processed image from the server
#     processed_image_data = client_socket.recv(4096)
#     processed_image_data = json.loads(processed_image_data.decode())

#     # Decode processed image from base64
#     processed_image_base64 = processed_image_data["processed_image_base64"]
#     processed_image_np = np.frombuffer(processed_image_base64, dtype=np.uint8)
#     processed_image = cv2.imdecode(processed_image_np, cv2.IMREAD_COLOR)

#     # Display original and processed images
#     plt.subplot(1, 2, 1)
#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     plt.title('Original Image')

#     plt.subplot(1, 2, 2)
#     plt.imshow(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
#     plt.title('Processed Image')

#     plt.show()

#     # Close the socket
#     client_socket.close()

# # Example usage
# if __name__ == "__main__":
#     # Specify the path to the image
#     image_path = "image.jpg"

#     # Submit image processing task
#     submit_image_processing_task(image_path)



# # import socket
# # import json
# # import uuid

# # # Function to submit tasks
# # def submit_task(matrix_a, matrix_b, output_path):
# #     # Create a unique task ID
# #     task_id = str(uuid.uuid4())
# #     print("entered in function")

# #     # Divide the matrix multiplication task into two parts
# #     task1 = {
# #         "task_type": "matrix_multiplication",
# #         "matrix_a": matrix_a,
# #         "matrix_b": matrix_b,
# #         "rows_to_process": [0, 1],  # First half of matrix_a rows
# #         "task_id": task_id,
# #         "output_path": output_path,
# #     }

# #     task2 = {
# #         "task_type": "matrix_multiplication",
# #         "matrix_a": matrix_a,
# #         "matrix_b": matrix_b,
# #         "rows_to_process": [2, 3],  # Second half of matrix_a rows
# #         "task_id": task_id,
# #         "output_path": output_path,
# #     }

# #     # Connect to the server
# #     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     client_socket.connect(('localhost', 12345))
# #     print("Connected to server")
# #     # Submit tasks to the server
# #     client_socket.sendall(json.dumps(task1).encode())
# #     print("task1 sent")
# #     client_socket.sendall(json.dumps(task2).encode())
# #     print("task2 sent")
# #     # Close the socket
# #     client_socket.close()

# # # Example usage
# # if __name__ == "__main__":
# #     # Define matrices
# #     matrix_a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# #     matrix_b = [[5, 6, 7], [8, 9, 10]]
    
# #     # Output path (not used in this example)
# #     output_path = "D:/User-Distributed-Task-Queue-System-using-socket-programming/result.json"

# #     # Submit tasks
# #     submit_task(matrix_a, matrix_b, output_path)


# import socket
# import json
# import uuid

# # Function to submit tasks
# def submit_task(matrix_a, matrix_b, output_path):
#     # Create a unique task ID
#     task_id = str(uuid.uuid4())

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

#     # Submit tasks to the server
#     client_socket.sendall(json.dumps(task1).encode())
#     client_socket.sendall(json.dumps(task2).encode())
#     print("task sent")
#     # Close the socket
#     client_socket.close()

# # Example usage
# if __name__ == "__main__":
#     # Define matrices
#     matrix_a = [[1, 2], [3, 4], [5, 6], [7, 8]]
#     matrix_b = [[5, 6, 7], [8, 9, 10]]
    
#     # Output path (use backslashes for Windows)
#     output_path = "D:/User-Distributed-Task-Queue-System-using-socket-programming/result.json"

#     # Submit tasks
#     submit_task(matrix_a, matrix_b, output_path)
