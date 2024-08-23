from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

start_cmand = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("👑 OWNER ", url="https://t.me/pandithaLee"),
                                    InlineKeyboardButton("💬 CHAT", url="https://t.me/KatzumeDochat")],
                                    ])


cmds_cmand = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("GATEWAYS", callback_data="gates"),
                                    InlineKeyboardButton("TOOLS", callback_data="tools"),],[
                                    InlineKeyboardButton("PERFIL", callback_data="perfil")],])



gatewys_cmds_buton = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("AUTH", callback_data="auth"),
                                    InlineKeyboardButton("CHARGED", callback_data="charged"),
                                    InlineKeyboardButton("CCN", callback_data="ccn")],[
                                    InlineKeyboardButton("MASS", callback_data="mass"),
                                    InlineKeyboardButton("FREE", callback_data="free"),
                                    InlineKeyboardButton("BACK", callback_data="back")]])

tools_cmds_buton = keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="back")]])

back_cmds_buton = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("GATEWAYS", callback_data="gates"),
                                    InlineKeyboardButton("TOOLS", callback_data="tools"),],[
                                    InlineKeyboardButton("PERFIL", callback_data="perfil")],])



charged1_button = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="gates")]])


charged2_button =  InlineKeyboardMarkup([[
                                        InlineKeyboardButton("BACK", callback_data="auth")]])

#charged3_button =  InlineKeyboardMarkup([[InlineKeyboardButton("⇷⇷⇷", callback_data="next"),
                                          #InlineKeyboardButton("BACK", callback_data="gates"),],])

mas_button =  InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="gates")]])

auth_button =  InlineKeyboardMarkup([[InlineKeyboardButton("NEX", callback_data="next"),
                                    InlineKeyboardButton("BACK", callback_data="gates")]])

auth2_button =  InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="auth")]])



start_text = """
Bienvenido a KATSUME -DO CHK BOT, espero 
te guste y disfrutes el bot.

Usuario: @{}
Id: <code>{}</code>**

𝐄𝐍𝐕𝐈𝐀 /cmds 𝐏𝐀𝐑𝐀 𝐕𝐄𝐑 𝐋𝐎𝐒 𝐂𝐎𝐌𝐀𝐍𝐃𝐎𝐒 𝐃𝐈𝐒𝐏𝐎𝐍𝐈𝐁𝐋𝐄𝐒 

VERSION 1.0!
"""

cmmds_text = """
Saludos binero @{} {}, te presento mis Gateways y Tools disponibles en KATSUME -DO Chk.
"""


gates_boton_text = '''KATSUME -DO  | 𝑮𝑨𝑻𝑬𝑺

カ Gates Online ➩ 14
カ Gates Offline 1

カ Gates Totals ➬ 15

カ Gates Auth ➭ 7
カ Gates Free ➭ 1
カ Gates Charged ➭ 3
カ Gates CCN Charged ➭ 2
カ Gates Mass ➭ 2'''

tools_boton_text = '''
HERRAMIENTAS | カツメ CHK 

カ BIN | /bin
カ EJEMPLO: /bin 474849

カ GEN | /gen
カ EJEMPLO: /gen 474849

カ EXTRA | /extra
カ EJEMPLO: /extra 474849

カ INFO SHOPIFY | /if
カ EJEMPLO: /if + Dominame
カ EJEMPLO: /if https://digitronaust.com.au/                      
'''

perfil_boton_text = '''
TU USERNAME: {}
TU  USERID: {}    '''

charged1_text = '''
CHARGED | カツメ CHK      

カ Command : /da
カ Pasarela : Shopify + Ayden
カ Charged : 05.00$
カ Status : ON ✅

カ Command : /sc
カ Pasarela : Shopify + Cybersource
カ Charged : 07.00$
カ Status : ON ✅

カ Command : /pp
カ Pasarela : Paypal
カ Charged : 01.00$
カ Status : ON ✅'''

charge2_text = '''
AUTH PAG. 2| カツメ CHK      

カ Command : /bm
カ Pasarela : Braintree Moneris Auth
カ Charged : 00.00$
カ Status : ON ✅

カ Command : /pay
カ Pasarela : Payflow Auth
カ Charged : 00.00$
カ Status : ON ✅'''
#charged3_text = ''''''


mass_text = '''
MASS CHEKING | カツメ CHK      

カ Command : /mda
カ Pasarela : Mass - Shopify + Ayden
カ Charged : 05.00$
カ Status : ON ✅

カ Command : /mb3
カ Pasarela : Mass - Braintree Auth
カ Charged : 00.00$
カ Status : ON ✅
'''

auth_text = '''
AUTH | カツメ CHK      

カ Command : /btw
カ Pasarela : Braintree Auth AVS 
カ Charged : 00.00$
カ Status : ON ✅

カ Command : /stp
カ Pasarela : Stripe Auth
カ Charged : 00.00$
カ Status : ON ✅

カ Command : /ze
カ Pasarela : Braintree auth
カ Charged : 00.00$
カ Status : ON ✅

カ Command : /clo
カ Pasarela : Braintree auth CCN
カ Charged : 00.00$
カ Status : ON ✅

カ Command : /bvs
カ Pasarela : Braintree auth AVS
カ Charged : 00.00$
カ Status : ON ✅
'''


free_text = '''
FREE | カツメ CHK      

カ Command : /vbv
カ Pasarela : 3D Braintree
カ Charged : 00.00$
カ Status : ON ✅                 
'''

ccn_text = '''
CCN | カツメ CHK      

カ Command : /po
カ Pasarela : Shopify + Braintree
カ Charged : 07.00$
カ Status : OFF ❌

カ Command : /ccn
カ Pasarela : Braintree CCN
カ Charged : 05.00$
カ Status : ON ✅'''
