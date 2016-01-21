import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('133.42.8.45', 6666))
chat = ['hi', 'hello', 'one', 'two', 'three', 'four']

while 1:
    c = chat[random.randint(0,5)]
    print c
    s.sendall('client :' + c)
    print s.recv(1000)
    time.sleep(1)