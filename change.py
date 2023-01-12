import subprocess
import time
import signal
import psutil
def main():
    process()
def process():
    x = 0 
    #test =  subprocess.Popen("play fichier1/current.wav repeat 10",stdout=subprocess.PIPE, 
    #stderr=subprocess.PIPE, shell=True) 
    test = subprocess.Popen("play fichier1/current.wav repeat 5",stdout=subprocess.PIPE, shell=True)
    print(test.pid)
    
    print(test)
    a = test.pid
    p = psutil.Process(a)
    p.terminate()
    #or p.kill()    subprocess.run(f"kill {a}")


def new_process(element,new_file): 
    element.kill()
    subprocess.run("play fichier1/ding.wav")
    test = subprocess.run(f"cp {new_file} fichier1/current.wav repeat 5", stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)


if __name__ == "__main__":
    main()
