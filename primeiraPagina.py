import mysql
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from casosPagina import CasosPagina


class PrimeiraPagina(RelativeLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        pass


    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)

class CaixaCasos(BoxLayout):
    pass


class ViewCasos:
    pass





class ViewCasos(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)


    def post_init(self, *args):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="librus"
            )

            c = mydb.cursor()
            c.execute("SELECT nomeCaso, descricao, idcasos FROM casos")
            resultados = c.fetchall()
            print(resultados)

            c.close()
            mydb.close()
        except:
            resultados = [('Teste 1', 'Descrição do teste', 2)]

        for resultado in resultados:
            self.submit = Button(text = f'{resultado[0]}' if len(resultado[0]) < 15 else f'{resultado[0][0:15]}...', font_size = 30, size_hint_y = None, height = 50, color = (0, 0, 0), background_color = (1, 1, 1, 0.1))
            self.submit.bind(on_press = self.pressed)
            self.submit.titulo = resultado[0]
            self.submit.desc = resultado[1]
            self.submit.ids['id'] = resultado[2]
            self.ids.box.add_widget(self.submit)
            self.input = TextInput(text=f'{resultado[1][0:100]}...', font_size=15, size_hint_y = None, height = 70, background_color = (0, 0, 0, 0), disabled = True, disabled_foreground_color = (0, 0, 0, 1))
            self.submit.input = self.input
            self.ids.box.add_widget(self.input)
        #print('children: ', self.ids.box.children)
        app = App.get_running_app()
        app.root.caixa = self.ids.box

    #def remover_widget(self):
     #   self.clear_widgets(self.children)



    def pressed(self, instance):
        print('self children: ', self.children)
        print('instancia-texto: ', instance.text)
        id = instance.ids
        print('instancia kids: ', instance.children)
        print(f'instancia: {instance.titulo}')

        tmp = CasosPagina()
        tmp.displayCaso(instance)
        print(id['id'])
        app = App.get_running_app()
        app.root.current = 'segunda'
        app.root.instancia = instance
        app.root.transition.direction = 'up'

        #remoção

        #self.ids.box.remove_widget(instance)
        #self.ids.box.remove_widget(instance.input)

