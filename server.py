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

def run_server():

	system("clear || cls")

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_ip = "192.168.2.59"
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