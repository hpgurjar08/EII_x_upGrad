# Imports 
import google.generativeai as genai

# Import our securely loaded API_KEY from the config file.
from backend.core.config import API_KEY

# Service Setup 
# This line configures the library with your API key.
genai.configure(api_key="AIzaSyAymAPjTFUTkMy6v84PGnsrrOou3eD_wUU")

# This initializes the specific generative model we want to use.
model = genai.GenerativeModel('gemini-2.5-flash-lite')


# Core Function (Synchronous Version) 
def generate_content_from_gemini(prompt: str, original_text: str) -> str:
    """
    Communicates with the Gemini API synchronously.

    Args:
        prompt (str): The specific instruction or question for the AI.
        original_text (str): The user-provided text (e.g., lecture transcript).

    Returns:
        str: The generated content from Gemini, or an error message.
    """
    full_prompt = f"{prompt}:\n\n---\n\n{original_text}"

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"🔴 An error occurred while calling the Gemini API: {e}")
        return "Error: Could not generate content from the AI model."