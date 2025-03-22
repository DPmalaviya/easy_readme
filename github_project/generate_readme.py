import os
import google.generativeai as genai
from fetch_repo import get_repo_details  

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_readme_with_gemini(repo_details):
    prompt = f"""
    Generate a structured README.md for a GitHub repository. remove "markdown" and "code" tags from the output.
    The README should be informative, engaging, and tailored to the following repository details:

    Project Name: {repo_details['name']}
    Description: {repo_details['description']}
    Main Language: {repo_details['language']}
    Technologies Used: {', '.join(repo_details['topics'])}
    Key Files: {', '.join(repo_details['files'])}
    Example File Contents: {repo_details['file_contents']}

    Maximize your creativity and provide a detailed, informative, and engaging README that includes sections like:
    """

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    return response.text


def save_readme_to_file(content, output_path="github_project/README.md"):
    try:
        with open(output_path, "w") as readme_file:
            readme_file.write(content)
        print(f"README.md file has been successfully created at {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the README file: {e}")

if __name__ == "__main__":
    link = input("Enter the GitHub repository URL: ")
    sample_repo = get_repo_details(link)
    if not sample_repo:
        print("Failed to fetch repository details.")
        exit(1)
    readme_content = generate_readme_with_gemini(sample_repo)
    save_readme_to_file(readme_content)