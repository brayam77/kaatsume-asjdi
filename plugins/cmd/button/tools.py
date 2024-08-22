from pyrogram import Client, filters
from procesos.plantillas import tools_boton_text,tools_cmds_buton

@Client.on_callback_query(filters.regex("tools"))
def atras(client, message):
    message.edit_message_text(tools_boton_text,reply_markup=tools_cmds_buton)