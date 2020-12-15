# import sys
# import fcntl
# import os
# import selectors
import threading

# # set sys.stdin non-blocking
# orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
# fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)

# sel=selectors.DefaultSelector()




# def getInput(stdin):
#     message=stdin.read()
#     print("qsdqsd+"+str(message))



# sel.register(sys.stdin,selectors.EVENT_READ,getInput)


# while True:
#     event=sel.select()
#     for key,mask in event:
#         callback=key.data 
#         callback(key.fileobj)

def listen1():
    cmd1=input('input1> ')
    print(cmd1)

def listen2():
    cmd2=input('input2> ')
    print(cmd2)



t1=threading.Thread(target=listen1)
t2=threading.Thread(target=listen2)
t1.start()
t2.start()
print('hello')