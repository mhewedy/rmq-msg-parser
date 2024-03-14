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
    # Find headers with "exception" (case-insensitive) in their names
    exception_headers = {k: v for k, v in m.headers.items() if k.lower().find("exception") != -1}

    # Check if any exception headers were found
    if exception_headers:
        print(f"Message ID: {m.id}")
        print(f"Payload: {m.payload}")

        # Print only the exception headers
        print(f"Exception Headers:")
        for k, v in exception_headers.items():
            print(f"\t{k}: {v}")

        print("\n")
```
