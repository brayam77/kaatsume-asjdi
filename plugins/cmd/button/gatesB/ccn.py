from pyrogram import Client, filters
from procesos.plantillas import ccn_text,mas_button

@Client.on_callback_query(filters.regex("ccn"))
def atras(client, message):
    message.edit_message_text(ccn_text,reply_markup=mas_button)