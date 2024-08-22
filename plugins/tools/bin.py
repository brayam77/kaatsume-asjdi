import requests
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('bin')
def bin(_, message):    
    
    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU == None: return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    

    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('Chat no autorizado')
    
    try:
        BIN = message.text[len("/bin"):11].strip()
        
        if len(BIN) < 6:
            message.reply("BIN INCORRECTO FORMATO DE BIN 6 DIGITOS /bin 455664")
            return
            
        if not BIN:
            message.reply("HERRAMIENTA BIN INFO, USE /bin 4556747")
            return
        
        func = requests.get(f'https://bins.antipublic.cc/bins/{BIN[:6]}')

        if "{'Status': 'NOT FOUND'}" in func.text: return message.reply('Bin not fund')
        else:
            texto = f'''
🌧 BIN FOUND 🌧

カ BIN ➳ {BIN[:6]} 
カ LEVEL ➳ <code>{func.json()['level']}</code>
カ TYPE ➳ code>{func.json()['type']}</code>
カ BRAND ➳ <code>{func.json()['brand']}</code>
カ BANK ➳ <code>{func.json()['bank']}</code>
カ COUNTRY ➳ <code>{func.json()['country']}</code> | <code>{func.json()['country_name']}</code> | <code>{func.json()['country_flag']}</code>
'''
            message.reply(texto)

    except: message.reply('Bin not fund')
