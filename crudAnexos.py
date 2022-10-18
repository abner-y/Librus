import mysql
from datetime import datetime

from kivy.uix.label import Label
from kivy.uix.popup import Popup
from mysql.connector import DataError, InternalError, IntegrityError, OperationalError, NotSupportedError, \
    ProgrammingError, Error, InterfaceError


def criarAnexo(titulo, tipo, casosRelacionados, autor, id):
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
        c.execute(f"INSERT INTO anexos (titulo, tipo, dataCriacao, casosRelacionados, autor, idcasos) VALUES ('{titulo}', '{tipo}', '{atual}', '{casosRelacionados}', '{autor}', '{id}')")
        mydb.commit()
        c.close()
        mydb.close()
        pop = Popup(title='Anexos',
                    content=Label(text='anexo criado com sucesso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()

    except DataError as err:
        print('Erro na criação')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InternalError as err:
        print('Erro interno')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except IntegrityError as err:
        print('Erro integridade')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except OperationalError as err:
        print('Erro operational')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except NotSupportedError as err:
        print('Erro not supported')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except ProgrammingError as err:
        print('Erro programming')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except Warning as err:
        print('Erro warning')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except Error as err:
        print('Errorrr programming')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InterfaceError as err:
        print('Errorrr programming')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except NotSupportedError as err:
        print('Errorrr programming')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0

    except:
        print("Unknown error occurred")
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao criar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    else:
        return 'Criado com sucesso'


def deletarAnexo(id):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="librus"
        )

        c = mydb.cursor()
        c.execute(f"DELETE FROM anexos WHERE idAnexo = '{id}'")
        print(id)
        mydb.commit()
        c.close()
        mydb.close()
        pop = Popup(title='Anexos',
                    content=Label(text='Anexo deletado com sucesso.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()

    except DataError as err:
        print('Erro na criação')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except InternalError as err:
        print('Erro interno')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except IntegrityError as err:
        print('Erro integridade')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except OperationalError as err:
        print('Erro operational')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except NotSupportedError as err:
        print('Erro not supported')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    except ProgrammingError as err:
        print('Erro programming')
        print(err)
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0

    except:
        print("Unknown error occurred")
        pop = Popup(title='Anexos',
                    content=Label(text='Erro ao deletar anexo.'),
                    size_hint=(None, None), size=(400, 200))
        pop.open()
        return 0
    else:
        return 'anexo Deletado com sucesso'

