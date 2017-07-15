import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'Pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request)
result = s.recv(4096)

print result

