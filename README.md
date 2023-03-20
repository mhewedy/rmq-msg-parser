# RabbitMQ Message Parser

## Install:
```shell
pip install git+https://github.com/mhewedy/rmq_msg_parser
```

## Usage:
```python
from rmqparser.messages import get_messages

msgs = get_messages(r'data/my_rabbitmq_messages.txt')

for m in msgs:
    print(m.payload, m.headers)

```