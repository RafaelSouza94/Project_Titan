import os
from OTXv2 import OTXv2, IndicatorTypes, BadRequest
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
except KeyError:
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

# TODO: add /getinfo/ endpoint to tell the client the available methods

# TODO: refactor
@otx_api.route(BASE_ADDR + 'getinfo/<var>', methods=['POST'])
def get_info(var):
    """
    **OTX get info about an IP or URL, based on <var>**
    
    :return: All information available about an IP address or URL
    
    - Example:
        POST /otx/getinfo/ip
        {"ip":"113.52.135.33"}
        
        POST /otx/getinfo/url
        {"url":"google.com"}
        
    - Expected Success Response:
        HTTP Status Code: 200
        JSON with info.
    """
    vars = {'ip': IndicatorTypes.IPv4, 'url': IndicatorTypes.DOMAIN}
    if not var in vars:
        return {"Error": "Invalid information source. Please access resource at {}".format(vars.keys())}
    if not request.is_json:
        return {"Error": "Request not in JSON format!"}
    else:
        values = request.json
        print("POST data: {}".format(values))
        if var in values:
            try:
                response = otx_call.get_indicator_details_full(
                    vars[var], values[var])
            except BadRequest as err:
                print(err)
                return str(err)
            else:
                return response
        else:
            return {"Error": f"Value {var} needed not found in input!"}        
