import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
from utils import *

api_base = 'https://api.gdax.com'


def products():
    response = requests.get(api_base + '/products')
    # check for invalid api response
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

#print(products())

class GDAXRequestAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        
    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())
        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request
    
auth = GDAXRequestAuth('44b43db5475bd10d553273fbb9cafe8f', 'nYU1W7uYEpOThf80ouWabRNjG2vzyIaJBjX5v4CDGc9pU9WePZHVsm+6rsEZhxZyTci9w9wyiPtgb6XmEscC6g==', '7x28p9fh7cl')

r = requests.get(api_base + '/accounts', auth=auth)
jsonDump(r)
print(" ")
acct_ids = []

for i in r.json():
    acct_ids.append(i['id'])



