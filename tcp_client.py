import socket
import ssl

target_host = 'www.google.com'
target_port = 443

context = ssl.create_default_context()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_socket:
  with context.wrap_socket(raw_socket, server_hostname = target_host) as client:

    client.connect((target_host, target_port))
    request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n"
    client.sendall(request.encode())

    response = b""

    while True:
      chunk = client.recv(4096)
      if not chunk:
        break
      response += chunk

print(response.decode())
