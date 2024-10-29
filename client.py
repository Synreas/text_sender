from EnMod import *
from os import system
import socket

em = EnMod()
server_ip = None
server_port = None
client = None

def get_msg():
	m = input("You: ")
	if(m == ""):
		exit()
	if(len(em.parser(m)) == 1):
		m += " "
	return m

def get_ip_port():
	global server_ip, server_port, client
	passed = False
	print("Welcome to TextSender")
	print("-~~~~~~~~~-~~~~~~~~~-")
	while not passed:
		try:
			err_msg = ""
			print("")
			print("choose the server")
			server_ip = input("IP:")
			if(server_ip == ""):
				exit()
			try:
				if len(em.parser(server_ip, ".")) != 4:
					err_msg = "!! enter the ip address correctly"
			except:
				err_msg = "!! enter the ip address correctly"
			server_port = int(input("port:"))
			client.connect((server_ip, server_port))

		except ConnectionRefusedError:
			err_msg = "!! no matching servers"

		except ValueError:
			err_msg = "!! enter port number correctly"

		except (socket.gaierror, OSError):
			err_msg = "!! enter the ip address correctly"

		else:
			passed = True

		print(err_msg)

def run_client():
	system("clear || cls")
	global server_ip, server_port, client

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	get_ip_port()

	print(f"connected to the server!")
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
		try:
			em.decrypt()
		except IndexError:
			print("connection lost!")
			exit()
		response = em.decrypted()
		print(f"Server: {response}")

	client.close()
	print("Connection to server closed")

run_client()
