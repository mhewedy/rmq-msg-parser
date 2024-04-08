from rmqparser import messages

print('list all messages:')
msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt')
for msg in msgs:
    print(f"message id: {msg.id}, payload: {msg.payload}")

print('\nfilter by messages that has header contains "error":')
msgs = messages.get_messages(r'data/my_rabbitmq_messages.txt', header_key_pattern='error')
for msg in msgs:
    print(f"message id: {msg.id}, payload: {msg.payload}, filtered_headers: {msg.filtered_headers}")

print('\ngroup messages that has header contains "exception":')
grouped_messages = messages.group_by_filtered_headers(r'data/my_rabbitmq_messages.txt', header_key_pattern='exception')
for key, value in grouped_messages.items():
    print("Header:", key)
    for msg in value:
        print(f"message id: {msg.id}, payload: {msg.payload}, filtered_headers: {msg.filtered_headers}")
