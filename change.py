import subprocess
import time
import signal
import psutil
import os
import datetime

class Statut():
    def __init__(self,*args):
        if len(args) > 0:
            self.x = args[0]
        else : 
            self.x = 0

    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x 
        

def main():
    process()
def process():
    
    stat = Statut(0) 
    timeout_s = 5
    x = "0"
    y = "0"   
    test = subprocess.Popen("~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio ~/blaasMaresicSAE/projetSAEescapegame/52.wav -ps 'RT' -ppm 1000000", shell=True)
    with open("log.txt", "a") as log: 
        
        now = datetime.datetime.now()
        log.write(f"{now.strftime('%d/%M/%Y %H-%M-%S')}  Début de l épreuve\n")


    while x == "0": 
        with open('value.txt', "r") as v:
            line = v.readline()
            x = line.split("\n")[0]
        
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
    

    print("la")
    while y == "0": 
        with open('value_y.txt', "r") as v:
            line = v.readline()
            y = line
        time.sleep(5)
    proc_stop()
    
    file_3 = subprocess.Popen("~/PiFmRds/src/pi_fm_rds -freq 107.9 -audio /home/pi/blaasMaresicSAE/projetSAEescapegame/522654.wav -ps 'RT' -ppm 1000000", shell=True)
    
    
    with open("log.txt", "a") as log : 
        
        now = datetime.datetime.now()
        log.write(f"{now.strftime('%d/%M/%Y %H-%M-%S')}   Fin de l épreuve, code diffusé\n")




    time.sleep(10000)
def proc_stop(): 
    for proc in psutil.process_iter():
        if proc.name() == "pi_fm_rds":
            proc.kill()
 
    

def new_process(element,new_file): 
    element.kill()
    subprocess.run("play fichier1/ding.wav")
    test = subprocess.run(f"cp {new_file} fichier1/current.wav repeat 5", stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)


if __name__ == "__main__":
    main()
