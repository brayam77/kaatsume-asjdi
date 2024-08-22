from pyrogram import Client
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient

@addCommand('addgate')
def registrar_comando(_, message):    
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
        if len(args) < 3: 
            return message.reply('Usalo /addgate comando nombre')

        comando, nombre = args[1:]

        MongoClient().collection_cuatro.insert_one({
            "comando": comando,
            "nombre": nombre,
            "gate": "ON✅",
            "estado": "✅",
        })

        message.reply(f'Se ha añadido el gate: NOMBRE: {nombre}, COMANDO: {comando}, ESTATUS: ON✅')

    except Exception as e:     
        message.reply(f'Error: {str(e)}')



