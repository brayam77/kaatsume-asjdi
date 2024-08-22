
from procesos.funciones import addCommand,generate_key,Client
from procesos.mongo_data import MongoClient



@addCommand('key')
def panel(_, message):    

    queryU = MongoClient().user_query(message.from_user.id)
    if queryU == None: return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    
    queryS = MongoClient().seller(message.from_user.id)
    if queryS == False: return message.reply('Comando para admins')

    data = message.text.split(' ')
    if len(data) < 2: return message.reply('usalo /key dias ')

    key = generate_key()

    message.reply(f"""
Key Genenerate Successfully ❇️
━ • ━━━━━━━━━━ • ━ 
Key: <code>{key}</code>
Type: <code>Premium</code>
Days: <code>{data[1]}</code>
User Generate: @{message.from_user.username} <code>[{queryU['rango']}]</code>
━ • ━━━━━━━━━━ • ━  """)
    MongoClient().save_key(key,int(data[1]))
    message_text = f"🔑 El administrador { message.from_user.first_name} - @{message.from_user.username} ha generado una clave con {data[1]} días:\n\n<code>{key}</code> 🔑"
    
    Client.send_message(_,chat_id=-1002214914825,text=message_text)
        
