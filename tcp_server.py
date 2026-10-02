import socket

server_ip = "192.168.10.254"
server_port = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"TCP Echo Server listening on {server_ip}:{server_port}...")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024)
        if data:
            client_socket.sendall(data)
        client_socket.close()
except KeyboardInterrupt:
    pass
finally:
    server_socket.close()
