from procesos.funciones import addCommand, Client
from procesos.mongo_data import MongoClient

# Función para enviar el mensaje a todos los usuarios
async def enviar_mensaje_a_todos(client, mensaje_id, chat_id):
    # Conectar a la base de datos de MongoDB
    db = MongoClient()
    collection = db.get_collection('users')
    
    # Obtener todos los IDs de usuarios
    resultados = collection.find({}, {"user_id": 1})
    
    for resultado in resultados:
        user_id = resultado['user_id']
        try:
            # Reenvía el mensaje al usuario
            await client.forward_messages(user_id, chat_id, mensaje_id)
        except Exception as e:
            error_msg = f"Error al reenviar mensaje a {user_id}: {str(e)}"
            print(error_msg)

# Comando para reenviar el último mensaje a todos los usuarios
@addCommand('reenviar')
async def reenviar_mensaje_privado(_, message):
    # Conectar a la base de datos de MongoDB
    db = MongoClient()
    collection = db.get_collection('users')

    # Verificar si el usuario tiene el rango de "Owner"
    user_id = message.from_user.id
    result = collection.find_one({"user_id": user_id}, {"rango": 1})
    
    if result is None or result.get('rango', '') not in ['Owner', 'Dev-Bol']:
        await message.reply(f"<b>No tienes permiso para usar este comando. ❌</b>")
        return

    # Verifica si el mensaje es una respuesta a otro mensaje
    if message.reply_to_message:
        mensaje_id = message.reply_to_message.id
        chat_id = message.reply_to_message.chat.id
        
        # Reenviar el mensaje a todos los usuarios
        await enviar_mensaje_a_todos(_, mensaje_id, chat_id)

        # Mensaje de confirmación
        mensaje_confirmacion = "El mensaje se está reenviando a todos los usuarios."
        await message.reply(mensaje_confirmacion)
    else:
        await message.reply("<b>Debes responder a un mensaje para reenviarlo. ❌</b>")
