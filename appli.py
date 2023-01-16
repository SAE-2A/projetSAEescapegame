#!/usr/bin/env python3





import sys
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.core.window import Window

Config.set('graphics','width','3000')
Config.set('graphics','height','420')
Config.set('graphics','resizable','0')

class Appli(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        Window.size = (720, 625)
        self.root.get_screen('inscription').ids.nom.halign = 'center'
        self.root.get_screen('inscription').ids.equipe.halign = 'center'
        pass

    def on_press_quit(self):
        sys.exit(0)
    
    def on_press_inscr(self):
        Window.fullscreen = True
        pass
    def on_press_return(self):
        Window.fullscreen = False
        Window.size = (720, 625)
    

class QuizzScreen(Screen):
    pass
class InscriptionScreen(Screen):
    pass
class WindowManager(ScreenManager):
    pass



sm=Builder.load_file('appli.kv')

Appli().run()
