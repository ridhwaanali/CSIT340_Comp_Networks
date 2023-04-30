
from socket import *
import threading


def serveClient(tcpConnectionSock,clientCount):
    print("Serving Client %d "%(clientCount))
    while True:
        sentence = tcpConnectionSock.recv(1024).decode()
        if(sentence.lower() == 'quit'):
            break
        else:
            capitalizedSentence = sentence.upper()
            tcpConnectionSock.send(capitalizedSentence.encode())
    print(" Client Has Left "%(clientCount,clientCount))



class ServerThread(threading.Thread):
    def __init__(self,tcpConnectionSocket,clientNum):
        self.tcpConnectionSocket = tcpConnectionSocket
        self.clientNum = clientNum
        threading.Thread.__init__(self)

    def run(self):
        serveClient(self.tcpConnectionSocket,self.clientNum)

clientCount = 0
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("The server is ready to receive.")
    clientCount += 1 # client counter. Not neccessary. Its just for my own sanity. Lol
    connectionSocket, addr = serverSocket.accept()
    t = ServerThread(connectionSocket,clientCount)
    t.start()
connectionSocket.close()
