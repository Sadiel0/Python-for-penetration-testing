import socket

# Creating the socket object
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

#Binding to socket
serversocket.bind((host,port))

# listen to TCP server
serversocket.listen(3)

# Starting connection
while True:
    clientsocket, address = serversocket.accept()

    print("Connection recieved from %s" % str(address))

    message = 'Hello! Thank you for connecting to the server. This is an example of how sockects can be used' + '\r\n' 
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()