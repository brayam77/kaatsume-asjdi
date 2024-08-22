
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('delgp')
def panel(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('usa el comando para registrarse /register')
        if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('Comando para admins')

        data = message.text.split(' ')
        if len(data) < 2: return message.reply('usalo /delgp id')

        MongoClient().grupo_eliminar(int(data[1]))
        message.reply(f'El usuario: {data[1]}, ha sido sacado del grupos aprovados.')

    
    except:     message.reply('No se encontro usuario.')
    