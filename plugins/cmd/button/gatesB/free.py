from pyrogram import Client, filters
from procesos.plantillas import free_text,mas_button

@Client.on_callback_query(filters.regex("free"))
def atras(client, message):
    message.edit_message_text(free_text,reply_markup=mas_button)