import os
import asyncio
from aio_pika import connect, Message, DeliveryMode

async def publish_message(queue_name, message_body):
    # Carregando as credenciais e o host a partir de variáveis de ambiente
    rabbitmq_user = os.getenv("RABBITMQ_USER", "default_user")
    rabbitmq_password = os.getenv("RABBITMQ_PASSWORD", "default_password")
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")  # Nome do serviço Docker

    try:
        # Estabelecendo a conexão com o RabbitMQ
        connection = await connect(f"amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}/")
        async with connection:
            channel = await connection.channel()
            message = Message(
                body=message_body.encode(),
                delivery_mode=DeliveryMode.PERSISTENT,
            )
            await channel.default_exchange.publish(
                message, routing_key=queue_name
            )
            print(f"Message published to queue '{queue_name}': {message_body}")
    except Exception as e:
        print(f"Failed to publish message: {e}")


