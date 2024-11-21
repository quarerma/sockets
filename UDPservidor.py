import socket
import time

localIP = "127.0.0.1"
localPort = 3333
bufferSize = 1024

# Buffer parameters
buffer = []
buffer_max_length = 10
buffer_reset_time = 60  # seconds
buffer_expiry_time = None

msgFromServer = "Oi UDP Cliente"
bytesToSend = str.encode(msgFromServer)

# Create datagram socket (UDP)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and IP
UDPServerSocket.bind((localIP, localPort))

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


print("Servidor UDP up e escutando...")

# Reset buffer after the expiry time
def reset_buffer():
    global buffer, buffer_expiry_time
    if buffer_expiry_time and time.time() >= buffer_expiry_time:
        buffer.clear()
        buffer_expiry_time = None
        print("Buffer has been cleared.")

# Serialize the string to buffer and handle adding numbers to buffer
def serialize_string_to_buffer(message):
    numbers = message.split()  # Split the string into a list by spaces
    try:
        numbers = [int(num) for num in numbers]  # Convert to integers
    except ValueError:
        return "Invalid input. Please send only numbers separated by spaces."

    # Add numbers to the buffer
    if len(buffer) < buffer_max_length:
        space_available = buffer_max_length - len(buffer)
        buffer.extend(numbers[:space_available])
        return f"Buffer updated. Current size: {len(buffer)} / {buffer_max_length}"
    else:
        return "Buffer is full. Cannot add more items."

# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('utf-8')  # Decode the incoming bytes to string
    address = bytesAddressPair[1]

    # Exercicio 1
    # Call the calculateExpression function with the client's message
    # result = calculateExpression(message)

    # Exercicio 2
    # Send reply message to client
    # bytesToSend = str.encode(str(result))

    reply_message = serialize_string_to_buffer(message)
    UDPServerSocket.sendto(str.encode(reply_message), address)
