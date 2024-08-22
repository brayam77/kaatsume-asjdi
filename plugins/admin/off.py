from pyrogram import Client
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient

@addCommand('gateoff')
def apagar_comando(_, message):    
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
            return message.reply('Usalo /gateoff comando')

        comando = args[1]

        MongoClient().collection_cuatro.update_one(
            {"comando": comando},
            {"$set": {"estado": "❌", "gate": "OFF❌"}}
        )

        message.reply(f'𝐄𝐥 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {comando} 𝐬𝐞 𝐡𝐚 𝐩𝐮𝐞𝐬𝐭𝐨 𝐞𝐧 𝐦𝐚𝐧𝐭𝐞𝐧𝐢𝐦𝐢𝐞𝐧𝐭𝐨 ⚠️')

    except Exception as e:     
        message.reply(f'Error: {str(e)}')


app = Client("my_bot")

if __name__ == '__main__':
    app.run()
