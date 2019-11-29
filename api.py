"""
Basic API module

.. moduleauthor:: Rafael Souza <https://github.com/RafaelSouza94>

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
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
    return jsonify({'Status': 'Working'})

@app.route('/tretas', methods=['GET'])
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
    return jsonify({'Tretas': 'Pesadas'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')