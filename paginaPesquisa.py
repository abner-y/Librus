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



class PaginaPesquisa(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        print('caixaPesq: ', self.ids.caixaPesq)
        app = App.get_running_app()
        app.root.caixaPesq = self.ids.caixaPesq

class CaixaPesquisa(BoxLayout):
    pass


class ViewPesquisa:
    pass





class ViewPesquisa(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        print('Box2: ', self.ids.box2)
        app = App.get_running_app()
        app.root.box2 = self.ids.box2



    #def remover_widget(self):
     #   self.clear_widgets(self.children)





        #remoção

        #self.ids.box.remove_widget(instance)
        #self.ids.box.remove_widget(instance.input)

