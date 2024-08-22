from pyrogram import Client, filters
import random,re,time

def addCommand(command):    
    cmm = Client.on_message(filters.command(command,prefixes=['.','/',',','¡','-','_','|','"',"'",'#','$','%','&','(',')','*','+','[',']',';','<','>','?','=','¿',':']))
    return cmm



def generate_key():
    key = f"Katsume-{random.randint(10000000, 99999999)}-PREMIUM"
    return key

def find_cards(text):
    try:
        card_info = re.search(r'(\d{15,16})+?[^0-9]+?(\d{1,2})[\D]*?(\d{2,4})[^0-9]+?(\d{3,4})', text)
        cc, mes, ano, cvv = card_info.groups()
        cc = cc.replace("-", "").replace(" ", "")
        return cc,mes,ano,cvv
    except: return '<b>ingrese la ccs.</b>'

last_request_time = {}
def antispam(tiempo , message):
    user_id = message.from_user.id
    current_time = time.time()
    
    if user_id in last_request_time and current_time - last_request_time[user_id] < tiempo:
        wait = int(tiempo - (current_time - last_request_time[user_id]))
        message.reply(f"<b>Espera: <code>{wait} segundos , antispam</code></b>")
        return True  
    
    last_request_time[user_id] = current_time
    return False 