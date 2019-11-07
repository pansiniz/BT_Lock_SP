# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 

# import sqlite for database functions
import sqlite3

import datetime as dt


code = '696969'
  
print_lock = threading.Lock() 
  
# thread fuction 
def threaded(c): 
    while True: 
        conn = sqlite3.connect('acl_master.db')
        co = conn.cursor()
        co.execute('''create table if not exists active_codes
            (room, name, code, end date)''')
        #co.execute("insert into active_codes values (100,'Test',12345,'2019-31-12')")
        conn.commit()
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Broken pipe on socket') 
              
            # lock released on exit 
            print_lock.release() 
            break
    
        dataArray = data.decode().split("|")
       
        print(data.decode())   # debug only format should be 'room|name|code|endDate
        print(dataArray[0])    # debug only
        print(dataArray[2])    # debug only
       
        recdRoomNum = dataArray[0]
        recdCode = dataArray[2]
        
        for rows in co.execute('select * from active_codes where trim(room) LIKE ? AND trim(code)=?', (recdRoomNum, recdCode)):
            lineParams = str(co.fetchone()).split(",")
            lineParams[3].replace(")","") 
            print(lineParams[3])
            
            
        
        
        #if:
        #    grant = 'granted|', endDate
        #    c.send(grant.encode())
        #else:
            # send back denial string to client 
        #    deny = 'denied|', endDate
        #    c.send(deny.encode())
            
        co.close()
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
