import os
from dotenv import load_dotenv, find_dotenv
from google import genai

# Load secret key from .env file
load_dotenv(find_dotenv())
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file!")
    exit(1)

# Initialize the official client
client = genai.Client(api_key=api_key)

# Call an active endpoint model
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Respond with: Local .env key configuration successful!"
)

print("\nModel Output:")
print(response.text)