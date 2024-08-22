import time
import random
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from procesos.funciones import addCommand
from procesos.func_gen import cc_gen
from procesos.mongo_data import MongoClient

import requests
from urllib.parse import urlparse#pip install urllib3
from pyrogram import Client
from pyrogram import filters


@addCommand('if')
def bin(_, message):
    queryU = MongoClient().user_query(message.from_user.id)

    if queryU == None: return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    
    
    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('Chat no autorizado')


    site = message.text[len("/if "):]

    if not site: return Client.send_message(_,chat_id=message.chat.id,text=f"『KATSUME DO CHK\n ❌Error-Message❌\n Mensaje: No has introducido ningun dominio.",reply_to_message_id=message.id)
    username = getattr(message.from_user, 'username', None)
    
    if "://" in site:
        parsed_url = urlparse(site)
        domain = parsed_url.netloc
        
    else:
        domain = site
    
    try:
        resp = requests.get(f"https://{domain}/products.json")
        
        if "shopify" in resp.text: result = resp.json()['products']
        else: return Client.send_message(_,chat_id=message.chat.id,text=f"KATSUME DO CHK\n❌Error-Message❌\n MSG: Revisamos el dominio '{domain}' y al parecer no es shopify.\nSi crees que es un error, contacta a un [Onwer, Seller, ADM]",reply_to_message_id=message.id)
        
            
    except: return Client.send_message(_,chat_id=message.chat.id,text=f"Error GET site, put data: {site}\nOnly Domanin or view data url",reply_to_message_id=message.id)

    

    min_price = float('inf')
    product_id = None
    title = None

    for item in result:
        
        variants = item.get('variants', [])
        for variant in variants:
            if variant.get('available') == True:
                price = float(variant.get('price'))
                if price < min_price:
                    min_price = price
                    title = item.get('title')
                    product_id = variant.get('id')
                    link = item.get('handle')
                    

    if product_id is not None:
        tex =f"""
🌧 INFO SHOPIFY  🌧
      
——————✅True Finish✅——————
カ Url ➳ <code>{domain}</code>
カ Price ➳ <code>{min_price}</code>
カ Title ➳ <code>{title}</code>
カ Product_id ➳ </code>{product_id}</code>
カ Link product ➳ <code>https://{domain}/products/{link}<code>
—————————————————————————
カ User ➳ @{username}"""
        
        return Client.send_message(_,chat_id=message.chat.id,text=tex,reply_to_message_id=message.id,disable_web_page_preview=True)
        
    else:
        return Client.send_message(_,chat_id=message.chat.id,text=f"KATSUME DO CHK\n❌Error❌\nNo se pudo obtener productos para:\nSite: {domain}",reply_to_message_id=message.id)
       
