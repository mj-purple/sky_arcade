import socket
from _thread import *

HOST = "127.0.0.1"
PORT = 7321

def client_handler(conn):
	while True:
		data = conn.recv(1024)
		message = data.decode('utf-8')
		if message == 'BYE':
			break
		print(message)
	conn.close()

def accept_connections(sock):
	client, addr = sock.accept()
	print('Connected to: ' + addr[0] + ':' + str(addr[1]))
	start_new_thread(client_handler, (client, ))

def start_server():
	sock = socket.socket()
	try:
		sock.bind((HOST, PORT))
	except socket.error as e:
		print(str(e))
	sock.listen()
	while True:
		accept_connections(sock)
start_server()