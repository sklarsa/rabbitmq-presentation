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
        # channel.queue_declare ...
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
        return body
