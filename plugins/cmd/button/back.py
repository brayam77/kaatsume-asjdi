from pyrogram import Client, filters
from procesos.plantillas import cmmds_text,back_cmds_buton

@Client.on_callback_query(filters.regex("back"))
def atras(client, message):
    message.edit_message_text(cmmds_text.format(message.from_user.username,message.from_user.id),reply_markup=back_cmds_buton)