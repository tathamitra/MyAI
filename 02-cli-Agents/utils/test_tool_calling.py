import json

from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME


client = Groq(api_key=GROQ_API_KEY)


def calculator(a, b):
    return a + b


def multiply(a, b):
    return a * b


tool_functions = {
    "calculator": calculator,
    "multiply": multiply,
}


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        },
    },
]


messages = [
    {
        "role": "user",
        "content": "Add 10 and 20, then multiply the result by 5.",
    }
]


# Agent loop
while True:

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    message = response.choices[0].message

    if not message.tool_calls:
        print("Final answer:", message.content)
        break

    tool_call = message.tool_calls[0]

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print("LLM requested tool:", tool_name)
    print("Arguments:", arguments)

    tool_function = tool_functions[tool_name]

    result = tool_function(
        arguments["a"],
        arguments["b"],
    )

    print("Tool result:", result)

    messages.append(message)

    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result),
        }
    )
