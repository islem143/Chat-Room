import socket
import selectors
import sys
import fcntl
import os

sel = selectors.DefaultSelector()
ENCODIING="utf-8"


class Client:
    def connect(self,host,port):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((str(host),int(port)))
            self.socket=s
            sel.register(s,selectors.EVENT_READ,self.listen)
            #self.listen()
        except OSError as err:
            print(err)
            sys.exit()
    def sendUserName(self):
        userName=input("enter your userName:")
        self.userName=userName
        self.socket.send(bytes(self.userName,ENCODIING))
        # set sys.stdin non-blocking
        orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
        fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)
        sel.register(sys.stdin,selectors.EVENT_READ,client.sendMessage)
    def listen(self):
            recv_data=self.socket.recv(512)    
            if(str(recv_data,ENCODIING)=="userName"):
                self.sendUserName()
            elif(len(recv_data)>0):
                print(str(recv_data,ENCODIING))
            else:
                self.socket.close()
                sys.exit()
    def sendMessage(self,stdin):
        message=stdin.read()
        if len(str(message))>0:
            self.socket.send(bytes(str(message),ENCODIING))
        


            


client=Client()
client.connect('127.0.0.1',5053)


while True:
    events=sel.select()
    for key,mask in events:
        if(key.data==client.listen):
            callback=key.data
            callback()
        elif(key.data==client.sendMessage):
            callback=key.data
            callback(key.fileobj)


