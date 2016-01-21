import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('133.42.8.45', 6666))
s.listen(5)
conn, addr = s.accept()
while 1:
    reads = conn.recv(1000)
    print reads
    conn.sendall('server : ' + reads)