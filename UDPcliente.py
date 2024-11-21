import socket

#Exercicio 1
#message       = input("type the arithmetic operation\n")
bytesToSend         = str.encode(message)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024



# Cria um socket UDP do lado cliente

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Envia msg ao servidor usando o socket UDP criado
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Mensagem vinda do Servidor {}".format(msgFromServer[0])
print(msg)