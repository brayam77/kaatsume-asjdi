import requests
from time import sleep
from procesos.funciones import addCommand

from procesos.mongo_data import MongoClient

@addCommand('rand')
def bin(_, m):    

    queryU = MongoClient().user_query(m.from_user.id)
    
    if queryU == None: return m.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return m.reply('usuario baneado no puede usarme.')
    
    
    if MongoClient().grupo_query(m.chat.id) == None: return m.reply('Chat no autorizado')
    
    infake = m.text[len("/rand"):]

    print(infake)
    
    if not infake: return m.reply("Por favor, proporciona una lista de países válidos con el comando /countrys")

    edit1 =  m.reply_text("<b>☯ Generando Datos Fake Premium...</b>")
     
    spli = infake.split()
    infake = spli[0]

    infake_api = requests.get(f'https://randomuser.me/api/?nat={infake}').json()

    name = infake_api["results"][0]["name"]
    gender = infake_api["results"][0]["gender"]
    age = infake_api["results"][0]["dob"]["age"]
    birthdate = infake_api["results"][0]["dob"]["date"]
    street = infake_api["results"][0]["location"]["street"]['number']
    street1 = infake_api["results"][0]["location"]["street"]['name']
        
    city = infake_api["results"][0]["location"]["city"]
    state = infake_api["results"][0]["location"]["state"]
    postal = infake_api["results"][0]["location"]["postcode"]
    email = infake_api["results"][0]["email"]
    country =infake_api["results"][0]["location"]["country"]


    edit1.edit(f"""
    
𝐃𝐀𝐓𝐎𝐒 𝐅𝐀𝐊𝐄 𝐏𝐑𝐄𝐌𝐈𝐔𝐌
𝆰 𝆰 𝆰 𝆰 𝆰 𝆰𝆰 𝆰 𝆰 𝆰 𝆰 𝆰<b>
⟿ Name : <code>{name["first"]} {name["last"]}</code>
⟿ Gender :<code> {gender}</code>
⟿ Age :<code> {age}</code>
⟿ Birthdate :<code> {birthdate}</code>
⟿ Country :<code> {country}</code>
⟿ Street :<code> {street}- {street1}</code>
⟿ City :<code> {city}</code>
⟿ State : <code>{state}</code>
⟿ Postal Code :<code> {postal}</code>
⟿ Email :<code> {email}</code></b>
 𝆰 𝆰 𝆰 𝆰 𝆰 𝆰𝆰 𝆰 𝆰 𝆰 𝆰 𝆰
⎚ 𝙘𝙝𝙚𝙘𝙠 @{m.from_user.username}

    """)
    
