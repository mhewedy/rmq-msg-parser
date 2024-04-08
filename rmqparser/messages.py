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
    filtered_headers: {}


def __get_routing_key(lines):
    pass


def __get_exchange(lines):
    pass


def __get_payload(lines):
    for line in reversed(lines):
        if line.strip():
            return line.strip()


def __get_headers(lines):
    headers = {}

    for line in lines:
        m = re.search(r'^(.*):\t(.*)$', line)
        if m is not None:
            headers[m.group(1)] = m.group(2).strip()

    return headers


def __get_lines(lines):
    ret = []
    for line in lines:
        ret.append(line.strip())
    return ret


def get_messages(file, header_key_pattern=None):
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
            headers = __get_headers(lines)

            if header_key_pattern is None or any(
                    re.search(header_key_pattern, header_key, re.IGNORECASE) for header_key in headers.keys()):
                msg = Message(id=msg_id,
                              lines=__get_lines(lines),
                              routing_key=__get_routing_key(lines),
                              exchange=__get_exchange(lines),
                              payload=__get_payload(lines),
                              headers=headers,
                              raw="".join(lines),
                              filtered_headers=
                              {key: value
                               for key, value in headers.items()
                               if header_key_pattern is not None and re.search(header_key_pattern, key, re.IGNORECASE)
                               }
                              )
                msgs.append(msg)

        return msgs


def group_by_filtered_headers(file, header_key_pattern: str):
    msgs = get_messages(file, header_key_pattern)
    grouped_messages = {}

    for msg in msgs:
        for fh in msg.filtered_headers.keys():
            grouped_messages.setdefault(fh, []).append(msg)

    return grouped_messages
