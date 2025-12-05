"""
Proxy Local para API Pilar Homes
Contorna CORS servindo a API através de um servidor Flask
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens

API_BASE = "https://pilarhomes.com.br/api"

# Lista branca de parâmetros aceitos pelos endpoints da API
ALLOWED_PARAMS = {
    'transactionType', 'page', 'perPage', 'propertyType', 'minPrice', 'maxPrice',
    'minArea', 'maxArea', 'bedrooms', 'suites', 'parkingSpots', 'city', 'region',
    'isExclusive'
}

# Headers necessários para passar pelo WAF
HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://pilarhomes.com.br/',
    'Origin': 'https://pilarhomes.com.br'
}

@app.route('/api/properties', methods=['GET'])
def proxy_properties():
    """Proxy para /api/properties"""
    try:
        # Filtra apenas parâmetros permitidos e normaliza tipos simples
        params = {}
        for key in request.args:
            if key in ALLOWED_PARAMS:
                val = request.args.get(key)
                # Normaliza booleanos comuns
                if key == 'isExclusive':
                    params[key] = str(val).lower() in {'1', 'true', 'yes'}
                # Converte inteiros esperados
                elif key in {'page', 'perPage', 'minPrice', 'maxPrice', 'minArea', 'maxArea', 'bedrooms', 'suites', 'parkingSpots'}:
                    try:
                        params[key] = int(val)
                    except (TypeError, ValueError):
                        continue  # ignora inválidos
                else:
                    # Strings seguras (city, region, propertyType, transactionType)
                    params[key] = val[:100]
        response = requests.get(f"{API_BASE}/properties", params=params, headers=HEADERS)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/properties/clusters', methods=['GET'])
def proxy_clusters():
    """Proxy para /api/properties/clusters"""
    try:
        # Clusters aceitam apenas transactionType
        params = {}
        txn = request.args.get('transactionType')
        if txn:
            params['transactionType'] = txn[:20]
        response = requests.get(f"{API_BASE}/properties/clusters", params=params, headers=HEADERS)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Pilar API Proxy running"})

if __name__ == '__main__':
    print("=" * 50)
    print("🏠 PILAR HOMES API PROXY")
    print("=" * 50)
    print("Endpoints disponíveis:")
    print("  - http://localhost:5000/api/properties")
    print("  - http://localhost:5000/api/properties/clusters")
    print("  - http://localhost:5000/health")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)
