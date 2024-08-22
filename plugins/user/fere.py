from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import PeerIdInvalid

staff_group_id = -1002214914825
approved_channel_id = -1002183452891  # ID del canal donde se enviará la referencia aprobada

approval_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='✅ Aprobar', callback_data='approve'),
            InlineKeyboardButton(text='❌ Denegar', callback_data='deny')
        ]
    ]
)

final_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='🌩️ Comprar Chk 🌩️', url='https://t.me/pandithaLee'),
            InlineKeyboardButton(text='🌧️ Chat Free 🌧️', url='https://t.me/+fL4BPwJ1RCtiZDQx')
        ]
    ]
)

from procesos.funciones import addCommand, Client
from procesos.mongo_data import MongoClient

@addCommand(["referencia", "refe"])
def bin(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU is None:
        return message.reply('Usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado':
        return message.reply('Usuario baneado no puede usarme.')
    
    if MongoClient().grupo_query(message.chat.id) is None:
        return message.reply('Chat no autorizado')
    
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo.file_id
        mensaje = message.reply_to_message.caption

        Client.send_photo(
            _,
            chat_id=staff_group_id,
            photo=photo,
            caption=f"""
KATSUME -DO  | REFERENCIAS

カUser Name ➢ @{message.from_user.username}

カMensaje ➢ {mensaje}""",
            reply_markup=approval_buttons
        )
        message.reply("Su referencia ya fue enviada para su revisión.")
    else:
        message.reply(f"<b>KATSUME -DO  SISTEMA DE REFERENCIA</b>\n<code>Hola @{message.from_user.username}</code><code>, Para enviar su referencia correctamente, suba la imagen sin texto. Después responde a su imagen y escribe /refe más un texto.</code>")

from pyrogram.errors import PeerIdInvalid

@Client.on_callback_query(filters.regex(r"^(approve|deny)$"))
async def callback_handler(client: Client, callback_query: CallbackQuery):
    action = callback_query.data
    if action == "approve":
        # Reenviar el mensaje al canal de referencias aprobadas con los botones finales
        if callback_query.message.photo:
            try:
                await client.send_photo(
                    chat_id=approved_channel_id,
                    photo=callback_query.message.photo.file_id,
                    caption=callback_query.message.caption,
                    reply_markup=final_buttons  # Añadir los botones finales al mensaje aprobado
                )
            except PeerIdInvalid:
                await callback_query.answer("Error: El ID del canal es inválido o el bot no tiene acceso.", show_alert=True)
                return
        await callback_query.answer("Referencia aprobada y enviada al canal.")
    elif action == "deny":
        await callback_query.answer("Referencia denegada.", show_alert=True)
    
    # Eliminar los botones de aprobación después de que se haya tomado una acción
    await callback_query.message.edit_reply_markup(reply_markup=None)
