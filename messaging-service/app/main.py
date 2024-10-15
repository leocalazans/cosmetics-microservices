from .rabbitmq import publish_message, consume_messages
from fastapi import FastAPI

app = FastAPI(title="API Menssageria",
    description="Api para menssageria interna",
    version="1.0.0")

@app.on_event("startup")
async def startup_event():
    await consume_messages()  # Começar a consumir mensagens ao iniciar o serviço

@app.post("/publish")
async def publish(msg: str):
    await publish_message("my_queue", msg)
    return {"status": "Message published"}
