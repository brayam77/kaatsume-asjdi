from time import sleep
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('countrys')
def bin(_, m):  
    

    queryU = MongoClient().user_query(m.from_user.id)
    if queryU['rango'] == 'Baneado': return m.reply('usuario baneado no puede usarme.')
    
    if queryU == None: return m.reply('usa el comando para registrarse /register')
    
    if MongoClient().grupo_query(m.chat.id) == None: return m.reply('Chat no autorizado')


    
    
    edit1 =  m.reply_text("<b>☇ Obteniendo Lista de Paises PREMIUM ...</b>")
    sleep(1.5)
    
   
    edit1.edit(f"""
    𝑻𝒊𝒆𝒏𝒆𝒔 𝒂 𝒕𝒖 𝒅𝒊𝒔𝒑𝒐𝒔𝒊𝒄𝒊𝒐𝒏 𝒖𝒏𝒂 𝒆𝒙𝒕𝒆𝒏𝒔𝒂 𝒍𝒊𝒔𝒕𝒂 𝒅𝒆 𝒍𝒐𝒔 𝒔𝒊𝒈𝒖𝒊𝒆𝒏𝒕𝒆𝒔 𝒑𝒂𝒊𝒔𝒆𝒔 𝒒𝒖𝒆 𝒑𝒖𝒆𝒅𝒆𝒔 𝒈𝒆𝒏𝒆𝒓𝒂𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊𝒐𝒏 𝒇𝒂𝒌𝒆:
𝆰 𝆰 𝆰 𝆰 𝆰 𝆰𝆰 𝆰 𝆰 𝆰 𝆰 𝆰
<b>COMANDO ⬌ CODE ⬌ COUNTRY 
<code>/rand AU </code>⬌ AUSTRALIA 
<code>/rand BR </code>⬌ BRASIL
<code>/rand CA </code> ⬌ CANADA
<code>/rand CH </code>⬌ SUIZA 
<code>/rand DE </code>⬌ ALEMANIA (GERMANY)
<code>/rand DK </code>⬌ DINAMARCA 
<code>/rand ES </code>⬌ ESPAÑA (SPAIN)
<code>/rand FI </code>⬌ FINDLANDIA
<code>/rand FR </code>⬌ FRANCIA 
<code>/rand GB </code>⬌ REINO UNIDO 
<code>/rand IE </code>⬌  IRLANDA
<code>/rand IN </code>⬌  INDIA
<code>/rand IR </code>⬌  IRAN
<code>/rand MX </code>⬌ MEXICO 
<code>/rand NL </code>⬌ NETHERLANDS
<code>/rand NO </code>⬌ NORWAY
<code>/rand NZ </code>⬌ HAMILTON
<code>/rand RS </code>⬌ SERVIA
<code>/rand TR </code>⬌ TURQUIA
<code>/rand UA </code>⬌ UKRANIA
<code>/rand US </code>⬌ ESTADOS UNIDOS
𝆰 𝆰 𝆰 𝆰 𝆰 𝆰𝆰 𝆰 𝆰 𝆰 𝆰 𝆰
Genera datos fake con: comando + el pais seleccionado.</b>

<code>/rand US</code>
𝆰 𝆰 𝆰 𝆰 𝆰 𝆰𝆰 𝆰 𝆰 𝆰 𝆰 𝆰 

    """)
    