import pika

def publish_event(event):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='cart_events', exchange_type='fanout')

    channel.basic_publish(exchange='cart_events', routing_key='', body=event)
    connection.close()
