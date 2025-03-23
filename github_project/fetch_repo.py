import requests
import os
import json  
import re

GITHUB_API_URL = "https://api.github.com/repos"
GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

def get_repo_contents(owner, repo, path=""):
    """Recursively fetch all files in a GitHub repo, including subfolders."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"{GITHUB_API_URL}/{owner}/{repo}/contents/{path}"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    contents = response.json()
    all_files = []

    for item in contents:
        if item["type"] == "file" and item["name"].endswith(".py"):
            file_data = fetch_python_file(owner, repo, item["path"])  # Read Python file
            all_files.append({"path": item["path"], "content": file_data})
        elif item["type"] == "dir":
            all_files.extend(get_repo_contents(owner, repo, item["path"]))  # Recursive call

    return all_files

def fetch_python_file(owner, repo, file_path):
    """Fetch and extract function definitions and comments from a Python file."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"{GITHUB_API_URL}/{owner}/{repo}/contents/{file_path}"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return ""

    file_content = response.json().get("content", "")
    return extract_definitions_and_comments(file_content)

def extract_definitions_and_comments(content):
    """Extract function definitions and comments from Python file content."""
    import base64
    decoded_content = base64.b64decode(content).decode("utf-8", errors="ignore")

    functions = re.findall(r"def (\w+)\(.*?\):", decoded_content)  # Extract function names
    comments = re.findall(r"# (.+)", decoded_content)  # Extract inline comments
    
    summary = {
        "functions": functions,
        "comments": comments[:10]  # Limit to avoid too much text
    }
    
    return summary

def get_repo_details(repo_url):
    """Extract owner and repo name from URL and fetch all Python file summaries."""
    owner, repo = repo_url.rstrip('/').split('/')[-2:]
    files = get_repo_contents(owner, repo)
    
    return {"name": repo, "owner": owner, "files": files}



def save_repo_details_to_json(repo_details, output_path="repo_details.json"):
    try:
        with open(output_path, "w") as json_file:
            json.dump(repo_details, json_file, indent=4)  
        print(f"Repository details have been successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the repository details to JSON: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/Avadh-Ladani-0/LeetCode_Practice"
    repo_details = get_repo_details(repo_url)
    print(repo_details)
    # save_repo_details_to_json(repo_details)