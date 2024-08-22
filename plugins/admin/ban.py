
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('ban')
def panel(_, message):    
    try:
        if MongoClient().grupo_query(message.chat.id) == None: return message.reply('Chat no autorizado')
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('usa el comando para registrarse /register')
        if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
        
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('Comando para admins')

        data = message.text.split(' ')
        if len(data) < 2: return message.reply('usalo /ban id ')

        MongoClient().ban(int(data[1]))
        message.reply(f'El usuario: {data[1]}, ha sido baneado.')

    
    except:     message.reply('No se encontro usuario.')
    