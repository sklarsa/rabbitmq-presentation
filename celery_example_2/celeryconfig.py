from kombu import Queue, Exchange
from routers import default_router

broker_url = 'amqp://guest:guest@localhost:5672/'
imports = ('neural_net.tasks', 'webapp.tasks', )
result_backend = 'db+sqlite:///results.db'

smart_exchange = Exchange('smart', 'topic')

task_routes = (default_router, )
task_queues = (
    Queue('neural_net', exchange=smart_exchange, routing_key='neural_net.#'),
    Queue('webapp', exchange=smart_exchange, routing_key='webapp.#'),
)
