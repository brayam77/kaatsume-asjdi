
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('rango')
def panel(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('usa el comando para registrarse /register')
        if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('Comando para admins')

        data = message.text.split(' ')
        if len(data) < 3: return message.reply('usalo /rango <id> <rango>')

        MongoClient().rango(int(data[1]), data[2])
        message.reply(f'Se ha actualizado el rango de : {data[2]} Ahora es  {data[1]}')

    
    except:     message.reply('No se encontro usuario.')
    