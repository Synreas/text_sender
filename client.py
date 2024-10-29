from EnMod import *
from os import system
import socket

em = EnMod()

def get_msg():
	m = input("You: ")
	if(len(em.parser(m)) == 1):
		m += " "

	return m

def run_client():

	system("clear || cls")

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_ip = "127.0.01"
	server_port = 8000

	print("Welcome to TextSender")
	print("-~~~~~~~~~-~~~~~~~~~-")
	print("")
	print("choose the server")
	server_ip = input("IP:")
	server_port = int(input("port:"))

	client.connect((server_ip, server_port))
	print(f"connected to the client!")
	print("")

	while True:

		em.reset()
		msg = get_msg()
		em.upload(msg)
		em.encrypt()
		msg = em.encrypted()
		client.send(msg.encode("utf-8")[:1024])

		response = client.recv(1024)
		response = response.decode("utf-8")
		em.reset()
		em.upload(response)
		em.decrypt()
		response = em.decrypted()

		if(response.lower() == "close"):
			break

		print(f"Server: {response}")

	client.close()
	print("Connection to server closed")

run_client()
