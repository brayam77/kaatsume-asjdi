from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient

@addCommand('claim')
def bin(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    if queryU['rango'] == 'Baneado':
        return message.reply('Usuario baneado no puede usarme.')
    
    if queryU is None:
        return message.reply('Usa el comando para registrarse /register')
    
    data = message.text.split(' ')
    if len(data) < 2:
        return message.reply('Usalo /claim Katsume-xxxxxxx-PREMIUM ')
    
    querk = MongoClient().key_query(data[1])
    
    if querk is None:
        return message.reply('La key no se encontró.')
    
    if querk['key'] == data[1]:
        MongoClient().addpremium(message.from_user.id, querk['dias'])
        MongoClient().delete_key(querk['key'])
        MongoClient().save_grupos(message.from_user.id, querk['dias'])
        
        # Send message to the specific chat ID
        chat_id = -1002214914825
        key_info_message = f'''Key Reclamada:
Usuario: @{message.from_user.username}
ID de Usuario: {message.from_user.id}
Key: {data[1]}
Días: {querk['dias']}
        '''
        message._client.send_message(chat_id, key_info_message)
        
        return message.reply(f'''
Reedem Successfully ❇️
━ • ━━━━━━━━━━ • ━ 
Key: <code>{data[1]}</code>
Type: <code>Premium</code>
Days: <code>{querk['dias']}</code>
New Status: @{message.from_user.username} <code>[Premium]</code>
━ • ━━━━━━━━━━ • ━''')
    
    else:
        return message.reply('Key no es válida')