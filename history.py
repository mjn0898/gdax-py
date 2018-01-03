import requests, json
from acct_info import auth, api_base, acct_ids
from utils import *

#acct_ids = ['3217c255-53fd-4282-bf8a-e837bd7ed1d8','49a1841c-117d-41a1-a98b-7312121fafba','dda3a3a7-acac-49ff-b79e-e805a86dc76c','a9cf1403-d42d-4ba0-a7f5-d123cf25fa3f','b10dc01a-819b-4c35-ba45-a70869204460']

# get LTC acct history
r = requests.get(api_base + '/accounts/' +  acct_ids[0] + '/ledger', auth=auth)
jsonDump(r)
print('')
# get ETH acct history
r = requests.get(api_base + '/accounts/' +  acct_ids[1] + '/ledger', auth=auth)
jsonDump(r)
print('')
# get BTC acct history
r = requests.get(api_base + '/accounts/' +  acct_ids[2] + '/ledger', auth=auth)
jsonDump(r)
print('')
# get USD acct history
r = requests.get(api_base + '/accounts/' +  acct_ids[3] + '/ledger', auth=auth)
jsonDump(r)
print('')
# get BCH acct history
r = requests.get(api_base + '/accounts/' +  acct_ids[4] + '/ledger', auth=auth)
jsonDump(r)



