import os
#from tkinter import filedialog
import shutil
import subprocess
#import sys
import tkinter as tk
from tkinter import filedialog

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
        os.chdir(caminho)
        for item in lista:
            os.remove(str(item))
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
    except:
        print('Erro ao copiar arquivo')

def excluirArquivo(nome, id):
    print(nome, id)
    caminho = r'C:\Users\CLEBER\PycharmProjects\librusV2\casos\caso-' + str(id)
    try:
        os.chdir(caminho)
        os.remove(str(nome))
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
        print('tudo certo visualizando!')
        return os.listdir(caminho)
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


