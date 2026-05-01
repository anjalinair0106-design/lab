import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
server_socket.bind(('127.0.0.1', 12345))

# Listen for connections
server_socket.listen(5)
print("Server is listening...")

# Accept connection
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# Receive data
data = client_socket.recv(1024).decode()
print("Client says:", data)

# Send response
client_socket.send("Hello Anjali".encode())

# Close connection
client_socket.close()
server_socket.close()