import socket
import sys

ENCODIING="utf-8"
class Client:
    def connect(self,host,port):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(host),int(port)))
            self.socket=s
            self.listen()
        except OSError as err:
            print(err)
            sys.exit()
    def sendUserName(self):
        userName=input("enter your userName:")
        self.userName=userName
        self.socket.send(bytes(self.userName,ENCODIING))
    def listen(self):
        while True:
            recv_data=self.socket.recv(512)    
            if(str(recv_data,ENCODIING)=="userName"):
                self.sendUserName()
            elif(len(recv_data)>0):
                print(str(recv_data,ENCODIING))
                self.sendMessage()
            else:
                self.socket.close()
                sys.exit()
    def sendMessage(self):
        message=input('enter the messsage: ')
        self.socket.send(bytes(message,ENCODIING))



            

    




client=Client()
client.connect('127.0.0.1',5053)
