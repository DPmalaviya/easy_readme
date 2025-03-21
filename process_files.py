import os
import re

def extract_python_functions(file_path):
    """Extract function names and docstrings from a Python file."""
    functions = []
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        matches = re.findall(r"def (\w+)\(.*?\):\s+\"\"\"(.*?)\"\"\"", content, re.DOTALL)
        for match in matches:
            functions.append({"name": match[0], "docstring": match[1].strip()})
    return functions

# Example usage
if __name__ == "__main__":
    file_path = "example.py"  # Replace with actual file
    print(extract_python_functions(file_path))
