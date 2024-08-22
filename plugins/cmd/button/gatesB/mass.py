from pyrogram import Client, filters
from procesos.plantillas import mass_text,mas_button

@Client.on_callback_query(filters.regex("mass"))
def atras(client, message):
    message.edit_message_text(mass_text,reply_markup=mas_button)