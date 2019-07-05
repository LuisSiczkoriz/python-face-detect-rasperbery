import socket

HOST = ''
PORT = 57000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
arq = open('/home/backup/foo.tar.gz', 'w')

while 1:
    dados = conn.recv(1024)
    if not dados:
        break
    arq.write(dados)

arq.close()
conn.close()