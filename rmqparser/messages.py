import re
from dataclasses import dataclass


@dataclass
class Message:
    id: int
    exchange: str
    routing_key: str
    headers: {}
    raw: str
    lines: [str]
    payload: str


def get_routing_key(lines):
    pass


def get_exchange(lines):
    pass


def get_payload(lines):
    for line in reversed(lines):
        if line.strip():
            return line.strip()


def get_headers(lines):
    headers = {}

    for line in lines:
        m = re.search(r'^(.*):\t(.*)$', line)
        if m is not None:
            headers[m.group(1)] = m.group(2).strip()

    return headers


def get_lines(lines):
    ret = []
    for line in lines:
        ret.append(line.strip())
    return ret


def get_messages(file):
    with open(file, encoding='UTF8') as f:

        msg_to_start_line = {}
        all_lines = f.readlines()

        line_number = 0
        for line in all_lines:
            line_number += 1
            m = re.search(r'^Message\s(\d+)$', line)
            if m is not None:
                msg_to_start_line[m.group(1)] = line_number

        msgs = []

        for index, key in enumerate(msg_to_start_line):
            msg_id = key
            start_line = msg_to_start_line[key] - 1
            end_line = msg_to_start_line[list(msg_to_start_line.keys())[index + 1]] - 1 \
                if index + 1 < len(msg_to_start_line) \
                else line_number

            lines = all_lines[start_line:end_line]
            msg = Message(id=msg_id,
                          lines=get_lines(lines),
                          routing_key=get_routing_key(lines),
                          exchange=get_exchange(lines),
                          payload=get_payload(lines),
                          headers=get_headers(lines),
                          raw="".join(lines),
                          )
            msgs.append(msg)

        return msgs
