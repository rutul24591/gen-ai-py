#  http://127.0.0.1:8000/docs for docs reference

from fastapi import Body
from fastapi import FastAPI
from ollama import Client

app = FastAPI()

client = Client(host="http://localhost:11434")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Hit http://127.0.0.1:8000/


@app.get("/contact_us")
async def contact_us():
    return {"email": "ramin222@gmail.com"}


# Hit http://127.0.0.1:8000


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# Hit http://127.0.0.1:8000/items/24?q=apple


@app.post("/chat")
def chat(message: str = Body(..., description="Message body")):
    print("REQ message:", message)
    response = client.chat(
        model="gemma:2b", messages=[{"role": "user", "content": message}]
    )
    return {"response": response.message.content}
