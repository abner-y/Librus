from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector

Builder.load_file('primeiraPagina.kv')
Builder.load_file('casosPagina.kv')

class PrimeiraTela(Screen):
    text_input_str = StringProperty()

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        print(self.text_input_str)

    def criarCaso(self):
        print('criar caso')
        print(self.ids)

    def painelInvestigacao(self):
        print('Painel')


class SegundaTela(Screen):
    pass




class TerceiraTela(Screen):
    pass


class WindowManager(ScreenManager):
    id_pagina = NumericProperty()



class EstruturaLivro(RelativeLayout):
    pass



#class LibrusApp(App):
 #   def on_start(self):
  #      print(self.root.ids)


class MainApp(App):
    tituloCaso = StringProperty('testee')
    descCaso = StringProperty('Texto descritivo aqui!')
    def on_build(self):
        pass



MainApp().run()
