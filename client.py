import socket
import threading
import sys
import os

ENCODIING="utf-8"


class Client:
    def connect(self,host,port):
        try:
            userName=input("enter your userName:")
            self.userName=userName
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(host),int(port)))
            self.socket=s
            self.initThreads()
        except OSError as err:
            print(err)
            sys.exit()
    def sendUserName(self):
        self.socket.send(bytes(self.userName,ENCODIING))
    def initThreads(self):
        listenThread=threading.Thread(target=self.listen)
        listenThread.start()
        sendThread=threading.Thread(target=self.sendMessage)
        sendThread.start()
    def listen(self):
        while True:
            recv_data=self.socket.recv(512)    
            if(str(recv_data,ENCODIING)=="userName"):
                self.sendUserName()
            elif(len(recv_data)>0):
                print(str(recv_data,ENCODIING))
            else:
                self.socket.close()
                sys.exit()
    def sendMessage(self):
        while True:
            message=input()
            if len(str(message))>0:
                self.socket.send(bytes(str(message.rstrip()),ENCODIING))
        


            


client=Client()
client.connect('127.0.0.1',5053)



