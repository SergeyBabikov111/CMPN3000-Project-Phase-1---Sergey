import socket

server_ip = "192.168.10.254"
server_port = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"UDP Echo Server listening on {server_ip}:{server_port}...")

try:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received from {client_address[0]}: {data.decode('utf-8')}")
        server_socket.sendto(data, client_address)
except KeyboardInterrupt:
    print("\nShutting down.")
finally:
    server_socket.close()
