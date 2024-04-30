import socket
from . import router

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8085

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

def start_server():
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()

    # Return an HTTP response
    response = router.handle_request(request)
    client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()




    

