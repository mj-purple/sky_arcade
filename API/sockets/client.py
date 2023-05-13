import test_socket as t
import socket

sock = socket.socket()
try:
    sock.connect((t.HOST, 7322))
except socket.error as e:
    print("hey")
    print(str(e))
 
message = "Hello Server :D"
sock.send(str.encode(message))
