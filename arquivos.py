import os

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
    pass

def adicionarArquivo(id):
    pass

def excluirArquivo(id):
    pass

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


