import socket

client = socket.socket()

# here you have to mention the same port n° as in server programming
client.connect(('localhost', 9999))

print(client.recv(1024).decode())