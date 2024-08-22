from procesos.funciones import addCommand
from procesos.mongo_data import MongoClient
import datetime

@addCommand(['my','me','info','yo'])
def bin(_, message):
    # Obtener el ID y nombre de usuario del mensaje original
    target_user_id = message.from_user.id
    target_username = message.from_user.username
    
    # Verificar si el mensaje es una respuesta a otro mensaje
    if message.reply_to_message:
        target_user_id = message.reply_to_message.from_user.id
        target_username = message.reply_to_message.from_user.username
    # Verificar si se proporcionó un ID de usuario como argumento
    elif message.text.strip().split()[1:]:
        target_user_id = int(message.text.strip().split()[1])
        # Obtener el nombre de usuario a partir del ID de usuario
        user_info = _.get_chat(target_user_id)
        target_username = user_info.username

    queryU = MongoClient().user_query(target_user_id)
    if queryU is None: 
        return message.reply('usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado': 
        return message.reply('usuario baneado no puede usarme.')

    tiempo = datetime.datetime.fromtimestamp(queryU['fecha_registro'])
    data = f'<code>{tiempo.day}/{tiempo.month}/{tiempo.year}</code>'

    if queryU['since'] is None:
        since = 'Sin plan'
    else:
        tiempo = datetime.datetime.fromtimestamp(queryU['since'])
        fecha_actual = datetime.datetime.now()
        fecha_futura = datetime.datetime(tiempo.year, tiempo.month, tiempo.day)
        diferencia = fecha_futura - fecha_actual
        since = f'{diferencia.days} Faltantes'

    message.reply(f"""<b>
𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: @{target_username}
𝙄𝘿:<code>{target_user_id}</code>
𝘼𝙣𝙩𝙞𝙎𝙥𝙖𝙢:<code>{queryU['antispam']}</code>
𝙍𝙖𝙣𝙜𝙚:<code>{queryU['rango']}</code>
𝙋𝙡𝙖𝙣:<code>{queryU['plan']}</code>
𝘾𝙧𝙚𝙙𝙞𝙩𝙨:<code>{queryU['creditos']}</code>
𝘿𝙖𝙮𝙨:<code>{since}</code>
𝙍𝙚𝙜𝙞𝙨𝙩𝙚𝙧𝙚𝙙:<code>{data}</code></b>""")
