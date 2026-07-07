from ai_client import ask_ai
from prompts import SYSTEM_PROMPT

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("🤖 Goodbye!")
        break

    if not user_input:
        continue

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        print("\nAI:\n")

        reply = ask_ai(messages)

        messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        print(e)
