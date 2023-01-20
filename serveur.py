import paho.mqtt.client as mqtt
import time
import mysql.connector
import json

def on_message(client, userdata, message):
	print("reçu")
	print(message.payload.decode("utf-8"))
	info = json.loads(str(message.payload.decode("utf-8"))) # dès qu'on reçoit un message on le met dans une variable
	print(str(info))
	if  info["type"] == "inscription":
		s = info["nom"]
		requete1= ("""CREATE TABLE IF NOT EXISTS %s (activite VARCHAR(40), status INT);"""% s)
		requete2= ("""INSERT INTO %s VALUES ("BLE", 0);"""% s)
		requete3 = ("""INSERT INTO %s VALUES ("IR", 0)"""% s)
		requete4 = ("""INSERT INTO %s VALUES ("CODE", 0)"""% s)
		cursor.execute(requete1)
		cursor.execute(requete2)
		cursor.execute(requete3)
		cursor.execute(requete4)
		con.commit()
		print("inscription faite")
	if info["type"] == "update":
		infor = (info["nom"], info["status"], info["activite"])
		requete = ("""UPDATE %s SET status = %s WHERE activite = '%s'"""% infor)
		print(requete)
		cursor.execute(requete)
		con.commit()
		client.publish("fini/fini", info["activite"])
def on_connect(client, userdata, flags, rc):
	print("connexion ok")
broker="10.11.22.123" #ip du serveur MQTT
print("nouvelle instance")
client = mqtt.Client("Serv_escape") #On se définit comme étant un client
client.on_connect = on_connect
client.on_message = on_message # on initialise la fonction prédéfinis on_message
client.username_pw_set("baptiste", "salut")
client.connect(broker, 1883) # on se connecte au serveur MQTT
client.loop_start() # on commence une boucle
client.subscribe("test/test") # on se met sur le canal de discussion publish/infos
con = mysql.connector.connect(user="baptiste", password="salut", host="localhost", database="SAE")
cursor = con.cursor()
try:
	while(1): # le programme tourne à l'infini
		time.sleep(4) 
except KeyboardInterrupt:
	con.close()
	client.loop_stop() # on stop la loop
