from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient

@addCommand('rango')
def panel(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU is None: 
            return message.reply('Usa el comando para registrarse /register')
        
        if queryU['rango'] == 'Baneado': 
            return message.reply('Usuario baneado no puede usarme.')
        
        # Verifica si el usuario tiene el rol de 'Owner' o 'Dev-Bol'
        if queryU['rango'] not in ['Owner', 'Dev-Bol']:
            return message.reply('No tienes permiso para usar este comando.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: 
            return message.reply('Comando para admins')

        data = message.text.split(' ')
        if len(data) < 3: 
            return message.reply('Úsalo /rango <id> <rango>')

        MongoClient().rango(int(data[1]), data[2])
        message.reply(f'Se ha actualizado el rango de: {data[1]}. Ahora es {data[2]}')
    
    except Exception as e:     
        message.reply(f'No se encontró usuario. Error: {str(e)}')
