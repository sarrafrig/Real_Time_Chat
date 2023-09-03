import socket

HOST = 'localhost'  # Replace with your PC server's IP address
PORT = 8765
connected_clients = {}

def handle_client(client_socket):
    print("Client connected:", client_socket.getpeername())

    while True:
        DATA = client_socket.recv(1024)
        username = DATA.decode("utf-8")
        print("Username connected:", username)

        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            print(f"From [{username}]:", message.decode("utf-8"))

            server_message = input("Enter a message to send to the client: ")
            client_socket.send(server_message.encode())

    print("Client disconnected:", client_socket.getpeername())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("Server listening on {}:{}".format(HOST, PORT))

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()