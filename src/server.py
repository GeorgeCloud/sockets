from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP
from sys import argv
from time import strftime, gmtime

buffer_length = 80
address = ('127.0.0.1', int(argv[1]))
sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)

#Connection Established
sock.bind(address)
sock.listen(1)
conn, addr = sock.accept()
print("\n--- Listening on port: {} at {} ---\
      ".format(address[1], strftime("%H:%M:%S %d/%m/%Y", gmtime())))

message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    print('{} sent: \t{}'.format(addr[0],part.decode('utf8')))
    if len(part) < buffer_length:
        break
message = 'Message Understood'
conn.sendall(message.encode('utf8'))
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

#Closing Connections
conn.close()
sock.close()

print("\n--- Closing Port: {} at {} ---\
".format(addr[1], strftime("%H:%M:%S %d/%m/%Y", gmtime())))
