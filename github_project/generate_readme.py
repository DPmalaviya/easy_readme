from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
# Configure the Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_readme_with_gemini(repo_details):
    # Create a prompt for the README generation
    prompt = f"""
    Generate a structured README.md for a GitHub repository.

    Project Name: {repo_details['name']}
    Description: {repo_details['description']}
    Main Language: {repo_details['language']}
    Technologies Used: {', '.join(repo_details['topics'])}
    Key Files: {', '.join(repo_details['files'])}

    The README should include an Introduction, Installation Guide, Usage Instructions, and Features.
    """

    # Create the model configuration
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 50,
        "max_output_tokens": 1024,
        "response_mime_type": "text/plain",
    }

    # Initialize the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start a chat session and send the prompt
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    # Return the generated README content
    return response.text

# Example usage
if __name__ == "__main__":
    sample_repo = {
        "name": "Sample Project",
        "description": "An example project",
        "language": "Python",
        "topics": ["flask", "machine-learning"],
        "files": ["app.py", "requirements.txt"]
    }

    readme_content = generate_readme_with_gemini(sample_repo)
    print(readme_content)