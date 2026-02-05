# Few Shot Prompting: Directly giving the inst to the model and few examples to the model
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Read the variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

SYSTEM_PROMPT = """
You should only and only answer the coding related questions and nothing else. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
 "code": "string" or null,
 "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
        return a + b", "isCodingQuestion": false }}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            # "content": "Hey, can you help me by explaining what is Agentic AI",
            "content": "Can you provide rust code to sum 2 numbers?",
            # "content": "What is the Integration in Mathematics?",
        },
    ],
)

print(response.choices[0].message.content)
