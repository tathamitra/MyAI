import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"
SYSTEM_PROMPT = (
    "You are a helpful assistant who explains technical topics clearly."
)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not found."
client = Groq( api_key=api_key)

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
            print("🤖 Bot: Goodbye! Have a great day! 👋")
            break
    if not user_input:
     continue

    try:
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        print("\nAI:\n")
        print(response.choices[0].message.content)
    except Exception as e:
        print(e)
