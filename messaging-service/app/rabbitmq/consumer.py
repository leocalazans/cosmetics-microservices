import os
import asyncio
from aio_pika import connect

async def consume_messages():
    rabbitmq_user = os.getenv("RABBITMQ_USER", "default_user")
    rabbitmq_password = os.getenv("RABBITMQ_PASSWORD", "default_password")
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")  

    try:
        connection = await connect(f"amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}/")
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue("my_queue")

            async for message in queue:
                async with message.process():
                    print(f"Received message: {message.body.decode()}")
    except Exception as e:
        print(f"Failed to consume messages: {e}")
