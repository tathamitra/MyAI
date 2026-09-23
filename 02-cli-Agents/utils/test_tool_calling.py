import json

from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME


client = Groq(api_key=GROQ_API_KEY)


def calculator(a, b):
    return a + b


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
    }
]


messages = [
    {
        "role": "user",
        "content": "What is 10 + 20?",
    }
]


# Step 1: Ask the LLM
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=messages,
    tools=tools,
)

message = response.choices[0].message


# Step 2: Check whether the LLM requested a tool
if message.tool_calls:

    tool_call = message.tool_calls[0]

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print("LLM requested tool:", tool_name)
    print("Arguments:", arguments)

    # Step 3: Execute the actual Python function
    if tool_name == "calculator":
        result = calculator(
            arguments["a"],
            arguments["b"],
        )

    print("Tool result:", result)

    # Step 4: Send the tool result back to the LLM
    messages.append(message)

    messages.append(
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result),
        }
    )

    # Step 5: Ask the LLM for the final answer
    final_response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    print("Final answer:", final_response.choices[0].message.content)
