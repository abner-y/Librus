from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
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


class QuartaTela(Screen):
    text_input_titulo = StringProperty()
    text_input_desc = StringProperty()

    def criarConf(self, widget):
        self.text_input_titulo = widget.ids['tituloCaso'].text
        self.text_input_desc = widget.ids['descCaso'].text
        print(self.text_input_titulo)
        print(self.text_input_desc)
        if ((self.text_input_titulo != '') and (self.text_input_desc != '')):
            crudCasos.criarCaso(self.text_input_titulo, self.text_input_desc)

        else:
            pop = Popup(title='Erro',
                        content=Label(text='Por favor preencha os campos corretamente.'),
                        size_hint=(None, None), size=(400, 200))
            pop.open()
        self.resetar(widget)
    def resetar(self, widget):
        widget.ids['tituloCaso'].text = ''
        widget.ids['descCaso'].text = ''


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
