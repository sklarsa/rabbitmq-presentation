import pika

EXCHANGE_NAME = 'foo'
QUEUE_NAME = 'bar'


def init_rabbitmq():
    connection = pika.BlockingConnection()
    channel = connection.channel()

    channel.exchange_declare(EXCHANGE_NAME, "topic")
    channel.queue_declare(QUEUE_NAME, durable=True)
    channel.queue_bind(QUEUE_NAME, EXCHANGE_NAME, "*")

    connection.close()


class Producer(object):

    def __init__(self, connection):
        self.connection = connection

    def send_message(self, message, exchange, routing_key):
        channel = self.connection.channel()
        channel.basic_publish(exchange, routing_key, message)
        channel.close()


class Consumer(object):

    def __init__(self, connection):
        self.connection = connection

    def get_message(self, queue):
        channel = self.connection.channel()
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
        return body


def hello_world():
    init_rabbitmq()

    conn = pika.BlockingConnection()

    p = Producer(conn)
    p.send_message("Hello World!", EXCHANGE_NAME, "test")

    c = Consumer(conn)
    print(c.get_message(QUEUE_NAME))


if __name__ == "__main__":
    hello_world()
