from procesos.funciones import addCommand, Client
from procesos.plantillas import start_cmand, start_text

@addCommand('start')
async def start(_, message):
    await Client.send_photo(
        _,
        chat_id=message.chat.id,
        caption=start_text.format(message.from_user.username, message.from_user.id),
        reply_markup=start_cmand, 
        reply_to_message_id=message.id,
        photo='https://i.ibb.co/QXHJ23c/LOGO-KATSUME-DO.png'  # Replace with the direct image link
    )
