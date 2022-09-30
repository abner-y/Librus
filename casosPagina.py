import mysql

from kivy.app import App
from kivy.properties import ObjectProperty, Clock, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

import crudCasos
import primeiraPagina


class CasosPagina(RelativeLayout):
    nomeCapitulo = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)


    def post_init(self, *args):
        self.nomeCapitulo = 'teste'

    def displayCaso(self, instance):
        """
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123456",
                database="librus",
            )

            c = mydb.cursor()

            c.execute(f"SELECT nomeCaso, descricao FROM casos WHERE idcasos = {id_caso}")
            resultados = c.fetchall()
            c.close()
            mydb.close()
        except:
            resultados = [('Teste 1', 'Descrição do teste')]
        print(resultados)
        """
        app = App.get_running_app()
        app.tituloCaso = str(instance.titulo)
        app.descCaso = instance.desc
        print('ids instancia: ', instance.ids['id'])

    def deletarCaso(self, instance):
        crudCasos.deletarCaso(instance.ids["id"])
        #print(f'id: {instance.ids["id"]}')
        app = App.get_running_app()
        tmp = app.root.caixa
        #print('temp: ', tmp)
        tmp.remove_widget(instance)
        tmp.remove_widget(instance.input)
        #tmp.remover_widget(primeiraPagina.ViewCasos())




class CaixaTitulo(BoxLayout):
    pass


class CaixaDescricao(BoxLayout):
    pass


