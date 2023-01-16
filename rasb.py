import paho.mqtt.client as mqtt
import time
import serial
import socket

def on_message(client, userdata, message):
	return
def on_connect(client, userdata, flags, rc):
	return


broker = "10.11.22.123"
print("nouvelle instance")
client = mqtt.Client("nom_equiement")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("baptiste", "salut")
client.connect(broker, 1883)
client.loop_start()
#tu peux mettre client.subscribe("topic")
#ou alors si tu veux publish c'est client.publish("topic", "message")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.33.109.122', 8880))
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		



try:
	while(1):
		time.sleep(4)
except KeyboardInterrupt:
	client.loop_stop()
	sock.close()