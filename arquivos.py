import os
#from tkinter import filedialog
import shutil
import subprocess
#import sys
import tkinter as tk
from tkinter import filedialog

import mysql
from kivy.app import App

import crudAnexos

root = tk.Tk()
root.withdraw()

def criarPasta(id):
    caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos'
    nome_pasta = 'caso-' + str(id)
    try:
        os.chdir(caminho)
        os.mkdir(nome_pasta)
        print('Pasta Criada')
    except FileExistsError:
        print(f'Pasta {nome_pasta} já existe')
    except:
        print('Erro desconhecido ao criar pasta!')


def excluirPasta(id):
    lista = visualizarArquivo(id)
    caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
    print('caminho: ', caminho)
    try:
        print('lista delete: ', lista)
        os.chdir(caminho)
        for item in lista:
            nome = item[1] + '.' + item[2]
            os.remove(str(nome))
            #excluirArquivo(nome, id, item[0])
        caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos'
        diretorio = 'caso-' + str(id)
        os.chdir(caminho)
        os.rmdir(diretorio)
        print('Pasta Removida')
    except OSError as error:
        print(error)
        print("Pasta não pode ser removida")
    except:
        print(f'Erro ao deletar pasta')


def adicionarArquivo(id):
    try:
        caminho = filedialog.askopenfilename()
        destino = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
        print('Caminho do arquivo selecionado: ', caminho)

        shutil.copy(caminho, destino)
        caminho = caminho.split('/')
        caminho = caminho[-1]
        caminho = caminho.split('.')
        titulo = caminho[-2]
        tipo = caminho[-1]
        print(f'titulo: {titulo}, tipo: {tipo}')
        app = App.get_running_app()
        autor = 'Abner'
        crudAnexos.criarAnexo(titulo, tipo, app.root.instancia.titulo, autor, id)
    except:
        print('Erro ao copiar arquivo')


def excluirArquivo(nome, id, idAnexo = 0):
    print(nome, id)
    caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
    try:
        os.chdir(caminho)
        print('caminho: ', caminho)
        print('nome: ', nome)
        os.remove(str(nome))

        print('idAnexo: ', idAnexo)
        if idAnexo != 0:
            crudAnexos.deletarAnexo(idAnexo)
        print('Arquivo Deletado!')
        return os.listdir(caminho)
    except FileNotFoundError:
        print('Arquivo não encontrado!')

    except:
        print('Erro desconhecido ao deletar arquivo!')


def visualizarArquivo(id):
    caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
    try:
        os.chdir(caminho)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus"
        )

        c = mydb.cursor()
        c.execute(f"SELECT idAnexo, titulo, tipo FROM anexos WHERE idcasos = {id}")
        lista = c.fetchall()
        print(lista)

        c.close()
        mydb.close()
        return lista
    except FileNotFoundError:
        criarPasta(id)
        return list()
    except:
        print('Erro desconhecido ao visualizar arquivo!')
        return list()


def abrirPasta(id):
    try:
        caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
        subprocess.Popen(f'explorer "{caminho}"')
    except:
        print('Erro ao abrir pasta de arquivos')


