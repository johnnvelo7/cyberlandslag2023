import json
import sys

data = {'email': 'example@example.com', 'uniqueid': 1679874056}
data_string = json.dumps(data)
data_length = len(data_string.encode('utf-8'))

print('JSON payload:', data_string)
print('Payload length (bytes):', data_length)

