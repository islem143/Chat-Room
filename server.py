import socket
import selectors
sel = selectors.DefaultSelector()
ENCODIING = "utf-8"


class Server:
    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)

    def initSocket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)
        s.setblocking(False)
        sel.register(s, selectors.EVENT_READ, data=None)
        self.socket = s
        return s

    def listen(self):
        while True:
            events = sel.select()
            for key, mask in events:
                if(key.data is None):
                    self.acceptNewConnection()
                else:
                    self.serveClient(key)

    def acceptNewConnection(self):
        clientSocket, address = self.socket.accept()
        events = selectors.EVENT_READ
        data = {"adress": address, "userName": ""}
        print(f'Accepted connection from{data["adress"]}')
        userName = self.getuserName(clientSocket)
        data["userName"] = userName
        sel.register(clientSocket, events, data)

    def getuserName(self, socket):
        socket.send(bytes('userName', ENCODIING))
        userName = socket.recv(20)
        print(f'{str(userName,ENCODIING)} has join the chat')
        socket.send(
            bytes(f'{str(userName,ENCODIING)} has join the chat', ENCODIING))
        return str(userName, ENCODIING)

    def serveClient(self, key):
        clientSocket = key.fileobj
        data = key.data
        recivedData = clientSocket.recv(512)
        if(recivedData):
            print(f'Recived Data : {str(recivedData,ENCODIING)}')
            clientSocket.send(bytes(f'{data["userName"]}:{str(recivedData,ENCODIING)}',ENCODIING))
        else:
            print(f'Closing connection to{data["adress"]}')
            clientSocket.close()
            sel.unregister(clientSocket)


server = Server('127.0.0.1', 5053)
try:
    s = server.initSocket()
    server.listen()
except KeyboardInterrupt:
    s.close()
