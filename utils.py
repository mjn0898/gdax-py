import json

def jsonDump(response):
    print(json.dumps(response.json(), sort_keys=True, indent=4))
    
