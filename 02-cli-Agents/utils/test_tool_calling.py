import json

from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME


client = Groq(api_key=GROQ_API_KEY)


def calculator(a, b):
    return a + b


def multiply(a, b):
    return a * b


# Python tool registry
tool_functions = {
    "calculator": calculator,
    "multiply": multiply,
}


# Tool definitions given to the LLM
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

    # Ask the LLM what to do
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    message = response.choices[0].message

    # If the LLM does not need a tool,
    # we have reached the final answer.
    if not message.tool_calls:
        print("Final answer:", message.content)
        break

    # Save the LLM's tool request(s) in the conversation
    messages.append(message)

    # Process every tool requested by the LLM
    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("LLM requested tool:", tool_name)
        print("Arguments:", arguments)

        # Find the actual Python function
        tool_function = tool_functions[tool_name]

        # Execute the tool
        result = tool_function(
            arguments["a"],
            arguments["b"],
        )

        print("Tool result:", result)

        # Send the tool result back to the LLM
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result),
            }
        )
