import pika

EXCHANGE_NAME = "my-exchange"
QUEUE_NAME = "my-queue"


def init_rabbitmq():
    conn = pika.BlockingConnection()
    chan = conn.channel()

    chan.exchange_declare(EXCHANGE_NAME, "direct")
    chan.queue_declare(QUEUE_NAME, durable=True)
    chan.queue_bind(QUEUE_NAME, EXCHANGE_NAME, "routing.key")

    conn.close()


class Producer(object):

    def __init__(self, conn):
        self.connection = conn

    def send_message(self, msg, exch, routing_key):
        chan = self.connection.channel()
        chan.basic_publish(exch, routing_key, msg)
        chan.close()


class Consumer(object):

    def __init__(self, conn):
        self.connection = conn

    def get_message(self, queue):
        chan = self.connection.channel()
        method_frame, _, body = chan.basic_get(queue)
        if method_frame:
            chan.basic_ack(method_frame.delivery_tag)
        return body


def hello_world():
    init_rabbitmq()

    conn = pika.BlockingConnection()

    p = Producer(conn)
    p.send_message("Hello World!", EXCHANGE_NAME, "routing.key")

    c = Consumer(conn)
    print(c.get_message(QUEUE_NAME))


if __name__ == "__main__":
    hello_world()
