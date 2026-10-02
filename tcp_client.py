import socket

server_ip = "192.168.10.254"
server_port = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    message = input("Enter a message: ")
    client_socket.sendall(message.encode('utf-8'))

    data = client_socket.recv(1024)
    print(f"Echo from server: {data.decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
