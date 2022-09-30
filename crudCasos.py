import mysql
from datetime import datetime

from kivy.uix.label import Label
from kivy.uix.popup import Popup
from mysql.connector import DataError, InternalError, IntegrityError, OperationalError, NotSupportedError, \
    ProgrammingError


def retornaId(titulo):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus"
        )

        c = mydb.cursor()
        c.execute(f"SELECT idcasos FROM casos WHERE nomeCaso = '{titulo}'")
        print(id)
        mydb.commit()
        c.close()
        mydb.close()
        pop = Popup(title='Casos',
                    content=Label(text='Caso deletado com sucesso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()

    except DataError as err:
        print('Erro na criação')
        print(err)

        return 0
    except InternalError as err:
        print('Erro interno')
        print(err)

        return 0
    except IntegrityError as err:
        print('Erro integridade')
        print(err)

        return 0
    except OperationalError as err:
        print('Erro operational')
        print(err)

        return 0
    except NotSupportedError as err:
        print('Erro not supported')
        print(err)

        return 0
    except ProgrammingError as err:
        print('Erro programming')
        print(err)

        return 0

    except:
        print("Unknown error occurred")
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao pegar Id.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    else:
        return 'Id recuperado com sucesso'


def criarCaso(nomeCaso, desc, caminho = ''):
    now = datetime.now()
    atual = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus"
        )

        c = mydb.cursor()
        c.execute(f"INSERT INTO casos (nomeCaso, descricao, dataAbertura, fotoCaso) VALUES ('{nomeCaso}', '{desc}', '{atual}', '{caminho}')")
        mydb.commit()
        c.close()
        mydb.close()
        pop = Popup(title='Casos',
                    content=Label(text='Caso criado com sucesso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()

    except DataError as err:
        print('Erro na criação')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InternalError as err:
        print('Erro interno')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except IntegrityError as err:
        print('Erro integridade')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except OperationalError as err:
        print('Erro operational')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except NotSupportedError as err:
        print('Erro not supported')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except ProgrammingError as err:
        print('Erro programming')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0

    except:
        print("Unknown error occurred")
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    else:
        return 'Criado com sucesso'


def deletarCaso(id):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus"
        )

        c = mydb.cursor()
        c.execute(f"DELETE FROM casos WHERE idcasos = '{id}'")
        print(id)
        mydb.commit()
        c.close()
        mydb.close()
        pop = Popup(title='Casos',
                    content=Label(text='Caso deletado com sucesso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()

    except DataError as err:
        print('Erro na criação')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InternalError as err:
        print('Erro interno')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except IntegrityError as err:
        print('Erro integridade')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except OperationalError as err:
        print('Erro operational')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except NotSupportedError as err:
        print('Erro not supported')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except ProgrammingError as err:
        print('Erro programming')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0

    except:
        print("Unknown error occurred")
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao deletar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    else:
        return 'Deletado com sucesso'