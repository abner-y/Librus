import mysql
from datetime import datetime

from kivy.uix.label import Label
from kivy.uix.popup import Popup
from mysql.connector import DataError, InternalError, IntegrityError, OperationalError, NotSupportedError, \
    ProgrammingError


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
        return 'Criado com sucesso'

    except DataError as err:
        print('Erro na criação')
        print(err)
        pop = Popup(title='Casos',
                    content=Label(text='Erro ao criar caso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InternalError as err:
        print('Erro na criação')
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
