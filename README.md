# RabbitMQ Message Parser

A Python library for parsing rabbitmq messages from text file

## Install:
```shell
pip install --upgrade --force-reinstall git+https://github.com/mhewedy/rmq-msg-parser
```

## Usage:
```python
from rmqparser import messages

msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')

for m in msgs:
    print(m.payload, m.headers)

```
