from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

import arquivos


class ArquivoPagina(RelativeLayout):
    def adicionarArquivos(self, id):
        arquivos.adicionarArquivo(id)

    def resetarArquivos(self):
        app = App.get_running_app()
        temp = app.root.arch
        temp.clear_widgets()

    def abrirPastas(self, id):
        print('id_pagina: ', id)
        arquivos.abrirPasta(id)



class ListaArquivos(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        print('BoxArch: ', self.ids.boxArch)
        app = App.get_running_app()
        app.root.arch = self.ids.boxArch



class CaixaArquivos(GridLayout):
    pass

