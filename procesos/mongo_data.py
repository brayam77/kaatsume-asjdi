import time
import requests
import pymongo
import datetime
import threading

class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://mongo:GjrRVvLqawIqZRwhCNVeFHPSOqwleYYs@viaduct.proxy.rlwy.net:49465")
        self.db = self.client["katsume"]
        self.users = self.db["users"]
        self.grupo = self.db["grupo"]
        self.keys = self.db["keys"]
        self.collection_cuatro = self.db['gates']

    def command_query(self, command_name):
        return self.collection_cuatro.find_one({"comando": command_name})
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

    def user_query(self, user_id):
        collection = self.get_collection('users')
        return collection.find_one({"user_id": user_id})

    def user_query(self, id:int = None):
        return self.users.find_one({"user_id": id})
    
    def grupo_query(self, id:int = None): return self.grupo.find_one({"id": id})

    def grupo_eliminar(self, id:int = None): return self.grupo.delete_one({"id": id})

    def key_query(self, key):
        return self.keys.find_one({"key": key})

    def register_user(self, id:int = None,rango:str = 'User',creditor:int = 0,antispam:int = 60,dias:int = 0,bin_lasted:str = None,fecha_registro = None):
        data  = {'user_id': id,'rango':rango,'plan':'Free','creditos': creditor,'antispam': antispam,'dias': dias,'bin_lasted': bin_lasted,'fecha_registro': fecha_registro, 'since':None}
        self.users.insert_one(data)

    def save_grupos(self, id,dias):
        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dias)
        times = tiempo_futuro.timestamp()
        data  = {'id': id,'dias': times}
        self.grupo.insert_one(data)

    def save_key(self, key,dias):
        data  = {'key': key,'dias': dias}
        self.keys.insert_one(data)

    def addcr(self, id, addcr):
        query = self.users.find_one({"user_id": id})

        self.users.update_one({'user_id': id}, {'$set': {'creditos': query['creditos'] + addcr}})


    def removecr(self, id, addcr):
        query = self.users.find_one({"user_id": id})

        self.users.update_one({'user_id': id}, {'$set': {'creditos': query['creditos'] - addcr}})
    

    def rango(self, id, rango):self.users.update_one({'user_id': id}, {'$set': {'rango': rango}})

    def addpremium(self, id, dia):
        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dia)
        times = tiempo_futuro.timestamp()
        self.users.update_one({'user_id': id}, {'$set': {'plan': 'Premium', 'antispam': 10,'since':times}})

    def delete_key(self, key):
         self.keys.delete_one({'key': key})

    def ban(self, id): self.users.update_one({'user_id': id}, {'$set': {'rango': 'Baneado'}})
    
    def unban(self, id): self.users.update_one({'user_id': id}, {'$set': {'rango': 'Free'}})

    def seller(self, id):
        query = self.users.find_one({"user_id": id})

        if 'Owner' in query['rango']: return True
        elif 'Admin' in query['rango']: return True
        elif 'Co-funder' in query['rango']: return True
        elif 'Humilde' in query['rango']: return True
        elif 'Seller' in query['rango']: return True
        elif 'Dev-Bol' in query['rango']: return True
        else: return False



def expulse_user():
    client = pymongo.MongoClient("mongodb://mongo:GjrRVvLqawIqZRwhCNVeFHPSOqwleYYs@viaduct.proxy.rlwy.net:49465")
    db = client["katsume"]
    collection = db["users"]
    collection1 = db["grupo"]
    

    while True:

        for user in collection1.find({"dias": {"$lt": time.time()}}):
            MongoClient().grupo_eliminar(user['id'])

            url = f'https://api.telegram.org/bot7299905528:AAHQU1bcUBGlFxHvdBBcGqUJ7hl-_eTGTvM/sendMessage'
            params = {'chat_id': user['id'],'text': '<b>Se acabo tu acceso al grupo de usar nuestro bot.❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)

            url = f'https://api.telegram.org/bot7299905528:AAHQU1bcUBGlFxHvdBBcGqUJ7hl-_eTGTvMPPI/sendMessage'
            params = {'chat_id': -1002214914825,'text': f'<b>Se le acabo el acceso de dias al chat con id :( {user["id"]}  )❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)
    

        for user in collection.find({"since": {"$lt": time.time()}}):
            
            collection.update_one({"user_id": user["user_id"]},{"$set": {"plan": "free","antispam": 40,"key": None,"since": None}})
            MongoClient().grupo_eliminar(user['user_id'])
            
            
            url = f'https://api.telegram.org/bot7299905528:AAHQU1bcUBGlFxHvdBBcGqUJ7hl-_eTGTvM/sendMessage'
            params = {'chat_id': user['user_id'],'text': '<b>Se acabo tu plan premium con nuestro bot.❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)

            url = f'https://api.telegram.org/bot7299905528:AAHQU1bcUBGlFxHvdBBcGqUJ7hl-_eTGTvM/sendMessage'
            params = {'chat_id': -1002214914825,'text': f'<b>Se le acabo el plan premium al usuario( {user["user_id"]}  )❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)

        time.sleep(3600)

thread2 = threading.Thread(target=expulse_user)
thread2.start()
