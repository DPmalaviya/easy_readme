import requests
import os
import json  # Import the JSON module

GITHUB_API_URL = "https://api.github.com/repos"
MY_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

def get_repo_details(repo_url):
    repo_owner, repo_name = repo_url.rstrip('/').split('/')[-2:]
    headers = {"Authorization": f"token {MY_GITHUB_TOKEN}"}
    
    repo_response = requests.get(f"{GITHUB_API_URL}/{repo_owner}/{repo_name}", headers=headers)
    repo_data = repo_response.json()
    
    if repo_response.status_code != 200:
        return {"error": repo_data.get("message", "Failed to fetch repo details")}

    contents_response = requests.get(f"{GITHUB_API_URL}/{repo_owner}/{repo_name}/contents", headers=headers)
    contents = contents_response.json()

    file_list = []
    file_contents = {}

    for file in contents:
        if "type" in file and file["type"] == "file":
            file_list.append(file["name"])
            
            # Fetch file content
            file_content_response = requests.get(file["download_url"], headers=headers)
            if file_content_response.status_code == 200:
                file_contents[file["name"]] = file_content_response.text
    return {
        "name": repo_data["name"],
        "description": repo_data["description"],
        "language": repo_data["language"],
        "topics": repo_data.get("topics", []),
        "files": file_list,
        "file_contents": file_contents 
    }


def summarize_code(file_contents):
    """
    Summarize the code content from the repository.

    Args:
        file_contents (dict): A dictionary where keys are file names and values are the file contents.

    Returns:
        dict: A dictionary where keys are file names and values are the summarized content.
    """
    summaries = {}

    for file_name, content in file_contents.items():
        lines = content.splitlines()
        summary = []
        in_docstring = False
        docstring_lines = []

        for line in lines:
            line = line.strip()

            # Capture module-level comments
            if line.startswith("#") and not summary:
                summary.append(line)

            # Capture function definitions
            elif line.startswith("def "):
                summary.append(line)
                in_docstring = False  # Reset docstring flag

            # Capture class definitions
            elif line.startswith("class "):
                summary.append(line)
                in_docstring = False  # Reset docstring flag

            # Capture docstrings (single-line or multi-line)
            elif line.startswith('"""') or line.startswith("'''"):
                if not in_docstring:
                    in_docstring = True
                    docstring_lines = [line]
                else:
                    in_docstring = False
                    docstring_lines.append(line)
                    summary.append(" ".join(docstring_lines))  # Add the full docstring
                    docstring_lines = []

            # Continue capturing multi-line docstrings
            elif in_docstring:
                docstring_lines.append(line)

        # Limit the summary to the first 15 lines for brevity
        summaries[file_name] = "\n".join(summary[:15])
    return summaries

def save_repo_details_to_json(repo_details, output_path="repo_details.json"):
    try:
        with open(output_path, "w") as json_file:
            json.dump(repo_details, json_file, indent=4)  
        print(f"Repository details have been successfully saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the repository details to JSON: {e}")

if __name__ == "__main__":
    repo_url = "https://github.com/ramitsurana/deeplearning-notebooks"
    repo_details = get_repo_details(repo_url)
    code_summaries = summarize_code(repo_details["file_contents"])
    repo_details["code_summaries"] = code_summaries # Add code summaries to the repo details
    # save_repo_details_to_json(repo_details)