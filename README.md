# RabbitMQ Message Parser

A Python library for parsing rabbitmq messages from text file

Learn more [https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e](https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e)

## Install:
```shell
pip install --upgrade --force-reinstall git+https://github.com/mhewedy/rmq-msg-parser
```

## Usage:
```python
from rmqparser import messages

msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')

for m in msgs:
    if m.headers.get('__Exception_Message__'):
        print(m.id, m.payload, m.headers, m.headers['__Exception_Message__'])

```
