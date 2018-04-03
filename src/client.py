import socket
from sys import argv

socket.getaddrinfo('127.0.0.1', argv[1])
infos = socket.getaddrinfo('127.0.0.1', argv[1])
buffer_length = 80

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
socket.getaddrinfo('127.0.0.1', argv[1])
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])

default_msg = 'Hello World'
# Second argument variable is message if inputed
try:
    client.sendall(argv[2].encode('utf8'))
except(IndexError):
    client.sendall(default_msg.encode('utf8'))
except:
    print('Something Really Went Wrong')



message_complete = False

while not message_complete:
    part = client.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
client.close()
