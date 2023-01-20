import time 
import socket

def infra_check():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(('10.33.109.182', 5002))
		data = None 
		while data == None:
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
			
		return data.hex()
	except KeyboardInterrupt:
		sock.close()
