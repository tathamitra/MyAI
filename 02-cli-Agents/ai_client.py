from time import time

from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def ask_ai(messages):
    stream = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        stream=True,
    )

    full_response = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            print(content, end="", flush=True)
            full_response += content


    print()

    return full_response
