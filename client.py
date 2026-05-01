import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('127.0.0.1', 12345))

# Send message
client_socket.send("Hello Server!".encode())

# Receive response
response = client_socket.recv(1024).decode()
print("Server says:", response)

# Close connection
client_socket.close()