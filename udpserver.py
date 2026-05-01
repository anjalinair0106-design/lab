import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))

data, addr = server_socket.recvfrom(1024)
print("Message:", data.decode())

server_socket.sendto("Hello UDP Client".encode(), addr)