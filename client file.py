import socket

def say_hello(client_socket):
    client_socket.send('1'.encode())
    message = client_socket.recv(1024).decode()
    print(f"Server says: {message}")

def file_transfer(client_socket, file_name):
    client_socket.send('2'.encode())
    client_socket.send(file_name.encode())

    response = client_socket.recv(1024).decode()
    if "File not found" in response:
        print(response)
    else:
        with open(file_name, 'wb') as file:
            data = client_socket.recv(1024)
            while data:
                file.write(data)
                data = client_socket.recv(1024)
        print(f"File '{file_name}' has been received successfully.")

def client_main():
    host = '127.0.0.1' # Loopback address
    port = 12345 # Port to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("1. Say Hello")
    print("2. File Transfer")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        say_hello(client_socket)
    elif choice == '2':
        file_name = input("Enter the name of the file to transfer: ")
        file_transfer(client_socket, file_name)
    else:
        print("Invalid choice.")

    client_socket.close()

if __name__ == "__main__":
    client_main()