import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print('Message reçu :', message)
        except:
            break

    client_socket.close()

def start_chat_client():
    host = '127.0.0.1'  # Adresse IP du serveur
    port = 8000  # Port du serveur

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Votre message : ")
        client_socket.sendall(message.encode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    start_chat_client()