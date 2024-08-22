from pyrogram import Client, filters
from procesos.plantillas import auth_text,auth_button

@Client.on_callback_query(filters.regex("auth"))
def atras(client, message):
    message.edit_message_text(auth_text,reply_markup=auth_button)