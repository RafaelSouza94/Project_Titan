from flakon import JsonBlueprint
"""OTX API communication module

 .. moduleauthor:: Rafael Souza <https://github.com/RafaelSouza94>
"""

otx_api = JsonBlueprint('OTX', __name__)


@otx_api.route('/otx', methods=['GET', 'POST'])
def otx():
    """
    **OTX Basic**
    
    :return: For now, just a Status: Working JSON
    
    - Example:
        Nothing yet
        
    - Expected Success Response:
        HTTP Status Code: 200
        {'Status': 'Working'}
    """

    return {'Status': 'Working'}
