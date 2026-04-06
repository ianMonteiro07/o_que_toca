import requests

API_KEY = "Rw54js0aQkIce16Vgi0Tps-ltATDjKBAxwEH"
BASE_URL = "https://api.setlist.fm/rest/1.0"

def buscar_ultimo_setlist(nome_banda):
    endpoint = f"{BASE_URL}/search/setlists"
    headers = {"x-api-key": API_KEY, "Accept": "application/json"}
    params = {"artistName": nome_banda, "p": 1}

    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            return dados.get("setlist", [])
        return {"erro": "Banda não encontrada."}
    except:
        return {"erro": "Erro de conexão."}