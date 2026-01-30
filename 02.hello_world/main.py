from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Responsible to reading the dotenv file. use pip3 install python-dotenv to install
client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o-mini", input="Write a one-sentence bedtime story about a unicorn."
# )

response = client.responses.create(
    model="gpt-4o-mini", input="Hey I'm Rutul Amin! How are you doing today?"
)

print(response.output_text)
