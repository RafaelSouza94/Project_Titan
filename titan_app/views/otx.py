import os
from flakon import JsonBlueprint
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


@otx_api.route(BASE_ADDR + 'getpulses')
def get_pulses():
    """
    **Get all OTX pulses for current API key**
    
    :return: All info about all pulses
    
    - Example:
        GET /otx/getpulses
        
    - Expected Success Response:
        HTTP Status Code: 200
        {'pulse1':'info', 'pulse2':'info'}
    """
    pulses = otx_call.getall(limit=20)
    return pulses


