import socket
import json
import cv2
import numpy as np
import socket
import json
import base64

import socket
import json
import cv2
import base64

# Function to submit image processing task
# Function to submit image processing task
def submit_image_processing_task(image_path, server_address):
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        # Convert image to base64 string
        _, image_encoded = cv2.imencode('.png', image)
        image_base64 = base64.b64encode(image_encoded).decode()

        # Prepare task data
        task_data = {
            "task_type": "image_processing",
            "image_base64": image_base64
        }

        # Connect to the server
        worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        worker_socket.connect(server_address)

        # Submit task to the server
        worker_socket.sendall(json.dumps(task_data).encode())

        # Close the socket
        worker_socket.close()

    except Exception as e:
        print(f"Error submitting task: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the path to the image
    image_path = "image.jpg"

    # Specify the server address
    server_address = ('localhost', 12345)

    # Submit image processing task to the server
    # ubmit_image_processing_task(image_path, server_address)


    # Submit image processing task to the server
    processed_image_base64 = submit_image_processing_task(image_path, server_address)

    # If processed image data is received, proceed with further processing
    if processed_image_base64 is not None:
        # Decode and display the processed image
        processed_image_np = base64.b64decode(processed_image_base64)
        processed_image = cv2.imdecode(np.frombuffer(processed_image_np, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Processed Image', processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




# # Function to submit image processing task
# def submit_image_processing_task(image_base64, server_address):
#     # Prepare task data
#     task_data = {
#         "task_type": "image_processing",
#         "image_base64": image_base64.decode()  # Decode bytes to convert to string
#     }

#     # Connect to the server
#     worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     worker_socket.connect(server_address)

#     # Submit task to the server
#     worker_socket.sendall(json.dumps(task_data).encode())

#     # Receive processed image from the server
#     processed_image_data = worker_socket.recv(4096)
#     processed_image_data = json.loads(processed_image_data.decode())

#     # Close the socket
#     worker_socket.close()

#     return processed_image_data

# # Example usage
# if __name__ == "__main__":
#     # Specify the path to the image
#     image_path = "image.jpg"

#     # Read the image
#     with open(image_path, "rb") as file:
#         image_base64 = base64.b64encode(file.read())

#     # Specify the server address
#     server_address = ('localhost', 12345)

# import socket
# import json
# import cv2
# import base64

# # Function to submit image processing task
# def submit_image_processing_task(image_path, server_address):
#     # Read the image
#     image = cv2.imread(image_path)
    
#     # Convert image to base64 string
#     _, image_encoded = cv2.imencode('.png', image)
#     image_base64 = base64.b64encode(image_encoded).decode()

#     # Prepare task data
#     task_data = {
#         "task_type": "image_processing",
#         "image_base64": image_base64
#     }

#     # Connect to the server
#     worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     worker_socket.connect(server_address)

#     # Submit task to the server
#     worker_socket.sendall(json.dumps(task_data).encode())

#     # Close the socket
#     worker_socket.close()

# # Example usage
# if __name__ == "__main__":
#     # Specify the path to the image
#     image_path = "image.jpg"

#     # Specify the server address
#     server_address = ('localhost', 12345)

#     # Submit image processing task to the server
    

#     # Submit image processing task to the server
#     processed_image_data =  submit_image_processing_task(image_path, server_address)


#     # Decode processed image from base64
#     processed_image_base64 = processed_image_data["processed_image_base64"]
#     processed_image_np = np.frombuffer(processed_image_base64, dtype=np.uint8)
#     processed_image = cv2.imdecode(processed_image_np, cv2.IMREAD_COLOR)

#     # Display original and processed images
#     cv2.imshow('Original Image', image)
#     cv2.imshow('Processed Image', processed_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()



# import socket
# import json
# import numpy as np

# # Function to start the worker
# def start_worker():
#     worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     worker_socket.connect(('localhost', 12345))
#     print("Connected to server")

#     while True:
#         # Receive a task from the server
#         task_data = worker_socket.recv(4096).decode()
#         task = json.loads(task_data)
#         print(f"Received task: {task}")
#         # Process the task and get the result
#         result = process_task(task)
#         print(f"Result for task {task['task_id']}: {result}")
#         # Send the result back to the server
#         worker_socket.sendall(json.dumps(result).encode())

# # Function to process tasks
# def process_task(task):
#     if task.get("task_type") == "matrix_multiplication":
#         # Convert matrices from task to numpy arrays
#         matrix_a = np.array(task["matrix_a"])
#         matrix_b = np.array(task["matrix_b"])

#         # Get the rows to process
#         rows_to_process = task["rows_to_process"]

#         # Perform matrix multiplication on the specified rows
#         partial_result = np.dot(matrix_a[rows_to_process], matrix_b)
#         print(f"Partial result for task {task['task_id']}: {partial_result}")
#         # Convert partial result to list and return
#         return {
#             "status": "success",
#             "task_id": task["task_id"],
#             "result": partial_result.tolist()
#         }

#     # If task type is not recognized, return an error message
#     return {"status": "error", "message": "Unknown task type"}

# # Run the worker
# if __name__ == "__main__":
#     start_worker()


