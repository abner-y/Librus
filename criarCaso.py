from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

import crudCasos
from casosPagina import CasosPagina


class CriarCaso(RelativeLayout):
    text_input_titulo = StringProperty()
    text_input_desc = StringProperty()

    def criarConf(self, widget):
        self.text_input_titulo = widget.ids['tituloCaso'].text
        self.text_input_desc = widget.ids['descCaso'].text
        print(self.text_input_titulo)
        print(self.text_input_desc)
        if ((self.text_input_titulo != '') and (self.text_input_desc != '')):
            crudCasos.criarCaso(self.text_input_titulo, self.text_input_desc)
            self.submit = Button(text=f'{self.text_input_titulo}' if len(
                self.text_input_titulo) < 15 else f'{self.text_input_titulo[0:15]}...',
                                 font_size=30, size_hint_y=None, height=50, color=(0, 0, 0),
                                 background_color=(1, 1, 1, 0.1))
            self.submit.bind(on_press=self.pressed)
            self.submit.titulo = self.text_input_titulo
            self.submit.desc = self.text_input_desc
            self.submit.ids['id'] = crudCasos.retornaId(self.text_input_titulo)
            self.input = TextInput(text=f'{self.text_input_desc[0:100]}...', font_size=15, size_hint_y=None, height=70,
                                   background_color=(0, 0, 0, 0), disabled=True, disabled_foreground_color=(0, 0, 0, 1))
            self.submit.input = self.input

            app = App.get_running_app()
            tmp = app.root.caixa
            tmp.add_widget(self.submit)
            tmp.add_widget(self.input)
            app.root.current = 'primeira'

        else:
            pop = Popup(title='Erro',
                        content=Label(text='Por favor preencha os campos corretamente.'),
                        size_hint=(None, None), size=(400, 200))
            pop.open()
        self.resetar(widget)

    def resetar(self, widget):
        widget.ids['tituloCaso'].text = ''
        widget.ids['descCaso'].text = ''

    def pressed(self, instance):
        id = instance.ids
        tmp = CasosPagina()
        tmp.displayCaso(instance)
        print(id['id'])
        app = App.get_running_app()
        app.root.id_pagina = id['id']
        app.root.current = 'segunda'
        app.root.instancia = instance
        app.root.transition.direction = 'up'
