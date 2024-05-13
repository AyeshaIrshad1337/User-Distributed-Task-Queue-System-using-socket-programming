import math
import json
import subprocess

def compute_factorial():
    return math.factorial(100)

def run_simulation():
    with open("params.json", "r") as file:
        params = json.load(file)
    # Assuming the simulation function is already defined or imported
    # For example:
    # result = simulate(params['param1'], params['param2'])
    # return result
    return f"Simulation with params {params} completed"  # Placeholder

def execute_script():
    # This assumes that `calculate_interest.py` takes a command line argument for the filename
    result = subprocess.run(['python', 'calculate_interest.py', 'interest_data.csv'], capture_output=True, text=True)
    return result.stdout

def execute_task(task_type):
    if task_type == 'factorial':
        return compute_factorial()
    elif task_type == 'simulation':
        return run_simulation()
    elif task_type == 'interest_calculation':
        return execute_script()
    else:
        return "Unknown task"

if __name__ == "__main__":
    # Example usage
    print(execute_task('factorial'))
    print(execute_task('simulation'))
    print(execute_task('interest_calculation'))
