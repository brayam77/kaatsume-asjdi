from pyrogram import Client, filters
from procesos.plantillas import gatewys_cmds_buton,gates_boton_text

@Client.on_callback_query(filters.regex("gates"))
def atras(client, message):
    message.edit_message_text(gates_boton_text,reply_markup=gatewys_cmds_buton)