import requests
import os

GITHUB_API_URL = "https://api.github.com/repos"
MY_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

def get_repo_details(repo_url):
    repo_owner, repo_name = repo_url.rstrip('/').split('/')[-2:]
    headers = {"Authorization": f"token {MY_GITHUB_TOKEN}"}
    
    # Fetch repo metadata
    repo_response = requests.get(f"{GITHUB_API_URL}/{repo_owner}/{repo_name}", headers=headers)
    repo_data = repo_response.json()
    
    if repo_response.status_code != 200:
        return {"error": repo_data.get("message", "Failed to fetch repo details")}

    # Fetch file list
    contents_response = requests.get(f"{GITHUB_API_URL}/{repo_owner}/{repo_name}/contents", headers=headers)
    contents = contents_response.json()

    file_list = [file["name"] for file in contents if "type" in file and file["type"] == "file"]
    
    return {
        "name": repo_data["name"],
        "description": repo_data["description"],
        "language": repo_data["language"],
        "topics": repo_data.get("topics", []),
        "files": file_list
    }

# Example usage
if __name__ == "__main__":
    repo_url = "https://github.com/DPmalaviya/working_code"
    print(get_repo_details(repo_url))
