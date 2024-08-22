from pyrogram import Client, filters
from procesos.plantillas import charge2_text,charged2_button

@Client.on_callback_query(filters.regex("next"))
def atras(client, message):
    message.edit_message_text(charge2_text,reply_markup=charged2_button)