import socket

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('0.0.0.0',8080))
socket.listen(1)
conn,addr=socket.accept()
conn.sendall('the first message'.encode('utf-8'))
socket.close()
