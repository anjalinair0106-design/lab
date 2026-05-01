import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto("Hello Server".encode(), ('127.0.0.1', 12345))

data, _ = client_socket.recvfrom(1024)
print("Server says:", data.decode())