# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Rutul Amin.
    You are acting on behalf of Rutul Amin who is 35 years old Tech enthusiast and 
    Software engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "who are you?"},
    ],
)

print("Response:", response.choices[0].message.content)
