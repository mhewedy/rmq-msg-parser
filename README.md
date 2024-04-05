# RabbitMQ Message Parser

A Python library for parsing rabbitmq messages from text file

Learn more [https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e](https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e)

## Install:
```shell
pip install --upgrade --force-reinstall git+https://github.com/mhewedy/rmq-msg-parser
```
### Install in non-pip envirnoment:
If your environment doesn't have pip, or you cannot install it, then follow the following steps:

1. create two directories, one for code and other for data
    ```shell
    mkdir data rmqparser
    ```
2. copy the code from [messages.py](https://raw.githubusercontent.com/mhewedy/rmq-msg-parser/master/rmqparser/messages.py) into rmqparser/messages.py
    ```shell
    vim rmqparser/messages.py
    ```
    then paste the code from the link above
3. copy the messages into data/my_rabbitmq_messages.txt
   ```shell
   vim data/my_rabbitmq_messages.txt
   ```
   then paste the messages into the opened vim file
4. create a main from the code in the [usage section](README.md#usage) below:
   ```shell
   vim main.py
   ```
   then copy and paste the code from the usage section below
5. run the main.py file
   ```shell
   python main.py
   ```
   should see result similar to
   ```shell
   Message ID: 1
   Payload: {"id":13}
   Exception Headers:
	   ExceptionMessage: no data found
	   ExceptionStackTrace: com.commons.integrations.Exception: no data found
   ```


## Usage:

1. Print any message that has an exception header:
```python
from rmqparser import messages

msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')

for m in msgs:
    # Find headers with "exception" (case-insensitive) in their names
    exception_headers = {k: v for k, v in m.headers.items() if k.lower().find("exception") != -1}

    # Check if any exception headers were found
    if exception_headers:
        print(f"\nmessage id: {m.id}, payload: {m.payload}")

        # Print only the exception headers
        print(f"exception Headers:")
        for k, v in exception_headers.items():
            print(f"\t{k}: {v}")
```
2. Print any message that has an exception header, **grouped by the exception header**:
```python
from rmqparser import messages

msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')

messages_by_exception = {}

for m in msgs:
    exception_headers = {k: v for k, v in m.headers.items() if k.lower().find("exception") != -1}
    if exception_headers:
        for h in exception_headers.values():
            messages_by_exception.setdefault(h, [m]).append(m)

for exception, exception_messages in messages_by_exception.items():
    print(f'\n********** exception: "{exception}", occurrence: {len(exception_messages)} **********')

    for message in exception_messages:
        print(f"message id: {message.id}, payload: {message.payload}")
```
