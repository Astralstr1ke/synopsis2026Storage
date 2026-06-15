import socket
import time


host = ''
port = 5560
connectedDevice = ''

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    connectedDevice =''
    connectedDevice =("$Connected to: " + address[0] + ":" + str(address[1]))
    return conn


def dataTransfer(conn):
        
            data = conn.recv(1024) # receive the data
            data = data.decode('utf-8')
            data += ' ' + connectedDevice
            message=data
            HOST, PORT = "NestServer", 5560
            sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            sock.send(message)
            sock.close
            
        

s = setupServer()

while True:
    try:
        
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break