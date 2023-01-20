
import serial


def main(): 
    distance_balise()

def distance_balise():
    ser = serial.Serial(
            port='COM9',
            baudrate=115200,
        )
    ser.close()
    ser.open()
    
   
    var = None
    chainee = ser.readline().decode("utf-8")
    formule = None
    
    while True : 
        
        chaine = ser.readline()
             #000800000805F9B0131
        #if str(chaine).startswith("0201041A") and not str(chaine).startswith("b'0201041AFF4C0002150005000100001000800000805F9B013100017F64B6"):
        #if str(chaine).startswith("0201041AFF"):
        if str(chaine).startswith("b'0201041AFF4C00021500050001000010008") or str(chaine).startswith("b'0201040303AAFE0E16AAFE10E9006379707265737300'") and not str(chaine).startswith("b'0201041AFF4C0002150005000100001000800000805F9B013100017F64B6"): 
            print(chaine)
        
            
            var = chaine.decode("utf-8").split("\r\n")[0]
            print(var)
            var = int(var[-2] + var[-1],16)-256
            
            formule = 10 ** ((-61-var)/(10*3))
            print(formule)
            if formule <= 0.5 : 
                return "réussi"
                
            else : 
                return formule 
        if formule != None : 
            break    


if __name__ == "__main__":
    main()