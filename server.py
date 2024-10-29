from EnMod import *
from os import system
import socket

em = EnMod()

def get_msg():
	m = input("You: ")
	if(m == ""):
		exit()
	if(len(em.parser(m)) == 1):
		m += " "
	return m

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def run_server():

	system("clear || cls")

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_ip = get_ip()
	port = 8000

	server.bind((server_ip, port))
	server.listen(0)

	print(f"Listening on {server_ip}:{port}")

	client_socket, client_address = server.accept()

	print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

	while True:
		request = client_socket.recv(1024)
		request = request.decode("utf-8")
		em.reset()
		em.upload(request)
		try:
			em.decrypt()
		except IndexError:
			print("Connection lost!")
			exit()
		request = em.decrypted()
		print(f"Client: {request}")

		response = get_msg()
		em.reset()
		em.upload(response)
		em.encrypt()
		response = em.encrypted() 
		response = response.encode("utf-8")
		client_socket.send(response)

	client_socket.close()
	print("Connection to client closed.")
	server.close()

run_server()