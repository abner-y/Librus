import mysql

from kivy.app import App
from kivy.properties import ObjectProperty, Clock, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

import arquivoPagina

import arquivos
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
        arquivos.excluirPasta(instance.ids["id"])
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
        if app.root.atualizar == 1:
            self.ids.btnDeletar.disabled = True
            self.ids.btnDeletar.opacity = 0
            self.ids.imageAtualizar.source = 'images/icons/icon-done.png'
        else:
            self.ids.btnDeletar.disabled = False
            self.ids.btnDeletar.opacity = 1
            self.ids.imageAtualizar.source = 'images/icons/icon-edit.png'
        if app.root.atualizar == 2:
            app.root.atualizar = 0
            crudCasos.atualizarCaso(instance.ids["id"], self.ids.nomeCap.text, self.ids.descCap.text)
            instance.text = f'{self.ids.nomeCap.text}' if len(self.ids.nomeCap.text) < 15 else f'{self.ids.nomeCap.text[0:15]}...'
            instance.input.text = f'{self.ids.descCap.text[0:100]}...'
        print('Atualizar: ', app.root.atualizar)

    def arquivos(self, instance):
        lista = arquivos.visualizarArquivo(instance.ids['id'])
        app = App.get_running_app()
        print('BoxArch listarArquivos: ')
        tmp = app.root.arch
        if len(lista) > 0:
            #tmp.add_widget(Label(text='tchau', font_size=30, size_hint_y=None, height=200))
            print('temp: ', tmp)
            for item in lista:
                label = Label(text=f'{item[1]}.{item[2]}' if len(item[1]) < 30 else f'{item[1][0:30]}....{item[2]}', pos_hint = {'left': 1}, font_size=20, size_hint_y=None, height=30, color = (0, 0, 0), halign = 'left')
                tmp.add_widget(label)
                button = Button(size_hint_y = None, size_hint_x = 0.05, pos_hint = {'right': 1}, height = 30)
                #source: 'images/icons/icon-deletev2.png'
                button.bind(on_press = self.pressed)
                button.nome = item
                button.id = instance.ids['id']
                button.idAnexo = item[0]
                button.label = label
                tmp.add_widget(button)


            print('lista: ', lista)

        app.root.anterior = app.root.current
        app.root.transition.direction = 'right'
        app.root.current = 'archTela'

    def pressed(self, instance):
        app = App.get_running_app()
        nome_arquivo = instance.nome[1] + '.' + instance.nome[2]
        arquivos.excluirArquivo(nome_arquivo, instance.id, instance.idAnexo)
        # print(f'id: {instance.ids["id"]}')

        tmp = app.root.arch
        # print('temp: ', tmp)
        tmp.remove_widget(instance)
        tmp.remove_widget(instance.label)



class CaixaTitulo(BoxLayout):
    pass


class CaixaDescricao(BoxLayout):
    pass


