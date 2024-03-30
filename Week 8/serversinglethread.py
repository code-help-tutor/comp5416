WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from socket import *
import uuid

serverPort = 12010
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)




#if __name__ == '__main__':
print ("Server Started ...")
print ("Waiting for other connection ...")
conn_socket, addr = serverSocket.accept()
print ("Connection established, receiving data...")
f = open(str(uuid.uuid4()), 'wb')
l = conn_socket.recv(1024)

while True:
    f.write(l)
    l = conn_socket.recv(1024)
    if len(l)==0:
        break


f.close()

print ("All data received, Connection closed")

conn_socket.close()
