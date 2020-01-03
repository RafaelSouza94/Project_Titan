import os
from OTXv2 import OTXv2, IndicatorTypes
from flakon import JsonBlueprint
from flask import request
"""OTX API communication module

 .. moduleauthor:: Rafael Souza <https://github.com/RafaelSouza94>
"""

OTX_KEY_NAME = 'OTX_KEY'
BASE_ADDR = '/otx/'
otx_api = JsonBlueprint('OTX', __name__)

try:
    OTX_KEY = os.environ[OTX_KEY_NAME]
except KeyError as err:
    print("Error: {} not found in environment variables!".
          format(OTX_KEY_NAME))
else:
    otx_call = OTXv2(OTX_KEY)
    
@otx_api.route(BASE_ADDR, methods=['GET', 'POST'])
def otx():
    """
    **OTX Basic**
    
    :return: Current status of the API
    
    - Example:
        GET /otx
        
    - Expected Success Response:
        HTTP Status Code: 200
        {'Status': 'Working'}
    """

    return {'Status': 'Working'}


@otx_api.route(BASE_ADDR + 'getinfoip', methods=['POST'])
def get_info_ip():
    """
    **OTX get info about an IP**
    
    :return: All information available about an IP address
    
    - Example:
        POST /otx/getinfoip
        {"ip":"113.52.135.33"}
        
    - Expected Success Response:
        HTTP Status Code: 200
        JSON with info about IP.
    """
    if request.is_json:
        ip = request.json
        print("IP: {}".format(ip))
        return otx_call.get_indicator_details_full(
            IndicatorTypes.IPv4, ip['ip'])
    else:
        return {"Error":"Request not in JSON format!"}








