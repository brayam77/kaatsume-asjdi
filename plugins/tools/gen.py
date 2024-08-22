import time
import re
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from procesos.mongo_data import MongoClient
from pyrogram import Client, filters
from procesos.func_gen import cc_gen
from procesos.funciones import addCommand

@addCommand('gen')
def bin(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU is None:
        return message.reply('Usa el comando para registrarse /register')
    if queryU['rango'] == 'Baneado':
        return message.reply('Usuario baneado no puede usarme.')

    if MongoClient().grupo_query(message.chat.id) is None:
        return message.reply('Chat no autorizado')
    username = message.from_user.username
    user_id = message.from_user.id  # Obtener el ID del usuario
    global input

    if message.reply_to_message:
        input = re.findall(r'[0-9x]+', message.reply_to_message.text)
    else:
        input = re.findall(r'[0-9x]+', message.text)

    if not input:
        message.reply("HERRAMIENTA BGEN DE CCS, USE /gen 4556747")
        return

    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input) == 2:
        cc = input[0]
        mes = input[1][0:2]
        ano = 'x'
        cvv = 'x'
    elif len(input) == 3:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = 'x'
    elif len(input) == 4:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]

    if len(input[0]) < 6:
        return message.reply('<b>Invalid Bin ⚠️</b>', quote=True)

    if mes != 'x':
        mes_int = int(mes)
    else:
        mes_int = None

    if ano != 'x':
        ano_int = int('20' + ano) if len(ano) == 2 else int(ano)
    else:
        ano_int = None

    current_year = int(time.strftime("%Y"))
    current_month = int(time.strftime("%m"))

    if ano_int is not None and ((ano_int < current_year) or (ano_int == current_year and mes_int is not None and mes_int < current_month)):
        return message.reply('<b>Error: Expiration date cannot be in the past. ⚠️</b>', quote=True)

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)

    extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
    if mes == 'x':
        mes_2 = 'rnd'
    else:
        mes_2 = mes
    if ano == 'x':
        ano_2 = 'rnd'
    else:
        ano_2 = ano
    if cvv == 'x':
        cvv_2 = 'rnd'
    else:
        cvv_2 = cvv

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='RE-GEN', callback_data=f"regen|{cc}|{mes}|{ano}|{cvv}|{user_id}")]
        ]
    )

    bins = message.text.split('gen ')
    func = requests.get(f'https://bins.antipublic.cc/bins/{bins[1]}')

    message.reply(f"""
🌧 𝐆𝐄𝐍 𝐂𝐂 🌧

<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
╔Bin ➳ <code>{func.json()['bin']}</code>
╟Info ➳ <code>{func.json()['brand']}</code> - <code>{func.json()['type']}</code> - <code>{func.json()['level']}</code>
╟Country ➳ <code>{func.json()['country_flag']} | {func.json()['country']} | {func.json()['country_name']}</code>
╚Bank ➳ <code>{func.json()['bank']}</code>""", reply_markup=buttons)

@Client.on_callback_query(filters.regex(r"^regen\|"))
def on_regen(client, callback_query: CallbackQuery):
    data = callback_query.data.split("|")
    cc = data[1]
    mes = data[2]
    ano = data[3]
    cvv = data[4]
    original_user_id = int(data[5])  # ID del usuario que generó el mensaje

    # Verificar si el usuario que presionó el botón es el mismo que generó el mensaje
    if callback_query.from_user.id != original_user_id:
        callback_query.answer("Usa tu propio menú para generar CCs.", show_alert=True)
        return

    if mes != 'x':
        mes_int = int(mes)
    else:
        mes_int = None

    if ano != 'x':
        ano_int = int('20' + ano) if len(ano) == 2 else int(ano)
    else:
        ano_int = None

    current_year = int(time.strftime("%Y"))
    current_month = int(time.strftime("%m"))

    if ano_int is not None and ((ano_int < current_year) or (ano_int == current_year and mes_int is not None and mes_int < current_month)):
        callback_query.answer('<b>Error: Expiration date cannot be in the past. ⚠️</b>', show_alert=True)
        return

    # Obtener la información adicional
    func = requests.get(f'https://bins.antipublic.cc/bins/{cc}')
    bin_info = func.json()

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)

    full_text = f"""
🌧 𝐆𝐄𝐍 𝐂𝐂 🌧

<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
╔Bin ➳ <code>{func.json()['bin']}</code>
╟Info ➳ <code>{func.json()['brand']}</code> - <code>{func.json()['type']}</code> - <code>{func.json()['level']}</code>
╟Country ➳ <code>{func.json()['country_flag']} | {func.json()['country']} | {func.json()['country_name']}</code>
╚Bank ➳ <code>{func.json()['bank']}</code>"""

    callback_query.message.edit_text(full_text, reply_markup=callback_query.message.reply_markup)
