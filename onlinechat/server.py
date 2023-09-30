import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print('Message reçu :', message)
                client_socket.sendall('Message reçu : {}'.format(message).encode('utf-8'))
        except:
            break

    client_socket.close()

def start_chat_server():
    host = '127.0.0.1'  # Adresse IP locale
    port = 8000  # Port à écouter

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Limite de connexions en attente

    print('Le serveur de chat est démarré sur {}:{}'.format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print('Nouvelle connexion établie :', addr)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    start_chat_server()