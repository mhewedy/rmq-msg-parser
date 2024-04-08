# RabbitMQ Message Parser

A Python library for parsing rabbitmq messages from text file

Learn
more [https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e](https://mohewedy.medium.com/parse-rabbitmq-messages-2b2dec09280e)

## Install:

```shell
pip install --upgrade --force-reinstall git+https://github.com/mhewedy/rmq-msg-parser
```

### Install in non-pip environment:

If your environment doesn't have pip, or you cannot install it, then follow the following steps:

1. create two directories, one for code and other for data
    ```shell
    mkdir data rmqparser
    ```
2. copy the code
   from [rmqparser/messages.py](https://raw.githubusercontent.com/mhewedy/rmq-msg-parser/master/rmqparser/messages.py) into
   rmqparser/messages.py
    ```shell
    vim rmqparser/messages.py
    ```
   then paste the code from the link above
3. copy the messages into data/my_rabbitmq_messages.txt (
   see [data/my_rabbitmq_messages.txt](https://raw.githubusercontent.com/mhewedy/rmq-msg-parser/master/data/my_rabbitmq_messages.py)
   for a reference )
   ```shell
   vim data/my_rabbitmq_messages.txt
   ```
   then paste the messages into the opened vim file
4. copy the code from [main.py](https://raw.githubusercontent.com/mhewedy/rmq-msg-parser/master/main.py) into main.py
    ```shell
    vim main.py
    ```
   then paste the code from the link above
5. run the main.py file
   ```shell
   python main.py
   ```

## Usage:

1. list all messages:

```python
from rmqparser import messages

print('list all messages:')
msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')
for msg in msgs:
    print(f"message id: {msg.id}, payload: {msg.payload}")
```

2. filter by messages that has header contains "error":

```python
from rmqparser import messages

print('\nfilter by messages that has header contains "error":')
msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt', header_key_pattern='error')
for msg in msgs:
    print(f"message id: {msg.id}, payload: {msg.payload}, filtered_headers: {msg.filtered_headers}")
```

3. group messages that has header contains "exception":

```python
from rmqparser import messages

print('\ngroup messages that has header contains "exception":')
grouped_messages = messages.group_by_filtered_headers(r'data/my_rabbitmq_messages.txt', header_key_pattern='exception')
for key, value in grouped_messages.items():
    print("Header:", key)
    for msg in value:
        print(f"message id: {msg.id}, payload: {msg.payload}, filtered_headers: {msg.filtered_headers}")
```
