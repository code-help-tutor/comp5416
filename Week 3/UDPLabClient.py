WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from socket import *

serverName = '127.0.0.1'
serverPort = 12003
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
message = message.encode('utf-8')
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
