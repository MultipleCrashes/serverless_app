import sys
from urllib.request import urlopen
from pprint import pprint 
import json 

# serverless


def main(dict):
    request_url = """https://pguat.paytm.com/oltp/HANDLER_INTERNAL/getTxnStatus?JsonData={%22MID%22:%22klbGlV59135347348753%22,%22ORDERID%22:%22ORDER48886809916%22,%22CHECKSUMHASH%22:%22wctrePBbNfJkGyNXRg8sHBTJZWGJEFMBuUtO3qoFkL2ox8HIe9YSzTU%2FpswpDbtAhS%2bkWiHgr5nmu9z9cn8rbzGsV0qy8D16c2negimoD%2Fs%3D%22}"""
    resp = urlopen(request_url)
    resp_body = resp.read()
    json_response = json.loads(resp_body.decode('utf-8'))
    print("type resp body",type(json_response))
    return json_response
