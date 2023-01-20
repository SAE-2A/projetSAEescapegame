import subprocess
import time
import signal
import psutil
import os
import datetime


def process():
    timeout_s = 5
    test = subprocess.Popen("~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio ~/blaasMaresicSAE/projetSAEescapegame/52.wav -ps 'RT' -ppm 1000000", shell=True)
    with open("log.txt", "a") as log: 
        
        now = datetime.datetime.now()
        log.write(f"{now.strftime('%d/%M/%Y %H-%M-%S')}  Début de l épreuve\n")


def test_fini_BLE():
    time.sleep(5)
    print("ici")
    for proc in psutil.process_iter():
        if proc.name() == "pi_fm_rds":
            proc.kill()
    file_2 = subprocess.Popen("~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio ~/blaasMaresicSAE/projetSAEescapegame/5226.wav -ps 'RT' -ppm 1000000", shell=True)
    
    
    with open("log.txt", "a") as log :
        
           
        now = datetime.datetime.now()

        log.write(f"{now.strftime('%d/%M/%Y %H-%M-%S')}   Deuxième étape de l épreuve \n")

    time.sleep(6)
    

def test_fini_quizz():
    proc_stop()
    
    file_3 = subprocess.Popen("~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio /home/pi/blaasMaresicSAE/projetSAEescapegame/522654.wav -ps 'RT' -ppm 1000000", shell=True)
    
    
    with open("log.txt", "a") as log : 
        
        now = datetime.datetime.now()
        log.write(f"{now.strftime('%d/%M/%Y %H-%M-%S')}   Fin de l épreuve, code diffusé\n")




    
def proc_stop(): 
    for proc in psutil.process_iter():
        if proc.name() == "pi_fm_rds":
            proc.kill()
 
    

def new_process(element,new_file): 
    element.kill()
    subprocess.run("play fichier1/ding.wav")
    test = subprocess.run(f"cp {new_file} fichier1/current.wav repeat 5", stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)




import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    info = message.payload.decode("UTF-8")
    print(info)
    if info == "BLE" :
        test_fini_BLE()
    elif info == "quizz":
        test_fini_quizz()
	
def on_connect(client, userdata, flags, rc):
	pass
def main():
    process()	
    broker = "10.11.22.123"
    print("nouvelle instance")
    client = mqtt.Client("nom_equiement")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("baptiste", "salut")
    client.connect(broker, 1883)
    client.loop_start()
    client.subscribe("fini/fini")
    #tu peux mettre client.subscribe("topic")
    #ou alors si tu veux publish c'est client.publish("topic", "message")

    try:
    	while(1):
	    	time.sleep(4)
    except KeyboardInterrupt:
	    client.loop_stop()
	    proc_stop()

if __name__ == "__main__":
    main()
