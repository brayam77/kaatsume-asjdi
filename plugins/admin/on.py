from pyrogram import Client
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient

@addCommand('gateon')
def encender_comando(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU is None: 
            return message.reply('Usa el comando para registrarte /register')
        if queryU['rango'] == 'Baneado': 
            return message.reply('Usuario baneado no puede usarme.')

        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: 
            return message.reply('Comando para admins')

        args = message.text.split(' ')
        if len(args) < 2: 
            return message.reply('Usalo /gateon comando')

        comando = args[1]

    
        MongoClient().collection_cuatro.update_one(
            {"comando": comando},
            {"$set": {"estado": "✅", "gate": "ON✅"}}
        )

        message.reply(f'El comando {comando} se ha activado correctamente ✅')

    except Exception as e:     
        message.reply(f'Error: {str(e)}')

