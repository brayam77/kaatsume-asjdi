from procesos.funciones import addCommand,Client
from procesos.mongo_data import MongoClient
import datetime


@addCommand('register')
async def start(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    if queryU == None:
        MongoClient().register_user(message.from_user.id,'User',0,60,0,None,datetime.datetime.now().timestamp())

        await message.reply('TE ACABAS DE REGISTRAR EN KATSUMe DO CHK') 

        texy = f"""
NUEVO USUARIO REGISTRADO EN Katsume
NAME: {message.from_user.first_name}
USER: @{message.from_user.username}
ID: {message.from_user.id}"""

        await Client.send_message(_,chat_id=-1002214914825,text=texy)
    else:
        await message.reply('Ya te encuentras registrado')


