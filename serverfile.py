import socket
import os

def say_hello(client_socket):
    message = "Hello from the server!"
    client_socket.send(message.encode())

def file_transfer(client_socket):
    file_name = client_socket.recv(1024).decode()
    try:
        with open(file_name, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
        print(f"File '{file_name}' has been sent successfully.")
    except FileNotFoundError:
        error_message = f"File '{file_name}' not found."
        client_socket.send(error_message.encode())

def server_main():
    host = '127.0.0.1' # Loopback address
    port = 12345 # Port to bind to

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        operation = client_socket.recv(1024).decode()

        if operation == '1':
            say_hello(client_socket)
        elif operation == '2':
            file_transfer(client_socket)
        else:
            print("Invalid operation code received.")

        client_socket.close()

if __name__ == "__main__":
    server_main()