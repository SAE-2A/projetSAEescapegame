import paho.mqtt.client as mqtt
import time


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

try:
	while(1):
		time.sleep(4)
except KeyboardInterrupt:
	client.loop_stop()
