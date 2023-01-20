import paho.mqtt.client as mqtt
import time
import json


def on_message(client, userdata, message):
	return
def on_connect(client, userdata, flags, rc):
	print("test")
	return


def send_message(message):
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
	client.publish("test/test", message)
	#try:
	#	while(1):
	#		time.sleep(4)
	#except KeyboardInterrupt:
	client.loop_stop()

def send_rasp(message):

	broker = "10.11.22.123"
	#broker = "192.168.1.49"
	print("nouvelle instance 2")
	client = mqtt.Client("nom_equiement")
	client.on_connect = on_connect
	client.on_message = on_message
	client.username_pw_set("baptiste", "salut")
	client.connect(broker, 1883)
	client.loop_start()
	#tu peux mettre client.subscribe("topic")
	#ou alors si tu veux publish c'est client.publish("topic", "message")
	client.publish("test/test", 'quizz')
	#client.publish("fini/fini", )
	#try:
	#	while(1):
	#		time.sleep(4)
	#except KeyboardInterrupt:
	client.loop_stop()

def send_inscription(message):
	send_message(json.dumps({"type": "inscription", "nom": message}))

def send_success(message):
	send_message(json.dumps({"type": "update", "activite": message, "status": 1}))

