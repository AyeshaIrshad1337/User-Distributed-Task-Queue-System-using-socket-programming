# User-Distributed-Task-Queue-System-using-socket-programming  
This project aims to create a task distribution system where a single client can submit tasks and the server will automatically distribute the tasks to workers. The goal is to efficiently allocate tasks and ensure timely completion of work. This system will help streamline the task management process and improve overall productivity.


## Prerequisites
- Python 3.10 installed on your system.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Create a Virtual Environment

3. Create a virtual environment by executing the following command:
    ```
    python3.10 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```

### Install Dependencies

5. Install the required dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```

## Running the System

Make sure to run the server, worker, and client in the specified order for the system to work properly.

1. Open a terminal and navigate to the project directory.
2. Run the server by executing the following command:
    ```
    python server.py
    ```

3. Finally, open another terminal and navigate to the project directory.
4. Run the client by executing the following command:
    ```
    python client.py
    ```
