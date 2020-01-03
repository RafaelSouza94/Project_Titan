from flakon import JsonBlueprint
"""Basic API module

 .. moduleauthor:: Rafael Souza <https://github.com/RafaelSouza94>
"""


api = JsonBlueprint('home', __name__)


@api.route('/api', methods=['GET', 'POST'])
def api_main():
    """
    **Main API view**

    :return: For now, just a Status: Working JSON

    - Example:
        Nothing really, just testing still

    - Expected Success Response:
        HTTP Status Code: 200
        {'Status': 'Working'}

    """
    return {'Status': 'Working'}


@api.route('/otx', methods=['GET', 'POST'])
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


@api.route('/tretas', methods=['GET'])
def tretas():
    """
    **Tretas API easter egg**

    :return: Tretas: Pesadas JSON.

    - Example:
        GET /tretas

    - Expected Success Response:
        HTTP Status Code: 200
        {'Tretas':'Pesadas'}
    """
    return {'Tretas': 'Pesadas'}
