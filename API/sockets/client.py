import test_socket as t
import socket

sock = socket.socket()
try:
    sock.connect((t.HOST, t.PORT))
except socket.error as e:
    print(str(e))
 
message = "Hello Server :D"
sock.send(str.encode(message))
sock.send(str.encode("BYE"))