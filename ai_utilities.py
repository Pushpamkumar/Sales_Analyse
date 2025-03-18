import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    """
    Generates AI-powered responses using OpenAI's API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    user_input = input("Ask me something: ")
    print(generate_response(user_input))
