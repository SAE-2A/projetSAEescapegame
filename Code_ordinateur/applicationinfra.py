from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
import time 
from testinfra import infra_check


from mqtt import send_inscription,send_rasp
import json



class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class ForthWindow(Screen): 
    pass
class FifthWindow(Screen):
    pass

class FinalWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Applicationinfra(App):
  
    def build(self):
        pass

    def first_answer(self): 
        """Fonction lancé depuis le bouton Réponse de la page 'first_enigme' utilisant la fonction infra_check
        du fichier testinfra pour enregistrer la réponse de l'utilisateur à la premier question du quiz
        
        
        """
    
        self.root.get_screen("first_enigme").ids.reponse_un.disabled = True
        data = infra_check()
        if data == "cf" or data == "85" or data == "ef" : 
            dic = {"cf": "1", "85":"3","ef":"4"}
            print(dic[data])
            with open("error.txt", "r") as er:
                line = er.readline()
                if line == "": 
                    line = 0

            with open("error.txt", "w") as er:
                er.write(str(int(line)+1))
            self.root.get_screen("first_enigme").ids.reponse_un.disabled = False
            self.root.get_screen("first_enigme").ids.error.text = dic[data]
            return 'first_enigme'
        elif data == "e7" : 
            print(data)
            self.root.get_screen("first_enigme").ids.reponse_un.disabled = False
            return "second_enigme"
        else : 
            self.root.get_screen("first_enigme").ids.reponse_un.disabled = False

    def second_answer(self): 
        """Fonction lancé depuis le bouton Réponse de la page 'second_enigme' utilisant la fonction infra_check
        du fichier testinfra pour enregistrer la réponse de l'utilisateur à la deuxième question du quiz
        
        
        """
        self.root.get_screen("second_enigme").ids.reponse_un.disabled = True
        data = infra_check()
        if data == "e7" or data == "85" or data == "ef" : 
            dic = {"e7": "2", "85":"3","ef":"4"}
            print(dic[data])
            with open("error.txt", "r") as er:
                line = er.readline()
                if line == "": 
                    line = 0

            with open("error.txt", "w") as er:
                er.write(str(int(line)+1))
            self.root.get_screen("second_enigme").ids.reponse_un.disabled = False
            self.root.get_screen("second_enigme").ids.error.text = dic[data]
            return 'second_enigme'
        elif data == "cf" : 
            print(data)
            self.root.get_screen("second_enigme").ids.reponse_un.disabled = False
            return "third_enigme"
        else : 
            self.root.get_screen("second_enigme").ids.reponse_un.disabled = False
          
        
    def third_answer(self): 
        """Fonction lancé depuis le bouton Réponse de la page 'third_enigme' utilisant la fonction infra_check
        du fichier testinfra pour enregistrer la réponse de l'utilisateur à la troisième question du quiz
        
        
        """

        self.root.get_screen("third_enigme").ids.reponse_un.disabled = True
        data = infra_check()
        if data == "e7" or data == "cf" or data == "ef" : 
            dic = {"e7": "2", "85":"3","ef":"4","cf": "1"}
            print(dic[data])
            with open("error.txt", "r") as er:
                line = er.readline()
                if line == "": 
                    line = 0

            with open("error.txt", "w") as er:
                er.write(str(int(line)+1))
            self.root.get_screen("third_enigme").ids.reponse_un.disabled = False
            self.root.get_screen("third_enigme").ids.error.text = dic[data]
            return 'third_enigme'
        elif data == "85" : 
            print(data)
            self.root.get_screen("third_enigme").ids.reponse_un.disabled = False
            return "forth_enigme"
        else : 
            self.root.get_screen("third_enigme").ids.reponse_un.disabled = False
          
               
    def forth_answer(self): 
        """Fonction lancé depuis le bouton Réponse de la page 'forth_enigme' utilisant la fonction infra_check
        du fichier testinfra pour enregistrer la réponse de l'utilisateur à la quatrième question du quiz
        
        
        """
        self.root.get_screen("forth_enigme").ids.reponse_un.disabled = True
        data = infra_check()
        if data == "e7" or data == "cf" or data == "ef" or "85" : 
            dic = {"e7": "2", "85":"3","ef":"4","cf": "1"}
           
            self.root.get_screen("forth_enigme").ids.reponse_un.disabled = False
     
            return "fifth_enigme"
        else : 
            self.root.get_screen("forth_enigme").ids.reponse_un.disabled = False
        
    def fifth_answer(self): 
        """Fonction lancé depuis le bouton Réponse de la page 'fifth_enigme' utilisant la fonction infra_check
        du fichier testinfra pour enregistrer la réponse de l'utilisateur à la cinquième question du quiz
        
        """
        self.root.get_screen("fifth_enigme").ids.reponse_un.disabled = True
        data = infra_check()
        if data == "e7" or data == "cf" or data == "ef" : 
            dic = {"e7": "2", "85":"3","ef":"4","cf": "1"}
            print(dic[data])
            with open("error.txt", "r") as er:
                line = er.readline()
                if line == "": 
                    line = 0

            with open("error.txt", "w") as er:
                er.write(str(int(line)+1))
            self.root.get_screen("fifth_enigme").ids.reponse_un.disabled = False
            self.root.get_screen("fifth_enigme").ids.error.text = dic[data]
            return 'fifth_enigme'
        elif data == "85" : 
            print(data)
            self.root.get_screen("fifth_enigme").ids.reponse_un.disabled = False
            send_rasp("quizz")
            return "final"
        else : 
            self.root.get_screen("fifth_enigme").ids.reponse_un.disabled = False
        
    def final(self):
        """Fonction verifiant que la véracité du code décrypter depuis le signal Radio FM
        
        """
        reponse = self.root.get_screen("final").ids.identif.text
        if reponse == "R&T":
            self.root.get_screen("final").ids.error.color = (0,1,0,1)
            self.root.get_screen("final").ids.error.text = "Bravo"
            
        else :
         
            self.root.get_screen("final").ids.error.text = "Erreur code"


if __name__ == "__main__":
    app = Applicationinfra()
    app.run()