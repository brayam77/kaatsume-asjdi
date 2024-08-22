
from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient


@addCommand('panel')
def panel(_, message):    

    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU == None: return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': return message.reply('usuario baneado no puede usarme.')
    

    queryS = MongoClient().seller(message.from_user.id)

    if queryS == False: return message.reply('Comando para admins')
    
    texto = """PANEL DE SELLERS

✦|Generar key /key + Dias
✦|Añadir creditos a usuarios /addcr + id del usuario + monto
✦|Volver un grupo premuim /addgp + id del grupo + dias
✦|Añadir Seller /rango + id + seller 
✦|Banear un usuario /ban + id del usuario
✦lBuscar informacion de un usuario /my + id del usuario
"""
    message.reply(texto)
