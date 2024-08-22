import requests,time
from procesos.funciones import addCommand,find_cards,antispam
from procesos.mongo_data import MongoClient
from pages.shayden import shayden

@addCommand('mda')
def panel(_, message):
    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('Chat no autorizado')    
    ini = time.time()
    queryU = MongoClient().user_query(message.from_user.id)
    if queryU == None: return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    if queryU['plan'] == 'Free': return message.reply('usuario Free .|. no puede usarme.')
    if queryU['creditos'] < 2: return message.reply('usuario sin creditos .|. no puede usarme.')
    if antispam(queryU['antispam'],message):return
    
    comando_info = MongoClient().collection_cuatro.find_one({"comando": "/mda"})
    print("Estado del gate 'on' en la base de datos:", comando_info)  
    
    if comando_info is None or comando_info.get('estado') != '✅':
        return message.reply('<b>Command: <code>$mda</code>\nGateway: <code>Mass - Shopify + Ayden</code>\nEstado: <code>OFF❌</code>\nFormat: <code>/mda cc|month|year|cvv.</code></b>')

    ini = time.time()
    if message.reply_to_message:
        cc = find_cards(message.reply_to_message.text)
    else:
        cc = find_cards(message.text)

    if '<b>ingrese la ccs.</b>' in cc:
        return message.reply('<b>Command: <code>$mda</code>\nGateway: <code>Mass - Shopify + Ayden</code>\nEstado: <code>✅</code>\nFormat: <code>/mda cc|month|year|cvv.</code></b>')
        
    data = message.text.split(" ", 2)
    if antispam(0,message):return

    if len(data) < 2: return message.reply("<b>CC Ivalida | $msh cc</b>",quote=True)
    
    ccs = data[1].split('\n')

    if len(ccs) >= 11: return message.reply("<b>solo 10 ccs o menos</b>",quote=True)
    boss =f'''<b>
Started the Cheking
━━━━━━━━━━━━━━━━━━
Verificando....
━━━━━━━━━━━━━━━━━━
</b>'''
    tex = message.reply(boss)
    MongoClient().addcr(message.from_user.id, -2)
    
    boss = '''<b>KATSUME -DO  | Shopify+Ayden 05.00 $
</b>'''

    for cc in ccs:
        card = find_cards(cc)
        cc = cc.split('|')
        if len(card) != 4 : return message.reply(card)
        achk = shayden(cc[0],cc[1], cc[2],cc[3])
        ccs = '{}|{}|{}|{}'.format(cc[0],cc[1], cc[2],cc[3])
        
        boss += f'''<b>
╔Card ➳ <code>{ccs}</code>
╟Status ➳ <code>{achk[1]}</code>
╚Response ➳ <code>{achk[0]}</code></b>'''
        tex.edit_text(boss)


    func = requests.get(f'https://bins.antipublic.cc/bins/{bin[6]}')
    fin = time.time()

    boss += f'''<b>
╔Bin ➳ <code>{cc[0][:6]}</code>
╟Bank ➳ <code>{func.json()['bank']}</code>
╟Info ➳ <code>{func.json()['brand']}-{func.json()['level']}-{func.json()['type']}</code>
╚Country ➳ <code>[{func.json()['country_flag']}] | {func.json()['country']} | {func.json()['country_name']}</code>'''
    tex.edit_text(boss)
        

        
