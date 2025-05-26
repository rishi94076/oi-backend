from flask import Flask, request, jsonify
import requests
from oi_fetcher import fetch_oi_data

app = Flask(__name__)

@app.route('/api/oi', methods=['GET'])
def get_oi_data():
    symbol = request.args.get('symbol', 'NIFTY')
    try:
        data = fetch_oi_data(symbol.upper())
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
