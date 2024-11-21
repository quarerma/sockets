import socket

# Exercicio 1
# message = input("type the arithmetic operation\n")
serverAddressPort = ("127.0.0.1", 3333)
bufferSize = 1024

# Cria um socket UDP do lado cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    #Exercicio 2 e 3
    # Get user input
    #message = input("Type a message to send to the server: ")
    payload = input('Type a series of space-separated numbers to store in the Buffer:')
    
    # Envia msg ao servidor usando o socket UDP criado
    UDPClientSocket.sendto(str.encode(payload), serverAddressPort)
    
    # Receive response from the server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Mensagem vinda do Servidor {}".format(msgFromServer[0].decode('utf-8'))
    print(msg)
    
    
