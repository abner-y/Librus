from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
import crudCasos

Builder.load_file('primeiraPagina.kv')
Builder.load_file('casosPagina.kv')
Builder.load_file('criarCaso.kv')
Builder.load_file('arquivoPagina.kv')


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

    #def remover_widget(self):
        #print(self.widget)
        #self.ids.box.remove_widget(self.ids['box'].Button)
        #self.ids.box.remove_widget(self.ids['box'].TextInput)


class SegundaTela(Screen):
    def resetar(self):
        if self.children[1].ids.descCap.disabled == False:
            self.children[1].ids.descCap.disabled = True
            self.children[1].ids.descCap.background_color = [0, 0, 0, 0]
            self.children[1].ids.nomeCap.disabled = True
            self.children[1].ids.nomeCap.background_color = [0, 0, 0, 0]
            self.children[1].ids.imageAtualizar.source = 'images/icons/icon-edit.png'
            self.children[1].ids.btnDeletar.disabled = False
            self.children[1].ids.btnDeletar.opacity = 1
        app = App.get_running_app()
        app.root.atualizar = 0






class TerceiraTela(Screen):
    pass


class QuartaTela(Screen):
    pass

class ArquivosTela(Screen):
    arquivo_widget = ObjectProperty()




class WindowManager(ScreenManager):
    arquivo_widget = ObjectProperty()
    id_pagina = NumericProperty()
    instancia = ObjectProperty()
    atualizar = NumericProperty()




class EstruturaLivro(RelativeLayout):
    pass



#class LibrusApp(App):
 #   def on_start(self):
  #      print(self.root.ids)


class MainApp(App):

    tituloCaso = StringProperty()
    descCaso = StringProperty()
    def build(self):
        pass



MainApp().run()
