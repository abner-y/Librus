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
        self.ids.descCap.disabled = True
        self.ids.descCap.background_color = [0, 0, 0, 0]
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

    def editarCaso(self, instance):
        if self.ids.descCap.disabled == True:
            self.ids.descCap.disabled = False
            self.ids.descCap.background_color = [0.8, 0.8, 0.8, 0.5]
            self.ids.nomeCap.disabled = False
            self.ids.nomeCap.background_color = [0.8, 0.8, 0.8, 0.5]
        else:
            self.ids.descCap.disabled = True
            self.ids.descCap.background_color = [0, 0, 0, 0]
            self.ids.nomeCap.disabled = True
            self.ids.nomeCap.background_color = [0, 0, 0, 0]
        app = App.get_running_app()
        app.root.atualizar += 1
        if app.root.atualizar == 2:
            app.root.atualizar = 0
            crudCasos.atualizarCaso(instance.ids["id"], self.ids.nomeCap.text, self.ids.descCap.text)
            instance.text = f'{self.ids.nomeCap.text}' if len(self.ids.nomeCap.text) < 15 else f'{self.ids.nomeCap.text[0:15]}...'
            instance.input.text = f'{self.ids.descCap.text[0:100]}...'
        print('Atualizar: ', app.root.atualizar)





class CaixaTitulo(BoxLayout):
    pass


class CaixaDescricao(BoxLayout):
    pass


