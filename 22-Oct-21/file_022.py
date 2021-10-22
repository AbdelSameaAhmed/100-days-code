
# exercise socket
# ex1
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# ---------------------------------pi
print("*"*50)
# ex2
import socket
from socket import socket,AF_INET, SOCK_STREAM
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect('data.pr4e.org', port=80)
cmd = 'GET http://data.pr4e.org/remeo.txt http:/0.1r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()


