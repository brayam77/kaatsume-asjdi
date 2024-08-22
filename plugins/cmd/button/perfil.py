from pyrogram import Client, filters
from procesos.plantillas import perfil_boton_text,tools_cmds_buton

@Client.on_callback_query(filters.regex("perfil"))
def atras(client, message):
    message.edit_message_text(perfil_boton_text.format(message.from_user.username,message.from_user.id),reply_markup=tools_cmds_buton)