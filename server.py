import socket


def parse_request(request):
  """
    Função para analisar a requisição HTTP e extrair o caminho solicitado.
    """
  lines = request.split("\r\n")  # \r retorno \n quebra de linha
  request_line = lines[0]
  method, path, _ = request_line.split(" ")
  return path


def generate_response(path):
  """
    Função para gerar uma resposta HTTP com base no caminho solicitado.
    """
  if path == "/":
    response_body = "Bem-vindo ao servidor HTTP educacional!"
  elif path == "/hello":
    response_body = "Olá! Esta é uma rota de exemplo."
  else:
    response_body = "Página não encontrada."

  # Cabeçalhos da resposta HTTP
  response_headers = [
      "HTTP/1.1 200 OK", "Content-Type: text/plain",
      f"Content-Length: {len(response_body)}", "\r\n"
  ]

  # Concatena cabeçalhos e corpo da resposta
  response = "\r\n".join(response_headers) + response_body
  return response


def run_server():
  """
    Função principal para iniciar o servidor e lidar com as requisições.
    """
  # Configuração do servidor
  host = "127.0.0.1"
  port = 8080

  # Criação do socket do servidor
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((host, port))
  server_socket.listen(1)

  print(f"server_socket: {server_socket}")
  print(f"Servidor HTTP em execução em http://{host}:{port}")

  while True:
    # Aguarda uma conexão
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address}")

    # Recebe os dados da requisição
    request_data = client_socket.recv(1024).decode("utf-8")
    print("Requisição recebida:")
    print(request_data)

    # Analisa a requisição e extrai o caminho
    path = parse_request(request_data)

    # Gera a resposta com base no caminho
    response = generate_response(path)

    # Envia a resposta de volta ao cliente
    client_socket.sendall(response.encode("utf-8"))

    # Fecha a conexão com o cliente
    client_socket.close()


if __name__ == "__main__":
  run_server()
