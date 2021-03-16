import socket

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(('127.0.0.1',8080))
data=socket.recv(1024)
socket.sendall(data)
socket.close()
print('Received:',data)