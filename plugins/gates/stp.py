import time
import requests
from procesos.funciones import addCommand, find_cards, antispam
from procesos.mongo_data import MongoClient
from pages.stripechk import *

@addCommand('stp')
def panel(_, message):
    if MongoClient().grupo_query(message.chat.id) is None:
        return message.reply('Chat no autorizado')

    queryU = MongoClient().user_query(message.from_user.id)
    if queryU is None:
        return message.reply('Usa el comando para registrarte /register')
    if queryU['rango'] == 'Baneado':
        return message.reply('Usuario baneado no puede usarme.')
    if queryU['plan'] == 'Free':
        return message.reply('Usuario Free no puede usarme.')
    if antispam(queryU['antispam'], message):
        return

    comando_info = MongoClient().collection_cuatro.find_one({"comando": "/stp"})
    print("Estado del gate 'on' en la base de datos:", comando_info)  
    
    if comando_info is None or comando_info.get('estado') != '✅':
        return message.reply('<b>Command: <code>$stp</code>\nGateway: <code>Stripe Auth</code>\nEstado: <code>OFF❌</code>\nFormat: <code>/stp cc|month|year|cvv.</code></b>')

    ini = time.time()
    if message.reply_to_message:
        cc = find_cards(message.reply_to_message.text)
    else:
        cc = find_cards(message.text)

    if '<b>ingrese la ccs.</b>' in cc:
        return message.reply('<b>Command: <code>$stp</code>\nGateway: <code>Stripe Auth</code>\nEstado: <code>✅</code>\nFormat: <code>/stp cc|month|year|cvv.</code></b>')

    ccsa = message.text.split('stp ')
    ccs = ccsa[1].split('|')
    texto_1 = message.reply(f'''
Started the Cheking
━━━━━━━━━━━━━━━━━━
╔Verificando....
╚Card: {ccs}
━━━━━━━━━━━━━━━━━━''')
    bins = message.text.split(' ')
    x = main(ccsa[1])
    func = requests.get(f'https://bins.antipublic.cc/bins/{bins[1]}')

    fin  = time.time()
    return texto_1.edit_text(f"""
KATSUME -DO  | Stripe Auth 00.00 $

╔Card ➳ <code>{ccsa[1]}</code>
╟Status ➳ {x[0]}
╚Response ➳ <code>{x[1]}</code>

╔Bin ➳ <code>{cc[0][:6]}</code>
╟Bank ➳ <code>{func.json()['bank']}</code>
╟Info ➳ <code>{func.json()['brand']}-{func.json()['level']}-{func.json()['type']}</code>
╚Country ➳ <code>[{func.json()['country_flag']}] | {func.json()['country']} | {func.json()['country_name']}</code>

╔Time ➳ <code>{fin-ini:0.4f}</code>
╚Checked By ➳ @{message.from_user.username} <code>[{queryU['rango']}]</code>""")
