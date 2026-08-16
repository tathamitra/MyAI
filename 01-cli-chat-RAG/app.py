from ai_client import ask_ai
from document_reader import read_document
from prompts import PROMPTS


print("=" * 40)
print("Choose your AI Assistant")
print("=" * 40)

for key, value in PROMPTS.items():
    print(f"{key}. {value['name']}")

choice = input("\nChoice: ")

system_prompt = PROMPTS.get(choice)

if not system_prompt:
    print("Invalid choice.")
    exit()

if choice == "6":
    document_path = input("\nEnter document path: ").strip()

    try:
        document = read_document(document_path)

    except Exception as e:
        print(f"Error reading document: {e}")
        exit()

messages = [
    {
        "role": "system",
        "content": system_prompt["prompt"]
    }
]
if choice == "6":
    messages.append(
        {
            "role": "user",
            "content": f"""
You will answer questions ONLY using the following document.

Document:

{document}
"""
        }
    )

while True:
    # Get user input .Multiple lines can be entered, finish with END on a new line
    print("You (finish with END on a new line):")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    user_input = "\n".join(lines).strip()

    # Check for exit command

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
