from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient
import datetime

@addCommand(['idch','idc','id','idchat'])
def bin(_, m):
    cc = f'id:<code>{m.from_user.id}</code>\nchat:<code>{m.chat.id}</code>'
    m.reply(cc)