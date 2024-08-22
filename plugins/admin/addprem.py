
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('pre')
def panel(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('usa el comando para registrarse /register')
        if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('Comando para admins')

        data = message.text.split(' ')
        if len(data) < 3: return message.reply('usalo /pre <id> <cantidad>')

        MongoClient().addpremium(int(data[1]), int(data[2]))
        message.reply(f'Se han añadido los dias {data[2]}  a {data[1]}')

    
    except:     message.reply('No se encontro usuario.')
    
