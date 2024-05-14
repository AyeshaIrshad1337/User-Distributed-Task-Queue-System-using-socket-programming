import math
import os
import requests
from bs4 import BeautifulSoup

def compute_factorial(n):
    """Compute the factorial of n."""
    return math.factorial(n)

def add(*args):
    """Add any number of values."""
    return sum(args)

def subtract(a, b, *args):
    """Subtract two or more numbers, starting with the first two."""
    result = a - b
    for arg in args:
        result -= arg
    return result

def multiply(*args):
    """Multiply any number of values."""
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(a, b):
    """Divide the first number by the second. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def sanitize_filename(name):
    """Sanitize filename to remove invalid characters."""
    return "".join(c for c in name if c not in "\\/:*?\"<>|")

def scrape_website(url):
    """Scrape the entire HTML of a website and save it to a file."""
    # Sanitize the filename derived from the URL to ensure it's valid for Windows filesystems.
    filename = sanitize_filename(url.split('//')[-1].replace('/', '_') + '.html')
    filepath = os.path.join('scraped_websites', filename)  # Specify a directory for scraped files
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Ensure the directory exists

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(response.text)
        return f"Webpage saved as {filepath}"
    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Scraping error: {e}"
def scrape_website_content(url):
    """Scrape specific content from a website."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check that the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find the main article content by common tags or classes
        content = soup.find('article') or soup.find('div', class_='main-content')
        if content:
            text_content = content.get_text(separator='\n', strip=True)
            return text_content
        else:
            return "No relevant content found on the page."

    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Scraping error: {e}"
def execute_task(task_type, *args):
    if task_type == 'factorial' and len(args) == 1:
        return compute_factorial(args[0])
    elif task_type == 'add':
        return add(*args)
    elif task_type == 'subtract':
        return subtract(*args)
    elif task_type == 'multiply':
        return multiply(*args)
    elif task_type == 'divide' and len(args) == 2:
        return divide(args[0], args[1])
    elif task_type == 'scrape_website' and len(args) == 1:
        return scrape_website(args[0])
    elif task_type == 'scrape_website_content' and len(args) == 1:
        return scrape_website_content(args[0])
    else:
        return "Unknown task or incorrect parameters"

if __name__ == "__main__":
    # Example usage
    print(execute_task('factorial', 5))  # Calculate factorial of 5
    print(execute_task('add', 1, 2, 3))  # Add 1, 2, and 3
    print(execute_task('subtract', 10, 5, 1))  # Subtract 1 from 5 from 10
    print(execute_task('multiply', 2, 3, 4))  # Multiply 2, 3, and 4
    print(execute_task('divide', 20, 4))  # Divide 20 by 4
    print(execute_task('scrape_website', 'https://www.freecodecamp.org/news/pass-the-github-actions-certification-exam/?ref=dailydev'))
    print(execute_task('scrape_website_content', 'https://www.freecodecamp.org/news/pass-the-github-actions-certification-exam/?ref=dailydev'))
    