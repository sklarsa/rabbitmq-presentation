import pika
from pika.exceptions import ChannelClosed

from amqp_example import init_rabbitmq, Producer, Consumer, QUEUE_NAME, EXCHANGE_NAME

EXCHANGE_WITH_AE = "exchange-with-ae"
AE_NAME = "my-ae"


def ae_example():

    # Just for convenience, use the same setup as the amqp_example
    init_rabbitmq()

    connection = pika.BlockingConnection()

    # Send a message with a bad routing key
    p = Producer(connection)
    p.send_message("Hello World!", EXCHANGE_NAME, "bad.routing.key")

    # Consume a message from the queue.  This returns None since the message was routed incorrectly
    c = Consumer(connection)
    if not c.get_message(QUEUE_NAME):
        print("No message on queue: %s" % QUEUE_NAME)

    # Attempt to modify the existing exchange to add an alternate exchange.
    # This will fail because you cannot change the properties of an existing exchange through exchange_declare
    # You can modify the exchange using rabbitmqctl
    try:
        channel = connection.channel()
        channel.exchange_declare(EXCHANGE_NAME, "topic", arguments={"alternate-exchange": AE_NAME})
    except ChannelClosed:
        print("Not allowed to alter the properties of an existing exchange...")

    channel = connection.channel()

    # Declare a new exchange with the alternate-exchange argument
    channel.exchange_declare(EXCHANGE_WITH_AE, "topic", arguments={"alternate-exchange": AE_NAME})
    # Declare the alternate exchange
    channel.exchange_declare(AE_NAME, "fanout")
    # Bind both exchanges to the queue
    channel.queue_bind(QUEUE_NAME, EXCHANGE_WITH_AE, "routing.key")
    channel.queue_bind(QUEUE_NAME, AE_NAME, "")
    channel.close()

    # Now, the message with the bad routing key gets routed to the alternate exchange, which routes
    # the message to the correct queue
    p.send_message("Hello World!", EXCHANGE_WITH_AE, "bad.routing.key")
    print(c.get_message(QUEUE_NAME))

    connection.close()


if __name__ == "__main__":
    ae_example()
