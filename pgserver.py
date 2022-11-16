import socket

s = socket.socket()
print("Socket successfully created")
port = 40674
s.bind(('',port))
print('Socket is binded to %s'%(port))
s.listen(5)
print("Socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from ',addr)
    c.send(b'Thank you for connection')
    c.close()