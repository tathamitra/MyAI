import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

question = input("You: ")

response = client.chat.completions.create(
    model="gpt-4.1-mini",  # Replace with the model you have access to
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful assistant who explains technical topics clearly."
            ),
        },
        {
            "role": "user",
            "content": question,
        },
    ],
)

print("\nAI:\n")
print(response.choices[0].message.content)
