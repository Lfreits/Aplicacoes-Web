import socket

def send_http_request(host, port, path="/"):
    # Criação do socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
      # Conecta ao servidor
      client_socket.connect((host, port))

      # Monta a requisição HTTP
      request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"

      # Envia a requisição ao servidor
      client_socket.sendall(request.encode("utf-8"))

      # Recebe a resposta do servidor
      response = client_socket.recv(1024).decode("utf-8")

      print(f"Resposta do servidor:\n{response}")

    finally:
      # Fecha a conexão do cliente
      client_socket.close()


if __name__ == "__main__":
    # Configurações do servidor
    server_host = "127.0.0.1"
    server_port = 8080

    # Envia uma requisição para o caminho "/"
    # send_http_request(server_host, server_port, "/")

    # Envia uma requisição para o caminho "/hello"
    send_http_request(server_host, server_port, "/hello")

    # Envia uma requisição para uma rota desconhecida "/xyz"
    # send_http_request(server_host, server_port, "/xyz")
