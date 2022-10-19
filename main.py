from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

import crudCasos
import paginaPesquisa

Builder.load_file('primeiraPagina.kv')
Builder.load_file('casosPagina.kv')
Builder.load_file('criarCaso.kv')
Builder.load_file('arquivoPagina.kv')
Builder.load_file('paginaPesquisa.kv')


class PrimeiraTela(Screen):
    text_input_str = StringProperty()

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        print(self.text_input_str)

    def criarCaso(self):
        print('criar caso')
        print(self.ids)

    def pesquisa(self, texto):
        print(f'Pesquisar: {texto}')
        app = App.get_running_app()
        tmp = app.root.box2
        app.root.caixaPesq.text = texto
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="librus"
            )

            c = mydb.cursor()
            c.execute(f"SELECT nomeCaso, descricao, idcasos FROM casos WHERE nomeCaso = '{texto}'")
            resultados = c.fetchall()
            print(resultados)

            c.close()
            mydb.close()
        except:
            resultados = [('Resultado', 'Não encontrado', 0)]
        print('resultados', resultados)
        for resultado in resultados:
            submit = Button(text = f'{resultado[0]}' if len(resultado[0]) < 15 else f'{resultado[0][0:15]}...', font_size = 30, size_hint_y = None, height = 50, color = (0, 0, 0), background_color = (1, 1, 1, 0.1))
            #self.submit.ids['id'] = resultado[2]
            tmp.add_widget(submit)
            input = TextInput(text=f'{resultado[1][0:100]}...', font_size=15, size_hint_y = None, height = 70, background_color = (0, 0, 0, 0), disabled = True, disabled_foreground_color = (0, 0, 0, 1))
            print('Texto Input: ', input.text)
            #self.submit.input = self.input
            tmp.add_widget(input)


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
    #meu_texto = StringProperty()
    #app = App.get_running_app()
    #print(app.root.texto2)
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

class MetadeLivro(RelativeLayout):
    pass

class CaixaPesquisa(RelativeLayout):
    pass

class ViewPesquisa(ScrollView):
    pass

class CaixaPesq(BoxLayout):
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
