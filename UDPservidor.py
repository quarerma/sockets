import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Oi UDP Cliente"
bytesToSend = str.encode(msgFromServer)

# Define the calculateExpression function first
def calculateExpression(expression):
    # Format client message
    # Expected operation
    operators = ['+', '-', '*', '/']

    for operator in operators:
        if operator in expression:
            numbers = expression.split(operator)

            num1 = int(numbers[0])
            num2 = int(numbers[1])

            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                return num1 / num2

    return 'Invalid expression'

# Create datagram socket (UDP)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and IP
UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP up e escutando...")

# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('utf-8')  # Decode the incoming bytes to string
    address = bytesAddressPair[1]

    clientMsg = "Mensagem do Cliente:{}".format(message)
    print(clientMsg)
    clientIP = "Endereco IP do Cliente:{}".format(address)
    print(clientIP)

    #Exercicio 1
    # Call the calculateExpression function with the client's message
    #result = calculateExpression(message)

    # Send reply message to client
    #bytesToSend = str.encode(str(result))
    
    UDPServerSocket.sendto(bytesToSend, address)
