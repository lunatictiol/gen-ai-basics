from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (looks for .env in current or parent dirs)
load_dotenv()
secret_key = os.getenv('GEMINI_API_KEY')
client = OpenAI(
    api_key=secret_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)