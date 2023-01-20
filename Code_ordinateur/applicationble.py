from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
import time 
from kivy.clock import Clock
import threading
from calcul_dist import distance_balise
from mqtt import send_inscription 
from mqtt import send_message
import json


class LoginWindow(Screen):
    pass

class FirstWindow(Screen):
    pass


 
class WindowManager(ScreenManager):
    pass

class Applicationble(App):
    def build(self):
        pass

    def update_ltxt(self):
        threading.Thread(target=self.update_label).start()
    
    def update_label(self):
        self.root.get_screen("hub").ids.distance.on_press = print("en cours")
       
       
        
        
        time.sleep(1)
        while True: 
            distance = None
            while distance == None :
                distance = str(distance_balise())
                #distance = "1"
            if distance != None:
                self.root.get_screen("hub").ids.distance.text = distance
                print(self.root.get_screen('hub').ids.distance.text)
            
           
            
            if distance == "réussi":
                self.root.get_screen("hub").ids.distance.text = distance
                with open("name.txt" , "r") as nm :
                    line = nm.readline()
                send_message(json.dumps({"type": "update", "activite": "BLE", "nom": line, "status": 1}))
                break 
        
        time.sleep(2)
        
    def nombre_joueur(self):
        """Fonction pour l'inscription et le début d'une équipe
        """
        racine = self.root.get_screen('login')
        try : 
            nb_joueur = str(racine.ids.identif.text)
            send_inscription(nb_joueur)           
            with open("name.txt", "w") as nm:
                nm.write(nb_joueur) 
        except ValueError : 
            print("typeerror")
            return



        
if __name__ == "__main__":
    app = Applicationble()
    app.run()





