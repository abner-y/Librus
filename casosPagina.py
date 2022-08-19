import mysql

from kivy.app import App
from kivy.properties import ObjectProperty, Clock, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

class CasosPagina(RelativeLayout):
    nomeCapitulo = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)


    def post_init(self, *args):
        self.nomeCapitulo = 'teste'

    def displayCaso(self, id_caso):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus",
        )

        c = mydb.cursor()
        app = App.get_running_app()
        c.execute(f"SELECT nomeCaso, descricao FROM casos WHERE idcasos = {id_caso}")
        resultados = c.fetchall()
        print(resultados)
        app.caso = resultados[0][0]

        c.close()
        mydb.close()


class CaixaTitulo(BoxLayout):
    pass