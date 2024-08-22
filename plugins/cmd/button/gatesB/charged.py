from pyrogram import Client, filters
from procesos.plantillas import charged1_text,charged1_button

@Client.on_callback_query(filters.regex("charged"))
def atras(client, message):
    message.edit_message_text(charged1_text,reply_markup=charged1_button)