# The Hare Wins the Race: Getting the most out of RabbitMQ in distributed applications

## Setting up the environment

#### Mac

Install using Homebrew
```
brew install rabbitmq
```

Add RabbitMQ to launchctl to launch the broker on startup (Optional)
```
ln -sfv /usr/local/opt/rabbitmq/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.rabbitmq.plist
```

## Examples
|Path|Description|How to run|
|----|-----------|----------|
|amqp\_example.py|Basic broker communication using pika|`python amqp_example.py`|
|celery\_example\_1|Celery example with default config|`cd celery_example_1; ./run_example.sh`|
|celery\_example\_2|Celery example with advanced routing|`cd celery_example_2; ./run_example.sh`|
|ae\_example.py|Alternate exchange usage to catch unrouted messages|`python ae_example.py`|


## Links

#### AMQP and RabbitMQ
* https://www.amqp.org/
* http://www.rabbitmq.com/

#### Python Packages
* https://github.com/celery/librabbitmq 
* https://github.com/celery/py-amqp
* https://github.com/pika/pika
* https://github.com/celery/kombu

#### Celery
* http://celeryproject.org/


