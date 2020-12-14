import sys
import fcntl
import os
import selectors

# set sys.stdin non-blocking
orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)

sel=selectors.DefaultSelector()




def getInput(stdin):
    print("data : "+stdin.read())



sel.register(sys.stdin,selectors.EVENT_READ,getInput)


while True:
    event=sel.select()
    for key,mask in event:
        callback=key.data 
        callback(key.fileobj)