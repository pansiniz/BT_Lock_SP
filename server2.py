# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 

# import sqlite for database functions
import sqlite3

code = '12345'
  
print_lock = threading.Lock() 
  
# thread fuction 
def threaded(c): 
    grant = 'granted'
    deny = 'denied'
    while True: 
  
        ## data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Broken pipe on socket') 
              
            # lock released on exit 
            print_lock.release() 
            break
    
        print(data.decode())
        dataArray = data.decode()
        dataArray = data.decode().split("|")
        print(dataArray[0])
        print(dataArray[1])
        print(dataArray[2])
        print(dataArray[3])
        #conn = sqlite3.connect('acl_master.db')
        #c = conn.cursor()
        #c.ex
        if (data.decode()==code):
            
            c.send(grant.encode())
        else:
            # send back denial string to client 
            c.send(deny.encode())
            
        c.close()
        print_lock.release()
        break
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket bound to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main()
