from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def test():
    return jsonify({'Status': 'Working'})

@app.route('/tretas', methods=['GET'])
def tretas():
    return jsonify({'Tretas': 'Pesadas'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')