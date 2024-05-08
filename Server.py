import socket

# Entering message
msg = bytes(input("Enter a message: ").encode('utf-8'))

# creating and assigning object to variable
server = socket.socket()
print("Socket Created")

# binding object to a localhost and port number
server.bind(('localhost', 9999))

# Waiting for client to establish connection
server.listen(3)
print("Waiting for connection")

while True:
    # Establishes connection
    client, address = server.accept()
    print("Got connected to", address)
    # Sending message to client
    client.send(msg)

    client.close()